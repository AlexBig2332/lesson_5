import divisor_master

def test_num_simple():
    assert divisor_master.num_simple(11) == True
    assert divisor_master.num_simple(5) == True
    assert divisor_master.num_simple(4) == False

def test_num_divisors():
    assert divisor_master.num_divisors(11) == [1,11]
    assert divisor_master.num_divisors(5) == [1,5]
    assert divisor_master.num_divisors(113) == [1,113]

def test_num_max_divisor():
    assert divisor_master.num_max_divisor(128) == 2
    assert divisor_master.num_max_divisor(11) == 11
    assert divisor_master.num_max_divisor(10) == 5
