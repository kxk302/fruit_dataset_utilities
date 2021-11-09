import argparse

import numpy as np
import pandas as pd

names = ['Label_unmapped', 'Label_name', 'File_name']
label_mapping = {
  8: 0,
  9: 1,
  78: 2,
  101: 3,
  109: 4,
  110: 5,
  116: 6,
  119: 7,
  124: 8,
  129: 9,
}

def map_input(input, output):
  df_in = pd.read_csv(input, sep="\t", names=names) 
  print(df_in.Label_unmapped.value_counts())
  df_in['Label'] = df_in.Label_unmapped.map(label_mapping) 
  print(label_mapping)
  print(df_in.Label.value_counts())
  df_out = df_in.drop(columns=['Label_unmapped'])
  df_out.to_csv(output, sep="\t", index=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', help='Input file', required=True)
  parser.add_argument('-o', '--output', help='Output file', required=True)
  args = parser.parse_args()
  map_input(args.input, args.output)
