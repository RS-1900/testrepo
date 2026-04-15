
FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app/ .

ENV PATH=/root/.local/bin:$PATH

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]


