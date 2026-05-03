"""
CHOPPIES SUPERMARKET — DATA GENERATOR
Run this FIRST. Generates 12 months of retail transaction data.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from itertools import combinations

np.random.seed(42)
random.seed(42)

print("=" * 70)
print("CHOPPIES SUPERMARKET — GENERATING RETAIL DATA")
print("=" * 70)

START_DATE = datetime(2025, 1, 1)
END_DATE   = datetime(2025, 12, 31)
DAYS       = (END_DATE - START_DATE).days + 1

# Product catalog
PRODUCTS = [
    # Category, Product, Base Price, Stock Level
    ("Dairy", "Milk 2L", 28.50, 500),
    ("Dairy", "Butter 500g", 45.00, 200),
    ("Dairy", "Cheese 250g", 52.00, 150),
    ("Dairy", "Yogurt 1L", 35.00, 180),
    ("Bakery", "White Bread", 12.50, 400),
    ("Bakery", "Brown Bread", 14.00, 300),
    ("Bakery", "Rolls Pack", 18.00, 250),
    ("Beverages", "Coca Cola 2L", 18.50, 600),
    ("Beverages", "Orange Juice 1L", 24.00, 300),
    ("Beverages", "Water 6pack", 22.00, 500),
    ("Beverages", "Tea Bags 100s", 38.00, 200),
    ("Snacks", "Chips 150g", 12.00, 350),
    ("Snacks", "Biscuits 200g", 15.50, 280),
    ("Snacks", "Chocolate Bar", 8.50, 400),
    ("Meat", "Chicken 1kg", 58.00, 200),
    ("Meat", "Beef Mince 500g", 65.00, 150),
    ("Meat", "Pork Chops 500g", 72.00, 120),
    ("Fresh Produce", "Tomatoes 1kg", 18.00, 250),
    ("Fresh Produce", "Onions 1kg", 15.00, 300),
    ("Fresh Produce", "Potatoes 2kg", 22.00, 400),
    ("Fresh Produce", "Apples 1kg", 32.00, 200),
    ("Household", "Washing Powder 2kg", 68.00, 180),
    ("Household", "Dish Soap 750ml", 24.50, 220),
    ("Household", "Toilet Paper 9pk", 42.00, 300),
    ("Personal Care", "Shampoo 400ml", 48.00, 150),
    ("Personal Care", "Toothpaste", 22.00, 200),
    ("Personal Care", "Soap 3pk", 18.50, 250),
]

products_df = pd.DataFrame(PRODUCTS, columns=["category","product","base_price","stock_level"])
products_df["product_id"] = ["P" + str(i+1).zfill(3) for i in range(len(products_df))]
products_df.to_csv("product_catalog.csv", index=False)

print(f"\n  ✅  {len(products_df)} products in catalog")

# Promotional periods
PROMOS = [
    ("Easter Sale", datetime(2025, 4, 15), 7, 0.15),
    ("Independence Day", datetime(2025, 9, 30), 3, 0.20),
    ("Black Friday", datetime(2025, 11, 28), 4, 0.25),
    ("Christmas Sale", datetime(2025, 12, 20), 10, 0.18),
]

# Association rules (products bought together)
ASSOCIATIONS = [
    (["Milk 2L", "White Bread"], 0.65),
    (["Milk 2L", "Butter 500g"], 0.45),
    (["Coca Cola 2L", "Chips 150g"], 0.55),
    (["Chicken 1kg", "Tomatoes 1kg", "Onions 1kg"], 0.50),
    (["Tea Bags 100s", "Milk 2L", "Biscuits 200g"], 0.40),
    (["Washing Powder 2kg", "Dish Soap 750ml"], 0.35),
    (["Shampoo 400ml", "Soap 3pk"], 0.42),
    (["White Bread", "Butter 500g", "Cheese 250g"], 0.38),
]

print(f"  ✅  {len(ASSOCIATIONS)} product associations defined")

# Generate transactions
print("\n[1/2] Generating transactions...")

transactions = []
transaction_id = 1

for day_offset in range(DAYS):
    current_date = START_DATE + timedelta(days=day_offset)
    day_name = current_date.strftime("%A")
    is_weekend = day_name in ("Saturday", "Sunday")
    
    # Check if promo period
    promo_multiplier = 1.0
    promo_name = None
    for p_name, p_date, p_days, p_discount in PROMOS:
        if abs((current_date - p_date).days) <= p_days:
            promo_multiplier = 1.0 + (p_discount * 2)  # Promo boosts traffic
            promo_name = p_name
            break
    
    # Daily transaction count
    base_txns = 180
    if is_weekend: base_txns = int(base_txns * 1.3)
    daily_txns = int(base_txns * promo_multiplier + random.gauss(0, 20))
    daily_txns = max(50, daily_txns)
    
    for _ in range(daily_txns):
        basket_size = random.choices([1,2,3,4,5,6,7,8], weights=[10,20,25,20,12,8,3,2])[0]
        
        # Select products (sometimes follow associations)
        basket = []
        if random.random() < 0.3 and basket_size >= 2:
            # Use association rule
            assoc = random.choice(ASSOCIATIONS)
            for prod_name in assoc[0][:basket_size]:
                basket.append(prod_name)
        
        # Fill rest randomly
        while len(basket) < basket_size:
            prod = random.choice(products_df["product"].tolist())
            if prod not in basket:
                basket.append(prod)
        
        # Create transaction
        for prod_name in basket:
            prod_row = products_df[products_df["product"] == prod_name].iloc[0]
            price = prod_row["base_price"]
            
            # Apply promo discount
            discount = 0
            if promo_name and random.random() < 0.4:
                for p_n, p_d, p_days, p_disc in PROMOS:
                    if p_n == promo_name:
                        discount = p_disc
                        break
            
            final_price = price * (1 - discount)
            
            transactions.append({
                "transaction_id": f"TXN{transaction_id:07d}",
                "date": current_date.strftime("%Y-%m-%d"),
                "day_of_week": day_name,
                "product_id": prod_row["product_id"],
                "product": prod_name,
                "category": prod_row["category"],
                "quantity": 1,
                "base_price": price,
                "discount_pct": round(discount * 100, 1),
                "final_price": round(final_price, 2),
                "promo_period": promo_name if promo_name else "No Promo",
            })
        
        transaction_id += 1

df_txns = pd.DataFrame(transactions)
df_txns.to_csv("transactions.csv", index=False)
print(f"  ✅  {len(df_txns):,} transaction line items")
print(f"  ✅  {transaction_id-1:,} total transactions")
print(f"  ✅  Total revenue: P{df_txns['final_price'].sum():,.2f}")

# Generate stock levels
print("\n[2/2] Generating inventory stock levels...")

stock_data = []
for _, prod in products_df.iterrows():
    product_txns = df_txns[df_txns["product"] == prod["product"]]
    total_sold = len(product_txns)
    avg_daily_sales = total_sold / DAYS
    
    current_stock = prod["stock_level"]
    reorder_point = int(avg_daily_sales * 7)  # 7 days buffer
    days_of_stock = int(current_stock / avg_daily_sales) if avg_daily_sales > 0 else 999
    stockout_risk = 1 if days_of_stock < 7 else 0
    
    stock_data.append({
        "product_id": prod["product_id"],
        "product": prod["product"],
        "category": prod["category"],
        "current_stock": current_stock,
        "total_sold_ytd": total_sold,
        "avg_daily_sales": round(avg_daily_sales, 2),
        "reorder_point": reorder_point,
        "days_of_stock": days_of_stock,
        "stockout_risk": stockout_risk,
    })

df_stock = pd.DataFrame(stock_data)
df_stock.to_csv("inventory_levels.csv", index=False)
print(f"  ✅  {len(df_stock)} products tracked")
print(f"  ✅  {df_stock['stockout_risk'].sum()} items at stockout risk")

print("\n" + "─"*70)
print("DATA GENERATION COMPLETE")
print("─"*70)
print(f"  📂 product_catalog.csv   : {len(products_df)} products")
print(f"  📂 transactions.csv      : {len(df_txns):,} line items")
print(f"  📂 inventory_levels.csv  : {len(df_stock)} items")
print(f"\n  Next: python 02_eda_ml.py")
print("=" * 70)
