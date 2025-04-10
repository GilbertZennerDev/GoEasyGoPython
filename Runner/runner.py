import pygame
from sys import exit

class Runner:
    def runGame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption("Runner")
        
        self.blob_speed = 3
        self.blob_dir = 1
        
        self.font = pygame.font.Font("Pixeltype.ttf", 50)
        
        self.blob_x = 250
        
        self.clock = pygame.time.Clock()
        self.player_surface = pygame.image.load("Player.png")
        self.player_rect = self.player_surface.get_rect(midbottom=(50, 300))
        self.blob_surface = pygame.image.load("Blob.png")
        self.blob_rect = self.blob_surface.get_rect(midbottom=(self.blob_x, 300))
        self.tree_surface = pygame.image.load("Tree.png")
        self.tree_rect = self.tree_surface.get_rect(midbottom=(100, 300))
        self.grass_surface = pygame.image.load("Grass.jpg")
        self.grasss_rect = self.grass_surface.get_rect(midtop=(400, 300))
        self.sky_surface = pygame.image.load("Sky.jpg")
        self.text_surface = self.font.render("Alive", False, "Black")
        self.text_rect = self.text_surface.get_rect(center=(400, 50))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            
            self.screen.blit(self.sky_surface, (0, 0))
            self.screen.blit(self.grass_surface, self.grasss_rect)
            self.screen.blit(self.tree_surface, self.tree_rect)
            self.screen.blit(self.player_surface, self.player_rect)
            self.blob_rect.x -= 1
            self.screen.blit(self.blob_surface, self.blob_rect)
            pygame.draw.rect(self.screen, "Pink", self.text_rect)
            pygame.draw.rect(self.screen, "Pink", self.text_rect, 20)
            self.screen.blit(self.text_surface, self.text_rect)
            if self.player_rect.colliderect(self.blob_rect):
                print("Collision")
                self.text_surface = self.font.render("Dead", False, "Black")
            
            pygame.display.update()
            self.clock.tick(60)
            
runner = Runner()
runner.runGame()