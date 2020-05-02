import sys
import os
import pickle
import re
import pandas as pd

sys.path.append(os.path.join('src'))
from utils import remove_special_char

def retrieve_tokens(text, df):
    main_tokens = []
    for token in df['tokens']:
        if token in text:
            token = remove_special_char(token)
            main_tokens.append(token)
    return main_tokens

def build_vis_table(topic_id, renamed_id, df, model, docs, person_doc):
    topic_tokens = model.print_topics(-1, num_words=20)[topic_id]
    
    tokens = []
    scores = []
    for i in topic_tokens[1].split('+'):
        token = re.sub('.*\*"(.*)".*', r'\1', i)
        score = re.sub(' *(.*)\*.*', r'\1', i)
        score = float(score)
        tokens.append(token)
        scores.append(score)
    token_score_dict = {'tokens': tokens, 'scores': scores}
    token_score = pd.DataFrame(token_score_dict)
    
    docs['tokens'] = docs['body'].apply(lambda text: retrieve_tokens(text, token_score))
    
    #filter by topic
    df = df.loc[df['topic_id'] == topic_id].sort_values(by=['topic_score'], ascending=False)
    df = df.head(20)
    
    ### merge topics and tokens
    df = pd.merge(df, docs, on='doc_id', how='inner')
    
    ### relate docs to list of persons
    #filters person_doc
    array = list(df['doc_id'])
    person_doc_filtered = person_doc.loc[person_doc['doc_id'].isin(array)]
    
    #apply list of persons
    person_doc_filtered = person_doc_filtered.groupby(['doc_id'])['name'].apply(list)
    person_doc_filtered = pd.DataFrame({'doc_id':person_doc_filtered.index, 'names':person_doc_filtered.values})
    
    #merge topics and persons
    df = pd.merge(df, person_doc_filtered, on='doc_id', how='outer')
    df = df.astype({'names': 'object'})
    for row in df.loc[df.names.isnull(), 'names'].index:
        df.at[row, 'names'] = []
    df['topic_id'] = renamed_id
    
    return df

def get_melted_df(df,variable):
    cols_to_drop = set(df.columns) - set(['doc_id'])
    topic = df[variable].apply(pd.Series) \
        .merge(df, left_index = True, right_index = True) \
        .drop(cols_to_drop, axis = 1) \
        .melt(id_vars = ['doc_id'], value_name = variable) \
        .drop("variable", axis = 1) \
        .dropna()
    return topic
