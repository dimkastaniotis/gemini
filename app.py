from flask import Flask, jsonify
import random
import os
from datetime import datetime

app = Flask(__name__)

# Λίστα με τυχαία facts
facts = [
    "Το 70% της Γης καλύπτεται από νερό.",
    "Οι καρχαρίες υπάρχουν πριν από τους δεινόσαυρους.",
    "Το μέσο όρο του ανθρώπινου εγκεφάλου ζυγίζει περίπου 1.4 κιλά.",
    "Το αλφάβητο της Χαβάης έχει μόνο 12 γράμματα.",
    "Το φως του ήλιου χρειάζεται 8 λεπτά και 20 δευτερόλεπτα για να φτάσει στη Γη."
]

# Λίστα με Python tips
python_tips = [
    "Χρησιμοποίησε τις λίστες (lists) για να αποθηκεύσεις πολλαπλά στοιχεία.",
    "Το `f-string` είναι ένας εύκολος τρόπος για να διαμορφώσεις strings.",
    "Χρησιμοποίησε τη συνάρτηση `enumerate()` για να πάρεις και το index και το value σε ένα loop.",
    "Το `zip()` σου επιτρέπει να συνδυάσεις πολλαπλές λίστες.",
    "Χρησιμοποίησε το `with` για να ανοίγεις αρχεία και να είσαι σίγουρος ότι θα κλείσουν σωστά."
]

# Συνάρτηση για να επιλέγει ένα τυχαίο fact
def get_random_fact():
    return random.choice(facts)

def get_python_tip():
    return random.choice(python_tips)
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
