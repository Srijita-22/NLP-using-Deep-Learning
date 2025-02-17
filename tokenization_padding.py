MAX_VOCAB_SIZE = 1000  # Limit vocabulary size
MAX_SEQUENCE_LENGTH = 10  # Limit sequence length

tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE)
tokenizer.fit_on_texts(df['cleaned_text'])
sequences = tokenizer.texts_to_sequences(df['cleaned_text'])
padded_sequences = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

# Print sample sequence
print("Sample Sequence:", sequences[0])
print("Padded Sequence:", padded_sequences[0])
