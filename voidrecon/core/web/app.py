from flask import Flask, render_template, request, jsonify

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/button-click', methods=['POST'])
        def button_click():
            return jsonify(message="Button click received by Flask!")

    def run(self, **kwargs):
        self.app.run(**kwargs)
