def steps(n):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")  
    
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps
