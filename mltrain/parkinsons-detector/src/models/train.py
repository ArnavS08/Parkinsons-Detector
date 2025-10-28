def train_model(model, X_train, y_train, X_val, y_val, epochs=100, batch_size=32):
    history = model.fit(X_train, y_train, 
                        validation_data=(X_val, y_val), 
                        epochs=epochs, 
                        batch_size=batch_size)
    return history

def evaluate_model(model, X_test, y_test):
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")
    return loss, accuracy

def save_model(model, filepath):
    model.save(filepath)
    print(f"Model saved to {filepath}")

def load_model(filepath):
    from tensorflow.keras.models import load_model
    model = load_model(filepath)
    print(f"Model loaded from {filepath}")
    return model