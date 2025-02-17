import numpy as np  
import pandas as pd  
import tensorflow as tf  
import matplotlib.pyplot as plt  
import nltk  
import re  
from nltk.corpus import stopwords  
from sklearn.model_selection import train_test_split  
from tensorflow.keras.preprocessing.text import Tokenizer  
from tensorflow.keras.preprocessing.sequence import pad_sequences  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout  
from tensorflow.keras.optimizers import Adam 