from users.utils import check_snt, check_trung_mang

## Định nghĩa hàm 

def test_abc(): 

    assert 1==1 ## Expect kết quả


def test_check_snt1():
    result = check_snt(2)
    assert result == True

def test_check_snt2():
    result = check_snt(4)
    assert result == False 

def test_check_snt3():
    result = check_snt(-2)
    assert result == False 

def test_check_snt4():
    result = check_snt(0.5)
    assert result == False 

def test_check_trung_mang_oneletter():
    array_not_dup = check_trung_mang([1,1,2,2,3,4])
    assert array_not_dup == [1,2,3,4]

def test_check_trung_mang_dupmiddle():
    array_not_dup = check_trung_mang([1,2,1,2,1,2])
    assert array_not_dup == [1,2]

def test_check_trung_mang_twoletters():
    array_not_dup = check_trung_mang([10,1,8,10,18])
    assert array_not_dup == [10,1,8,18]

def test_check_trung_mang_threeletters():
    array_not_dup = check_trung_mang([123,231,12,23,123,213])
    assert array_not_dup == [123,231,12,23,213]

def test_check_trung_mang_none():
    array_not_dup = check_trung_mang([])
    assert array_not_dup == []

def test_check_trung_mang_onedata():
    array_not_dup = check_trung_mang([1])
    assert array_not_dup == [1]


