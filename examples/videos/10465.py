from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def context_dependent_logger(log_level="info"):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_msg = f"{func.__name__} called with result: {result}"
            if log_level == "info":
                logger.info(log_msg)
            elif log_level == "warning":
                logger.warning(log_msg)
            else:
                logger.error(log_msg)
            return result
        return wrapper
    return log_decorator

@context_dependent_logger(log_level="warning")
def calculate_area(radius):
    return 3.14159 * radius ** 2

@context_dependent_logger(log_level="error")
def divide(a, b):
    if b == 0:
        return "Division by zero error!"
    return a / b

# Test context-aware logging behavior
calculate_area(10)
divide(20, 0)

# Context-dependent pricing logic based on time of day
def time_based_discount(func):
    def wrapper(*args, **kwargs):
        current_hour = datetime.now().hour
        discount = 0.8 if 9 <= current_hour < 17 else 1.0
        result = func(*args, **kwargs)
        return result * discount
    return wrapper

@time_based_discount
def calculate_price(base_price):
    return base_price

# Test the dynamic discounting function
print("Price with context-based discount:", calculate_price(100))

# Context-based retry mechanism for unreliable network API calls
import requests
from time import sleep

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    logger.warning(f"Attempt {attempts + 1} failed: {e}")
                    attempts += 1
                    sleep(delay)
            return "Failed after multiple retries."
        return wrapper
    return decorator

@retry_on_failure(retries=5, delay=1)
def fetch_data(url):
    response = requests.get(url, timeout=1)
    response.raise_for_status()
    return response.json()

# Example with context-sensitive function retries
url = "https://api.example.com/data"
fetch_data(url)