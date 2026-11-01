# Create the base image from the official Python 3.11 image
FROM python:3.11-slim 

# Set the working directory in the container
WORKDIR /app 

# Copy everything into the container
COPY . /app

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP = app.py

# Run the Flask app when the continer starts
CMD ["flasf", "run", "--host = 0.0.0.0", "--port = 5000"]