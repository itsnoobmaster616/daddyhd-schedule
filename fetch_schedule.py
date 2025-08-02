import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Referer': 'https://dlhd.click/',
}
def fetch_schedule():
    print("Fetching DaddyHD Schedule...")

    res = requests.get('https://dlhd.click/schedule/schedule-generated.php', headers=HEADERS)
    if res.status_code != 200:
        print(f"✖ Failed (Status Code: {res.status_code})")
        return None

    data = res.json()
    with open("schedule.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✔ schedule.json saved")
    return data

if __name__ == "__main__":
    fetch_schedule()
