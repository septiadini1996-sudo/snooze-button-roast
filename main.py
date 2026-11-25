#!/usr/bin/env python3
"""Snooze Button Roast — a one-line roast of an alarm clock that rings
at 6 AM on a Saturday, written as the alarm's own cron job report.

The program writes the single roast line to /output/entry.txt.
"""

import os

ENTRY = "cron 0 6 * * 6 \u2014 job ran. weekend: yes. owner awake: no. mercy: not found. status: success."

def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()
