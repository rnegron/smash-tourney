#!/usr/bin/env python3

# external dependencies: pydub

from urllib.request import Request, build_opener
from urllib.error import HTTPError
from pydub import AudioSegment
from random import shuffle
from os import remove, path, makedirs
from sys import argv
from glob import glob

def link_sound(file1, file2):

    # initialize the .wav files
    name1 = AudioSegment.from_file('./{}.wav'.format(file1))
    versus = AudioSegment.from_file('./versus.wav')
    name2 = AudioSegment.from_file('./{}.wav'.format(file2))

    # Lower the 'versus' volume by 5 dB
    versus -= 5

    # pydub is so abstract
    combined = name1 + versus + name2

    # create the combined file
    combined.export('./tourney/{}_vs_{}.wav'.format(file1, file2), format='wav')

    # the original player .wav files are deleted if there is an error creating them

def create_sound(name, lang):

    # variable to return, signals if an error ocurred when creating the wav file
    error = False

    # template url for Google TTS
    tts = 'http://translate.google.com/translate_tts?tl={}&q={}'
    opener = build_opener()

    # request the sound file for the player name
    request = Request( tts.format(lang, name.replace(' ', '%20')) )

    # this line tricks Google Translate into accepting the query
    request.add_header('User-agent', 'Mozilla/6.0')

    # prepare the file for writing sound into
    sound = open('{}.wav'.format(name), 'wb')

    # basic error-checking for common errors related to Google TTS's
    try:
        sound.write(opener.open(request).read())

    except HTTPError as err:
        # if an error ocured, notify and prepare error variable
        print('--- Could not create sound! \'{}\' ---\n'.format(err))
        error = True

    finally:
        # no matter what, close the file and remove the original .wav
        sound.close()
        remove('./{}.wav'.format(name))

        # also return the error to the calling function
        return error

def main():

    # create a folder 'tourney' if it does not exist already
    # the resulting sound files will exist here
    if not path.exists('./tourney'):
        makedirs('./tourney')

    else:
        # Empty the tourney dir
        rem = glob('./tourney/*.wav')
        for file in rem:
            remove(file)

    with open('names.txt', 'r') as file:

        # populate the list with formatted names
        names = [name.replace('\n', '') for name in file if name != '\n']

        # Google TTS supports many languages
        languages = {'english':'en', 'spanish': 'es', 'french': 'fr',
                    'italian': 'it', 'portuguese': 'pt'}

        # default to english if no language specified via command-line
        lang = 'english' if len(argv) == 1 else argv[1]

        if not lang in languages:
            print('No such language!\n')
            print('Example usage: {} english\n'.format(argv[0]))
            return

        # shuffle the list. this is how we randomize the selection
        shuffle(names)

        # keep track of all matchups in a dict as key:value pairs
        vs_dict = {}

        # if there are an odd number of players, there is an extra player
        extra = None

        # if an error ocurred while creating sound files, change output slightly
        sound_error1 = False
        sound_error2 = False

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

            # format their names for file creation
            name1 = name1.replace(' ', '')
            name2 = name2.replace(' ', '')

            # create the .wav files for each name in the language specified
            # and receive the error signal in case the creation succeded or failed
            sound_error1 = create_sound(name1, languages[lang])
            sound_error2 = create_sound(name2, languages[lang])

            # if any of the two files could not be created, do not try to link them
            if not sound_error1 and not sound_error2:
                
                # link the two names and the 'versus' sound
                link_sound(name1, name2)

        print('Roster complete!!\n\n')
        for player1, player2 in vs_dict.items():
            print('{} vs. {}!!'.format(player1, player2))

        if extra:
            print('And {} as the extra player!'.format(extra))

        print('\n')
        return

if (__name__) == '__main__':
    main()
