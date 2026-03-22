import requests
import time
import random

URLS = [
    "https://app1.streamlit.app",
    "https://app2.streamlit.app",
    "https://app3.streamlit.app"
]

BOTS_PER_APP = 2  # keep low to avoid detection

def ping_all():
    for url in URLS:
        for i in range(BOTS_PER_APP):
            try:
                start = time.time()
                response = requests.get(url, timeout=10)
                latency = round((time.time() - start) * 1000, 2)

                print(f"{url} | Bot-{i+1} | Status: {response.status_code} | {latency} ms")

            except Exception as e:
                print(f"{url} | Bot-{i+1} | Error: {e}")

            # small random delay between bots
            time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    print("Starting ping cycle...")
    ping_all()
    print("Done.")