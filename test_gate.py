import numpy as np 
from gates import gate_x, gate_z, gate_h, apply_gate, gate_cnot
from qubit_state import ket_0, ket_1, is_normalized
from tensor import tensor_product 
import math




def test_gate_X():
    result_gate_x0 = apply_gate(gate_x, ket_0)
    assert np.allclose(result_gate_x0, [0,1])
    assert is_normalized(result_gate_x0)

    result_gate_x1 = apply_gate(gate_x, ket_1)
    assert np.allclose(result_gate_x1, [1,0])
    assert is_normalized(result_gate_x1)

def test_gate_Z():
    result_gate_z0 = apply_gate(gate_z, ket_0)
    assert np.allclose(result_gate_z0, [1,0])
    assert is_normalized(result_gate_z0)

    result_gate_z1 = apply_gate(gate_z, ket_1)
    assert np.allclose(result_gate_z1, [0,-1])
    assert is_normalized(result_gate_z1)

def test_gate_H():
    result_gate_h0 = apply_gate(gate_h, ket_0)
    assert np.allclose(result_gate_h0, [1/math.sqrt(2), 1/math.sqrt(2)])
    assert is_normalized(result_gate_h0)

    result_gate_h1 = apply_gate(gate_h,ket_1)
    assert np.allclose(result_gate_h1, [1/math.sqrt(2), -(1/math.sqrt(2))])
    assert is_normalized(result_gate_h1)

def test_gate_CNOT():
    res_00 = apply_gate(gate_cnot, tensor_product(ket_0, ket_0))
    res_01 = apply_gate(gate_cnot, tensor_product(ket_0, ket_1))
    res_10 = apply_gate(gate_cnot, tensor_product(ket_1, ket_0))
    res_11 = apply_gate(gate_cnot, tensor_product(ket_1, ket_1))

    assert np.allclose(res_00, tensor_product(ket_0, ket_0))
    assert np.allclose(res_01, tensor_product(ket_0,ket_1))
    assert np.allclose(res_10,tensor_product(ket_1, ket_1))
    assert np.allclose(res_11,tensor_product(ket_1, ket_0))




def test_Bell_state():
    h0 = apply_gate(gate_h, ket_0)
    result_Bell_state = apply_gate(gate_cnot, tensor_product(h0,ket_0))
    assert np.allclose(result_Bell_state, [1/math.sqrt(2), 0, 0, 1/math.sqrt(2)])
    assert np.allclose(result_Bell_state[1],0)
    assert np.allclose(result_Bell_state[2],0)
    assert is_normalized(result_Bell_state)











