# external dependencies for main usage : pydub, gTTS

import logging
import sys
from collections import defaultdict
from pathlib import Path
from random import shuffle
from tempfile import TemporaryDirectory
from time import time
from typing import Dict, List

from gtts import gTTS
from pydub import AudioSegment

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_sound_google(temp_dir: Path, text: str) -> None:
    # gTTS greatly simplifies accessing Google's text-to-speech API
    tts = gTTS(text=text)
    temp_file = str(temp_dir / f"{text.replace(' ', '')}.wav")
    tts.save(temp_file)


def link_sound(tourney_dir: Path, temp_dir: Path, name_1: str, name_2: str) -> None:

    # First, attempt to load the versus sound.
    # This is to make sure it still exists between
    # each match creation, as the script could take awhile to complete.

    try:
        versus = AudioSegment.from_file("./versus.wav")
    except FileNotFoundError:
        logger.error('No "versus.wav" file found in the directory!')
        sys.exit(1)

    # initialize the .wav files
    file_1 = AudioSegment.from_file(str(temp_dir / f"{name_1}.wav"))
    file_2 = AudioSegment.from_file(str(temp_dir / f"{name_2}.wav"))

    # Lower the 'versus' volume by 5 dB
    versus -= 5

    # pydub is so abstract
    combined = file_1 + versus + file_2

    # Export the finalized file into the tourney directory
    result = combined.export(
        str(tourney_dir / f"{name_1}_vs_{name_2}.wav"), format="wav"
    )
    result.close()


def main() -> None:
    if len(sys.argv) == 2:
        file_with_names = Path(sys.argv[1])
        if not Path(file_with_names).exists():
            raise FileNotFoundError

    else:
        print(f"Usage: smash-tourney file_with_names")
        sys.exit(1)

    start_time = time()

    # First, we make sure there is a versus sound file to work with
    versus_file = Path("./versus.wav")
    if not versus_file.exists():
        logger.warning(
            'No "versus.wav" file found in the directory! Will use a GTTS one...'
        )

        # Generate a versus.wav file
        create_sound_google(Path("."), "versus")
        if not versus_file.exists():
            logger.error("Could not generate a versus.wav file automatically...")
            sys.exit(1)

    tourney_dir = Path.cwd().joinpath("tourney")

    # Check to see if there is an existing directory
    if not tourney_dir.is_dir():

        # There is no directory, but there may be a file of some sort
        if tourney_dir.exists():

            # So we remove it if it exists, to be safe
            tourney_dir.unlink()

        # Create the tourney directory
        tourney_dir.mkdir()

    # The tourney directory already exists
    else:
        # Clean up possibly existing .wav files
        files_to_remove = tourney_dir.glob("*.wav")
        for file in files_to_remove:
            file.unlink()

    # Create a temporary directory to hold intermediate sound files
    with TemporaryDirectory() as tmp:
        temp_dir = Path(tmp)

        # Iterate through each of the names in the provided file
        with file_with_names.open() as name_file:

            # Populate the list with formatted names
            names: List[str] = [name.strip() for name in name_file.readlines()]

            # Shuffle the list. This is how we randomize the selection
            shuffle(names)

            # Keep track of all matchups in a dict as key:value pairs
            vs_dict: Dict[str, str] = defaultdict(str)

            # If there are an odd number of players, there is an extra player
            extra = None

            logger.info("Making tourney...")

            # Odd amount of names means there is an extra player
            if len(names) % 2 == 1:
                extra: str = names.pop()
                logger.info("Extra player found!")

            # Count iterations left to report them to the main
            iterations_left = len(names) // 2

            # Iterate through the names list, removing two at a time
            while len(names) > 0:

                logger.info(f"Iterations left: {iterations_left}...")

                # pop two players off the list
                name_1: str = names.pop()
                name_2: str = names.pop()

                # add them to the dict
                vs_dict[name_1] = name_2

                # create the .wav files for each name
                create_sound_google(temp_dir, name_1)
                create_sound_google(temp_dir, name_2)

                # We needed to keep the spaces, if they existed,
                # to help the TTS engine. But now, we really only
                # care about the file names
                name_1 = name_1.replace(" ", "")
                name_2 = name_2.replace(" ", "")

                # link the two names and the 'versus' sound
                link_sound(tourney_dir, temp_dir, name_1, name_2)
                iterations_left -= 1

            logger.info("Roster complete!! Here are the matchups:\n")
            for i, (player_1, player_2) in enumerate(vs_dict.items(), start=1):
                logger.info(f"\t#{i}: {player_1} vs. {player_2}!!")

            if extra:
                logger.info(f"\tAnd {extra} as the extra player!\n")

        end_time = time()

        print(f"\nTourney generated in {round(end_time - start_time, 2)} seconds")
    return


if __name__ == "__main__":
    main()
