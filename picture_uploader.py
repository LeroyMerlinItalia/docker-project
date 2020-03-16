from flask import request, jsonify
from google.cloud import storage
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def HelloWorld():
    return 'Hello World'


def upload_image(request):
    response = {}
    if request.method != 'POST':
        response['message']='Wrong method'
    elif 'file' not in request.files:
        response['success'] = False
        response['message'] = 'No file part'
    else: 
        file = request.files['file']
        if file.filename == '':
            response['success']=False
            response['message']='No selected file'
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            client = storage.Client()
            #get_bucket('bucket-id') <- https://console.cloud.google.com/storage/browser/[bucket-id]/
            bucket = client.get_bucket('lmit-flask-example')
            blob=bucket.blob('/' + filename) #Path and File name that will be saved.
            blob.upload_from_file(file)
            response['success']=True
            response['message']='Upload done'
        else: 
            response['success'] = False
            response['message'] = 'Invalid file'
    return jsonify(response)