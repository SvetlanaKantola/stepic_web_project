def app(environ, start_response):
      data = b"Hello, World!\n"
      args = environ['QUERY_STRING']
      args = args.replace("&", "\n")
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(args)))
      ])
      return iter([args])

