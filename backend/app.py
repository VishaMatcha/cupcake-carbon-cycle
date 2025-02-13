from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:password@localhost/carbon_cycle"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class CarbonData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    co2_level = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def serialize(self):
        return {
            "id": self.id,
            "location": self.location,
            "co2_level": self.co2_level,
            "temperature": self.temperature,
            "timestamp": self.timestamp
        }

@app.route("/data", methods=["GET"])
def get_data():
    records = CarbonData.query.all()
    return jsonify([record.serialize() for record in records])

@app.route("/data", methods=["POST"])
def add_data():
    data = request.get_json()
    record = CarbonData(location=data["location"], co2_level=data["co2_level"], temperature=data["temperature"])
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Data added successfully"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port = 5001)
