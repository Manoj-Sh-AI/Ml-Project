# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and setup file to the container
COPY requirements.txt setup.py ./

# Install any needed packages specified in requirements.txt
# The '-e .' in requirements.txt will trigger setup.py
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run application.py when the container launches
CMD ["python", "application.py"]
