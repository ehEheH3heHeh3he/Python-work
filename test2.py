import requests

# Define the URL you want to send the PUT request to
url = "http://192.168.1.111"

# Define the XML payload
xml_payload = """
<AudioSetting xmlns="urn:psialliance-org" version="1.0">
    <AudioInVolume min="0" max="100">20</AudioInVolume>
    <AudioInMute>false</AudioInMute>
</AudioSetting>
"""

# Send the PUT request with the XML payload
response = requests.put(url, data=xml_payload, headers={"Content-Type": "application/xml"})

# Print the response status code and content
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)