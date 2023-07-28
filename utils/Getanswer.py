from sentence_transformers import util
# from utils.process_question import ProcessQuestion
import pandas as pd
import numpy as np
import os
import re
import pickle

embeded_par = pickle.load(open('models/embeded_par.pkl','rb'))
embedding_model = pickle.load(open('models/embeded_model.pkl','rb'))
clean_text_list = pickle.load(open('models/clean_text.pkl','rb'))


class GetAnswer:


    def Getans(self,embeded_par , embaded_question):
        search_score = []
        for i in range(len(embeded_par)):
            score = util.semantic_search(embeded_par[i],embaded_question)[0][0]['score']
            search_score.append(score)
        answer = clean_text_list[pd.DataFrame({'simlarity_score':search_score}).sort_values(['simlarity_score'] , ascending=False).index[0]]
        return answer

