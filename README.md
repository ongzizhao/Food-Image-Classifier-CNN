# SG Dishes CNN Image Classifier
This is a front-to-end project whereby a Flask web app is dockerized and deployed to classify 12 food images.

## Data Source
Data can be downloaded as a tar file [here](https://drive.google.com/file/d/17rG2Bj56ESfVfOGUrMiTfK2x6IRXS8Gh/view?usp=sharing). Consist of 12 different food items totalling 1224 images. 

## Architecture of Model
The model is built upon a ResNet50V2 model, followed by a global pooling, 512 neurons dense layer with ReLU and finally a softmax output with 12 classes. The weights in the base model is 
kept fixed while the weights in the dense and softmax layers are trainable. This model has 1,055,244 trainable parameers.

The 12 food items are chilli_crab, curry_puff, dim_sum, ice_kacang, kaya_toast, nasi_ayam, popiah, roti_prata, sambal_stingray, satay, tau_huay, wanton_noodle.

## Training
The model is trained with an initial 1224 images of food items. The dataset is then expanded with various image augmentation techniques to generate more training images. The images are rotated, translated, sheared, minimized, magnified and a cut out is randomly applied across the image. The dataset is expanded to 6244 images after image augmentation.

## Performance
The model performed decently well with an accuracy of 70-75% average over the 12 food items

## Setting up
### Dependencies
This project uses the Flask framework to set up and is runnng tensorflow for the deep learning model.
- Numpy: 1.18.5
- Pandas: 1.1.5
- Tensorflow: 2.0.0
- Pillow
- Flask: 1.1.2
- Gunicorn: 20.1.0
- H5py: 2.10.0

### Running the Flask web app
To run the web app locally, you can deploy the web app locally using flask on the terminal
<li>set FLASK_APP=app.py</li>
<li>set FLASK_ENV=develpment</li>
<li>set FLASK_RUN_PORT=8000</li>
<li>set FLASK_RUN_host=0.0.0.0</li>
<li>flask run </li>
<br>
The flask web app will be run on locally on port 8000. Upload a food image and click submit to see the image uploaded. Click Classify to see the results

## Deployment
The project is created using Flask, Gunicorn, with Pure-CSS as the frame work (a basic usage as i am still quite new to CSS and HTML).

### Folder Structure
```python:
├── conda.yml
├── model.h5
├── notebook.ipynb
├── README.md
├── src
│   ├── app.py
│   ├── inference.py
│   └── templates
│        ├── index.html
│        └── documentation.html
```

## Demo

![alt text](https://github.com/ongzizhao/Food-Image-Classifier-CNN/blob/main/data/Demo.JPG?raw=true)
