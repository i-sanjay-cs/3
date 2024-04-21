from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

server = SimpleXMLRPCServer(("localhost",8000))
server.register_function(factorial,"Factorial_RPC")

try:
    print("Server is started on port 8080")
    print("Press Ctrl + C to exit the server")
    server.serve_forever()
except KeyboardInterrupt:
    print("Exiting")