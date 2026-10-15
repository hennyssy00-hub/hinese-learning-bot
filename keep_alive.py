"""
Keep-alive HTTP server for Render deployment.
Render Free tier requires a Web Service to bind to an HTTP port (PORT environment variable)
and answer HTTP health checks. This keeps the Telegram bot process alive.
"""

import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Bot Telegram Hoc Tieng Trung dang hoat dong 24/7!")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

    def log_message(self, format, *args):
        # Tranh spam log console moi lan ping
        pass


def run_server(port: int):
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"[KeepAlive] Web server listening on port {port} (Ready for Render & UptimeRobot)")
    server.serve_forever()


def keep_alive():
    """Khoi dong HTTP server o mot background thread doc lap."""
    port = int(os.environ.get("PORT", 8080))
    thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    thread.start()
