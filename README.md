# Ecommerce Product Scraper

A Python web scraper that extracts product information from e-commerce websites and stores it in a local SQLite database.

The script collects the following fields when available:
- Product name
- Price
- Brand
- Category and subcategory
- Availability status
- Product image URL
- Product URL (used as unique identifier)

Data is saved into a SQLite database (`product.db`) with duplicate prevention based on the product URL.

## Features

- Extracts structured product data using requests and BeautifulSoup
- Stores data in a local SQLite database
- Prevents duplicate entries using product URL as unique key
- Supports scraping single products or multiple products via URL list
- Minimal dependencies and lightweight execution

## Requirements

- Python 3.8+
- requests
- beautifulsoup4

## Installation

1. Clone the repository

   ```
   git clone https://github.com/syedawais355/ecommerce-product-scraper.git
   cd ecommerce-product-scraper
   ```

2. (Recommended) Create and activate a virtual environment

   ```
   python -m venv venv
   
   # Linux / macOS
   source venv/bin/activate
   
   # Windows (Command Prompt)
   venv\Scripts\activate
   
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies

   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

### Single product

Edit `scraper.py` and set the URL, then run:

```
python scraper.py
```

Example in code:

```
url = "https://automationexercise.com/product_details/30"
get_product(url)
```

### Multiple products

Modify the script to include a list of URLs:

```
urls = [
    "https://automationexercise.com/product_details/30",
    "https://automationexercise.com/product_details/31",
    "https://automationexercise.com/product_details/32",
    # add more URLs here
]

for url in urls:
    get_product(url)
```

Then execute:

```
python scraper.py
```

## Output

After running, two main outputs are generated:

1. Console output showing each processed product  
2. SQLite database file: `product.db`

You can inspect the database using any SQLite viewer or with Python:

```python
import sqlite3

conn = sqlite3.connect('product.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM products")
print(cursor.fetchall())
conn.close()
```

Example console output:

```
Product: Blue Top
Price: Rs. 500
Brand: Polo
Category: Women > Tops
Availability: In Stock
Image: https://...
URL: https://automationexercise.com/product_details/30
----------------------------------------
```

## Project Files

```
ecommerce-product-scraper/
├── scraper.py          Main scraping logic and database storage
├── requirements.txt    Project dependencies
├── product.db          Created automatically after first run (git ignored)
└── README.md
```

## Notes

- This scraper is tailored to the structure of automationexercise.com.  
  For other websites, selectors (find, find_all, get_text, etc.) will likely need adjustment.
- Always respect the website’s `robots.txt` and terms of service.
- Consider adding delays (time.sleep) when scraping multiple pages to avoid rate limiting or IP blocking.
