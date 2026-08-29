# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-08-30

### Added

- CLI support using `argparse`.
- `encode` command for converting text to Morse code.
- `decode` command for converting Morse code to text.
- `encode-audio` command for generating Morse-code audio.
- `decode-audio` command for decoding Morse-code audio files.
- `version` command
- Optional `-o` / `--output` option for saving generated audio.
- MkDocs documentation for the CLI.

### Fixed

- Added validation for unsupported audio output formats in decode_from_file().

---

## [0.1.0]

### Added

- Initial release of `pymorsed`.
- Text-to-Morse conversion.
- Morse-to-text conversion.
- Multi-language Morse-code support.
- Morse audio signal generation.
- Morse audio decoding from files.
- Waveform visualization.