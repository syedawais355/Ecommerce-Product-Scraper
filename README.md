# 🛒 Ecommerce Product Scraper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BeautifulSoup](https://img.shields.io/badge/Scraper-BeautifulSoup4-green.svg)](https://www.crummy.com/software/BeautifulSoup/)

A robust, professional Python-based web scraper designed to extract detailed product information from e-commerce platforms. This tool streamlines data collection by capturing product names, pricing, branding, categories, and more, storing them in a structured SQLite database.

---

## 🚀 Features

- **🔍 Precise Extraction:** Captures Name, Price, Brand, Category, Subcategory, Availability, and Image URL.
- **🗄️ SQLite Integration:** Automatically stores data in a local `product.db` for easy access and persistence.
- **🛡️ Duplicate Prevention:** Uses unique product URLs as keys to ensure data integrity and avoid redundant entries.
- **📊 Detailed Logging:** Comprehensive logging for monitoring scraping progress and debugging issues.
- **🛠️ Robust Error Handling:** Gracefully handles network timeouts, HTTP errors, and missing data points.

---

## 📂 Project Structure

```text
ecommerce-product-scraper/
├── scraper.py          # Main scraping engine and database logic
├── requirements.txt    # Project dependencies
├── product.db          # Local SQLite database (auto-generated)
├── LICENSE             # MIT License file
└── README.md           # Project documentation
```

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/syedawais355/ecommerce-product-scraper.git
cd ecommerce-product-scraper
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Running the Scraper
The scraper is configured to process a single product URL by default. Execute the script with:

```bash
python scraper.py
```

### Customizing the Target
To scrape a different product, modify the `target_url` in the `if __name__ == "__main__":` block of `scraper.py`:

```python
if __name__ == "__main__":
    init_db()
    target_url = "https://automationexercise.com/product_details/1" # Change this
    get_product(target_url)
```

---

## 📊 Data Schema

The collected data is stored in the `products` table of `product.db` with the following structure:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary Key (Auto-increment) |
| `name` | TEXT | Product Name |
| `category` | TEXT | Primary Category |
| `subcategory` | TEXT | Specific Subcategory |
| `price` | TEXT | Product Price (Numeric string) |
| `image_url` | TEXT | URL to the product image |
| `availability`| TEXT | Stock status (In Stock / Out of Stock) |
| `brand` | TEXT | Manufacturer/Brand name |
| `product_url` | TEXT | Unique identifier for the product |

---

## 🛡️ Best Practices & Ethics

- **Respect Robots.txt:** Always check the website's `robots.txt` before scraping.
- **Rate Limiting:** If scraping multiple products, implement `time.sleep()` to avoid overwhelming server resources.
- **User-Agent:** Consider adding a custom User-Agent in `requests.get()` headers for more professional requests.

---

## 🛣️ Roadmap

- [ ] Support for multiple concurrent URLs (Threading/Async).
- [ ] Export functionality (CSV, JSON, Excel).
- [ ] Support for additional e-commerce templates.
- [ ] Integration with Headless Browsers (Playwright/Selenium) for dynamic content.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Developed with ❤️ by [Syed Muhammad Awais Gillani](https://github.com/syedawais355)**
