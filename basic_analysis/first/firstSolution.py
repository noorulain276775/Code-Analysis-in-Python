"""
For mutable-default argument problem
Safe pattern: use None as a parameter and create a new list inside.

"""

def append_item(value, lst=None):
	if lst is None:
		lst = []
	lst.append(value)
	return lst

"""
Create new inner lists for each row:
"""
def create_grid(rows, cols, fill=0):
	grid = [[fill for _ in range(cols)] for _ in range(rows)]
	return grid