#!/usr/bin/env python3
"""Serve the Panda3DS wasm build with correct MIME types and no-cache headers."""
import functools
import http.server
import os
import socketserver
import sys

PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "0.0.0.0")
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **getattr(http.server.SimpleHTTPRequestHandler, "extensions_map", {}),
        ".wasm": "application/wasm",
        ".js": "application/javascript",
        ".html": "text/html",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


os.chdir(ROOT)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving {ROOT} at http://{HOST}:{PORT}", flush=True)
    httpd.serve_forever()
