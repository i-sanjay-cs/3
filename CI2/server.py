import Pyro4

@Pyro4.expose
class StringConcat:
    def string_concat(self,s1,s2):
        return s1 + s2

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(StringConcat)
    ns.register("string.concatenator",uri)
    print("Server is ready")
    daemon.requestLoop()

if __name__ == "__main__":
    main()