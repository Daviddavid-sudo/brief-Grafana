from prometheus_client import Counter, Histogram

# Counter for total requests
REQUEST_COUNTER = Counter("myapp_requests_total", "Total requests received")

# Histogram for latency
REQUEST_LATENCY = Histogram("myapp_request_latency_seconds", "Request latency in seconds")
