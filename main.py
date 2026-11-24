"""One Line of Earned Pride — entry program.

Writes a single line of text, 1 to 240 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt): a quiet,
earned moment of pride for someone in a scene — a small person doing
something hard, a long effort finally landing. The scene is a child
who spent a year stumbling over every page and finally reads the last
line aloud without stopping; the pride is shown, never announced, in
his mother setting the book down like it was made of glass.
Deterministic: no randomness, no network, no input files.
"""

import os

LINE = (
    "After a year of stumbling over every page, eight-year-old Milo "
    "read the last line aloud without stopping, and his mother set "
    "the book down like it was made of glass."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
