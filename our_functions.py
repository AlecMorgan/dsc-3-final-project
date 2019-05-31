# Build our own library!

def display_acc_and_f1_score(true, preds, model_name):
    acc = accuracy_score(true, preds)
    f1 = f1_score(true, preds)
    print("Model: {}".format(model_name))
    print("Accuracy: {}".format(acc))
    print("F1-Score: {}".format(f1))
    
    
performance_list = []  
    def score_keeper(model_name, model_score, score_note=none):
        score_model = ['model type: ': model_name]
        score_note = ['score notes: ': score_note]
    if not any(d['model_name'] == 'model_type' for d in performance_list):
        performance_list.append(score_model)
    