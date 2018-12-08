import collections as cl
import json
import pprint

def strToJson(str):
    textArray = str.split('\n')
    # jsonBof = '{"text":'
    # jsonComma = ', "text":'
    # jsonEof = '}'


    jsonFile = None

    # count = 1
    # for text in textArray
    #     jsonFile += text
    #
    #     if len(textArray) > count
    #         jsonFile += jsonComma
    #     else:
    #         jsonFile += jsonEof
    #
    #     count += 1

    # for i in range(len(textArray)):
    #     jsonFile += textArray[i]
    #
    #     if len(textArray) > i+1:
    #         jsonFile += jsonComma
    #     else:
    #         jsonFile += jsonEof
    #
    # print(json.dumps(jsonFile))

    jsonFile = dict(text = textArray)

    print(json.dumps(jsonFile))

    return json.dumps(jsonFile)

if __name__ == '__main__':
    json = strToJson('sakufhdsfu\noisjdoisj\niusdhius')


    # dic = json.load(json)
    # pprint.pprint(dic, width=40)
