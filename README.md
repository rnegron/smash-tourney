smash-versus-tourney
===================

The Open Source Super Smash Bros. 1v1 randomizer and announcer voice implementer (written in Python 3)!
## About

A simple python script that, given a list of player names, outputs a random pairing of them (representing two players who will fight) and creates .wav files for each pairing. The .wav file contains a text-to-speech reading of the first player's name, followed by the classic "VERSUS" line, and ends with the second player's name.

smash-versus-tourney expects a `versus.wav` file in the same folder as `smash_tourney.py`. Previously, I
had included the file in this repository, but I'm not quite sure I'm allowed to do that. Instead, I'll link to
[The Sounds Resource](http://www.sounds-resource.com/3ds/supersmashbrosfornintendo3ds/sound/3535/), where you can find the announcer voice samples (in this case, Xander Mobus from Smash 4). Make sure the sound file is called `versus.wav`!

## How to use

_**Intended for use with a Python 3 interpreter**_.

smashtourney.py uses [pydub](https://github.com/jiaaro/pydub/) to handle audio files. `pydub` can be easily installed using `pip`:

`$ pip install pydub`

Next, you'll need to create a `names.txt` file in the same directory as `smash_tourney.py`. In the text file, insert line-separated names for the players who will be participating in the tourney.


You're ready to run the script!

`$ python3 smash_tourney.py`

**IMPORTANT**

smash_tourney.py will create a folder called `tourney`, where it will store the created .wav files for convenience.

## Common issues and bugs

[_HTTP Error 403_](https://en.wikipedia.org/wiki/HTTP_403)

Since this script uses Google Translate to perform the text-to-speech, an error
occurs frequently which apparently has to do with the servers rejecting a request
due to a high volume of tries or 'suspucious activity'. Basically, the server thinks the script is a malicious bot and rejects the input. I've read that not performing and queries for at least 24 hours should fix it, but I'm not completely sure that's the underlying issue.



## To-Do
- [x] More intuitive TTS language selection
- [x] Better error-checking and handling
- [ ] General clean-up

Of course, I could always improve both the language selection and the error handling, but at least
they are much better now.



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
