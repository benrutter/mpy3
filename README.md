# mpy3 🐍
Ultra-minimal cli mp3 player

Want to play mp3 without distractions like GUIs, playlists or features? Look no further!

mpy3 is a very, very, veeerrry simple command line mp3 player that can be pip installed.

Navigate to a folder with mp3s in it (or in a subdirectory) using the command line and run:

```bash
$ mpy3
```

You should see something like this (and importantly hear music):

```bash
 >>  [1/12] Patricia Wolf - See-Through - 01 Woodland Encounter 00:02/06:07
```

That's basically it, stop playing with ctrl+c to exit the script, otherwise, it'll keep playing until it runs out of mp3s.

A few extra features. . . .

*Skip past some songs*
```bash
$ mpy3 --skip 3
  >>  [3/11] morimoto naoki - kotoba - 03 koyoi 00:00/03:21
```

*Shuffle everything in the folder*
```bash
$ mpy3 --shuffle
  >>  [1/11] wait what - the notorious xx - 07 everyday shelter -the notorious b.i.g. vs. the xx- 00:17/03:35
```

*Takes glob-like search strings to quickly filter for an album etc*
```bash
$ mpy3 --find Almanacs
  >>  [1/1] Almanacs - Templo Animal - Vol. 2 - 04 Starfields 00:02/06:08
```

That's literally everything you can do - enjoy!


# Installation / Dependencies

This whole tool is basically just a simple wrapper over the top of pygame's ability to read and play mp3s with typer.

It's only about 50 lines of code total, and most of the actual work is done by it's dependencies:
- Pygame
- Typer
- Rich

Installation is through pip:
```bash
pip install mpy3
```

