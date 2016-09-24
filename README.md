smash-versus-tourney
===================

The Open Source Super Smash Bros. 1v1 randomizer and announcer voice implementer (written in Python 3)!
## About

A simple python script that, given a list of player names, outputs a random pairing of them (representing two players who will fight) and creates .wav files for each pairing. The .wav file contains a text-to-speech reading of the first player's name, followed by the classic "VERSUS" line, and ends with the second player's name.

smash-versus-tourney expects a `versus.wav` file in the same folder as `smash_tourney.py`. Previously, I
had included the file in this repository, but I'm not quite sure I'm allowed to do that. Instead, I'll link to
[The Sounds Resource](http://www.sounds-resource.com/3ds/supersmashbrosfornintendo3ds/sound/3535/), where you can find the announcer voice samples (in this case, Xander Mobus from Smash 4). Look for the 'snd_se_narration_menu_00000013.wav' file inside the 'snd_se_narration_menu' folder. Make sure the file is called `versus.wav` inside your working directory!

## How to use

_**Intended for use with a Python 3 interpreter**_.

smashtourney.py uses [pydub](https://github.com/jiaaro/pydub/) to handle audio files and [gTTS](https://github.com/pndurette/gTTS) to interface with Google's text-to-speech API.

Both can be easily installed using `pip`:

`$ pip install pydub`

`$ pip install gTTS`

Alternatively, you may use the provided `requirements.txt` file to install the dependencies:

`$ pip install -r requirements.txt`

Next, you'll need to create a `names.txt` file in the same directory as `smash_tourney.py`. In the text file, insert line-separated names for the players who will be participating in the tourney.


You're ready to run the script!

`$ python3 smash_tourney.py`

**IMPORTANT**

smash_tourney.py will create a folder called `tourney` in its working directory, where it will store the created .wav files for convenience.



## To-Do
- [ ] Add TTS language selection (currently defaults to English)
- [ ] Write tests
- [ ] Improve name import method (at least provide more customization)
- [ ] Improve file handling


## License (MIT)

Copyright (c) 2016 Raúl Negrón

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
