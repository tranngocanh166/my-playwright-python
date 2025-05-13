# test_sample.py
from playwright.sync_api import expect

def test_run(context_with_trace):
    page = context_with_trace
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    heading_text = page.locator("h1123")  # Intentionally wrong selector
    expect(heading_text).to_have_text("Practice Page")
