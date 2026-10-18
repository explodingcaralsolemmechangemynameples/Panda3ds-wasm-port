# Notes

- `Alber.wasm` is the Emscripten output of the Panda3DS SDL frontend.
- `index.html` expects `Alber.js` next to it (same directory).
- Do not open via `file://` — use `serve.py` or any static host that serves `.wasm` as `application/wasm`.
