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
