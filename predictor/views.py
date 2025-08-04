import pickle
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CropSelectionForm

model = pickle.load(open('random_forest.sav', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

def home(request):
    return render(request, 'predictor/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def predict_crop(request):
    result = None
    if request.method == 'POST':
        form = CropSelectionForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['nitrogen'],
                form.cleaned_data['phosphorus'],
                form.cleaned_data['potassium'],
                form.cleaned_data['temperature'],
                form.cleaned_data['humidity'],
                form.cleaned_data['ph'],
                form.cleaned_data['rainfall'],
            ]
            prediction_encoded = model.predict([data])[0]
            prediction = label_encoder.inverse_transform([prediction_encoded])[0]
            result = prediction
    else:
        form = CropSelectionForm()
    return render(request, 'predictor/crop_form.html', {'form': form, 'result': result})
