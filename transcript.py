from flask import Blueprint, Flask, request, jsonify, send_from_directory
import os

transcript_blueprint = Blueprint('transcript', __name__)

@transcript_blueprint.route('/transcript')
def transcript():
    return send_from_directory('static', 'transcript.html')

app = Flask(__name__)

# Specify the absolute path where you want to save the output.txt file
OUTPUT_DIR = r'C:\Users\Lenovo\Desktop\Summereaze'


@app.route('/save_transcript', methods=['POST'])
def save_transcript():
    try:
        data = request.json
        print(f"Received data: {data}")
        
        text = data.get('text', '')
        if not text:
            return jsonify({"status": "error", "message": "No text provided"}), 400
        
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        file_path = os.path.join(OUTPUT_DIR, "output.txt")
        print(f"File path: {file_path}")

        with open(file_path, "w") as f:
            f.write(text)
            f.write("\n")
        
        return jsonify({"status": "success"})
    
    except Exception as e:
        print(f"Error saving transcript: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
