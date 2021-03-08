# from django.test import TestCase
import requests

# Tests for the API endpoints.

base_url = 'http://localhost:8002/api/v1/facility/'
# base_url = 'https://ml.nmugaya.org/api/v1/facility/'

headers = {'Authorization': 'Token 760e0f1b4a9f3defa67926cad3634ec5fb0cbe42'}

params = {
    "name": "Test facility 007-001",
    "official_name": "Test facility 007-001",
    "reg_number": "1010",
    "keph_level": 4,
    "beds": 7,
    "cots": 6,
    "is_operational": True,
    "facility_type": 1,
    "owner_type": 1,
    "approved": True
}
# Test delete
test = 0
facility_id = '59403259-737e-4d1e-8798-6c554a9ca178'
if test == 0:
    url = base_url + facility_id + '/'
    response = requests.delete(url, headers=headers)
    print(response.headers)
    print(response.content)
elif test == 1:
    # Test create
    url = base_url
    response = requests.post(url, json=params, headers=headers)
    print(response.headers)
    print(response.json())
elif test == 2:
    # Test Update
    url = base_url + facility_id + '/'
    response = requests.put(url, json=params, headers=headers)
    print(response.headers)
    print(response.json())
