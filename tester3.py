class Tester():
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
        self.typeop_menu = {
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

    def show_menu(self):
        """ 主選單"""
        print(self.divider)
        print(self.menu_title,self.account)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def login_or_signup(self,account=''):
        """輸入名字"""
        user_name = input('請先輸入姓名:')
        # print(self.divider)
        self.account = user_name
        return self.account
        
    def type_op(self):
        """選擇測驗類型"""
        for i, p in self.op_menu.items():
            print('%s:%s' % (i, p))
        print(self.divider)
        option = input('請選擇: ').lower()
        if option in self.op_menu.keys():
            return option,self.op_menu[option]
        else:
            return option, '無此功能！'

    def op_test(self):
        """選擇測驗篇"""
        for i, p in self.typeop_menu.items():
            print('%s:%s' % (i, p))
        print(self.divider)
        option = input('請選擇: ').lower()
        if option in self.typeop_menu.keys():
            return option,self.typeop_menu[option]
        else:
            return option, '無此功能！'
                
    def op_one(self):
        """看英辨中"""
        import random
        score = 0
        self.words = []
        print(self.divider)
        for words in self.dictionary:
                self.words.append(words)
        for i in range(1,6):
            ques = random.choice(self.words)
            print('第%s題:%s'%(i,ques))
            ans = input('請作答:')
            if ans == self.dictionary[ques]:
                print('正確!')
                score+=20
                self.words.remove(ques)
                print(self.divider)
            else:
                print('***錯誤,正確答案是:%s!***'%self.dictionary[ques])
                self.words.remove(ques) 
                print(self.divider)
        print('%s,你的成績是%s!'%(self.account,score))

    def op_two(self):
        """看中辨英"""
        import random
        score = 0
        self.words = []
        print(self.divider)
        for words in self.dictionary:
                self.words.append(self.dictionary[words])
        for i in range(1,6):
            ques = random.choice(self.words)
            b = list(self.dictionary.keys())[list(self.dictionary.values()).index(ques)]
            print('第%s題:%s'%(i,ques))
            b = list(self.dictionary.keys())[list(self.dictionary.values()).index(ques)]
            ans = input('請作答:')
            if ans == b:
                print('正確!')
                score+=20
                self.words.remove(ques)
                print(self.divider)
            else:
                print('***錯誤,正確答案是:%s!***'%b)
                self.words.remove(ques) 
                print(self.divider)
        print('%s,你的成績是%s!'%(self.account,score))

    
tester = Tester()
while True:
    func_id, func_name = tester.show_menu()
    if func_id == 'q':
        break
    elif func_id == '':
        print(func_name)
    else:
        if tester.account == '':
            user_name= tester.login_or_signup()
            tester.account = user_name
        else:
            while True:
                while True:
                    o,p = tester.op_test()
                    if o in tester.typeop_menu.keys():
                        print(p)
                        print(tester.divider)
                        break
                    else:
                        print(p)
                        print(tester.divider)
                if o == 'a':
                    tester.dictionary = {
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
                    tester.dictionary = {
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
                    tester.dictionary = {
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
                    tester.dictionary = {'allocate':'撥出',
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
                    tester.dictionary = {'allocate':'撥出',
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
                    tester.dictionary = {'allocate':'撥出',
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
                    tester.dictionary = {'allocate':'撥出',
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
                    tester.dictionary = {'allocate':'撥出',
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
                a,c = tester.type_op()
                if a == 'a':
                    print(c)
                    b = tester.op_one()
                    break
                elif a == 'b':
                    print(c)
                    b = tester.op_two()
                    break
                else:
                    print(c)
                    print(tester.divider)