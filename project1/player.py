from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt


        if keys[pygame.K_a]:
            self.rotate(-dt)
            #self.rotation = self.rotation - (PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            #self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer <= 0:
                self.shoot()
                self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED

# Creates a new Shot at the current position of the player.
# Sets the shot's .velocity attribute:
# Start with a pygame.Vector2 of (0, 1).
# .rotate() the vector in the direction the player is facing.
# Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.
# In your Player class, handle the spacebar (pygame.K_SPACE) and call the shoot method when it's pressed.
# Run your game for at least a few seconds, and fire some shots. Make sure the bullets are being created and moving in the correct direction.