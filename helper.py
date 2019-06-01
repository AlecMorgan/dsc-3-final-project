from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import numpy as np


def get_preds(model, X, clf_thres=.5):
    """Performs binary classification based on the chosen probability/confidence level
    (clf_thres). For example, clf_thres=.9 means the model will predict category 1 only
    if it is at least 90% confident, else category 2."""
    y_pred = model.predict_proba(X)
    return np.array([0 if y[0] >= clf_thres else 1 for y in y_pred])


def score_model(y_true, y_pred, round_to=4, output='print'):
    """Scores a binary classification model in accuracy, precision, f1, and recall."""
    scores = {
        'accuracy': np.round(accuracy_score(y_true, y_pred), round_to),
        'precision': np.round(precision_score(y_true, y_pred), round_to),
        'f1': np.round(f1_score(y_true, y_pred), round_to),
        'recall': np.round(recall_score(y_true, y_pred), round_to)
    }
    
    if output == 'print':
        for score_name, score_val in scores.items():
            print(f'{score_name.title()}: {score_val}')
    elif output == 'dict':
        return scores
        
        
#give us a running list of model performances with room for notes
def score_keeper(model_name, model_score, performance_list, score_note=None):
    #score_model = ['model type'] = model_name
    #score_note = ['score notes'] = score_note
    if not any(d['model_name'] == 'model_type' for d in performance_list):
        performance_list.append(score_model)
    
    
def human_readify(df):
    map_ = [
        ('annotate', 'anotate_codes.csv'),
        ('commod', 'commodity_codes.csv'),
        ('commtype', 'commod_type_codes.csv'),
        ('lab', 'lab_codes.csv'), 
        ('pestcode', 'pest_codes.csv'),
        ('testclass', 'test_class_codes.csv'), 
        ('confmethod', 'confmethod_codes.csv'),
        ('mean', 'mean_codes.csv'),
        ('extract', 'extract_codes.csv'),
        ('determin', 'determin_codes.csv')
    ]
    for col, csv in map_:
        with open(f'data/{csv}') as f:
            for row in f:
                row = row.split(',')
                df[col].replace(row[0], row[1])
                
    return df