import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'yesplease'

import sys
from pygame import mixer
import glob
import random
import time

import typer
from rich import print

app = typer.Typer()


# load all mp3s
class mpy3_app:
    def __init__(self, skip: int = 1, shuffle: bool = False, find: str = '*'):
        self.load_tracks(find)
        if len(self.tracks) == 0:
            print(':face_with_raised_eyebrow: No tunes found - try running command in directory with mp3 files')
        self.skip = skip
        if shuffle:
            self.shuffle_tracks()
        self.play()

    def load_tracks(self, match_string):
        self.tracks = glob.glob(f'**/*{match_string}*.mp3', recursive=True)

    def shuffle_tracks(self):
        random.shuffle(self.tracks)
        mixer.init()

    def read_track_data(self, track, i):
        self.track_title = os.path.basename(track).rsplit('.', 1)[0]
        self.track_length = mixer.Sound(track).get_length()
        self.track_length = time.strftime('%M:%S', time.gmtime(self.track_length))
        self.track_number = f'[{i + self.skip}/{len(self.tracks)}]'

    def play(self):
        mixer.init()

        for i, track in enumerate(self.tracks[self.skip-1:]):
            mixer.music.load(track)
            self.read_track_data(track, i)
            mixer.music.play()
            while mixer.music.get_busy():
                self.track_progress = time.strftime(
                    '%M:%S', time.gmtime(mixer.music.get_pos() / 1000)
                )
                self.print_display()
                time.sleep(1)
            print('')

    def print_display(self):
        width = os.get_terminal_size().columns
        display = f'  >>  {self.track_number} [i]{self.track_title}[/i] {self.track_progress}/{self.track_length}'
        if len(display) > width:
            display = display[:width-1]
        else:
            display += (width - len(display) - 1) * ' '
        print(display, end='\r', flush=True)

def run_app():
    typer.run(mpy3_app)

if __name__ == '__main__':
    run_app()
