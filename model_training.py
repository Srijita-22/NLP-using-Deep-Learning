history = model.fit(X_train, y_train, epochs=10, batch_size=4, validation_data=(X_test, y_test))
