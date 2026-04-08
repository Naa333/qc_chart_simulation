from datetime import datetime, timezone

import requests


def main() -> None:
    payload = {
        "test_name": "glucose",
        "value": 42.0,
        "unit": "mg/dL",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "instrument_id": "analyzer-A",
    }

    response = requests.post("http://127.0.0.1:8000/results", json=payload, timeout=10)
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()
