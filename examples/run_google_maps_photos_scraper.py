#!/usr/bin/env python3
"""
Google Maps Contributor & Local Guide Photos Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-maps-photos-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-maps-photos-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-maps-photos-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_maps_photos_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "contributors": ["https://www.google.com/maps/contrib/102520373756565203865"],
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}

run = client.actor("unitbytes/google-maps-photos-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("name"), item.get("placeName"), item.get("placeRating"))
