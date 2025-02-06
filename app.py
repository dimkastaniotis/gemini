from flask import Flask, jsonify
import random
from datetime import datetime
import os  # Εισαγωγή της βιβλιοθήκης os

app = Flask(__name__)

# Λίστα με τυχαία facts
facts = [
    "70% of the Earth is covered by water.",
    "Sharks have existed before dinosaurs.",
    "The average human brain weighs about 1.4 kilograms.",
    "The Hawaiian alphabet only has 12 letters.",
    "Sunlight takes 8 minutes and 20 seconds to reach Earth."

]

# Λίστα με Python tips
python_tips = [
    "(lists) olalal",
    "to  `f-string` einai kalo",
    
]

# Συνάρτηση για να επιλέγει ένα τυχαίο fact
def get_random_fact():
    return random.choice(facts)

# Συνάρτηση για να επιλέγει ένα τυχαίο tip
def get_python_tip():
    random.seed(datetime.now().day)
    return random.choice(python_tips)

# Διαδρομή για τυχαίο fact
@app.route("/api/fact", methods=["GET"])
def random_fact():
    fact = get_random_fact()
    return jsonify({"fact": fact})

# Διαδρομή για τυχαίο Python tip
@app.route("/api/tip", methods=["GET"])
def python_tip():
    tip = get_python_tip()
    return jsonify({"tip": tip})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
