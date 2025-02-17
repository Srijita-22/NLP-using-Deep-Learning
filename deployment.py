# Save model
model.save("text_classification_model.h5")

# Load model
loaded_model = tf.keras.models.load_model("text_classification_model.h5")

# Test loaded model
print(predict_category("New sports event is happening!"))
