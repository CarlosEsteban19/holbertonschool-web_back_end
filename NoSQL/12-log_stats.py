#!/usr/bin/env python3
"""task 12"""

from pymongo import MongoClient


def log_stats():
    """log stats"""
    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: collection.count_documents({"method": method})
        for method in methods
    }

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{total_logs} logs")
    print("Methods:")
    print("\n".join(
        [f"\tmethod {method}: {method_counts[method]}" for method in methods]))
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
