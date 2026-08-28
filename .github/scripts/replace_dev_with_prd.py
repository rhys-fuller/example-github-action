"""Replace every occurrence of the substring "DEV" with "PRD" in a given list of files.

Usage: python replace_dev_with_prd.py <path_to_file_listing_changed_files>

The listing file should contain one file path per line (relative to the repo root).
Missing files, directories, and binary/unreadable files are skipped safely.
"""

import sys
from pathlib import Path

SEARCH = "DEV"
REPLACE = "PRD"


def process_file(path: Path) -> bool:
    if not path.is_file():
        return False

    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        print(f"Skipping (not a readable text file): {path}")
        return False

    if SEARCH not in text:
        return False

    path.write_text(text.replace(SEARCH, REPLACE), encoding="utf-8")
    print(f"Updated: {path}")
    return True


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python replace_dev_with_prd.py <changed_files_list>")
        sys.exit(1)

    listing_path = Path(sys.argv[1])
    if not listing_path.is_file():
        print(f"No changed files listing found at {listing_path}")
        return

    lines = [line.strip() for line in listing_path.read_text(encoding="utf-8").splitlines()]
    changed_files = [line for line in lines if line]

    if not changed_files:
        print("No changed files to process.")
        return

    any_updated = False
    for file_str in changed_files:
        if process_file(Path(file_str)):
            any_updated = True

    if not any_updated:
        print("No occurrences of DEV found in changed files.")


if __name__ == "__main__":
    main()
