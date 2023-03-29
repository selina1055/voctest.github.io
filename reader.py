
class Reader():
    def __init__(self):
        self.account = ''
        
        self.menu = {
            'a':'開始測驗',          
            'q':'離開'
        }        
        self.op_menu = {
            'a':'看英辨中',          
            'b':'看中辨英'
        }
        self.divider = '='*15        

    def show_menu(self):
        """ 主選單"""
        opt = input('a.開始測驗 q.離開 請選擇: ',validate=self.check_key1 ).lower()
        return opt,self.menu[opt]
        
    def check_key1(self,opt):  # return None when the check passes, otherwise return the error message
        if opt in self.menu.keys():
            pass
        else:
            return '無此功能!'

    def login_or_signup(self,account=''):
        """輸入名字"""
        user_name = input('姓名:')
        self.account = user_name
        return self.account

    def op_test(self):
        """選擇測驗篇"""
        for i, p in self.typeop_menu.items():
            print('%s:%s' % (i, p))
        print(self.divider)
        option = input('請選擇: ',validate=self.check_key3).lower
        return option,self.typeop_menu[option]

    def check_key3(self,option):  
        if option in self.op_menu.keys():
            pass
        else:
            return '無此功能!'
        
    def type_op(self):
        """選擇測驗類型"""
        option = input('a.看英辨中 b.看中辨英 請選擇: ',validate=self.check_key2).lower()
        return option,self.op_menu[option]
        
    def check_key2(self,option):  # return None when the check passes, otherwise return the error message
        if option in self.op_menu.keys():
            pass
        else:
            return '無此功能!'
                
    def op_one(self):
        """看英辨中"""
        import random
        score = 0
        self.words = []
        self.dictionary = {'executive':'主管','shareholder':'股東','consultant':'顧問','rep':'業務員','supplier':'供應商','account':'客戶','receptionist':'接待員','board_of_directors':'董事會','spectator':'參觀者','applicant':'申請人','supervisor':'管理者','tenant':'房客','plumber':'水電工','secretary':'秘書','supervisor':'監督人','president':'總經理','vice_president':'副總經理','client':'顧客','opponent':'對手','novice':'新手'}
        a = self.dictionary
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
        self.dictionary =  {'executive':'主管','shareholder':'股東','consultant':'顧問','rep':'業務員','supplier':'供應商','account':'客戶','receptionist':'接待員','board_of_directors':'董事會','spectator':'參觀者','applicant':'申請人','supervisor':'管理者','tenant':'房客','plumber':'水電工','secretary':'秘書','supervisor':'監督人','president':'總經理','vice_president':'副總經理','client':'顧客','opponent':'對手','novice':'新手'}
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

def voctest():
    reader = Reader()
    put_markdown('# 多益單字測驗(人物篇)')
    put_image('https://shopee.tw/blog/wp-content/uploads/2019/11/toeic.jpg',title='取自網路',width='40%')
    put_text('')
    put_info("""TOEIC多益是一種英文檢定，考試內容範圍以職場商業英語為主

許多大學商管科系及研究所會將多益成績列為畢業門檻之一。而且不少公司徵才需要考量英語能力時，亦會參考採認多益成績

本自主學習題目旨在撰寫一個簡易多益單字挑戰測驗系統，用以練習python及強化多益單字能力""")
    put_info('每次測驗共5題，每題20分，共100分。')
    put_text(reader.divider)
    put_markdown(" - 功能列表")
    for fid, fname in reader.menu.items():
        put_table([
    ['%s'%fid, '%s'%fname],
])
    put_text(reader.divider)    
    put_markdown(" - 測驗選項列表")
    for i, p in reader.op_menu.items():
        put_table([
    ['%s'%i, '%s'%p],
])
    put_text(reader.divider)
    while True:
        func_id, func_name = reader.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            if reader.account == '':
                user_name= reader.login_or_signup()
                reader.account = user_name
                
            else:
                while True:
                    while True:
                        o,p = reader.op_test()
                        if o in reader.typeop_menu.keys():
                            print(p)
                            print(reader.divider)
                            break
                        else:
                            print(p)
                            print(reader.divider)
                    if o == 'a':
                        reader.dictionary = {
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
                        reader.dictionary = {
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
                        reader.dictionary = {
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
                        reader.dictionary = {'allocate':'撥出',
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
                        reader.dictionary = {'allocate':'撥出',
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
                        reader.dictionary = {'allocate':'撥出',
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
                        reader.dictionary = {'allocate':'撥出',
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
                        reader.dictionary = {'allocate':'撥出',
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
        

                    a,c = reader.type_op()
                    if a == 'a':
                        print(c)
                        b = reader.op_one()
                        break
                    elif a == 'b':
                        print(c)
                        b = reader.op_two()
                        break
                    else:
                        print(c)
                        
            
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/voctest", webio_handler(voctest)),  
    ])
    application.listen(port=80, address='localhost')
    tornado.ioloop.IOLoop.current().start()
    session.hold()



            
            
            

            
            
        
            

    