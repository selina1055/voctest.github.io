class Tester():
    def __init__(self):
        self.account = ''
        self.menu_title = '多益單字測驗(人物篇)'
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
        print(self.divider)
        print(self.menu_title)
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
        user_name = input('姓名:')
        print(self.divider)
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
                
    def op_one(self):
        """看英辨中"""
        import random
        score = 0
        self.words = []
        self.dictionary = {'executive':'主管','shareholder':'股東','consultant':'顧問','rep':'業務員','supplier':'供應商','account':'客戶','receptionist':'接待員','board_of_directors':'董事會','spectator':'參觀者','applicant':'申請人','supervisor':'管理者','tenant':'房客','plumber':'水電工','secretary':'秘書','supervisor':'監督人','president':'總經理','vice_president':'副總經理','client':'顧客','opponent':'對手','novice':'新手'}
        a = self.dictionary
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
        self.dictionary =  {'executive':'主管','shareholder':'股東','consultant':'顧問','rep':'業務員','supplier':'供應商','account':'客戶','receptionist':'接待員','board_of_directors':'董事會','spectator':'參觀者','applicant':'申請人','supervisor':'管理者','tenant':'房客','plumber':'水電工','secretary':'秘書','supervisor':'監督人','president':'總經理','vice_president':'副總經理','client':'顧客','opponent':'對手','novice':'新手'}
        a = self.dictionary
        print(self.divider)
        for words in self.dictionary:
                self.words.append(self.dictionary[words])
        for i in range(1,6):
            
            ques = random.choice(self.words)
            
            b = list(a.keys())[list(a.values()).index(ques)]
            
            print('第%s題:%s'%(i,ques))
            b = list(a.keys())[list(a.values()).index(ques)]
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
            while True:
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
                
        else:
            while True:
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
            