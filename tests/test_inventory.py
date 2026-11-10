from pages.login_page import LoginPage


class TestInventory:
    """Kasus uji alur inventori & keranjang belanja (Shopping Cart Flow)."""

    def test_add_to_cart_flow(self, inventory_page):
        """TC-04: Add Backpack -> badge keranjang menunjukkan '1'."""
        inventory_page.add_backpack_to_cart()

        badge = inventory_page.get_cart_badge_count()
        assert badge == "1", f"Badge keranjang diharapkan '1', tetapi '{badge}'"
        assert inventory_page.is_remove_button_displayed() is True, (
            "Tombol Remove tidak tampil setelah produk ditambahkan!"
        )

    def test_logout_flow(self, driver, inventory_page):
        """TC-05: Logout -> kembali ke URL login & tombol Login tampil."""
        inventory_page.logout()

        login_url = LoginPage.URL
        inventory_page.wait_for_url(login_url)
        assert inventory_page.get_current_url() == login_url, (
            "Pengguna tidak dialihkan ke halaman login setelah logout!"
        )
        assert LoginPage(driver).is_login_button_displayed() is True, (
            "Tombol Login tidak tampil setelah logout!"
        )

    def test_remove_from_cart_flow(self, inventory_page):
        """TC-06 (tambahan): Add lalu Remove -> badge keranjang hilang."""
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"

        inventory_page.remove_backpack_from_cart()
        assert inventory_page.is_cart_badge_present() is False, (
            "Badge keranjang masih tampil padahal produk sudah dihapus!"
        )
