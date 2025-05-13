from playwright.sync_api import sync_playwright, expect, Page

def test_run():
    trace_file = f"{test_run.__name__}.zip"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo = 2000, channel = 'chrome')
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/", timeout=880000)

        # Locator Assertions
        heading_text = page.locator("h1")

        # expect(heading_text).to_have_text("Practice Page123")
        expect(heading_text).to_have_text("Practice Page")

        expect(page.locator("#autocomplete")).to_be_visible()

        page.click("#hide-textbox")

        expect(page.locator("#displayed-text")).to_be_hidden()

        page.wait_for_timeout = 20000

        # context.tracing.stop(path="trace.zip")
        context.tracing.stop(path=trace_file)

        browser.close()

if __name__ == "__main__":
    test_run()
