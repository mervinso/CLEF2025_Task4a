import pandas as pd
import argparse

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path, sep='\t')
    df = df.dropna(subset=['text'])  # basic cleaning: drop rows without text
    df['text_clean'] = df['text'].str.lower()
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    preprocess(args.input, args.output)