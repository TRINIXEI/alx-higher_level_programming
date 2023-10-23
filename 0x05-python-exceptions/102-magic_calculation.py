#!/usr/bin/python3
def magic_calculation(n, m):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += n ** m / i
        except Exception:
            result = m + n
            break
    return result
