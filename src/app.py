import imghdr
import os
from inference import run, get_model
from flask import Flask, render_template, request,  redirect, url_for, abort, send_from_directory, jsonify
from werkzeug.utils import secure_filename
#from waitress import serve

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2*1024*1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jpeg']
app.config["UPLOAD_PATH"] = "uploads"
app_root = os.path.dirname(os.path.abspath(__file__)) +"/" + app.config["UPLOAD_PATH"]


#load model into memory for faster inference
model = get_model()


def validate_image(stream):
    header = stream.read(1024)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + format

@app.route("/")
def index():
    return render_template('index.html')
    

@app.route("/",methods=['GET','POST'])
def upload_file():
    
    if request.method == "POST": 
        if "file" not in request.files:
            print("nofile attached in request")
            return redirect(url_for("index"))
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                print(file_ext)
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:    
                    abort(400)
                print("starting to save file")
                file.save(os.path.join(app_root, filename))
                print("file saved sucessfully at {}".format(os.path.join(app_root, filename)))
            files = os.listdir(app_root)    
            return render_template('index.html',files=files)
    else:
        files = os.listdir(app_root) 
        return render_template('index.html',files=files)

@app.route("/show_pred",methods=["POST"])
def show_pred():
    if request.method=="POST":
        prediction = []
        probs = []
        files = os.listdir(app_root)
        for file in files:
            print(file)
            output , prob = run(os.path.join(app_root,file),model)
            prob = round(prob*100,2)
            probs.append(str(prob)+"%")
            prediction.append("I think the food is {} with a probability of {}%".format(output,prob))
            
        for file in files:
            os.remove(os.path.join(app_root,file)) 
        return render_template('index.html',prediction_text=prediction, files=files)
        
    else:
        return redirect(url_for('upload_file'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app_root, filename)


@app.route("/predict",methods=["GET","POST"])
def predict():
    files = os.listdir(app_root)
    predictions = []
    probs = []
    for file in files:
        output , prob= run(os.path.join(app_root, file))

        prob = round(prob*100,2)
        predictions.append(output)
        probs.append(str(prob)+"%")


    preds = {
        "food":predictions,
        "probability":probs
    }    
    return jsonify(preds)

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route('/info', methods=['GET'])
def short_description():
    desc = {
     "model": "Resnet50V2",
     "input-size": "224x224x3",
     "num-classes": 12,
     "pretrained-on": "ImageNet"
     }
    return jsonify(desc)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    # For production mode, comment the line above and uncomment below
    # serve(app, host="0.0.0.0", port=8000)
