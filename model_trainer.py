import json
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

colors = ['red', 'yellow', 'green', 'blue']
types = ['1', '2', '3', '4', '5',  '6', '7', '8', '9', 'reverse', 'skip', 'wild', 'wild_draw4']


def encode_card(card):
    color_encoded = [0] * len(colors)
    type_emcoded = [0] * len(types)

    if 'wild' in card:
        color = 'wild'
        type_ = card
    else:
        color, type_ = card.split('_')
