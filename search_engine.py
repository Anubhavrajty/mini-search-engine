#!/usr/bin/env python
import os
import sys
import urllib.parse

if len(sys.argv) < 3:
    print("Usage: search [g|d|y|w|gh|so|img] query")
    sys.exit()

command = sys.argv[1]
query = urllib.parse.quote(" ".join(sys.argv[2:]))

# Define URLs for each command
if command == "g":
    url = f"https://www.google.com/search?q={query}"
elif command == "d":
    url = f"https://duckduckgo.com/?q={query}"
elif command == "y":
    url = f"https://www.youtube.com/results?search_query={query}"
elif command == "w":
    url = f"https://en.wikipedia.org/wiki/{query}"
elif command == "gh":
    url = f"https://github.com/search?q={query}"
elif command == "so":
    url = f"https://stackoverflow.com/search?q={query}"
elif command == "img":
    url = f"https://www.google.com/search?tbm=isch&q={query}"
else:
    print("Unknown command. Use g, d, y, w, gh, so, or img")
    sys.exit()

# Open URL in Android browser (Termux) or Linux default browser
os.system(f'am start -a android.intent.action.VIEW -d "{url}"')