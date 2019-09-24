# Turn Lights Colors with NLP

Use a very simple neural net ([Pytorch](https://github.com/pytorch/pytorch)) to turn text into colors. Then via [Flask](https://github.com/pallets/flask) and [Phue](https://github.com/studioimaginaire/phue/blob/master/phue.py) turns your lights into colors, assuming you have Hue lights in your house.


# Warning

The Flask app uses [literal eval](https://docs.python.org/3/library/ast.html#ast.literal_eval) so be careful to secure whatever server your lights are running on so someone malicious doesn't crash it :)

## Some quick notes

- The model uses pre-trained GloVe word vectors, and by default picks a random vector for unknown tokens.
- I used training data from [here](https://github.com/andrewortman/colorbot/tree/master/data), which I learned of via Janelle Shane's [post](https://aiweirdness.com/post/160985569682/paint-colors-designed-by-neural-network-part-2) about generating color names via RNN.
- Used this [function](https://gist.github.com/error454/6b94c46d1f7512ffe5ee) to convert rgb to xy. 

## How to use

1. Make sure everything in requirements.txt is installed.
2. You will need to discover the IP of your Bridge and upload this value as config.py. Instructions available at the Phillips Hue API [Developer's Guide](https://developers.meethue.com/develop/get-started-2/).
3. You may need to push the button on the bridge the first time you load the Flask server.
