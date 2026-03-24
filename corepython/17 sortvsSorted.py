"""
==============================
sort() vs sorted() in Python
==============================
"""

# --------------------------------------------------
# 1. sort() Method
# --------------------------------------------------
"""
sort() is a list method.

• Works only on lists
• Modifies the original list (in-place)
• Does NOT return a new list (returns None)
• Supports reverse and key parameters

Syntax:
list.sort(reverse=False, key=None)
"""

# nums = [3, 1, 4, 2]
# nums.sort()
# print(nums)   


# --------------------------------------------------
# 2. sorted() Function
# --------------------------------------------------
"""
sorted() is a built-in function.

• Works on any iterable (list, tuple, string, dictionary, etc.)
• Does NOT modify the original data
• Returns a NEW sorted list
• Supports reverse and key parameters

Syntax:
sorted(iterable, reverse=False, key=None)
"""

# nums = (3, 1, 4, 2)
# new_nums = sorted(nums)
# print(new_nums)
# print(type(new_nums))
# print(nums)        # Original tuple unchanged


# --------------------------------------------------
# Comparison Table
# --------------------------------------------------
"""
| Feature            | sort()           | sorted()                         |
|--------------------|------------------|----------------------------------|
| Type               | List method      | Built-in function                |
| Returns            | None             | New sorted list                  |
| Modifies original? | Yes              | No                               |
| Usable on          | Only lists       | Any iterable                     |
| Output type        | None             | Always a list                    |
"""


# --------------------------------------------------
# When to Use What?
# --------------------------------------------------
"""
• Use sort() when:
  - You want to sort a list permanently
  - You don't need the original order

• Use sorted() when:
  - You want to keep original data unchanged
  - You are working with tuples, strings, or other iterables
"""
