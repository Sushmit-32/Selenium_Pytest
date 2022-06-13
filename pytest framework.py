import pytest

@pytest.mark.demo1
def test_m1():
    a=5
    b=6
    if(a==b):
        print("Test Failed")
    else:
        print("Test passed")

@pytest.mark.demo2
def test_m2():
    a=6
    b=7
    c=(a+b)
    if(c>5):
        print("Not Required")
    else:
        print("Great")
@pytest.mark.demo1
def test_m3():
    a=5
    b=6
    c=a*b
    if(c>10):
        print("Product is greater than 10")
    else:
        print("Product is less than 10")