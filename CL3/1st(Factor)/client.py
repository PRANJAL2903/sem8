import requests
def get_factorial(server_address, n):
	url = f"http://{server_address}/factorial"
	response = requests.post(url, json={"n": n})
	factorial = response.json()["factorial"]
	return factorial

if __name__ == "__main__":
	server_address = "localhost:50051" # Replace with your server's address and port
	n = int(input("Enter a non-negative integer: "))
	factorial = get_factorial(server_address, n)
	print(f"Factorial of {n} is {factorial}")