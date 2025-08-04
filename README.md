# 🌾 Smart Farming: ML-Driven Crop Recommendation System
A Django-based web application that empowers farmers, agronomists, and researchers with data-driven crop selection using Machine Learning. This platform recommends the most suitable crop for cultivation based on real-time assessments of soil nutrients and local weather conditions through an intuitive, secure web interface and robust MySQL-backed user management.

### ✨ Key Features
#### Machine Learning-Powered Crop Recommendation
Input: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall
Output: Best crop to cultivate, tailored to your field's profile.

#### Interactive Web Interface
Modern login, signup, and crop prediction pages with dynamic design and background imagery.

#### Secure User Authentication
Django’s built-in login/signup/logout ensures account security and privacy.

#### MySQL Database Integration
Comprehensive user management and data storage for scalability and data integrity.

#### eusable, Real-Time ML Model
Optimized Random Forest Classifier (pickled for efficient predictions) seamlessly integrated.

### 🛠️ Technology Stack
<img width="958" height="249" alt="image" src="https://github.com/user-attachments/assets/a626e8fd-a8c4-4dc4-bf07-bc2d49c00194" />


### ⚡ Installation & Setup

#### Clone the Repository
git clone https://github.com/yourusername/cropselection.git
cd cropselection

#### Create & Activate a Virtual Environment
python -m venv venv
#### Windows:
venv\Scripts\activate
#### macOS/Linux:
source venv/bin/activate

#### Install Dependencies
pip install -r requirements.txt

#### Configure MySQL in settings.py
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cropdb',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#### Apply Migrations and Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

#### Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ to use the application.

### 🤖 Machine Learning Model
Model: Random Forest Classifier
Features: N, P, K, Temperature, Humidity, pH, Rainfall
Serialized As: random_forest.sav
Integrated in views.py for seamless live crop recommendations.
