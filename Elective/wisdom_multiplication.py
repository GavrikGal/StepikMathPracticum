import pandas as pd

df = pd.DataFrame([x*y for x in range(10, 100) for y in range(10, 100)], columns=['NxM'])
pd.set_option('display.min_rows', 100)

def multiplication_check_list(start=10, stop=99):
    right = 0
    wrong = 0
    res_list = []
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            res = (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y)
            res_list.append(res)
            if res == x * y:
                right += 1
            else:
                wrong += 1
    print(f'Правильных результатов: {right}')
    print(f'Неправильных результатов: {wrong}')
    return res_list


def multiplication_check_list(start=10, stop=99, length_check=True):
    right = 0
    wrong = 0
    res_list = []
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            first_x = 100 - x
            first_y = 100 - y
            first_res = str(100 - (first_x + first_y))
            last_res = str(first_x * first_y)
            if length_check:
                if len(last_res) < 2:
                    last_res = '0' + last_res
            res = int(first_res + last_res)
            res_list.append(res)
            if res == x * y:
                right += 1
            else:
                wrong += 1
    print(f'Правильных результатов: {right}')
    print(f'Неправильных результатов: {wrong}')
    return res_list


list_with_check = multiplication_check_list(10, 99, length_check=True)
list_without_check = multiplication_check_list(10, 99, length_check=False)

df['With Check'] = pd.DataFrame(list_with_check)
df['Without Check'] = pd.DataFrame(list_without_check)

def highlight(df, col2highlite="With Check"):
    ret = pd.DataFrame("", index=df.index, columns=df.columns)
    ret.loc[df["NxM"] != df["With Check"], col2highlite] = "background-color: red"
    ret.loc[df["NxM"] == df["With Check"], col2highlite] = "background-color: green"

    ret.loc[df["NxM"] != df["Without Check"], col2highlite] = "background-color: red"
    ret.loc[df["NxM"] == df["Without Check"], col2highlite] = "background-color: green"
    return ret

df.style.apply(highlight, axis=None)

df.to_html('table.html')