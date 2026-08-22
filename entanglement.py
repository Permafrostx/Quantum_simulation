import numpy as np  
from gates import apply_gate, gate_h,gate_cnot
from qubit_state import is_normalized, normalize, ket_0, ket_1
from tensor import tensor_product
from measure import measure, plot
import math



if __name__ == '__main__':
    res_00 = apply_gate(gate_cnot, tensor_product(ket_0, ket_0))
    res_01 = apply_gate(gate_cnot, tensor_product(ket_0, ket_1))
    res_10 = apply_gate(gate_cnot, tensor_product(ket_1, ket_0))
    res_11 = apply_gate(gate_cnot, tensor_product(ket_1, ket_1))

    check_00 = np.allclose(res_00, tensor_product(ket_0, ket_0))
    check_01 = np.allclose(res_01, tensor_product(ket_0,ket_1))
    check_10 = np.allclose(res_10,tensor_product(ket_1, ket_1))
    check_11 = np.allclose(res_11,tensor_product(ket_1, ket_0))
    h0 = apply_gate(gate_h, ket_0)
    res_plus = apply_gate(gate_cnot, tensor_product(h0,ket_0))
    check_entanglement = np.allclose(res_plus, [1/math.sqrt(2), 0, 0, 1/math.sqrt(2)])

    etiquette = ['00','01','10','11'] 
    print(check_00)
    print(check_01)
    print(check_10)
    print(check_11)

    print(check_entanglement)
    print(is_normalized(res_plus))
    print(res_plus)
    
    draw_bell = measure(res_plus, etiquette)
    draw_prod = measure(tensor_product(h0, h0), etiquette)
    print(draw_bell)      
    print(draw_prod)      
    plot(draw_bell, etiquette)
    plot(draw_prod, etiquette)

