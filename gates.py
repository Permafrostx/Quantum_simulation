import numpy as np 
import math
from qubit_state import is_normalized, ket_0, ket_1
from measure import measure

gate_x = np.array([ket_1, ket_0], dtype = complex)
gate_z = np.array([[1,0],[0,-1]], dtype = complex)
gate_h = np.array([(1/math.sqrt(2)*np.array([ket_0[0],ket_0[0]])),(1/math.sqrt(2)*np.array([ket_0[0],-(ket_1[1])]))], dtype = complex)
gate_cnot = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype = complex)



def apply_gate(gate, state):
    res = (gate @ state)
    return res


if __name__ == "__main__":

    etiquette = [0,1]

    resultat_gate_x0 = apply_gate(gate_x, ket_0)
    print(np.allclose(resultat_gate_x0, [0,1]))
    print(measure(resultat_gate_x0,[0,1]))
    print(is_normalized(resultat_gate_x0))
    print("----------")

    resultat_gate_x1 = apply_gate(gate_x, ket_1)
    print(np.allclose(resultat_gate_x1, [1,0]))
    print(measure(resultat_gate_x1,[0,1]))
    print(is_normalized(resultat_gate_x1))
    print("----------")


    resultat_gate_z0 = apply_gate(gate_z, ket_0)
    print(np.allclose(resultat_gate_z0, [1,0]))
    print(measure(resultat_gate_z0,[0,1]))
    print(is_normalized(resultat_gate_z0))
    print("----------")



    resultat_gate_z1 = apply_gate(gate_z, ket_1)
    print(np.allclose(resultat_gate_z1, [0,-1]))
    print(measure(resultat_gate_z1,[0,1]))
    print(is_normalized(resultat_gate_z1))
    print("----------")


    
    resultat_gate_h0 = apply_gate(gate_h, ket_0)
    print(np.allclose(resultat_gate_h0, [1/math.sqrt(2), 1/math.sqrt(2)]))
    print(measure(resultat_gate_h0,[0,1]))
    print(is_normalized(resultat_gate_h0))
    print("----------")

    
    resultat_gate_h1 = apply_gate(gate_h,ket_1)
    print(np.allclose(resultat_gate_h1, [1/math.sqrt(2), -(1/math.sqrt(2))]))
    print(measure(resultat_gate_h1,[0,1]))
    print(is_normalized(resultat_gate_h1))



