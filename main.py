from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lyrics = [
        "Every day, every night, every second of my life",
        "Let it rain, let it shine, I will choose you every time",
        "Every beat, every breath, every minute I have left",
        "You’re the only thing in life I’ve ever had",
        "That I wanted to",
        "Last forever"
    ]
    return render_template('index.html', lyrics=lyrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
