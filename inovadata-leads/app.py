from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-leads", methods=["POST"])
def get_leads():
    data = request.get_json()
    domain = data.get("company", "").strip().lower()

    sample_data = {
        "openai.com": [
            {"name": "Sam Altman", "position": "CEO", "email": "sam@openai.com", "confidence": "95%"},
            {"name": "Mira Murati", "position": "CTO", "email": "mira@openai.com", "confidence": "92%"},
        ],
        "google.com": [
            {"name": "Sundar Pichai", "position": "CEO", "email": "sundar@google.com", "confidence": "96%"},
            {"name": "Jeff Dean", "position": "Head of AI", "email": "jeff@google.com", "confidence": "90%"},
        ],
        "microsoft.com": [
            {"name": "Satya Nadella", "position": "CEO", "email": "satya@microsoft.com", "confidence": "97%"},
            {"name": "Kevin Scott", "position": "CTO", "email": "kevin@microsoft.com", "confidence": "91%"},
        ],
        "amazon.com": [
            {"name": "Andy Jassy", "position": "CEO", "email": "andy@amazon.com", "confidence": "95%"},
            {"name": "Swami Sivasubramanian", "position": "VP of AI", "email": "swami@amazon.com", "confidence": "89%"},
        ],
        "meta.com": [
            {"name": "Mark Zuckerberg", "position": "CEO", "email": "mark@meta.com", "confidence": "98%"},
            {"name": "Andrew Bosworth", "position": "CTO", "email": "boz@meta.com", "confidence": "90%"},
        ],
        "tesla.com": [
            {"name": "Elon Musk", "position": "CEO", "email": "elon@tesla.com", "confidence": "96%"},
            {"name": "Drew Baglino", "position": "SVP Powertrain", "email": "drew@tesla.com", "confidence": "89%"},
        ],
        "nvidia.com": [
            {"name": "Jensen Huang", "position": "CEO", "email": "jensen@nvidia.com", "confidence": "97%"},
            {"name": "Bill Dally", "position": "Chief Scientist", "email": "bill@nvidia.com", "confidence": "92%"},
        ],
    }

    leads = sample_data.get(domain, [
        {"name": "John Doe", "position": "Marketing Manager", "email": f"john@{domain}", "confidence": "85%"},
        {"name": "Jane Smith", "position": "Sales Lead", "email": f"jane@{domain}", "confidence": "88%"}
    ])

    return jsonify(leads)

if __name__ == "__main__":
    app.run(debug=True)
