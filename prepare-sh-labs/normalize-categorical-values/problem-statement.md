# Normalize Categorical Values

## Background
In many real-world datasets, categorical variables are often represented as text labels such as `'low'`, `'medium'`, and `'high'`. These labels need to be converted into numerical values for machine learning models or data analysis tasks. Normalizing these categorical values into a consistent numerical format is a common preprocessing step.

## Problem
You are tasked with writing a Python function that normalizes categorical values representing levels of intensity or priority. The function should convert the categorical values `'low'`, `'medium'`, and `'high'` into the numerical values `0`, `1`, and `2`, respectively. The function should also handle case-insensitivity, meaning that it should treat `'Low'`, `'LOW'`, `'Medium'`, `'MEDIUM'`, `'High'`, and `'HIGH'` as valid inputs and normalize them accordingly.

## Requirements

### Function Signature
```python
def normalize_category(category: str) -> int:
```

# Normalize Categorical Values

## Function Description
The function `normalize_category` takes a single string argument `category` and returns an integer based on the following mapping:

- `'low'` → `0`
- `'medium'` → `1`
- `'high'` → `2`

The function should handle case insensitivity and unexpected inputs gracefully.

---

## Input
- The input is a string representing the category level. The input can be in any case (e.g., `'low'`, `'Low'`, `'LOW'`, `'medium'`, `'Medium'`, `'MEDIUM'`, `'high'`, `'High'`, `'HIGH'`).

---

## Output
- The function returns an integer based on the mapping:
  - `'low'` → `0`
  - `'medium'` → `1`
  - `'high'` → `2`
- If the input is not one of the expected categories (e.g., `'very low'`, `'medium-high'`, etc.), the function raises a `ValueError` with an appropriate error message.

---

## Case Insensitivity
The function is case-insensitive. For example:
- `'Low'`, `'LOW'`, and `'low'` are all treated as `'low'` and mapped to `0`.
- `'Medium'`, `'MEDIUM'`, and `'medium'` are all treated as `'medium'` and mapped to `1`.
- `'High'`, `'HIGH'`, and `'high'` are all treated as `'high'` and mapped to `2`.

---

## Error Handling
If the input is not one of the expected categories, the function raises a `ValueError` with a descriptive message. For example:
```python
raise ValueError("Invalid category: 'Very Low'. Expected one of: 'low', 'medium', 'high'.")
```