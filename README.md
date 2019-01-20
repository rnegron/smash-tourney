# smash-tourney

[![Build Status](https://travis-ci.org/rnegron/smash_tourney.svg?branch=master)](https://travis-ci.org/rnegron/smash_tourney)
[![Coverage Status](https://coveralls.io/repos/github/rnegron/smash_tourney/badge.svg?branch=master)](https://coveralls.io/github/rnegron/smash_tourney?branch=master)
[![Updates](https://pyup.io/repos/github/rnegron/smash_tourney/shield.svg)](https://pyup.io/repos/github/rnegron/smash_tourney/)
[![Python 3](https://pyup.io/repos/github/rnegron/smash_tourney/python-3-shield.svg)](https://pyup.io/repos/github/rnegron/smash_tourney/)

## About

A simple Python script that, given a list of player names, outputs a random pairing of them (representing two players who will fight) and creates .mp3 files for each pairing. The .mp3 file contains a text-to-speech reading of the first player's name, followed by a customizable phrase (say, a classic "VERSUS" line?) and ends with the second player's name.

smash_tourney accepts a `versus.wav` file in your working directory. This is used to customize the sound used in the end result. Previously, I had included the file in this repository, but I'm not quite sure I'm allowed to do that. Instead, I'll link to [The Sounds Resource](http://www.sounds-resource.com/), where you can find Smash Bros announcer voice samples. Make sure the file is called `versus.wav` inside your working directory!

## How to use

_**Intended for use with Python >= 3.6**_.

smash_tourney depends on two external libraries: [pydub](https://github.com/jiaaro/pydub/) to handle audio files and [gTTS](https://github.com/pndurette/gTTS) to interface with Google's text-to-speech API.

You can install smash_tourney using pip!

`$ pip install smash-tourney`

Next, you'll need to create a file with line-separated names for the players who will be participating the the tourney.

You're ready to run the script! Suppose the file with the player names is called `names.txt` in the current directory. Then simply run:

`$ smash-tourney names.txt`

**IMPORTANT**

smash_tourney will create a folder called `tourney` in its working directory, where it will store the created .wav files for convenience.
