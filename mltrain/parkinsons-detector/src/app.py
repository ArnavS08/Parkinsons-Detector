from data.load_data import load_data
from data.preprocess import preprocess_data
from features.extract_features import extract_features
from models.train import train_model

def main():
    # Load the dataset
    data = load_data('path/to/dataset.csv')
    
    # Preprocess the data
    preprocessed_data = preprocess_data(data)
    
    # Extract features
    features, labels = extract_features(preprocessed_data)
    
    # Train the model
    model = train_model(features, labels)
    
    # Save the trained model (optional)
    # model.save('path/to/save/model')

if __name__ == "__main__":
    main()