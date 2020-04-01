def maximo(n, y, z):
    if n >= y and n >= z:
        return n
    elif y>=n and y>= z:
        return y
    elif z>=n and z>= y:
        return z
    