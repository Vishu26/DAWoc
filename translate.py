import pandas as pd
import numpy as np
from keras.models import Model
from keras.layers import Input, LSTM, Dense

samples = 10000

path = 'fra.txt'
data = pd.DataFrame.from_csv(path, sep='\t', header=0)
data.columns = ['fr']

data['en'] = data.index
data.reset_index(inplace=True)
fr = np.array(data['fr'])[:samples]
en = np.array(data['en'])[:samples]

for i in range(samples):
    fr[i] = '\t' + fr[i] + '\n'

en_char = set()
fr_char = set()

for word in en:
    for char in word:
        en_char.add(char)

for word in fr:
    for char in word:
        fr_char.add(char)

en_char = sorted(list(en_char))
fr_char = sorted(list(fr_char))
encoder_tokens = len(en_char)
decoder_tokens = len(fr_char)
encoder_seq_length = max([len(line) for line in en])
decoder_seq_length = max([len(line) for line in fr])

en_word_idx = dict([(char, i) for i, char in enumerate(en_char)])
fr_word_idx = dict([(char, i) for i, char in enumerate(fr_char)])


encoder_input_data = np.zeros(
    (len(en), encoder_seq_length, encoder_tokens),
    dtype='float32')
decoder_input_data = np.zeros(
    (len(en), decoder_seq_length, decoder_tokens),
    dtype='float32')
decoder_target_data = np.zeros(
    (len(en), decoder_seq_length, decoder_tokens),
    dtype='float32')

for i, (input_text, target_text) in enumerate(zip(en, fr)):
    for t, char in enumerate(input_text):
        encoder_input_data[i, t, en_word_idx[char]] = 1.
    for t, char in enumerate(target_text):
        decoder_input_data[i, t, fr_word_idx[char]] = 1.
        if t > 0:
            decoder_target_data[i, t - 1, fr_word_idx[char]] = 1.

units = 256
epochs = 10
batch_size = 512


enc_input = Input(shape=(None, encoder_tokens))
encoder = LSTM(units, return_state=True)
encoder_outputs, state_h, state_c = encoder(enc_input)

encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(None, decoder_tokens))

decoder_lstm = LSTM(units, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                                     initial_state=encoder_states)
decoder_dense = Dense(decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([enc_input, decoder_inputs], decoder_outputs)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)

model.save('tran.h5')
