# Problem Statement: Rolling Average Calculation

## Objective
Write a Python function to compute the **rolling average** (also known as the moving average) of a list of numbers given a specified window size. The rolling average is a statistical calculation used to analyze data points by creating a series of averages of different subsets of the full dataset.

## Detailed Requirements

### Input:
- A list of numbers (e.g., `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`).
- A window size `k` (e.g., `k = 3`), which represents the number of consecutive elements to consider for each average.

### Output:
- A list of rolling averages, where each element is the average of `k` consecutive elements from the input list.

### Edge Cases:
- If the input list is empty, return an empty list.
- If the window size `k` is greater than the length of the list, return an empty list.
- If `k` is less than or equal to 0, return an empty list.

### Example:
- **Input**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `k = 3`
- **Output**: `[2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]`
  - **Explanation**:
    - The first rolling average is calculated as `(1 + 2 + 3) / 3 = 2.0`.
    - The second rolling average is calculated as `(2 + 3 + 4) / 3 = 3.0`.
    - This process continues until the last window `(8 + 9 + 10) / 3 = 9.0`.

### Constraints:
- The input list can contain both positive and negative numbers.
- The input list can contain floating-point numbers.
- The window size `k` will always be an integer.

### Follow-Up Questions (for interviews):
1. How would you optimize your solution for very large input lists?
2. Can you handle streaming data where the list is not fully available at once?
3. How would you modify your solution to calculate a rolling weighted average?

---

## Function Signature
```python
from typing import List

def rolling_average(numbers: List[float], k: int) -> List[float]:
    pass
```