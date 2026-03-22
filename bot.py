from playwright.sync_api import sync_playwright
import time
import random

URLS = [
    "https://arthgyan-site.streamlit.app/",
    "https://bizsight-ai---business-intelligence-platform.streamlit.app/",
    "https://market-regime-shift-detector.streamlit.app/",
    "https://monte-carlo-option-pricing-dashboard.streamlit.app/",
    "https://monte-carlo-stimulation.streamlit.app/",
    "https://quant-analytics-app.streamlit.app/"
]

BOTS_PER_APP = 2  # keep low
WAIT_TIME = 8     # seconds to simulate user

def run_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for url in URLS:
            for i in range(BOTS_PER_APP):
                page = browser.new_page()
                try:
                    print(f"Opening {url} | Bot-{i+1}")
                    start = time.time()

                    page.goto(url, timeout=60000)
                    time.sleep(WAIT_TIME)  # simulate user staying

                    latency = round((time.time() - start) * 1000, 2)
                    print(f"SUCCESS {url} | Bot-{i+1} | {latency} ms")

                except Exception as e:
                    print(f"ERROR {url} | Bot-{i+1} | {e}")

                finally:
                    page.close()

                # random delay (important)
                time.sleep(random.uniform(2, 5))

        browser.close()

if __name__ == "__main__":
    print("🚀 Starting Playwright bot...")
    run_bot()
    print("✅ Done.")
