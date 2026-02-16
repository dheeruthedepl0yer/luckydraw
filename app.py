from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

participants = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global participants
    file = request.files["file"]
    df = pd.read_excel(file)

    filtered = df[df["Are you attending the Year End Event?"].str.lower() == "yes"]

    participants = [
        {
            "name": row["Name"],
            "email": row["Email"]
        }
        for _, row in filtered.iterrows()
        if pd.notna(row["Name"]) and pd.notna(row["Email"])
    ]

    return jsonify(participants)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
