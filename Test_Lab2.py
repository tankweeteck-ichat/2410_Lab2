import Lab2

def test_find_min_max():
    test_array=[1,3,5,4,2]
    expected_result=[1,5]
    test_rslt=[]
    test_rslt = Lab2.find_min_max(test_array)
    assert(test_rslt == expected_result)


def test_calc_average():
    test_array=[1,3,5,4,2]
    expected_result=3
    test_rslt = Lab2.calc_average(test_array)
    assert(test_rslt == expected_result)



def test_calc_median_temperature_odd_array():
    test_array=[10,35,50,40,20]
    expected_result=35
    test_rslt = Lab2.calc_median_temperature(test_array)
    assert(test_rslt == expected_result)



def test_calc_median_temperature_even_array():
    test_array=[10,35,50,40,20,45]
    expected_result=37.5
    test_rslt = Lab2.calc_median_temperature(test_array)
    assert(test_rslt == expected_result)
