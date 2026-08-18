import numpy as np
import math
import matplotlib.pyplot as plt
from qubit_state import is_normalized, normalize, ket_0

def biased(state, etiquette):
    rand = np.random.random()
    if len(etiquette) == 2:
        if rand <= np.abs(state[0])**2:
            return etiquette[0]
        else:
            return etiquette[1]
    elif len(etiquette) == 4:
        place0 = np.abs(state[0])**2 
        place1 = np.abs(state[1])**2 
        place2 = np.abs(state[2])**2 
        if rand <= place0 :
            return etiquette[0]
        elif rand > place0 and rand <= (place0 + place1):
            return etiquette[1]
        elif rand > (place0 + place1) and rand <= (place0 + place1 + place2):
            return etiquette[2]
        else:
            return etiquette[3]
    else:
        print("Etiquette error")
        return None

def repeat(state, etiquette):
    lst = []
    for i in range(1000):
        result = biased(state, etiquette)
        lst.append(result)
    return lst


def counter(lst, etiquette):
    res = [0] * len(etiquette)

    for resultat in lst:
        position = etiquette.index(resultat)
        res[position] += 1

    return res

def plot(liste1, etiquette):
    if len(etiquette) ==2:
        plt.bar([str(etiquette[0]),str(etiquette[1])], liste1, color='skyblue')
    else:
        plt.bar(etiquette,liste1, color='skyblue')

    plt.xlabel('Measured outcome')
    plt.ylabel('Number of measurements')
    plt.title('Measurement results over 1000 shots')
    plt.show()

def measure(state, etiquette):
    check = is_normalized(state)
    if not check:
        print("Unnormalized state:", state,", normalizing...")
        state = normalize(state)
    lst = repeat(state, etiquette)
    res = counter(lst, etiquette)
    return res


if __name__ == "__main__":

    state = np.array([math.sqrt(0.8),math.sqrt(0.2)], dtype = complex)
    raw_state = np.array([math.sqrt(3), math.sqrt(7)], dtype = complex)
    h = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype = complex)
    etiquette = [0,1]
    m_ket = measure(ket_0,etiquette)
    m_state = measure(state,etiquette)
    m_raw = measure(raw_state, etiquette)
    print(m_ket)
    print(m_state)
    print(m_raw)

    plot(m_ket,etiquette)
    plot(m_state, etiquette)
    plot(m_raw,etiquette)
    print(measure(h,etiquette))
    plot(measure(h,etiquette),etiquette)

   













