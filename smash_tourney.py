#!/usr/bin/env python3

# external dependencies: pydub, gTTS

from pydub import AudioSegment
from gtts import gTTS
from random import shuffle
from os import remove, path, makedirs
from sys import argv
from glob import glob

def link_sound(file1, file2):

    # initialize the .wav files
    name1 = AudioSegment.from_file('./{}.wav'.format(file1.replace(' ', '')))
    versus = AudioSegment.from_file('./versus.wav')
    name2 = AudioSegment.from_file('./{}.wav'.format(file2.replace(' ', '')))

    # Lower the 'versus' volume by 5 dB
    versus -= 5

    # pydub is so abstract
    combined = name1 + versus + name2
    combined.export('./tourney/{}_vs_{}.wav'.format(file1, file2), format='wav')

def create_sound(name):

    # gTTS greatly simplifies accessing Google's text-to-speech API
    tts = gTTS(text=name)
    tts.save('{}.wav'.format(name.replace(' ', '')))


def main():

    # create a folder 'tourney' if it does not exist already
    # the resulting sound files will exist here
    if not path.exists('./tourney'):
        makedirs('./tourney')

    else:
        # Empty the tourney dir
        rem = glob('./tourney/*.wav')
        for wav_file in rem:
            remove(wav_file)

    with open('names.txt', 'r') as text_file:

        # populate the list with formatted names
        names = [name.strip() for name in text_file if name != '\n']

        # shuffle the list. this is how we randomize the selection
        shuffle(names)

        # keep track of all matchups in a dict as key:value pairs
        vs_dict = {}

        # if there are an odd number of players, there is an extra player
        extra = None

        print('Making tourney...')

        if len(names) % 2 == 1:
            extra = names.pop()
            print('Extra player found!')

        while len(names) > 0:

            # pop two players off the list
            name1 = names.pop()
            name2 = names.pop()

            # add them to the dict
            vs_dict[name1] = name2

            # create the .wav files for each name
            create_sound(name1)
            create_sound(name2)

            # link the two names and the 'versus' sound
            link_sound(name1, name2)

        print('Roster complete!!\n\n')
        for player1, player2 in vs_dict.items():
            print('{} vs. {}!!'.format(player1, player2))

        if extra:
            print('And {} as the extra player!'.format(extra))

        print('')

        # remove the individual wav files, if they exist
        rem = glob('./*.wav')
        for wav_file in rem:
            remove(wav_file)

        return

if (__name__) == '__main__':
    main()
