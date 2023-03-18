from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class StateMachine:
    state = State.A

    def step(self):
        return self.update({
            State.A: [State.B, 0],
            State.C: [State.A, 4],
            State.D: [State.E, 5],
            State.E: [State.E, 7],
            State.F: [State.G, 8]
        })

    def mask(self):
        return self.update({
            State.A: [State.F, 1],
            State.B: [State.C, 2],
            State.C: [State.D, 3],
            State.E: [State.F, 6],
            State.F: [State.F, 9],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()


if __name__=="__main__":
    o = main()
    print(o.step())  # 0
    print(o.mask())  # 2
    print(o.step())  # 4
    print(o.step())  # 0
    #o.step()  # KeyError
    print(o.mask())  # 2
    print(o.mask())  # 3
    o.mask()  # KeyError
    o.step()  # 5
    o.step()  # 7
    o.mask()  # 6
    o.mask()  # 9
    o.step()  # 8