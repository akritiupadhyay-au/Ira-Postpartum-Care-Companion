# Trusted source registry for postpartum article feeds.

from __future__ import annotations

TRUSTED_SOURCES = [
    {
        "source_name": "WHO (RSS)",
        "source_type": "rss",
        "url": "https://www.who.int/feeds/entity/news-room/rss.xml",
        "topic_tags": ["maternal_health", "postpartum", "women_health"],
        "trust_tier": "high",
    },
    {
        "source_name": "CDC (RSS)",
        "source_type": "rss",
        "url": "https://tools.cdc.gov/api/v2/resources/media/403372.rss",
        "topic_tags": ["postpartum_depression", "maternal_health", "breastfeeding"],
        "trust_tier": "high",
    },
    {
        "source_name": "NHS (RSS)",
        "source_type": "rss",
        "url": "https://www.nhs.uk/rss/news.xml",
        "topic_tags": ["postnatal_care", "mental_health", "women_health"],
        "trust_tier": "high",
    },
    {
        "source_name": "WHO - Postnatal Care Guidelines",
        "source_type": "page",
        "url": "https://www.who.int/publications/i/item/9789240045989",
        "topic_tags": [
            "postpartum care",
            "maternal health",
            "newborn care",
            "postnatal depression",
            "breastfeeding",
            "maternal safety",
            "global health guidelines",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "WHO - Maternal and Newborn Health Overview",
        "source_type": "page",
        "url": "https://www.who.int/health-topics/maternal-health",
        "topic_tags": [
            "pregnancy",
            "postpartum recovery",
            "maternal mortality",
            "newborn health",
            "antenatal care",
            "postnatal care systems",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "WHO - Postnatal Care for a Positive Experience (BMJ Series)",
        "source_type": "page",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9887708/",
        "topic_tags": [
            "postnatal care quality",
            "maternal mental health",
            "postpartum depression",
            "healthcare systems",
            "postpartum recovery",
            "family-centered care",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "WHO - Pregnancy, Childbirth, Postpartum and Newborn Care Guide",
        "source_type": "page",
        "url": "https://www.ncbi.nlm.nih.gov/books/NBK326678/",
        "topic_tags": [
            "postpartum hemorrhage",
            "breastfeeding support",
            "maternal complications",
            "newborn care",
            "postnatal depression",
            "clinical guidelines",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "CDC - Maternal Health Overview",
        "source_type": "page",
        "url": "https://www.cdc.gov/reproductivehealth/maternal-mortality/",
        "topic_tags": [
            "maternal health risks",
            "postpartum depression",
            "chronic conditions in pregnancy",
            "maternal mortality",
            "public health surveillance",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "CDC - PRAMS Maternal & Infant Health Surveillance",
        "source_type": "page",
        "url": "https://www.cdc.gov/prams/",
        "topic_tags": [
            "postpartum depression data",
            "maternal behavior tracking",
            "infant health outcomes",
            "pregnancy surveys",
            "epidemiology",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "NHS - Postnatal Care and Recovery",
        "source_type": "page",
        "url": "https://www.nhs.uk/pregnancy/labour-and-birth/after-the-birth/your-body-after-the-birth/",
        "topic_tags": [
            "postpartum recovery",
            "breastfeeding support",
            "mental health after birth",
            "physical healing",
            "baby care",
            "maternal wellbeing",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "NHS - Perinatal Mental Health Support",
        "source_type": "page",
        "url": "https://www.nhs.uk/mental-health/conditions/perinatal-mental-health/",
        "topic_tags": [
            "postpartum depression",
            "postpartum anxiety",
            "psychosis risk",
            "maternal mental health services",
            "therapy",
            "crisis support",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "PMC - Postpartum Depression Research Collection",
        "source_type": "page",
        "url": "https://pmc.ncbi.nlm.nih.gov/",
        "topic_tags": [
            "postpartum depression",
            "maternal psychiatry",
            "anxiety disorders",
            "hormonal changes",
            "neurobiology",
            "treatment studies",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "PMC - Maternal Health & Postpartum Care Reviews",
        "source_type": "page",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/?term=postpartum+care",
        "topic_tags": [
            "postpartum complications",
            "maternal outcomes",
            "breastfeeding research",
            "healthcare interventions",
            "global maternal health studies",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "CDC - Breastfeeding Guidance",
        "source_type": "page",
        "url": "https://www.cdc.gov/breastfeeding/",
        "topic_tags": [
            "lactation",
            "breastfeeding problems",
            "nipple pain",
            "milk supply",
            "infant nutrition",
            "maternal health support",
        ],
        "trust_tier": "high",
    },
    {
        "source_name": "WHO - Maternal Mental Health",
        "source_type": "page",
        "url": "https://www.who.int/teams/mental-health-and-substance-use/promotion-prevention/maternal-mental-health",
        "topic_tags": [
            "postpartum depression",
            "anxiety disorders",
            "psychosis",
            "maternal mental health screening",
            "emotional wellbeing",
        ],
        "trust_tier": "high",
    },
]

KNOWLEDGE_BASE_REFERENCES = [
    {
        "source_name": (
            "WHO - WHO Recommendations on Maternal and Newborn Care "
            "for a Positive Postnatal Experience"
        ),
        "url": "https://www.who.int/publications/i/item/9789240045989",
        "topic_tags": [
            "postpartum care",
            "maternal mental health",
            "postnatal depression screening",
            "breastfeeding",
            "maternal safety",
            "clinical guidelines",
        ],
        "why_useful": [
            "Defines postnatal mental health screening",
            "Emphasizes early detection of depression",
            "Supports escalation of emotional bonding issues",
        ],
    },
    {
        "source_name": "WHO - Maternal Mental Health Overview",
        "url": (
            "https://www.who.int/teams/mental-health-and-substance-use/"
            "promotion-prevention/maternal-mental-health"
        ),
        "topic_tags": [
            "postpartum depression",
            "anxiety",
            "psychosis risk",
            "perinatal mental health",
            "screening",
            "global health",
        ],
        "key_insight": (
            "Clear classification of postpartum depression as a medical condition "
            "including sadness, guilt, and bonding issues."
        ),
    },
    {
        "source_name": "CDC - Depression Among Women / Postpartum Depression",
        "url": "https://www.cdc.gov/reproductive-health/depression/index.html",
        "topic_tags": [
            "postpartum depression",
            "mood disorders",
            "maternal mental health",
            "screening",
            "epidemiology",
        ],
        "key_insight": (
            "Postpartum depression includes persistent sadness, loss of interest, "
            "fatigue, and bonding difficulty."
        ),
    },
    {
        "source_name": "CDC - Maternal Health Indicators (PRAMS)",
        "url": "https://www.cdc.gov/cdi/indicator-definitions/maternal-health.html",
        "topic_tags": [
            "postpartum depression",
            "maternal outcomes",
            "infant bonding",
            "breastfeeding impact",
        ],
        "key_insight": (
            "Postpartum depression impacts maternal behavior, infant bonding, "
            "and breastfeeding outcomes."
        ),
    },
    {
        "source_name": "NHS - Perinatal Mental Health",
        "url": "https://www.nhs.uk/mental-health/conditions/perinatal-mental-health/",
        "topic_tags": [
            "postpartum depression",
            "anxiety",
            "psychosis",
            "mental health services",
            "maternal support",
        ],
        "why_useful": [
            "Explicitly categorizes postpartum depression, anxiety, and psychosis",
            "Emphasizes early intervention",
        ],
    },
    {
        "source_name": "PMC - Postpartum Depression Updates in Evaluation and Care",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9767320/",
        "topic_tags": [
            "postpartum depression",
            "diagnostic criteria",
            "peripartum depression",
            "psychiatric evaluation",
        ],
        "key_insight": (
            "Clinical symptom pattern includes sadness, guilt, loss of interest, "
            "bonding difficulty, and emotional numbness."
        ),
    },
    {
        "source_name": "PMC - Pathophysiological Mechanisms in PPD",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6370514/",
        "topic_tags": [
            "depression criteria",
            "DSM symptoms",
            "postpartum mood disorder",
            "clinical thresholds",
        ],
        "key_insight": (
            "Diagnostic symptoms include depressed mood, guilt, concentration "
            "issues, loss of pleasure, and fatigue."
        ),
    },
    {
        "source_name": "PMC - Maternal and Infant Outcomes of PPD",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9767320/",
        "topic_tags": [
            "maternal outcomes",
            "infant bonding",
            "untreated depression",
            "postpartum impact",
        ],
        "why_useful": [
            "Shows untreated postpartum depression affects bonding and caregiving",
            "Highlights long-term maternal health consequences",
        ],
    },
]