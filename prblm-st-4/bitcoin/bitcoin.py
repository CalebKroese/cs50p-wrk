import sys
import requests

def main():
    # Check command‐line argument
    if len(sys.argv) != 2:
        sys.exit("Missing or too many command‐line arguments")

    # Try to convert the argument to float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command‐line argument is not a number")

    # Query the CoinCap API
    api_key = "YourApiKey"  # <-- replace with your actual key
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Could not request Bitcoin price.")

    # Parse JSON
    try:
        data = response.json()
        # According to CoinCap docs, "priceUsd" is the key for the price in USD
        price_str = data["data"]["priceUsd"]
        price = float(price_str)
    except (KeyError, TypeError, ValueError):
        sys.exit("Invalid response from API.")

    # Calculate cost
    cost = n * price

    # Format with , as a thousands separator, 4 decimal places
    # Example: if cost is 1234567.891234, this prints "$1,234,567.8912"
    formatted = f"${cost:,.4f}"
    print(formatted)


if __name__ == "__main__":
    main()