def outer_function():
    x = "outer x"  # Enclosing scope

    def inner_function():
        x = "inner x"  # Local scope
        print("Inner function:", x)  # Should print "inner x"

    inner_function()
    print("Outer function:", x)  # Should print "outer x"

x = "global x"  # Global scope
outer_function()
print("Global scope:", x)  # Should print "global x"