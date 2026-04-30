from utils import parse_price
from pages.base_page import BasePage

PRICE_SELECTORS = [
    "[data-test='main-price']",
    ".product-new-price",
    ".pricing-block .product-new-price",
    ".product-highlight-price .product-new-price",
    "span.product-new-price",
]


class EmagProductPage(BasePage):
    site_name = "eMAG"

    def get_current_price(self):
        for selector in PRICE_SELECTORS:
            locator = self.page.locator(selector).first
            if locator.count() > 0:
                try:
                    raw = locator.inner_text(timeout=5000)
                    price = parse_price(raw)
                    if price:
                        return price
                except Exception:
                    continue
        raise ValueError(f"Price element not found on {self.page.url}. Tried selectors: {PRICE_SELECTORS}")

    def get_original_price(self, current_price):
        pricing_block = self.page.locator(".product-highlight-price, .pricing-block").first
        strikethrough = pricing_block.locator("s")
        if strikethrough.count() == 0:
            return None
        raw = strikethrough.first.inner_text()
        original = parse_price(raw)
        if original < current_price:
            return None
        return original
