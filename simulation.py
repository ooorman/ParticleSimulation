import math
# import time
import time

import numpy as np
from scipy.spatial import KDTree
import pygame
from examples import *

pygame.init()
all_particles = []
activeHeight = 800
activeWidth = 800


class Particle:
    def __init__(self, position, power, weight, size=5):
        self.color = (255, 0, 0) if power == 1 else (0, 255, 0)
        self.size = size
        self.position = position
        self.power = power
        self.weight = weight
        self.action_radius = weight * 10
        self.impulse_x = 0
        self.impulse_y = 0
        self.collisions = []

    def get_particles_in_action_radius(self, tree, all_particles):
        self_x = self.position['x']
        self_y = self.position['y']
        self_power = self.power
        self.collisions.clear()
        indices = tree.query_ball_point([self_x, self_y], self.action_radius)
        for idx in indices:
            particle = all_particles[idx]
            if particle is not self:
                dx = particle.position['x'] - self_x
                dy = particle.position['y'] - self_y
                dist = dx * dx + dy * dy
                if dist != 0:
                    self.collisions.append(particle)
                    factor = particle.power * self_power / math.sqrt(dist)
                    particle.impulse_y += dy * factor
                    particle.impulse_x += dx * factor

    def impulse_to_coords(self):
        self.position['x'] += int(self.impulse_x) / self.weight
        self.position['y'] += int(self.impulse_y) / self.weight


def render_particles(screen, particles_list, selection, font, rentgen, is_stop):
    screen.fill((255, 255, 255))
    # Отрисовка выделенной области и подсчет частиц внутри нее
    if selection:
        pygame.draw.rect(screen, (0, 0, 180), selection)
    # Отрисовка линий для rentgen
    if rentgen:
        processed_collisions = set()

        for particleA in particles_list:
            for particleB in particleA.collisions:
                if particleB not in processed_collisions:
                    pygame.draw.line(screen, (150, 150, 150), (particleA.position['x'], particleA.position['y']), (particleB.position['x'], particleB.position['y']), 2)
                    processed_collisions.add(particleA)
    # Отрисовка всех частиц
    for particle in particles_list:
        pygame.draw.circle(screen, particle.color, (particle.position['x'], particle.position['y']), particle.size)

    if selection:
        pr_count = sum(1 for particle in particles_list if selection.collidepoint(particle.position['x'], particle.position['y']) and particle.power == 1)
        el_count = sum(1 for particle in particles_list if selection.collidepoint(particle.position['x'], particle.position['y']) and particle.power != 1)
        sum_energy = round(sum(abs(particle.impulse_x) + abs(particle.impulse_y) for particle in particles_list if selection.collidepoint(particle.position['x'], particle.position['y'])))

        text = f"{sum_energy}, -{el_count}, +{pr_count}"
        screen.blit(font.render(text, True, (255, 255, 255)), (selection.bottomright[0] - len(text) * 10, selection.bottomright[1] - 30))
    # Отображение общей кинетической энергии, если игра остановлена
    if is_stop:
        total_kinetic_energy = round(sum(abs(particle.impulse_y + particle.impulse_x) for particle in particles_list))
        text = f"Общее кол-во кинетической энергии: {total_kinetic_energy}"
        screen.blit(font.render(text, True, (0, 0, 0)), (activeWidth - len(text) * 11, activeHeight - 50))

    pygame.display.update()


def main():
    global all_particles

    screen = pygame.display.set_mode((activeWidth, activeHeight))
    pygame.display.set_caption('Симуляция')

    # #Заполняем массив частицами из тестовых примеров. Можно поменять на test2 и т.д.
    all_particles += test1()

    stop = False
    clock = pygame.time.Clock()
    selection = None
    first_selecting_pos = None
    font = pygame.font.SysFont('Comic Sans', 20)
    FPS = 60
    selecting = False
    rentgen = False
    while True:

        time_start = time.time()
        if not pygame.mouse.get_pressed()[0]:
            selecting = False
        if pygame.key.get_pressed()[pygame.K_UP]:
            if FPS + 10 <= 5000:
                FPS += 10
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            if FPS - 10 >= 60:
                FPS -= 10
        if not stop:
            tree = KDTree(np.array([[p.position['x'], p.position['y']] for p in all_particles]))

            for particle in all_particles:
                particle.get_particles_in_action_radius(tree, all_particles)

            for particle in all_particles:
                if not 0 < particle.position['x'] + particle.impulse_x / particle.weight < activeWidth:
                    particle.impulse_x *= -1
                if not 0 < particle.position['y'] + particle.impulse_y / particle.weight < activeHeight:
                    particle.impulse_y *= -1
                particle.impulse_to_coords()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = True if not stop else False
                elif event.key == pygame.K_r:
                    rentgen = True if not rentgen else False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                first_selecting_pos = pygame.mouse.get_pos()
                selecting = True
            elif event.type == pygame.MOUSEMOTION:
                if selecting:
                    pos = event.pos
                    width = pos[0] - first_selecting_pos[0]
                    height = pos[1] - first_selecting_pos[1]
                    x, y = first_selecting_pos[0], first_selecting_pos[1]
                    w, h = width, height
                    if w < 0:
                        w = -w
                        x = x - w
                    if h < 0:
                        h = -h
                        y = y - h
                    selection = pygame.Rect(x, y, w, h)
                else:
                    first_selecting_pos = False
                    selection = False
        render_particles(screen, all_particles, selection, font, rentgen, stop)
        print(time.time() - time_start)
        clock.tick(FPS)


if __name__ == '__main__':
    main()
