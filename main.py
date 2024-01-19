from flask import Flask
import pickle
import warnings
from urllib.parse import unquote_plus
import requests
warnings.filterwarnings('ignore')

class Model:
    def __init__(self):
        self.model = pickle.load(open('SpamURL_Classifier.pkl', 'rb'))
        self.vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

    def predict(self, url):
        try:
            if not url.startswith("https://") and not url.startswith("http://"):
                url = "https://" + url
            final_url = self.get_final_url(url)
            x = self.vectorizer.transform([final_url])
            if self.model.predict(x)[0]:
                return 'Spam', final_url
            else:
                return 'Not Spam', final_url
        except Exception as e:
            return e

    @staticmethod
    def get_final_url(url):
        response = requests.head(url, allow_redirects=True)
        return response.url

app = Flask(__name__)

@app.route('/predict/<path:encoded_url>')
def predict(encoded_url):
    url = unquote_plus(encoded_url)
    model = Model()
    prediction = model.predict(url)
    return str(prediction)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
