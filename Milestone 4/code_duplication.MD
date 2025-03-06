# Reflections on the DRY Principle

## What are the issues with duplicated code?

1. **Increased Maintenance Effort**: Every time a change or bug fix is needed, it must be applied to every instance of the duplicated code. This increases the chance of errors and inconsistency.
2. **Reduced Readability**: Repetitive code bloats the codebase and makes it harder to read and understand. It takes more time to comprehend the code because developers need to scan through similar blocks of code.
3. **Difficulty in Updates**: When code is duplicated, it becomes harder to make global changes. If the logic needs to be updated, the same modification must be made in multiple places, which increases the potential for mistakes or omissions.
4. **Higher Risk of Bugs**: With repeated code, there’s a higher chance that not all instances are updated correctly, leading to inconsistent behavior across the application.

## How does refactoring improve maintainability?

1. **Centralised Logic**: By consolidating repeated code into a single function or module, any changes made to that logic are automatically reflected throughout the codebase, making maintenance easier.
2. **Improved Readability**: Refactoring simplifies the code structure by removing unnecessary repetition, which leads to a cleaner, more understandable codebase.
3. **Easier Debugging**: With less repetition, debugging becomes more straightforward because there's only one place to look for issues related to a specific logic or feature.
4. **Scalability**: Refactored code that follows the DRY principle is easier to extend and scale. New features can be added without introducing unnecessary complexity or repeated logic.
5. **Reduced Risk of Errors**: By avoiding code duplication, the likelihood of errors caused by inconsistency across multiple code blocks is greatly reduced.

## Example Code

### Before Refactoring:

```python
def calculate_price(item, discount):
    price = item['price'] * (1 - discount)
    return price

def calculate_total(items, discount):
    total = 0
    for item in items:
        price = item['price'] * (1 - discount)
        total += price
    return total
```

### After Refactoring:

```python
def calculate_price(item, discount):
    return item['price'] * (1 - discount)

def calculate_total(items, discount):
    total = 0
    for item in items:
        total += calculate_price(item, discount)
    return total
```

By centralising the price calculation logic in a single function `calculate_price`, we avoid duplicating the price computation in multiple places. This makes the code cleaner, easier to maintain, and reduces the risk of errors in the future.
