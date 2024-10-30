# Understanding integer caching and comparison in Python

def compare_integers(a, b):
    # Compare using 'is' (identity)
    identity_check = (a is b)
    # Compare using '==' (equality)
    equality_check = (a == b)
    return identity_check, equality_check

def main():
    # Test cases with small integers
    small_int1 = 100
    small_int2 = 100
    small_int3 = 300
    small_int4 = 300

    # Comparison results for small integers
    small_results = compare_integers(small_int1, small_int2)
    print(f"Comparing {small_int1} and {small_int2}: is = {small_results[0]}, == = {small_results[1]}")

    # Comparison results for larger integers
    large_results = compare_integers(small_int3, small_int4)
    print(f"Comparing {small_int3} and {small_int4}: is = {large_results[0]}, == = {large_results[1]}")

    # Test cases with strings
    str1 = "hello"
    str2 = "hello"
    str3 = "world"
    
    # Comparison results for strings
    string_results1 = compare_integers(str1, str2)
    string_results2 = compare_integers(str1, str3)
    print(f"Comparing '{str1}' and '{str2}': is = {string_results1[0]}, == = {string_results1[1]}")
    print(f"Comparing '{str1}' and '{str3}': is = {string_results2[0]}, == = {string_results2[1]}")

if __name__ == "__main__":
    main()