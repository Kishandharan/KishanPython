from playwright.sync_api import sync_playwright

def test_t1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        title = page.title()
        browser.close()
        assert title == "Google", "Title mismatch"
        
