from pages.base_page import BasePage


class CarrefourProductPage(BasePage):
    site_name = "Carrefour"

    def get_current_price(self):
        el = self.page.locator("[data-price-type='finalPrice']").first
        return float(el.get_attribute("data-price-amount"))

    def get_original_price(self, current_price):
        el = self.page.locator("[data-price-type='oldPrice']")
        if el.count() == 0:
            return None
        original = float(el.first.get_attribute("data-price-amount"))
        if original < current_price:
            return None
        return original
