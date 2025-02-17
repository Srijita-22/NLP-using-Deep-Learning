def predict_category(text):
    cleaned_text = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned_text])
    padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
    prediction = model.predict(padded_sequence)
    category_index = np.argmax(prediction)
    return label_encoder.inverse_transform([category_index])[0]

# Example Predictions
print(predict_category("The president announces new policies"))
print(predict_category("The stock market crashes"))
print(predict_category("The football team signs a new player"))
