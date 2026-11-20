from playwright.sync_api import sync_playwright as plwright

with plwright() as p: 
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://chatgpt.com")
    page.get_by_role("textbox").fill("Hello, chatgpt! How can I help you?")
    page.get_by_role("textbox").press("Enter")
    page.get_by_label("Stop Generating").wait_for(
        state="detached",
        timeout=1200000
    )
    input()
    browser.close()
