def is_even(n):
    if n %2 == 0:
        return True
    elif n % 2 != 0:
        return False

n = int(input())

answer = is_even(n)
print(answer)

