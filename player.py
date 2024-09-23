import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64)) #Change to 50 later!!
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        
        
        #Player Movement
        self.direction = pygame.math.Vector2(0,0) #More complicated coordinate system
        self.speed = 8 #Multiplies with the direction of the player to give it a sense of moving
        self.gravity = 0.8
        self.j_force = -16 #Jump force is negative because we want player to go up

    def get_input(self):
        keys = pygame.key.get_pressed()

        #Add some forward jumping too like SPACE + W makes jump farther
        #Maybe a def superjump()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self): #Gravity for the player
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.direction.y == 0:
            self.direction.y = self.j_force
    def update(self):
        self.get_input()
        