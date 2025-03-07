# Common Refactoring Techniques

## Example of Overly Complicated Code

```python
# Bad Example: Complex and hard-to-read function

def calculate_data(values):
    total = 0
    count = 0
    for i in range(len(values)):
        total += values[i]
        count += 1
    avg = total / count if count != 0 else 0

    filtered_values = []
    for i in range(len(values)):
        if values[i] > avg:
            filtered_values.append(values[i])

    print("Average:", avg)
    print("Filtered Values:", filtered_values)
    return filtered_values
```

### What Made the Code Complex?

- **Manually iterating with range(len(values)) instead of using loops.**
- **Redundant calculations (count could be replaced by len(values)).**
- **Separate loops for summing and filtering, making it inefficient.**
- **Printing inside the function reduces flexibility.**

## Refactored Code

```python
# Good Example: Simpler, more readable function

def calculate_average(values):
    return sum(values) / len(values) if values else 0

def filter_above_average(values, avg):
    return [value for value in values if value > avg]

def process_values(values):
    avg = calculate_average(values)
    filtered_values = filter_above_average(values, avg)
    return avg, filtered_values

values = [10, 20, 30, 40, 50]
average, filtered = process_values(values)
print("Average:", average)
print("Filtered Values:", filtered)
```

### How Did Refactoring Improve It?

- **Modular Approach**: Functions have clear responsibilities.
- **Pythonic Code**: List comprehensions replace explicit loops.
- **Improved Readability**: Easier to understand at a glance.
- **Better Maintainability**: Each function can be tested and modified separately.

## How Refactoring Improved the Code

Refactoring removed redundancy, improved efficiency, and made the code more readable. Breaking it into smaller functions made debugging and future modifications easier. The new version follows clean code principles, improving maintainability and performance.
