"""Small local echo server for Day 2.

It listens only on 127.0.0.1 and supports GET requests.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs, urlparse


HOST = "127.0.0.1"
PORT = 8002


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        raw_args = parse_qs(parsed.query)
        args = {
            key: values[0] if len(values) == 1 else values
            for key, values in raw_args.items()
        }
        response_data = {
            "args": args,
            "headers": dict(self.headers.items()),
            "method": "GET",
            "path": parsed.path,
            "url": f"http://{HOST}:{PORT}{self.path}",
        }
        body = json.dumps(response_data, ensure_ascii=False, indent=2).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.client_address[0]} - {format % args}")


def main() -> None:
    server = HTTPServer((HOST, PORT), EchoHandler)
    print(f"Day 2 Echo Server: http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Day 2 Echo Server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
