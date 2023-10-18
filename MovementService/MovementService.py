from ParticleService.ParticleModel import ParticleElement
import numpy as np


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

def particleCollision(particle1:ParticleElement, particle2:ParticleElement):
    if np.sqrt((particle1.posX-particle2.posX)**2 + (particle1.posY-particle2.posY)**2) < (particle1.size + particle2.size):
        velocityX = particle1.speedX -  particle2.speedX
        velocityY = particle1.speedY -  particle2.speedY
        phi = np.random.rand()*2*np.pi
        velocityCenterX = (particle1.mass*particle1.speedX + particle2.mass*particle2.speedX) / (particle1.mass + particle2.mass) 
        velocityCenterY = (particle1.mass*particle1.speedY + particle2.mass*particle2.speedY) / (particle1.mass + particle2.mass)
        particle1.speedX = particle2.mass/(particle1.mass + particle2.mass) * (np.cos(phi)*velocityX+np.sin(phi)*velocityCenterX) + velocityCenterX
        particle1.speedY = particle2.mass/(particle1.mass + particle2.mass) * (np.cos(phi)*velocityY+np.sin(phi)*velocityCenterY) + velocityCenterY
        particle2.speedX = -particle1.mass/(particle1.mass + particle2.mass) * (np.cos(phi)*velocityX+np.sin(phi)*velocityCenterX) + velocityCenterX
        particle2.speedY = -particle1.mass/(particle1.mass + particle2.mass) * (np.cos(phi)*velocityY+np.sin(phi)*velocityCenterY) + velocityCenterY