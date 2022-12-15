from unicodedata import name
from urllib import response
import xml.etree.ElementTree
import subprocess
import requests
FQDN = "dvs-uatblue.digivalet.com"
Rundeck_Token = "GPE0a5rF328fUHV9Zwj1kmQSudVY0zOn"

try:
    response = requests.get(f"https://{FQDN}/r/api/17/execution/6166/", headers={"X-Rundeck-Auth-Token": Rundeck_Token})
    if response.status_code == 200:
        xmlDocument = xml.etree.ElementTree.fromstring(response.text)
        status = xmlDocument.find("./execution").get('status')
        successfulNodes = [node.get('name') for node in xmlDocument.findall("./execution/successfulNodes/node")]
        failedNodes = [node.get('name') for node in xmlDocument.findall("./execution/failedNodes/node")]
        print(status)
        print(successfulNodes)
        print(failedNodes)
    else:
        print("Pending")
except Exception as e:
    print(e)

