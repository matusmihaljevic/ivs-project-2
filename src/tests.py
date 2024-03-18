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
    result = calc.div(dividend=4,divisor=2)
    assert result == 2
    result = calc.div(dividend=5,divisor=-3)
    assert result == round(-(5/3), 7)
    result = calc.div(dividend=0,divisor=2)
    assert result == 0
    
    with pytest.raises(ZeroDivisionError):
        calc.div(2, 0)
    
#TEST ADVANCED MATH FUNCTIONS

def test_MOD():
    result = calc.mod(dividend=2,divisor=3)
    assert result == 2
    result = calc.mod(dividend=-1,divisor=3)
    assert result == 2
    result = calc.mod(dividend=5.5,divisor=2)
    assert result == 1.5
    result = calc.mod(dividend=42,divisor=21)
    assert result == 0
    
    with pytest.raises(ZeroDivisionError):       
        calc.mod(2, 0)
    
def test_FACT():
    
    result = calc.fact(self=0)
    assert result == 1
    result = calc.fact(self=4)
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
    assert result == round(math.sqrt(2)/2, 7)

    with pytest.raises(ValueError):       
        calc.root(3, -3)
    with pytest.raises(ValueError):       
        calc.root(2, 1.5)
    
def test_LN():
    result = calc.ln(self=math.e)
    assert result == 1
    result = calc.ln(self=2)
    assert result == round(math.log(2), 7)
    
    with pytest.raises(ValueError):       
        calc.ln(-1)
    with pytest.raises(ValueError):       
        calc.ln(0)

def test_LOG():
    result = calc.log(base=2,argument=8)
    assert result == 3
    result = calc.log(base=3,argument=9)
    assert result == 2
    
    with pytest.raises(ValueError):       
        calc.log(-2,4)
    with pytest.raises(ValueError):       
        calc.log(0,4)
    with pytest.raises(ValueError):       
        calc.log(1,4)