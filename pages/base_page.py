import os
import re


class BasePage:
    site_name = None

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url, timeout=60000, wait_until="domcontentloaded")
        try:
            self.page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            self.page.wait_for_timeout(3000)

    def screenshot_on_failure(self, url):
        safe_name = re.sub(r"[^\w]", "_", url)[:80]
        path = os.path.join("screenshots", f"{safe_name}.png")
        os.makedirs("screenshots", exist_ok=True)
        try:
            self.page.screenshot(path=path)
            return path
        except Exception:
            return None
