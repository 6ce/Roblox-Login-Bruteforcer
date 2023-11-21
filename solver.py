import requests as Requests
import json as JSON

CAP_API_KEY = "IMPORT_CAPSOLVER_API_KEY_HERE"
CAP_BAL_API = "https://api.capsolver.com/getBalance"
CAP_CREATE_API = "https://api.capsolver.com/createTask"
CAP_RESULT_API = "https://api.capsolver.com/getTaskResult"

Headers = {
    "Content-Type": "application/json", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

class Funcaptcha:
    def __init__(self):
        print("[+] Funcaptcha Solver Loaded")

    def GetTask(self, Url: str, JSUrl: str, Key: str, Blob: dict):
        Data = {
            "clientKey": CAP_API_KEY,
            "task": {
                "type": "FunCaptchaTaskProxyLess",
                "websiteURL": Url,
                "funcaptchaApiJSSubdomain": JSUrl,
                "websitePublicKey": Key,
                "data": JSON.dumps(Blob)
            }
        }
        Data = JSON.dumps(Data)
        Response = Requests.post(url=CAP_CREATE_API, headers=Headers, data=Data)
        return Response.json()["taskId"]

    def GetResult(self, TaskId: str):
        Data = {
            "clientKey": CAP_API_KEY,
            "taskId": TaskId
        }
        Data = JSON.dumps(Data)
        Response = Requests.post(url=CAP_RESULT_API, headers=Headers, data=Data)
        return Response.json()
