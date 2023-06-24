import requests

# Replace YOUR_ACCESS_KEY with your actual access key obtained from Numverify
access_key = "YOUR_ACCESS_KEY"

# Enter the phone number to be tracked in the format "+1234567890"
phone_number = "+1234567890"

# Call the Numverify API to validate and track the phone number
response = requests.get(f"http://apilayer.net/api/validate?access_key={access_key}&number={phone_number}")

# Parse the JSON response returned by the API
data = response.json()

# Print the tracking information obtained from the API
print("Country: " + data["country_name"])
print("Location: " + data["location"])
print("Carrier: " + data["carrier"])
