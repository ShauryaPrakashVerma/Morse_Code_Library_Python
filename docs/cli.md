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

Convert text into a Morse-code audio signal and play the generated audio. The audio can optionally be saved to a file using the `-o` or `--output` option.

### Syntax

```bash
pymorsed encode-audio <text> [-o <output_file>]
```

### Arguments and Options

| Argument / Option | Required | Description |
|:---|:---:|:---|
| `text` | Yes | Text to convert into Morse-code audio. |
| `-o`, `--output` | No | Save the generated audio to the specified file. |

### Examples

**Encode a single word:**

```bash
pymorsed encode-audio "HELLO"
```

This converts `HELLO` to Morse code and plays the generated audio.

**Encode text without quotation marks:**

```bash
pymorsed encode-audio HELLO
```

!!! tip "Using multiple words"

    Put text containing spaces inside quotation marks.

    ```bash
    pymorsed encode-audio "SOS HELP"
    ```

### Saving the Generated Audio

Use `-o` or `--output` to save the generated audio to a file.

```bash
pymorsed encode-audio "HELLO" -o hello.wav
```

The long form can also be used:

```bash
pymorsed encode-audio "HELLO" --output hello.wav
```

If no output option is provided, the generated audio is only played and is not saved.

### Supported Output Formats

The output format is determined by the file extension. Supported formats include:

- `.wav`
- `.flac`
- `.ogg`
- `.mp3`

You **do not need to provide the file extension explicitly**. If no extension is provided, `.wav` is used by default.

For example:

```bash
pymorsed encode-audio "SOS" -o sos
```

saves the audio as:

```text
output/sos.wav
```



You can also explicitly specify a supported extension:

```bash
pymorsed encode-audio "SOS" -o sos.wav
```

```bash
pymorsed encode-audio "SOS" -o sos.flac
```

!!! warning "Unsupported formats"

    An unsupported file extension will result in an error. Use one of the supported audio formats when specifying `--output`.

### Command Help

To view the available arguments and options:

```bash
pymorsed encode-audio --help
```


------------------------------------------------------------------------

## `decode-audio`

Convert Morse-code audio into text.

### Syntax

``` bash
pymorsed decode-audio <audio_file_path>
```

### Argument

| Argument | Required | Description |
| -------- | -------- | ----------- |
| `audio_file_path` | Yes | Path to the audio file containing Morse code. |

### Example

``` bash
pymorsed decode-audio "E://audios/morse.wav"
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
| `pymorsed decode-audio <audio_file_path>` | Decode Morse-code audio into text. |
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
pymorsed decode-audio "E://audios/morse.wav"
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
│
├── decode
│
├── encode-audio
│   ├── text
│   └── -o, --output
│
└── decode-audio
    └── audio_file
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
