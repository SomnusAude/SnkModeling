from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ParticleElement:
    id: int
    mass: float
    size: float
    color: List[int]
    posX: float
    posY: float
    speedX: float
    speedY: float

    @staticmethod
    def from_dict(obj: Any) -> 'ParticleElement':
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("id")))
        mass = from_float(obj.get("mass"))
        size = from_float(obj.get("size"))
        color = from_list(from_int, obj.get("color"))
        posX = from_float(obj.get("posX"))
        posY = from_float(obj.get("posY"))
        speedX = from_float(obj.get("speedX"))
        speedY = from_float(obj.get("speedY"))
        return ParticleElement(id, mass, size, color, posX, posY, speedX, speedY)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(str(self.id))
        result["mass"] = to_float(self.mass)
        result["size"] = to_float(self.size)
        result["color"] = from_list(from_int, self.color)
        result["posX"] = to_float(self.posX)
        result["posY"] = to_float(self.posY)
        result["speedX"] = to_float(self.speedX)
        result["speedY"] = to_float(self.speedY)
        return result


def Particlefromdict(s: Any) -> List[ParticleElement]:
    return from_list(ParticleElement.from_dict, s)


def Particletodict(x: List[ParticleElement]) -> Any:
    return from_list(lambda x: to_class(ParticleElement, x), x)
