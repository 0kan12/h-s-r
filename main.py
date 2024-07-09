from flask import Flask, render_template

app = Flask(__name__)

# Bildirimleri içeren bir liste oluştur
notifications = [
    "Bildirim 1: Lorem ipsum dolor sit amet.",
    "Bildirim 2: Consectetur adipiscing elit.",
    "Bildirim 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Bildirim 4: Ut enim ad minim veniam.",
    "Bildirim 5: Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
]

@app.route('/')
def index():
    return render_template('index.html', notifications=notifications)

if __name__ == '__main__':
    app.run(debug=True)
