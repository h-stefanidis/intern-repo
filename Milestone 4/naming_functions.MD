# Best Practices for Naming Variables and Functions

## What Makes a Good Variable or Function Name?

- **Descriptive**: The names should clearly indicate the purpose of the variable or function.
- **Concise**: Avoiding overly long names, but ensure they remain meaningful.
- **Consistent**: Follow a consistent naming convention (e.g., camelCase, snake_case, PascalCase) based on the project style guide.
- **Avoid Abbreviations**: Use full words unless an abbreviation is widely recognised (e.g., `id`, `URL`).
- **Action-Oriented for Functions**: Function names should describe what they do, often starting with verbs like `get`, `set`, `calculate`, etc.

## Issues with Poorly Named Variables

- **Lack of Clarity**: Hard to understand what the variable represents.
- **Ambiguity**: Similar names can lead to confusion (e.g., `temp1` and `temp2`).
- **Inconsistent Naming**: Makes it harder to follow the logic throughout the code.
- **Misleading Names**: Names that do not accurately represent the data they hold can cause bugs.

## Example of Unclear Variable Names

```python
# Bad Example: Unclear variable names
x = 10
y = 5
z = x * y
print(z)
```

### Issues:

- `x`, `y`, and `z` provide no context on what they represent.
- Difficult to understand the purpose of the calculation.

## Refactored Code with Clear Naming

```python
# Good Example: Meaningful variable names
length = 10
width = 5
area = length * width
print(area)
```

### Improvements:

- Variables clearly describe what they represent.
- The logic of the calculation is easier to follow.

## How Refactoring Improved Readability

Renaming variables and functions improves clarity, making it easier for developers to understand the purpose of each element at a glance. This reduces confusion, minimises errors, and enhances maintainability in collaborative projects.
