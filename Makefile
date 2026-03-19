up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

venv:
	python3 -m venv .venv && . .venv/bin/activate && python -m pip install -U pip setuptools wheel

api:
	. .venv/bin/activate && uvicorn app:app --reload --port 8000
