# Obbjective: To make the pymorsed Library accessible from the CLI

# pymorsed --help

# Support Piping

# 1. Create cli.py
#        ↓
# 2. Create main()
#        ↓
# 3. Create argparse parser
#        ↓
# 4. Add encode subcommand
#        ↓
# 5. Connect encode → existing encode()
#        ↓
# 6. Add decode subcommand
#        ↓
# 7. Connect decode → existing decode()
#        ↓
# 8. Test with python -m pymorsed.cli
#        ↓
# 9. Add console-script entry point
#        ↓
# 10. Rebuild package
#        ↓
# 11. Install fresh package
#        ↓
# 12. Test `pymorsed --help`
#        ↓
# 13. Test `pymorsed encode`
#        ↓
# 14. Test `pymorsed decode`
#        ↓
# 15. Add piping
#        ↓
# 16. Add audio commands

import argparse

from .encoder import encode
from .decoder import decode

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

    elif args.command == "version":
        print(f"pymorsed {PACKAGE_VERSION}")


if __name__ == "__main__":
    main()