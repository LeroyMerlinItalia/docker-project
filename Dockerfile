# Use the official image as a parent image
FROM python:latest

# Set the working directory
COPY . /app

# Copy the file from your host to your current location
WORKDIR /app

# Run the command inside your image filesystem
RUN pip install -r requirements.txt

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 5000

# Run the specified command within the container.
ENTRYPOINT ["python"]

# Copy the rest of your app's source code from your host to your image filesystem.
CMD ["app.py"]