from my_package import my_module

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert my_module.top_n([2,7,3,6], 3) == [7,3,6], 'incorrect'
    assert my_module.top_n([10,1,12,9,2], 2) == [12,10], 'incorrect'
    assert my_module.top_n([1,2,3,4,5], 5) == [5,4,3,2,1], 'incorrect'