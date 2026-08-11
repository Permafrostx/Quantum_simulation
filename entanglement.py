import numpy as np  
from gates import apply_gate, ket_0, ket_1, gate_h
from measure import is_normalized, normalize
from tensor import tensor_product
import math
import matplotlib.pyplot as plt


gate_cnot = np.array([tensor_product(ket_0,ket_0),tensor_product(ket_0, ket_1),tensor_product(ket_1,ket_1), tensor_product(ket_1, ket_0)])


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




def biased2(state):
    rand = np.random.random()
    place0 = np.abs(state[0])**2 
    place1 = np.abs(state[1])**2 
    place2 = np.abs(state[2])**2 
    if rand <= place0 :
        return '00' 
    elif rand > place0 and rand <= (place0 + place1):
        return '01'
    elif rand > (place0 + place1) and rand <= (place0 + place1 + place2):
        return '10'
    else:
        return '11'

def loop(state):
    lst = []
    for i in range(1000):
        res = biased2(state)
        lst.append(res)
    return lst

def counter(liste):
    a = b = c = d = 0
    for i in range(1000):
        if liste[i] == '00':
            a+=1 
        elif liste[i] == '01':
            b+=1 
        elif liste[i] == '10':
            c+=1 
        else:
            d+=1 
    return [a,b,c,d]

def measure2(state):

    check = is_normalized(state)
    if not check:
        print("Unnormalize state",state," normalizing")
        state = normalize(state)
    lst = loop(state)
    res = counter(lst)
    return res


def plot2(liste):
    liste1 = ['00','01','10','11']
    plt.bar(liste1, liste, color = 'red')
    plt.xlabel('Measured outcome')
    plt.ylabel('Number of measurements')
    plt.title('Measurement results over 1000 shots')
    plt.show()
      

if __name__ == '__main__':
    
    print(check_00)
    print(check_01)
    print(check_10)
    print(check_11)

    print(check_entanglement)
    print(is_normalized(res_plus))
    print(res_plus)
    draw1 = measure2(res_plus)
    
    draw2 = measure2(tensor_product(h0,h0))

    plot2(measure2(res_plus))
    plot2(measure2(tensor_product(h0,h0)))






