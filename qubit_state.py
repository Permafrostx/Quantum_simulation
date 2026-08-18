import numpy as np 

ket_0 = np.array([1,0], dtype = complex)
ket_1 = np.array([0,1], dtype = complex)
raw_state = np.array([2,9], dtype = complex)

def squared_norm(state):
    res = np.sum(np.abs(state)**2)
    return res

def is_normalized(state):
    res = squared_norm(state)
    return np.isclose(res,1) #I used isclose and not "==" because the floating point could give 0.9999 instead of 1



def normalize(state):
    return state/np.sqrt(squared_norm(state))



if __name__ == "__main__":

    print(squared_norm(ket_0))
    print(squared_norm(ket_1))
    print(is_normalized(ket_0))
    print(is_normalized(ket_1))
    print(is_normalized(raw_state)) #should be false
    print(normalize(ket_0))
    print(normalize(raw_state))
    print(squared_norm(raw_state))
    print(is_normalized((normalize(raw_state)))) #should be True






