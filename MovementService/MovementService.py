from ParticleService.ParticleModel import ParticleElement


def wallCollision(particle: ParticleElement, xMax: float, yMax: float):
    posX = particle.posX
    posY = particle.posY
    speedX = particle.speedX
    speedY = particle.speedY
    size = particle.size

    # отражение от правой стенки
    if speedX > 0 and (size+posX) > xMax:
        particle.speedX = -speedX

    # отражение от левой стенки
    if speedX < 0 and (posX-size) < 0:
        particle.speedX = -speedX

    # отражение от нижней стенки
    if speedY < 0 and (posY-size) < 0:
        particle.speedY = -speedY

    # отражение от верхней стенки
    if speedY > 0 and (posY+size) > yMax:
        particle.speedY = -speedY


def movement(particle: ParticleElement, timeDelta: float) -> ParticleElement:
    posX = particle.posX
    posY = particle.posY
    speedX = particle.speedX
    speedY = particle.speedY

    particle.posX += speedX*timeDelta
    particle.posY += speedY*timeDelta
