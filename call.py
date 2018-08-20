# coding:utf-8
from pykakasi import kakasi
import MeCab
import morse


def convert(pic):
    pic = ''.join(pic.split())  # 空白の削除

    # MeCabによる形態素解析
    try:
        m = MeCab.Tagger("-Owakati")
        pic = m.parse(pic)
        pic = pic.strip()  # 先頭と末尾の空白を削除
        pic = pic.replace(' ', '_')  # 単語間に開けた空白を変換
    except RuntimeError:
        pic = ""

    # pykakasiによるカタカナ・漢字のひらがなへの変換
    k = kakasi()
    k.setMode("K", "H")  # カタカナをひらがなに
    k.setMode("J", "H")  # 漢字をひらがなに
    conv = k.getConverter()
    pic = conv.do(pic)

    context = ""
    for c in pic:
        context += c + "~"
    context.strip()

    ans = ""
    for c in context:
        ans += morse.s2m(c)

    return ans
    # Javaのファイルで文字列をモールス信号に変換
    # cmd = 'java morseRet ' + pic
    # process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
    #                            shell=True).communicate()[0]

    # def res_cmd(cmd):
    #     return process

    # str = res_cmd(cmd).decode('utf-8')
    # for num in range(len(str)):

    #     if str[num] == '.':
    #         print('とん')
    #         # print('処理A')  1拍点灯
    #     if str[num] == '-':
    #         print('つー')
    #         # print('処理B')  3拍点灯
    #     if str[num] == '~':
    #         print('スペース')
    #         # print('処理C')  　3拍消灯
    #     if str[num] == '_':
    #         print('アンダースコア')
    #     # print('処理D')  7拍消灯
    #     # ７拍点灯だがスペース時の3拍に挟まれるため1拍消灯で3+1+3で7拍消灯となる
