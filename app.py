from flask import Flask, request, jsonify
import picture_uploader
app = Flask(__name__)

@app.route('/', methods=['GET'])
def HelloWorld():
    return picture_uploader.HelloWorld()

@app.route('/image', methods=['POST'])
def upload_image():
    return picture_uploader.upload_image(request)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
