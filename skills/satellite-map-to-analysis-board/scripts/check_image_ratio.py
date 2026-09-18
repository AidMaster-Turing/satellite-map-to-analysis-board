#!/usr/bin/env python3
"""Read display dimensions and compare exact aspect ratios. Never edit files."""
import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

def image_info(path):
    from PIL import Image
    with Image.open(path) as image:
        width, height = image.size
        orientation = image.getexif().get(274, 1)
        if orientation in (5, 6, 7, 8):
            width, height = height, width
    ratio = Fraction(width, height)
    return {"file": str(Path(path)), "width": width, "height": height,
            "ratio": f"{ratio.numerator}:{ratio.denominator}",
            "decimal_ratio": width / height, "exif_orientation": orientation}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("output", nargs="?")
    args = parser.parse_args()
    try:
        source = image_info(args.source)
        result = {"source": source}
        code = 0
        if args.output:
            output = image_info(args.output)
            a = source["width"] * output["height"]
            b = output["width"] * source["height"]
            exact = a == b
            result.update(output=output, exact_ratio_match=exact,
                          relative_ratio_error_percent=100 * abs(b - a) / a)
            code = 0 if exact else 1
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
