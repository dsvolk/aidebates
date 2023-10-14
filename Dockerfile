FROM python:3.10-slim

LABEL maintainer="Denis Volk <denis.volk@toptal.com>"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# Copy the rest of the application code into the container at /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app
COPY . /app

# Install requirements
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# Make the port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the bot
CMD ["python", "src/app.py"]