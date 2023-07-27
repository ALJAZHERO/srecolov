import csv
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def load_data_from_csv(filename, encoding='utf-8'):
    data_dict = {}
    with open(filename, 'r', newline='', encoding=encoding) as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                number, name = row
                data_dict[int(number)] = name
            except ValueError:
                return {}
    return data_dict

filename = "dobitki.csv"  # Replace with the actual filename of your CSV
data_dict = load_data_from_csv(filename, encoding='cp1250')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    try:
        user_input = int(request.form['number'])
        if 1 <= user_input <= 1000:
            if user_input in data_dict:
                result = data_dict[user_input]
            else:
                result = "  tevilka ni veljavna v excel datoteki."
        else:
            result = "Prosim vnesite   tevilko od 1 - 1000."
    except ValueError:
        result = "neveljavni vnos. Prosim vnesite veljavno   tevilko."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
