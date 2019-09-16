from flask import Flask, make_response, request, abort, jsonify, render_template
from dumb_colors import predict_color, get_some_rgb_from_text
from phue import Bridge
import config
b = Bridge(config.bridge_ip)

app = Flask(__name__)
app.debug = True

@app.route('/connect_bridge', methods=['POST'])
def connect_bridge():
    b.connect()
    return jsonify(response), 201

@app.route('/change_color', methods=['POST'])
def colorify_lights():
    if not request.json or ('text_input' not in request.json):
        abort(400)

    text_input = request.json['text_input']
    which_lights = ['lights']

    color = predict_color(text_input)

    rgb = get_some_rgb_from_text(text_input)

    response = {
        'rgb': rgb,
    }

    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fancy')
def styled_page():
    return render_template('home_with_styling.html')
    
if __name__ == '__main__':
    app.run(debug=False)
