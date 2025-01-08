class DataValidationError(Exception):
    def __init__(self, message, field, expected_type, actual_value):
        super().__init__(message)
        self.field = field
        self.expected_type = expected_type
        self.actual_value = actual_value

    def __str__(self):
        return (f"{self.args[0]} | Field: '{self.field}', Expected Type: '{self.expected_type}', "
                f"Received: '{self.actual_value}' (type: {type(self.actual_value).__name__})")

def validate_user_data(user_data):
    if not isinstance(user_data.get("age"), int):
        raise DataValidationError("Invalid data type", field="age", expected_type="int", actual_value=user_data.get("age"))
    if not isinstance(user_data.get("email"), str) or "@" not in user_data["email"]:
        raise DataValidationError("Invalid email format", field="email", expected_type="str with '@'", actual_value=user_data.get("email"))

user_info = {"age": "twenty-five", "email": "useratexample.com"}

try:
    validate_user_data(user_info)
except DataValidationError as e:
    print("Data validation failed:", e)

# Real-world example: handling detailed errors in nested structures
def validate_order(order):
    required_fields = ["order_id", "customer_id", "items"]
    for field in required_fields:
        if field not in order:
            raise DataValidationError("Missing required field", field=field, expected_type="present", actual_value=None)
        elif field == "items" and not isinstance(order["items"], list):
            raise DataValidationError("Invalid data type for items", field="items", expected_type="list", actual_value=order["items"])

order_data = {
    "order_id": 1023,
    "customer_id": "cust_45",
    "items": "item1,item2"  # This should be a list, not a string
}

try:
    validate_order(order_data)
except DataValidationError as e:
    print("Order validation error:", e)

# Catching and logging errors with context
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    validate_user_data({"age": 30, "email": "notanemail"})
except DataValidationError as e:
    logger.error("Validation error with details: %s", e)