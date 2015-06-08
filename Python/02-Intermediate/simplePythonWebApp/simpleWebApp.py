from os import curdir, sep

from http.server import BaseHTTPRequestHandler, HTTPServer

class StoreHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		print("Enter do_Get: " + self.path)
		if self.path.endswith("index.html"):
			f = open("index.html")
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes(f.read(), 'UTF-8')  )
			f.close()
			return
		if self.path.endswith("form1.html"):
			f = open("form1.html")
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes(f.read(), 'UTF-8')  )
			f.close()
			return
		if self.path.endswith("list1.html"):
			f = open("list1.html")
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes(f.read(), 'UTF-8')  )
			f.close()
			return
		if self.path.endswith("jquery.min.js"):
			f = open("jquery.min.js")
			self.send_response(200)
			self.send_header('Content-type', 'text/javascript')
			self.end_headers()
			self.wfile.write(bytes(f.read(), 'UTF-8')  )
			f.close()
			return
		if self.path.endswith("get_list"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			list = self.get_user_list_html()
			self.wfile.write(bytes(list, 'UTF-8'))
			return
		if self.path.endswith("favicon.ico"):
			# ignore this request
			return
		self.send_response(404)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		not_found_page = (
			"<HTML><HEAD><TITLE>Page Not Found</TITLE></HEAD><BODY>" + 
			"Sorry that page could not be found " + 
			"</BODY></HTML>"
		)
		self.wfile.write(bytes(not_found_page, 'UTF-8'))
		return
		
	def do_POST(self):
		print("Enter do_POST: " + self.path)
		if self.path.endswith("form1"):
			length = self.headers['content-length']
			data = self.rfile.read(int(length))
			print("data: " + data.decode(encoding='UTF-8'))
			rawParam = data.decode(encoding='UTF-8')
			params = rawParam.split("&")
			name, name_value = params[0].partition("=")[::2]
			new_name_value = name_value.replace("+", " ")
			age, age_value = params[1].partition("=")[::2]
			print("name: " + new_name_value)
			print("age: " + age_value)
			self.save_user(new_name_value, age_value)
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			page = (
				"<HTML><HEAD><TITLE>Entry Added Successfully</TITLE></HEAD><BODY>" + 
				"Thank you for adding " + 
				" the name " + new_name_value + " with an age of " + age_value +
				"<table><tr><td><a href=\"index.html\">Home</a></td></tr></table>" +
				"</BODY></HTML>"
			)
			self.wfile.write(bytes(page, 'UTF-8'))
		return
		
	def save_user(self, name, age):
		print("name: " + name + " age: " + age)
		with open('user_data.txt', 'a') as file:
			file.write(name + ", " + age + "\n")
		return
		
	def get_user_list_html(self):
		ins = open( "user_data.txt", "r" )
		user_html = "<ul>"
		for line in ins:
			user_html += "<li>" + line.strip() + "</li>"
		ins.close()
		user_html += "</ul>"
		return user_html

server = HTTPServer(('', 8000), StoreHandler)
server.serve_forever()

