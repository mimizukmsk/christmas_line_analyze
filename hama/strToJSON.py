import json, codecs
from os import mkdir
from os.path import join, dirname, abspath, exists

#出力先パスの取得
def getFileName():
    json_folder = join(dirname(abspath('__file__')), 'json_folder/')
    if not exists(json_folder):
        mkdir(json_folder)

    return join(json_folder,'line_history.json')

#JSONファイルの取得
def strToJson(str):
    lineHistoryArray = str.split('\n')
    lineHistoryDict = dict(text = lineHistoryArray)

    ## JSONファイル出力
    # with codecs.open(getFileName(),'w','utf-8') as fw:
    #     json.dump(lineHistoryDict, fw, ensure_ascii=False, indent=2)

    ## JSON形式で返す
    return json.dumps(lineHistoryDict, ensure_ascii=False)

#main関数
if __name__ == '__main__':
    print(strToJson('こんにちは\n今日は\nコンニチ\nさs\noasidhias\n12334'))
