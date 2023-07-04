import flask

app = Flask(__name__)

@app.run("/")
def index():
    return "hi"

if __name__ == "__main__":
    app.run(port="9900")
