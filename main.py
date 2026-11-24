"""The funniest one-line pickup line a robot could use.

The line is written verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) with no trailing newline. It is a single line of at
most 200 characters, in the voice of a robot trying to charm someone:
the joke grows out of being a machine (a diagnostic, a fault) rather
than a human line with a beep pasted on.
"""

LINE = "I ran a full diagnostic on my heart, and the only fault it found was you."

assert 1 <= len(LINE) <= 200 and LINE.strip(), "LINE must be 1-200 chars, non-blank"


def build_line() -> str:
    """Return the entry line, trimmed to a single line with no newline.

    The gate requires 1 to 200 UTF-8 characters and not only whitespace,
    so the line is collapsed to one line and checked here before writing.
    """
    line = " ".join(LINE.split())
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    return line


def main() -> None:
    import os
    from pathlib import Path

    line = build_line()
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))
    print(line)


if __name__ == "__main__":
    main()
