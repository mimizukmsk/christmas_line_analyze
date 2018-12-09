import json, codecs
from os import mkdir
from os.path import join, dirname, abspath, exists

from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    version='{version}',
    iam_apikey='{iam_apikey}',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

## 出力先パスの取得
def getFileName():
    json_folder = join(dirname(abspath('__file__')), 'json_folder/')
    if not exists(json_folder):
        mkdir(json_folder)

    return join(json_folder,'line_history.json')

## JSONファイルの取得
def strToJson(str):
    lineHistoryArray = str.split('\n')
    tmpList = []
    for value in lineHistoryArray:
        tmpList.append(dict(content=value,contenttype="text/plain",language='ja'))
    lineHistoryDict = dict(contentItems = tmpList)

    ## JSONファイル出力
    with codecs.open(getFileName(),'w','utf-8') as fw:
        json.dump(lineHistoryDict, fw, ensure_ascii=False, indent=2)

    ## JSON形式で返す
    return json.dumps(lineHistoryDict, ensure_ascii=False)

## 文字列(str)から性格情報(JSON)を取得
def getPersonalityInsights(str):

    ## JSONファイルを認識
    #with open(join(dirname(__file__), './json_folder/line_history.json')) as profile_json:
    #     profile = personality_insights.profile(
    #         profile_json.read(),
    #         content_type='application/json',
    #         consumption_preferences=True,
    #         raw_scores=True
    #     ).get_result()

    ## JSONデータを認識
    profile = personality_insights.profile(
        strToJson(str),
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()

    print(json.dumps(profile, indent=2))

    return json.dumps(profile, indent=2)

## main関数
if __name__ == '__main__':
    printPersonality_insights("""Anaconda - Red Hat Linux, Fedora LinuxのGUIインストーラ
Anki - 出題頻度を自動調整する暗記カードソフトウェア
Bazaar - オープンソースの分散型バージョン管理システム
Anaconda - Red Hat Linux, Fedora LinuxのGUIインストーラ
Anki - 出題頻度を自動調整する暗記カードソフトウェア
Bazaar - オープンソースの分散型バージョン管理システム""")
