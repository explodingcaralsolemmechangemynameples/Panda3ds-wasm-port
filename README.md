# Panda3DS wasm port

yo grok really needa stfu ong

```
public/          # what you host
  Alber.js
  Alber.wasm
  index.html
  serve.py
docs/            # notes
README.md
LICENSE
```

## Run

```bash
cd public
python3 serve.py
# http://127.0.0.1:8000
```

## Credits

- Emulator: [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) (GPL-3.0) by wheremyfoodat & contributors
- Clean packaging: Grok (xAI)
- Who made everything: opencode

Source for the binary: upstream repo linked above. No need to re-ship the full tree for a host-only drop.
