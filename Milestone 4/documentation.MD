# Best Practices for Writing Comments and Documentation

## When Should You Add Comments?

- **Clarifying Complex Logic**: If a piece of code involves intricate logic, add a comment explaining its purpose.
- **Explaining Workarounds**: If you use an unconventional approach due to limitations or bugs, document why.
- **Providing Context**: When a function or class is part of a larger system, clarify its role.
- **Marking TODOs and Fixes**: Helps track improvements or known issues.

## When Should You Avoid Comments and Instead Improve the Code?

- **Redundant Comments**: If the comment repeats what the code already says, it's unnecessary.
- **Obsolete Comments**: Avoid comments that may become outdated; instead, write self-explanatory code.
- **Poorly Named Variables/Functions**: If a comment explains what a variable or function does, rename it instead.

## Example of Poorly Commented Code

```python
# This function calculates the square of a number
# Then, it prints the square
# Finally, it returns the square

def sq(n):
    res = n * n  # Multiplying n by itself
    print("Square:", res)  # Print result
    return res  # Return result
```

### Issues:

- **Redundant comments**: The function is simple and self-explanatory.
- **Unclear function name**: `sq(n)` is not descriptive.
- **Unnecessary print statement inside function.**

## Improved Code with Better Documentation

```python
def square_number(number: int) -> int:
    """
    Calculates and returns the square of a given number.
    :param number: The number to be squared.
    :return: The squared result.
    """
    return number ** 2

result = square_number(5)
print("Square:", result)
```

### Improvements:

- **Descriptive Function Name**: Clearly states its purpose.
- **Docstring Instead of Comments**: Helps auto-generate documentation.
- **Eliminated Redundant Comments**: The function speaks for itself.
- **Separated Logic and Output**: Allows function reuse without forcing a print statement.
