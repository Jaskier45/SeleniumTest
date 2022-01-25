import pytest

# @pytest.fixture()
# def setup():
#     print("Once before every method")

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after every method")
    

def testMethod1(setup):
    print("First test is successfully complete")

def testMethod2(setup):
    print("Second test is successfully complete")





