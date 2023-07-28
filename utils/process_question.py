from sentence_transformers import SentenceTransformer,util
import typing
import re
import pickle

embedding_model = pickle.load(open('models/embeded_model.pkl','rb'))
class ProcessQuestion:


    def question_process(self,question):
        clean_question = re.sub('[0-9:{|}~@[\\]/#$%&\'()*+╯╭]'," ",question)
        embed_question = embedding_model.encode(clean_question)
        return embed_question
