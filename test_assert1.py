def f():
    return 1

def test_function():
    assert f() == 1
    
def test_function2():
    assert f() == 1

def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    print('HUNG')