# Dataset Loader for loading PDF, CSV, and XLSX files from Kaggle datasets.
# RAG is used for extracting texts from the PDF files.

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_classic.storage import LocalFileStore


# ── Datasets ──────────────────────────────────────────────────────────────────

DATASETS = {
    "postpartum_pdf":      "/kaggle/input/datasets/akritiupadhyayks/comprehensive-postpartum-dataset/comprehensive_postpartum_dataset_v2.pdf",
    "maternal_sleep":      "/kaggle/input/datasets/thedevastator/impact-of-maternal-mental-health-on-infant-sleep/Dataset_maternal_mental_health_infant_sleep.csv",
    "maternal_sleep_2":    "/kaggle/input/datasets/thedevastator/maternal-mental-health-and-infant-sleep/Dataset_maternal_mental_health_infant_sleep.csv",
    "birth_weight":        "/kaggle/input/datasets/ziya07/maternal-health-features-dataset/birth_weight_dataset.csv",
    "maternal_risk":       "/kaggle/input/datasets/drmbsharma/maternal-health-risk-data-set/Maternal_Risk.csv",
    "maternal_risk_2":     "/kaggle/input/datasets/mohamedmansourabbas/maternal-risk-prediction/Maternal Health Risk Data Set (project 7).csv",
    "postpartum_depression": "/kaggle/input/datasets/parvezalmuqtadir2348/postpartum-depression/post natal data.csv",
    "gdm_csv":             "/kaggle/input/datasets/prashanthana/early-prediction-of-gdm/gdm_synthetic_data.csv",
    "gdm_xlsx":            "/kaggle/input/datasets/prashanthana/early-prediction-of-gdm/GDM_Variable_Descriptions.xlsx",
}


# ── PDF RAG Pipeline ──────────────────────────────────────────────────────────

class PDFRAGPipeline:
    def __init__(self, pdf_path: str):
        self.pdf_path    = pdf_path
        self.vectorstore = None
        self.retriever   = None
        self._build()

    def _load_pdf(self):
        return PyPDFLoader(self.pdf_path).load()

    def _split(self, docs):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
        )
        return splitter.split_documents(docs)

    def _embeddings(self):
        underlying_embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        store = LocalFileStore("/kaggle/working/cache/")
        return CacheBackedEmbeddings.from_bytes_store(
            underlying_embeddings,
            store,
            namespace="all-MiniLM-L6-v2",
        )

    def _build(self):
        docs   = self._load_pdf()
        chunks = self._split(docs)
        self.vectorstore = FAISS.from_documents(chunks, self._embeddings())
        self.retriever   = self.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 5},
        )

    def retrieve_context(self, question: str) -> str:
        docs = self.retriever.invoke(question)
        return "\n\n".join(d.page_content for d in docs)


# ── Structured Data Loader ────────────────────────────────────────────────────

class StructuredDataLoader:
    def __init__(self, datasets: Dict[str, str]):
        self.datasets = datasets
        self.frames: Dict[str, pd.DataFrame] = {}

    def load(self):
        for name, path in self.datasets.items():
            p = Path(path).expanduser()
            if not p.exists():
                continue
            try:
                if p.suffix == ".csv":
                    self.frames[name] = pd.read_csv(p)
                elif p.suffix in [".xlsx", ".xls"]:
                    self.frames[name] = pd.read_excel(p)
            except Exception:
                continue

    def get_stats(self):
        stats = {}
        for name, df in self.frames.items():
            stats[name] = {
                col: float(df[col].mean())
                for col in df.columns
                if pd.api.types.is_numeric_dtype(df[col])
            }
        return stats

    def get_df(self, name: str):
        return self.frames.get(name)


# ── Context Builder ───────────────────────────────────────────────────────────

class ContextBuilder:
    """Retrieves context from PDF RAG pipeline."""

    def __init__(self, pdf_rag: PDFRAGPipeline):
        self.pdf_rag = pdf_rag

    def build(self, query: str) -> str:
        raw = self.pdf_rag.retrieve_context(query)
        return f"[Source: Postpartum Clinical Document]\n\n{raw}"


# ── Dataset Manager ───────────────────────────────────────────────────────────

class DatasetManager:
    def __init__(self):
        self.structured      = StructuredDataLoader(DATASETS)
        self.structured.load()
        self.pdf_rag         = PDFRAGPipeline(DATASETS["postpartum_pdf"])
        self.context_builder = ContextBuilder(pdf_rag=self.pdf_rag)

    def get_context(self, query: str) -> str:
        return self.context_builder.build(query)

    def get_stats(self):
        return self.structured.get_stats()

    def get_dataframe(self, name: str):
        return self.structured.get_df(name)

    def dataset_source_count(self) -> int:
        return len(self.structured.frames)

    def dataset_source_summary(self):
        loaded  = list(self.structured.frames.keys())
        missing = [
            k for k in self.structured.datasets
            if k not in self.structured.frames
            and k != "postpartum_pdf"
        ]
        return {"available": loaded, "missing": missing}

    def get_diet_data(self, phase: str):
        diet_map = {
            "immediate_postpartum": [
                "Warm fluids like jeera water, ajwain water, and mild herbal teas",
                "Iron-rich foods like spinach, methi, lentils, and jaggery",
                "Easily digestible foods such as khichdi and light soups",
                "Avoid cold, raw, or refrigerated foods",
                "Avoid gas-forming foods like eggplant, cabbage, and excess legumes",
            ],
            "early_postpartum": [
                "High-protein foods like dal, eggs, paneer, and lean meats",
                "Hydration with coconut water, warm water, and buttermilk",
                "Light soups and steamed vegetables",
                "Fiber-rich foods to support digestion",
                "Avoid overly spicy, oily, or processed foods",
            ],
            "late_postpartum": [
                "Balanced diet with seasonal vegetables and fruits",
                "Whole grains like brown rice, oats, and whole wheat",
                "Calcium-rich foods like milk, curd, sesame seeds, and ragi",
                "Healthy fats from nuts, seeds, and ghee",
                "Continue iron-rich foods if needed for recovery",
            ],
        }
        return diet_map.get(
            phase,
            ["Balanced nutritious diet", "Stay hydrated", "Eat home-cooked meals"]
        )