from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class ContactHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Change to the directory where the script is located
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == '/save-contact':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            # Ensure the contact.txt file exists
            with open('contact.txt', 'a') as f:
                f.write(post_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Success')
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/':
            # Serve index.html for root path
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/get-contacts':
            try:
                if os.path.exists('contact.txt'):
                    with open('contact.txt', 'r') as f:
                        contacts = f.read()
                else:
                    contacts = ''

                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(contacts.encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            # Serve static files
            return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ContactHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever() 