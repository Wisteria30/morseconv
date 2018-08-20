# coding:utf-8

def s2m(c):
    # 欧文
    if (c == 'a' or c == 'A'):
        return "・－"
    if (c == 'b' or c == 'B'):
        return "－・・・"
    if (c == 'c' or c == 'C'):
        return "－・－・"
    if (c == 'd' or c == 'D'):
        return "－・・"
    if (c == 'e' or c == 'E'):
        return "・"
    if (c == 'f' or c == 'F'):
        return "・・－・"
    if (c == 'g' or c == 'G'):
        return "－－・"
    if (c == 'h' or c == 'H'):
        return "・・・・"
    if (c == 'i' or c == 'I'):
        return "・・"
    if (c == 'j' or c == 'J'):
        return "・－－－"
    if (c == 'k' or c == 'K'):
        return "－・－"
    if (c == 'l' or c == 'L'):
        return "・－・・"
    if (c == 'm' or c == 'M'):
        return "－－"
    if (c == 'n' or c == 'N'):
        return "－・"
    if (c == 'o' or c == 'O'):
        return "－－－"
    if (c == 'p' or c == 'P'):
        return "・－－・"
    if (c == 'q' or c == 'Q'):
        return "－－・－"
    if (c == 'r' or c == 'R'):
        return "・－・"
    if (c == 's' or c == 'S'):
        return "・・・"
    if (c == 't' or c == 'T'):
        return "－"
    if (c == 'u' or c == 'U'):
        return "・・－"
    if (c == 'v' or c == 'V'):
        return "・・・－"
    if (c == 'w' or c == 'W'):
        return "・－－"
    if (c == 'x' or c == 'X'):
        return "－・・－"
    if (c == 'y' or c == 'Y'):
        return "－・－－"
    if (c == 'z' or c == 'Z'):
        return "－－・・"

    # 欧文記号
    if (c == ','):
        return "－－・・－－"
    if (c == '.'):
        return "・－・－・－"
    if (c == '?'):
        return "・・－－・・"

    # ひらがな
    if (c == 'あ' or c == 'ぁ'):
        return "－－・－－"
    if (c == 'い' or c == 'ぃ'):
        return "・－"
    if (c == 'う' or c == 'ぅ'):
        return "・・－"
    if (c == 'え' or c == 'ぇ'):
        return "－・－－－"
    if (c == 'お' or c == 'ぉ'):
        return "・－・・・"
    if (c == 'か' or c == 'が'):
        if (c == 'が'):
            return "・－・・　・・"
        return "・－・・"
    if (c == 'き' or c == 'ぎ'):
        if (c == 'ぎ'):
            return "－・－・・　・・"
        return "－・－・・"
    if (c == 'く' or c == 'ぐ'):
        if (c == 'ぐ'):
            return "・・・－　・・"
        return "・・・－"
    if (c == 'け' or c == 'げ'):
        if (c == 'げ'):
            return "－・－－　・・"
        return "－・－－"
    if (c == 'こ' or c == 'ご'):
        if (c == 'ご'):
            return "－－－－　・・"
        return "－－－－"
    if (c == 'さ' or c == 'ざ'):
        if (c == 'ざ'):
            return "－・－・－　・・"
        return "－・－・－"
    if (c == 'し' or c == 'じ'):
        if (c == 'じ'):
            return "－－・－・　・・"
        return "－－・－・"
    if (c == 'す' or c == 'ず'):
        if (c == 'ず'):
            return "－－－・－　・・"
        return "－－－・－"
    if (c == 'せ' or c == 'ぜ'):
        if (c == 'ぜ'):
            return "・－－－・　・・"
        return "・－－－・"
    if (c == 'そ' or c == 'ぞ'):
        if (c == 'ぞ'):
            return "－－－・　・・"
        return "－－－・"
    if (c == 'た' or c == 'だ'):
        if (c == 'だ'):
            return "－・　・・"
        return "－・"
    if (c == 'ち' or c == 'ぢ'):
        if (c == 'ぢ'):
            return "・・－・　・・"
        return "・・－・"
    if (c == 'つ' or c == 'づ' or c == 'っ'):
        if (c == 'づ'):
            return "・－－・　・・"
        return "・－－・"
    if (c == 'て' or c == 'で'):
        if (c == 'で'):
            return "・－・－－　・・"
        return "・－・－－"
    if (c == 'と' or c == 'ど'):
        if (c == 'ど'):
            return "・・－・・　・・"
        return "・・－・・"
    if (c == 'な'):
        return "・－・"
    if (c == 'に'):
        return "－・－・"
    if (c == 'ぬ'):
        return "・・・・"
    if (c == 'ね'):
        return "－－・－"
    if (c == 'の'):
        return "・・－－"
    if (c == 'は' or c == 'ば' or c == 'ぱ'):
        if (c == 'ば'):
            return "－・・・　・・"
        if (c == 'ぱ'):
            return "－・・・　・・－－・"
        return "－・・・"
    if (c == 'ひ' or c == 'び' or c == 'ぴ'):
        if (c == 'び'):
            return "－－・・－　・・"
        if (c == 'ぴ'):
            return "－－・・－　・・－－・"
        return "－－・・－"
    if (c == 'ふ' or c == 'ぶ' or c == 'ぷ'):
        if (c == 'ぶ'):
            return "－－・・　・・"
        if (c == 'ぷ'):
            return "－－・・　・・－－・"
        return "－－・・"
    if (c == 'へ' or c == 'べ' or c == 'ぺ'):
        if (c == 'べ'):
            return "・　・・"
        if (c == 'ぺ'):
            return "・　・・－－・"
        return "・"
    if (c == 'ほ' or c == 'ぼ' or c == 'ぽ'):
        if (c == 'ぼ'):
            return "－・・　・・"
        if (c == 'ぽ'):
            return "－・・　・・－－・"
        return "－・・"
    if (c == 'ま'):
        return "－・・－"
    if (c == 'み'):
        return "・・－・－"
    if (c == 'む'):
        return "－"
    if (c == 'め'):
        return "－・・・－"
    if (c == 'も'):
        return "－・・－・"
    if (c == 'や' or c == 'ゃ'):
        return "・－－"
    if (c == 'ゆ' or c == 'ゅ'):
        return "－・・－－"
    if (c == 'よ' or c == 'ょ'):
        return "－－"
    if (c == 'ら'):
        return "・・・"
    if (c == 'り'):
        return "－－・"
    if (c == 'る'):
        return "－・－－・"
    if (c == 'れ'):
        return "－－－"
    if (c == 'ろ'):
        return "・－・－"
    if (c == 'わ' or c == 'ゎ'):
        return "－・－"
    if (c == 'ゐ'):
        return "・－・・－"
    if (c == 'ゑ'):
        return "・－－・・"
    if (c == 'を'):
        return "・－－－"    
    if (c == 'ん'):
        return "・－・－・"
  
    # カタカナ
    if (c == 'ア' or c == 'ァ'
            or c == 'ｱ' or c == 'ｧ'):
        return "－－・－－"
    if (c == 'イ' or c == 'ィ'
            or c == 'ｲ' or c == 'ｨ'):
        return "・－"
    if (c == 'ウ' or c == 'ゥ'
            or c == 'ｳ' or c == 'ｩ'):
        return "・・－"
    if (c == 'エ' or c == 'ェ'
            or c == 'ｴ' or c == 'ｪ'):
        return "－・－－－"
    if (c == 'オ' or c == 'ォ'
            or c == 'ｵ' or c == 'ｫ'):
        return "・－・・・"
    if (c == 'カ' or c == 'ガ' or c == 'ｶ'):
        if (c == 'ガ'):
            return "・－・・　・・"
        return "・－・・"
    if (c == 'キ' or c == 'ギ' or c == 'ｷ'):
        if (c == 'ギ'):
            return "－・－・・　・・"
        return "－・－・・"
    if (c == 'ク' or c == 'グ' or c == 'ｸ'):
        if (c == 'グ'):
            return "・・・－　・・"
        return "・・・－"
    if (c == 'ケ' or c == 'ゲ' or c == 'ｹ'):
        if (c == 'ゲ'):
            return "－・－－　・・"
        return "－・－－"
    if (c == 'コ' or c == 'ゴ' or c == 'ｺ'):
        if (c == 'ゴ'):
            return "－－－－　・・"
        return "－－－－"
    if (c == 'サ' or c == 'ザ' or c == 'ｻ'):
        if (c == 'ザ'):
            return "－・－・－　・・"
        return "－・－・－"
    if (c == 'シ' or c == 'ジ' or c == 'ｼ'):
        if (c == 'ジ'):
            return "－－・－・　・・"
        return "－－・－・"
    if (c == 'ス' or c == 'ズ' or c == 'ｽ'):
        if (c == 'ズ'):
            return "－－－・－　・・"
        return "－－－・－"
    if (c == 'セ' or c == 'ゼ' or c == 'ｾ'):
        if (c == 'ゼ'):
            return "・－－－・　・・"
        return "・－－－・"
    if (c == 'ソ' or c == 'ゾ' or c == 'ｿ'):
        if (c == 'ゾ'):
            return "－－－・　・・"
        return "－－－・"
    if (c == 'タ' or c == 'ダ' or c == 'ﾀ'):
        if (c == 'ダ'):
            return "－・　・・"
        return "－・"
    if (c == 'チ' or c == 'ヂ' or c == 'ﾁ'):
        if (c == 'ヂ'):
            return "・・－・　・・"
        return "・・－・"
    if (c == 'ツ' or c == 'ヅ' or c == 'ッ'
            or c == 'ﾂ' or c == 'ｯ'):
        if (c == 'ヅ'):
            return "・－－・　・・"
        return "・－－・"
    if (c == 'テ' or c == 'デ' or c == 'ﾃ'):
        if (c == 'デ'):
            return "・－・－－　・・"
        return "・－・－－"
    if (c == 'ト' or c == 'ド' or c == 'ﾄ'):
        if (c == 'ド'):
            return "・・－・・　・・"
        return "・・－・・"
    if (c == 'ナ' or c == 'ﾅ'):
        return "・－・"
    if (c == 'ニ' or c == 'ﾆ'):
        return "－・－・"
    if (c == 'ヌ' or c == 'ﾇ'):
        return "・・・・"
    if (c == 'ネ' or c == 'ﾈ'):
        return "－－・－"
    if (c == 'ノ' or c == 'ﾉ'):
        return "・・－－"
    if (c == 'ハ' or c == 'バ' or c == 'パ'
            or c == 'ﾊ'):
        if (c == 'バ'):
            return "－・・・　・・"
        if (c == 'パ'):
            return "－・・・　・・－－・"
        return "－・・・"
    if (c == 'ヒ' or c == 'ビ' or c == 'ピ'
            or c == 'ﾋ'):
        if (c == 'ビ'):
            return "－－・・－　・・"
        if (c == 'ピ'):
            return "－－・・－　・・－－・"
        return "－－・・－"
    if (c == 'フ' or c == 'ブ' or c == 'プ'
            or c == 'ﾌ'):
        if (c == 'ブ'):
            return "－－・・　・・"
        if (c == 'プ'):
            return "－－・・　・・－－・"
        return "－－・・"
    if (c == 'ヘ' or c == 'ベ' or c == 'ペ'
            or c == 'ﾍ'):
        if (c == 'ベ'):
            return "・　・・"
        if (c == 'ペ'):
            return "・　・・－－・"
        return "・"
    if (c == 'ホ' or c == 'ボ' or c == 'ポ'
            or c == 'ﾎ'):
        if (c == 'ボ'):
            return "－・・　・・"
        if (c == 'ポ'):
            return "－・・　・・－－・"
        return "－・・"
    if (c == 'マ' or c == 'ﾏ'):
        return "－・・－"
    if (c == 'ミ' or c == 'ﾐ'):
        return "・・－・－"
    if (c == 'ム' or c == 'ﾑ'):
        return "－"
    if (c == 'メ' or c == 'ﾒ'):
        return "－・・・－"
    if (c == 'モ' or c == 'ﾓ'):
        return "－・・－・"
    if (c == 'ヤ' or c == 'ャ'
            or c == 'ﾔ' or c == 'ｬ'):
        return "・－－"
    if (c == 'ユ' or c == 'ュ'
            or c == 'ﾕ' or c == 'ｭ'):
        return "－・・－－"
    if (c == 'ヨ' or c == 'ョ'
            or c == 'ﾖ' or c == 'ｮ'):
        return "－－"
    if (c == 'ラ' or c == 'ﾗ'):
        return "・・・"
    if (c == 'リ' or c == 'ﾘ'):
        return "－－・"
    if (c == 'ル' or c == 'ﾙ'):
        return "－・－－・"
    if (c == 'レ' or c == 'ﾚ'):
        return "－－－"
    if (c == 'ロ' or c == 'ﾛ'):
        return "・－・－"
    if (c == 'ワ' or c == 'ヮ' or c == 'ﾜ'):
        return "－・－"
    if (c == 'ヰ'):
        return "・－・・－"
    if (c == 'ヱ'):
        return "・－－・・"
    if (c == 'ヲ' or c == 'ｦ'):
        return "・－－－"
    if (c == 'ン' or c == 'ﾝ'):
        return "・－・－・"

    # 数字
    if (c == '１' or c == '1'):
        return "・－－－－"
    if (c == '２' or c == '2'):
        return "・・－－－"
    if (c == '３' or c == '3'):
        return "・・・－－"
    if (c == '４' or c == '4'):
        return "・・・・－"
    if (c == '５' or c == '5'):
        return "・・・・・"
    if (c == '６' or c == '6'):
        return "－・・・・"
    if (c == '７' or c == '7'):
        return "－－・・・"
    if (c == '８' or c == '8'):
        return "－－－・・"
    if (c == '９' or c == '9'):
        return "－－－－・"
    if (c == '０' or c == '0'):
        return "－－－－－"

    # 日本語記号
    if (c == 'ー'):
        return "・－－・－"
    if (c == '、'):
        return "・－・－・－"
    if (c == 'ﾞ' or c == '゛'):
        return "・・"
    if (c == 'ﾟ' or c == '゜'):
        return "・・－－・"

    # 一致しない場合
    return "　"