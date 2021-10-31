from flask import Flask, render_template, request, redirect, send_file, abort, flash
from gs import GoogleBucket
import os
from pathlib import PureWindowsPath


credentials = PureWindowsPath("path to json")


class DevConfig:
    SECRET_KEY = 'SECRET-KEY'
    DEBUG = True

app = Flask(__name__)
app.config.from_object(DevConfig)

#UPLOAD_FOLDER = "uploads"
BUCKET = "bucket_name"

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/upload")
def home():
    #contents = list_buckets()
    return render_template('upload.html')


@app.route("/upload_file", methods=['POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(f.filename))
        source_filename = f.filename
        google_bucket = GoogleBucket(credentials,BUCKET)
        path = 'uploads'
        gs_filename = '/'.join([path,source_filename])
        try:
            google_bucket.upload_file(source_filename, gs_filename)
            flash('Carga satisfactoria!', 'success')
        except Exception as e:
            abort(404)
        finally:
            os.remove(f.filename)

        return redirect("/upload")
#
#
#@app.route("/download/<string:filename>", methods=['GET'])
#def download(filename):
#    if request.method == 'GET':
#        output = download_file(filename, BUCKET)
#
#        return send_file(output, as_attachment=True)
#