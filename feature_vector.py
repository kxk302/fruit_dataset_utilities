import argparse
import cv2
import json
import os
import sys

from pathlib import Path

def create_label_map(directory, label_map_file):
  # Return if the label map file already exists
  if Path(label_map_file).is_file():
    return 
  # Otherwise, create the label map file
  else:
    label_map = {}
    with open(label_map_file, 'w') as f1:
      p = Path(directory)
      subdirs = [x for x in p.iterdir() if x.is_dir()]
      for idx, subdir in enumerate(subdirs):
        print("str(subdir): {}, idx: {}".format(str(os.path.basename(subdir)), idx))
        label_map[str(os.path.basename(subdir))] = idx
      json.dump(label_map, f1) 

def create_feature_vectors(directory, feature_vector_file, label_map_file):
  with open(feature_vector_file, 'w') as f1, open(label_map_file, 'r') as f2:
    label_map = json.load(f2)
    p = Path(directory)
    subdirs = [x for x in p.iterdir() if x.is_dir()]
    for subdir in subdirs:
      p = Path(subdir)
      subdir_files = [x for x in p.iterdir() if not x.is_dir()]

      for subdir_file in subdir_files:
        print(subdir_file)
        im = cv2.imread(str(subdir_file))
        im = im.reshape(im.shape[0] * im.shape[1] * im.shape[2])
        im = im.tolist()
        f1.write('\t'.join(map(str, im)) + '\t' + str(label_map[str(os.path.basename(subdir))]) + '\t' + 
                 str(os.path.basename(subdir)) + '\t' +  str(subdir_file) + '\n')

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--directory', help='Directory for train/test image files', required=True)
  parser.add_argument('-f', '--feature_vector_file', help='Feature vector file', required=True)
  parser.add_argument('-l', '--label_map_file', help='Numeric to string mapping of fruit labels', required=True)
  args = parser.parse_args()
  create_label_map(args.directory, args.label_map_file)
  create_feature_vectors(args.directory, args.feature_vector_file, args.label_map_file)
