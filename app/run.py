from flask import Flask, render_template
from app.modules.string.views import stringProcessorAPI

app = Flask(__name__)

# String processor APIs
app.register_blueprint(stringProcessorAPI)


@app.route('/')
def index():
    return render_template("index.html")


# NEED to set host='0.0.0.0' otherwise the service won't be reachable when running in a Docker container
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9528)
