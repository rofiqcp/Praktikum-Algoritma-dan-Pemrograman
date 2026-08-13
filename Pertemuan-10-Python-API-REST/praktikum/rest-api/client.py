import requests

BASE = "http://127.0.0.1:5000/api"


def show_response(response):
    print("status:", response.status_code)
    content_type = response.headers.get("Content-Type", "")
    if response.content:
        print(response.json() if "application/json" in content_type else response.text)


def get_products(query=""):
    try:
        response = requests.get(
            BASE + "/products",
            params={"q": query} if query else None,
            timeout=5,
        )
        show_response(response)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print("Request melewati batas waktu.")
    except requests.HTTPError as exc:
        print("HTTP error:", exc)
    except requests.RequestException as exc:
        print("Network error:", exc)
    return None


def create_product(name, price, stock):
    try:
        response = requests.post(
            BASE + "/products",
            json={"name": name, "price": price, "stock": stock},
            timeout=5,
        )
        show_response(response)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print("Request melewati batas waktu.")
    except requests.HTTPError as exc:
        print("HTTP error:", exc)
    except requests.RequestException as exc:
        print("Network error:", exc)
    return None


if __name__ == "__main__":
    print("== GET collection ==")
    get_products()
    print("== GET dengan query parameter ==")
    get_products("key")
    print("== POST contoh ==")
    create_product("Monitor", 1500000, 3)
