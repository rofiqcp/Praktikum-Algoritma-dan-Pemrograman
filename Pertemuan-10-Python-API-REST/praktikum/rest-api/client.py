import requests
URL='http://127.0.0.1:5000/api/products'
try:
    r=requests.get(URL,timeout=5); r.raise_for_status(); print('GET',r.json())
    r=requests.post(URL,json={'name':'USB Hub','stock':4},timeout=5); r.raise_for_status(); print('POST',r.json())
except requests.Timeout: print('Timeout')
except requests.RequestException as e: print('Request error',e)
