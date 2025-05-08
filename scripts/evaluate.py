import pandas as pd
import pickle
import argparse
from sklearn.metrics import classification_report

def evaluate(model_path, test_path, output_path):
    df = pd.read_csv(test_path, sep='\t')
    X_test = df['text'].str.lower()
    y_true = df.iloc[:, 2:]

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    X_test_vec = model.estimators_[0].named_steps['tfidfvectorizer'].transform(X_test)
    y_pred = model.predict(X_test_vec)

    report = classification_report(y_true, y_pred, output_dict=True)
    pd.DataFrame(report).to_json(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--test", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    evaluate(args.model, args.test, args.output)