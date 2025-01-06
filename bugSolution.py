def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("Both inputs are zero; division is undefined.")
    if a == 0:
        return b
    if b == 0:
        return a
    return a / b

try:
    result = function_with_uncommon_error(0,0)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")
