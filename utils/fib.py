def fib(n):
    """
    This is fib method.
    """
    return fibab(n, 1, 1)

def fibab(n, a, b):
    """
    This is general fib method.
    """
    if n<2:
        return 1
    else:
        return a*fibab(n-1,a,b) + b*fibab(n-2,a,b)
