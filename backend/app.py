from flask import Flask, request, jsonify
from flask_cors import CORS
from generator import generate_email_tests, generate_password_tests

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate_tests():
    
    data = request.json
    field_type = data.get("field_type")
    
    if field_type == "email":
        result = generate_email_tests()
    
    elif field_type == "password":
        result = generate_password_tests()
    
    else:
        result = ["Unsupported field type"]

    return jsonify({
        "field_type": field_type,
        "test_cases": result
    })


if __name__ == "__main__":
    app.run(debug=True)