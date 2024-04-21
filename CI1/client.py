import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    while True:
        n = int(input("Enter the number to calculate the factorial for that:"))
        
        result = proxy.Factorial_RPC(n)
        print(f"Factorial of {n} is {result}")
except KeyboardInterrupt:
    print("Exiting...")