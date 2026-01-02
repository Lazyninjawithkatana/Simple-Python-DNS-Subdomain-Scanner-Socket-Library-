Simple Python DNS Subdomain Scanner (Socket Library)

Learn how to use Python's built-in socket library to perform DNS reconnaissance. This script automates the process of identifying active subdomains on a target by attempting to resolve them into IPv4 addresses. It’s a lightweight, "real-world" tool for understanding how network requests work at a lower level than typical web scrapers.

Key Features:

Fast DNS Resolution: Uses socket.gethostbyname for direct IP lookups.

Colorized Output: Visual feedback for successful hits (Green) and errors (Red) using Colorama.

Auto-Logging: Saves every discovered IP and subdomain to a .txt file for later analysis.

Error Handling: Safely skips subdomains that don't exist without crashing the script.

How to use:

Place your subdomain wordlist (e.g., bitquark-top100k.txt) in the same folder.

Run the script: python3 dns_scanner.py

Enter your target (e.g., example.com).

⚠️ Legal Disclaimer: This tool is for educational purposes and authorized security testing only. Never scan targets you do not have explicit permission to test.
