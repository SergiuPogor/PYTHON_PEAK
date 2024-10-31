# Using the walrus operator to simplify code
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without walrus operator
squared_even = []
for num in data:
    if num % 2 == 0:
        squared_even.append(num ** 2)

# With walrus operator
squared_even_walrus = [
    (squared := num ** 2) for num in data if num % 2 == 0
]

print("Squared even numbers without walrus:", squared_even)
print("Squared even numbers with walrus:", squared_even_walrus)

# The walrus operator allows us to assign and use the squared value in one line,
# resulting in cleaner and more concise code.