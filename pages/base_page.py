from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Kelas dasar yang diwarisi oleh seluruh halaman Page Object."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, locator):
        """Mencari elemen tunggal dengan explicit wait visibility."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Elemen dengan lokator {locator} tidak ditemukan dalam waktu tunggu."
            )

    def is_element_present(self, locator) -> bool:
        """True jika elemen terlihat dalam waktu tunggu, False jika tidak."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        """Menunggu elemen dapat diklik lalu melakukan aksi klik."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Mengisi teks ke input field setelah membersihkan teks sebelumnya."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Mengambil teks visual dari suatu elemen web."""
        return self.find_element(locator).text

    def get_current_url(self):
        """Mendapatkan alamat URL browser saat ini."""
        return self.driver.current_url

    def wait_for_url(self, url):
        """Menunggu (explicit wait) sampai URL sama persis dengan yang diharapkan."""
        return self.wait.until(EC.url_to_be(url))
