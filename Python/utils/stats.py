def sum(lst):
	"""
	Args:
	    lst: list.
	"""
	result = 0
	for l in lst:
		result += l
	return result

def max(lst):
	result = lst[0]
	for i in lst:
		if i>result:
			result = i
	return result

def min(lst):
	result = lst[0]
	for i in lst:
		if i<result:
			result = i
	return result

def mean(lst):
	return sum(lst) / len(lst)