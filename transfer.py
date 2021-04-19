#!/usr/bin/env python

import requests
import argparse

print('here')

parser = argparse.ArgumentParser(
    description='Transfer ReadsPerGene.out.tab files generated by STAR to DMAC Olympus server.'
)

parser.add_argument('--file',
                       type=str,
                       help='the file to transfer')

parser.add_argument('--path',
                       type=str,
                       help='the destination folder')

parser.add_argument('--rename',
                       type=str,
                       help='descriptive name for file')

parser.add_argument('--token',
                       type=str,
                       help='POST url endpoint')


args = parser.parse_args()
print(args)

data = {
    'rename': args.rename,
    'path': args.path,
    'token': args.token
}

with open(args.file, "rb") as a_file:
    file_dict = {args.rename: a_file}
    response = requests.post('https://b5143783ea53.ngrok.io/api/file-transfer/', files=file_dict, data=data)
    print(str(response.text))