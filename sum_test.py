import sum

def test_1():
    assert sum.sum(1,1) == 2
def test_2():
    assert sum.sum(4,-2) == 2
def test_3():
    assert sum.sum(1,2) == 3
def test_4():
    assert sum.sum(5,5) == 10