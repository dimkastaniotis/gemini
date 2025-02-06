from flask import Flask, jsonify
import random

app = Flask(__name__)

# Λίστα με αποφθέγματα
quotes = [
    "Το μόνο αδύνατο είναι αυτό που δεν προσπάθησες.",
    "Η μάθηση είναι το μοναδικό όπλο που δεν μπορεί να αφαιρεθεί.",
    # ... Πρόσθεσε περισσότερα αποφθέγματα
]

@app.route('/quote')
def get_quote():
    # Επιλογή τυχαίου αποφθέγματος
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(debug=True)
