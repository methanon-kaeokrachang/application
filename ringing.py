import pygame
import threading
import time

class SoundPlayer(threading.Thread):

    def __init__(self, sound_file):
        super().__init__()
        self.sound_file = sound_file
        self.should_stop = False
        self.start_time = time.time()
        self.end_time = 0
        self.duration = 0


    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()
        pygame.time.delay(1500)
        pygame.mixer.music.stop()

