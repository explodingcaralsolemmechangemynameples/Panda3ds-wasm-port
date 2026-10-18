# Contributing

## Scope of this repo

This repository is a **web packaging + performance shell** around the official Panda3DS wasm build.

- Bugs in **game compatibility, core emulation, shaders, audio** → report upstream:  
  https://github.com/wheremyfoodat/Panda3DS/issues
- Bugs in **index.html, serve.py, resolution limiter, hosting docs** → open an issue here.

## Pull requests

1. Keep the host page dependency-free (no npm runtime deps required to play).
2. Do not strip or weaken the Credits section in `README.md`.
3. If you replace `Alber.js` / `Alber.wasm`, note the upstream commit / build flags in the PR description.
4. Test at least 1× and 2× scale in Chromium and Firefox.

## License

All contributions must be compatible with **GPL-3.0** (same as upstream Panda3DS).
