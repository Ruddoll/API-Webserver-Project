import http.server
import socketserver
import json
import sqlite3

# Set the port number to listen on
PORT = 8000

# Define the request handler class
class APIRequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.db_connection = sqlite3.connect('mydatabase.db')
        super().__init__(*args, **kwargs)

    # Set the response headers
    def set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    # Handle GET requests
    def do_GET(self):
        try:
            if self.path == '/users':
                # Retrieve all users from the database
                cursor = self.db_connection.cursor()
                cursor.execute('SELECT * FROM users')
                users = cursor.fetchall()

                # Prepare the response data
                response_data = {
                    'users': users
                }
                response = json.dumps(response_data)

                # Set the response headers and send the response content
                self.set_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                self.handle_error('Not found', status_code=404)
        except Exception as e:
            self.handle_error(str(e))

    # Handle POST requests
    def do_POST(self):
        try:
            if self.path == '/users':
                # Retrieve and parse the request payload
                content_length = int(self.headers.get('Content-Length'))
                payload = self.rfile.read(content_length).decode('utf-8')
                payload_data = json.loads(payload)

                # Validate and sanitize the data
                name = payload_data.get('name')
                email = payload_data.get('email')

                # Check if required fields are present
                if not name or not email:
                    self.handle_error('Missing required fields', status_code=400)
                    return

                # Insert the new user into the database
                cursor = self.db_connection.cursor()
                cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
                self.db_connection.commit()

                # Prepare the response data
                response_data = {
                    'message': 'User created successfully'
                }
                response = json.dumps(response_data)

                # Set the response headers and send the response content
                self.set_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                self.handle_error('Not found', status_code=404)
        except Exception as e:
            self.handle_error(str(e))

    # Handle errors and return appropriate error codes and messages
    def handle_error(self, message, status_code=500):
        response_data = {
            'error': message
        }
        response = json.dumps(response_data)
        self.set_headers(status_code=status_code)
        self.wfile.write(response.encode('utf-8'))

    def finish(self):
        self.db_connection.close()
        super().finish()

# Create a socket server with the specified port
with socketserver.TCPServer(('', PORT), APIRequestHandler) as server:
    print(f'Server running on port {PORT}')

    # Start the server
    server.serve_forever()
