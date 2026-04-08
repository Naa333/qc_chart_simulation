# lab-system

Clean minimal FastAPI project with one endpoint: `POST /results`.

## Project structure

```text
lab-system/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── models/
│   │   └── result_model.py
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   ├── services/
│   │   └── result_service.py
│   ├── validators/
│   │   └── result_validator.py
│   └── events/
│       └── event_handler.py
│
├── scripts/
│   └── producer.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run API

```bash
uvicorn app.main:app --reload
```

## Test endpoint

```bash
curl -X POST http://127.0.0.1:8000/results \
	-H "Content-Type: application/json" \
	-d '{"sample_id":"A-100","value":42, "metadata":{"source":"manual"}}'
```

## Simulate analyzer

```bash
python scripts/producer.py
```
