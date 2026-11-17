import pandas as pd
import matplotlib.pyplot as plt

# Load Superstore dataset
df = pd.read_csv("Dataset/Sample - Superstore.csv", encoding="cp1252")

# Display first five rows
print(df.head())

# Display dataset information
print(df.info())

# Display number of rows and columns
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Convert date columns into datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%m/%d/%Y"
)

# Verify date types
print("\nUpdated Data Types:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Feature Engineering

# Extract year from Order Date
df["Order Year"] = df["Order Date"].dt.year

# Extract month from Order Date
df["Order Month"] = df["Order Date"].dt.month

# Calculate shipping duration
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Calculate profit margin
df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
) * 100

# Display new columns
print("\nFeature Engineering Results:")
print(df[[
    "Order Year",
    "Order Month",
    "Shipping Days",
    "Profit Margin"
]].head())

print("\nUpdated Dataset Shape:")
print(df.shape)

# Business KPI Analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n========== BUSINESS KPIs ==========")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# Monthly Sales Trend

monthly_sales = df.set_index("Order Date").resample("ME")["Sales"].sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Sales by Category

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Profit by Category

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Sales by Region

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Profit by Region

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Sales by Segment

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Profit by Segment

segment_profit = df.groupby("Segment")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
segment_profit.plot(kind="bar")

plt.title("Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Top 10 Products by Sales

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.tight_layout()
plt.show()

# Top 10 Customers by Sales

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_customers.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

plt.tight_layout()
plt.show()

# Sales by Ship Mode

ship_mode_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
ship_mode_sales.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Shipping Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Sales by Sub-Category

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 7))
subcategory_sales.plot(kind="barh")

plt.title("Sales by Sub-Category")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.show()

# Profit by Sub-Category

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 7))
subcategory_profit.plot(kind="barh")

plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.show()

# Monthly Profit Trend

monthly_profit = df.set_index("Order Date").resample("ME")["Profit"].sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_profit.index, monthly_profit.values)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Discount vs Profit

plt.figure(figsize=(10, 6))

plt.scatter(df["Discount"], df["Profit"], alpha=0.5)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()

# Sales vs Profit

plt.figure(figsize=(10, 6))

plt.scatter(df["Sales"], df["Profit"], alpha=0.5)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()

# Business Insights: Sub-Category Performance

subcategory_performance = (
    df.groupby("Sub-Category")[["Sales", "Profit"]]
    .sum()
    .sort_values(by="Profit", ascending=False)
)

print("\n========== SUB-CATEGORY PERFORMANCE ==========")
print(subcategory_performance)

print("\nMost Profitable Sub-Category:")
print(subcategory_performance["Profit"].idxmax())

print("\nLeast Profitable Sub-Category:")
print(subcategory_performance["Profit"].idxmin())

# Top 10 Products by Profit

top_products_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")
print(top_products_profit)

# Bottom 10 Products by Profit

bottom_products_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print("\n========== BOTTOM 10 PRODUCTS BY PROFIT ==========")
print(bottom_products_profit)

# Yearly Sales Growth

yearly_sales = df.groupby("Order Year")["Sales"].sum()

yearly_growth = yearly_sales.pct_change() * 100

print("\n========== YEARLY SALES ==========")
print(yearly_sales.round(2))

print("\n========== YEARLY SALES GROWTH ==========")
print(yearly_growth.round(2))

# Sales by State

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== TOP 10 STATES BY SALES ==========")
print(state_sales.head(10).round(2))

print("\n========== BOTTOM 10 STATES BY SALES ==========")
print(state_sales.tail(10).round(2))

# Customer Segment Analysis

customer_analysis = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique"),
    Total_Customers=("Customer ID", "nunique")
)

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")
print(customer_analysis.round(2))

# Discount Impact Analysis

discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Average_Profit=("Profit", "mean"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
)

print("\n========== DISCOUNT IMPACT ANALYSIS ==========")
print(discount_analysis.round(2))

# Shipping Performance Analysis

shipping_analysis = df.groupby("Ship Mode").agg(
    Average_Shipping_Days=("Shipping Days", "mean"),
    Total_Orders=("Order ID", "nunique"),
    Total_Sales=("Sales", "sum")
)

print("\n========== SHIPPING PERFORMANCE ==========")
print(shipping_analysis.round(2))

# Profit Margin by Category

category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

category_analysis["Profit_Margin"] = (
    category_analysis["Total_Profit"] /
    category_analysis["Total_Sales"]
) * 100

print("\n========== PROFIT MARGIN BY CATEGORY ==========")
print(category_analysis.round(2))

# Correlation Analysis

correlation = df[
    ["Sales", "Profit", "Quantity", "Discount"]
].corr()

print("\n========== CORRELATION ANALYSIS ==========")
print(correlation.round(2))

# Export Cleaned Dataset

df.to_csv("Dataset/Cleaned_Superstore.csv", index=False)

print("\nCleaned dataset exported successfully!")

# Export Business Analysis Results to Excel

with pd.ExcelWriter("Dataset/Business_Analysis_Results.xlsx") as writer:

    category_analysis.to_excel(writer, sheet_name="Category Analysis")
    region_sales.to_excel(writer, sheet_name="Region Sales")
    region_profit.to_excel(writer, sheet_name="Region Profit")
    segment_sales.to_excel(writer, sheet_name="Segment Sales")
    subcategory_performance.to_excel(writer, sheet_name="Subcategory")
    yearly_sales.to_excel(writer, sheet_name="Yearly Sales")
    customer_analysis.to_excel(writer, sheet_name="Customer Analysis")
    discount_analysis.to_excel(writer, sheet_name="Discount Analysis")
    shipping_analysis.to_excel(writer, sheet_name="Shipping Analysis")
    correlation.to_excel(writer, sheet_name="Correlation")

print("\nBusiness analysis results exported successfully!")

# Sales Forecasting - Prepare Monthly Data

monthly_data = (
    df.set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
    .reset_index()
)

monthly_data.columns = ["Date", "Sales"]

# Create time-based feature
monthly_data["Month_Number"] = range(len(monthly_data))

print("\n========== MONTHLY SALES DATA ==========")
print(monthly_data.head())

print("\nTotal Months:", len(monthly_data))

# Train Linear Regression Model

from sklearn.linear_model import LinearRegression

# Prepare input and output
X = monthly_data[["Month_Number"]]
y = monthly_data["Sales"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

print("\n========== MODEL TRAINING ==========")
print("Model trained successfully!")
print("Model Coefficient:", model.coef_[0])
print("Model Intercept:", model.intercept_)

# Predict Sales for Next 12 Months

import numpy as np

future_months = np.arange(48, 60).reshape(-1, 1)

future_sales = model.predict(future_months)

forecast = pd.DataFrame({
    "Month_Number": range(48, 60),
    "Predicted_Sales": future_sales
})

print("\n========== NEXT 12 MONTHS SALES FORECAST ==========")
print(forecast.round(2))

# Historical vs Predicted Sales

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_data["Date"],
    monthly_data["Sales"],
    label="Historical Sales"
)

future_dates = pd.date_range(
    start="2018-01-31",
    periods=12,
    freq="ME"
)

plt.plot(
    future_dates,
    future_sales,
    label="Predicted Sales",
    linestyle="--"
)

plt.title("Superstore Sales Forecast - Next 12 Months")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# Evaluate Sales Forecasting Model

from sklearn.metrics import mean_absolute_error, r2_score

predicted_historical_sales = model.predict(X)

mae = mean_absolute_error(y, predicted_historical_sales)
r2 = r2_score(y, predicted_historical_sales)

print("\n========== MODEL EVALUATION ==========")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 4))

