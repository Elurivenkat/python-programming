Sure! Here's a **basic-level explanation** for each of the Python list tasks from 1 to 50:

---

### 1. Create a list and print all elements:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

### 2. Append an element to a list:
```python
fruits.append("orange")
print(fruits)
```

### 3. Insert an element at a specific index:
```python
fruits.insert(1, "grape")
print(fruits)
```

### 4. Delete an element using remove():
```python
fruits.remove("banana")
print(fruits)
```

### 5. Delete an element using pop() and del:
```python
fruits.pop()  # Removes last
print(fruits)
del fruits[0]  # Removes first
print(fruits)
```

### 6. Slice a list to get a sublist:
```python
sub = fruits[1:3]
print(sub)
```

### 7. Reverse a list:
```python
print(fruits[::-1])  # Using slicing
fruits.reverse()     # Using method
print(fruits)
```

### 8. Sort a list:
```python
nums = [3, 1, 4, 2]
nums.sort()
print("Ascending:", nums)
nums.sort(reverse=True)
print("Descending:", nums)
```

### 9. Find the length of a list:
```python
print(len(nums))
```

### 10. Check if an element exists:
```python
if 3 in nums:
    print("3 is in the list")
```

### 11. Count occurrences:
```python
nums = [1, 2, 2, 3]
print(nums.count(2))
```

### 12. Find the index:
```python
print(nums.index(2))
```

### 13. Create list from user input:
```python
nums = list(map(int, input("Enter numbers:").split()))
print(nums)
```

### 14. Remove duplicates:
```python
nums = [1, 2, 2, 3]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)
```

### 15. Merge two lists:
```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
```

### 16. Largest and smallest:
```python
print("Max:", max(nums))
print("Min:", min(nums))
```

### 17. Sum and average:
```python
print("Sum:", sum(nums))
print("Average:", sum(nums)/len(nums))
```

### 18. Copy a list:
```python
copy1 = nums[:]
copy2 = nums.copy()
print(copy1)
print(copy2)
```

### 19. Swap first and last:
```python
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)
```

### 20. Even/Odd lists:
```python
even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]
print(even, odd)
```

### 21. Flatten a nested list:
```python
nested = [[1, 2], [3, 4]]
flat = [i for sub in nested for i in sub]
print(flat)
```

### 22. Rotate list:
```python
k = 2
rotated = nums[k:] + nums[:k]
print(rotated)
```

### 23. Remove empty strings:
```python
words = ["apple", "", "banana"]
words = [w for w in words if w != ""]
print(words)
```

### 24. Split into chunks:
```python
n = 2
chunks = [nums[i:i+n] for i in range(0, len(nums), n)]
print(chunks)
```

### 25. 2nd largest and smallest:
```python
nums.sort()
print(nums[1], nums[-2])
```

### 26. Count pos/neg/odd/even:
```python
pos = neg = odd = even = 0
for i in nums:
    if i > 0: pos += 1
    if i < 0: neg += 1
    if i % 2 == 0: even += 1
    else: odd += 1
print(pos, neg, odd, even)
```

### 27. Common elements:
```python
a = [1, 2, 3]
b = [2, 3, 4]
common = [i for i in a if i in b]
print(common)
```

### 28. Difference:
```python
diff = [i for i in a if i not in b]
print(diff)
```

### 29. Find duplicates:
```python
seen = set()
dups = set()
for i in nums:
    if i in seen:
        dups.add(i)
    else:
        seen.add(i)
print(dups)
```

### 30. Remove duplicates (no set):
```python
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)
```

### 31. Squares:
```python
squares = [x*x for x in range(1, 11)]
print(squares)
```

### 32. Filter even numbers:
```python
even = [x for x in nums if x % 2 == 0]
print(even)
```

### 33. Convert to uppercase:
```python
words = ["hi", "hello"]
upper = [w.upper() for w in words]
print(upper)
```

### 34. Elements > 50:
```python
nums = [10, 60, 70]
result = [x for x in nums if x > 50]
print(result)
```

### 35. Replace negative with 0:
```python
nums = [-1, 2, -3]
nums = [0 if x < 0 else x for x in nums]
print(nums)
```

### 36. Sort by length:
```python
words = ["a", "abcd", "abc"]
words.sort(key=len)
print(words)
```

### 37. Sort list of tuples:
```python
tuples = [(1, 2), (3, 1)]
tuples.sort(key=lambda x: x[1])
print(tuples)
```

### 38. Linear search:
```python
x = 3
found = False
for i in nums:
    if i == x:
        found = True
        break
print(found)
```

### 39. Check sorted:
```python
print(nums == sorted(nums))
```

### 40. Binary search:
```python
import bisect
nums.sort()
index = bisect.bisect_left(nums, 3)
print(index)
```

### 41. All prime numbers:
```python
nums = [2, 3, 4, 5, 6, 7]
primes = []
for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
print(primes)
```

### 42. Frequency of elements:
```python
freq = {}
for i in nums:
    freq[i] = freq.get(i, 0) + 1
print(freq)
```

### 43. Rotate list by one:
```python
nums = [1, 2, 3, 4]
nums = nums[1:] + nums[:1]
print(nums)
```

### 44. Check palindrome:
```python
nums = [1, 2, 3, 2, 1]
print(nums == nums[::-1])
```

### 45. Most frequent element:
```python
from collections import Counter
cnt = Counter(nums)
print(cnt.most_common(1)[0][0])
```

### 46. List of chars to string:
```python
chars = ['H', 'i']
string = ''.join(chars)
print(string)
```

### 47. Multiply all numbers:
```python
result = 1
for i in nums:
    result *= i
print(result)
```

### 48. Remove negative numbers:
```python
nums = [1, -2, 3, -4]
nums = [x for x in nums if x >= 0]
print(nums)
```

### 49. Group anagrams:
```python
words = ["bat", "tab", "cat"]
from collections import defaultdict
anagrams = defaultdict(list)
for word in words:
    anagrams[''.join(sorted(word))].append(word)
print(list(anagrams.values()))
```

### 50. Sort list of dicts by key:
```python
students = [{"name": "John", "age": 20}, {"name": "Amy", "age": 18}]
students.sort(key=lambda x: x["age"])
print(students)
```

---

Let me know if you want output, explanation, or practice for any specific one!
