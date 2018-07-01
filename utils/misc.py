import pytesseract
import re
from PIL import Image

# install tesseract https://stackoverflow.com/a/46420423
pytesseract.pytesseract.tesseract_cmd = r'D:\Software\Tesseract-OCR\tesseract.exe'
# TODO need some tanwan surname
chinese_surname_list = set(['ai', 'an', 'ang', 'ao', 'au', 'yeung', 'ba', 'bai', 'ban', 'bao', 'bau', 'bi', 'bo', 'bu', 'cai', 'cao', 'cha', 'chai', 'cham', 'chan', 'chang', 'chao', 'chau', 'che', 'cheah', 'chee', 'chen', 'cheng', 'cheong', 'chern', 'cheung', 'chew', 'chi', 'chia', 'chiang', 'chiao', 'chien', 'chim', 'chin', 'ching', 'chiong', 'chiou', 'chiu', 'cho', 'choi', 'chong', 'choo', 'chou', 'chow', 'choy', 'chu', 'chua', 'chuang', 'chui', 'chun', 'chung', 'cong', 'cui', 'dai', 'dang', 'dea', 'deng', 'ding', 'do', 'dong', 'doo', 'du', 'duan', 'dung', 'eng', 'fan', 'fang', 'fei', 'feng', 'fok', 'fong', 'foo', 'fu', 'fung', 'gan', 'gang', 'gao', 'gau', 'ge', 'geng', 'go', 'goh', 'gong', 'gu', 'guan', 'guo', 'ha', 'hai', 'han', 'hang', 'hao', 'hau', 'he', 'ho', 'hoh', 'hom', 'hon', 'hong', 'hoo', 'hou', 'hsi', 'hsia', 'hsiao', 'hsieh', 'hsiung', 'hsu', 'hsueh', 'hu', 'hua', 'huang', 'hui', 'huie', 'hum', 'hung', 'huo', 'hwang', 'hy', 'ing', 'ip', 'jan', 'jang', 'jen', 'jeng', 'jeung', 'jew', 'jia', 'jian', 'jiang', 'jiao', 'jim', 'jin', 'jing', 'jo', 'joe', 'jong', 'joo', 'jou', 'jow', 'ju', 'jue', 'jung', 'kam', 'kan', 'kang', 'kao', 'kau', 'ke', 'keng', 'kho', 'khoo', 'kiang', 'king', 'ko', 'koh', 'kong', 'koo', 'kook', 'kou', 'ku', 'kuan', 'kuang', 'kuk', 'kung', 'kuo', 'kwan', 'kwock', 'kwok', 'kwon', 'kwong', 'lai', 'lam', 'lan', 'lang', 'lao', 'lau', 'lee', 'lei', 'leng', 'leong', 'leung', 'lew', 'li', 'lian', 'liang', 'liao', 'liaw', 'lien', 'liew', 'lim', 'lin', 'ling', 'liou', 'liu', 'lo', 'loh', 'lok', 'long', 'loo', 'lou', 'louie', 'lu', 'lua', 'lui', 'luk', 'lum', 'lung', 'luo', 'ma', 'mah', 'mai', 'mak', 'man', 'mao', 'mar', 'mau', 'may', 'mei', 'meng', 'miao', 'min', 'ming', 'miu', 'mo', 'mok', 'mon', 'mou', 'moy', 'mu', 'mui', 'na', 'ng', 'ngai', 'ngan', 'ngo', 'ni', 'nie', 'ning', 'niu', 'on', 'ong', 'ou', 'yang', 'ow', 'owyang', 'pan', 'pang', 'pao', 'pau', 'pei', 'peng', 'pi', 'ping', 'po', 'pon', 'pong', 'poon', 'pu', 'pun', 'qi', 'qian', 'qiao', 'qin', 'qiu', 'qu', 'quan', 'que', 'rao', 'ren', 'rong', 'ruan', 'sam', 'san', 'sang', 'seto', 'sha', 'sham', 'shan', 'shang', 'shao', 'shaw', 'shek', 'shen', 'sheng', 'sheu', 'shi', 'shiau', 'shieh', 'shih', 'shing', 'shiu', 'shu', 'shum', 'shy', 'shyu', 'si', 'sieh', 'sin', 'sing', 'sit', 'situ', 'siu', 'so', 'soh', 'song', 'soo', 'soon', 'soong', 'su', 'suen', 'sui', 'sum', 'sun', 'sung', 'sze', 'szeto', 'tai', 'tam', 'tan', 'tang', 'tao', 'tay', 'te', 'teh', 'teng', 'teo', 'tian', 'tien', 'tin', 'ting', 'tiu', 'to', 'toh', 'tom', 'tong', 'tsai', 'tsang', 'tsao', 'tsay', 'tse', 'tseng', 'tso', 'tsoi', 'tsou', 'tsu', 'tsui', 'tu', 'tuan', 'tung', 'tzeng', 'u', 'un', 'ung', 'wah', 'wai', 'wan', 'wang', 'wee', 'wei', 'wen', 'weng', 'wing', 'wong', 'woo', 'woon', 'wu', 'xi', 'xia', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xu', 'xue', 'yam', 'yan', 'yao', 'yap', 'yau', 'yaw', 'ye', 'yee', 'yeh', 'yen', 'yi', 'yim', 'yin', 'ying', 'yip', 'yiu', 'yong', 'yoon', 'you', 'young', 'yu', 'yuan', 'yue', 'yuen', 'yun', 'yung', 'zang', 'zeng', 'zha', 'zhan', 'zhang', 'zhao', 'zhen', 'zheng', 'zhong', 'zhou', 'zhu', 'zhuang', 'zhuo', 'zong', 'zou'])
def ocr(img):
    ret = pytesseract.image_to_string(Image.fromarray(img))
    if (len(ret) == 0):
        return False
    # print(ret)
    ret = re.sub(r'[^a-z0-9 ]', ' ', ret.lower())
    name = ret.split(' ')
    print(name)
    for part in name:
        if (part in chinese_surname_list):
            print(part)
            return True
    else:
        return False

def findFirstBlue(nameBox, x0, y0, fbBlue):
    height, width, _ = nameBox.shape
    print(height, width)
    for i in range(height):
        for j in range(width):
            find = True
            # print(nameBox[i][j][0], nameBox[i][j][1], nameBox[i][j][2])
            for c in range(3):
                find = find and (abs(nameBox[i][j][c] - fbBlue[c]) < 5)
            #print(find)
            if find == True:
                break
        if find == True:
            break
    if find == True:
        return [x0+j, y0+i]
    raise Exception('NameBox error', 'cannot find fb blue so cannot find name')

"""Assume rect is a list [top, bottom, left, right]"""
def getCenter (rect):
    top, bottom, left, right = rect
    return [int((left + right) / 2), int((top + bottom) / 2),]

'''return [height, width]'''
def getDim (rect):
    top, bottom, left, right = rect
    return [bottom - top, right - left]