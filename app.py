from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from flask import redirect, flash
import smtplib
from email.mime.text import MIMEText
import re
import csv

app = Flask(__name__)
secret_key = 'your_secret_key'

# Define responses based on keywords

responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "pneumonia": "Pneumonia is an infection that inflames the air sacs in one or both lungs. It can be caused by bacteria, viruses, or fungi.",
    "symptoms": "Common symptoms of pneumonia include cough with phlegm or pus, fever, chills, and difficulty breathing.",
    "treatment": "Treatment for pneumonia may include antibiotics, antiviral drugs, or antifungal drugs, depending on the cause.",
    "prevention": "To prevent pneumonia, practice good hygiene, get vaccinated, and avoid smoking.",
    "contact": "You can contact us at varsharacharla1503@gmail.com or call us at +91-12345-67890.",
    "hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "location": "Our clinic is located at 123 Health Street, Wellness City.",
    "insurance": "Yes, we accept most major insurance plans. Please contact our office for more details.",
    "appointment": "You can book an appointment by calling +91-12345-67890 or visiting our website.",
    "services": "We offer a range of services including X-rays, blood tests, and comprehensive health check-ups.",
    "emergency": "In case of an emergency, please call the emergency services at 112."
}

# Ensure the 'uploads' folder exists
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model and define the class labels
model = load_model('our_model3.h5')
class_labels = [ 'Normal', 'Pneumonia'] 

def predict_image(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Ensure the image is normalized

    # Make predictions
    predictions = model.predict(img_array)

    # Classification prediction
    class_prediction = np.argmax(predictions)
    class_label = class_labels[class_prediction]
    class_confidence = predictions[0][class_prediction] * 100  # Convert to percentage

    # Collect all class probabilities
    probabilities = {class_labels[i]: float(predictions[0][i]) * 100 for i in range(len(class_labels))}

    return class_label, class_confidence, probabilities

def load_cities():
    cities_data = {}
    with open('sc.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            state = row['state']
            city = row['city']
            if state not in cities_data:
                cities_data[state] = []
            cities_data[state].append(city)
    return cities_data

cities_data = load_cities()

@app.route('/get-states', methods=['GET'])
def get_states():
    states = list(cities_data.keys())
    return jsonify({'states': states})

@app.route('/get-cities', methods=['GET'])
def get_cities():
    state = request.args.get('state')
    cities = cities_data.get(state, [])
    return jsonify({'cities': cities})

doctors_data = [
    {"name": "Dr. A", "specialization": "Cardiologist", "phone": "1234567890", "email": "doctorA@example.com", "state": "Andhra Pradesh", "city": "Visakhapatnam"},
    {"name": "Dr. B", "specialization": "Dentist", "phone": "2345678901", "email": "doctorB@example.com", "state": "Andhra Pradesh", "city": "Vijayawada"},
    {"name": "Dr. C", "specialization": "Neurologist", "phone": "3456789012", "email": "doctorC@example.com", "state": "Karnataka", "city": "Bangalore"},
    {"name": "Dr. D", "specialization": "Pediatrician", "phone": "4567890123", "email": "doctorD@example.com", "state": "Karnataka", "city": "Mysore"},
    {"name": "Dr. E", "specialization": "General Physician", "phone": "5678901234", "email": "doctorE@example.com", "state": "Tamil Nadu", "city": "Chennai"},
    {"name": "Dr. F", "specialization": "Dermatologist", "phone": "6789012345", "email": "doctorF@example.com", "state": "Maharashtra", "city": "Mumbai"}
]
@app.route('/get-doctors', methods=['GET'])
def get_doctors():
    state = request.args.get('state')
    city = request.args.get('city') 
    filtered_doctors = [doctor for doctor in doctors_data if doctor['state'] == state and doctor['city'] == city]
    return jsonify({'doctors': filtered_doctors})



def find_response(user_input):
    for key in responses:
        if re.search(key, user_input):
            return responses[key]
    return "I'm not sure how to help with that. Please ask about pneumonia symptoms, treatment, prevention, or contact information."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip().lower()
    response = find_response(user_input)
    return jsonify(response=response)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Perform prediction
        predicted_class, confidence, probabilities = predict_image(file_path)

        # Redirect to the result page with prediction result
        return redirect(url_for('result', filename=file.filename, predicted_class=predicted_class, confidence=confidence))

    return jsonify({'error': 'File not processed'})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/uploadfile')
def uploadfile():
    return render_template('upload.html')

@app.route('/consult')
def consult():
    return render_template('consult.html')

@app.route('/result')
def result():
    filename = request.args.get('filename')
    predicted_class = request.args.get('predicted_class')
    confidence = float(request.args.get('confidence'))   
    return render_template('result.html', filename=filename, predicted_class=predicted_class, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
