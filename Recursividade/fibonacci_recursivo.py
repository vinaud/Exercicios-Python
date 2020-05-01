# calcula o n-ésimo elemento da sequencia de fibonacci, de forma recursiva

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))