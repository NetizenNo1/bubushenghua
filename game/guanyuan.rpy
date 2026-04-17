init python:
    guanwei = ["","一品","二品","三品","四品","五品","六品","七品","八品","九品","",""]
    Guanyuan_page=0
    class MalesFactory(object):
        def instantiation_Males(self):
            return NPC_Males()




    class Males(object):
        def __init__(self):
            self.xing = xing
            self.ming = ming
            self.name = name
            self.age = age
            self.level = level
            self.duty = duty
            self.zhong = zhong
            self.neng = neng
            self.exp = exp
            self.shili = shili
            self.feizi = feizi
            self.zhichi = zhichi
            self.friends = friends
            self.foes = foes
            self.marry = marry
            self.qizi = None
            self.qieshi = qieshi
        
        def Males_creat(self):
            self.xing = ""
            self.ming = ""
            self.name = ""
            self.age = 0
            self.face = 0
            self.beauty = 0
            self.shou = 80
            self.level = 0
            self.duty = ""
            self.zhong = 0
            self.neng = 0
            self.exp = 0
            self.shili = 0
            self.feizi = []
            self.zhichi = None
            self.friends = []
            self.foes = []
            self.marry = False
            self.qizi = None
            self.qieshi = []

    def Males_random(self,whose,how):
        self.xing = whose.xing
        self.ming = renpy.random.choice(malename_list)+renpy.random.choice(malename2_list)
        self.name = self.xing+self.ming
        if how == 0 or how ==10: 
            self.age =  whose.age + renpy.random.randint(18,40)
            self.marry = True
        elif how == 1 or how ==11:
            self.age =  whose.age + renpy.random.randint(-10,10)
            if self.age <= 16:
                self.age = 16
            lucky = renpy.random.randint(0,self.age)
            if lucky <= 12:
                pass
            else:
                self.marry = True
        elif how == 2 or how ==12:
            self.age =  whose.age + renpy.random.randint(36,60)
            if self.age >= 70:
                self.age = 70
            self.marry = True
        else:
            self.age = whose.age + renpy.random.randint(-20,20)
            if self.age <= 16:
                self.age = 16
            self.marry = True
        
        self.face = 0
        self.beauty = renpy.random.randint(0,100)
        self.shou = renpy.random.randint(self.age+5,100)
        
        self.level = whose.familylevel  
        self.duty = whose.fatherduty 
        self.zhong = renpy.random.randint(0,100)  
        self.neng = renpy.random.randint(0,100)  
        self.shili = (11 - self.level)*renpy.random.randint(1,10) *0.1 + renpy.random.randint(-10,10) + self.neng  
        self.exp = renpy.random.randint(-20,20)   
        if how >= 10:
            pass
        else:
            self.feizi.append(whose)
        self.zhichi = None
        self.friends = []
        self.foes = []




    class NPC_Males(Males):
        def __init__(self):
            Males.Males_creat(self)

    Malesfactory = MalesFactory()

    def Creat_Males(whose,how):
        a = Malesfactory.instantiation_Males()
        Males_random(a,whose,how)
        if how == 0:
            whose.father = a
        else:
            pass
        whose.jiazu.append(a)
        if 1 <= a.level <= 9:
            guanyuan_list.append(a)

    def gyb_change(how):
        global guanyuan_list
        if how == "level":
            guanyuan_list = sorted(guanyuan_list, key=attrgetter(how),reverse = False)
        else:
            guanyuan_list = sorted(guanyuan_list, key=attrgetter(how),reverse = True)

    def guanyuan_levelchange(self,sheng):
        temptext = guanwei[self.level]+self.duty+self.name
        if sheng == True:
            self.shili += self.neng*0.1
            self.level -= 1
            tempstory = str(year)+"年"+str(month)+"月，家父"+str(temptext) +"晋升为"+str(guanwei[self.level])+str(self.duty)+"。\n"
            tempstory2 = "【前朝】"+str(year)+"年"+str(month)+"月，"+str(temptext)+ "晋升为"+str(guanwei[self.level])+str(self.duty)+"。\n"
            allstory.insert(0,tempstory2)
        
        else:
            self.shili -= self.neng*0.1
            self.level += 1
            if self.level > 9 :
                self.level = 12
                self.duty = "平民"
                guanyuan_list.remove(self)
                tempstory = str(year)+"年"+str(month)+"月，家父"+str(temptext)+"被褫夺官位，沦为平民。\n"
                tempstory2 = "【前朝】"+str(year)+"年"+str(month)+"月，"+str(temptext)+ "被褫夺官位，沦为平民。\n"
            
            else:
                tempstory = str(year)+"年"+str(month)+"月，家父"+str(temptext)+"贬谪为"+str(guanwei[self.level])+str(self.duty)+"。\n"
                tempstory2 = "【前朝】"+str(year)+"年"+str(month)+"月，"+str(temptext)+ "贬谪为"+str(guanwei[self.level])+str(self.duty)+"。\n"
            allstory.insert(0,tempstory2)
        
        
        for i in self.feizi:
            i.story.append(tempstory)
            i.familylevel = self.level
            if self.level > 9 :
                i.family = "平民之女"
            else:
                i.family = str(guanwei[i.familylevel]) + i.fatherduty + i.familylocation
            if i.familylevel > 3 and tags_family[1] in i.tags:
                i.tags.remove(tags_family[1])
            if i.familylevel <= 3 and tags_family[1] not in i.tags:
                i.tags.insert(0,tags_family[1])
            if i.familylevel < 8  and tags_family[2] in i.tags:
                i.tags.remove(tags_family[2])
            if i.familylevel >= 8 and tags_family[2] not in i.tags:
                i.tags.insert(0,tags_family[2])

    def fushang_levelchange(self,sheng):
        if sheng == True:
            self.duty = renpy.random.choice(['文官', '武将'])
            self.shili += self.neng*0.1
            self.level -= 1
            tempstory = str(year)+"年"+str(month)+"月，家父"+str(self.name)+"弃商入仕，成为"+str(guanwei[self.level])+str(self.duty)+"。\n"
            tempstory2 = "【前朝】"+str(year)+"年"+str(month)+"月，富商"+str(self.name)+"入仕从官，成为"+str(guanwei[self.level])+str(self.duty)+"。\n"
            guanyuan_list.append(self)
            allstory.insert(0,tempstory2)
            for i in self.feizi:
                i.familylocation = "嫡女"
                i.fatherduty = self.duty
                i.story.append(tempstory)
                i.familylevel = self.level
                i.family = str(guanwei[i.familylevel]) + i.fatherduty + i.familylocation
        
        else:
            self.shili -= self.neng*0.1
            self.level += 1
            self.duty = "平民"
            tempstory = str(year)+"年"+str(month)+"月，家父经营不善，沦为平民。\n"
            for i in self.feizi:
                i.fatherduty = self.duty
                i.story.append(tempstory)
                i.familylevel = self.level
                i.family = "平民之女"
        return



    def pingmin_levelchange(self):
        self.shili += self.neng*0.1
        self.level -= 1
        self.duty = "富商"
        tempstory = str(year)+"年"+str(month)+"月，家中白手起家，经营有方，成为当地富商。\n"
        for i in self.feizi:
            i.story.append(tempstory)
            i.familylevel = self.level
            i.family = "富商之女"
        return


label 前朝演变:
    python:
        lucky = renpy.random.randint(0, 6)
        if lucky == 0 :
            guanyuan_list = sorted(guanyuan_list, key=attrgetter("neng"),reverse = True)
            guanyuan_list[0].exp += (guanyuan_list[0].neng+guanyuan_list[0].zhong)*0.02*guanyuan_list[0].level
            if guanyuan_list[0].duty == "文官":
                huangdi["政务"] += 0.5
            else:
                huangdi["军事"] += 0.5
        elif lucky == 1:
            guanyuan_list = sorted(guanyuan_list, key=attrgetter("zhong"),reverse = True)
            guanyuan_list[0].exp += (guanyuan_list[0].neng+guanyuan_list[0].zhong)*0.02*guanyuan_list[0].level
            if guanyuan_list[0].duty == "文官":
                huangdi["政务"] += 0.5
            else:
                huangdi["军事"] += 0.5
        else:
            tempgy = renpy.random.choice(guanyuan_list)
            lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                if tempgy.zhong >= 70:
                    tempgy.exp += (tempgy.neng+tempgy.zhong)*0.02*tempgy.level
                elif tempgy.zhong <= 30:
                    tempgy.exp -= (tempgy.neng-tempgy.zhong)*0.02*tempgy.level
                else:
                    pass
            elif lucky == 1:
                if tempgy.neng >= 70:
                    tempgy.exp += (tempgy.neng+tempgy.zhong)*0.02*tempgy.level
                elif tempgy.zhong <= 30:
                    tempgy.exp -= (tempgy.neng-tempgy.zhong)*0.02*tempgy.level
                else:
                    pass
            else:
                tempgy.exp += (tempgy.neng+tempgy.zhong)*0.02*tempgy.level

        lucky = renpy.random.randint(0, 100)
        if lucky < huangdi["暴戾"]:
            guanyuan_list = sorted(guanyuan_list, key=attrgetter("shili"),reverse = True)
            guanyuan_list[0].shili -= huangdi["暴戾"]*0.05 + renpy.random.randint(0,2)
            guanyuan_list[0].exp -= (guanyuan_list[0].neng-guanyuan_list[0].zhong)*0.05*guanyuan_list[0].level
        else:
            pass

        for i in guanyuan_list:
            lucky = renpy.random.randint(0,100)
            if lucky < i.neng :
                i.exp += i.neng*0.005
            lucky = renpy.random.randint(0,100)
            if lucky < i.zhong :
                i.exp += i.zhong*0.005
            if i == taoning.father :
                i.exp = 0
            
            if i.exp >= 100 and i.level == 1:
                i.exp -=100
                i.shili += 5
            elif i.exp >= 100 :
                i.exp -=100
                renpy.call("官员升降",who = i,how = 0,from_current=False)
            elif i.exp <= -20:
                i.exp += 20
                renpy.call("官员升降",who = i,how = 1,from_current=False)
            else:
                pass

        for i in NPC_fz_list:
            if i == my:
                pass
            if i in juqingfei:
                pass
            
            elif i.familylevel == 11 or i.familylevel == 10:
                tempnum = 0
                if diwei(i) == 0 :
                    tempnum += 5
                elif diwei(i) == 1:
                    tempnum += 3
                elif diwei(i) == 2:
                    tempnum += 1
                else:
                    pass
                if i.love >= 20:
                    tempnum += (i.love-20)*0.1
                lucky = renpy.random.randint(0,10)
                if lucky < tempnum :
                    if i.familylevel == 11:
                        i.father.exp += tempnum*1.5
                    else:
                        i.father.exp += tempnum
                else:
                    pass
        for i in NPC_fz_list:
            if i.father == "":
                pass
            elif isinstance(i.father,NoneType):
                pass
            
            
            else:
                if i.father.exp >= 100 and i.father.level >= 10:
                    i.father.exp -= 100
                    if i.familylevel == 11:
                        pingmin_levelchange(i.father)
                        if i == my:
                            renpy.call("平民升级",from_current=False)
                    if i.familylevel == 10:
                        fushang_levelchange(i.father,True)
                        if i == my:
                            renpy.call("富商升降",how = 0,from_current=False)
                elif i.father.exp <= -20 and i.familylevel == 10:
                    i.father.exp += 20
                    fushang_levelchange(i.father,False)
                    if i == my:
                        renpy.call("富商升降",how = 1,from_current=False)
                else:
                    pass




    python:
        renpy.return_statement()



label 富商升降(how):
    if how == 0:
        $ bg("寝居")
        show 我的宫女
        我的宫女 "主子，有好消息呐！"
        我的宫女 "[my.xing]大人捎了信说他花了重金买了一个官位……如今也算是入仕了！"
    else:

        $ bg("寝居")
        show 我的宫女
        我的宫女 "主子，不好了……"
        我的宫女 "[my.xing]大人捎了信说，家中经营不善，所幸以前还存着些积蓄，倒不至于倾家荡产，但以后的日子可要难过了……"
    hide 我的宫女

    return


label 平民升级:

    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子，有好消息呐！"
    我的宫女 "[my.xing]大人捎了信说他之前用存的积蓄收购了几家铺子，如今情势大好，已是一方富商了！"
    hide 我的宫女

    python:
        renpy.return_statement()


label 官员升降(who, how):
    if how == 0:
        $ guanyuan_levelchange(who,True)
        if my in who.feizi:
            "前朝传来了你的父亲升职的消息。"
            "（家世变更为[my.family]）"
        else:
            pass
    else:
        $ guanyuan_levelchange(who,False)
        if my in who.feizi:
            "前朝传来了你的父亲被贬的消息。"
            "（家世变更为[my.family]）"
        else:
            pass
    python:
        renpy.return_statement()



style guanyuanbiao_button_text:
    font "问藏书房.ttf"
    min_width 110
    size 30
    text_align 0.5


style guanyuanbiao_text:
    font "问藏书房.ttf"
    min_width 120
    size 25
    text_align 0.5


screen guanyuanbiao:
    style_prefix "guanyuanbiao"
    $ next_Guanyuan_page = Guanyuan_page + 1
    $ prev_Guanyuan_page = Guanyuan_page - 1
    $ max_Guanyuan_page = round(len(guanyuan_list)/10)+1
    $ b = Guanyuan_page*10+10

    if b >= len(guanyuan_list):
        $ b = len(guanyuan_list)
    else:
        pass
    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        xsize 1400
        ysize 680
        align (0.5,0.5)
        hbox:
            align (0.5, 1.0)
            spacing 0
            if Guanyuan_page > 0:
                textbutton "《《" action SetVariable('Guanyuan_page', prev_Guanyuan_page), Show("guanyuanbiao")
            else:
                textbutton "《《"
            text "第[next_Guanyuan_page]页"
            if Guanyuan_page < max_Guanyuan_page:
                textbutton "》》" action SetVariable('Guanyuan_page', next_Guanyuan_page), Show("guanyuanbiao")
            else:
                textbutton "》》"

        vbox:
            pos (0.05,0.05)
            xsize 1400
            ysize 600
            spacing 10
            $ a = 0
            $ next_Guanyuan_page = Guanyuan_page + 1
            fixed:
                xsize 1400
                ysize 40
                hbox:
                    textbutton "职位":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"level")
                        align (0.0,0.0)
                    textbutton "名字":
                        text_style "guanyuanbiao_button_text"
                        action NullAction()
                        align (0.0,0.0)
                    textbutton "年龄":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"age")
                        align (0.0,0.0)
                    textbutton "外貌":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"beauty")
                        align (0.0,0.0)
                    textbutton "能力":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"neng")
                        align (0.0,0.0)
                    textbutton "忠诚":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"zhong")
                        align (0.0,0.0)
                    textbutton "势力":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"shili")
                        align (0.0,0.0)
                    textbutton "功勋":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"exp")
                        align (0.0,0.0)
                    textbutton "婚配":
                        text_style "guanyuanbiao_button_text"
                        action NullAction()
                        align (0.0,0.0)
                    textbutton "关系":
                        text_style "guanyuanbiao_button_text"
                        action NullAction()
                        align (0.0,0.0)


            for i in guanyuan_list[Guanyuan_page*10:b]:
                if a <= b:
                    fixed:
                        xsize 1400
                        ysize 40
                        hbox:
                            text guanwei[i.level] + i.duty align (0.0,0.0)
                            text "[i.name]" align (0.0,0.0)
                            text str(i.age)+"岁" align (0.0,0.0)
                            text str(i.beauty) align (0.0,0.0)
                            text str(int(i.neng)) align (0.0,0.0)
                            text str(int(i.zhong)) align (0.0,0.0)
                            text str(int(i.shili)) align (0.0,0.0)
                            text str(int(i.exp)) align (0.0,0.0)
                            if i.marry == True:
                                text "已婚" align (0.0,0.0)
                            else:
                                text "未婚" align (0.0,0.0)
                            python:
                                temptext = ""

                                for j in i.feizi:
                                    temptext += j.hao+j.weifen+j.name + " "
                                if i.qizi != None:
                                    temptext += i.qizi.fenghao + i.qizi.name+ " "
                                if i.zhichi != None:
                                    temptext +=  i.zhichi.cheng+i.zhichi.name
                            text "{size=20}[temptext]" align (0.0,0.0)


                    $ a = a + 1
                else:
                    null
            if a < 10:
                for j in range(a, 10):
                    null
    frame:
        background None
        align (1.0,1.0)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("guanyuanbiao"),Jump("寝居界面")
 
