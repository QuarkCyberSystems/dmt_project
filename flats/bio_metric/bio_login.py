import frappe
import requests ,json
import hashlib
from PIL import Image
import base64
import datetime,calendar
from datetime import timedelta
from frappe.utils import encode, get_files_path
from frappe.utils.file_manager import get_file_path




# device login

@frappe.whitelist()
def megvii_login_challenge(device_username, device_password, device_url):
	url = device_url + "/api/auth/login/challenge?username=" + device_username

	payload = {}
	files = {}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload, files=files)

	json_data = json.loads(response.text)
	session_id = json_data['session_id']
	if session_id:
		h_string = str(device_password) + str(json_data['salt']) + str(json_data['challenge'])
		h_pass = hashlib.sha256(h_string.encode("utf-8")).hexdigest()
		return session_id, h_pass


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



# push the personal data to the device

@frappe.whitelist(allow_guest=True)
def create_personal_id():
	device_username="admin"
	device_password="222www"
	device_url="http://hanayenoffice.ddns.net:53443"
	
	session_id, h_pass = megvii_login_challenge(device_username, device_password, device_url)
	status = megvii_device_login(device_username, device_url, session_id, h_pass)
	
	media = get_file_path("hiran95b570.jpeg")
	with open(media, 'rb') as f:
		contents = f.read()
		encoded_string = base64.b64encode(contents)
	
	en_string=encoded_string.decode('UTF-8')  
	 
	if status == 200:
		url = device_url + "/api/persons/item"
		payload = json.dumps({
			"recognition_type": "staff",
			"is_admin": 0,
			"person_name": "arul",
			"group_list": ["1"],
			"face_list":[{"idx":0, "data":en_string}],
			"card_number": "123456425deddswsejf73w25"
		})
		headers = {
			'Content-Type': 'application/json',
			'Cookie': 'sessionID=' + session_id
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		json_data = json.loads(response.text)
		frappe.errprint(json_data['status'])
		return json_data

  
def personal_log(json_data):
	
	frappe.errprint(json_data)
	if(json_data['recognition_type']):
		doc=frappe.new_doc("Personal Log")
		doc.update({
			"person_name":json_data['recognition_type'],
			"card_number":json_data['person_name'],
			"message":"Success",
		})
		doc.save(ignore_permissions=True)
	if(json_data['status']==400):
		doc=frappe.new_doc("Personal Log")
		doc.update({
			"person_name":"ds",
			"card_number":"ewe",
			"message":json_data['detail']
		})
		doc.save(ignore_permissions=True)
 
# Set third-party server push configuration

@frappe.whitelist(allow_guest=True)
def set_third_party_push():
	device_username="admin"
	device_password="222www"
	device_url="http://hanayenoffice.ddns.net:53443"
	
	session_id, h_pass = megvii_login_challenge(device_username, device_password, device_url)
	status = megvii_device_login(device_username, device_url, session_id, h_pass)
	frappe.errprint(session_id)

	
	if status == 200:
		url = device_url + "/api/subscribe/push"
		payload = json.dumps({
			"server_uri": "http://167.172.80.19/",
			"method": "post",
		})
		headers = {
			'Content-Type': 'application/json',
			'Cookie': 'sessionID=' + session_id
		}

		response = requests.request("PUT", url, headers=headers, data=payload)
		json_data = json.loads(response.text)
  
		
		return json_data


# pull the data from the device

def access_record():
	device_username="admin"
	device_password="222www"
	device_url="http://hanayenoffice.ddns.net:53443"
	
	session_id, h_pass = megvii_login_challenge(device_username, device_password, device_url)
	status = megvii_device_login(device_username, device_url, session_id, h_pass)
	frappe.errprint(session_id)
 
	to_time = datetime.datetime.now()
	from_time=to_time-timedelta(hours=1, minutes=1)
 
	from_epoch = calendar.timegm(from_time.timetuple())
	to_epoch = calendar.timegm(to_time.timetuple())

	
	if status == 200:
		url = device_url + "/api/passes/query"
		payload = json.dumps({
			"begin_time": from_epoch,
			"end_time": to_epoch,
		})
		headers = {
			'Content-Type': 'application/json',
			'Cookie': 'sessionID=' + session_id
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		json_data = json.loads(response.text)
		return accept_data_log(json_data)


#  Create log for accept data

def accept_data_log(json_data):
	
	person_id = json_data['person_id']
	if(person_id):
		timestamp=json_data['timestamp']
  
		date_time = datetime.datetime.fromtimestamp(timestamp)  
		date=date_time.date()
		time=date_time.time()
		
		doc=frappe.new_doc("Accept Data Log")
		doc.update({
			"person_id":person_id,
			"person_name":json_data['person_name'],
			"card_number":json_data['card_number'],
			"date":date,
			"time":time
		})
		doc.save(ignore_permissions=True)
  
