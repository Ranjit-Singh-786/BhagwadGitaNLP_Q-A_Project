from flask import Flask,render_template,jsonify,url_for,request
import pickle
from utils.process_question import ProcessQuestion
from utils.Getanswer import GetAnswer
app = Flask(__name__)

obj = ProcessQuestion()
obj2 = GetAnswer()

embeded_par = pickle.load(open('models/embeded_par.pkl','rb'))
embedding_model = pickle.load(open('models/embeded_model.pkl','rb'))
clean_text_list = pickle.load(open('models/clean_text.pkl','rb'))


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/answer', methods=['GET','POST'])
def answer():
    if request.method=='POST':
        question = request.form['question']
        processed_embedded_question = obj.question_process(question=question)
        answer = obj2.Getans(embeded_par=embeded_par,embaded_question=processed_embedded_question)
        output = answer
    return render_template('index.html' , answerr = output , question = question)


if __name__=="__main__":
    app.run(debug=True)