# Panda3DS WebAssembly — clean package

Stripped build-wasm folder: runtime only, no CMake/ninja/object junk.

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

Drop a decrypted `.3ds` / `.cci` / `.cxi` / `.app`, click Start. Press **F** to copy the FPS log.

## What was removed

From the raw `build-wasm` tree (~664 files / build intermediates):

- `CMakeFiles/`, `*.o`, `*.a`, `build.ninja`, `.ninja_*`, `CMakeCache.txt`
- `third_party/` static libs and cmake crumbs
- `autotest/`, screenshot dumps, `profile.cpuprofile`, fuzz binaries
- `Alber.js.bak`, accel probe HTML/GLSL test pages
- `__cmrc*` generated intermediates

Left: the wasm binary, JS loader, host page, and a tiny static server.

## Credits

- Emulator: [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) (GPL-3.0) by wheremyfoodat & contributors
- Clean packaging: Grok (xAI) and opencode

Source for the binary: upstream repo linked above. No need to re-ship the full tree for a host-only drop.
