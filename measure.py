import numpy as np
import math
import matplotlib.pyplot as plt

ket_0 = np.array([1,0], dtype = complex)
state = np.array([math.sqrt(0.8),math.sqrt(0.2)], dtype = complex)
raw_state = np.array([math.sqrt(3), math.sqrt(7)], dtype = complex)


def squared_norm(state):
    res = np.sum(np.abs(state)**2)
    return res


def is_normalized(state):
    return np.isclose(squared_norm(state),1)


def normalize(state):
    return state/np.sqrt(squared_norm(state))


def biased(state):
    rand = np.random.random()
    if rand <= np.abs(state[0])**2:
        return 0 
    else:
        return 1


def repeat(state):
    lst = []
    for i in range(1000):
        result = biased(state)
        lst.append(result)
    return lst



def count(liste):
    a = 0 
    b = 0 
    for i in range(len(liste)):
        if liste[i] == 0:
            a+=1 
        else:
            b+=1 
    return [a,b]



def plot(liste2):
    liste1 = ['0','1']
    plt.bar(liste1, liste2, color='skyblue')
    plt.xlabel('Measured outcome')
    plt.ylabel('Number of measurements')
    plt.title('Measurement results over 1000 shots')
    plt.show()
    

def measure(state):
    check = is_normalized(state)
    if check == False:
        print("Unnormalized state: ", state,", normalizing...")
        state = normalize(state)
    lst = repeat(state)
    res = count(lst)
    return res

m_ket = measure(ket_0)
m_state = measure(state)
m_raw = measure(raw_state)
print(m_ket)
print(m_state)
print(m_raw)

plot(m_ket)
plot(m_state)
plot(m_raw)

















