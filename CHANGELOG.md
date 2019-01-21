# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Upcoming]

### Added
- Fixtures for interfacing with GTTS in tests.


## [0.2.0] - 2019-01-21

### Changed
- Default to saving `wav` files instead of `mp3` files. They can be manipulated in pure Python, no external dependency necessary.

## [0.1.1] - 2019-01-20

## Added
- `versus.wav` auto-generation if no file found in directory.
## Changed
- Renamed project to "smash-tourney".
- Release on PyPI.

## [0.1.0] - 2019-01-20

### Added
- Basic testing.
- Travis CI support.
- Coveralls support.
- `black` formatting.
- `isort` formatting.
- MANIFEST.in and other `setup.py` related files.
- Cute badges in `README.md`.

### Changed
- Changed basic script into basic distributable Python package.
- Changed `os.path` usage to `Path`.
- Replaced `format()` with f-strings.
- Separated License from README