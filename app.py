import streamlit as st
import pickle
from PIL import Image
import base64
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction System", layout="wide", page_icon="🩺")

# Function to set background image
def set_bg_image(image_file):
    with open(image_file, "rb") as image_file:
        image_data = image_file.read()
    b64_image = base64.b64encode(image_data).decode()
    bg_image_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{b64_image}");
        background-position: center;
        background-size: full;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.8;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        position: absolute;
    }}
    </style>
    """
    st.markdown(bg_image_style, unsafe_allow_html=True)

# Path to your image
set_bg_image(r"C:\Users\dell\New folder\multiple disease\116.jpg")

# Load the models
heart_disease_model = pickle.load(open(f'Saved_model/Heart_Disease.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'Saved_model/Kidney_Disease.pkl', 'rb'))
liver_disease_model = pickle.load(open(f'Saved_model/Liver_Disease.pkl', 'rb'))


# Create sidebar with option menu including Home button
with st.sidebar:
    selected = option_menu(
        " Main Menu",
        options=['Home', 'Heart Disease Prediction', 'Kidney Disease Prediction', 'Liver Disease Prediction'],
        menu_icon='folder',  # Main menu icon
        icons=['house', 'heart', 'person', 'capsule'],  # Icons for Home, Heart, Kidney, Liver
        default_index=0
    )

# Home Page
if selected == 'Home':
    # Main Title
    #st.markdown("<h1 style='text-align: center; color: black;'> MULTIPLE DISEASE PREDICTION SYSTEM 🩺</h1>", unsafe_allow_html=True)
    # CSS styling for the box
    box_css = """
    <style>
    .box {
        border: 6px double black; /* Double border style */
        padding: 2px;
        text-align: center;
        width: 65%;
        margin: 2px auto; /* Center the box */
    }

    .box h1 {
        font-family: 'Time New Roman';
        font-size: 25px;
        font-weight: bold;
        color: #333; /* Dark color for the text */
    }

    
    """

# Apply the custom CSS in Streamlit
    st.markdown(box_css, unsafe_allow_html=True)

# Content inside the box
    st.markdown("""
    <div class="box">
                <h1>   MULTIPLE DISEASE PREDICTION SYSTEM 🩺</h1>
    </div>
    """, unsafe_allow_html=True)

# Description Text
# CSS to center content with equal margins
    centered_text_css = """
    <style>
    .centered-section {
        margin: 0 auto; /* Auto margins to center */
        max-width: 700px; /* Set a max width for the section */
        padding: 10px; /* Add padding for spacing */
        text-align: center; /* Center the text */
        font-family: 'Arial', sans-serif;
    }

    .centered-section h2 {
        font-size: 20px; /* Title font size */
        #margin-bottom: 15px;
    }

    .centered-section p {
        font-size: 16px; /* Text font size */
        line-height: 1.5; /* Adjust line height for readability */
        text-align: justify; /* Justify text for a clean look */
    }
    </style>
    """

    # Apply the custom CSS
    st.markdown(centered_text_css, unsafe_allow_html=True)
    st.markdown("""
    <div class="centered-section">
        <p>
        This Web Application is designed to help users predict the likelihood of developing certain diseases based on their input features. With the use of trained and tested machine learning models, we provide predictions for **Heart Disease, **Kidney Diseaser** and **Liver Disease**.
        </p>
    </div>""", unsafe_allow_html=True)

    # Add custom CSS to remove the margins between the images
    st.markdown("<div style ='margin-bottom:10px;'> </div>", unsafe_allow_html=True)

# Create 3 columns for the images of heart, kidney, and liver with no space
    col1, col2, col3 = st.columns([1, 1, 1])  # Use equal width for each column

# Load and display the images with no space between them
    with col1:
        st.image("C:/Users/dell/New folder/multiple disease/heart.jpg", caption="Heart Disease", width=300)
    with col2:
        st.image("C:/Users/dell/New folder/multiple disease/kidney.jpeg", caption="Kidney Disease", width=300)
    with col3:
        st.image("C:/Users/dell/New folder/multiple disease/liver.jpeg", caption="Liver Disease", width=300)

# Remove column padding and margins using CSS
    st.markdown(
        """
        <style>
        [data-testid="column"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
                
    # Content for "How to Use" section
    st.markdown("""
    <div class="centered-section">
        <h2>How to Use :</h2>
        <p>
        1. Navigate to the Main Menu using the top-left corner of the screen.<br>
        2. Click on the desired tab among 'Heart Disease', 'Kidney Disease', and 'Liver Disease' to access prediction tools for specific diseases.<br>
        3. Enter relevant information as requested in the input fields.<br>
        4. Click on the "Test Result" button to obtain predictions based on the provided data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Content for "Disclaimer" section
    st.markdown("""
    <div class="centered-section">
        <h2>Disclaimer :</h2>
        <p>
        1. This Web App may not provide accurate predictions at all times. When in doubt, please enter the values again and verify the predictions.<br>
        2. It is important to note that individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.
        </p>
    </div>
    """, unsafe_allow_html=True)    



# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex: 1 for Male, 0 for Female")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
    with col2:
        chol = st.text_input("Serum Cholesterol (mg/dl)")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results (0-2)")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina (1 = yes; 0 = no)")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of Peak Exercise ST Segment (0-2)")
    with col3:
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy (0-3)")
    with col1:
        thal = st.text_input("Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)")

    # Button for prediction
    if st.button("Predict Heart Disease"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        result = "This person has heart disease" if prediction[0] == 1 else "This person does not have heart disease"
        st.success(result)

# Kidney Disease Prediction
if selected == 'Kidney Disease Prediction':
    st.title("Kidney Disease Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        blood_pressure = st.text_input('Blood Pressure')
    with col3:
        specific_gravity = st.text_input('Specific Gravity')
    with col1:
        albumin = st.text_input('Albumin')
    with col2:
        sugar = st.text_input('Sugar')
    with col3:
        red_blood_cells = st.text_input('Red Blood Cells')
    with col1:
        pus_cell = st.text_input('Pus Cell')
    with col2:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')
    with col3:
        bacteria = st.text_input('Bacteria')
    with col1:
        blood_glucose_random = st.text_input('Blood Glucose Random')
    with col2:
        blood_urea = st.text_input('Blood Urea')
    with col3:
        serum_creatinine = st.text_input('Serum Creatinine')
    with col1:
        sodium = st.text_input('Sodium')
    with col2:
        potassium = st.text_input('Potassium')
    with col3:
        haemoglobin = st.text_input('Haemoglobin')
    with col1:
        packed_cell_volume = st.text_input('Packed Cell Volume')
    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')
    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')
    with col1:
        hypertension = st.text_input('Hypertension')
    with col2:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')
    with col3:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')
    with col1:
        appetite = st.text_input('Appetite')
    with col2:
        peda_edema = st.text_input('Peda Edema')
    with col3:
        anaemia = st.text_input('Anaemia')

    # Button for prediction
    if st.button("Predict Kidney Disease"):
        user_input = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps,
                      bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin,
                      packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus,
                      coronary_artery_disease, appetite, peda_edema, anaemia]
        user_input = [float(x) for x in user_input]
        prediction = kidney_disease_model.predict([user_input])
        result = "This person has kidney disease" if prediction[0] == 1 else "This person does not have kidney disease"
        st.success(result)

# Liver Disease Prediction
if selected == 'Liver Disease Prediction':
    st.title("Liver Disease Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input("Age")
    with col2:
        Gender = st.text_input("Gender: 1 for Male, 0 for Female")
    with col3:
        Total_Bilirubin = st.text_input("Total Bilirubin")
    with col1:
        Direct_Bilirubin = st.text_input("Direct Bilirubin")
    with col2:
        Alkaline_Phosphotase = st.text_input("Alkaline Phosphotase")
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')
    with col2:
        Total_Proteins = st.text_input('Total Proteins')
    with col3:
        Albumin = st.text_input('Albumin')
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')

    # Button for prediction
    if st.button("Predict Liver Disease"):
        user_input = [Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase, Total_Proteins, Albumin, Albumin_and_Globulin_Ratio]
        user_input = [float(x) for x in user_input]
        prediction = liver_disease_model.predict([user_input])
        result = "This person has liver disease" if prediction[0] == 1 else "This person does not have liver disease"
        st.success(result)

        
