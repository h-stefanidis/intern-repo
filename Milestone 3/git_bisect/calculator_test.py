def divide(a, b):
    return a / b  # BUG: Removed division by zero check

print(divide(10, 0))  # This will now cause a crash
