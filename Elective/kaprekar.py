def numerics(n):
    return list(map(int, str(n)))

def kaprekar_step(L):
    sorted_up = sorted(L)
    sorted_down = sorted(L, reverse=True)
    kaprekar_num = list_to_num(sorted_down) - list_to_num(sorted_up)
    return kaprekar_num

def list_to_num(L):
    num = 0
    for i, elem in zip(range(len(L)-1, -1, -1), L):
        num += elem*(10**i)
    return num

def kaprekar_loop(n):
    if kaprekar_check(n):
        allow_nums = [495, 6174, 549945, 631764]
        founded_nums = []
        while True:
            print(n)
            founded_nums.append(n)
            if n not in allow_nums:
                num_list = numerics(n)
                n = kaprekar_step(num_list)
                if n in founded_nums:
                    print(f"Следующее число - {n}, кажется процесс зациклился...")
                    break
            else:
                break
    else:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")

def kaprekar_check(n) -> bool:
    if not validate_quantity(n):
        return False
    if not validate_variety(n):
        return False
    if not validate_round(n):
        return False
    return True

def quantity(n) -> int:
    quantity = 1
    while True:
        if n // 10**(quantity - 1) < 10:
            return quantity
        else:
            quantity += 1

def validate_quantity(n) -> bool:
    allow_quantity = [3, 4, 6]
    if quantity(n) in allow_quantity:
        return True
    return False

def validate_round(n) -> bool:
    if n % 10**quantity(n-1) != 0:
        return True
    return False

def validate_variety(n) -> bool:
    num_list = numerics(n)
    for num in num_list:
        if num_list.count(num) < 4:
            return True
    return False



L = [6, 8, 0, 4]
num = 1234

kaprekar_loop(num)