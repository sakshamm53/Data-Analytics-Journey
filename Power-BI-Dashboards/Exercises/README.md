# Power BI Practice Log & Insights 📊

This log contains detailed summaries of the exercises, techniques, and key analytical findings from my completion of the **Introduction to Power BI** course. 

---

## 📂 Chapter 1: Getting Started with Power BI

### 1. Data Modeling & Slicer Interactions (`Columns in Power BI.pbix`)
*   **Business Context:** Worldwide Importers (WWI) sells dry and chilled goods (requiring specialized packaging). The objective was to analyze sales volumes and understand salesperson performance.
*   **Techniques Applied:**
    *   **Data Modeling:** Established a relationship between `FactSales[Invoice Date Key]` and `DimDate[Date]`.
    *   **Relationship Mapping:** Connected `FactSales[Salesperson Key]` to `DimEmployee[Employee Key]`.
    *   **Interactive Slicers:** Added an Employee slicer and formatted it as a dropdown visual.
*   **Key Insights:**
    *   **Chilled vs. Dry Sales Trend:** Uncovered that WWI **only started selling chilled items in 2016**; prior to 2016, sales consisted entirely of dry goods.
    *   **Salesperson Performance:** Sliced performance for salesperson **Taj Shand** to isolate specific sales patterns in the year 2014.

### 2. Transaction Detail Tables (`Tables in Power BI.pbix`)
*   **Business Context:** Creating detailed transactional views that dynamically react to page filters for granular sales auditing.
*   **Techniques Applied:** Added a details table with conditional formatting, synced with date and customer slicers.
*   **Key Insights:**
    *   **Auditing Specific Metrics:** Verified that salesperson **Sophia Hinton** generated a total sales volume (including tax) of **`$309,004.06`** in 2016.

---

## 📂 Chapter 2: Transforming Data (Power Query Editor)

### 1. Data Cleaning & Transformation Before Load
*   **Techniques Applied:**
    *   Removed irrelevant leading rows and promoted the correct row to headers.
    *   Built and tracked a **6-step data transformation pipeline** inside Power Query Editor.

### 2. Customer Aggregation & Clustered Visuals
*   **Business Context:** Finding buying groups and analyzing transaction minimums.
*   **Techniques Applied:**
    *   Ingested and cleaned `DimCustomer`.
    *   Created a clustered column chart plotting buying groups (`DimCustomer`) against `Total Including Tax` (`FactSale`).
    *   Changed the default aggregation of the numerical field to **Minimum** to analyze baseline ticket values.
*   **Key Insights:**
    *   Identified that the cheapest transaction made by the **Tailspin Toys** buying group was **`$5.52`**.

### 3. Column Data Anomalies & Type Corrections
*   **Techniques Applied:**
    *   Cleaned anomalies (such as replacing `?` and `-` symbols) in the `Credit Limit` column inside Power Query.
    *   Converted columns to **Currency** data types in Table View for `Profit` and `Total Including Tax` to ensure correct monetary formatting (averaging **`$865.82`** in total sales per ticket).

### 4. Geographic Data & Map Visualizations
*   **Business Context:** Identifying state-level profitability where standard bar charts become too cluttered.
*   **Techniques Applied:**
    *   Loaded `DimCity` and mapped the `State Province` column to the geographic **State or Province** category.
    *   Rendered a map visualization tracking average profit.
*   **Key Insights:**
    *   Identified that **Washington** generated the highest average profit for customer **Wing Tip Toys** at **`$465.47`**.

---

## 📂 Chapter 3: Visualizing Data

### 1. Visual Selection & Hierarchical Treemaps
*   **Techniques Applied:**
    *   Converted a standard Donut Chart into a **Treemap** to display product category proportions more clearly.
    *   Converted standard Cards to a **Multi-row Card** to compare forecasted vs. budgeted sales values.
*   **Key Insights:**
    *   Determined that the **Total Forecasted Sales Amount** across the dataset is **`$18.13bn`**.

### 2. Grid Structuring & Summary Matrices
*   **Techniques Applied:** Converted a detailed Table visual into a summarized **Matrix** to improve readability.
*   **Key Insights:**
    *   Summarized the budget amount for the **Cell Phones** category to be exactly **`$1,208,041,332.59`**.

---

## 📂 Chapter 4: Filtering & Interactions

### 1. Turning Off Cross-Filtering Interactions
*   **Business Context:** Ensuring high-level KPI cards (Actual, Forecast, Budget) remain static to show overall totals, even when a user filters other charts on the page.
*   **Techniques Applied:** Used **Edit Interactions** to disable cross-filtering on the KPI cards.
*   **Key Insights:**
    *   When cross-filtering is disabled, the Budget card maintains its static overall total of **`$17.17bn`** regardless of other visual selections.

### 2. Top-N Advanced Filtering
*   **Business Context:** Isolating the top-performing sales locations out of hundreds of entries.
*   **Techniques Applied:** Created a clustered bar chart and applied a visual-level **Top 5** filter sorted by sales amount.
*   **Key Insights:**
    *   Identified the top 5 stores. **Contoso North America Reseller** ranked as the **5th best performing store** overall.
