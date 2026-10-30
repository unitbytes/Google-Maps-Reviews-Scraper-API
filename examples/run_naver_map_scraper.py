#!/usr/bin/env python3
"""
Naver Map Scraper: Korean Leads & Menus — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/naver-map-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/naver-map-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/naver-map-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_naver_map_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "queries": ["강남 맛집"],
    "scrapeDetails": True,
    "maxItems": 20,
    "sortBy": "popular",
    "maxReviewsPerPlace": 10,
    "includeBlogReviews": True
}

run = client.actor("unitbytes/naver-map-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("name"), item.get("searchQuery"), item.get("rating"))
