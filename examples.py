import random

from simulation import Particle


def test1():
    p1 = Particle({'x': 100, 'y': 300}, 1, 10)
    p1.impulse_x = 10
    p2 = Particle({'x': 400, 'y': 300}, -1, 10)
    return p1,p2

def test2():
    particles = []
    for i in range(15):
        particles.append(Particle({'x': random.randint(0, 800), 'y': random.randint(0, 800)}, [-1, 1][random.randint(0, 1)], 10))
    return particles

def test3():
    p1 = Particle({'x': 350, 'y': 250}, 1, 10)
    p1.impulse_x = -20
    p2 = Particle({'x': 350, 'y': 300}, -1, 10)
    p2.impulse_x = 20
    return p1,p2

def test4():
    particles = []
    for i in range(0, 41, 2):
        if i == 0 or i == 40:
            continue
        particles.append(Particle({'x': i * 20, 'y': 300}, -1, 10))
    for i in range(0, 41, 2):
        if i == 0 or i == 40:
            continue
        particles.append(Particle({'x': i * 20, 'y': 250}, 1, 10))
    return particles
def test5():
    particles = []
    for i in range(2):
        particles.append(Particle({'x': 100 + i, 'y': 300}, 1, 10))
    return particles
def test6():
    particles = []
    for i in range(2000):
        particles.append(Particle({'x': random.randint(2,798), 'y': random.randint(2,798)}, [-1,1][random.randint(0,1)], 10))
    return particles

def test7():
    particles = []
    for i in range(10):
        for j in range(10):
            particles.append(Particle({'x': 400 + i*11, 'y': 400 + j * 11}, 1, 1))
    for i in range(10):
        p = Particle({'x': 300, 'y': 400 + 11 * i}, 1, 1)
        p.impulse_x = 1
        particles.append(p)
    for i in range(10):
        p = Particle({'x': 400 + 11 * i, 'y': 300}, 1, 1)
        p.impulse_y = 1
        particles.append(p)
    return particles

def test8():
    particles = []
    for i in range(30):
        particles.append(Particle({'x': 250 + i*11, 'y': 400}, -1, 1))
    p = Particle({'x': 100, 'y': 400}, -1, 1)
    p.impulse_x = 3
    particles.append(p)
    return particles
def test9():
    p1 = Particle({'x':400,'y':400}, -1, 100)
    p2 = Particle({'x':400,'y':300}, 1, 1)
    p21 = Particle({'x':400,'y':300}, 1, 1)
    p3 = Particle({'x':300,'y':400}, 1, 1)
    p31 = Particle({'x':300,'y':400}, 1, 1)
    p4 = Particle({'x':500,'y':400}, 1, 1)
    p41 = Particle({'x':500,'y':400}, 1, 1)
    p5 = Particle({'x':400,'y':500}, 1, 1)
    p51 = Particle({'x':400,'y':500}, 1, 1)

    p2.impulse_x = -10
    p2.impulse_y = 10

    p3.impulse_x = 10
    p3.impulse_y = 10

    p4.impulse_x = -10
    p4.impulse_y = -10

    p5.impulse_x = 10
    p5.impulse_y = -10

    return [p1,p2,p3,p4,p5, p21, p31,p41,p51]
