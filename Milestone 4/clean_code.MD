# Clean Code Principles

## Simplicity

Keep code as simple as possible. Avoid unnecessary complexity, redundant logic, and over-engineered solutions. Simple code is easier to understand, debug, and modify.

## Readability

Code should be easy to read and understand. Use meaningful variable and function names, proper indentation, and comments where necessary. Readable code reduces cognitive load and improves collaboration.

## Maintainability

Future developers should be able to work with the code easily. You must write modular, well-documented code to ensure long-term usability and scalability.

## Consistency

Follow style guides and project conventions. Keeping code consistent makes it easier to navigate and reduces confusion. Stick to naming conventions, formatting rules, and code structure patterns.

## Efficiency

Write optimised code while avoiding over-engineering. Optimise only when necessary and prioritise clarity over micro-optimisations.

## Example of Messy Code

```python
# Bad Example: Hard to Read and Maintain
def c(n):
    if n < 2:
        return n
    else:
        return c(n-1) + c(n-2)
print(c(10))
```

### Issues:

- Non-descriptive function name (`c` is unclear)
- Lacks comments explaining the logic
- Inefficient recursive Fibonacci implementation

## Refactored Clean Code

```python
# Good Example: Clear and Efficient Fibonacci Function
def fibonacci(n):
    """Calculate the nth Fibonacci number using memoisation for efficiency."""
    memo = {0: 0, 1: 1}

    def helper(num):
        if num not in memo:
            memo[num] = helper(num - 1) + helper(num - 2)
        return memo[num]

    return helper(n)

print(fibonacci(10))
```

### Improvements:

- Descriptive function name (`fibonacci`)
- Added a docstring for clarity
- Uses memoisation for efficiency
- Clearly structured and easier to read
