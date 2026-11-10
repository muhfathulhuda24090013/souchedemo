# SauceDemo Test Automation (Selenium + pytest + Page Object Model)

Praktikum Pengujian Perangkat Lunak (TI505) - Pertemuan 7.
Target aplikasi: https://www.saucedemo.com/

## Struktur
```
pages/        Page Object (lokator Relative XPath + aksi)
  base_page.py, login_page.py, inventory_page.py
tests/        Skrip uji + assertion (tanpa lokator)
  test_login.py, test_inventory.py
conftest.py   Fixture browser & precondition login
pytest.ini    Konfigurasi pytest
```

## Menjalankan
```bash
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1   |  Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
pytest -v            # tampil browser
HEADLESS=1 pytest -v # tanpa GUI (Windows PowerShell: $env:HEADLESS=1; pytest -v)
```

## Test case
| ID | Test | Assertion utama |
|----|------|-----------------|
| TC-01 | Login valid | URL inventory + logo tampil |
| TC-02 | Login locked_out_user | Pesan error locked out |
| TC-03 | Login password kosong | Pesan "Password is required" |
| TC-04 | Add Backpack ke cart | Badge = "1" |
| TC-05 | Logout | URL login + tombol Login tampil |
| TC-06 | Remove dari cart | Badge hilang |

## Anggota Kelompok
| Nama | NIM |
|------|-----|
| (isi) | (isi) |
