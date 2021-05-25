# Date Sequence Generator
User-defined function that generates a sequence of dates (year-month combinations) in Python.
This function is entirely built using standard Python code. That is, it does not use any external libraries.

### Example:
```python
# Import function
from crops import gen

# Generate lists
dates_tup, dates_str = gen('2015-06', '2021-03')

# Print first five tupples
print(dates_tup[:5])
> [(2015, 6), (2015, 7), (2015, 8), (2015, 9), (2015, 10)]

# Print first five strings
print(dates_str[:5])
> ['2015-06', '2015-07', '2015-08', '2015-09', '2015-10']
```
