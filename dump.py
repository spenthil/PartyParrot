#!/usr/bin/python3

import json
import urllib.request
import urllib.parse

urls = {
    'parrots': 'https://api.github.com/repos/spenthil/PartyParrot/contents/media/parrots',
    'parrots_hd': 'https://api.github.com/repos/spenthil/partyparrot/contents/media/parrots/hd',
    'guests': 'https://api.github.com/repos/spenthil/partyparrot/contents/media/guests/' ,
    'guests_hd': 'https://api.github.com/repos/spenthil/partyparrot/contents/media/guests/hd',
}

files = {}

for category, url in urls.items():
    files[category] = []
    f = urllib.request.urlopen(url)
    for file in json.loads(f.read().decode('utf-8')):
        if file['type'] != 'file':
            continue
        files[category].append((file['download_url']))

print(json.dumps(files))

