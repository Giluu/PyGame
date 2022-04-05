import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, image, x, y, direction, angle, name, rect, health, armor, speed, range, damage, rotation_speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.direction = direction
        self.angle = angle
        self.rotation_speed = rotation_speed
        self.rect = rect
        self.image = image
        self.name = name
        self.health = health
        self.armor = armor
        self.speed = speed
        self.range = range
        self.damage = damage
    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        if self.direction == -1:
            self.angle += self.rotation_speed
    def update(self):
        self.set_rotation()

class LightTank(Tank):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/lighttank.png')
        self.rect = self.image.get_rect(center = (640, 360))
        self.name = "Light Tank"
        self.direction = 0
        self.angle = 0
        self.health = 150
        self.armor = 10
        self.speed = 60
        self.range = 30
        self.damage = 75

class MediumTank(Tank):
    def __init__(self):
        self.image = pygame.image.load('assets/mediumtank.png')
        self.rect = self.image.get_rect(center = (640, 360))
        self.name = "Medium Tank"
        self.direction = 0
        self.angle = 0
        self.health = 300
        self.armor = 25
        self.speed = 45
        self.range = 30
        self.damage = 125

class HeavyTank(Tank):
    def __init__(self):
        self.image = pygame.image.load('assets/heavytank.png')
        self.rect = self.image.get_rect(center = (640, 360))
        self.name = "Heavy Tank"
        self.direction = 0
        self.angle = 0
        self.health = 600
        self.armor = 50
        self.speed = 30
        self.range = 30
        self.damage = 250


pygame.init()
screen = pygame.display.set_mode([500, 500])
icon = pygame.image.load('assets/mediumtank.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("PyTanks")

player1 = pygame.sprite.GroupSingle(LightTank())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player1.draw(screen)
    player1.update() 