FROM python:3.10-slim

ARG GRADIO_SERVER_PORT=7860

LABEL maintainer="Denis Volk <the.denis.volk@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

ENV GRADIO_SERVER_PORT "${GRADIO_SERVER_PORT}"

# Copy the rest of the application code into the container at /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app
COPY . /app

# Install requirements
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE "${GRADIO_SERVER_PORT}"

# Run the command to start the bot
CMD ["python", "/app/src/app.py"]