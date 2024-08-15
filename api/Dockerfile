ARG DOCKER_BUILDKIT=1
FROM python:3.10-alpine AS builder
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
# CMD ["pip", "list"]

FROM builder
WORKDIR /src
COPY --from=builder /app /src
COPY .  .
# EXPOSE 8000
CMD ["python", "-u", "app.py"]
