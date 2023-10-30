def numerics(n):
    return list(map(int, str(n)))


def kaprekar_10(n):
    num_sqr = n**2
    num_sqr_str = str(num_sqr)
    for i in range(1, len(num_sqr_str)):
        if (int(num_sqr_str[i:]) != 0) and (int(num_sqr_str[0:i]) + int(num_sqr_str[i:]) == n):
            return True
    return False


def to_char(n):
    str_nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return str_nums[n]


def convert(num, to_base=10, from_base=10):
    num = str(num)
    num_10 = int(num, base=from_base)
    if to_base == 10:
        return str(num_10)
    else:
        res_list = []
        while True:
            if num_10 >= to_base:
                new_num = to_char(num_10 % to_base)

                res_list.append(str(new_num))
                num_10 //= to_base
            else:
                res_list.append(to_char(num_10))
                break
        res_list.reverse()
        return ''.join(res_list)


def kaprekar(n, base=10):
    num_10 = int(convert(n, from_base=base))
    sqr_based_str = convert(num_10**2, to_base=base)
    for i in range(1, len(sqr_based_str)):
        if (int(convert(sqr_based_str[i:], from_base=base)) != 0) \
                and (int(convert(sqr_based_str[0:i], from_base=base))
                     + int(convert(sqr_based_str[i:], from_base=base))
                     == int(convert(n, from_base=base))):
            return True
    return False


test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Тест чисел Капрекара из системы с основанием 16