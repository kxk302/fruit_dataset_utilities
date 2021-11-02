import argparse
import json
import pandas as pd

def feature_vector_subset(feature_vector_file, subset_label_map_file, new_feature_vector_file):
  with open(subset_label_map_file, 'r') as f:
    subset_label_map = json.load(f)
    labels = subset_label_map.values()
    df = pd.read_csv(feature_vector_file, sep='\t')
    df = df[df.iloc[:, 30000].isin(labels)]
    df.to_csv(new_feature_vector_file, sep="\t", index=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('-f', '--feature_vector_file', help='Feature vector file', required=True)
  parser.add_argument('-s', '--subset_label_map_file', help='Subset of fruit labels to keep', required=True)
  parser.add_argument('-o', '--new_feature_vector_file', help='New feature vector file', required=True)

  args = parser.parse_args()
  feature_vector_subset(args.feature_vector_file, args.subset_label_map_file, args.new_feature_vector_file)
  
  

