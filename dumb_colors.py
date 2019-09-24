import torch
from torchnlp.word_to_vector import GloVe
import torch.nn as nn
import torch.nn.functional as F
import math

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(300, 500)
        self.fc2 = nn.Linear(500, 200)
        self.fc3 = nn.Linear(200, 3)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return (x)

random_tensor = torch.Tensor.uniform_
vectors = GloVe('6B', unk_init = random_tensor)

net = Net()
net.load_state_dict(torch.load('color_model_dict.pt'))
net.eval()

def get_some_rgb_from_text(color_string):
    input_words = str(color_string).split()
    sample_tensors = [vectors[x] for x in input_words]
    mean_sample = torch.mean(torch.stack(sample_tensors), dim=0)
    rgb = tuple(int(x) if x<255 else 255 for x in net(mean_sample.view(-1,300))[0])
    return rgb

def EnhanceColor(normalized):
    if normalized > 0.04045:
        return math.pow( (normalized + 0.055) / (1.0 + 0.055), 2.4)
    else:
        return normalized / 12.92

def hgb_to_xy(rgb_as_iter):
    r,g,b = rgb_as_iter
    rNorm = r / 255.0
    gNorm = g / 255.0
    bNorm = b / 255.0

    rFinal = EnhanceColor(rNorm)
    gFinal = EnhanceColor(gNorm)
    bFinal = EnhanceColor(bNorm)
    
    X = rFinal * 0.649926 + gFinal * 0.103455 + bFinal * 0.197109
    Y = rFinal * 0.234327 + gFinal * 0.743075 + bFinal * 0.022598
    Z = rFinal * 0.000000 + gFinal * 0.053077 + bFinal * 1.035763

    if X + Y + Z == 0:
        return (0,0)
    else:
        xFinal = X / (X + Y + Z)
        yFinal = Y / (X + Y + Z)
    
        return (xFinal, yFinal)

def predict_color(text_string):
    rgb_tup = get_some_rgb_from_text(text_string)
    converted_xy = hgb_to_xy(rgb_tup)
    return converted_xy


