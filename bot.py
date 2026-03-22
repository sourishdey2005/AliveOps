import requests
import time
import random

URLS = [
    "https://arthgyan-site.streamlit.app/",
    "https://bizsight-ai---business-intelligence-platform.streamlit.app/",
    "https://market-regime-shift-detector.streamlit.app/"
    "https://monte-carlo-option-pricing-dashboard.streamlit.app/"
    "https://monte-carlo-stimulation.streamlit.app/"
    "https://quant-analytics-app.streamlit.app/"
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
