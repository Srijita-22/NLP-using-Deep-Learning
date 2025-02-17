X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, df['category_encoded'], test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
