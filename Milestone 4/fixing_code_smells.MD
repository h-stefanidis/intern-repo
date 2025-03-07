# Code Smells & Refactoring

## Common Code Smells & Examples

### 1. Magic Numbers & Strings

**Problem:** Hardcoded values make code difficult to understand and maintain.

```python
# Bad example
final_price = price * 1.1  # What does 1.1 represent?
```

**Refactored:**

```python
# Good example
TAX_RATE = 1.1
final_price = price * TAX_RATE
```

### 2. Long Functions

**Problem:** Functions doing too much, making them hard to read and debug.

```python
# Bad example
def process_order(order):
    discount = 0
    if order.customer == "VIP":
        discount = 10
    order.total -= discount
    save_to_db(order)
    send_email(order.customer, "Order processed")
```

**Refactored:**

```python
# Good example
def apply_discount(order):
    if order.customer == "VIP":
        order.total -= 10

def finalise_order(order):
    save_to_db(order)
    send_email(order.customer, "Order processed")
```

### 3. Duplicate Code

**Problem:** Repeated logic instead of reusing functions.

```python
# Bad example
def calculate_discount_vip(price):
    return price * 0.9

def calculate_discount_regular(price):
    return price * 0.95
```

**Refactored:**

```python
# Good example
def calculate_discount(price, rate):
    return price * rate
```

### 4. Large Classes (God Objects)

**Problem:** Classes that handle too many responsibilities.

```python
# Bad example
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total(self):
        # Logic to calculate total

    def apply_discount(self):
        # Logic to apply discount

    def save_to_db(self):
        # Logic to save order
```

**Refactored:**

```python
# Good example
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

class OrderProcessor:
    def calculate_total(self, order):
        pass

    def apply_discount(self, order):
        pass
```

### 5. Deeply Nested Conditionals

**Problem:** Complex nested logic makes code unreadable.

```python
# Bad example
if user:
    if user.is_active:
        if user.has_permission():
            access_granted = True
```

**Refactored:**

```python
# Good example
if user and user.is_active and user.has_permission():
    access_granted = True
```

### 6. Commented-Out Code

**Problem:** Clutters codebase and adds confusion.

```python
# Bad example
# def old_function():
#     print("This is old")
```

**Solution:** Remove unused code.

### 7. Inconsistent Naming

**Problem:** Variables and functions are not clearly named.

```python
# Bad example
def calc(x, y):
    return x * y  # What is x and y?
```

**Refactored:**

```python
# Good example
def calculate_area(width, height):
    return width * height
```

## Reflections

### What code smells did you find in your code?

- Magic numbers
- Large functions doing too much
- Duplicate logic in multiple functions
- Deeply nested conditionals

### How did refactoring improve readability and maintainability?

- Using constants made the purpose of values clearer.
- Breaking large functions into smaller, single-responsibility ones improved readability.
- Using reusable functions removed redundant code.
- Flattening deeply nested conditionals made logic easier to follow.

### How can avoiding code smells make future debugging easier?

- Clean, structured code is easier to read and debug.
- Proper function names reduce ambiguity.
- Smaller functions allow targeted debugging without affecting the whole program.
