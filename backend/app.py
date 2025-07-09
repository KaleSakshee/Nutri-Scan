from flask import Flask, request, jsonify
from analyzer import analyze_product
from barcode_parser import parse_barcode
from history_manager import save_search, get_search_history
from profile_manager import get_user_profile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "NutriScan backend is running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json(force=True)
    product_name = data.get('product_name')
    user_id = data.get('user_id')

    if not product_name or not user_id:
        return jsonify({'error': 'Missing product_name or user_id'}), 400

    user_allergies = get_user_profile(user_id)
    result = analyze_product(product_name)
    result['user_allergies'] = user_allergies

    save_search(user_id, product_name, result)
    return jsonify(result)

@app.route('/scan-barcode', methods=['POST'])
def scan_barcode():
    data = request.get_json(force=True)
    barcode = data.get('barcode')
    user_id = data.get('user_id')

    if not barcode or not user_id:
        return jsonify({'error': 'Missing barcode or user_id'}), 400

    product_name = parse_barcode(barcode)
    if not product_name:
        return jsonify({'error': 'Product not found'}), 404

    user_allergies = get_user_profile(user_id)
    result = analyze_product(product_name)
    result['user_allergies'] = user_allergies

    save_search(user_id, product_name, result)
    return jsonify(result)

@app.route('/history/<user_id>', methods=['GET'])
def history(user_id):
    return jsonify({'history': get_search_history(user_id)})

if __name__ == '__main__':
    app.run(debug=True)
