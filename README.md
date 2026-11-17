# Task_03---Business-Intelligence-Dashboard

## Project Overview

This project focuses on **Exploratory Data Analysis (EDA), Business Performance Analysis, Data Visualization, and Sales Forecasting** using the Superstore dataset.

The objective is to analyze sales, profit, customer segments, product performance, regional performance, and shipping operations to extract meaningful business insights. It also uses a **Linear Regression model** to forecast sales for the next 12 months.

## Project Objectives

- Analyze overall business performance using key performance indicators (KPIs).
- Identify sales and profit trends over time.
- Evaluate product, category, and sub-category performance.
- Analyze sales and profitability across different regions and states.
- Understand customer segment performance.
- Investigate the impact of discounts on profitability.
- Evaluate shipping performance and delivery duration.
- Perform correlation analysis between numerical variables.
- Build a Linear Regression model for sales forecasting.
- Export cleaned data and business analysis results.

## Technologies & Libraries

The project uses the following tools and Python libraries:

- **Python** – Programming language
- **Pandas** – Data cleaning, manipulation, and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Scikit-learn** – Machine learning and sales forecasting
- **Excel** – Exporting business analysis results

## Project Structure

```text
Superstore-Sales-Analysis/
│
├── Dataset/
│   ├── Sample - Superstore.csv
│   ├── Cleaned_Superstore.csv
│   └── Business_Analysis_Results.xlsx
│
├── superstore_analysis.py
│
└── README.md
```

## Project Workflow

### 1. Data Loading and Exploration
- Load the Superstore dataset using Pandas.
- Display the first five records.
- Examine dataset structure and dimensions.
- Check missing values and duplicate records.

### 2. Data Cleaning and Feature Engineering
- Convert Order Date and Ship Date into datetime format.
- Extract Order Year and Order Month.
- Calculate Shipping Days.
- Calculate Profit Margin.

### 3. Business KPI Analysis

Calculate important business metrics:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value (AOV)
- Overall Profit Margin

### 4. Exploratory Data Analysis (EDA)

Perform detailed analysis of:

- Monthly Sales Trends
- Monthly Profit Trends
- Sales by Category
- Profit by Category
- Sales by Region
- Profit by Region
- Sales by Customer Segment
- Profit by Customer Segment
- Top 10 Products by Sales
- Top 10 Customers by Sales
- Sales by Shipping Mode
- Sales and Profit by Sub-Category
- Top 10 Products by Profit
- Bottom 10 Products by Profit
- Sales by State

### 5. Business Performance Analysis

Additional business analysis includes:

- Yearly Sales Growth
- Customer Segment Analysis
- Discount Impact Analysis
- Shipping Performance Analysis
- Profit Margin by Category
- Correlation Analysis

### 6. Data Visualization

Matplotlib is used to create visualizations, including:

- Line Charts
- Bar Charts
- Horizontal Bar Charts
- Scatter Plots

These visualizations help identify business trends, patterns, and relationships.

### 7. Sales Forecasting

A Linear Regression model from Scikit-learn is used to forecast future sales.

**Steps:**
1. Aggregate sales data monthly.
2. Create a numerical time-based feature.
3. Train a Linear Regression model.
4. Predict sales for the next 12 months.
5. Visualize historical sales against predicted sales.
6. Evaluate model performance using:
   - Mean Absolute Error (MAE)
   - R² Score

### 8. Export Results

The project generates two output files:

- `Cleaned_Superstore.csv` – Contains the cleaned dataset with additional engineered features.
- `Business_Analysis_Results.xlsx` – Contains multiple sheets with business analysis results.

## Key Business Metrics

The following KPIs are calculated:

| KPI | Description |
|---|---|
| Total Sales | Sum of all sales |
| Total Profit | Sum of all profit |
| Total Orders | Unique order count |
| Total Customers | Unique customer count |
| Average Order Value | Total Sales / Total Orders |
| Profit Margin | Total Profit / Total Sales × 100 |

## Machine Learning Model

**Algorithm:** Linear Regression

**Prediction Target:** Monthly Sales

**Forecast Period:** Next 12 Months

**Evaluation Metrics:**
- Mean Absolute Error (MAE)
- R² Score

The model uses monthly sales history and a numerical month index to identify a linear trend and generate future sales predictions.

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Superstore-Sales-Analysis.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Superstore-Sales-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib scikit-learn openpyxl
```

### Step 4: Add the Dataset

Place the original Superstore CSV file inside the `Dataset` folder:

```text
Dataset/Sample - Superstore.csv
```

### Step 5: Run the Python Script

```bash
python superstore_analysis.py
```

The script will display analysis results, generate visualizations, export the cleaned dataset, and save business analysis results in Excel format.

## Model Evaluation

The forecasting model is evaluated using:

- **MAE:** Measures the average absolute difference between actual and predicted sales.
- **R² Score:** Measures how well the model explains variation in historical sales.

Actual evaluation results are printed when the script runs.

## Conclusion

This project demonstrates how Python can be used to transform raw business data into meaningful insights.

By combining data cleaning, exploratory data analysis, business KPI calculations, visualization, and machine learning, the project provides a structured approach to understanding business performance and forecasting future sales.

## Author

**Sidra Maqsood**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Data Visualization | Machine Learning

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
