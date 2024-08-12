import requests

response = requests.get("https://www.sydney.edu.au/units/INFO1110/2023-S1C-ND-CC")

htmlbody = str(response.content)

htmlbody.split("")

if ("assessmentDetails" in str(response.content)):
    print("epic")
else:
    print("rip")

print(response.content)


