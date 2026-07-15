# Power BI & DAX Course Exercises 📊

This folder houses the hands-on exercises, dashboard files (`.pbix`), and key insights from my completed Power BI learning path.

---

## 🎓 Completed Courses

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

#### 1. Calculated Columns vs. Measures
*   **Business Context:** Adventure Works Cycles wanted to understand their yearly profitability and order trends.
*   **Profit Column (Calculated Column):** Created a column to calculate gross profit per transaction:
    ```dax
    Profit = Sales[Line Price] - Sales[Line Cost]
    ```
    *Insight:* Verified that Adventure Works gained **`$4.44Bn`** in total profits for the year 2019.
*   **Sales Count (Measure):** Implemented a transaction counter to identify order velocity:
    ```dax
    Sales Count = COUNT(Sales[SalesOrderNumber])
    ```
    *Insight:* Found that **May 2020** represented the highest single sales velocity period.
*   **Profit Margin Ratio (Measure):** Created a core metric comparing profit against revenue using safe division:
    ```dax
    Profit Margin Ratio = DIVIDE([Total Profit], [Total Sales])
    ```
    *Insight:* Identified **2019** as the year with the highest profit margin percentage.

#### 2. Evaluation Context & Iterators
*   **Row Context:** Iterating calculations row-by-row (implicit in calculated columns; explicit in iterators).
*   **Filter Context:** Evaluating aggregates based on active filters (slicers, visual placement, or pane selection).
*   **Iterator Functions (`SUMX`, `AVERAGEX`):** Used to perform row-by-row computations over a table before aggregating:
    *   Designed `AvgProfit` using `AVERAGE()` and compared it to `AvgProfit_X` using `AVERAGEX(Sales, Sales[Profit])` via a clustered column chart to confirm matching distribution behaviors.

#### 3. Advanced Context Modification (`CALCULATE` & Variables)
*   **Variables (`VAR` / `RETURN`):** Implemented variables to compute inflation adjustments cleanly without hardcoding values multiple times:
    ```dax
    TotalSales_w_increase = 
    VAR increase = 0.05
    RETURN '_Calculations'[TotalSales] + ('_Calculations'[TotalSales] * increase)
    ```
    *Insight:* Projected adjusted sales of **`$31M`** (a 5% increase over the baseline **`$29M`**).
*   **Filter Overriding (`CALCULATE`):** Used `CALCULATE` to evaluate transactions under specific dimensions:
    ```dax
    2018_Bike_revenue = 
    CALCULATE(
        SUM(Sales[Line Price]),
        Sales[Product Category] = "Bikes",
        YEAR(Sales[OrderDate]) = 2018
    )
    ```
    *Insight:* Analyzed category performance where Bikes accounted for a specific **`3%`** proportion.

#### 4. Time Intelligence & Calendar Dimensions
*   **Date Tables (`CALENDAR` / `CALENDARAUTO`):** Created dedicated date tables to support time intelligence functions (such as `LASTDATE` and `DATESBETWEEN`):
    ```dax
    DateTable = CALENDARAUTO(12)
    ```
*   **Logistics Lag (`DATEDIFF`):** Calculated delivery duration timelines from order placement to customer receipt:
    ```dax
    Delivery_Lag = DATEDIFF(Sales[OrderDate], Sales[DeliveryDate], DAY)
    ```
    *Insight:* Uncovered an average delivery shipping lag of **`7.47 days`**.
*   **Quick Measures:** Constructed Quarter-over-Quarter percentage change metrics for `TotalSales` over consecutive periods.
