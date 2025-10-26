"""first.py — intentionally buggy examples for deep analysis.

This file contains two common Python traps:

- mutable default argument (state is shared across calls)
- list-of-lists aliasing via list multiplication (rows reference the same list)

Task: analyze these traps, find the root cause and write fixes/solutions.
"""

def append_item(value, lst=[]):
	lst.append(value)
	return lst


def create_grid(rows, cols, fill=0):
	return [[fill] * cols] * rows


def safe_create_grid(rows, cols, fill=0):
	return [[fill for _ in range(cols)] for _ in range(rows)]


def demonstrate():
	print("Mutable default argument trap:")
	print("First call (expect [1]):", append_item(1))
	print("Second call (expect [2], but gets [1, 2]):", append_item(2))
	print("Call with explicit new list (works as intended):", append_item(3, []))

	print("\nList-of-lists aliasing trap:")
	g = create_grid(3, 3, 0)
	print("Initial grid:", g)
	g[0][0] = 9
	print("After setting g[0][0] = 9 (unexpected change in all rows):", g)

	print("\nCorrect grid (no aliasing):")
	g2 = safe_create_grid(3, 3, 0)
	print("Before:", g2)
	g2[0][0] = 7
	print("After changing g2[0][0] = 7:", g2)


if __name__ == '__main__':
	demonstrate()

