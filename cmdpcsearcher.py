import os

# Dictionary mapping asset numbers to IP addresses
asset_to_ip = {
    'asset1': '192.168.1.1',
    'asset2': '192.168.1.2',
    'asset3': '192.168.1.3',
    # Add more assets as needed
}

# Function to ping a single IP address
def ping(ip):
    print(f"Pinging IP address: {ip}")
    response = os.system(f"ping -n 1 {ip}")

    if response == 0:
        return f"{ip} is reachable"
    else:
        return f"{ip} is not reachable"

# Main function to loop through assets and ping each one, saving the results
def main():
    results = []  # List to store the results
    for asset, ip in asset_to_ip.items():
        print(f"Asset Number: {asset}")
        result = ping(ip)
        results.append(result)  # Add the result to the list

    # Print all the results at the end
    print("\nPing Results:")
    for result in results:
        print(result)

# Start the program
if __name__ == "__main__":
    main()
