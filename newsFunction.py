import requests
import threading

def actionSendWithApi(esp_ip):
    print(f"Sending msg with API, ip:{esp_ip}")

def actionSendDefault(esp_ip):
    print("Send msg default")

def actionGoGome(esp_ip):
    # Yangi threadda so'rovni bajaramiz
    threading.Thread(target=send_request(esp_ip)).start()

def send_request(esp_ip):
    try:
        # Toggle LED
        response = requests.get('http://192.168.187.183/toggle')  # ESP32 IP manzilini qo'shing
        if response.status_code == 200:
            print("LED toggled successfully")
        else:
            print("Failed to toggle LED")

        # Go Home command
        response = requests.get(f'http://{esp_ip}/go_home')  # ESP32 IP manzilini qo'shing
        if response.status_code == 200:
            print("Go Home command sent successfully")
        else:
            print("Failed to send Go Home command")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error: {e}")



