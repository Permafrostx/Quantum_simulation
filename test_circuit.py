from circuit import Circuit
from gates import gate_x
from qubit_state import ket_0, ket_1
import numpy as np 

def test_circuit_apply():
    c = Circuit(ket_0)
    assert np.allclose(c.state,ket_0)
    c.apply(gate_x)
    assert np.allclose(c.state,ket_1)
    c.apply(gate_x)
    assert np.allclose(c.state,ket_0)

def test_circuit_measure():
    c = Circuit(ket_0)
    assert np.allclose(c.run_measure(['0','1']),[1000,0])
