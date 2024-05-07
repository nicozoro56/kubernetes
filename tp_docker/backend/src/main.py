import pandas as pd
import numpy as np
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading
import mysql.connector

hostName = "0.0.0.0"
serverPort = 5000

class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
      # curl http://<ServerIP>/index.html
      if self.path == "/":
          # Respond with the file contents.
          try:
            cnx = mysql.connector.connect(user='pythonuser', password='test1234', host='mysql', database='db_example')
            l = []
            with cnx.cursor as cursor:
              result = cursor.execute("SELECT * FROM students")
              rows = cursor.fetchall()
              for row in rows:
                l.append({"name": row[1], "surname": row[2], "student number":row[3]})
          except (mysql.connector.Error, IOError) as err:
            print(err)
            return
          self.send_response(200)
          self.send_header("Content-type", "application/json")
          self.end_headers()
          df = pd.DataFrame(l)
          print(df)
          content = df.to_json().encode()
          self.wfile.write(content)
          cnx.close()

      else:
          self.send_response(404)

      return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""


def main():
  webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
  print("Server started http://%s:%s" % (hostName, serverPort))

  try:
      webServer.serve_forever()
  except KeyboardInterrupt:
      pass

  webServer.server_close()
  print("Server stopped.")


if __name__ == "__main__":
    main()