def q_to_b(text):
    """全角转半角: 半角 + 0x7e = 全角
    
    Arguments:
        text {unicode} -- py2: unicode, py3: str
    """
    b_str = ''
    for c in text:
        c_code = ord(c)
        if c_code == 12288:
            # 替换全角空格
            c_code = 32
        elif 65374 >= c_code >= 65281:
            c_code -= 65248

        b_str += chr(c_code)

    return b_str

def eng_to_ch(text):
    text = text.replace(',', '，').replace('?', '？')
    text = text.replace('!', '！').replace(';', '；')
    text = text.replace(':', '：')
    return text

def remove_s(text):
    text = text.replace(' ', '').replace('\n', '').replace('\t', '')
    text = text.replace('\r', '')
    return text