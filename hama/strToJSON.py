import collections as cl
import json
import pprint
from os import mkdir, remove
from os.path import join, dirname, abspath, exists



#line_history.json

def getFileName():
    json_folder = join(dirname(abspath('__file__')), 'json_folder/')
    if not exists(json_folder):
        mkdir(json_folder)

    return join(json_folder,'line_history.json')

def strToJson(str):
    lineHistoryArray = str.split('\n')
    lineHistoryDict = dict(text = lineHistoryArray)

    with open(getFileName(),'w') as fw:
        json.dump(lineHistoryDict, fw, indent=2)

if __name__ == '__main__':
    strToJson('sakufhdsfu\noisjdoisj\niusdhius')
