import json, codecs
from os import mkdir
from os.path import join, dirname, abspath, exists

from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='F8mkr5wIMV_8vaQN8xoXVyVuPtmGiuU1S_Fwz_zdm0nd',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

## 出力先パスの取得
def getFileName():
    json_folder = join(dirname(abspath('__file__')), 'json_folder/')
    if not exists(json_folder):
        mkdir(json_folder)

    return join(json_folder,'line_history.json')

## 文字列からJSONデータ（ファイル）を取得
def strToJson(str):
    lineHistoryArray = str.split('\n')
    tmpList = []
    for value in lineHistoryArray:
        tmpList.append(dict(content=value,contenttype="text/plain",language='ja'))
    lineHistoryDict = dict(contentItems = tmpList)

    ## JSONファイル出力
    # with codecs.open(getFileName(),'w','utf-8') as fw:
    #     json.dump(lineHistoryDict, fw, ensure_ascii=False, indent=2)

    ## JSON形式で返す
    return json.dumps(lineHistoryDict, ensure_ascii=False)

## 配列からJSONデータ（ファイル）を取得
def arrayToJson(array):
    lineHistoryDict = []
    for oneWeekArray in array:
        weekTmpList = []
        for value in oneWeekArray:
            weekTmpList.append(dict(content=value,contenttype="text/plain",language='ja'))
        allTmpList = dict(contentItems = weekTmpList)
        lineHistoryDict.append(allTmpList)

    lineHistoryDict = dict(lineHistoryDict)

    ## print
    print(json.dumps(lineHistoryDict, indent=2))

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




    getPersonalityInsights(
        """通話ってなると今大丈夫な感じですかね？
        了解です。
        一応大丈夫かもです。
        ありがとうございます。
        一応、うちにiPadと、液晶がバキバキのアンドロイド(動作正常)があるので、複垢ができたら大丈夫かもなんです
        なるほど…
        分かりました。
        分かりました。
        ざっと見てたんですけど、Line Beacon、どうもスマホ間通信の情報が出てこないです。
        そうですね…話にあったアイドルのやつもQiitaにあったんですけど、専用端末使ってるぽいです
        あら…すみません
        いえいえ。
        とりあえず今のところはお疲れ様です！
        おねがいします🙏✨
        おっと…大丈夫ですか？
        そうですねー…ちょっと今は思いつかないですけど…
        その人に合ったアカウントをサジェストする感じですかね？
        今ちょっと同じこと思ってました
        あ、相性ですか
        なるほど、FF内のアカウントとかとの相性ですかね
        あー…
        たしかき
        誤字りました…
        一対一の相性診断ですね
        面白そうです
        そうですね。ちょっとそれで一先ず取り掛かってみたいと思います！
        モチベーション的にはぜひそこまで行きたいですが、詰まり方によるかも知れないです…
        せっかくなのでPythonですかねー。プログラミングの方面だとやっぱり機械学習にも興味があるので。
        ただ、渡辺さんから見てざっとどの言語での前例が多かったとかってありますかね？
        なるほど。
        分かりました！
        通話ってなると今大丈夫な感じですかね？
        了解です。
        一応大丈夫かもです。
        ありがとうございます。
        一応、うちにiPadと、液晶がバキバキのアンドロイド(動作正常)があるので、複垢ができたら大丈夫かもなんです
        なるほど…
        分かりました。
        分かりました。
        ざっと見てたんですけど、Line Beacon、どうもスマホ間通信の情報が出てこないです。
        そうですね…話にあったアイドルのやつもQiitaにあったんですけど、専用端末使ってるぽいです

        あら…すみません
        いえいえ。
        とりあえず今のところはお疲れ様です！
        おねがいします🙏✨
        おっと…大丈夫ですか？
        そうですねー…ちょっと今は思いつかないですけど…
        その人に合ったアカウントをサジェストする感じですかね？
        今ちょっと同じこと思ってました
        あ、相性ですか
        なるほど、FF内のアカウントとかとの相性ですかね
        あー…
        たしかき
        誤字りました…
        一対一の相性診断ですね
        面白そうです
        そうですね。ちょっとそれで一先ず取り掛かってみたいと思います！
        モチベーション的にはぜひそこまで行きたいですが、詰まり方によるかも知れないです…
        せっかくなのでPythonですかねー。プログラミングの方面だとやっぱり機械学習にも興味があるので。
        ただ、渡辺さんから見てざっとどの言語での前例が多かったとかってありますかね？
        なるほど。
        分かりました！
        通話ってなると今大丈夫な感じですかね？
        了解です。
        一応大丈夫かもです。
        ありがとうございます。
        一応、うちにiPadと、液晶がバキバキのアンドロイド(動作正常)があるので、複垢ができたら大丈夫かもなんです
        なるほど…
        分かりました。
        分かりました。
        ざっと見てたんですけど、Line Beacon、どうもスマホ間通信の情報が出てこないです。
        そうですね…話にあったアイドルのやつもQiitaにあったんですけど、専用端末使ってるぽいです

        あら…すみません
        いえいえ。
        とりあえず今のところはお疲れ様です！
        おねがいします🙏✨
        おっと…大丈夫ですか？
        そうですねー…ちょっと今は思いつかないですけど…
        その人に合ったアカウントをサジェストする感じですかね？
        今ちょっと同じこと思ってました
        あ、相性ですか
        なるほど、FF内のアカウントとかとの相性ですかね
        あー…
        たしかき
        誤字りました…
        一対一の相性診断ですね
        面白そうです
        そうですね。ちょっとそれで一先ず取り掛かってみたいと思います！
        モチベーション的にはぜひそこまで行きたいですが、詰まり方によるかも知れないです…
        せっかくなのでPythonですかねー。プログラミングの方面だとやっぱり機械学習にも興味があるので。
        ただ、渡辺さんから見てざっとどの言語での前例が多かったとかってありますかね？
        なるほど。
        分かりました！
        通話ってなると今大丈夫な感じですかね？
        了解です。
        一応大丈夫かもです。
        ありがとうございます。
        一応、うちにiPadと、液晶がバキバキのアンドロイド(動作正常)があるので、複垢ができたら大丈夫かもなんです
        なるほど…
        分かりました。
        分かりました。
        ざっと見てたんですけど、Line Beacon、どうもスマホ間通信の情報が出てこないです。
        そうですね…話にあったアイドルのやつもQiitaにあったんですけど、専用端末使ってるぽいです

        あら…すみません
        いえいえ。
        とりあえず今のところはお疲れ様です！
        おねがいします🙏✨
        おっと…大丈夫ですか？
        そうですねー…ちょっと今は思いつかないですけど…
        その人に合ったアカウントをサジェストする感じですかね？
        今ちょっと同じこと思ってました
        あ、相性ですか
        なるほど、FF内のアカウントとかとの相性ですかね
        あー…
        たしかき
        誤字りました…
        一対一の相性診断ですね
        面白そうです
        そうですね。ちょっとそれで一先ず取り掛かってみたいと思います！
        モチベーション的にはぜひそこまで行きたいですが、詰まり方によるかも知れないです…
        せっかくなのでPythonですかねー。プログラミングの方面だとやっぱり機械学習にも興味があるので。
        ただ、渡辺さんから見てざっとどの言語での前例が多かったとかってありますかね？
        なるほど。
        分かりました！"""
    )