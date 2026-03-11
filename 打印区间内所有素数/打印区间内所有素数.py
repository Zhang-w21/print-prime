def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
def print_primes(start,end):
    for i in range(start, end+1):
        if is_prime(i):
            print(f"{i}是素数")
num1 = int(input("请输入起点数字："))
num2 = int(input("请输入终点数字："))
print_primes(num1,num2)
