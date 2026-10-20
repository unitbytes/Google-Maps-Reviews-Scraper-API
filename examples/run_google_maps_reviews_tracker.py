#!/usr/bin/env python3
"""
Google Maps Reviews Tracker: Check Removed & Edited Reviews — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-maps-reviews-tracker?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-maps-reviews-tracker/
n8n Template: https://unitbytes.com/n8n/workflows/google-maps-reviews-tracker-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_maps_reviews_tracker.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "reviewsToCheck": [
        "https://maps.app.goo.gl/wSLNNUnwRAwg1T4W9",
        "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUNwLWNMM2J3EAE!2m1!1s0x0:0x57656ffbe42744ba!3m1!1s2@1:CAIQACodChtycF9oOlJORWFGdmxEN3VmeDI1VlFXRXotRXc%7C%7C?hl=en-US"
    ],
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}

run = client.actor("unitbytes/google-maps-reviews-tracker").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("reviewer_name"), item.get("business_name"), item.get("review_date"))
