def countdown(n):
    if n <= 0: # Base case
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

countdown(10)