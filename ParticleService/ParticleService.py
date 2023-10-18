from ParticleService.ParticleModel import ParticleElement
from random import choice
import numpy as np

defaultIdList = "0123456789qwertyuiopasdfghjklzxcvbnm"
defaultNumberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# TODO: Добавить возможность выбора параметров частицы


def generateParticle(maxX: int, maxY: int) -> ParticleElement:
    id = "".join([choice(defaultIdList) for i in range(9)])
    size = choice(defaultNumberList)+choice(defaultNumberList)/10
    particle = ParticleElement(
        id=id,
        mass=choice(defaultNumberList)+choice(defaultNumberList)/10,
        size=size,
        color=[choice(range(0, 2)) for i in range(3)],
        posX=round(np.random.rand()*(maxX-2*size), 1),
        posY=round(np.random.rand()*(maxY-2*size), 1),
        speedX=choice(range(0, 10)),
        speedY=choice(range(0, 10))
    )
    print(f"Generated new particle {particle}")
    return particle
