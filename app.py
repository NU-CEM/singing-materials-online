# Import statement
from flask import Flask, render_template, request
import subprocess

# Flask app initialization
app = Flask(__name__)

# Defines route for root url
@app.route('/')
def index():
    return render_template('index.html')

# Defines a route for handling form submissions sent
@app.route('/submit', methods=['POST'])
def submit():
    mp_ids = request.form.getlist('mp_id')
    min_phonon = request.form.get('min_phonon')
    max_phonon = request.form.get('max_phonon')
    time_length = request.form.get('time_length')

    # Build the command to run the sound_module.py script
    command = [
        'python', 'sound_module.py',
        *mp_ids,
        '--min_phonon', min_phonon,
        '--max_phonon', max_phonon,
        '--timelength', time_length
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        return "Sound generated successfully!"
    except subprocess.CalledProcessError as e:
        return f"Error generating sound: {e}"

if __name__ == "__main__":
    app.run(debug=True)
