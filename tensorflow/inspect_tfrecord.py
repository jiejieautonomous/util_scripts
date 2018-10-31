import tensorflow as tf
import argparse
"""
usage example:
python inspect_tfrecord.py
/Users/jjacquot/traffic_signal_sf_av/tfrecords/train_001.tfrecord
feature, e.g. image/shape
"""
parser = argparse.ArgumentParser(description='filename')
parser.add_argument('--filename', type=str, help='name of file to inspect')
parser.add_argument('--feature', type=str, help='feature to return')
args = parser.parse_args()

for example in tf.python_io.tf_record_iterator(args.filename):
    result = tf.train.Example.FromString(example)
    print(result.features.feature[args.feature])
