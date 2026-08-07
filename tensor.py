from measure import is_normalized
from gates import gate_x, gate_z, gate_h, apply_gate 
import numpy as np 
import math 



ket_0 = np.array([1,0], dtype = complex)
ket_1 = np.array([0,1], dtype = complex)


def tensor_product(state1, state2):
    res = np.kron(state1,state2)
    return res


if __name__ == '__main__':

    ket_plus = apply_gate(gate_h, ket_0)
    res = tensor_product(ket_plus,ket_plus)
    res2 = tensor_product(ket_0,ket_0)
    res3 = tensor_product(ket_0, ket_1)
    res4 = tensor_product(ket_0, ket_plus)
    res5 =  tensor_product(ket_1, ket_plus)
    print(np.allclose(res2, [1,0,0,0]))
    print(np.allclose(res3, [0,1,0,0]))
    print(np.allclose(res4, [1/math.sqrt(2),1/math.sqrt(2),0,0]))
    print(np.allclose(res5, [0,0,1/math.sqrt(2),1/math.sqrt(2)]))

    print(is_normalized(res))
    print(is_normalized(res2))
    print(is_normalized(res3))
    print(is_normalized(res4))
    print(is_normalized(res5))



