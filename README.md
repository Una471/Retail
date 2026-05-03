
---

## 🛒 Retail Analytics Project

🔗 **Retail Analytics Dashboard:** https://retail-dashboardd.streamlit.app/  
🔗 **Retail Management System:** https://retail-system.streamlit.app/

```markdown
## ValueMart Supermarket Gaborone — BI & Analytics Solution

> **How I helped a supermarket optimize shelf placement, prove promotion ROI, and reduce stockouts using transaction data.**

---

## 📖 The Story

### The Client

ValueMart Supermarket is a grocery store in Gaborone serving 180-230 customers daily. They carry 27 core products across 9 categories — dairy, bakery, beverages, snacks, meat, fresh produce, household, and personal care. Annual revenue is approximately P8.2 million.

The store had been operating the same way for years. Products went wherever there was shelf space. Promotions ran during every holiday because "that's what supermarkets do." Inventory was reordered when someone noticed a shelf was empty.

Nobody was using data to make decisions.

---

### The Problems They Hired Me to Solve

When I came in as a Data Analyst, ValueMart was facing three problems that were silently eating into their profits:

#### Problem 1: Random Shelf Placement Was Shrinking Basket Sizes

Products were placed on shelves without any strategy. Milk was in one corner, bread was three aisles away. Coca Cola and chips were in completely different sections. Nobody had ever asked: *Which products do customers usually buy together?*

**What this meant:** A customer coming in for bread might never walk past the butter aisle. A customer grabbing Coca Cola might not see the chips on the other side of the store. The store was unknowingly discouraging customers from buying complementary products — leaving money on the table with every transaction.

#### Problem 2: Promotions Ran Without Proof They Worked

ValueMart ran four major sales events every year — Easter, Independence Day, Black Friday, and Christmas. Each required:
- Extra staff hours
- Marketing materials and advertising
- Price discounts that cut into margins

After every promotion, the manager would say "I think it went well" or "seemed quieter than last year." But nobody could answer the basic question: *Did this promotion actually generate more sales than a regular day, or did we just discount products to customers who would have bought them anyway?*

**What this meant:** The store kept investing in promotions without knowing which ones delivered results. Maybe Black Friday was a goldmine while Easter Sale was losing money. Nobody knew.

#### Problem 3: Frequent Stockouts Were Bleeding Revenue

High-demand products like Milk, Bread, and Chicken regularly sold out before the next delivery. The reordering process was completely manual — someone walked the aisles, visually checked shelves, and estimated what to order. By the time a stockout was noticed, customers had already walked out empty-handed.

**What this meant:** Every time a customer came in for Milk and found an empty shelf, ValueMart didn't just lose the P28.50 Milk sale. They lost the entire shopping basket — bread, eggs, butter, everything. If just 5 customers a day left because of stockouts, that's over P180,000 in lost annual revenue.

---

### What I Discovered in Their Data

I analyzed 75,459 customer shopping baskets across a full year and found patterns the store never knew existed:

**Product Relationships Hidden in the Data:**
- **Milk + White Bread:** Bought together 65% of the time — the strongest relationship in the store
- **Coca Cola + Chips:** 55% association — but they were placed in different aisles
- **Chicken + Tomatoes + Onions:** 50% of chicken buyers also bought these vegetables — they should be in the same section
- **Tea + Milk + Biscuits:** 40% association — three products, three different aisles
- **Washing Powder + Dish Soap:** 35% association — household products that should be together

**Promotion Truth Revealed:**
- Black Friday was the star performer: **+40% sales lift** above normal days
- Easter Sale was disappointing: only **+18% lift** — barely covering the discount costs
- The average lift across all promotions was **+27%** — proving promotions work, but some work much better than others

**Inventory Risks Nobody Saw Coming:**
- **8 out of 27 products (30%)** were at risk of stocking out within a week
- Milk had only **3 days of stock left** but was selling 22 units per day
- White Bread had **4 days** remaining with 18 daily sales
- These patterns repeated every month because reordering wasn't based on actual sales data

---

### The Solutions I Built

I didn't just hand over a spreadsheet. I built two working tools the store can use every day.

#### Solution 1: Retail Analytics Dashboard

**An interactive tool that puts all store data in one place.**

Instead of guessing, the manager now opens one dashboard and sees:

- **Sales Overview** — Annual revenue, transaction count, average basket size, revenue by product category, daily sales trends
- **Market Basket Analysis** — The top 15 product pairs customers buy together, with clear explanations of what "65% confidence" and "2.85 lift" actually mean for the business
- **Promotion Effectiveness** — Sales lift for every promotional campaign, proving which events deliver the best return on investment
- **Inventory Alerts** — Red alert cards showing every product at risk of stocking out, sorted by urgency

**Real impact:** The manager now knows exactly which products to place together, which promotions are worth the investment, and which items need reordering today.

#### Solution 2: Retail Management System

**Daily operational tools for store staff.**

This system has two practical features used every morning:

**Automated Reorder Alerts:**
The system scans all 27 products and flags any item with less than 7 days of stock remaining. Instead of walking the aisles hoping to spot empty shelves, staff open this app and see exactly what to order. Red alerts show: product name, days of stock left, and recommended reorder quantity.

**Shelf Placement Recommendations:**
Based on the association rules discovered during analysis, the system suggests which products should be placed near each other. Staff can see recommendations like "Place Milk 2L near White Bread" and adjust shelf layout during restocking. No technical knowledge required — just follow the suggestions.

---

### The Results

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| Shelf Placement Strategy | Random, no data | 20+ product pairs identified | Data-driven merchandising |
| Promotion Measurement | None (guesswork) | Measured lift for 4 campaigns | Proven +27% avg ROI |
| Black Friday Performance | Unknown | +40% lift documented | Justified increased budget |
| Products at Stockout Risk | 8 items | ~6-7 items | 18% reduction |
| Reordering Process | Reactive (visual checks) | Proactive (7-day alerts) | Stockouts caught earlier |
| Decision Making | Gut feeling | Data-driven | Every decision has evidence |

**Financial Impact Summary:**

| Source | Annual Value |
|--------|-------------|
| Basket size increase (shelf optimization) | P330,000+ (estimated from pair placements) |
| Stockout prevention revenue saved | P78,840 (2 fewer lost baskets/day) |
| Promo budget optimization | Redirected spend from weak to strong campaigns |
| **Total Potential Annual Value** | **P400,000+** |

---

### The Skills This Project Demonstrates

- Market Basket Analysis & Association Rule Mining
- Retail transaction data analysis
- Promotion effectiveness measurement
- Inventory optimization
- KPI dashboard development
- Business-facing operational tools
- Translating complex analytics into business recommendations

---

### Project Files

| File | What It Contains |
|------|-----------------|
| `transactions.csv` | 264,129 transaction line items across 75,459 customer baskets |
| `product_catalog.csv` | 27 products with categories and prices |
| `inventory_levels.csv` | Stock levels, sales rates, and stockout risk assessment |
| `association_rules.csv` | Top product pairs with lift, confidence, and support metrics |
| `promo_effectiveness.csv` | Sales lift data for all promotional campaigns |
| `category_performance.csv` | Revenue breakdown by product category |
| `03_dashboard.py` | The management dashboard application |
| `04_software.py` | The retail operations system |

---


*This project uses synthetic data generated for demonstration purposes. ValueMart Supermarket is a fictional business created for this portfolio project. The analytical approach, problem-solving methodology, and technical implementation are entirely real.*
