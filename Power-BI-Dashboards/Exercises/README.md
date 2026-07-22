# Power BI & DAX Course Exercises 📊

This folder houses the hands-on exercises, dashboard files (`.pbix`), and key insights from my completed Power BI learning path.

---

## 🎓 Course Logs

### 📘 Course 1: Introduction to Power BI (Completed ✅)
*   **Overview:** Foundational skills for importing, transforming, modeling, and visualizing data inside Power BI Desktop.
*   **Chapters & Completed Work:**
    *   **Chapter 1: Getting Started with Power BI**
        *   `Columns in Power BI.pbix` - Analyzed sales volumes for Worldwide Importers and discovered chilled products sales began in **2016**.
        *   `Tables in Power BI.pbix` - Formatted tables and matrices with conditional formatting. Verified **Sophia Hinton** generated **`$309,004.06`** in 2016.
    *   **Chapter 2: Transforming Data**
        *   Utilized **Power Query Editor** to clean, shape, reshape, change data types, and manage null values in raw data. Cleaned data anomalies (`?` and `-` symbols) in `Credit Limit` column. Found cheapest transaction for **Tailspin Toys** was **`$5.52`**.
    *   **Chapter 3: Visualizing Data**
        *   Built standard visualizations (bar charts, line charts, cards, treemaps) and applied dashboard design best practices. Verified total forecasted sales of **`$18.13bn`** and Cell Phones budget of **`$1,208,041,332.59`**.
    *   **Chapter 4: Filtering & Interactions**
        *   Configured visual-level, page-level, and report-level filters and managed visual cross-filtering behaviors (card budget value resolved to **`$17.17bn`**). Visualized Top 5 stores: **Contoso North America Reseller** ranked 5th.

---

### 📘 Course 2: Introduction to DAX (Completed ✅)
*   **Overview:** Mastering Data Analysis Expressions (DAX) to build custom calculations, measures, and data models in Power BI.
*   **Key Concepts & Skills Learned:**
    *   **Calculated Columns vs. Measures:** Understanding when to pre-calculate values row-by-row (`Profit = Sales[Line Price] - Sales[Line Cost]`, Adventure Works gained **`$4.44Bn`** in 2019) vs. calculating aggregates dynamically on the fly (`Sales Count = COUNT(Sales[SalesOrderNumber])`, peak in **May 2020**).
    *   **Evaluation Context:** Row Context (current row iteration) and Filter Context (active filters on the report page).
    *   **Variables (`VAR` / `RETURN`):** Used to calculate inflation adjustments cleanly (projected sales of **`$31M`** vs. baseline of **`$29M`**).
    *   **DAX Functions Mastered:**
        *   *Filter Control:* `CALCULATE` (e.g. `2018_Bike_revenue`), `FILTER`, `ALL`.
        *   *Safe Division:* `DIVIDE` (Profit Margin Ratio).
        *   *Time Intelligence:* `CALENDARAUTO(12)` for date dimensions, and `DATEDIFF` for delivery shipping lag (**`7.47 days`** average).

---

### 📘 Course 3: Data Visualisation in Power BI (Completed ✅)
*   **Overview:** Advanced visual storytelling, executive report structuring, cognitive load optimization, and custom charting in Power BI Desktop for *Threads Ltd.*
*   **Core Concepts:**
    *   **Less is More & Cognitive Load:** Reducing visual clutter, balancing information-rich visuals with negative space, and using color as a pre-attentive emphasis attribute.
    *   **Dashboards vs. Paginated Reports:** Distinguishing single-pane-of-glass real-time operational views from pixel-perfect, multi-page printable reports.

#### 📂 Chapter 1: The Audience is King (Audience-Driven Design)
*   **Target Stakeholder:** Head of Sales at Threads Ltd.
*   **Exercise 1: Granular Order Detail Table & Slicers**
    *   *Visuals:* Data table (`Product SKU`, `Order ID`, `Order Quantity`, `Sales Amount`) paired with Year and Product Name dropdown slicers.
    *   *Key Insight:* Identified that Order ID **`6160`** generated the highest sales amount for **Aero Daily Fitness Tee** at **`€1,200,000`**.
*   **Exercise 2: Sales vs. COGS Scatter Plot**
    *   *Business Context:* Investigating the relationship between Sales Revenue and Cost of Goods Sold (COGS) to track gross profit trends over time.
    *   *Key Insight:* Discovered that the peak single-day sales volume during 2020–2021 occurred on **Friday, March 26, 2021** reaching **`€19,218`**.
*   **Exercise 3: Multi-Dimensional Bubble Chart**
    *   *Business Context:* Evaluating product price vs. sales amount vs. order volume to inform catalog expansion for "Tank Tops".
    *   *Setup:* X-axis = `SUM(Sales Amount)`, Y-axis = `Average Product Price`, Size = `SUM(Order Quantity)`.
    *   *Key Insight:* For the product with the highest average price (**`€21.5`**), total order quantity reached **`262`** units.

#### 📂 Chapter 2: Getting An Emotional Response (Formatting & Visual Hierarchy)
*   **Target Stakeholder:** Product Manager at Threads Ltd.
*   **Exercise 1: Channel-Filtered Clustered Bar Chart**
    *   *Setup:* Product Sales Amount by Product Name, filtered to `Product Gender = Women`, `Year = 2021`, `Channel = Supermarket`.
    *   *Key Insight:* **Hera Pullover Hoodie** generated the highest total sales volume for women's products in supermarkets at **`€11k`**.
*   **Exercise 2: Analytics Pane Constant Lines (`Product Comparison`)**
    *   *Technique:* Applied an **Ideal Sales Amount** constant reference line to benchmark catalog items visually.
    *   *Key Insight:* **Troy Yoga Short** fell just below the target ideal sales threshold line.
*   **Exercise 3: Stacking Variables across Distribution Channels**
    *   *Visual:* Stacked Bar Chart tracking total order quantities by channel and product categories.
    *   *Key Insight:* The **Franchise** channel processed the largest volume of orders overall.
*   **Exercise 4: Small Multiples for Multi-Dimensional Comparisons**
    *   *Technique:* Used Small Multiples to compare Hoodies & Sweatshirts sales by color and clothing gender for Franchise outlets without creating multiple separate charts.
    *   *Key Insight:* Identified **Blue, Men** as the top-performing gender and color combination for Franchise orders in 2021.

#### 📂 Chapter 3: Reducing Cognitive Load (Executive Reporting)
*   **Target Stakeholder:** Chief Commercial Officer (CCO) at Threads Ltd.
*   **Exercise 1: Financial Trend Line & Area Charts**
    *   *Business Context:* Tracking Revenue, COGS, and Gross Profit over time.
    *   *Key Insight:* Peak gross profit over the 4-year period occurred in **March 2018** reaching **`€107,691.49`**.
*   **Exercise 2: Rate vs. Count Combination Charts (Combo Charts)**
    *   *Technique:* Comparing counting variables (Gross Profit) against rate variables (Gross Profit Margin %) on a dual-axis visual.
    *   *Key Insight:* In **March 2019**, the average profit margin for Tank Tops reached its peak at **`58.94%`**.

#### 📂 Chapter 4: Less is More (Target Tracking & Executive Design)
*   **Target Stakeholder:** Executive Leadership & CCO at Threads Ltd.
*   **Exercise 1: Shares of the Whole (Pie Chart vs. Treemap)**
    *   *Technique:* Compared static pie charts vs. hierarchical treemaps for order quantities across retail channels.
    *   *Key Insight:* Medium (**'M'**) sized products ordered from **Small Chain Stores** reached **`352`** units.
*   **Exercise 2: Gauges & Custom KPI Card Thresholds**
    *   *Technique:* Configured a Gauge visual with a company target profit margin of **70%** (`0.70`), and created measures `Orders Above Target Profit Margin` and `Orders Below Target Profit Margin`.
    *   *Key Insight:* Comparing "Tees" sales in 2020 vs. 2021, **2020** recorded a higher number of orders exceeding the target profit margin.
*   **Exercise 3: Executive Key Performance Indicators (KPI Visuals)**
    *   *Business Context:* Monitoring total orders and order return variance against organizational benchmarks.
    *   *Key Insight:* Total order fulfillment volume underperformed against the executive target by **`-21.67%`**.
