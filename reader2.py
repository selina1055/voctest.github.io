
class Reader():
    def __init__(self):
        self.account = ''
        self.dictionary = {}
        self.menu_title = '多益單字測驗'
        self.menu = {
            'a':'開始測驗',          
            'q':'離開'
        }        
        self.op_menu = {
            'a':'看英辨中',          
            'b':'看中辨英'
        }
        self.type_op_menu = {
            'a':'人物篇',          
            'b':'辦公室篇',
            'c':'人事管理篇',          
            'd':'薪資金錢篇',
            'e':'業務篇',          
            'f':'財務篇',
            'g':'貿易篇',          
            'h':'會議篇'
        }
        self.divider = '='*20      

    def login_or_signup(self,account=''):
        """輸入名字"""
        user_name = input('姓名:')
        self.account = user_name
        put_markdown('# %s,您好!'%user_name)

    
        
    def type_op(self,o):
        """選擇測驗類型"""
        if o == 'a':
            toast("您選擇了人物篇")
            self.dictionary = {
        'executive':'主管',
        'shareholder':'股東',
        'consultant':'顧問',
        'rep':'業務員',
        'supplier':'供應商',
        'account':'客戶',
        'receptionist':'接待員',
        'board_of_directors':'董事會',
        'spectator':'參觀者',
        'applicant':'申請人',
        'supervisor':'管理者',
        'tenant':'房客',
        'plumber':'水電工',
        'secretary':'秘書',
        'supervisor':'監督人',
        'president':'總經理',
        'vice_president':'副總經理',
        'client':'顧客',
        'opponent':'對手',
        'novice':'新手'}
        elif o == 'b':
            toast("您選擇了辦公室篇")
            self.dictionary = {
        'appointment':'約會',
        'attendance':'出席',
        'cabinet':'顧問',
        'calendar':'日曆',
        'clerk':'辦事員',
        'directory':'人名住址簿',
        'duplicate':'複製',
        'filing':'歸檔',
        'in-tray':'待處理文件盒',
        'monitor':'檢測',
        'out-tray':'已處理文件盒',
        'partition':'分隔',
        'postage':'郵費',
        'punctuality':'準時',
        'schedule':'時間表',
        'shift':'換班',
        'staff':'全體職員',
        'strike':'罷工',
        'task':'工作',
        'work_force':'工作人員',
        'assignment':'分配',
        'bulletin':'公報',
        'calculator':'計算器',
        'carbon_copy':'用複寫紙複製的副本',
        'colleague':'同事',
        'document':'文件',
        'extension':'分機（電話）',
        'intercom':'對講機',
        'memo':'便條',
        'operator':'接線生',
        'overtime':'加班的時間',
        'portfolio':'作品夾',
        'printed_matter':'印刷品',
        'receptionist':'接待員',
        'secretary':'秘書',
        'shorthand':'速記',
        'stapler':'釘書機',
        'tardy':'遲緩的',
        'typist':'打字員',
        'xerox':'影印'   }
        elif o == 'c':
            toast("您選擇了人事管理篇")
            self.dictionary = {
        'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}
        elif o == 'd':
            toast("您選擇了薪資金錢篇")
            self.dictionary = {'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}
        elif o == 'e':
            toast("您選擇了業務篇")
            self.dictionary = {'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}
        elif o == 'f':
            toast("您選擇了財務篇")
            self.dictionary = {'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}
        elif o == 'g':
            toast("您選擇了貿易篇")
            self.dictionary = {'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}
        elif o == 'h':
            toast("您選擇了會議篇")
            self.dictionary = {'allocate':'撥出',
        'applicant':'申請人',
        'authorize':'授權',
        'capability':'能力',
        'lay_off':'暫時解雇',
        'collaboration':'合作',
        'consultation':'諮詢',
        'curriculum_vitae':'履歷',
        'eligible':'合格的',
        'emplyer':'雇主',
        'executive':'行政或管理人員',
        'appoint':'任命',
        'benefit':'有益於',
        'candidate':'候選人',
        'certificate':'證書',
        'competent':'有能力的',
        'coordinate':'協調',
        'deadline':'截至期限',
        'employee':'受雇者',
        'expertise':'專門技術或知識'}


                
    def op_one(self):
        """看英辨中"""
        import random
        score = 0
        self.words = []
        if self.dictionary=={}:
            toast("請先選擇不同類型篇")
        for words in self.dictionary:
                self.words.append(words)
        for i in range(1,6):
            ques = random.choice(self.words)
            ans = input('第%s題:%s'%(i,ques))
            if ans == self.dictionary[ques]:
                toast('正確!')
                score+=20
                self.words.remove(ques)
            else:
                toast('***錯誤,正確答案是:%s!***'%self.dictionary[ques])
                self.words.remove(ques) 
        popup('%s,你的成績是%s!'%(self.account,score))

    def op_two(self):
        """看中辨英"""
        import random
        score = 0
        self.words = []
        if self.dictionary=={}:
            toast("請先選擇不同類型篇")
        a = self.dictionary
        for words in self.dictionary:
                self.words.append(self.dictionary[words])
        for i in range(1,6):
            ques = random.choice(self.words)            
            b = list(a.keys())[list(a.values()).index(ques)]
            ans = input('第%s題:%s'%(i,ques))
            if ans == b:
                toast('正確!')
                score+=20
                self.words.remove(ques)
            else:
                toast('***錯誤,正確答案是:%s!***'%b)
                self.words.remove(ques) 
        popup('%s,你的成績是%s!'%(self.account,score))

    

            

from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler
from pywebio import session
from functools import partial

def startbutton():
    reader = Reader()
    reader.login_or_signup()
    put_button(label='人物篇', onclick=partial(reader.type_op,o='a'))
    put_button(label='辦公室篇', onclick=partial(reader.type_op,o='b'))
    put_button(label='人事管理篇', onclick=partial(reader.type_op,o='c'))
    put_button(label='薪資金錢篇', onclick=partial(reader.type_op,o='d'))
    put_button(label='業務篇',onclick=partial(reader.type_op,o='e'))
    put_button(label='財務篇', onclick=partial(reader.type_op,o='f'))
    put_button(label='貿易篇', onclick=partial(reader.type_op,o='g'))
    put_button(label='會議篇', onclick=partial(reader.type_op,o='h'))
    put_text(reader.divider)
    put_button(label='看英辨中',color= 'warning',onclick=reader.op_one)
    put_button(label='看中辨英',color= 'warning',onclick=reader.op_two)
    put_text(reader.divider)


    

def voctest():
    put_markdown('# 多益單字測驗(人物篇)')
    put_info("""TOEIC多益是一種英文檢定，考試內容範圍以職場商業英語為主

許多大學商管科系及研究所會將多益成績列為畢業門檻之一。而且不少公司徵才需要考量英語能力時，亦會參考採認多益成績

本自主學習題目旨在撰寫一個簡易多益單字挑戰測驗系統，用以練習python及強化多益單字能力""")
    put_info('每次測驗共5題，每題20分，共100分。')
    put_image('https://shopee.tw/blog/wp-content/uploads/2019/11/toeic.jpg',title='取自網路',width='40%')
    reader = Reader()
    put_text(reader.divider)
    put_button(label='開始測驗',color='success',onclick=startbutton)
    put_text(reader.divider)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/voctest2.0", webio_handler(voctest)),  
    ])
    application.listen(port=80, address='localhost')
    tornado.ioloop.IOLoop.current().start()
    session.hold()


            
            
            

            
            
        
            

    
