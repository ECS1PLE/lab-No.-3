from dataclasses import dataclass

@dataclass(frozen=True)
class addressRecord:
    city: str
    street: str
    house: str
    floor: int