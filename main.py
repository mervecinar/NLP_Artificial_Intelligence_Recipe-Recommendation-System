from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pandas as pd

app = Flask(__name__)

# Geliştirilmiş Eğitim Verisi
data = {
    "text": [
        "I am so happy today!", "I feel very sad and depressed.", "I am extremely stressed out!",
        "I am feeling very tired and exhausted.", "I am just okay, neither happy nor sad.", "I am so angry right now!",
        "What a wonderful day!", "I can't stop crying.", "Everything is going wrong!",
        "I don't have any energy left.", "I am content and relaxed.", "I am furious about what happened!",
        "Feeling great after my workout!", "It's a gloomy day.", "Work is overwhelming me.",
        "I need to take a nap.", "I feel calm and peaceful.", "I am really annoyed!",
        "Life is beautiful!", "I am feeling blue.", "The pressure is too much.",
        "I can't keep my eyes open.", "Everything is in balance.", "I am enraged!",
    ],
    "label": [
        "mutlu", "üzgün", "stresli", "yorgun", "nötr", "sinirli",
        "mutlu", "üzgün", "stresli", "yorgun", "rahat", "sinirli",
        "mutlu", "üzgün", "stresli", "yorgun", "rahat", "sinirli",
        "mutlu", "üzgün", "stresli", "yorgun", "rahat", "sinirli"
    ]
}

df = pd.DataFrame(data)

# TF-IDF Vektörleştirici ve Model Eğitimi
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']
model = LinearSVC(C=0.5)  # C değeri ayarlanabilir
#model = LogisticRegression(C=1.0)
model.fit(X, y)

# Geliştirilmiş Yemek Tarifleri
recipes = {
    "mutlu": ["Izgara Sebzeler", "Meyve Salatası", "Yeşil Smoothie", "Meyveli Yoğurt", "Cevizli Salata"],
    "üzgün": ["Tavuk Çorbası", "Domates Çorbası", "Kremalı Makarna", "Sıcak Çikolata", "Kakao"],
    "yorgun": ["Yulaf Ezmesi", "Protein Smoothie", "Enerji Barları", "Meyve Suyu", "Fıstık Ezmeli Sandviç"],
    "enerjik": ["Quinoa Salatası", "Avokado Tost", "Badem Ezmesi", "Kinoa Salatası", "Fındık"],
    "stresli": ["Muzlu Smoothie", "Yulaf Ezmesi", "Izgara Tavuk", "Muz", "Karpuz"],
    "rahat": ["Yoğurtlu Meyve", "Tam Buğday Tost", "Sebzeli Omlet", "Balık Tacos", "Domates Salatası"],
    "sinirli": ["Lavanta Çayı", "Ihlamur", "Çikolata", "Sıcak Çikolata", "Kek"]
}

#diyetkolik
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']

    if not text:
        return jsonify({"error": "Metin boş olamaz."}), 400

    # Duygu analizi yap
    X_input = vectorizer.transform([text])
    emotion = model.predict(X_input)[0]

    # Duygu durumuna göre yemek tarifi öner
    recipe_suggestions = recipes.get(emotion, ["Herhangi bir tarif bulunamadı."])

    return jsonify({"emotion": emotion, "recipes": recipe_suggestions})


if __name__ == '__main__':
    app.run(debug=True)
