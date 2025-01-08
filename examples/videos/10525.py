def create_dynamic_variables():     
    # Example dictionary to simulate dynamic variable creation     
    data = {         
        "name": "John",         
        "age": 30,         
        "country": "USA"     
    }      

    # Dynamically create variables from dictionary keys     
    for key, value in data.items():         
        globals()[key] = value  # Use globals() to create variables dynamically at the global level      

    # Print dynamically created variables     
    print(f"Name: {name}")     
    print(f"Age: {age}")     
    print(f"Country: {country}")  

# Example usage of the function 
if __name__ == "__main__":     
    create_dynamic_variables()

