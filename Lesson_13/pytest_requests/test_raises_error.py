import pytest
import pytest_check

def test_handling_error():
    with pytest.raises(ZeroDivisionError) as e:
        print(50 / 0)
    pytest_check.equal(str(e.type),"<class 'ZeroDivisionError'>")
    # assert str(e.type) == "<class 'ZeroDivisionError'> "
    print("After a check....")
    pytest_check.equal(str(e.value), 'division by zero')
    # assert str(e.value) == 'division by zer
    # o'