#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

try:
    import barcodenumber
except ImportError:  # pragma: no cover - optional dependency
    barcodenumber = None


def is_valid_ean13(value: str) -> bool:
    """Validate an EAN-13 code and ensure it contains only digits."""
    if not value or len(value) != 13 or not value.isdigit():
        return False

    if barcodenumber is not None:
        return bool(barcodenumber.check_code("ean13", value))

    digits = [int(ch) for ch in value]
    weighted_total = sum(digits[i] for i in range(0, 12, 2)) + (
        3 * sum(digits[i] for i in range(1, 12, 2))
    )
    expected_check_digit = (10 - (weighted_total % 10)) % 10
    return digits[-1] == expected_check_digit


def generate_ean_numbers(start_code: str, count: int, output_path: Path) -> int:
    """Generate valid EAN-13 numbers and append them to a text file."""
    if count <= 0:
        raise ValueError("Count must be greater than zero.")
    if not is_valid_ean13(start_code):
        raise ValueError(f"Invalid EAN-13 start code: {start_code!r}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    current = int(start_code)
    produced = 0

    with output_path.open("a", encoding="utf-8", newline="\n") as handle:
        while produced < count:
            candidate = str(current)
            if not is_valid_ean13(candidate):
                current += 1
                continue

            handle.write(f"{candidate}\n")
            produced += 1
            current += 1

    return produced


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate valid EAN-13 note numbers.")
    parser.add_argument("--start", default="8053831640150", help="Starting EAN-13 number")
    parser.add_argument("--count", type=int, default=300, help="How many EAN numbers to generate")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("ean13_numbers.txt"),
        help="Output text file to write EAN numbers into",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generate_ean_numbers(args.start, args.count, args.output)
    print(f"Generated {args.count} codes in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
