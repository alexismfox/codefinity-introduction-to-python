# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for product_name, revenue in sorted(revenues):
        print(f"{product_name} has total revenue of ${revenue}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]      # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Task 3: Calculate revenue and Task 4: pair products with their revenues
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))

# Task 5: Print formatted, sorted output
formatted_output(revenue_per_product)