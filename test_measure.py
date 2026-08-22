from measure import measure 
from qubit_state import ket_0
import numpy as np 
import math

state = np.array([math.sqrt(0.8),math.sqrt(0.2)], dtype = complex)
raw_state = np.array([math.sqrt(3), math.sqrt(7)], dtype = complex)
h = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype = complex)
etiquette = [0,1]

def test_measure():
    assert measure(ket_0, etiquette) == [1000,0]
    
    result1 = measure(state,etiquette) 
    assert (700 <= result1[0] <= 900) and (100 <= result1[1] <= 300)
    assert sum(result1) == 1000

def test_measure_superposition():
    result2 = measure(h,etiquette)
    assert (400 <= result2[0] <= 600) and (400 <= result2[1] <= 600)
    assert sum(result2) == 1000

def test_measure_unnormalized():
    result3 = measure(raw_state,etiquette)
    assert (200 <= result3[0] <= 400) and (600 <= result3[1] <= 800)
    assert sum(result3) == 1000






