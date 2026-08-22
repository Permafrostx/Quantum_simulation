from qubit_state import squared_norm, is_normalized, normalize, ket_0, ket_1, raw_state
import numpy as np



def test_squared_norm():
    assert np.allclose(squared_norm(ket_0),1)
    assert np.allclose(squared_norm(ket_1),1)
    assert not np.allclose(squared_norm(raw_state),1)

def test_is_normalized():
    assert is_normalized(ket_0)
    assert is_normalized(ket_1)
    assert not is_normalized(raw_state)

def test_normalized():
    assert np.allclose(normalize(ket_0),[1,0])
    assert np.allclose(normalize(ket_1),[0,1])
    assert is_normalized(normalize(raw_state))






