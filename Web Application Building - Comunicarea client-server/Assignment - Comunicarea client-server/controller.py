from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import model
import json

HOST = '127.0.0.1'
PORT = 80

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
           self.curent_path('client_app.html')
        else:
            try:
                path = parse_qs(self.path[2:])
                if model.data(path['student_card_number'][0]) != None:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'name':model.data(path['student_card_number'][0], 'name'),
                        'last_name':model.data(path['student_card_number'][0], 'last_name'),
                        'student_card_number':model.data(path['student_card_number'][0], 'student_card_number'),
                        'note':model.data(path['student_card_number'][0], 'note')
                    }).encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write('incorect parameters'.encode())  
            except :
                pass

    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            model.save_in_db(data['add_name'][0], data['add_last_name'][0], data['add_student_card_number'][0], data['add_note'][0])
            self.log_message('success')
            self.wfile.write('Succes added'.encode())
        except KeyError:
            self.log_message('incorect parameters')
            self.wfile.write('incorect parameters'.encode())

    def curent_path(self, data):
        with open(data) as html:
            file = html.read()
        self.send_response_to_client(200, file)

    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        
        self.end_headers()
        self.wfile.write(str(data).encode())

if __name__ == '__main__':
    server_adress = (HOST, PORT)
    http_server = HTTPServer(server_adress, RequestHandler)
    http_server.serve_forever()