## 1st Python Traps

the first trap in below code is **mutable-default argument problem**

```bash

def append_item(value, lst=[]):
	lst.append(value)
	return lst

```

Using an empty list as the default triggers the mutable-default argument problem. When lst isn’t provided, the function reuses the same list across calls, so each call appends to the previous result.

### Why it happens:
Default parameter values are evaluated once at function definition time, not on every call. So your lst=[] is a single list object that all calls share when lst isn’t passed.


## 2nd Python Traps

the first trap in below code is **rows referencing**

```bash

def create_grid(rows, cols, fill=0):
	return [[fill] * cols] * rows

```

With fill=0, [ [fill] * cols ] creates one row. Multiplying by rows repeats that same list reference rather than building new lists. Therefore, every row refers to the same object in memory, and mutating any row affects all of them.

### Why it happens:

1. some_list * n does not create n independent copies.
2. It creates a new outer list that repeats references to the same underlying objects (a shallow copy).