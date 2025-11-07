from step_function import step_function

def test_step_function():

    assert step_function(1) == 1
    assert step_function(0) == 1


    assert step_function(-1) == 0
    

    assert step_function(6, threshold=5) == 1
    assert step_function(5, threshold=5) == 1
    assert step_function(4.99, threshold=5) == 0