# Base image with Python 3.12 runtime
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy dependency file to container
COPY requirements.txt /app

# Install dependencies without caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files to container
COPY . .

# Command to run the Python application
CMD [ "python", "iSolution-app.py" ]
