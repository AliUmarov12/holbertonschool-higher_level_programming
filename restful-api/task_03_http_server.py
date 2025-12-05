#!/usr/bin/python3
import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests"""

        # ============================
        # 1) Root endpoint: "/"
        # ============================
        if self.path == "/":
            self.send_response(200)  # Status code = 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # ============================
        # 2) /data → return JSON data
        # ============================
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())
            return

        # ============================
        # 3) /status → return API status
        # ============================
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # ============================
        # 4) Undefined endpoint → 404
        # ============================
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"404 Not Found: This endpoint does not exist")


# ============================
# Running the HTTP server
# ============================
if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("localhost", port), SimpleAPI)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()
