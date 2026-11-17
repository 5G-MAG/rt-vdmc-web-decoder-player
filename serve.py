# © 2026 Nokia
#
# Licensed under the 5G-MAG Public License (v1.0)

import http.server
import sys
import os
import mimetypes
import argparse
import json
import re

mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')

LEVELS = {'log': '', 'info': '', 'warn': 'WARN ', 'error': 'ERROR'}

# Mirror every forwarded browser log line to this file so it can be inspected
# offline (the agent reads it instead of scraping the terminal).
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'browser-console.log')


# Browser-supplied text goes to the terminal and the log file: drop control characters and newlines
# (keeps tab) so a message cannot clear the screen or forge extra log lines.
_CTRL = re.compile(r'[\x00-\x08\x0a-\x1f\x7f]')


def _clean(text, limit=2000):
    return _CTRL.sub(' ', str(text))[:limit]


def _tee(line):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as fh:
            fh.write(line + '\n')
    except Exception:
        pass


class DevHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'credentialless')
        super().end_headers()

    def do_GET(self):
        # Convenience: redirect the bare root to the sample app.
        if self.path == '/' or self.path == '':
            self.send_response(302)
            self.send_header('Location', '/sample-app/index.html')
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self):
        if self.path == '/log':
            length = min(int(self.headers.get('Content-Length', 0)), 65536)
            body = self.rfile.read(length).decode('utf-8', errors='replace')
            try:
                data = json.loads(body)
                level = data.get('level', 'log')
                if level not in LEVELS:
                    level = 'log'
                msg = _clean(data.get('msg', ''))
                tag = '\033[33mWARN\033[0m ' if level == 'warn' else \
                      '\033[31mERROR\033[0m' if level == 'error' else \
                      '\033[36m[JS]\033[0m '
                print(f'{tag} {msg}', flush=True)
                _tee(f'{level.upper():5} {msg}')
            except Exception:
                print('[JS RAW]', _clean(body[:300]), flush=True)
                _tee(f'RAW   {_clean(body[:300])}')
            self.send_response(204)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        status = args[1] if len(args) > 1 else ''
        if str(status) not in ('200', '204', '304'):
            print(f'[HTTP] {format % args}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dev server with the cross-origin isolation headers the SDK needs.')
    parser.add_argument('port', nargs='?', type=int, default=8080)
    parser.add_argument('--host', default='127.0.0.1',
                        help='address to listen on (default 127.0.0.1; use 0.0.0.0 to reach it from a phone)')
    args = parser.parse_args()
    port = args.port
    # Serve from the package root so /sdk/, /sample-app/, /verify/ and /verification/ are reachable.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Start each run with a fresh log file.
    try:
        open(LOG_FILE, 'w', encoding='utf-8').close()
    except Exception:
        pass
    # Threaded so one stalled client connection (e.g. a flaky wireless-adb phone) can't block the
    # whole server. daemon_threads lets it exit cleanly on Ctrl-C.
    server = http.server.ThreadingHTTPServer((args.host, port), DevHandler)
    server.daemon_threads = True
    print(f'Serving on http://{args.host}:{port}/sample-app/index.html  (console logs forwarded here)')
    server.serve_forever()
