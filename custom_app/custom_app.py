from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Get current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Render an HTML template with the message and image
    return render_template("index.html", time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
