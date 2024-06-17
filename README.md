# Emotion-Based Recipe Suggestion App

This project is a Flask web application that suggests recipes based on the user's emotional state. The application analyzes text input to determine the user's mood and provides recipes tailored to that mood. It leverages natural language processing (NLP) and machine learning techniques to deliver these functionalities.

## Features

- **Emotion Analysis**: Analyzes the text input from the user to identify emotions such as "happy," "sad," "stressed," "tired," "neutral," and "angry."
- **Recipe Suggestions**: Offers recipe recommendations based on the detected emotion.
- **User-Friendly Interface**: Provides a simple web interface where users can input text and view the suggested recipes.

## Technical Details

- **Flask**: Manages the web-based interface and server-side functionality.
- **scikit-learn**: Utilized for natural language processing and emotion analysis.
- **TF-IDF Vectorization**: Converts user input text into numerical features for model processing.
- **LinearSVC Model**: Used for classifying the text data and predicting the user's emotional state.

## Data Set

- **Training Data**: The project uses a training dataset consisting of sentences representing various emotional states.
- **Recipes**: Lists of suitable recipes are provided for each emotional state. For example, for a "happy" mood, it suggests dishes like fruit salad or green smoothies.

## Setup and Running

To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mervecinar/NLP_Artificial_Intelligence_Recipe-Recommendation-System
   cd NLP_Artificial_Intelligence_Recipe-Recommendation-System 
2. **Install Requirements**:
    ```bash
   pip install -r requirements.txt

3. **Run the Application**:
    ```bash
     python app.py

 4. Usage
On the homepage, enter a sentence in the text input box that reflects your current mood.
Click the "Analyze" button.
The application will analyze your mood and suggest appropriate recipes.


