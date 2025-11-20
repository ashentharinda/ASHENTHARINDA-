import http.server
import socketserver
import os

PORT = 8001

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html' # Default to index.html
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Navigate to this address in your web browser to see your portfolio.")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()