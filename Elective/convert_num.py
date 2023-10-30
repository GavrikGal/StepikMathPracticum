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


n = '2A'
print(convert(n, 35, 16))