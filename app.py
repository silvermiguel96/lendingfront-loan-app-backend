from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evaluate-loan', methods=['POST'])
def evaluate_loan():
    data = request.json
    requested_amount = data.get('requestedAmount')

    if requested_amount is None:
        return jsonify({"error": "requestedAmount is required"}), 400

    if requested_amount > 50000:
        decision = "Declined"
    elif requested_amount == 50000:
        decision = "Undecided"
    else:
        decision = "Approved"

    return jsonify({"loanDecision": decision})

if __name__ == '__main__':
    app.run(debug=True)
