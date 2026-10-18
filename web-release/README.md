# Panda3DS WebAssembly (Optimized)

Browser port of **[Panda3DS](https://github.com/wheremyfoodat/Panda3DS)** — an HLE Nintendo 3DS emulator — compiled to WebAssembly via Emscripten and tuned for playable performance in Chromium / Firefox / Edge.

Drop a decrypted ROM, hit Start, play. No native install.

---

## What this is

| Piece | Source |
|-------|--------|
| Emulator core + SDL frontend | [wheremyfoodat/Panda3DS](https://github.com/wheremyfoodat/Panda3DS) (upstream C++ → wasm build) |
| Web shell, resolution limiter, host page, packaging | This repo |

Upstream already ships an experimental `build-wasm/` target (`Alber.js` / `Alber.wasm`). This release keeps that binary and replaces the stock `index.html` with a performance-focused shell.

---

## Why it was slow (and what we fixed)

A typical session log looked like:

```
env: canvas 2400x1196 css 2400x1196 dpr 0.8 ...
FPS 14–22  |  ~45–68 ms/frame  (CPU 30+ / IDLE 50+)
```

Native 3DS dual-screen layout is **400×480**. The original web page let the WebGL backbuffer track the full CSS viewport, so every frame paid for ~2.9M pixels instead of ~0.19M.

**Optimizations in this shell:**

- Internal render scale locked to **1× / 2× / 3× / 4×** of 400×480 (default **2× = 800×960**)
- CSS display scales independently (`object-fit` + `image-rendering: pixelated`) — looks large, costs little
- Scale locked after Start (no mid-run resize storms)
- Optional pause of the Emscripten main loop when the tab is hidden
- Longer IDBFS sync interval (less main-thread stall on save flush)
- Correct `application/wasm` MIME + no-cache headers from `serve.py`

You should see `canvas 800x960` (or 400×480) in the FPS log env line instead of 2400×1196, and steady-state FPS rise accordingly.

---

## Requirements

- Modern browser with **WebAssembly + WebGL2** (Chrome / Edge / Firefox recent; Safari varies)
- A **decrypted** 3DS ROM: `.3ds`, `.cci`, `.cxi`, `.app`, or `.zcci`
- Local HTTP server (browsers block `file://` for wasm modules) — use the included `serve.py` or any static host

---

## Quick start

```bash
# clone or download this release
cd panda3ds-web-release   # or whatever you named the folder

python3 serve.py
# → Serving at http://0.0.0.0:8000
```

Open **http://127.0.0.1:8000**, drop a ROM, choose scale (start at **1×** or **2×**), click **Start**.

| Key | Action |
|-----|--------|
| **F** | Copy the rolling FPS / timing log to the clipboard |
| **F4** | Pause / resume (emulator hotkey) |
| **F5** | Reset (emulator hotkey) |

Audio unlocks on the Start click (browser autoplay policy).

---

## Files

```
Alber.js          Emscripten loader + runtime (modularized as Panda3DS)
Alber.wasm        Emulator binary (~5.3 MB)
index.html        Optimized host page (resolution cap, UI, persistence)
serve.py          Tiny Python static server (correct MIME, no-cache)
README.md         This file
LICENSE           GPL-3.0 (inherits upstream)
```

---

## Hosting elsewhere

Any static host works (GitHub Pages, Cloudflare Pages, nginx, Caddy, etc.) as long as:

1. `.wasm` is served as `application/wasm`
2. You are not opening via `file://`
3. (Optional) If you later rebuild with pthreads, add COOP/COEP headers — stubs are commented in `serve.py`

Example nginx snippet:

```nginx
location ~* \.wasm$ {
    default_type application/wasm;
    add_header Cache-Control "no-store";
}
```

---

## Performance tips

1. Prefer **1×** or **2×** scale. Higher scales are for high-end machines only.
2. Keep the tab focused; enable “Low-power mode” in the UI if you background the tab often.
3. Decrypted ROMs only — encrypted dumps will not boot.
4. This build uses the **CPU interpreter** path on wasm (no dynarmic). Further speed needs a source rebuild (`-O3`, LTO, optional frame-skip, stripping diagnostic `glFinish`).

---

## Rebuilding from upstream (optional)

If you want a fresh wasm binary from [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) sources:

```bash
# Emscripten SDK activated
git clone --recursive https://github.com/wheremyfoodat/Panda3DS.git
cd Panda3DS
mkdir build-wasm && cd build-wasm
emcmake cmake .. -DCMAKE_BUILD_TYPE=Release
emmake ninja Alber   # or cmake --build . --target Alber
```

Then copy `Alber.js` / `Alber.wasm` over the ones in this folder and keep the optimized `index.html`.

---

## Credits

### Upstream

- **[Panda3DS](https://github.com/wheremyfoodat/Panda3DS)** by [wheremyfoodat](https://github.com/wheremyfoodat) and contributors — the emulator itself (HLE 3DS core, SDL frontend, experimental Emscripten target). Licensed under **GPL-3.0**.

### This web release (optimization shell + packaging)

- **Grok** ([xAI](https://x.ai)) — performance analysis of the FPS logs, resolution-cap design, optimized `index.html`, `serve.py`, and packaging for a clean GitHub-ready drop.
- **opencode** — collaboration and tooling support on the web port packaging and release prep.

Neither Grok nor opencode claims authorship of the emulator core. All credit for Panda3DS itself belongs to the upstream authors. This repo is a performance-tuned web front-end and distribution of their wasm build.

---

## License

**GPL-3.0** — same as [Panda3DS](https://github.com/wheremyfoodat/Panda3DS).

You must keep the license, preserve upstream attribution, and distribute corresponding source for any modified versions of the emulator binary. The host-page optimizations in `index.html` / `serve.py` are provided under the same license for consistency with the project they ship with.

---

## Disclaimer

This is an unofficial web packaging of an experimental wasm build. Compatibility matches upstream Panda3DS (many titles boot; many still have issues). For native builds and the latest compatibility notes, use the official site: [panda3ds.com](https://panda3ds.com/).

Only use ROMs you legally own.
