import requests
import os

def test_predict_endpoint(csv_file_path: str):
    with open(csv_file_path, 'rb') as f:
        files = {'file': ('data.csv', f, 'multipart/form-data')}
        response = requests.post('http://localhost:8000/predict', files=files)
    
    print(response.json())

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'test.csv')
    test_predict_endpoint(csv_file_path)