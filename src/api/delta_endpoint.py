import json

from src.config import config
from flask import Flask, jsonify
from deltalake import DeltaTable

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/delta', methods=['GET'])
def home():
    dt = DeltaTable(config.get("delta-input-data"))

    pd = dt.to_pyarrow_dataset().to_table().to_pandas()

    json_str = pd.to_json(orient="records")

    parsed = json.loads(json_str)

    return jsonify(parsed)


if __name__ == "__main__":
    app.run()