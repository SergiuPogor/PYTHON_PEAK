import cProfile
import pstats
import time

# Simulate a time-consuming task
def slow_function():
    time.sleep(1)  # Simulates a delay
    return sum(i * i for i in range(10000))

def fast_function():
    return sum(i for i in range(10000))

# Profile the slow function
def profile_code():
    cProfile.run('slow_function()', 'slow_function_stats')

    # Analyze the stats
    with open('slow_function_report.txt', 'w') as f:
        ps = pstats.Stats('slow_function_stats', stream=f)
        ps.sort_stats('cumulative')  # Sort by cumulative time
        ps.print_stats()

# Profile the fast function
def profile_fast_code():
    cProfile.run('fast_function()', 'fast_function_stats')

    # Analyze the stats
    with open('fast_function_report.txt', 'w') as f:
        ps = pstats.Stats('fast_function_stats', stream=f)
        ps.sort_stats('cumulative')  # Sort by cumulative time
        ps.print_stats()

if __name__ == "__main__":
    profile_code()  # This will create a report for the slow function
    profile_fast_code()  # This will create a report for the fast function