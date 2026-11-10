from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object untuk halaman Inventory (daftar produk) SauceDemo."""

    URL = "https://www.saucedemo.com/inventory.html"

    # ---- Lokator (Relative XPath) ----
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title' and text()='Products']")
    ADD_BACKPACK_BUTTON = (By.XPATH, "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]")
    REMOVE_BACKPACK_BUTTON = (By.XPATH, "//button[contains(@data-test, 'remove-sauce-labs-backpack')]")
    CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge' or contains(@class, 'shopping_cart_badge')]")
    CART_LINK = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def is_loaded(self) -> bool:
        return self.find_element(self.PAGE_TITLE).is_displayed()

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def get_cart_badge_count(self) -> str:
        """Teks angka pada badge keranjang (mis. '1')."""
        return self.get_text(self.CART_BADGE)

    def is_remove_button_displayed(self) -> bool:
        return self.find_element(self.REMOVE_BACKPACK_BUTTON).is_displayed()

    def is_cart_badge_present(self) -> bool:
        """False jika badge tidak muncul (keranjang kosong)."""
        return self.is_element_present(self.CART_BADGE)

    def open_menu(self):
        self.click(self.BURGER_MENU_BUTTON)

    def logout(self):
        """Buka burger menu lalu klik Logout."""
        self.open_menu()
        self.click(self.LOGOUT_LINK)
