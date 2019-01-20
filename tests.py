import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from smash_tourney import create_sound_google, link_sound, main


class TestSmashTourney(unittest.TestCase):
    def test_can_create_gtts_file(self):
        with TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            name_1 = "Test"

            create_sound_google(temp_dir, name_1)

            result_file = temp_dir / f"{name_1}.mp3"

            self.assertTrue(result_file.exists())

    def test_two_person_tourney_created(self):
        with TemporaryDirectory() as tmp:
            with TemporaryDirectory() as tmp_2:
                tourney_dir = Path(tmp)
                temp_dir = Path(tmp_2)
                name_1 = "Test"
                name_2 = "Prueba"

                create_sound_google(temp_dir, name_1)
                create_sound_google(temp_dir, name_2)

                # Create the wav file as well
                create_sound_google(Path.cwd(), "versus", fmt="wav")

                link_sound(tourney_dir, temp_dir, name_1, name_2)
                result_file = tourney_dir / f"{name_1}_vs_{name_2}.mp3"
                self.assertTrue(result_file.exists())


if __name__ == "__main__":
    unittest.main()
