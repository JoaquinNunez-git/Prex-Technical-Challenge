
from flask import Flask, request, jsonify
import csv
from datetime import datetime
import os

app = Flask(__name__)

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/submit', methods=['POST'])
def submit_info():
    data = request.json
    ip_address = data['ip_address']
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"{ip_address}_{timestamp}.csv"
    filepath = os.path.join(DATA_DIR, filename)
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ip_address', 'processor', 'processes', 'users', 'os_name', 'os_version'])
        writer.writerow([
            ip_address,
            data['processor'],
            ','.join(data['processes']),
            ','.join(data['users']),
            data['os_name'],
            data['os_version']
        ])
    
    return jsonify({"message": "Data received and stored successfully"}), 200

@app.route('/query/<ip_address>', methods=['GET'])
def query_info(ip_address):
    files = os.listdir(DATA_DIR)
    matching_files = [f for f in files if f.startswith(ip_address)]
    
    if not matching_files:
        return jsonify({"message": "No data found for the given IP address"}), 404
    
    latest_file = max(matching_files)
    filepath = os.path.join(DATA_DIR, latest_file)
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        data = next(reader)
    
    # Convert string representations back to lists
    data['processes'] = data['processes'].split(',')
    data['users'] = data['users'].split(',')
    
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)