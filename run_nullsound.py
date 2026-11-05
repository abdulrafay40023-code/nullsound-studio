import http.server
import socketserver
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 7860
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def guess_type(self, path):
        if path.endswith(".m4a"):
            return "audio/mp4"
        if path.endswith(".mp3"):
            return "audio/mpeg"
        if path.endswith(".wav"):
            return "audio/wav"
        return super().guess_type(path)

def start_server():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print("=" * 60)
        print("NULLSOUND STUDIO IS RUNNING ON http://localhost:7860")
        print("CORS & Range Audio Streaming Enabled!")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()

if __name__ == "__main__":
    start_server()
