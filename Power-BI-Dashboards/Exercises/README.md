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

### 📘 Course 3: Data Visualisation in Power BI (In Progress 🔄)
*   **Overview:** Advanced visual storytelling, layout design, user-centric report structuring, and custom charting in Power BI.
*   **Progress:**
    *   **Chapter 1:** *[Notes & Exercises to be added]*
    *   **Chapter 2:** *[Notes & Exercises to be added]*
    *   **Chapter 3:** *[Upcoming]*
    *   **Chapter 4:** *[Upcoming]*
