import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def risky_function(x):
    if x < 0:
        logging.error("Negative value encountered: %d", x)
        raise ValueError("Value must be non-negative")
    result = 10 / x
    logging.info("Processed value: %d, Result: %f", x, result)
    return result

def main():
    values = [10, 5, 0, -3]
    for value in values:
        try:
            logging.info("Trying value: %d", value)
            risky_function(value)
        except Exception as e:
            logging.exception("An error occurred while processing value: %d", value)

if __name__ == "__main__":
    main()