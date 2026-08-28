# Command-Line Interface

The **`pymorsed` CLI** provides a convenient way to use Morse-code
functionality directly from the terminal.

!!! tip "Quick Start" 
      Install the package and check the available commands:

    ``` bash
    pip install pymorsed
    pymorsed --help
    ```

------------------------------------------------------------------------

## Installation

Install the latest release from PyPI:

``` bash
pip install pymorsed
```

After installation, verify that the CLI is available:

``` bash
pymorsed --help
```

!!! note 
      The `pymorsed` command is installed automatically with the package.

------------------------------------------------------------------------

## Basic Usage

The general syntax is:

``` text
pymorsed <command> [arguments]
```

For example:

``` bash
pymorsed encode-audio "HELLO WORLD"
```

To see the options available for any command:

``` bash
pymorsed <command> --help
```

------------------------------------------------------------------------

# Audio Commands

The audio commands allow you to convert between text and Morse-code
audio.

## `encode-audio`

Convert text into a Morse-code audio signal.

### Syntax

``` bash
pymorsed encode-audio <text>
```

### Argument

  Argument    Required  Description
  ---------- ---------- ----------------------------------------
  `text`        Yes     Text to convert into Morse-code audio.

### Example

``` bash
pymorsed encode-audio "HELLO"
pymorsed encode-audio HELLO
```

!!! tip "Using multiple words" 
      Put text containing spaces inside quotation marks.

    ```bash
    pymorsed encode-audio "SOS HELP"
    ```

### Command Help

``` bash
pymorsed encode-audio --help
```

------------------------------------------------------------------------

## `decode-audio`

Convert Morse-code audio into text.

### Syntax

``` bash
pymorsed decode-audio <audio_file>
```

### Argument

  Argument        Required  Description
  -------------- ---------- -----------------------------------------------
  `audio_file`      Yes     Path to the audio file containing Morse code.

### Example

``` bash
pymorsed decode-audio morse.wav
```

The command reads the Morse-code signal from the audio file and outputs
the decoded text.

### Command Help

``` bash
pymorsed decode-audio --help
```

------------------------------------------------------------------------

# Help and Discoverability

The CLI provides help at both the global and command levels.

## Global Help

Use:

``` bash
pymorsed --help
```

This displays the available commands and global options.

## Command-Specific Help

Use:

``` bash
pymorsed encode-audio --help
```

or:

``` bash
pymorsed decode-audio --help
```

This displays the syntax, arguments, and description for the selected
command.

!!! tip "Not sure what to use?" 
      Start with `pymorsed --help` and then open the help page for the command you want to use.

------------------------------------------------------------------------

## Command Reference

| Command | Description |
|:---|:---|
| `pymorsed --help` | Display general CLI help. |
| `pymorsed encode-audio <text>` | Convert text to Morse-code audio. |
| `pymorsed decode-audio <audio_file>` | Decode Morse-code audio into text. |
| `pymorsed <command> --help` | Display help for a specific command. |


# Examples

### Encode text

``` bash
pymorsed encode-audio "SOS"
```

### Encode a sentence

``` bash
pymorsed encode-audio "HELLO WORLD"
```

### Decode an audio file

``` bash
pymorsed decode-audio morse.wav
```

### Explore available commands

``` bash
pymorsed --help
```

------------------------------------------------------------------------

# CLI Architecture

The CLI is implemented using Python's
[`argparse`](https://docs.python.org/3/library/argparse.html) module.

The command structure follows a **subcommand-based design**:

``` text
pymorsed
│
├── encode
├── decode
├── encode-audio
└── decode-audio
```

Each subcommand has its own parser and arguments. This provides:

-   Clear command organization
-   Command-specific help
-   Argument validation
-   Easy extension for future commands

!!! info "Design principle" 
      The CLI separates the command interface from
      the underlying Morse-code functionality. This allows the same library
      functionality to be used both programmatically from Python and
      interactively from the terminal.

<!-- ------------------------------------------------------------------------ -->

<!-- # Typical Workflow

A typical user workflow looks like this:

``` text
Install pymorsed
      │
      ▼
pymorsed --help
      │
      ▼
Choose a command
      │
      ├───────────────┐
      ▼               ▼
encode-audio      decode-audio
      │               │
      ▼               ▼
   Text            Audio file
      │               │
      ▼               ▼
Morse audio       Decoded text
```

This makes the CLI a simple entry point for users who want to use
`pymorsed` without writing Python code. -->
