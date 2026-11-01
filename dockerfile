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
ENV FLASK_APP=app.py

# Run the Flask app when the continer starts
CMD ["flask", "run", "--host=0.0.0.0"]






# Step 1: Now build the Docker image using the following command in the terminal:
# docker build -t my-flask-app .
# Step 2: Then run the container with the following command:
# docker run -p 5000:5000 my-flask-app
# Step 3: Tag the image for Docker Hub (replace <username> with your Docker Hub username):
# docker tag my-flask-app <username>/my-flask-app:latest
# Step 4: Push the image to Docker Hub:
# docker push <username>/my-flask-app:latest
# Step 5: Pull the image from Docker Hub on another machine (replace <username> with your Docker Hub username):
# docker pull <username>/my-flask-app:latest
# Step 6: Run the pulled image from Docker Hub:
# docker run -p 5000:5000 <username>/my-flask-app:latest