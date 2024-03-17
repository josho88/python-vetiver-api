from vetiver.server import predict, vetiver_endpoint
import pandas as pd
import unittest

class TestVetiverModelEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8080/predict"

    def test_single_prediction(self):
        endpoint = vetiver_endpoint(self.base_url)
        new_dict = {"cyl": [4], "disp": [200], 
                    "hp": [100], "drat": [3],
                    "wt": [3], "qsec": [17], 
                    "vs": [0], "am": [1],
                    "gear": [4], "carb": [2]}
        new_data = pd.DataFrame(new_dict)
        preds = predict(endpoint, new_data)
        self.assertIsNotNone(preds)  # Ensure predictions are not None
        self.assertEqual(len(preds), 1)  # Ensure only one prediction is returned
        self.assertTrue(isinstance(preds.iloc[0, 0], (int, float)))  # Ensure prediction is numeric
        self.assertTrue(preds.iloc[0, 0] >= 0)  # Ensure prediction is positive

    def test_missing_inputs(self):
            endpoint = vetiver_endpoint(self.base_url)
            # Creating a DataFrame with missing inputs
            new_dict = {"cyl": [4], "hp": [100], "drat": [3],
                        "wt": [3], "qsec": [17], "vs": [0],
                        "am": [1], "gear": [4], "carb": [2]}
            new_data = pd.DataFrame(new_dict)
            # Expecting a prediction even with missing inputs
            preds = predict(endpoint, new_data)
            self.assertIsNotNone(preds)  # Ensure predictions are not None
            self.assertEqual(len(preds), 1)  # Ensure only one prediction is returned
            self.assertTrue(isinstance(preds.iloc[0, 0], (int, float)))  # Ensure prediction is numeric
            self.assertTrue(preds.iloc[0, 0] >= 0)  # Ensure prediction is positive

if __name__ == '__main__':
    unittest.main()
