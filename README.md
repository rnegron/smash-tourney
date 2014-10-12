smash-versus-tourney
===================

The Super Smash Bros. 2v2 randomizer and announcer voice implementer...!

## About

A simple python script that, given a list of player names, outputs a random pairing of them (representing two players who will fight) and creates .wav files for each pairing. The .wav file is contains a text-to-speech reading of the first player's name, followed by the classic "VERSUS" line, and ends with the second player's name.

smash-versus-tourney currently uses the Super Smash Bros. for 3DS version of the announcer voice. The `versus.wav` file in this repository was downloaded from [The Sounds Resource](http://www.sounds-resource.com/other_systems/supersmashbrosfornintendo3ds/sound/3535/).
## How to use

_**Intended for use with a Python 3 interpreter**_.

smashtourney.py uses [pydub](https://github.com/jiaaro/pydub/) to handle audio files. `pydub` can be easily installed using `pip`:

`$ pip install pydub`

and you're ready to run the script! 

`$ python3 smashtourney.py`

**IMPORTANT**

smashtourney.py will create a folder called `tourney`, where it will store the created .wav files for convenience.

## To-Do
- [x] Allow different TTS languages 
- [ ] Allow different announcer voices (from past Smash games)
-  [ ] General clean-up
-  [ ] Better error-checking and handling


## License (MIT)

Copyright (c) 2014 Raúl Negrón

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.