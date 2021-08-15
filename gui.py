import pygame

class DrawGUI:
    def __init__(self):
        self.width, self.height = 280, 280
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Draw Number')
        pygame.display.flip()
        self.running = True
        self.draw_handler()
    def draw_handler(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            color = (255,0,0)
            pygame.draw.rect(self.screen, color, pygame.Rect(30, 30, 60, 60))
            pygame.display.flip()
if __name__ == "__main__":
    DrawGUI()