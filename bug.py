def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of a == 0
    if b == 0:
        return a  # Correct handling of b == 0
    return a / b

result = function_with_uncommon_error(0,0)
print(result)