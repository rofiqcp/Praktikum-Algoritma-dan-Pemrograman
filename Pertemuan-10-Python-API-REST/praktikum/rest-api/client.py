import requests
BASE="http://127.0.0.1:5000/api"

def call(method,path,**kwargs):
    try:
        r=requests.request(method,BASE+path,timeout=5,**kwargs)
        print(method,path,"->",r.status_code)
        if r.content: print(r.json() if "application/json" in r.headers.get("Content-Type","") else r.text)
        return r
    except requests.Timeout: print("Request timeout")
    except requests.RequestException as e: print("Network error:",e)

if __name__=="__main__":
    call("GET","/health")
    call("GET","/products")
    call("POST","/products",json={"name":"Monitor","price":1500000,"stock":3})
    call("PATCH","/products/1",json={"stock":9})
    call("GET","/products/999")
