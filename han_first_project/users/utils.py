
def sum_a_b(a, b):
    return a + b

def check_snt(num): 
    count = 0
    if num < 2: 
        return False
    elif num == 2: 
        return True
    else: 
        for x in range(2,num+1):
            if num % x == 0:
                count += 1
    return False if count > 1 else True

def check_trung_mang (arr):
    arr_new = []
    for item in arr: 
        if item in arr_new:
            continue
        else: 
            arr_new.append(item)
    return arr_new
