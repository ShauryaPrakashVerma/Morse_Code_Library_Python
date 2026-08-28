# Obbjective: To make the pymorsed Library accessible from the CLI

# pymorsed --help

# Support Piping

#        ↓
# 16. Add audio commands

import argparse

from .encoder import encode
from .decoder import decode
from .audio_decoder import decode_from_file
from .audio_encoder import play_audio, morse_to_audio, save_audio

from importlib.metadata import version

PACKAGE_VERSION = version("pymorsed")

def main():
    parser = argparse.ArgumentParser(
        prog="pymorsed",
        description="Encode and decode Morse code."
    )
    
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {PACKAGE_VERSION}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # -------------------------------------------------------------------------------------------------------------------
    # encode command

    encode_parser = subparsers.add_parser(
        "encode",
        help="Convert text to Morse code."
    )

    encode_parser.add_argument(
        "text",
        help="Text to encode."
    )

    # -------------------------------------------------------------------------------------------------------------------
    # decode command

    decode_parser = subparsers.add_parser(
        "decode",
        help="Convert Morse code to text."
    )

    decode_parser.add_argument(
        "text",
        help="Morse code to decode."
    )
    
    # -------------------------------------------------------------------------------------------------------------------
    # audio decode command

    audio_decode_parser = subparsers.add_parser(
        "decode-audio",
        help="Convert Morse code audio to text."
    )
    
    audio_decode_parser.add_argument(
        "audio_file",
        help="Audio file containing Morse code to decode."
    )
    
    # -------------------------------------------------------------------------------------------------------------------
    # audio encode command

    audio_encode_parser = subparsers.add_parser(
        "encode-audio",
        help="Convert text to Morse audio."
    )

    audio_encode_parser.add_argument(
        "text",
        help="Text to encode into Morse code audio."
    )
    
    audio_encode_parser.add_argument(
        "-o",
        "--output",
        help="Save the generated audio to the specified file."
    )

    # -------------------------------------------------------------------------------------------------------------------
    # version command

    subparsers.add_parser(
        "version",
        help="Show the pymorsed version."
    )

    # Parse arguments
    args = parser.parse_args()

    # -------------------------------------------------------------------------------------------------------------------
    # Execute command

    if args.command == "encode":
        result = encode(args.text)
        print(result)

    elif args.command == "decode":
        result = decode(args.text)
        print(result)
        
    elif args.command == "decode-audio":
            result = decode_from_file(args.text)
            print(result)
    
    elif args.command == "encode-audio":
            audio = morse_to_audio(encode(args.text))
            play_audio(audio)
        
            if args.output:
                save_audio(audio, args.output, 44100)
    
    elif args.command == "version":
        print(f"pymorsed {PACKAGE_VERSION}")


if __name__ == "__main__":
    main()
    
    


# Update version number


# Upload to test.pypi
# Check
# Upload to pypi

# Update README

# Create Release

# Check next feature to be released.

# Changelog