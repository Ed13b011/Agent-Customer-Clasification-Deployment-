# Importing essential libraries
from flask import Flask, render_template, request
import pickle

# Load the model and CountVectorizer object
filename = 'agent_cust_ivr_svc_model.pkl'
classifier = pickle.load(open('agent_cust_ivr_svc_model.pkl', 'rb', 3))
cv = pickle.load(open('count_vectorizer.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
        '''
        For rendering results on GUI
        '''

        if request.method == 'POST':
                input_text = request.form['text']
                data = [input_text]
                vect = cv.transform(data).toarray()
                my_prediction = classifier.predict(vect)
                return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
	app.run(debug=True)
