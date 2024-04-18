import Pyro4
import time

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        result = str1 + str2
        return result

def main():
    daemon = Pyro4.Daemon()  # Create a Pyro daemon

    # Wait for a while to ensure the nameserver is running
    time.sleep(5)

    try:
        ns = Pyro4.locateNS()  # Locate the Pyro nameserver
    except Pyro4.errors.NamingError:
        print("Error: Could not locate the Pyro nameserver.")
        print("Make sure the nameserver is running.")
        return

    # Create an instance of the server class
    server = StringConcatenationServer()

    # Register the server object with the Pyro nameserver
    uri = daemon.register(server)
    ns.register("string.concatenation", uri)

    print("Server URI:", uri)

    try:
        with open("server_uri.txt", "w") as f:
            f.write(str(uri))
            f.flush()  # Ensure data is written immediately
    except IOError as e:
        print("Error writing to file:", e)

    daemon.requestLoop()

if __name__ == "__main__":
    main()
