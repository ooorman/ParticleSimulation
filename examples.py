import random

from simulation import Particle


def test1(gravity=0):
    p1 = Particle({'x': 100, 'y': 300}, 1, 10, gravity=gravity)
    p1.impulse_x = 10
    p2 = Particle({'x': 400, 'y': 300}, -1, 10, gravity=gravity)
    return p1,p2

def test2(gravity=0):
    particles = []
    for i in range(15):
        particles.append(Particle({'x': random.randint(0, 800), 'y': random.randint(0, 800)}, [-1, 1][random.randint(0, 1)], 10, gravity=gravity))
    return particles

def test3(gravity=0):
    p1 = Particle({'x': 350, 'y': 250}, 1, 10, gravity=gravity)
    p1.impulse_x = -20
    p2 = Particle({'x': 350, 'y': 300}, -1, 10, gravity=gravity)
    p2.impulse_x = 20
    return p1,p2

def test4(gravity=0):
    particles = []
    for i in range(0, 41, 2):
        if i == 0 or i == 40:
            continue
        particles.append(Particle({'x': i * 20, 'y': 300}, -1, 10, gravity=gravity))
    for i in range(0, 41, 2):
        if i == 0 or i == 40:
            continue
        particles.append(Particle({'x': i * 20, 'y': 250}, 1, 10, gravity=gravity))
    return particles
def test5(gravity=0):
    particles = []
    for i in range(2):
        particles.append(Particle({'x': 100 + i, 'y': 300}, 1, 10, gravity=gravity))
    return particles
def test6(gravity=0):
    particles = []
    for i in range(500):
        particles.append(Particle({'x': random.randint(2,798), 'y': random.randint(2,798)}, [-1,1][random.randint(0,1)], 10, gravity=gravity))
    return particles
def test7(gravity=0):
    particles = []
    for index_y, y in enumerate(range(0, 800, 80)):
        for index_x, x in enumerate(range(0, 800, 80)):
            if (index_y + index_x) % 2 == 0:
                particles.append(Particle({'x': x+40, 'y': y+40}, 1, 10, gravity=gravity))
            else:
                particles.append(Particle({'x': x+40, 'y': y+40}, -1, 20, gravity=gravity))
    return particles
def test8(gravity=0):
    particles = []
    for i in range(68):
        p = Particle({'x': 200, 'y': 750 - i * 11}, -1, 1, gravity=gravity)
        p.impulse_x = 1
        particles.append(p)
    for i in range(68):
        p = Particle({'x': 500, 'y': 741 - i * 11}, -1, 1, gravity=gravity)
        p.impulse_x = -1
        particles.append(p)
    return particles
def test9(gravity=0):
    particles = []
    for i in range(68):
        particles.append(Particle({'x': 200, 'y': 750 - i * 11}, -1, 1, gravity=gravity))
    for i in range(10):
        p = Particle({'x': 500, 'y': 300 + i * 11}, -1, 1, gravity=gravity)
        p.impulse_x = -1
        p.impulse_y = 1
        particles.append(p)
    return particles
def test10(gravity=0):
    particles = []
    for i in range(10):
        for j in range(10):
            particles.append(Particle({'x': 400 + i*11, 'y': 400 + j * 11}, 1, 1, gravity=gravity))
    for i in range(10):
        p = Particle({'x': 300, 'y': 400 + 11 * i}, 1, 1, gravity=gravity)
        p.impulse_x = 1
        particles.append(p)
    for i in range(10):
        p = Particle({'x': 400 + 11 * i, 'y': 300}, 1, 1, gravity=gravity)
        p.impulse_y = 1
        particles.append(p)
    return particles

def test11(gravity=0):
    particles = []
    for i in range(30):
        particles.append(Particle({'x': 250 + i*11, 'y': 400}, -1, 1, gravity=gravity))
    p = Particle({'x': 100, 'y': 400}, -1, 1, gravity=gravity)
    p.impulse_x = 3
    particles.append(p)
    return particles
