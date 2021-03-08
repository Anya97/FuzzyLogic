import os, pygame
from math import radians
from pygame.math import Vector2
from utils import *
from fozzy_control import *        

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Foozy Logic")

        self.width = 800
        self.height = 800

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        drone = Drone(470, 30) #позиция дрона

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "drone1.png")
        drone_image = pygame.image.load(image_path)

        target = Vector2(30, 470) #позиция цели

        drone_speed = 1 #скорость дрона

        while not self.exit: # будет работать пока не закрыть окно
            dt = self.clock.get_time() / 1000 # для плавности движения

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # pressed = pygame.key.get_pressed()

            # Logic

            if (drone.position.distance_to(target) > 20): #если отклонение в 20 пикселей, то будет выполн
                Xc = int(target.x - drone.position.x) # разница по х
                Yc = int(target.y - drone.position.y) # разница по Y

                degreesAngle = processRules(Xc, Yc) # запускаем процессор и получаем угол в град
                dirAngle = get_direction(radians(degreesAngle)) # задаем вектор направления движения

                drone.velocity += Vector2(mult_tuple(dirAngle, drone_speed * dt)) #скорость дрона
            else:
                drone.velocity = Vector2(0.0, 0.0) #прекращение движения

            drone.update(dt) #обновление позиции

            # Drawing
            self.screen.fill((0,0,0))

            self.show_text(f"({drone.position.x:0.2f}, {drone.position.y:0.2f}) | (500, 500)", (60, 50))
            self.screen.blit(drone_image, drone.get_position())

            self.show_text(f"Speed: {drone.velocity.x:.0f} km/h", (100, 10))
            crcl = pygame.draw.circle(self.screen, (50, 100, 80), v2_to_tuple(target), 5)
            
            pygame.display.flip()

            self.clock.tick(self.ticks)

        pygame.quit()

    def _text_objects(self, text, font):
        textSurf = font.render(text, True, (255,255,255))
        return textSurf, textSurf.get_rect()


    def show_text(self, text, pos):
        textFont = pygame.font.Font('arial_bold.ttf', 30)
        textSurf, textRect = self._text_objects(text, textFont)
        textRect.center = ((textRect.center[0] + pos[0]), (textRect.center[1] + pos[1]))
        self.screen.blit(textSurf, textRect)

class Drone(): #логика дрона
    def __init__(self, x, y, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)

        self.max_acceleration = max_acceleration

        self.acceleration = 0.0
        self.max_velocity = 50

    def update(self, dt):
        self.velocity = Vector2(max(-self.max_velocity, min(self.max_velocity, self.velocity.x)),
                                max(-self.max_velocity, min(self.max_velocity, self.velocity.y)))
        self.position += self.velocity

    def get_position(self):
        return (int(self.position.x - 50), int(self.position.y - 50))

