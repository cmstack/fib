from fib import fibnumber, fibseries


def test_fibseries():
    assert fibseries.fibseries(0) == None


def test_fibnumber():
    assert fibnumber.fibnumber(20) == 6765