init python:
    class KidsFactory(object):
        def instantiation_Kids(self):
            return NPC_Kids()






    class Kids(object):
        def __init__(self):
            self.sex = sex
            self.paixu = paixu
            self.name = name
            self.age = age
            self.cheng = cheng
            self.face = face
            self.state = state
            self.mother = mother
            self.shengmu = shengmu
            self.health = health 
            self.beauty = beauty 
            self.iq = iq 
            self.qingxiang = qingxiang
            self.wen = wen 
            self.wu = wu 
            self.duli = duli 
            self.qinmian = qinmian
            self.xingge = xingge
            self.xingqing = xingqing
            self.pingjia = pingjia
            self.like = like
            self.hdlike = hdlike
            self.zheng = zheng 
            self.ceshi = ceshi
            self.qie = qie
            self.kids = kids
            self.shou = shou
            self.plan = plan 
            self.fenghao = fenghao
            self.qinzi = qinzi 
            self.likefz = likefz
            self.hatefz = hatefz
            self.friends = friends
            self.foes = foes
            self.live = live
            self.story = story
            self.shili = shili
            self.zhichi = zhichi
            self.zhichizhe = zhichizhe
            self.nengli = nengli
            self.exp = exp
        
        def Kids_creat(self):
            self.sex = "皇子"
            self.name = ""
            self.age = 0
            self.qinzi = 0
            self.cheng = ""
            self.face = ""
            self.state = "寻常"
            self.mother = None
            self.shengmu = None
            self.health = 0 
            self.beauty = 0 
            self.iq = 0 
            self.ability = 0 
            self.qingxiang = 0
            self.wen = 0 
            self.wu = 0 
            self.duli = 0 
            self.qinmian = 0
            self.xingge = ""
            self.xingqing = ""
            self.pingjia = ""
            self.like = 0
            self.hdlike = 0
            self.zheng = None 
            self.ceshi =[]
            self.qie = []
            self.kids = []
            self.shou = 0
            self.paixu = 0
            self.likefz = []
            self.hatefz = []
            self.friends = []
            self.foes = []
            self.zhichi = None
            self.zhichizhe =[]
            self.shili = 0
            self.live = 0 
            self.plan = "顺其自然" 
            self.fenghao = ""
            self.nengli = 0
            self.exp = 0

    class NPC_Kids(Kids):
        def __init__(self):
            Kids.Kids_creat(self)

    Kidsfactory = KidsFactory()

    def Creat_Kids(whose):
        a = Kidsfactory.instantiation_Kids()
        NPC_Kids_list.append(a)
        Kids_random(a)
        a.shengmu = whose
        a.mother = whose
        whose.kids.append(a)
        Kids_tianfu(a,whose)


    def Kids_random(self):
        self.sex = renpy.random.choice(["皇子","公主"])
        self.age = 0
        self.paixu = len(NPC_Kids_list)+1
        self.xingge = renpy.random.choice(["内向","外向","中庸"])
        self.xingqing = self.xingge
        self.shou = renpy.random.randint(45, 85)
        self.qingxiang = renpy.random.randint(0, 100)
        self.state = "寻常"
        self.plan = "顺其自然"
        self.zhichizhe = []
        
        if self.sex == "皇子":
            self.name = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
            self.face = "B1"
            if len(huangzi) != 0:
                self.cheng = huangzi[0]
                huangzi.remove(self.cheng)
            else:
                self.cheng = "皇子"
        else:
            self.name = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
            if len(self.name) > 2:
                self.name = self.name[0] + self.name[1]
            if self.name in teshuming :
                if self.name in ming_list:
                    ming_list.remove(self.name)
            
            self.face = "G1"
            if len(gongzhu) != 0:
                self.cheng = gongzhu[0]
                gongzhu.remove(self.cheng)
            else:
                self.cheng = "公主"
        self.story = []

    def Kids_tianfu(self,shengmu):
        self.health = int(self.shengmu.health*0.1) + renpy.random.randint(-30, 30)
        if self.health < 20:
            self.health = 20
        elif self.health > 100:
            self.health = 100
        else:
            pass
        
        self.beauty = int(self.shengmu.yuanmao*0.1) + renpy.random.randint(-20, 20)
        if self.beauty < 0:
            self.beauty = 0
        elif self.beauty > 100:
            self.beauty = 100
        else:
            pass
        
        self.iq = self.shengmu.book*0.5 + self.shengmu.lucky*0.5 + renpy.random.randint(-20, 20)
        if self.iq < 0:
            self.iq = 0
        elif self.iq > 100:
            self.iq = 100
        else:
            pass
        self.iq = int(self.iq)
        
        self.wen = 0
        self.wu = 0
        self.duli = renpy.random.randint(30, 70)
        self.qinmian = renpy.random.randint(30, 70)
        
        self.pingjia = ""
        
        self.like = 0
        
        self.hdlike = int(self.shengmu.love*0.3 + self.beauty*0.2)


    def Kids_fenghao(self):
        if self.fenghao == "{color=#FF3030}皇太子{/color}":
            pass
        elif self.wen + self.wu + self.hdlike > 250 or self.hdlike > 80:
            if self.sex == "皇子":
                self.fenghao = "{color=#EE00EE}亲王{/color}"
            else:
                if len(hime_hao) == 0:
                    self.fenghao ="{color=#EE00EE}"+ renpy.random.choice(hime_hao1) + renpy.random.choice(hime_hao2) + "公主{/color}"
                else:
                    self.fenghao = renpy.random.choice(hime_hao)
                    hime_hao.remove(self.fenghao)
                    self.fenghao ="{color=#EE00EE}" + self.fenghao + "公主{/color}"
        
        else:
            if self.sex == "皇子":
                self.fenghao = "{color=#0040FF}郡王{/color}"
            else:
                self.fenghao = "{color=#0040FF}"+renpy.random.choice(hime_hao1) + renpy.random.choice(hime_hao2) + "公主{/color}"
        
        return self.fenghao

    def Kids_hunpei(self):
        if self.hdlike > 80:
            templist = [0,0,0,1,1,1,1,2,2,3,3]
        elif self.mother.love > 80:
            templist = [0,0,1,1,2,2,3,3,4]
        elif self.wen +self.wu +self.iq>= 250:
            templist = [0,1,1,2,2,2,2,3,3,3,3,3,3,4,4,5,999]
        else:
            templist = [1,2,2,2,3,3,3,3,4,4,4,4,4,5,6,999]
        
        list = []
        daixuan_nvxu = []
        for i in guanyuan_list:
            if i.marry == False:
                daixuan_nvxu.append(i)
        if self.sex == "皇子" and len(daixuan_erxi)>0:
            temp = renpy.random.choice(daixuan_erxi)
            list.append(temp)
            templist = renpy.random.sample(templist,2)
        elif self.sex == "公主" and len(daixuan_nvxu)>0:
            temp = renpy.random.choice(daixuan_nvxu)
            list.append(temp)
            templist = renpy.random.sample(templist,2)
        else:
            templist = renpy.random.sample(templist,3)
        
        for i in templist :
            if self.sex == "皇子":
                a = factory.instantiation_Feizi()
                Erxi_random(a,i)
                daixuan_erxi.append(a)
            
            else:
                a = Malesfactory.instantiation_Males()
                Nvxu_random(a,i)
            list.append(a)
        return list

    def Kids_hunpei_HD(self):
        if self.hdlike > 80:
            templist = [0,0,0,1,1,1,1,2,2,3,3]
        elif self.mother.love > 80:
            templist = [0,0,1,1,2,2,3,3,4]
        elif self.wen +self.wu +self.iq>= 250:
            templist = [0,1,1,2,2,2,2,3,3,3,3,3,3,4,4,5,9]
        else:
            templist = [1,2,2,2,3,3,3,3,4,4,4,4,4,5,6,9]
        tempnum = renpy.random.choice(templist)
        daixuan_nvxu = []
        for i in guanyuan_list:
            if i.marry == False:
                daixuan_nvxu.append(i)
        if self.sex == "皇子":
            if len(daixuan_erxi) == 0 or self.hdlike > 80 or self.mother.love > 80:
                lucky = 0
            else:
                lucky = renpy.random.randint(0,1)
            if lucky == 0:
                a = factory.instantiation_Feizi()
                Erxi_random(a,tempnum)
            else:
                a = renpy.random.choice(daixuan_erxi)
                daixuan_erxi.remove(a)
        
        else:
            if len(daixuan_nvxu) == 0 or self.hdlike > 80 or self.mother.love > 80:
                lucky = 0
            else:
                lucky = renpy.random.randint(0,1)
            if lucky == 0:
                a = Malesfactory.instantiation_Males()
                Nvxu_random(a,tempnum)
            else:
                a = renpy.random.choice(daixuan_nvxu)
                daixuan_nvxu.remove(a)
            a.marry = True
            a.qizi =  self
        self.zheng = a
        self.plan = "顺其自然"
        if self.sex == "公主":
            tempstory =str(year)+"年"+str(month)+"月，下嫁于"+str(guanwei[a.level]) + str(a.duty)+str(a.name)+"，封为"+str(self.fenghao)+"。\n"
            self.story.append(tempstory)
        else:
            tempstory =str(year)+"年"+str(month)+"月，迎娶"+str(a.family) +str(a.name)+"，封为"+str(self.fenghao)+"。\n"
            self.story.append(tempstory)






    def Nvxu_random(self,how):
        self.xing = renpy.random.choice(xing_list)
        self.ming = renpy.random.choice(malename_list)+renpy.random.choice(malename2_list)
        self.name = self.xing+self.ming
        self.marry = False
        self.face = 0
        self.beauty = renpy.random.randint(0,100)
        if how == 0:
            self.age = renpy.random.randint(14,25)
            self.level = 0
            self.duty = renpy.random.choice(["国公","国公之子","国公之侄","国公之孙","国侯","国侯之子","国侯之侄","国侯之孙"])
            
            self.shou = renpy.random.randint(self.age+10,100)
        elif 1 <= how <= 6:
            self.age = renpy.random.randint(18,45)
            self.level = how  
            self.duty = renpy.random.choice(["文官","武官"])
            guanyuan_list.append(self)
        else:
            self.age = renpy.random.randint(18,45)
            self.familylevel = 0
            if self.age >= 25:
                self.duty = renpy.random.choice(["异国王","异国王","异国王","异国王","异国王子"])
            else:
                self.duty  = renpy.random.choice(["异国王","异国王子","异国王子","异国王子","异国王子"])
        
        self.zhong = renpy.random.randint(0,100)  
        self.neng = renpy.random.randint(0,100)  
        self.shili = (11 - self.level)*renpy.random.randint(1,10) *0.1 + renpy.random.randint(-10,10) + self.neng  
        self.exp = renpy.random.randint(-20,20)   
        self.feizi = []
        self.zhichi = None
        self.friends = []
        self.foes = []
        self.marry = False
        self.qizi = None
        self.qieshi = []

    def Erxi_random(self,how):
        randomname(self)
        self.AP = 5
        self.age = renpy.random.randint(15,18)
        self.face = 0
        self.year = 0
        self.tags = []
        self.state = "寻常"
        self.palace = " "
        self.health = renpy.random.randint(350, 920)
        self.dance = renpy.random.randint(0, 90)
        self.book = renpy.random.randint(0, 90)
        self.battle = 0
        self.medic = 0
        self.muzic = renpy.random.randint(0, 90)
        self.cixiu = renpy.random.randint(0, 90)
        self.xingge = renpy.random.choice(["活泼","温婉","圆滑","安静","清冷","娇纵","势利"])
        self.xinji = renpy.random.randint(0, 999)
        self.xinji1 = False
        self.huaiyun = 0
        self.lucky = renpy.random.randint(20, 80)
        self.jinzu = 0
        
        if self.xingge == "活泼" :
            self.qingxiang = renpy.random.randint(10, 60)
        elif self.xingge == "温婉":
            self.qingxiang = renpy.random.randint(20, 60)
        elif self.xingge == "圆滑":
            self.qingxiang = renpy.random.randint(30, 80)
        elif self.xingge == "安静":
            self.qingxiang = renpy.random.randint(20, 70)
        elif self.xingge == "清冷":
            self.qingxiang = renpy.random.randint(10, 50)
        elif self.xingge == "娇纵":
            self.qingxiang = renpy.random.randint(40, 90)
        elif self.xingge == "势利":
            self.qingxiang = renpy.random.randint(60, 100)
        else:
            self.qingxiang = renpy.random.randint(0, 100)
        
        
        
        Erxifamily(self,how)
        self.makelucky = renpy.random.randint(1000,1500) + self.familylevel*renpy.random.randint(70,100)
        
        randomshuxing(self)
        self.beauty += 200
        if self.beauty >= 1000:
            self.beauty = 1000
        
        
        
        
        self.love = 0
        self.taihoulike = (self.beauty +self.meili+self.qizhi)/250 - self.familylevel/4


    def Erxifamily(self,how):
        self.father = None
        self.jiazu = []
        if how == 9:
            lucky = renpy.random.randint(0, 1)
            if lucky == 0:
                pass
            else:
                self.xing = renpy.random.choice(['阿史那', '赫连',"耶律","郁久闾"])
            self.name = self.xing + self.ming
            self.familylevel = 0
            self.fatherduty = "国王"
            self.family = "和亲公主"
            self.familylocation = renpy.random.choice(['嫡女', '庶女'])
            self.tags.append(tags_family[0])
            Creat_Males(whose = self,how = 10)
        
        else:
            tempnum = 10
            lucky = renpy.random.randint(1, 60)
            self.fatherduty = renpy.random.choice(['文官', '武将'])
            if lucky < 10:
                self.familylocation = "庶女"
            elif lucky < 20:
                self.familylocation = "侄女"
                tempnum = 13
            elif lucky < 30 :
                self.familylocation = "孙女"
                tempnum = 12
            elif lucky < 40 :
                self.familylocation = "之妹"
                tempnum = 11
            else:
                self.familylocation = "嫡女"
            if how == 1:
                self.familylevel = 1
                self.family = "一品" + self.fatherduty + self.familylocation
                self.tags.append(tags_family[1])
            elif how == 2:
                self.familylevel = 2
                self.family = "二品" + self.fatherduty + self.familylocation
                self.tags.append(tags_family[1])
            elif how == 3:
                self.familylevel = 3
                self.family = "三品" + self.fatherduty + self.familylocation
                self.tags.append(tags_family[1])
            elif how == 4:
                self.familylevel = 4
                self.family = "四品" + self.fatherduty + self.familylocation
            elif how == 5:
                self.familylevel = 5
                self.family = "五品" + self.fatherduty + self.familylocation
            elif how == 6:
                self.familylevel = 6
                self.family = "六品" + self.fatherduty + self.familylocation
            else:
                lucky = renpy.random.randint(0, 1)
                if lucky == 0:
                    pass
                else:
                    self.xing = renpy.random.choice(['阿史那', '赫连',"耶律","郁久闾"])
                self.name = self.xing + self.ming
                self.familylevel = 0
                self.fatherduty = "国王"
                self.family = "和亲公主"
                self.tags.append(tags_family[0])
                Creat_Males(whose = self,how = 10)
            
            Creat_Males(whose = self,how = tempnum)




label 召见子嗣(kid):
    scene 寝居
    show 孩子 at chara
    if kid.age < 1:
        $ kid.like = kid.like + 0.5
        if kid.health < 20:
            "[kid.cheng] [kid.name]" "（被乳娘抱着来到你的面前，眼睛眯着缝，看起来有些萎靡不振。）"
            "乳娘" "[my.cheng]，[kid.cheng]幼小体弱，太医说需要多补补身子。"
            我 "知道了，把[kid.cheng]抱下去吧。"
            hide 孩子
        elif kid.xingge == "外向":
            "[kid.cheng] [kid.name]" "（被乳娘抱着来到你的面前，一看到你便兴奋得哇哇直叫。）"
        elif kid.xingge == "中庸":
            "[kid.cheng] [kid.name]" "（被乳娘抱着来到你的面前，咿咿呀呀，手舞足蹈，看起来煞是可爱。）"
        else:
            "[kid.cheng] [kid.name]" "（被乳娘抱着来到你的面前，看到你，一双大眼睛怯生生的。）"
    elif kid.age < 5:
        if my.level == 0:
            $ cheng = "母后"
        else:
            $ cheng = "母妃"
        if kid.health < 20:
            "[kid.cheng] [kid.name]" "咳咳……儿臣参见[cheng]……"
        elif kid.iq > 80:
            "[kid.cheng] [kid.name]" "……诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也……（放下手里的书册）[cheng]，儿臣参见[cheng]！"
        elif kid.iq < 20:
            if my.level == 0:
                "[kid.cheng] [kid.name]" "母吼！母吼！鹅臣饿了，次糖糖！次肉肉！"
            else:
                "[kid.cheng] [kid.name]" "母灰！母灰！鹅臣饿了，次糖糖！次肉肉！"
        elif kid.xingge == "外向":
            "[kid.cheng] [kid.name]" "（笑嘻嘻地拉着你的手）[cheng][cheng]，陪儿臣到院子里玩会儿吧！"
        elif kid.xingge == "中庸":
            "[kid.cheng] [kid.name]" "[cheng]，今天儿臣学了一首诗，让儿臣念给你听吧！"
        else:
            "[kid.cheng] [kid.name]" "[cheng]，儿臣想听您讲故事。"
    else:
        if my.level == 0:
            $ cheng = "母后"
        else:
            $ cheng = "母妃"
        "[kid.cheng] [kid.name]" "儿臣参见[cheng]。"
        menu:
            "闲聊":

                $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    if kid.xingge == "外向":
                        menu:
                            "[kid.cheng] [kid.name]" "[cheng]，儿臣今天在回宫的路上碰到父皇了，儿臣本想同他多聊几句，父皇却说有事要忙，是因为儿臣话太多了吗？"
                            "或许是，以后要稍微收敛一些":
                                $ kid.duli = kid.duli + 1
                                "[kid.cheng] [kid.name]" "[cheng]，儿臣今天在回宫的路上碰到父皇了，儿臣本想同他多聊几句，父皇却说有事要忙，是因为儿臣话太多了吗？"
                            "定然不是，父皇只是政务繁忙":
                                $ kid.qinmian=kid.qinmian + 1
                                "[kid.cheng] [kid.name]" "那儿臣也要好好用功，希望以后能够为父皇和[cheng]分忧。"
                    elif kid.xingge == "中庸":
                        "[kid.cheng] [kid.name]" "[cheng]，儿臣今天在回宫的路上碰到父皇了，儿臣同父皇聊了好一会儿，父皇看起来心情不错，还说得空便来[cheng]这里。"
                    else:
                        menu:
                            "[kid.cheng] [kid.name]" "[cheng]，儿臣今天在回宫的路上碰到父皇了，父皇问儿臣话，儿臣有些紧张，没有回答好，父皇似乎不太高兴……"
                            "下次好好回父皇的话":
                                $ kid.duli = kid.duli + 1
                                "[kid.cheng] [kid.name]" "[cheng]，儿臣、儿臣知道，儿臣会尽力的！"
                            "父皇知道你的性子，不会放在心上":
                                $ kid.qinmian=kid.qinmian + 1
                                "[kid.cheng] [kid.name]" "若真是如此就好，儿臣不善言辞，只能读书多刻苦些，希望父皇和[cheng]不会嫌弃儿臣。"
                elif lucky == 1:
                    if kid.xingge == "外向" and kid.duli > 70:
                        "[kid.cheng] [kid.name]" "儿臣喜欢同人说话，也喜欢同别人一起做事。"
                    elif kid.xingge == "中庸" and kid.duli > 70:
                        "[kid.cheng] [kid.name]" "儿臣认为，想要成为人上人，便不得甘于平庸、泯然众人。"
                    elif kid.xingge == "内向" and kid.duli <30:
                        "[kid.cheng] [kid.name]" "[cheng]，您找儿臣？太好了……儿臣能在您这儿多待一会儿吗啊？"
                    elif kid.duli>50:
                        "[kid.cheng] [kid.name]" "[cheng]得空了可否多陪陪儿臣呢？"
                    else:
                        "[kid.cheng] [kid.name]" "[cheng]，有事找儿臣吗？……哦，没有，只是儿臣今天遇到些烦心事儿，想自己待会儿。"
                elif lucky == 2:
                    if kid.qinmian > 70:
                        menu:
                            "[kid.cheng] [kid.name]" "参见[cheng]，请[cheng]恕罪，儿臣方才看书入迷，一时没有听见您的传召。"
                            "爱看书是好事，但不要看书成痴":
                                $ kid.duli = kid.duli + 1
                                "[kid.cheng] [kid.name]" "读万卷书，行万里路，儿臣明白。"
                            "你如此勤奋，[cheng]欣慰":
                                $ kid.qinmian=kid.qinmian + 1
                                "[kid.cheng] [kid.name]" "书上说，业精于勤，荒于嬉；行成于思，毁于随。"
                    elif kid.qinmian < 30 and kid.plan == "勤学苦练":
                        "[kid.cheng] [kid.name]" "（小脸儿瘪着，一脸苦相）儿臣好累，儿臣不想学习……"
                    elif kid.qinmian < 30:
                        menu:
                            "[kid.cheng] [kid.name]" "（衣角脏乱，发丝上挂着汗珠）参见[cheng]，儿臣方才在后院同几个丫头玩蹴鞠呢！"
                            "小心不要受伤了":
                                $ kid.duli = kid.duli + 1
                                "[kid.cheng] [kid.name]" "[cheng]放心，儿臣可厉害啦，怎么会受伤呢！嘻嘻，要是能不去上学、玩一整天就更好啦！"
                            "玩乐适度，不要荒废了学业":
                                $ kid.qinmian=kid.qinmian + 1
                                "[kid.cheng] [kid.name]" "[cheng]放心，儿臣可厉害啦，怎么会受伤呢！嘻嘻，要是能不去上学、玩一整天就更好啦！"
                    else:
                        "[kid.cheng] [kid.name]" "[cheng]问儿臣最近学业如何？"
                        "[kid.cheng] [kid.name]" "儿臣一直谨遵先生的教诲，循序渐进，[cheng]不必担心。"
                elif lucky == 3:
                    if kid.wen > 70:
                        "[kid.cheng] [kid.name]" "子用私道者家必乱，臣用私义者国必危。书中所言，字字珠玑。"
                    elif kid.wen < 30 and kid.iq < 30:
                        menu:
                            "[kid.cheng] [kid.name]" "儿臣今日下学时听见师傅在同别人说话，说儿臣天生愚钝，朽木不可雕也……"
                            "这是为师者的无能！":
                                $ kid.duli = kid.duli + 1
                                "[kid.cheng] [kid.name]" "真的么？儿臣真的不比别人差吗？"
                            "勤能补拙，你更要好好学习":
                                $ kid.qinmian=kid.qinmian + 1
                                "[kid.cheng] [kid.name]" "儿臣会的……（脸上的落寞却加深了几分）"
                    else:
                        "[kid.cheng] [kid.name]" "儿臣对那些诗书啊、史记啊并没有太大的兴趣，只是按照先生的吩咐在修习罢了。"
                else:
                    if kid.wu > 70 and kid.sex == "皇子" and kid.xingge == "外向":
                        "[kid.cheng] [kid.name]" "儿臣空有一身武艺，却不能驰骋沙场，这种感觉真是叫人难受！"
                    elif kid.wu > 70 and kid.sex == "皇子" and kid.xingge == "中庸":
                        "[kid.cheng] [kid.name]" "儿臣虽擅长武艺，但儿臣更希望这世道能让儿臣永无用武之地。"
                    elif kid.wu > 70 and kid.sex == "皇子" and kid.xingge == "内向":
                        "[kid.cheng] [kid.name]" "先生说儿臣武艺出众？儿臣自己倒不这么觉得。"
                    elif kid.wu < 30 and kid.sex == "皇子":
                        "[kid.cheng] [kid.name]" "儿臣实在不喜欢舞枪弄剑。"
                    elif kid.sex == "皇子":
                        "[kid.cheng] [kid.name]" "儿臣对习武练兵并没有太大的兴趣，只是按照先生的吩咐在练习罢了。"
                    elif kid.wu > 70 and kid.sex == "公主":
                        "[kid.cheng] [kid.name]" "儿臣身为公主，定然要善才多艺，才能不丢了父皇和[cheng]的颜面。"
                    elif kid.wu < 30 and kid.sex == "公主":
                        "[kid.cheng] [kid.name]" "儿臣实在不喜欢那劳什子的琴棋书画，无趣的很。"
                    else:
                        "[kid.cheng] [kid.name]" "儿臣对琴棋书画并没有太大的兴趣，只是按照先生的吩咐在练习罢了。"

                $ kid.like = kid.like + 0.5
            "勉励":
                if kid.qinmian < 30:
                    "[kid.cheng] [kid.name]" "（皱着眉头）是，儿臣知道。"
                    $ kid.like = kid.like - 0.5
                    $ kid.qinmian = kid.qinmian + 0.5
                else:
                    "[kid.cheng] [kid.name]" "是，儿臣知道。"

                $ kid.like = kid.like - 0.5
                $ kid.qinmian = kid.qinmian + 0.5
                $ kid.duli = kid.duli + 1
            "表扬":
                "[kid.cheng] [kid.name]" "儿臣多谢[cheng]夸奖！"

                $ kid.like = kid.like + 1
                $ kid.qinmian = kid.qinmian - 1
                $ kid.duli = kid.duli - 1
            "训诫":
                "[kid.cheng] [kid.name]" "儿臣……儿臣知错了，儿臣会谨记[cheng]的教诲。"

                $ kid.like = kid.like - 1
                $ kid.qinmian = kid.qinmian + 2
                $ kid.duli = kid.duli - 1
            "责备":
                if kid.xingge == "外向":
                    "[kid.cheng] [kid.name]" "（一脸惶恐委屈）儿臣做错了什么让[cheng]如此生气？"
                elif kid.xingge == "中庸":
                    "[kid.cheng] [kid.name]" "（一脸惶恐委屈）儿臣知错了，还请[cheng]不要生气！"
                else:
                    "[kid.cheng] [kid.name]" "（一脸惶恐委屈）母、[cheng]……你不要这样，儿臣害怕……"

                $ kid.like = kid.like - 2
                $ kid.qinmian = kid.qinmian + 5
                $ kid.duli = kid.duli + 2

    $ AP = AP - 1
    $ timenum = timenum + 1
    jump 寝居界面






screen kids(list):
    $ next_kids_page = kids_page + 1
    $ prev_kids_page = kids_page - 1
    $ max_kids_page = int(math.modf(len(list)/4)[1])
    $ b = kids_page*4+4
    $ c = list[next_kids_page*4:next_kids_page*4+4]


    if b >= len(list):
        $ b = len(list)
    else:
        pass


    frame:
        xysize (1400,800)
        align (0.5,0.5)

        hbox xpos 0.05 yalign 0.0 spacing 10:
            for i in list[kids_page*4:b]:
                python:
                    health = int(i.health)
                    beauty = int(i.beauty)
                    wen = int(i.wen)
                    wu = int(i.wu)
                    duli = int(i.duli)
                    qinmian = int(i.qinmian)
                    like = int(i.like)
                    neng = int(i.nengli)

                fixed xmaximum 330 ymaximum 750:
                    vbox xysize (188,263):
                        add "images/Kid/[i.face].webp" maxsize (188,263) align (0.5,1.0)
                    vbox ypos 0.36 spacing 3:
                        if i.mother == my:
                            text "{color=#DF013A}[i.cheng] [i.name]" align (0.5,0.5)
                        else:
                            text "[i.cheng] [i.name]" align (0.5,0.5)

                        if i.live == 1 or i == taizi:

                            if i.sex == "皇子" and i.live == 1:
                                textbutton "{size=35}已离宫" align (0.5,0.5)
                                text "{size=25}[i.fenghao]（配偶:"+i.zheng.family+i.zheng.name+"）"
                            elif i == taizi:
                                text "{size=25}[i.fenghao]"
                                if i.live == 1:
                                    textbutton "{size=35}已离宫" align (0.5,0.5)
                                    text "{size=25}[i.fenghao]（配偶:"+i.zheng.family+i.zheng.name+"）"
                            else:

                                text "{size=25}[i.fenghao]（配偶:"+guanwei[i.zheng.level] + i.zheng.duty+i.zheng.name+"）"
                        elif i.live == -1:
                            textbutton "{size=35}已离世" align (0.5,0.5)
                        elif timenum != 5 and  i.plan == "休息玩乐":
                            textbutton "{size=35}召见" align (0.5,0.5) action Hide("kids"),Call("召见子嗣",kid = i)
                        elif i.age >= 5 and timenum <= 3:
                            textbutton "{size=35}上课中" align (0.5,0.5)
                        elif timenum == 5:
                            textbutton "{size=35}已歇息" align (0.5,0.5)
                        elif i.mother != my and my.level != 0:
                            textbutton "{size=35}召见" align (0.5,0.5)
                        else:
                            textbutton "{size=35}召见" align (0.5,0.5) action Hide("kids"),Call("召见子嗣",kid = i)
                        textbutton "{size=35}记事" align (0.5,0.5) action ToggleScreen("KidStory", kid = i)
                        text "{size=25}年龄:[i.age]岁" align (0.0,0.5)
                        text "{size=25}状态:[i.state]" align (0.0,0.5)

                        text "{size=25}母妃:[i.mother.hao][i.mother.weifen][i.mother.name]" align (0.0,0.5)




                        text "{size=25}体质:[health]  容貌:[beauty]" align (0.0,0.5)
                        if i.sex == "皇子":
                            text "{size=25}学识:[wen]  武艺:[wu]" align (0.0,0.5)
                        else:
                            text "{size=25}学识:[wen]  才艺:[wu]" align (0.0,0.5)




                        if i.age >= 5:
                            text "{size=25}性格:[i.xingqing]" align (0.0,0.5)
                            text "{size=25}评价:[i.pingjia]" align (0.0,0.5)

                        else:
                            text "{size=25}性格:[i.xingge]" align (0.0,0.5)
                            text "{size=25}评价:暂无" align (0.0,0.5)
                        if persistent.ycsz == False:
                            text "{size=25}天资:"+str(int(i.iq)) +"  能力:[neng]" align (0.0,0.5)
                            text "{size=25}器重:"+str(int(i.hdlike)) +"  势力:"+str(int(i.shili)) align (0.0,0.5)

                        else:
                            pass
                        if i.age >= 5  and i.live == 0:
                            text "{size=25}培养方式:[i.plan]"
                        if i.age >= 5  and i.live == 0 and i.mother == my and timenum == 1 or i.age >= 5  and i.live == 0 and my.level == 0 and timenum == 1:
                            if i.plan == "顺其自然":
                                textbutton "{size=30}修改" align (1.0,0.5) action SetField(i,"plan","勤学苦练")
                            elif i.plan == "勤学苦练":
                                textbutton "{size=30}修改" align (1.0,0.5) action SetField(i,"plan","重在实践")
                            elif i.plan == "重在实践":
                                textbutton "{size=25}修改" align (1.0,0.5) action SetField(i,"plan","休息玩乐")
                            else:
                                textbutton "{size=30}修改" align (1.0,0.5) action SetField(i,"plan","顺其自然")
                        else:
                            pass
        hbox align (0.5,1.0):
            if kids_page > 0:
                textbutton "上一页" action SetVariable('kids_page', prev_kids_page)
            textbutton "我的" action SetVariable('kids_page', 0),Show("kids",list = my.kids)
            textbutton "全部" action SetVariable('kids_page', 0),Show("kids",list = NPC_Kids_list)
            if kids_page < max_kids_page and max_kids_page > 1 and len(c)>0:
                textbutton "下一页" action SetVariable('kids_page', next_kids_page)
        textbutton "关闭":
            align (1.0,1.0)
            action Hide("kids"),Show("myroom")

screen KidStory(kid):
    default textlist = ""
    add "gui/frame.webp" zoom 1.2 xalign 0.5 yalign 0.5
    viewport:
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        xsize 950
        ysize 600
        align (0.5,0.5)
        has vbox
        for i in kid.story:
            $ textlist = textlist + i
            text i:

                size 22
                font "问藏书房.ttf"
    textbutton "{size=20}{font=问藏书房.ttf}复制" align (0.82,0.7) action Function(scrubs, textlist)
    imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
        align (0.85,0.85)
        action Hide("KidStory")


screen Hunpei(list, sex):
    frame:
        xysize (1280,720)
        align (0.5,0.5)
        if sex == "皇子":
            hbox spacing 50 align (0.5,0.5):
                for i in list:
                    vbox spacing 25:
                        text "姓名："+i.name
                        text "年龄："+str(int(i.age))
                        text "身份："+i.family
                        text "容貌："+str(int(i.beauty*0.1))
                        text "性格："+i.xingge
                        textbutton "选定" action SetVariable("who",i),Hide("Hunpei"),Return()
        else:
            hbox spacing 50 align (0.5,0.5):
                for i in list:
                    vbox spacing 25:
                        text "姓名："+i.name
                        text "年龄："+str(i.age)
                        text "身份："+guanwei[i.level] + i.duty
                        text "容貌："+str(int(i.beauty))
                        text "能力："+str(int(i.neng))
                        textbutton "选定" action SetVariable("who",i),Hide("Hunpei"),Return()




label 皇嗣婚配:
    python:
        kehunpei = []
        if my.level == 0:
            for i in NPC_Kids_list:
                if i.age >= 15 and i.live == 0:
                    kehunpei.append(i)
                else:
                    pass
        elif my.level < 4:
            for i in my.kids:
                if i.age >= 15 and i.live == 0:
                    kehunpei.append(i)
                else:
                    pass
        else:
            pass
    if len(kehunpei) == 0:
        "当前尚无可婚配皇嗣。"
        jump 寝居界面
    else:
        menu:
            "当宫中尚未婚配的皇嗣超过六位，需优先为前六位皇嗣赐婚。"
            "[kehunpei[0].cheng] [kehunpei[0].name]" if len(kehunpei)>0:
                $ beihunpei = kehunpei[0]
            "[kehunpei[1].cheng] [kehunpei[1].name]" if len(kehunpei)>1:
                $ beihunpei = kehunpei[1]
            "[kehunpei[2].cheng] [kehunpei[2].name]" if len(kehunpei)>2:
                $ beihunpei = kehunpei[2]
            "[kehunpei[3].cheng] [kehunpei[3].name]" if len(kehunpei)>3:
                $ beihunpei = kehunpei[3]
            "[kehunpei[4].cheng] [kehunpei[4].name]" if len(kehunpei)>4:
                $ beihunpei = kehunpei[4]
            "[kehunpei[5].cheng] [kehunpei[5].name]" if len(kehunpei)>5:
                $ beihunpei = kehunpei[5]
            "再做打算":
                jump 寝居界面
        $ templist = Kids_hunpei(beihunpei)
        $ who = None
        call screen Hunpei(templist,beihunpei.sex)
        $ beihunpei.zheng = who
        $ beihunpei.live = 1
        $ beihunpei.plan = "顺其自然"
        if beihunpei.sex == "公主":
            $ who.marry = True
            $ who.qizi = beihunpei
        else:
            if who in daixuan_erxi:
                $ daixuan_erxi.remove(who)
        $ Kids_fenghao(beihunpei)
        "掖廷的人在上报给皇帝以后便开始着手操办。"
        python:
            if beihunpei.sex == "公主":
                tempstory =str(year)+"年"+str(month)+"月，下嫁于"+str(guanwei[who.level]) + str(who.duty)+str(who.name)+"，封为"+str(beihunpei.fenghao)+"。\n"
                beihunpei.story.append(tempstory)
            else:
                tempstory =str(year)+"年"+str(month)+"月，迎娶"+str(who.family) +str(who.name)+"，封为"+str(beihunpei.fenghao)+"。\n"
                beihunpei.story.append(tempstory)


        $ timenum = timenum +1
        $ AP = AP -1
        jump 寝居界面


screen choicekid(list):
    style_prefix "choice"
    $ next_choice_page = choice_page + 1
    $ prev_choice_page = choice_page - 1
    $ max_choice_page = int(math.modf(len(list)/6)[1])
    $ b = choice_page*6+6
    $ c = list[next_choice_page*6:next_choice_page*6+6]


    if b >= len(list):
        $ b = len(list)
    else:
        pass

    vbox:
        for i in list[choice_page*6:b]:
            textbutton i.cheng+i.name action SetVariable('choice_page', 0),SetVariable("kid",i),Hide("choicekid"),Return()
        if choice_page > 0:
            textbutton "上一页" action SetVariable('choice_page', prev_choice_page)
        if choice_page < max_choice_page and max_choice_page > 1 and len(c)>0:
            textbutton "下一页" action SetVariable('choice_page', next_choice_page)

screen choicekid_dx(list, choicedlist, num):
    style_prefix "choicemianban"
    $ a = (len(list)-1)/3 + 1
    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        align (0.5,0.2)
        xsize 960
        ysize 540
        text "  " align (0.5,0.02)
        vpgrid:
            align (0.5,0.5)
            xsize 940
            ysize 400

            rows a
            cols 3

            draggable True
            mousewheel True
            xspacing 20
            yspacing 35


            for i in list:
                if len(choicedlist) >= num and i not in choicedlist:
                    textbutton "{size=25}"+i.cheng+" "+i.name
                elif i in choicedlist:
                    textbutton "{size=25}"+i.cheng+" "+i.name action RemoveFromSet(choicedlist,i)
                else:
                    textbutton "{color=#B22222}{size=25}"+i.cheng+" "+i.name action AddToSet(choicedlist,i)
            if len(list)-1 - 3*a == 1:
                textbutton ""
            elif len(list)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        if len(choicedlist) == 0:
            pass
        else:
            textbutton "确定":
                align (0.5,1.0)
                action Hide("choicekid_dx"),Return()
init python:
    def guoji(kid,fz):
        if kid not in fz.kids:
            fz.kids.append(kid)
        if kid.mother.love < 0 or fz.love < 0:
            pass
        else:
            kid.hdlike -= kid.mother.love*0.3
            kid.hdlike += fz.love *0.3
        kid.mother = fz
        if kid.hdlike > 0:
            fz.exp += kid.hdlike
        else:
            pass
        fz.yali -= 20
        if kid.mother == kid.shengmu:
            tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(kid.cheng)+(kid.name)+"被送回生母"+str(fz.hao)+(fz.weifen)+str(fz.name)+"名下。\n"
            allstory.insert(0,tempstory2)
            tempstory =str(year)+"年"+str(month)+"月，"+str(kid.cheng)+(kid.name)+"被送回至其名下。\n"
            fz.story.append(tempstory)
            tempstory =str(year)+"年"+str(month)+"月，被送回生母"+str(fz.hao)+(fz.weifen)+str(fz.name)+"名下。\n"
            kid.story.append(tempstory)
        else:
            tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(kid.cheng)+(kid.name)+"被过继到"+str(fz.hao)+(fz.weifen)+str(fz.name)+"名下。\n"
            allstory.insert(0,tempstory2)
            tempstory =str(year)+"年"+str(month)+"月，"+str(kid.cheng)+(kid.name)+"被过继至其名下。\n"
            fz.story.append(tempstory)
            tempstory =str(year)+"年"+str(month)+"月，被过继至"+str(fz.hao)+(fz.weifen)+str(fz.name)+"名下。\n"
            kid.story.append(tempstory)



    def guoji_check(kid,fz):
        if fz.love < 0:
            return False
        elif diwei(fz) > 2:
            return False
        else:
            pass
        tempnum = (kid.mother.level - fz.level) +  (kid.mother.familylevel - fz.familylevel) + (fz.love - kid.mother.love)*0.1
        tempnum -= len(fz.kids)*3
        if fz.year < 5 :
            tempnum -= (5-fz.year)
        else:
            pass
        if fz == my and kid.like < 0:
            return False
        elif fz == my and kid.like > 0:
            tempnum += kid.like*0.1
        else:
            pass
        if tempnum >= 0:
            return True
        else:
            return False


label 皇帝过继子嗣:
    python:
        keguoji = []
        for i in NPC_Kids_list:
            if i.live == 0 and i.shengmu in NPC_fz_list and i.shengmu != i.mother:
                keguoji.append(i)
    if len(keguoji) == 0:
        pass
    else:
        $ kid = renpy.random.choice(keguoji)
        if guoji_check(kid,kid.shengmu) == False:
            pass
        else:
            $ kid.mother.yali += kid.qinzi
            $ kid.shengmu.yali -= 10
            $ guoji(kid,kid.shengmu)
            if fz == my:
                show 我的宫女
                我的宫女 "主子，方才圣宸宫下了旨意，说是……将[kid.cheng][kid.name]送回咱们宫里抚养了！"
                menu:
                    "大喜过望":
                        $ kid.like += 10
                    "知道了":
                        pass
            else:
                show 我的宫女
                我的宫女 "主子，方才圣宸宫下了旨意，说是将[kid.cheng][kid.name]送回[fz.cheng][fz.name]宫里抚养了。"
                menu:
                    "知道了":
                        pass

    python:
        keguoji = []
        for i in NPC_Kids_list:
            if i.live == 0 and i.mother not in NPC_fz_list:
                keguoji.append(i)
        if len(keguoji) == 0:
            templist = []
        else:
            keguoji = sorted(keguoji, key=attrgetter("hdlike"),reverse = True)
            kid = keguoji[0]
            templist = []
            for i in NPC_fz_list:
                if len(i.kids) >= 5 or i.year <= 5 or i.love < 10 or i.familylevel >= 10 or tags[4] in i.tags or havetag("失心成疯",i) == True or jinzu(i) == True or huaiyun(i) == True:
                    pass
                else:
                    templist.append(i)
    if len(templist) == 0:
        pass
    else:
        $ lucky = renpy.random.randint(0, 20)

        if lucky == 0:
            $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
            $ fz = templist[0]
        elif lucky == 1 or lucky == 2:
            $ templist = sorted(templist, key=attrgetter("level"),reverse = False)
            $ fz = templist[0]
        elif lucky == 3 or lucky == 4:
            $ templist = sorted(templist, key=attrgetter("year"),reverse = True)
            $ fz = templist[0]
        elif lucky == 5 or lucky == 6:
            $ templist = sorted(templist, key=attrgetter("familylevel"),reverse = False)
            $ fz = templist[0]
        else:
            $ fz = renpy.random.choice(templist)
        $ guoji(kid,fz)
        if fz == my:
            show 我的宫女
            我的宫女 "主子，方才圣宸宫下了旨意，说是将[kid.cheng][kid.name]送到咱们宫里由您抚养呢！"
            menu:
                "知道了":
                    pass
        else:
            show 我的宫女
            我的宫女 "主子，方才圣宸宫下了旨意，说是将[kid.cheng][kid.name]送到[fz.cheng][fz.name]宫里抚养了。"
            menu:
                "知道了":
                    pass
    python:
        renpy.return_statement()

label 皇帝归还子嗣:
    python:
        keguoji = []
        for i in NPC_Kids_list:
            if i.live == 0 and i.shengmu in NPC_fz_list and i.shengmu != i.mother:
                keguoji.append(i)
    if len(keguoji) == 0:
        pass
    else:
        $ kid = renpy.random.choice(keguoji)
        if guoji_check(kid,kid.shengmu) == False:
            pass
        else:
            $ kid.mother.yali += kid.qinzi
            $ kid.shengmu.yali -= 10
            $ guoji(kid,kid.shengmu)
            if fz == my:
                show 我的宫女
                我的宫女 "主子，方才圣宸宫下了旨意，说是……将[kid.cheng][kid.name]送回咱们宫里抚养了！"
                menu:
                    "大喜过望":
                        $ kid.like += 10
                    "知道了":
                        pass
            else:
                show 我的宫女
                我的宫女 "主子，方才圣宸宫下了旨意，说是将[kid.cheng][kid.name]送回[fz.cheng][fz.name]宫里抚养了。"
                menu:
                    "知道了":
                        pass



    python:
        renpy.return_statement()



label 子嗣过继:
    python:
        keguoji = []
        for i in NPC_Kids_list:
            if i.live == 0 and i.mother not in NPC_fz_list:
                keguoji.append(i)
    if len(keguoji) == 0:
        "暂无可过继皇嗣。"
        jump 寝居界面

    call screen choicekid(keguoji)
    if my.level == 0:
        "要向皇上请求将[kid.name]过继到哪位嫔妃膝下？"
        call screen choicefz(NPC_fz_list)
        if fz == my:
            menu:
                "要向皇上请求将[kid.name]过继到自己膝下吗？"
                "请求过继":
                    if guoji_check(kid,fz) == True:
                        $ guoji(kid,fz)
                        "片刻后，宫人回禀，皇上已经同意将[kid.cheng]过继到你膝下。"
                    else:
                        "片刻后，宫人回禀，皇上认为此事还需从长计议。"
                    $ AP -= 1
                    $ timenum += 1
                    jump 寝居界面
        else:
            menu:
                "要向皇上请求将[kid.name]过继到[fz.cheng]膝下吗？"
                "请求过继":
                    if guoji_check(kid,fz) == True:
                        $ guoji(kid,fz)
                        "片刻后，宫人回禀，皇上已经同意将[kid.cheng]过继到[fz.cheng]膝下。"
                        "而[fz.cheng]因此对你感恩戴德。"
                        $ fz.like += 20
                    else:

                        "片刻后，宫人回禀，皇上认为此事还需从长计议。"
                    $ AP -= 1
                    $ timenum += 1
                    jump 寝居界面
                "再做打算":

                    jump 寝居界面
    else:
        menu:
            "要向皇上请求将[kid.name]过继到自己膝下吗？"
            "请求过继":
                if guoji_check(kid,my) == True:
                    $ guoji(kid,my)
                    "片刻后，宫人回禀，皇上已经同意将[kid.cheng]过继到你膝下。"
                else:

                    "片刻后，宫人回禀，皇上认为此事还需从长计议。"
                $ AP -= 1
                $ timenum += 1
                jump 寝居界面
            "再做打算":
                jump 寝居界面

label 子嗣演变:
    python:
        for i in NPC_Kids_list:
            if i.live == -1:
                pass
            else:
                if i.health <= 0:
                    tempstory = str(year)+"年"+str(month)+"月，因身体虚弱病故。\n"
                    tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+str(i.cheng)+str(i.name)+ "因身体虚弱病故。\n"
                    allstory.insert(0,tempstory2)
                    i.story.append(tempstory)
                    i.live = -1
                    i.mother.yali += 30
                    i.shengmu.yali += 30
                    if i == taizi:
                        taizi = None
                    
                    renpy.call("皇嗣去世",kid = i,from_current=False)
                elif i.age > i.shou:
                    tempstory = str(year)+"年"+str(month)+"月，寿终正寝。\n"
                    tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+str(i.cheng)+str(i.name)+ "寿终正寝。\n"
                    allstory.insert(0,tempstory2)
                    i.story.append(tempstory)
                    i.live = -1
                    i.mother.yali += 20
                    i.shengmu.yali += 20
                    if i == taizi:
                        taizi = None
                    renpy.call("皇嗣寿终正寝",kid = i,from_current=False)
                elif i.state == "抱恙" :
                    lucky = renpy.random.randint(0,4)
                    if lucky == 0 or i.health >= 80:
                        i.state = "寻常"
                        if i.mother == my and i.live == 0:
                            renpy.call("皇嗣康复",kid = i,from_current=False)
                        else:
                            if i.plan == "休息玩乐":
                                i.plan = "顺其自然"
                elif  i.state == "病重":
                    lucky = renpy.random.randint(0,12)
                    if lucky == 0 or i.health >= 90:
                        i.state = "寻常"
                        if i.mother == my and i.live == 0:
                            renpy.call("皇嗣康复",kid = i,from_current=False)
                        else:
                            if i.plan == "休息玩乐":
                                i.plan = "顺其自然"
                else:
                    lucky = renpy.random.randint(0,int(i.health*10+200))
                    if lucky <= 1 and i.health < 90:
                        i.state = "病重"
                        if i.mother == my and i.live == 0:
                            renpy.call("皇嗣生病",kid = i,zhong = True,from_current=False)
                        else:
                            i.plan = "休息玩乐"
                    elif lucky <= 4 and i.health < 80:
                        i.state = "抱恙"
                        if i.mother == my and i.live == 0:
                            renpy.call("皇嗣生病",kid = i,zhong = False,from_current=False)
                        else:
                            i.plan = "休息玩乐"
                    else:
                        pass
                
                if i.age < 3 or i.live == -1:
                    pass
                elif i.live == 1 :
                    tempnum = int(100 - i.qingxiang)
                    if tempnum <= 0:
                        tempnum = 1
                    lucky =  renpy.random.randint(0,tempnum)
                    if lucky == 0:
                        i.shili += i.nengli *0.001 + i.qingxiang*0.001
                else:
                    i.wen = i.wen + i.iq*0.001 + i.qinmian*0.001
                    i.wu = i.wu  + i.iq*0.001 + i.qinmian*0.001
                    i.duli = i.duli + renpy.random.randint(-2,2)*0.1
                    i.qinmian = i.qinmian + renpy.random.randint(-2,2)*0.1
                
                if i.plan == "顺其自然":
                    if i.state == "抱恙":
                        i.health = i.health - renpy.random.randint(2,4)
                    elif i.state == "病重":
                        i.health = i.health - renpy.random.randint(3,5)
                    else:
                        pass
                    if i.age < 5:
                        if i.mother == my:
                            i.health = i.health + renpy.random.randint(-1,1)*0.1
                            i.like = i.like + renpy.random.randint(1,2)*0.1
                        else:
                            pass
                    else:
                        i.health = i.health + renpy.random.randint(-1,2)*0.1
                        lucky = renpy.random.randint(0,100)
                        if lucky < i.qinmian:
                            if i.health >= 75:
                                templist = ["武"]
                            elif i.health <= 25:
                                templist = ["文"]
                            else:
                                templist =  []
                            if i.xingge == "外向":
                                templist.append(["文","文","武","武","武"])
                            elif i.xingge == "内向":
                                templist.append(["文","文","文","武","武"])
                            else:
                                templist.append(["文","文","武","武"])
                            lucky = renpy.random.choice(templist)
                            if lucky == "文":
                                i.wen = i.wen + i.iq*0.003
                            else:
                                i.wu = i.wu  + i.iq*0.003
                        
                        else:
                            lucky = renpy.random.randint(0,100)
                            if lucky < i.qingxiang:
                                i.nengli += i.duli*0.003
                            else:
                                i.health = i.health + renpy.random.randint(-1,2)*0.1
                        i.duli = i.duli + renpy.random.randint(-2,2)*0.1
                        i.qinmian = i.qinmian + renpy.random.randint(-2,2)*0.1
                        if i.mother == my:
                            i.like = i.like + renpy.random.randint(1,2)*0.1
                        else:
                            pass
                elif i.plan == "勤学苦练":
                    if i.state == "抱恙":
                        i.health = i.health - renpy.random.randint(3,5)
                    elif i.state == "病重":
                        i.health = i.health - renpy.random.randint(4,6)
                    else:
                        pass
                    i.health = i.health - renpy.random.randint(-3,1)*0.1
                    if i.health >= 75:
                        templist = ["武"]
                    elif i.health <= 25:
                        templist = ["文"]
                    else:
                        templist =  []
                    if i.xingge == "外向":
                        templist.append(["文","文","武","武","武"])
                    elif i.xingge == "内向":
                        templist.append(["文","文","文","武","武"])
                    else:
                        templist.append(["文","文","武","武"])
                    lucky = renpy.random.choice(templist)
                    if lucky == "文":
                        i.wen = i.wen + i.iq*0.005
                    else:
                        i.wu = i.wu  + i.iq*0.005
                    i.duli= i.duli - renpy.random.randint(-4,1)*0.1
                    if i.mother == my:
                        i.like = i.like + renpy.random.randint(-2,1)*0.1
                    else:
                        pass
                
                
                elif i.plan == "重在实践" :
                    if i.state == "抱恙":
                        i.health = i.health - renpy.random.randint(2,4)
                    elif i.state == "病重":
                        i.health = i.health - renpy.random.randint(3,5)
                    else:
                        pass
                    if i.health >= 75:
                        templist = ["武"]
                    elif i.health <= 25:
                        templist = ["文"]
                    else:
                        templist =  []
                    if i.xingge == "外向":
                        templist.append(["文","文","武","武","武"])
                    elif i.xingge == "内向":
                        templist.append(["文","文","文","武","武"])
                    else:
                        templist.append(["文","文","武","武"])
                    lucky = renpy.random.choice(templist)
                    if lucky == "文":
                        i.wen = i.wen + i.iq*0.001
                    else:
                        i.wu = i.wu  + i.iq*0.001
                    i.nengli += i.qingxiang*0.004
                    i.qinmian= i.qinmian - renpy.random.randint(-4,1)*0.1
                    i.duli = i.duli + renpy.random.randint(4,8)*0.1
                    i.health = i.health + renpy.random.randint(4,8)*0.1
                    if i.mother == my:
                        i.like = i.like + renpy.random.randint(-1,2)*0.1
                    else:
                        pass
                
                
                else:
                    if i.state == "抱恙":
                        i.health = i.health + 1
                    elif i.state == "病重":
                        i.health = i.health + 1
                    else:
                        pass
                    i.health = i.health + 0.5
                    if i.mother == my:
                        i.like = i.like + 0.5
                    else:
                        i.qinzi += 0.5
                    
                    i.qinmian = i.qinmian - 0.5
                
                if hdxingge == "风流":
                    lucky = renpy.random.randint(0, 30)
                elif hdxingge == "刚正":
                    lucky = renpy.random.randint(0, 15)
                else:
                    lucky = renpy.random.randint(0, 20)
                if lucky == 0:
                    
                    renpy.call("皇帝过继子嗣",from_current=False)
                
                if i.live == 0 and i.age >= 5 and i.state == "寻常":
                    templist = Kid_richanglist(i)
                    tempnum = renpy.random.choice(templist)
                    Kid_richang(i,tempnum)
                
                
                if i.health > 100 :
                    i.health = 100
                elif i.health < 0:
                    i.health = 0
                else:
                    pass
                if i.beauty > 100 :
                    i.beauty = 100
                elif i.beauty < 0:
                    i.beauty = 0
                else:
                    pass
                if i.wen > 100 :
                    i.wen = 100
                elif i.wen < 0:
                    i.wen = 0
                else:
                    pass
                
                if i.wu > 100 :
                    i.wu = 100
                elif i.wu < 0:
                    i.wu = 0
                else:
                    pass
                if i.qinmian >= 100:
                    i.qinmian = 100
                elif i.qinmian <= 0:
                    i.qinmian = 0
                else:
                    pass
                if i.duli >= 100:
                    i.duli = 100
                elif i.duli <= 0:
                    i.duli = 0
                else:
                    pass
                if i.mother == my:
                    i.qinzi = i.like
                if i.qinzi > 100:
                    i.qinzi = 100
                
                if i.like > 100:
                    i.like = 100
                else:
                    pass
                if i.hdlike > 100:
                    i.hdlike = 100
                else:
                    pass
                if i.shili > 100:
                    i.shili = 100
                if i.iq > 100:
                    i.iq = 100
                else:
                    pass
                
                
                if i.mother.family == "和亲公主" or i.live  == -1 or i.age < 10 or i.sex == "公主":
                    pass
                else:
                    lucky = renpy.random.randint(0,100)
                    if i.qingxiang > lucky:
                        dachen = Kid_guanyuan_1(i)
                        if dachen == None:
                            pass
                        
                        else:
                            Kid_guanyuan_2(i,dachen)
                    tempnum = i.hdlike*0.8 + i.shili*0.5
                    for j in i.zhichizhe:
                        tempnum += j.shili*0.1
                    if i == taizi:
                        taizi_shili = tempnum
                    
                    if i != taizi and taizi != None:
                        tempnum = tempnum*0.5
                        if tempnum > taizi_shili :
                            taizi_shili = tempnum
                            renpy.call("改立太子",fei = taizi,li = i,from_current=False)
                        else:
                            pass
                    if taizi == None  :
                        tempnum += (hdage - 40)
                        
                        if tempnum > 100 or i.hdlike >= 100:
                            taizi_shili = tempnum
                            renpy.call("立太子",self = i,from_current=False)
                        else:
                            pass
                
                
                if i.xingge == "内向" and i.duli >70:
                    i.xingqing = "偏执"
                elif i.xingge == "中庸" and i.duli >70:
                    i.xingqing = "固执"
                elif i.xingge == "外向" and i.duli >70:
                    i.xingqing = "果断"
                elif i.xingge == "内向" and i.duli < 30:
                    i.xingqing = "孤僻"
                elif i.xingge == "中庸" and i.duli < 30:
                    i.xingqing = "软弱"
                elif i.xingge == "外向" and i.duli < 30:
                    i.xingqing = "幼稚"
                
                elif i.xingge == "内向" and i.qinmian < 30:
                    i.xingqing = "散漫"
                elif i.xingge == "中庸" and i.qinmian < 30:
                    i.xingqing = "贪玩"
                elif i.xingge == "外向" and i.qinmian < 30:
                    i.xingqing = "顽劣"
                
                elif i.xingge == "内向" and 40< i.duli < 60:
                    i.xingqing = "温和"
                elif i.xingge == "中庸" and 40< i.duli < 60:
                    i.xingqing = "乐观"
                elif i.xingge == "外向" and 40< i.duli < 60:
                    i.xingqing = "开朗"
                else:
                    pass
                if i.wen + i.wu + i.iq > 250 and i.iq > 80 and i.nengli > 80 and i.duli > 30:
                    i.pingjia = "不世奇才"
                elif  i.wen + i.wu + i.iq> 220 and i.iq > 70 and i.nengli > 50 :
                    i.pingjia = "七窍玲珑"
                elif  i.wen + i.wu + i.iq> 150 and i.iq > 60 and i.nengli > 50 :
                    i.pingjia = "未来可期"
                elif  i.iq < 50 and i.qinmian < 50 :
                    i.pingjia = "难成大器"
                elif i.iq < 30 and i.qinmian < 30 :
                    i.pingjia = "冥顽不灵"
                else:
                    i.pingjia = "暂无"
    return
init python:
    def Kid_richanglist(kid):
        list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        if kid.qinmian >= 85:
            list.append(11)
        if kid.qinmian >= 70:
            list.append(12)
        if kid.qinmian >= 50:
            list.append(13)
        if kid.qinmian <= 30:
            list.append(14)
        if kid.qinmian <= 15:
            list.append(15)
        
        if kid.duli >= 85:
            list.append(21)
        if kid.duli >= 70:
            list.append(22)
        if kid.duli >= 50:
            list.append(23)
        if kid.duli <= 30:
            list.append(24)
        if kid.duli <= 30:
            list.append(25)
        
        if kid.qingxiang >= 85:
            list.append(41)
        if kid.qingxiang >= 70:
            list.append(42)
        if kid.qingxiang >= 50:
            list.append(43)
        if kid.qingxiang <= 30:
            list.append(44)
        if kid.qingxiang <= 30:
            list.append(45)
        
        if kid.hdlike >= 85:
            list.append(31)
        if kid.hdlike >= 70:
            list.append(32)
        if kid.hdlike >= 50:
            list.append(33)
        if kid.hdlike <= 30:
            list.append(34)
        if kid.hdlike <= 30:
            list.append(35)
        
        if kid.mother != my and kid.mother in NPC_fz_list:
            list.append(51)
            list.append(52)
            list.append(53)
        
        list.append(61)
        
        
        if kid.duli >70 and kid.qinmian < 30:
            list.append(71)
        if kid.duli >70 and kid.qinmian > 50 and huangdi["昏庸"] > 50:
            list.append(72)
        if kid.duli >70 and kid.qinmian < 30:
            list.append(73)
        
        return list


    def Kid_richang(kid,what):
        templist = []
        
        if what == 11:
            tempstory =str(year)+"年"+str(month)+"月，请求先生给自己开小灶的时候碰到皇帝，得到皇帝的亲自指导。\n"
            kid.story.append(tempstory)
            kid.wen += huangdi["政务"]*0.01
            kid.hdlike += 0.5
        if what == 12:
            tempstory =str(year)+"年"+str(month)+"月，在皇帝前往重华宫时受到先生表扬。\n"
            kid.story.append(tempstory)
            kid.hdlike += 0.5
        if what == 13:
            pass
        if what == 14:
            tempstory =str(year)+"年"+str(month)+"月，在皇帝前往重华宫时被先生批评。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 0.5
            kid.qinmian += 0.5
        if what == 15:
            for i in NPC_Kids_list:
                if i == kid or i.live != 0 or i.plan == "休息玩乐" or i.state != "寻常" or i.age < 5:
                    pass
                else:
                    templist.append(i)
            if len(templist) == 0:
                tempstory =str(year)+"年"+str(month)+"月，偷偷逃学出去，被皇帝撞见，怒斥一通。\n"
                kid.hdlike -= 2
                kid.qinmian += 1
                kid.story.append(tempstory)
            else:
                tempkid = renpy.random.choice(templist)
                tempstory =str(year)+"年"+str(month)+"月，偷偷逃学出去，被"+str(tempkid.cheng)+str(tempkid.name)+"告诉了老师。\n"
                kid.hdlike -= 1
                kid.foes.append(tempkid)
                kid.story.append(tempstory)
                tempstory =str(year)+"年"+str(month)+"月，发现"+str(kid.cheng)+str(kid.name)+"逃学，告诉了老师。\n"
                tempkid.story.append(tempstory)
        
        
        if what == 21:
            tempstory =str(year)+"年"+str(month)+"月，在和皇帝探讨历史典故时各持己见，当众争执不下，皇帝脸色很不好看。\n"
            kid.wen += huangdi["政务"]*0.1
            kid.story.append(tempstory)
            kid.hdlike -= 0.5
        if what == 22:
            tempstory =str(year)+"年"+str(month)+"月，和先生因为对书中理解不同而产生了冲突，最后谁也没说服谁。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 0.2
        
        if what == 23:
            pass
        if what == 24:
            for i in NPC_Kids_list:
                if i == kid or i.live != 0 or i.plan == "休息玩乐" or i.state != "寻常" or i.age < 5:
                    pass
                else:
                    templist.append(i)
            if len(templist) == 0:
                tempstory =str(year)+"年"+str(month)+"月，听到有宫女在嘲笑自己仍然要奶娘陪着睡觉之事，羞愤不堪。\n"
                kid.story.append(tempstory)
                kid.duli += 1
                kid.qingxiang += 1
            
            else:
                tempkid = renpy.random.choice(templist)
                tempstory =str(year)+"年"+str(month)+"月，听到"+str(tempkid.cheng)+str(tempkid.name)+"在嘲笑自己仍然要奶娘陪着睡觉之事，羞愤不堪。\n"
                kid.story.append(tempstory)
                kid.foes.append(tempkid)
                kid.duli += 1
                kid.qingxiang += 1
        if what == 25:
            tempstory =str(year)+"年"+str(month)+"月，被皇帝发现在路边和小花小草说话。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 1
        
        
        if what == 31:
            tempstory =str(year)+"年"+str(month)+"月，被召见至圣宸宫，皇帝理政时一直随侍在旁。\n"
            kid.story.append(tempstory)
            kid.wen += huangdi["政务"]*0.01
            kid.hdlike += 0.5
        if what == 32:
            tempstory =str(year)+"年"+str(month)+"月，和皇帝一起在御花园散步闲聊。\n"
            kid.story.append(tempstory)
            kid.hdlike += 0.5
        
        if what == 33:
            pass
        if what == 34:
            pass
        if what == 35:
            pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if what == 51 :
            tempstory =str(year)+"年"+str(month)+"月，深夜偷吃点心被"+str(kid.mother.hao)+str(kid.mother.weifen)+str(kid.mother.name)+"发现。\n"
            kid.story.append(tempstory)
            kid.qinzi -= 1
        if what == 52 :
            tempstory =str(year)+"年"+str(month)+"月，送了亲手做的纸蝴蝶给"+str(kid.mother.hao)+str(kid.mother.weifen)+str(kid.mother.name)+"，却被其误认作螳螂，吓了一跳。\n"
            kid.story.append(tempstory)
            kid.qinzi -= 1
        if what == 53  :
            tempstory =str(year)+"年"+str(month)+"月，"+str(kid.mother.hao)+str(kid.mother.weifen)+str(kid.mother.name)+"亲自到重华宫指点功课。\n"
            kid.story.append(tempstory)
            kid.qinzi += 1
            kid.wen += kid.mother.book *0.01
        
        
        if what == 61 and kid.sex == "公主":
            for i in NPC_Kids_list:
                if i == kid or i.live != 0 or i.state != "寻常" or i.age < 5:
                    pass
                else:
                    templist.append(i)
            if len(templist) == 0:
                pass
            else:
                tempkid = renpy.random.choice(templist)
                tempstory =str(year)+"年"+str(month)+"月，和"+str(tempkid.cheng)+str(tempkid.name)+"比赛击毽，大获全胜，但由于其大哭不止，只好将自己所绣绣品赠送予其，二人重归于好。"
                kid.story.append(tempstory)
                tempstory =str(year)+"年"+str(month)+"月，和"+str(kid.cheng)+str(kid.name)+"比赛击毽，一败涂地，只能大哭不止，但收到其所绣绣品，二人重归于好。"
                tempkid.story.append(tempstory)
                kid.friends.append(tempkid)
                tempkid.friends.append(kid)
        
        if what == 71  :
            tempstory =str(year)+"年"+str(month)+"月，在课堂上公然顶撞先生扰乱教学，皇帝得知后气愤不已。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 1
        
        if what == 72  :
            tempstory =str(year)+"年"+str(month)+"月，公然直谏皇帝行事铺张，劳民伤财，令其勃然大怒。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 2
            huangdi["昏庸"] -= 2
            huangdi["暴戾"] += 1
        if what == 73  :
            tempstory =str(year)+"年"+str(month)+"月，在重华宫玩骰子取乐，被先生罚抄书百遍，仍然我行我素。\n"
            kid.story.append(tempstory)
            kid.hdlike -= 2

    def Kid_guanyuan_1(kid):
        if kid.duli >= kid.qinmian and kid.duli >= kid.nengli:
            templist = sorted(guanyuan_list, key=attrgetter("shili"),reverse = True)
            templist2 = []
        
        elif kid.qinmian >= kid.duli and kid.qinmian >= kid.nengli:
            templist = sorted(guanyuan_list, key=attrgetter("zhong"),reverse = True)
            templist2 = []
        
        elif kid.qinmian >= kid.duli and kid.qinmian >= kid.nengli:
            templist = sorted(guanyuan_list, key=attrgetter("zhong"),reverse = True)
            templist2 = []
        else:
            templist = sorted(guanyuan_list, key=attrgetter("level"),reverse = False)
            templist2 = []
        
        if kid.wen >= kid.wu:
            temptext == "文官"
        else:
            temptext == "武官"
        for i in templist:
            if i.duty == temptext and i not in kid.zhichizhe:
                templist2.append(i)
        if kid.mother.father in guanyuan_list and kid.mother.father not in templist2:
            templist2.append(kid.mother.father)
        if kid.mother.father in guanyuan_list and kid.mother.father not in templist2:
            templist2.append(kid.mother.father)
        
        
        if len(templist2) == 0:
            for i in templist :
                if i not in kid.zhichizhe:
                    templist2.append(i)
        if len(templist2) > 10:
            templist2 = renpy.random.sample(templist2, 10)
        if len(templist2) == 0:
            dachen = None
        else:
            lucky = renpy.random.randint(0,14)
            if lucky < len(templist2) :
                dachen = templist2[lucky]
            
            elif lucky >= len(templist2) :
                dachen = renpy.random.choice(templist2)
            else :
                dachen = None
        
        
        
        return dachen

    def Kid_guanyuan_2(kid,who):
        lucky = renpy.random.randint(30,100)
        if who.duty == "文官":
            tempnum = kid.wen
        else:
            tempnum = kid.wu
        if kid.cheng == "大皇子" :
            tempnum += (who.zhong-30)*0.5
        if kid.shengmu.level == 0 or kid.mother.level == 0:
            tempnum +=  (who.zhong-30)*0.5
        if who.qizi != None :
            if who.qizi.mother == kid.mother  or who.qizi.mother == kid.mother:
                tempnum +=  30
        if kid.zheng != None and who in kid.zheng.jiazu:
            tempnum += (100-who.zhong)
        
        
        
        
        
        
        tempnum += (kid.nengli - who.neng)
        if who.zhichi != None:
            tempnum = tempnum*0.5
        if tempnum > 50 and who not in kid.zhichizhe:
            tempstory =str(year)+"年"+str(month)+"月，与"+str(guanwei[who.level]) + str(who.duty)+str(who.name)+"私下商谈许久，似乎达成了共识。\n"
            kid.story.append(tempstory)
            kid.zhichizhe.append(who)
            who.zhichi = kid




label 改立太子(fei, li):
    nvl clear
    旁白 "[nianhao][year]年[month]月，皇帝以诏布告天下——"
    nvl clear
    $ fei.fenghao = ""
    $ Kids_fenghao(fei)
    旁白 "皇太子[fei.name]，不法祖德，不遵圣训，惟肆恶暴戾淫秽，纳邪说，怀异端，伤败於典礼，惊骇於视听。不可守器纂统，承七庙之重。"
    旁白 "今褫夺皇太子位，降为[fei.fenghao]。"
    nvl clear
    $ temptext = str(li.cheng+li.name)
    旁白 "另，[temptext]，承祧行庆，端在元良，宜承大统，故授以册宝，立为皇太子，正位东宫。"
    nvl clear
    $ li.fenghao = "{color=#FF3030}皇太子{/color}"
    $ taizi = li
    $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，原太子"+str(fei.cheng)+str(fei.name)+"被废，改立"+str(li.cheng)+str(li.name) +"为太子。\n"
    $ allstory.insert(0,tempstory2)
    $ tempstory =str(year)+"年"+str(month)+"月，被立为太子。\n"
    $ li.story.append(tempstory)
    $ tempstory =str(year)+"年"+str(month)+"月，被褫夺皇太子位，降为"+fei.fenghao+"。\n"
    $ fei.story.append(tempstory)
    nvl clear
    return


label 立太子(self):
    nvl clear
    旁白 "[nianhao][year]年[month]月，皇帝以诏布告天下——"
    nvl clear
    $ temptext = ""
    if self.cheng == "大皇子":
        $ temptext += "宗室首嗣，"
    if self.mother.level == 0 or self.shengmu.level == 0:
        $ temptext += "嫡室所出，"
    旁白 "[self.cheng][guoxing][self.name]，[temptext]天意所属。"
    旁白 "兹恪遵初昭，载稽典礼，抚顺舆情，授以册宝，立为皇太子，正位东宫。"
    nvl clear
    $ self.fenghao = "{color=#FF3030}皇太子{/color}"
    $ taizi = self
    $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(self.cheng)+str(self.name) +"被立为太子。\n"
    $ allstory.insert(0,tempstory2)
    $ tempstory =str(year)+"年"+str(month)+"月，被立为太子。\n"
    $ self.story.append(tempstory)
    nvl clear
    return

label 皇嗣寿终正寝(kid):
    if kid.zheng == None:
        "宫中来报——"
        "[kid.cheng][kid.name]已于宫中寿终正寝。"
    else:
        "宫外来报——"
        "[kid.fenghao][kid.name]已于府中寿终正寝。"

    return


label 皇嗣去世(kid):
    if kid.mother != my:
        $ ("寝居")
        show 我的宫女
        我的宫女 "[my.cheng]，不好了，听说……听说[kid.cheng]没了！"
        我 "什么？"
        我 思 "（[kid.cheng]身子骨素来弱得很，今日之事倒也并不叫人意外，只是……）"
    else:

        $ ("寝居")
        show 我的宫女
        我的宫女 "[my.cheng]！[my.cheng]！您去看看[kid.cheng]吧……[kid.cheng]情况有些不妙了！"
        我 惊 "[kid.name]……怎么了？！"
        我的宫女 "奴婢也说不上来……已经派人去请太医了……"
        hide 我的宫女
        "片刻后——"
        show 太医令
        我 "大人，[kid.cheng]如今如何了？"
        太医令 "（摇头）[kid.cheng]现下……微臣只能尽力而为，实在不敢做出任何担保。"
        我 泪 "怎会如此……"
        hide 太医令
        "一夜无眠……"
        if kid.hdlike >= 50:
            "宫人" "皇上到——"
            show 皇帝
            我 泪 "臣妾参——"
            皇上 "[kid.name]如今如何了？"
            我 泪 "太医还在诊治……"
            皇上 "[kid.name]一定会没事的……"
            hide 皇帝
        "良久，太医缓缓步出殿内。"
        show 太医令
        太医令 "陛下、娘娘……请节哀。"
        太医令 "微臣无能……未能保住[kid.cheng]的性命……"
        我 泪 "[kid.name]……"
    hide 太医令
    return

label 皇嗣生病(kid, zhong):
    $ ("寝居")
    show 我的宫女
    if zhong == False:
        我的宫女 "主子，今日[kid.cheng]看起来有些没精打采的，请了太医来看后说是有些微恙，虽无大碍但还是需要好生休息才是。"
    else:
        我的宫女 "主子，今日[kid.cheng]看起来脸色十分不好，请了太医来看后说是病得不清，已经开了药了，但这阵子也得好好休息才能痊愈。"
    hide 我的宫女
    "是否要让[kid.cheng]休息养病？"
    menu:
        "是":
            $ kid.plan = "休息玩乐"
        "不必":
            pass
    return

label 皇嗣康复(kid):
    $ ("寝居")
    show 我的宫女
    我的宫女 "主子，今日太医来看过了，说[kid.cheng]已经痊愈了。"
    hide 我的宫女
    if kid.age < 5 and kid.plan == "休息玩乐":
        $ kid.plan = "顺其自然"
    return
 
