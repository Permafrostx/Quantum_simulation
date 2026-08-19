from gates import gate_x
from qubit_state import ket_0, ket_1
from measure import measure




class Circuit:


    def __init__(self,state):
        self.state = state

    def apply(self,gate):
        self.state = gate @ self.state

    def run_measure(self, etiquette):
        return measure(self.state, etiquette)

if __name__ == "__main__":
    c = Circuit(ket_0)
    c.apply(gate_x)
    print(c.run_measure(['0','1']))

    c = Circuit(ket_1)
    c.apply(gate_x)
    print(c.run_measure(['0','1']))

    c = Circuit(ket_0)
    c.apply(gate_x)
    c.apply(gate_x)
    print(c.run_measure(['0','1']))







