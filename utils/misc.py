import pytesseract
import re
from PIL import Image

# need some tanwan surname
pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract-OCR/tesseract'
chinese_surname_list = set(['a','ba','pa','ma','fa','da','ta','na','la','ga','ka','ha','zha','cha','sha','za','ca','sa','ai','bai','pai','mai','dai','tai','nai','lai','gai','kai','hai','zhai','chai','shai','zai','cai','sai','an','an','ban','pan','man','fan','dan','tan','nan','lan','gan','kan','han','zhan','chan','shan','ran','zan','can','san','ang','ang','bang','pang','mang','fang','dang','tang','nang','lang','gang','kang','hang','zhang','chang','shang','rang','zang','cang','sang','ao','ao','bao','pao','mao','dao','tao','nao','lao','gao','kao','hao','zhao','chao','shao','rao','zao','cao','sao','me','de','te','ne','le','ge','ke','he','zhe','che','she','re','ze','ce','se','ei','ei','bei','pei','mei','fei','dei','nei','lei','gei','hei','shei','zei','en','en','ben','pen','men','fen','den','nen','gen','ken','hen','zhen','chen','shen','ren','zen','cen','sen','eng','beng','peng','meng','feng','deng','teng','neng','leng','geng','keng','heng','zheng','cheng','sheng','reng','zeng','ceng','seng','er','er','i','yi','bi','pi','mi','di','ti','ni','li','ji','qi','xi','zhi','chi','shi','ri','zi','ci','si','ia','ya','dia','lia','jia','qia','xia','ian','yan','bian','pian','mian','dian','tian','nian','lian','jian','qian','xian','yang','niang','liang','jiang','qiang','xiang','iao','yao','biao','piao','miao','diao','tiao','niao','liao','jiao','qiao','xiao','ie','ye','bie','pie','mie','die','tie','nie','lie','jie','qie','xie','in','yin','bin','pin','min','nin','lin','jin','qin','xin','ing','ying','bing','ping','ming','ding','ting','ning','ling','jing','qing','xing','yo','yong','jiong','qiong','xiong','iu','you','miu','diu','niu','liu','jiu','qiu','xiu','o','o','bo','po','mo','fo','lo','ong','weng','dong','tong','nong','long','gong','kong','hong','zhong','chong','rong','zong','cong','song','ou','ou','pou','mou','fou','dou','tou','nou','lou','gou','kou','hou','zhou','chou','shou','rou','zou','cou','sou','wu','bu','pu','mu','fu','du','tu','nu','lu','gu','ku','hu','zhu','chu','shu','ru','zu','cu','su','ua','wa','gua','kua','hua','zhua','shua','uai','wai','guai','kuai','huai','chuai','shuai','uan','wan','duan','tuan','nuan','luan','guan','kuan','huan','zhuan','chuan','shuan','ruan','zuan','cuan','suan','uang','wang','guang','kuang','huang','zhuang','chuang','shuang','ue','yue','nüe','lüe','jue','que','xue','wei','dui','tui','gui','kui','hui','zhui','chui','shui','rui','zui','cui','sui','un','wen','dun','tun','lun','gun','kun','hun','zhun','chun','shun','run','zun','cun','sun','uo','wo','duo','tuo','nuo','luo','guo','kuo','huo','zhuo','chuo','shuo','ruo','zuo','cuo','suo','ü','yu','nü','lü','ju','qu','xu','üan','yuan','juan','quan','xuan','yun','jun','qun','xun','tsui','chow','ng','lee','wong','lam','lo','tse','sung','tso','coi','sek','lv'])
def ocr(img):
    ret = pytesseract.image_to_string(Image.fromarray(img))
    if (len(ret) == 0):
        return False
    print(ret)
    ret = re.sub(r'[^a-z0-9 ]', ' ', ret.lower())
    surname = ret.split(' ')
    print(surname)
    if (surname[0] in chinese_surname_list
        or surname[1] in chinese_surname_list):
        #or surname[2] in chinese_surname_list):
        return True
    else:
        return False

def findFirstBlue(nameBox, x0, y0, fbBlue):
    print(fbBlue)
    height, width,_ = nameBox.shape
    for i in range(height):
        for j in range(width):
            find = True
            for c in range(3):
                find = find and abs(nameBox[i][j][c] - fbBlue[c]) < 1
            if (find):
                print (i,j)
                return [x0+i, y0+j]
    raise Exception('NameBox error', 'cannot find fb blue so cannot find name')