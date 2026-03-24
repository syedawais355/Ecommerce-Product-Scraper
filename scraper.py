import requests
from bs4 import BeautifulSoup
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def init_db(db_name="product.db"):
    """Initializes the SQLite database and creates the products table if it doesn't exist."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                subcategory TEXT,
                price TEXT,
                image_url TEXT,
                availability TEXT,
                brand TEXT,
                product_url TEXT UNIQUE
            )
        """)
        conn.commit()

def get_product(url, db_name="product.db"):
    """
    Scrapes product details from the given URL and saves them to the database.

    Args:
        url (str): The URL of the product page to scrape.
        db_name (str): The name of the SQLite database file.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.find("div", class_="product-information")

    if not info:
        logging.warning(f"Could not find product information on {url}")
        return

    product = {}

    # Extract Product Name
    name_tag = info.find("h2")
    product["name"] = name_tag.text.strip() if name_tag else "Unknown"

    # Extract Category and Subcategory
    product["category"] = "None"
    product["subcategory"] = "None"
    for p in info.find_all("p"):
        text = p.get_text(strip=True)
        if "Category:" in text:
            category_text = text.replace("Category:", "").strip()
            parts = [part.strip() for part in category_text.split(">")]
            product["category"] = parts[0] if len(parts) > 0 else "None"
            product["subcategory"] = parts[1] if len(parts) > 1 else "None"
            break

    # Extract Price
    try:
        outer_span = info.find("span")
        inner_span = outer_span.find("span")
        product["price"] = inner_span.text.replace("Rs.", "").strip()
    except AttributeError:
        product["price"] = "Unknown"

    # Extract Availability
    product["availability"] = "In Stock" if "In Stock" in info.text else "Out of Stock"

    # Extract Brand
    product["brand"] = "None"
    for p in info.find_all("p"):
        b_tag = p.find("b")
        if b_tag and "Brand:" in b_tag.text:
            product["brand"] = b_tag.next_sibling.strip() if b_tag.next_sibling else "None"
            break

    # Extract Image URL
    try:
        view_product = soup.find("div", class_="view-product")
        image = view_product.find("img")
        product["image_url"] = "https://automationexercise.com" + image["src"]
    except (AttributeError, TypeError):
        product["image_url"] = "None"

    # Output to console
    print("-" * 40)
    print(f"Name:         {product['name']}")
    print(f"Category:     {product['category']}")
    print(f"Subcategory:  {product['subcategory']}")
    print(f"Price:        {product['price']}")
    print(f"Brand:        {product['brand']}")
    print(f"Availability: {product['availability']}")
    print(f"Image URL:    {product['image_url']}")
    print("-" * 40)

    # Save to Database
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO products
                (name, category, subcategory, price, image_url, availability, brand, product_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                product["name"], product["category"], product["subcategory"], product["price"],
                product["image_url"], product["availability"], product["brand"], url
            ))
            if cursor.rowcount > 0:
                logging.info(f"Successfully saved to {db_name}")
            else:
                logging.info(f"Product already exists in {db_name}, skipping.")
            conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")

if __name__ == "__main__":
    # Initialize Database
    init_db()

    # Example URL to scrape
    target_url = "https://automationexercise.com/product_details/30"
    logging.info(f"Starting scraper for: {target_url}")
    get_product(target_url)
