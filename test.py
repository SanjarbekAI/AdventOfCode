import requests

url = "https://api.marsit.uz/api/v1/coins/mark_student"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3aG8iOjAsInN1YiI6IjMyNSIsImV4cCI6MTcwMTc3MzMzOX0.x0GuC0L_Wc202kQ0rlcc08pzmice2M6zoGzWzFewyAk",
    "Content-Type": "application/json",
}


payload = {
    "student_id": 1966,
    "group_id": 353,
    "coins": 10
}

response = requests.post(url, headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    print("POST request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
