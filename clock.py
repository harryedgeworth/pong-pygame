import pygame


class Clock:
    def __init__(self, fps):
        self.framerate = fps
        self.frame_count = 0
        self.start_time = 90
        self.clock = pygame.time.Clock()
        self.total_seconds = 0
        self.minutes = 0
        self.seconds = 0
        self.output_string = None
        self.font = pygame.font.Font(None, 25)

    def tick(self):
        self.total_seconds = self.frame_count // self.framerate
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60

        self.output_string = "{0:02}:{1:02}".format(self.minutes, self.seconds)

        self.frame_count += 1