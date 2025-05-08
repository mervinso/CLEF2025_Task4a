import pandas as pd
import pickle
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

def train(input_path, model_path):
    df = pd.read_csv(input_path)
    X = TfidfVectorizer(max_features=5000).fit_transform(df['text_clean'])
    y = df.iloc[:, 2:]  # assumes labels start from third column
    model = MultiOutputClassifier(LogisticRegression(max_iter=1000))
    model.fit(X, y)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    train(args.input, args.model)