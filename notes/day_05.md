# Day 5 — Python Testing & Debugging

## Topics Covered

- Python testing fundamentals
- pytest basics
- Assertions
- Testing exceptions with `pytest.raises()`
- Debugging and identifying logic errors
- Input validation
- Two-pointer technique for palindrome problems

## Python Testing

Practiced writing tests for simple Python functions using pytest.

Key concepts:
- `assert actual == expected` checks whether the result matches the expected value.
- `pytest.raises()` can be used to verify that a function raises the expected exception.
- Tests should verify intended behavior, not just whether the code executes.

Example:

```python
with pytest.raises(ValueError):
    calculate_discount(1000, -10)
```

## Exception Handling

For `calculate_discount()`, invalid discount percentages were defined as values below 0 or above 100.

Instead of using `print()` for invalid input, the function raises:

```python
ValueError("Discount percentage must be between 0 and 100")
```

This makes the error explicit and allows the caller or test to handle it.

## Debugging Practice

Worked through a bug in an average calculation:

```python
return total / len(numbers) - 1
```

The issue was the unnecessary `- 1`.

Correct version:

```python
return total / len(numbers)
```

Also considered the behavior for an empty list, where calculating an average is undefined.

## DSA — Valid Palindrome

Solved LeetCode #125 — Valid Palindrome.

Initial approach:
- Remove non-alphanumeric characters.
- Convert the string to lowercase.
- Compare characters from opposite ends.

Improved the solution to use the two-pointer technique:

```python
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        return False

    left += 1
    right -= 1
```

### Two-Pointer Pattern

The two pointers start at opposite ends of the string and move toward the center.

- `left` moves forward.
- `right` moves backward.
- If characters don't match, return `False`.
- If the pointers meet/cross without finding a mismatch, the string is a palindrome.

### Complexity

- Time: O(n)
- Space: O(n) because the cleaned string is created.

## Key Learning

Today I practiced not only writing code but also thinking about how to verify that code behaves correctly.

I also learned to recognize the two-pointer pattern for problems where elements from opposite ends need to be compared.

## Confidence

**Python Testing:** 3/5  
**Debugging:** 3/5  
**Two Pointers:** 3/5

## Day Reflection

Day 5 helped me understand the importance of testing expected behavior rather than only checking whether code runs. I practiced testing normal and invalid inputs and learned when to raise an exception instead of printing an error.

For DSA, I initially solved Valid Palindrome using indexing and then improved it to the intended two-pointer approach. I need more practice recognizing algorithmic patterns quickly.

## Status

**Day 5 — Complete ✅**
