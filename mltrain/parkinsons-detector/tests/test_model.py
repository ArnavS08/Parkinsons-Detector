import unittest
from src.models.model import ParkinsonsModel

class TestParkinsonsModel(unittest.TestCase):

    def setUp(self):
        self.model = ParkinsonsModel()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model)

    def test_model_prediction_shape(self):
        sample_input = [[0.1, 0.2, 0.3, 0.4]]  # Example input shape
        prediction = self.model.predict(sample_input)
        self.assertEqual(prediction.shape, (1,))  # Expecting a single prediction

    def test_model_training(self):
        X_train = [[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]]  # Example training data
        y_train = [0, 1]  # Example labels
        self.model.train(X_train, y_train)
        self.assertTrue(hasattr(self.model, 'trained_model'))  # Check if model is trained

if __name__ == '__main__':
    unittest.main()