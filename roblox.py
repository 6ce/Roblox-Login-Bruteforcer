import base64 as Base64
import json as JSON
import requests as Requests
import time as Time
from solver import Funcaptcha

Funcaptcha = Funcaptcha()

LOGIN_API = "https://auth.roblox.com/v2/login"
ROBLOX_URL = "https://www.roblox.com"
JS_URL = "https://roblox-api.arkoselabs.com"

ROBLOX_KEY = "476068BF-9607-4799-B53D-966BE98E2B81"

Username = "IMPORT_ROBLOX_USERNAME_HERE"
Password = "IMPORT_ROBLOX_PASSWORD_HERE"

def GetCSRF():
    Response = Requests.post(url=LOGIN_API)
    return Response.headers["x-csrf-token"]

def DecodeMetadata(MetadataB64: str):
    return JSON.loads(Base64.b64decode(MetadataB64).decode("utf-8"))

def StartLogin():
    print("[+] Generating CSRF Token")
    CSRF = GetCSRF()
    print(f"[+] Generated CSRF Token: {CSRF}")
    Headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Csrf-Token": CSRF
    }
    Data = {
        "ctype": "Username",
        "cvalue": Username,
        "password": Password
    }
    print("[+] Starting login process")
    Response = Requests.post(url=LOGIN_API, headers=Headers, json=Data)
    ResHeaders = Response.headers

    if Response.status_code == 429:
        print("[+] Ratelimited. Waiting a minute to retry.")
        Time.sleep(60)
        return StartLogin()

    ChallengeId = ResHeaders["rblx-challenge-id"]
    MetadataB64 = ResHeaders["rblx-challenge-metadata"]
    print(f"[+] FunCaptcha Challenge ID: {ChallengeId}")

    Metadata = DecodeMetadata(MetadataB64)
    DataExchange = Metadata["dataExchangeBlob"]
    Blob = {"data[blob]": DataExchange}

    TaskId = Funcaptcha.GetTask(Url=ROBLOX_URL, JSUrl=JS_URL, Key=ROBLOX_KEY, Blob=Blob)
    print(f"[+] FunCaptcha TaskId: {TaskId}")
    Result = Funcaptcha.GetResult(TaskId)
    print(f"[+] FunCaptcha Task Result: {str(Result)}")
    
StartLogin()
