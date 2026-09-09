import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/72f7eea9-6c1c-4099-852a-32ae1028a645"
STUDENT_NAME = "홍길동"

# 2건의 경보 데이터를 각각 단일 JSON 객체로 구성
alerts_list = [
    {
        "student": STUDENT_NAME,
        "src_ip": "1.2.3.114",
        "level": 10,  # 레벨 10 이상 -> deny
        "rule": "5712"
    },
    {
        "student": STUDENT_NAME,
        "src_ip": "192.168.0.10",
        "level": 3,   # 레벨 10 미만 -> allow
        "rule": "1001"
    }
]

def send_alerts():
    for alert in alerts_list:
        print(f"[전송 중] IP: {alert['src_ip']} / Level: {alert['level']}...")
        try:
            response = requests.post(N8N_WEBHOOK_URL, json=alert, timeout=5)
            if response.status_code == 200:
                print(f" 성공 (HTTP {response.status_code})")
            else:
                print(f" 경고 (HTTP {response.status_code}): {response.text}")
        except Exception as e:
            print(f" 오류 발생: {e}")

if __name__ == "__main__":
    send_alerts()