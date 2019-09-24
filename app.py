from flask import Flask, make_response, request, abort, jsonify, render_template
from dumb_colors import predict_color, get_some_rgb_from_text
from phue import Bridge
import config
import ast

b = Bridge(config.bridge_ip)

app = Flask(__name__)
app.debug = True

@app.route('/connect_bridge', methods=['POST'])
def connect_bridge():
    print("connecting to bridge...")
    b.connect()
    response = {}
    return jsonify(response), 201

@app.route('/change_color', methods=['POST'])
def colorify_lights():
    if not request.json or ('text_input' not in request.json):
        abort(400)

    text_input = request.json['text_input'].lower()
    which_lights = request.json['lights']

    color = predict_color(text_input)

    rgb = get_some_rgb_from_text(text_input)

    response = {
        'rgb': rgb,
    }

    lights = ast.literal_eval(which_lights)

    b.set_light(lights, {'on': True, 'xy': color})

    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
