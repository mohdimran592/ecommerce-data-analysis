import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_excel('practice3.xlsx')
df['Order_Date'] = pd.to_datetime(df['Order_Date'],format='mixed',errors='coerce')

# ========================== SALES ANALYSIS ==========================

total_sales = df['Net_Sales'].sum()
total_quantity = df['Quantity'].sum()
total_discount = df['Discount_Amount'].sum()
total_orders = df['Order_ID'].nunique()
total_customer = df['Customer_ID'].nunique()

# average order
aov = total_sales / total_orders

# Monthly sales and month-over-month change
df['Month'] = df['Order_Date'].dt.to_period('M')

month_wise_sales = (
    df.groupby('Month')['Net_Sales']
      .sum()
      .sort_index()
      .to_frame()
)
month_wise_sales['MoM_%'] = month_wise_sales['Net_Sales'].pct_change() * 100

product_wise_sales = (
    df.groupby('Product')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)

category_wise_sales = (
    df.groupby('Category')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)

city_wise_sales = (
    df.groupby('City')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)

segment_wise_sales = (
    df.groupby('Segment')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)

payment_method_wise_sales = (
    df.groupby('Payment_Method')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)


# ========================== PRODUCT ANALYSIS ==========================

product_wise_profit = (
    df.groupby('Product')['Profit']
      .sum()
      .sort_values(ascending=False)
)

# Average discount rate by product
product_average_discount = (
    df.groupby('Product')['Discount']
      .mean()
      .sort_values(ascending=False)
)

# Discount amount by product
product_wise_discount_amount = (
    df.groupby('Product')['Discount_Amount']
      .sum()
      .sort_values(ascending=False)
)

product_wise_quantity = (
    df.groupby('Product')['Quantity']
      .sum()
      .sort_values(ascending=False)
)

product_wise_orders = df.groupby('Product')['Order_ID'].nunique()

product_aov = (
    df.groupby('Product')['Net_Sales'].sum()
    / product_wise_orders
)

product_contribution = (
    df.groupby('Product')['Net_Sales'].sum()
    / total_sales
    * 100
)

product_average_price = (
    df.groupby('Product')['Net_Sales'].sum()
    / product_wise_quantity
)

product_highest = product_wise_sales.head(1)
product_lowest = product_wise_sales.tail(1)


# ========================== CUSTOMER ANALYSIS ==========================

customer_sales = (
    df.groupby('Customer_ID')['Net_Sales']
      .sum()
      .sort_values(ascending=False)
)

customer_profit = (
    df.groupby('Customer_ID')['Profit']
      .sum()
      .sort_values(ascending=False)
)

customer_quantity = (
    df.groupby('Customer_ID')['Quantity']
      .sum()
      .sort_values(ascending=False)
)

customer_discount = (
    df.groupby('Customer_ID')['Discount_Amount']
      .sum()
      .sort_values(ascending=False)
)

customer_orders = df.groupby('Customer_ID')['Order_ID'].nunique()

customer_aov = (
    df.groupby('Customer_ID')['Net_Sales'].sum()
    / customer_orders
)

customer_contribution = (
    df.groupby('Customer_ID')['Net_Sales'].sum()
    / total_sales
    * 100
)

customer_highest = customer_sales.head(1)
customer_lowest = customer_sales.tail(1)


# ========================== PRINT RESULTS ==========================

print('\n=== SALES PERFORMANCE ANALYSIS ===')
print(f'Total sales: {total_sales:,.2f}')
print(f'Total quantity: {total_quantity:,.0f}')
print(f'Total orders: {total_orders:,}')
print(f'Total customers: {total_customer:,}')
print(f'Total discount amount: {total_discount:,.2f}')
print(f'Average order value: {aov:,.2f}')

print('\nTop 5 products by sales:')
print(product_wise_sales.head(5))

print('\nTop 5 customers by sales:')
print(customer_sales.head(5))

print('\nCategory sales:')
print(category_wise_sales)

print('\nMonthly sales and MoM change:')
print(month_wise_sales)

print('\nSegment sales:')
print(segment_wise_sales)

print('\nPayment method sales:')
print(payment_method_wise_sales)


print('\n=== PRODUCT ANALYSIS ===')
print('Top 5 products by sales:')
print(product_wise_sales.head(5))

print('\nTop 5 products by quantity:')
print(product_wise_quantity.head(5))

print('\nTop 5 products by profit:')
print(product_wise_profit.head(5))

print('\nTop 5 products by discount amount:')
print(product_wise_discount_amount.head(5))

print('\nProduct AOV:')
print(product_aov.sort_values(ascending=False))

print('\nProduct sales contribution (%):')
print(product_contribution.sort_values(ascending=False))

print('\nProduct average selling price:')
print(product_average_price.sort_values(ascending=False))

print('\nAverage discount by product:')
print(product_average_discount)

print('\nHighest-sales product:')
print(product_highest)

print('\nLowest-sales product:')
print(product_lowest)


print('\n=== CUSTOMER ANALYSIS ===')
print('Top 5 customers by sales:')
print(customer_sales.head(5))

print('\nTop 5 customers by quantity:')
print(customer_quantity.head(5))

print('\nTop 5 customers by profit:')
print(customer_profit.head(5))

print('\nTop 5 customers by discount amount:')
print(customer_discount.head(5))

print('\nCustomer orders:')
print(customer_orders)

print('\nCustomer AOV:')
print(customer_aov.sort_values(ascending=False))

print('\nCustomer sales contribution (%):')
print(customer_contribution.sort_values(ascending=False))

print('\nHighest-sales customer:')
print(customer_highest)

print('\nLowest-sales customer:')
print(customer_lowest)