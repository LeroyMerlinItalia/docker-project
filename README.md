# docker-project


## Local version

```bash
pip install -r requirements.txt
$env:GOOGLE_APPLICATION_CREDENTIALS=".\GOOGLE_CREDENTIAL_FILE.json"
py app.py runserver
```

Using Postman, I made a POST request to localhost:5000/image.
request.Body has a field named File, containg the image to send.


## Docker version

```bash
docker build -t DOCKER_NAME .
docker run -d -p 6080:5000 DOCKER_NAME
```
Using Postman, I made a POST request to 192.168.99.100:6080/image.
request.Body has a field named File, containg the image to send.


## Cloud Run

```bash
docker build -t DOCKER_NAME .
docker tag DOCKER_NAME eu.gcr.io/lmit-factorylab-dev-itlm/DOCKER_NAME
docker push eu.gcr.io/lmit-factorylab-dev-itlm/DOCKER_NAME
```

I generated a IDENTITY_TOKEN using:

```bash
gcloud auth print-identity-token
```
Using Postman, I made a POST request to https://lmit-picture-uploader-ohgh6dv4bq-ew.a.run.app/image.
request.Authoization (type Bearer Token) contains IDENTITY_TOKEN.
request.Body has a field named File, containg the image to send.

## Cloud Functions

Using Postman, I made a POST request to https://us-central1-lmit-factorylab-dev-itlm.cloudfunctions.net/picture_uploader.
request.Body has a field named File, containg the image to send.