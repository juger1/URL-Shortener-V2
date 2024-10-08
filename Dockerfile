FROM python:3.11-slim-bullseye

# Install required system packages
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 build-essential python3-dev git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application files
COPY . .

# Set the command to run both scripts
CMD ["sh", "-c", "python3 get_config.py && python3 main.py"]
