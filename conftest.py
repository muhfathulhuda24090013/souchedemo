import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="function")
def driver():
    """Browser Chrome baru untuk setiap test; ditutup otomatis setelah selesai."""
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1366,768")
    # Matikan popup password manager Chrome yang bisa mengganggu test.
    options.add_experimental_option(
        "prefs",
        {"credentials_enable_service": False, "profile.password_manager_enabled": False},
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Mode headless: set HEADLESS=1 sebelum menjalankan pytest
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def inventory_page(driver):
    """Precondition: sudah login sebagai standard_user & berada di halaman inventory."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    page = InventoryPage(driver)
    page.wait_for_url(InventoryPage.URL)
    return page
