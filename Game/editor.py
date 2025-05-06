import pygame, sys
import gamemodule as g
import sceneeditor

class Editor():
    def run(self):
        pygame.init()
        pygame.font.init()
        self.scene = 'editor'
        self.state = ''
        self.state_edit = ''
        self.resolution = [1280, 800]
        self.surface = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync = 1)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.delta = 1 / self.FPS
        self.loop()

    def loop(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_scene()
            self.handle_input()

    def handle_scene(self):
        if self.scene == 'editor':
            sceneeditor.loop(self)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                button = event.button

                if self.scene == 'editor':
                    sceneeditor.mouse_down(self, pos, button)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                button = event.button

                if self.scene == 'editor':
                    sceneeditor.mouse_up(self, pos, button)

            if event.type == pygame.KEYDOWN:
                key = event.key

                if self.scene == 'editor':
                    sceneeditor.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key

                if self.scene == 'editor':
                    sceneeditor.key_up(self, key)

if __name__ == '__main__':
    Editor().run()
