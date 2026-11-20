from playwright.sync_api import sync_playwright

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://coachcluster.nichesolv.com/")
    page.get_by_text("Subscription").click()
    input()
    browser.close()

