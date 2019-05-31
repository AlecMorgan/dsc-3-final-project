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


def score(model, X_test):
    model.predict_proba(X_test)