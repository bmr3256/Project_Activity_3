import requests

# API 

def get_ipv4(): #Gets IPv4 address using ipify.
    try:
        response = requests.get(
            "https://api.ipify.org?format=json",
            timeout=5
        )
        response.raise_for_status()

        data = response.json()
        return data["ip"]

    except (requests.RequestException, KeyError, ValueError):
        return "Unavailable"


def get_ipv6(): #Gets IPv6 address using ipify.
    try:
        response = requests.get(
            "https://api6.ipify.org?format=json",
            timeout=5
        )
        response.raise_for_status()

        data = response.json()
        return data["ip"]

    except (requests.RequestException, KeyError, ValueError):
        return "Unavailable"


def get_ip_information(ip_address): #Gets extra IP info vusing ipwho.is
    try:
        response = requests.get(
            f"https://ipwho.is/{ip_address}",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if not data.get("success"):
            return None

        connection = data.get("connection", {})

        return {
            "ip": data.get("ip", "Unavailable"),
            "country_name": data.get("country", "Unavailable"),
            "country": data.get("country_code", "Unavailable"),
            "city": data.get("city", "Unavailable"),
            "region": data.get("region", "Unavailable"),
            "org": connection.get("isp", "Unavailable"),
            "asn": connection.get("asn", "Unavailable")
        }

    except (requests.RequestException, ValueError):
        return None


# Starts App

if __name__ == "__main__":
    from gui import create_application

    create_application()
