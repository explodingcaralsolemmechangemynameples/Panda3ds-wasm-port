# Panda3DS WebAssembly — Optimized Release (full package)

This archive contains:

| Path | Contents |
|------|----------|
| `web-release/` | Ready-to-host optimized wasm build (open `index.html` via `python3 serve.py`) |
| `Panda3DS-master-src.zip` | Full upstream Panda3DS source tree this wasm binary was built from |

## Quick run

```bash
cd web-release
python3 serve.py
# open http://127.0.0.1:8000
```

## Credits

- **Emulator core / original wasm target:** [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) by wheremyfoodat & contributors (GPL-3.0)
- **"optimizing" Just made it load faster and like 2-3 extra frames >:(, packaging, README:** Grok (xAI) and opencode

See `web-release/README.md` for performance notes, file list, rebuild steps, and full attribution.

## License

GPL-3.0 — same as upstream Panda3DS. Source is included so the release stays compliant.
