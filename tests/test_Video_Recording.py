from playwright.sync_api import sync_playwright, expect, Page

def test_video_recording():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo = 2000, channel = 'chrome')
        context = browser.new_context(
            record_video_dir=r"I:\TMAsolutions\Training\Playwright\Playwright_session7",
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/", timeout=880000)

        heading_text = page.locator("h1")
        expect(heading_text).to_have_text("Practice Page")
        expect(page.locator("#autocomplete")).to_be_visible()

        page.click("#hide-textbox")
        expect(page.locator("#displayed-text")).to_be_hidden()

        page.wait_for_timeout(2000)

        # ✅ Get the video path before closing the context
        video_path = page.video.path()
        print(f"📹 Video saved at: {video_path}")

        context.close()
        browser.close()

if __name__ == "__main__":
    test_video_recording()
