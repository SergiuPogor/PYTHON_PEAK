# Function to sum values from a list of dictionaries
def sum_dict_values(data, key):
    return sum(item[key] for item in data)

# Function to sum attribute values of custom objects
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"

def sum_product_prices(products):
    return sum(product.price for product in products)

def main():
    # Example data: list of dictionaries
    sales_data = [
        {"item": "Laptop", "amount": 1200},
        {"item": "Mouse", "amount": 25},
        {"item": "Keyboard", "amount": 75}
    ]
    
    # Calculate total sales amount
    total_sales = sum_dict_values(sales_data, 'amount')
    print("Total sales amount:", total_sales)
    
    # Example data: list of Product objects
    products = [
        Product("Laptop", 1200),
        Product("Mouse", 25),
        Product("Keyboard", 75)
    ]
    
    # Calculate total price of all products
    total_price = sum_product_prices(products)
    print("Total price of products:", total_price)

if __name__ == "__main__":
    main()
