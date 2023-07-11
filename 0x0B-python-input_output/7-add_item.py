#!/usr/bin/python3
'''this module reads from commandline and saves i json fiile'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


number_arg = len(sys.argv)

newlist = load_from_json_file('add_item.json')

# create a newlist
for x in range(1, number_arg):
    newlist.append(sys.argv[x])

# save to the json file
save_to_json_file(newlist, 'add_item.json')
# load from the json file
