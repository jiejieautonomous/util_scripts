#!/usr/bin/env python2
"""Script to inspect checkpoint.
Usage: inspect_checkpoint list ckpt_filename
"""


import tensorflow as tf
import os
import argparse
import numpy as np
import pprint as pp
from functools import reduce
from signal import signal, SIGPIPE, SIG_DFL


def command_list(args):
    reader = tf.train.NewCheckpointReader(args.input_file[0])
    shape_map = reader.get_variable_to_shape_map()
    varnames = sorted(shape_map.keys())
    for var_name in varnames:
        output = var_name
        num_elements = 1
        if shape_map[var_name]:
            num_elements = reduce(lambda x, y: x * y, shape_map[var_name])
        x = None

        if args.shapes:
            output += " " + str(shape_map[var_name])
        if args.elements:
            output += " " + str(num_elements)
        if args.bytes:
            x = x or reader.get_tensor(var_name)
            output += " " + str(x.nbytes)
        print(output)


def command_print(args):
    reader = tf.train.NewCheckpointReader(args.input_file[0])
    x = reader.get_tensor(args.tensor_name[0])
    np.set_printoptions(threshold=np.nan, suppress=False)
    np.set_printoptions(linewidth=args.line_width,)
    pp.pprint(x)


def main():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    # set default handler to no-op
    signal(SIGPIPE, SIG_DFL)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands', dest='action')
    # List
    sub = subparsers.add_parser('list', help="""
      List all the tensors in a checkpoint file.
    """)
    sub.add_argument("--shapes", action='store_true', default=True, help="display tensor shape")
    sub.add_argument("--elements", action='store_true', default=False,
                     help="display total number of elements in tensor")
    sub.add_argument("--bytes", action='store_true', default=False, help="display tensor sizes in bytes")
    sub.add_argument("input_file", nargs=1, help="input checkpoint file")
    sub.set_defaults(func=command_list)
    # Print
    sub = subparsers.add_parser('print', help="""
      Print a tensor.
    """)
    sub.add_argument("input_file", nargs=1, help="input checkpoint file")
    sub.add_argument("tensor_name", nargs=1, help="tensor name")
    sub.add_argument("--line_width", action='store', default=200, type=int, help="maximum line length")
    sub.set_defaults(func=command_print)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
