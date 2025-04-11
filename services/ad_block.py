def block_ads(data):
    # Simulate ad-blocking logic
    blocked = ["ads.example.com", "tracker.example.com"]
    return [url for url in data if url not in blocked]