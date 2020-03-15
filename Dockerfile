# Use the official image as a parent image
FROM python:latest

# Set the working directory
COPY . /app

# Copy the file from your host to your current location
WORKDIR /app

#Google Cloud Credentials Environment Variable
ENV GOOGLE_APPLICATION_CREDENTIALS /app/lmit-factorylab-dev-c14b9bdb72ca.json

#Cloud run Environment Variables
ENV PORT 5000
ENV HOST 0.0.0.0

# Run the command inside your image filesystem
RUN pip install -r requirements.txt

# Run the specified command within the container.
ENTRYPOINT ["python"]

# Copy the rest of your app's source code from your host to your image filesystem.
CMD ["app.py"]
