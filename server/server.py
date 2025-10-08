from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime, timezone
import socket

class LoggingHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print('Allah Hu')
        ts = datetime.now(timezone.utc).isoformat(timespec='milliseconds') + 'Z'
        host = socket.gethostname()
        ip = self.client_address[0]
        status = "SUCCESS" if args[1] == 200 else "FAILURE"
        print(f"[{ts}] [{host} ({ip})] {status} - {format % args}")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), LoggingHandler)
    print("Server started on port 8080")
    server.serve_forever()
