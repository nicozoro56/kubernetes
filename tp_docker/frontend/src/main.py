import pandas as pd
import numpy as np
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading
import urllib.request

hostName = "0.0.0.0"
serverPort = 8080

class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
      backendURL = "http://backend-service.default.svc.cluster.local:5000/"
      # curl http://<ServerIP>/index.html
      if self.path == "/":
          # Respond with the file contents.
          self.send_response(200)
          self.send_header("Content-type", "application/json")
          self.end_headers()
          content = ''.encode()
          with urllib.request.urlopen(backendURL) as url:
            content = json.dumps(json.load(url)).encode()
            
          self.wfile.write(content)

      else:
          self.send_response(404)

      return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""


def main():
  df = pd.DataFrame([{"name": "Nicolas", "surname": "Pluven", "student number":21907722},{"name": "Théophile", "surname": "Romieu", "student number":22306075}])
  print(df)
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