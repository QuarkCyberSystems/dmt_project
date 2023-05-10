import frappe
import requests ,json
import hashlib
from PIL import Image
import base64




@frappe.whitelist(allow_guest=True)
def megvii_login_challenge(device_username, device_password, device_url):
    url = device_url + "/api/auth/login/challenge?username=" + device_username
    payload = {}
    files = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    json_data = json.loads(response.text)
    session_id = json_data['session_id']
    h_string = str(device_password) + str(json_data['salt']) + str(json_data['challenge'])
    h_pass = hashlib.sha256(h_string.encode("utf-8")).hexdigest()
    return session_id, h_pass
    # frappe.errprint(session_id)
    # return megvii_device_login(device_username, device_url, session_id, h_pass)


def megvii_device_login(device_username, device_url, session_id, h_pass):
    
    url = device_url + "/api/auth/login"
    payload = json.dumps({
        "session_id": session_id,
        "username": device_username,
        "password": str(h_pass)
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    status = json_data['status']
    return status
    # frappe.errprint(json_data['session_id'])
    # frappe.errprint(json_data['status'])

    # return session_id
    
    # if status==200:
    #     return create_personal_id(ss_id)
    # else:
    #     return status

@frappe.whitelist(allow_guest=True)
def receive_post_data():
    data = frappe.request.data()
    return data

@frappe.whitelist()
def device_login():

    url = "http://qcshome.hopto.org:9001/api/auth/login/challenge?username=admin&password=222www"
    payload={}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    # session_id = json_data['session_id']
    return json_data
    # return create_personal_id(session_id)

def create_personal_id():
    device_username="admin"
    device_password="222www"
    device_url="http://qcshome.hopto.org:9001"
    # ss_id=megvii_login_challenge(device_username, device_password, device_url)
    ss_id=megvii_login_challenge(device_username, device_password, device_url)
    status=megvii_device_login(device_username, device_url, ss_id[0], ss_id[1])
    
    
    # return ss_id[1]
    # with open("http://167.172.80.19/files/WHG%20Logo%20copy.png", "rb") as img_file:
    #     my_string = base64.b64encode(img_file.read())
    #     return my_string
    if status==200:
        url = "http://qcshome.hopto.org:9001/api/persons/item"
        payload = json.dumps({
            "recognition_type": "staff",
            "is_admin":0,
            "person_name": "anil",
            "group_list":["1"]
        })
        headers = {
            'Content-Type': 'application/json',
            'Cookies':ss_id[1]
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        return json_data
    
                # "card_number": "123456",
