from dataclasses import dataclass

@dataclass
class Confini:
    dyad:int
    state1no:int
    state1ab: str
    state2no:int
    state2ab: str
    year : int
    conttype: int
    version:float

    def __str__(self):
        return f"{self.state1ab} - {self.state2ab}"
    def __hash__(self):
        return hash(f"{self.state1no} - {self.state2no}")