import pytest
import calc as calc
import math

#TEST BASIC ARITHMETIC

def test_ADD():
    result = calc.add(a=1,b=3)
    assert result == 4
    result = calc.add(a=-1,b=3)
    assert result == 2
    result = calc.add(a=0,b=2)
    assert result == 2
    
def test_SUB():
    result = calc.sub(a=1,b=3)
    assert result == -2
    result = calc.sub(a=1,b=-3)
    assert result == 4
    result = calc.sub(a=0,b=2)
    assert result == -2
    
def test_MUL():
    result = calc.mult(a=2,b=3)
    assert result == 6
    result = calc.mult(a=-1,b=3)
    assert result == -3
    result = calc.mult(a=0,b=2)
    assert result == 0

def test_DIV():
    result = calc.div(a=4,b=2)
    assert result == 2
    result = calc.div(a=5,b=-3)
    assert result == -(5/3)
    result = calc.div(a=0,b=2)
    assert result == 0
    
    with pytest.raises(ZeroDivisionError):
        calc.div(2, 0)
    
#TEST ADVANCED MATH FUNCTIONS

def test_INT_DIV():
    result = calc.int_div(a=8,b=3)
    assert result == 2
    result = calc.int_div(a=-6,b=3)
    assert result == -2
    result = calc.int_div(a=5.5,b=2)
    assert result == 2
    result = calc.int_div(a=42,b=21)
    assert result == 2
    
    with pytest.raises(ZeroDivisionError):       
        calc.int_div(2, 0)
    
def test_FACT():
    
    result = calc.fact(n=0)
    assert result == 1
    result = calc.fact(n=4)
    assert result == 24
    
    with pytest.raises(ValueError):
        calc.fact(-5)
    with pytest.raises(TypeError):
        calc.fact(4.20)

def test_POW():
    result = calc.pow(base=4,exponent=2)
    assert result == 16
    result = calc.pow(base=0.5,exponent=2)
    assert result == 0.25
    result = calc.pow(base=-2,exponent=0)
    assert result == 1
    
    with pytest.raises(ValueError):       
        calc.pow(0, -2)
    with pytest.raises(ValueError):       
        calc.pow(2, 1.5)
        
def test_root():
    result = calc.root(base=8,index=3)
    assert result == 2
    
    with pytest.raises(ValueError):
        calc.root(base=0.5,index=-2)

    result = calc.root(base=0.5,index=2)
    assert result == pytest.approx((math.sqrt(2)/2))

    with pytest.raises(ValueError):       
        calc.root(3, -3)
    with pytest.raises(ValueError):       
        calc.root(2, 1.5)
    
def test_LN():
    result = calc.ln(n=math.e)
    assert result == pytest.approx(1)
    result = calc.ln(n=2)
    assert result == pytest.approx(math.log(2))
    
    with pytest.raises(ValueError):       
        calc.ln(-1)
    with pytest.raises(ValueError):       
        calc.ln(0)

def test_LOG():
    result = calc.log(base=2,argument=8)
    assert result == 3
    result = calc.log(base=3,argument=9)
    assert result == pytest.approx(2)
    
    with pytest.raises(ValueError):       
        calc.log(-2,4)
    with pytest.raises(ValueError):       
        calc.log(0,4)
    with pytest.raises(ValueError):       
        calc.log(1,4)