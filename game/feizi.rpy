init python:
    class FeiziFactory(object):
        def instantiation_Feizi(self):
            return NPC_Feizi()


    class Feizi(object):
        def __init__(self):
            self.name = name
            self.xing = xing
            self.ming = ming
            self.face = face 
            self.level = level
            self.weifen = weifen 
            self.hao = hao 
            self.cheng = cheng
            self.state = state 
            self.palace = palace
            self.qinju = qinju
            self.jiazu = jiazu
            self.father = father
            self.age = age
            self.sisters = sisters
            self.family = family
            self.familylevel = familylevel
            self.fatherduty = fatherduty
            self.familylocation = familylocation
            self.health = health
            self.beauty = beauty
            self.yuanmao = yuanmao
            self.qizhi = qizhi
            self.meili = meili
            self.dance = dance
            self.book = book
            self.cixiu = cixiu
            self.muzic = muzic
            self.battle = battle
            self.medic = medic
            self.like = like
            self.love = love
            self.power = power
            self.exp = exp
            self.story = story
            self.year = year
            self.xinji = xinji
            self.xinji1 = xinji1
            self.xinjilv = xinjilv
            self.xingge = xingge
            self.xingge1 = xingge1
            self.healthlv = healthlv
            self.beautylv = beautylv
            self.qizhilv = qizhilv
            self.meililv = meililv
            self.dancelv = dancelv
            self.booklv = booklv
            self.cixiulv = cixiulv
            self.muziclv = muziclv
            self.mediclv = mediclv
            self.battlelv = battlelv
            self.likelv = likelv
            self.lovelv = lovelv
            self.meet = meet
            self.kids = kids
            self.taihoulike = taihoulike
            self.lucky = lucky
            self.makelucky = makelucky
            self.Gongnv = Gongnv
            self.qingxiang = qingxiang
            self.shiqin = shiqin
            self.palacenum = palacenum
            self.qinjunum = qinjunum
            self.jinzu = jinzu
            self.huaiyun = huaiyun
            self.friends = friends
            self.foes = foes
            self.shou = shou
            self.tags = tags
            self.yali = yali
            self.tequan1 = tequan1
            self.tequan2 = tequan2
            self.paixu = paixu
            self.meishu = meishu
            self.huashu = huashu
            self.anhai = anhai
            self.fangyu = fangyu
            self.AP = AP
            self.jiayun = jiayun
            self.skillcosts = self.skillcosts
        
        def Feizi_creat(self):
            self.name = ""
            self.xing = ""
            self.ming = ""
            self.face = 0
            self.level = -1
            self.weifen = ""
            self.hao = ""
            self.cheng = ""
            self.state = ""
            self.palace = ""
            self.qinju = ""
            self.jiazu = []
            self.father = ""
            self.sisters = []
            self.age = 0
            self.family = ""
            self.familylevel = 0
            self.fatherduty = ""
            self.familylocation = ""
            self.health = 0
            self.beauty = 0
            self.qizhi = 0
            self.meili = 0
            self.dance = 0
            self.book = 0
            self.cixiu = 0
            self.muzic = 0
            self.battle = 0
            self.medic = 0
            self.like = 0
            self.love = 0
            self.power = 0
            self.exp = 0
            self.story = []
            self.year = 0
            self.xinji = 0
            self.xinji1 = False
            self.xinjilv = ""
            self.xingge = 0
            self.xingge1 = False
            self.healthlv = ""
            self.beautylv = ""
            self.qizhilv = ""
            self.meililv = ""
            self.dancelv =""
            self.booklv = ""
            self.cixiulv = ""
            self.muziclv = ""
            
            self.mediclv = ""
            self.battlelv =""
            self.likelv =""
            self.lovelv = ""
            self.meet =0
            self.kids = []
            self.taihoulike = 0
            self.lucky =0
            self.makelucky = 0
            self.Gongnv =[]
            self.qingxiang = 0
            self.shiqin =0
            self.palacenum = 0
            self.qinjunum = 0
            self.jinzu = 0
            self.huaiyun = 0
            self.friends = []
            self.foes = []
            self.yuanmao = 0
            self.shou = 0
            self.tags = []
            self.yali = 0
            self.tequan1 = -1
            self.tequan2 = -1
            self.paixu = 0
            self.meishu = {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
            self.huashu =  {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
            self.anhai =  {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
            self.fangyu = {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
            self.jiayun = False
            self.skillcosts = 0
            self.AP = 5

    def Feizi_skills_random(self):
        self.skillcosts = 0
        
        tempnum = self.familylevel
        if self.xingge == "圆滑" or self.xingge == "势力":
            tempnum -= 2
        elif self.xingge == "娇纵" or self.xingge == "清冷":
            tempnum += 2
        else:
            pass
        if tempnum <= 0:
            self.huashu["初始"] = 3
        else:
            lucky = renpy.random.randint(0,int(tempnum))
            if lucky == 0:
                self.huashu["初始"] = 3
            elif lucky == 1 or lucky == 2 or lucky == 3 :
                self.huashu["初始"] = renpy.random.randint(2,3)
            elif lucky == 4 or lucky == 5 or lucky == 6 or lucky == 7:
                self.huashu["初始"] = renpy.random.randint(1,2)
            else:
                self.huashu["初始"] = renpy.random.randint(0,1)
        if self.huashu["初始"] != 0:
            if self.huashu["初始"] == 3:
                self.huashu["一A"] = renpy.random.randint(0,self.huashu["初始"])
                self.huashu["一B"] = renpy.random.randint(0,self.huashu["初始"])
            if self.huashu["一A"] != 0 or self.huashu["一B"] != 0:
                if self.huashu["一A"]<= self.huashu["一B"]:
                    tempnum = self.huashu["一A"]
                else:
                    tempnum = self.huashu["一B"]
                self.huashu["二A"] = renpy.random.randint(0,tempnum)
                self.huashu["二B"] = renpy.random.randint(0,tempnum)
            if self.huashu["二A"] != 0 or self.huashu["二B"] != 0:
                if self.huashu["二A"]<= self.huashu["二B"]:
                    tempnum = self.huashu["二A"]
                else:
                    tempnum = self.huashu["二B"]
                self.huashu["三级"] = renpy.random.randint(0,tempnum)
        
        tempnum = (10-self.meili*0.01) + (13-self.familylevel)
        if tempnum <= 0:
            self.meishu["初始"] = 3
        else:
            lucky = renpy.random.randint(0,int(tempnum))
            if lucky == 0:
                self.meishu["初始"] = 3
            elif lucky == 1 or lucky == 2 or lucky == 3 :
                self.meishu["初始"] = renpy.random.randint(2,3)
            elif lucky == 4 or lucky == 5 or lucky == 6 or lucky == 7:
                self.meishu["初始"] = renpy.random.randint(1,2)
            else:
                self.meishu["初始"] = renpy.random.randint(0,1)
        
        if self.meishu["初始"] != 0:
            if self.meishu["初始"] == 3:
                self.meishu["一A"] = renpy.random.randint(0,self.meishu["初始"])
                self.meishu["一B"] = renpy.random.randint(0,self.meishu["初始"])
            if self.meishu["一A"] != 0 or self.meishu["一B"] != 0:
                if self.meishu["一A"]<= self.meishu["一B"]:
                    tempnum = self.meishu["一A"]
                else:
                    tempnum = self.meishu["一B"]
                self.meishu["二A"] = renpy.random.randint(0,tempnum)
                self.meishu["二B"] = renpy.random.randint(0,tempnum)
            if self.meishu["二A"] != 0 or self.meishu["二B"] != 0:
                if self.meishu["二A"]<= self.meishu["二B"]:
                    tempnum = self.meishu["二A"]
                else:
                    tempnum = self.meishu["二B"]
                self.meishu["三级"] = renpy.random.randint(0,tempnum)
        
        
        tempnum = self.qingxiang*0.1
        if self.xingge == "圆滑" or self.xingge == "温婉":
            tempnum -= 2
        elif self.xingge == "安静" or self.xingge == "清冷":
            tempnum -= 1
        else:
            pass
        if tempnum <= 0:
            self.fangyu["初始"] = 3
        else:
            lucky = renpy.random.randint(0,int(tempnum))
            if lucky == 0:
                self.fangyu["初始"] = 3
            elif lucky == 1 or lucky == 2 or lucky == 3 :
                self.fangyu["初始"] = renpy.random.randint(2,3)
            elif lucky == 4 or lucky == 5 or lucky == 6 or lucky == 7:
                self.fangyu["初始"] = renpy.random.randint(1,2)
            else:
                self.fangyu["初始"] = renpy.random.randint(0,1)
        
        if self.fangyu["初始"] != 0:
            if self.fangyu["初始"] == 3:
                self.fangyu["一A"] = renpy.random.randint(0,self.fangyu["初始"])
                self.fangyu["一B"] = renpy.random.randint(0,self.fangyu["初始"])
        if self.fangyu["一A"] != 0 or self.fangyu["一B"] != 0:
            if self.fangyu["一A"]<= self.fangyu["一B"]:
                tempnum = self.fangyu["一A"]
            else:
                tempnum = self.fangyu["一B"]
            self.fangyu["二A"] = renpy.random.randint(0,tempnum)
            self.fangyu["二B"] = renpy.random.randint(0,tempnum)
        if self.fangyu["二A"] != 0 or self.fangyu["二B"] != 0:
            if self.fangyu["二A"]<= self.fangyu["二B"]:
                tempnum = self.fangyu["二A"]
            else:
                tempnum = self.fangyu["二B"]
            self.fangyu["三级"] = renpy.random.randint(0,tempnum)
        
        
        tempnum = (100-self.qingxiang)*0.1 + (1000-self.xinji)*0.01
        if tempnum <= 0:
            self.anhai["初始"] = 3
        else:
            lucky = renpy.random.randint(0,int(tempnum))
            if lucky == 0:
                self.anhai["初始"] = 3
            elif lucky == 1 or lucky == 2 or lucky == 3 :
                self.anhai["初始"] = renpy.random.randint(2,3)
            elif lucky == 4 or lucky == 5 or lucky == 6 or lucky == 7:
                self.anhai["初始"] = renpy.random.randint(1,2)
            else:
                self.anhai["初始"] = renpy.random.randint(0,1)
        
        if self.anhai["初始"] != 0:
            if self.anhai["初始"] == 3:
                self.anhai["一A"] = renpy.random.randint(0,self.anhai["初始"])
                self.anhai["一B"] = renpy.random.randint(0,self.anhai["初始"])
        if self.anhai["一A"] != 0 or self.anhai["一B"] != 0:
            if self.anhai["一A"]<= self.anhai["一B"]:
                tempnum = self.anhai["一A"]
            else:
                tempnum = self.anhai["一B"]
            self.anhai["二A"] = renpy.random.randint(0,tempnum)
            self.anhai["二B"] = renpy.random.randint(0,tempnum)
        if self.anhai["二A"] != 0 or self.anhai["二B"] != 0:
            if self.anhai["二A"]<= self.anhai["二B"]:
                tempnum = self.anhai["二A"]
            else:
                tempnum = self.anhai["二B"]
            self.anhai["三级"] = renpy.random.randint(0,tempnum)





    def Feizi_random(self,type):
        
        
        randomname(self)
        self.age = renpy.random.randint(15,18)
        self.face = renpy.random.choice(list_femaleface)
        list_femaleface.remove(self.face)
        self.AP = 5
        
        if type == 0 :
            self.year = 3
            self.age += 3
        else:
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
        
        
        
        Feizifamily(self)
        self.makelucky = renpy.random.randint(1000,1500) + self.familylevel*renpy.random.randint(70,100)
        
        randomshuxing(self)
        self.yuanmao =self.beauty
        if self.fatherduty == '武将':
            self.health = self.health + renpy.random.randint(20, 50)
        elif self.fatherduty == '文官':
            self.qizhi = self.qizhi + renpy.random.randint(20, 50)
        elif self.fatherduty == "内侍":
            self.meili = self.meili + renpy.random.randint(20, 50)
        else :
            self.beauty = self.beauty + renpy.random.randint(20, 50)
        if self.familylocation == "义女" or self.familylocation == "庶女":
            self.beauty = self.beauty + renpy.random.randint(30, 50)
            self.xinji = self.xinji + renpy.random.randint(30, 50)
        else:
            pass
        
        
        
        randomtags(self)
        tags_buff(self)
        tags_limitcheck(self)
        
        
        
        if type == 1:
            self.love = (self.beauty +self.meili+self.qizhi)/250 + self.familylevel/4
            self.taihoulike = (self.beauty +self.meili+self.qizhi)/250 - self.familylevel/4
        else :
            self.love = (self.beauty +self.meili+self.qizhi)/25 + (self.dance+self.book+self.muzic+self.cixiu)/100 + + self.familylevel + renpy.random.randint(-10, 40)
            self.taihoulike = renpy.random.randint(-10, 80)
        
        
        
        
        tempnum = self.dance + self.book + self.cixiu + self.muzic
        tempnum2 = self.familylevel
        if self.familylocation == "义女":
            tempnum2 = self.familylevel + 2
        elif self.familylocation == "庶女":
            tempnum2 = self.familylevel + 1
        else:
            pass
        
        self.exp =0
        self.love = 0
        
        if type == 0 or  type == 2:
            self.shiqin = 1
            self.meet = 0
            self.xingge1 = False
            self.like = renpy.random.randint(0, 10)
            self.love = renpy.random.randint(0, 80)
            if player == 0 :
                self.exp = weifen_list[1][3]*renpy.random.randint(1, 10)*0.1 - weifen_list[1][3]*(tempnum2)*0.1 + renpy.random.randint(-300, 600)
                if self.exp <= 0:
                    self.exp = 0
                self.exp += self.beauty/5 + self.qizhi/10 + self.meili/10 +tempnum/15 + self.love*20
            elif  player == 1 :
                self.exp = weifen_list[1][3]*renpy.random.randint(1, 10)*0.1 - weifen_list[1][3]*(tempnum2)*0.1 + renpy.random.randint(-400, 800)
                if self.exp <= 0:
                    self.exp = 0
                self.exp += self.beauty/5 + self.qizhi/10 + self.meili/10 +tempnum/15 + self.love*20
            else:
                self.love = renpy.random.randint(0, 60)
                self.exp = weifen_list[1][3]*renpy.random.randint(1, 10)*0.1 - weifen_list[1][3]*(tempnum2+1)*0.1 + renpy.random.randint(-50, 400)
                if self.exp <= 0:
                    self.exp = 0
                self.exp += self.beauty/3 + self.qizhi/5 + self.meili/5 +tempnum/10 + self.love*25
        
        
        elif  type == 1:
            self.like = renpy.random.randint(0, 15)
            self.love = (self.beauty +self.meili+self.qizhi)/250 + self.familylevel/4
            a = int(len(weifen_list)*0.5)
            self.exp = weifen_list[a][3] - weifen_list[a][3]*(tempnum2*0.12) + self.beauty/40 + self.qizhi/80 + self.meili/80 + self.love + renpy.random.randint(-30, 50)
            for i in self.sisters:
                self.exp += i.love*0.1
                if i.exp >= weifen_list[0][3]:
                    self.exp += weifen_list[0][3]*0.05
                elif i.exp <= 0:
                    pass
                else:
                    self.exp += i.exp*0.05
            
            if self.exp < 0:
                self.exp = 0
            else:
                pass
            
            self.meet = 0
            if year == 4 and player == 0 :
                self.meet = 1
                self.xingge1 = True
                self.shiqin = 0
            elif player == 1 and year == 4:
                self.shiqin = renpy.random.randint(0, 2)
                self.exp += 10*self.shiqin
                self.love += 5*self.shiqin
                self.xingge1 = False
            
            else:
                self.shiqin = 0
                self.xingge1 = False
        
        
        
        else :
            self.shiqin = 0
            self.meet = 0
            self.xingge1 = False
            self.like = 0
            self.love = 0
            self.exp = 0
        
        if self.familylevel == 0 and self.exp >= weifen_list[1][3]:
            self.exp = weifen_list[1][3]
        
        
        self.shou = renpy.random.randint(45,65)
        if self.health < 300:
            self.shou = self.shou - renpy.random.randint(5,10)
        elif self.health > 700:
            self.shou = self.shou + renpy.random.randint(5,10)
        else:
            pass
        if self.beauty > 900:
            self.shou = self.shou - renpy.random.randint(5,10)
        elif self.beauty < 400:
            self.shou = self.shou + renpy.random.randint(5,10)
        else:
            pass
        
        self.yali = 500 - abs(self.xinji-500)
        self.yali = self.yali*0.05
        
        
        if self.year == 3 or self.love > 15:
            lucky = renpy.random.randint(0, 2)
            if lucky == 0:
                self.hao = renpy.random.choice(hao_list)
                hao_list.remove(self.hao)
            else :
                self.hao = ""
        
        elif self.year == 0 and self.love > 10 :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                self.hao = renpy.random.choice(hao_list)
                hao_list.remove(self.hao)
            else :
                self.hao = ""
        else:
            self.hao = ""
        
        
        self.tequan1 = -1
        self.tequan2 = -1
        
        self.friends = []
        self.foes = []
        self.kids = []
        self.Gongnv = []
        Feizi_skills_random(self)

    def Xiunv_random(self):
        randomname(self)
        self.AP = 5
        self.age = renpy.random.randint(15,18)
        self.face = renpy.random.choice(list_femaleface)
        list_femaleface.remove(self.face)
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
        
        
        
        Xiunvfamily(self)
        self.makelucky = renpy.random.randint(1000,1500) + self.familylevel*renpy.random.randint(70,100)
        
        randomshuxing(self)
        if self.fatherduty == '武将':
            self.health = self.health + renpy.random.randint(20, 50)
        elif self.fatherduty == '文官':
            self.qizhi = self.qizhi + renpy.random.randint(20, 50)
        elif self.fatherduty == "内侍":
            self.meili = self.meili + renpy.random.randint(20, 50)
        else :
            self.beauty = self.beauty + renpy.random.randint(20, 50)
        if self.familylocation == "义女" or self.familylocation == "庶女":
            self.beauty = self.beauty + renpy.random.randint(30, 50)
            self.xinji = self.xinji + renpy.random.randint(30, 50)
        else:
            pass
        
        
        
        randomtags(self)
        tags_buff(self)
        tags_limitcheck(self)
        
        
        
        
        
        
        
        
        self.yuanmao =self.beauty    
        Feizi_skills_random(self)



    def Xiunv_cefeng(self):
        tempnum = self.dance + self.book + self.cixiu + self.muzic
        tempnum2 = self.familylevel
        if self.familylocation == "义女":
            tempnum2 = self.familylevel + 2
        elif self.familylocation == "庶女":
            tempnum2 = self.familylevel + 1
        else:
            pass
        if len(self.sisters) == 0 and self != taoning:
            Creat_Males(whose = self,how = 0)
        
        self.like = renpy.random.randint(0, 15)
        self.love = (self.beauty +self.meili+self.qizhi)/250 + self.familylevel/4
        a = int(len(weifen_list)*0.5)
        self.exp = weifen_list[a][3] - weifen_list[a][3]*(tempnum2*0.12) + self.beauty/40 + self.qizhi/80 + self.meili/80 + self.love + renpy.random.randint(-30, 50)
        for i in self.sisters:
            self.exp += i.love*0.1
            if i.exp >= weifen_list[0][3]:
                self.exp += weifen_list[0][3]*0.05
            elif i.exp <= 0:
                pass
            else:
                self.exp += i.exp*0.05
        if self.exp < 0:
            self.exp = 0
        else:
            pass
        
        self.meet = 0
        self.shiqin = 0
        self.xingge1 = False
        
        
        self.shou = renpy.random.randint(45,65)
        if self.health < 300:
            self.shou = self.shou - renpy.random.randint(5,10)
        elif self.health > 700:
            self.shou = self.shou + renpy.random.randint(5,10)
        else:
            pass
        if self.beauty > 900:
            self.shou = self.shou - renpy.random.randint(5,10)
        elif self.beauty < 400:
            self.shou = self.shou + renpy.random.randint(5,10)
        else:
            pass
        
        self.yali = 500 - abs(self.xinji-500)
        self.yali = self.yali*0.05
        
        
        
        if self.year == 3 or self.love > 15:
            lucky = renpy.random.randint(0, 2)
            if lucky == 0:
                self.hao = renpy.random.choice(hao_list)
                hao_list.remove(self.hao)
            else :
                self.hao = ""
        
        elif self.year == 0 and self.love > 10 :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                self.hao = renpy.random.choice(hao_list)
                hao_list.remove(self.hao)
            else :
                self.hao = ""
        else:
            self.hao = ""
        
        
        self.tequan1 = -1
        self.tequan2 = -1
        Feizilevel_xuanxiu(self)
        
        self.friends = []
        self.foes = []
        self.kids = []




    class NPC_Feizi(Feizi):
        def __init__(self):
            Feizi.Feizi_creat(self)

    factory = FeiziFactory()

    def Creat_Feizi(num,type):
        
        
        global jinshu
        global NPC_fz_list
        tempnum = 0
        while tempnum < num:
            a = factory.instantiation_Feizi()
            Feizi_random(a,type)
            if type == 1:
                Feizilevel_xuanxiu(a)
            if type == 1 and taoning_xuanxiu == True:
                maketaoning(taoning)
                NPC_newfz_list.append(taoning)
                tempnum += 1
                Feizilevel_xuanxiu(taoning)
            if len(NPC_fz_list) > 0 and my.name == "魏锦婳" and jinshu == False:
                jinshu = True
                Creat_TSFZ(a,"魏","锦书")
            if a not in NPC_fz_list :
                
                lucky = renpy.random.randint(0,30)
                if type == 0 and lucky == 0:
                    mysister(a)
                else:
                    pass
                NPC_fz_list.append(a)
            tempnum += 1
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("exp"),reverse = True)

    def Creat_Xiunv(num):
        global NPC_newfz_list
        tempnum = 0
        while tempnum < num:
            if taoning_xuanxiu == True:
                maketaoning(taoning)
                NPC_newfz_list.append(taoning)
                tempnum += 1
            else:
                a = factory.instantiation_Feizi()
                Xiunv_random(a)
                NPC_newfz_list.append(a)
                tempnum += 1


    def Creat_TSFZ(who,xing,ming):
        if xing == "魏" and ming == "锦书":
            who.xing = "魏"
            who.ming = "锦书"
            who.name = "魏锦书"
            who.like = 80
            who.face = "jinshu"
            who.qingxiang = renpy.random.randint(10, 50)
            who.xingge = "安静"
            who.familylevel = my.familylevel
            who.family = my.family
            who.fatherduty = my.fatherduty
            temp = who.father
            my.sisters.append(who)
            if who.sisters == []:
                pass
            else:
                for i in who.sisters:
                    i.sisters.remove(who)
                    who.sisters.remove(i)
                    randomname(i)
                    Creat_Males(i,how = 0)
            who.sisters.append(my)
            
            if temp in guanyuan_list:
                guanyuan_list.remove(temp)
            del temp
            del who.father
            who.father = my.father
            my.father.feizi.append(who)
            if tags_family[0] in who.tags:
                who.tags.remove(tags_family[0])
            if who.familylevel > 3 and tags_family[1] in who.tags:
                who.tags.remove(tags_family[1])
            if who.familylevel <= 3 and tags_family[1] not in who.tags:
                who.tags.insert(0,tags_family[1])
            if who.familylevel < 8  and tags_family[2] in who.tags:
                who.tags.remove(tags_family[2])
            if who.familylevel >= 8 and tags_family[2] not in who.tags:
                who.tags.insert(0,tags_family[2])
        NPC_fz_list.append(who)

    def mysister(who):
        who.xing = my.xing
        who.name = who.xing + who.ming
        who.familylevel = my.familylevel
        who.family = my.family
        who.fatherduty = my.fatherduty
        temp = who.father
        my.sisters.append(who)
        who.sisters.append(my)
        
        if temp in guanyuan_list:
            guanyuan_list.remove(temp)
        del temp
        del who.father
        who.father = my.father
        my.father.feizi.append(who)
        if tags_family[0] in who.tags:
            who.tags.remove(tags_family[0])
        if who.familylevel > 3 and tags_family[1] in who.tags:
            who.tags.remove(tags_family[1])
        if who.familylevel <= 3 and tags_family[1] not in who.tags:
            who.tags.insert(0,tags_family[1])
        if who.familylevel < 8  and tags_family[2] in who.tags:
            who.tags.remove(tags_family[2])
        if who.familylevel >= 8 and tags_family[2] not in who.tags:
            who.tags.insert(0,tags_family[2])





screen feizihudong():
    style_prefix "meetNPC"

    $ b = len(fzhd)
    if (b % 3) == 0:
        $ a = b/3
    elif (b % 3) == 1:
        $ a = round(b/3) + 1
    else:
        $ a = round(b/3) + 1
    frame align (0.5,0.8):
        background None

        has grid 3 a
        spacing 20
        for i in fzhd:
            if i == "闲聊" or i == "讨好" or i == "夸奖" or i == "赏赐" or i == "送礼" or i == "提点":
                textbutton "{font=问藏书房.ttf}{size=35}"+i:
                    align (0.5,0.5)
                    action SetVariable("fzhdlabel","妃嫔互动_"+i),Hide("fzhd"),Return()
            else:
                textbutton "{font=问藏书房.ttf}{size=35}"+i:
                    align (0.5,0.5)
                    action RemoveFromSet(fzhd,i),SetVariable("fzhdlabel","妃嫔互动_"+i),Hide("fzhd"),Return()
        if 3*a - b == 1:
            textbutton ""
        elif 3*a - b == 2:
            textbutton ""
            textbutton ""
        else:
            pass

label 妃嫔互动_请安:
    if fz.like < 0 and fz.xinji < 700:
        "[fz.hao][fz.weifen] [fz.name]" "啧，给本宫请安？真不知道安的什么心呐……"
    elif fz.xingge == "娇纵" and my.love > 80:
        "[fz.hao][fz.weifen] [fz.name]" "哎哎哎，本宫可受不起[my.cheng]的大礼，谁不知道你是皇上心尖上的人呐。"
    elif fz.xingge == "娇纵" and my.love < 25:
        "[fz.hao][fz.weifen] [fz.name]" "哎，有什么事儿就说罢，本宫没工夫跟你浪费时间。"
    elif fz.xingge == "娇纵" and fz.like < 50:
        "[fz.hao][fz.weifen] [fz.name]" "哎，有什么事儿就说罢，本宫没工夫跟你浪费时间。"
    elif fz.xingge == "势利" and my.love < 20:
        "[fz.hao][fz.weifen] [fz.name]" "哎，有什么事儿就说罢，本宫没工夫跟你浪费时间。"
    else:
        $ Feizilike_Up(fz,0.5)
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]免礼罢。"
    return

label 妃嫔互动_问好:
    if fz.like < 0 and fz.xinji < 700:
        "[fz.hao][fz.weifen] [fz.name]" "（小声）啧，黄鼠狼上门来拜年了？真不知道安的什么心呐……"
    elif fz.xingge == "势利" and my.love < 20 and fz.like < 30:
        "[fz.hao][fz.weifen] [fz.name]" "（敷衍）[my.cheng]安。"
    else:
        $ Feizilike_Up(fz,renpy.random.randint(3, 6)*0.1)
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]安。"
    return

label 妃嫔互动_闲聊:




    if fz.like < 0 and fz.xinji < 700:
        if my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]冷哼了一声。）"
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]说吧，嫔妾听着便是了。"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]冷哼了一声，狠狠瞪你一眼。）"
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]本宫与你没什么好说的！"
    elif fz.xingge == "活泼"and fz.xinji < 700:
        "[fz.hao][fz.weifen] [fz.name]" "（聊天时，[fz.name]时长提起自己的童年生活，还偶尔抱怨起宫廷之中规矩繁琐。）"
        if fz.xingge1 == False:
            "[fz.name]看起来倒很是活泼可爱。"
            $ Feizilike_Up(fz,1)
            $ fz.xingge1 = True
        else:
            $ lucky = renpy.random.randint(0, 5)
            if lucky == 0 and my.level <= fz.level:
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，你的位份比我高，如果有机会的话，你跟皇上说一声，让我出宫去玩玩，好不好哇。"
                menu:
                    "如果有机会的话……":
                        "[fz.hao][fz.weifen] [fz.name]" "嘻嘻，其实我知道这是不可能的啦，不过，还是谢谢您……"
                        $ Feizilike_Up(fz,2)
                    "身为帝王嫔妃，自由终究遥不可及":

                        "[fz.hao][fz.weifen] [fz.name]" "（面露哀伤）是啊，大概我也只能做一做梦了……"
                        $ fz.xinji = fz.xinji + 20
                        $ fz.qingxiang = fz.qingxiang + 5
                    "绝无可能，少做梦了":
                        "[fz.hao][fz.weifen] [fz.name]" "[fz.name]脸上的笑容顿时消失了。她愣了一下，眼底似乎有什么东西破碎了。"
                        $ fz.qingxiang += 5
                        $ fz.like = fz.like - 2
            elif lucky == 0 and my.level > fz.level:
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，你说，如果有机会我让皇上放我出宫去玩玩，他会同意吗？"
                menu:
                    "如果皇上高兴的话……":
                        "[fz.hao][fz.weifen] [fz.name]" "嘻嘻，其实我知道这是不可能的啦，不过，还是谢谢你的安慰……"
                        $ Feizilike_Up(fz,2)
                    "身为帝王嫔妃，自由终究遥不可及":

                        "[fz.hao][fz.weifen] [fz.name]" "（面露哀伤）是啊，大概我也只能做一做梦了……"
                        $ fz.xinji = fz.xinji + 20
                        $ fz.qingxiang = fz.qingxiang + 5
                    "绝无可能！":
                        "[fz.hao][fz.weifen] [fz.name]" "[fz.name]脸上的笑容顿时消失了。她愣了一下，眼底似乎有什么东西破碎了。"
                        $ fz.qingxiang -= 5
                        $ fz.like = fz.like - 2
                        "[fz.hao][fz.weifen] [fz.name]" "（过了一会儿。）"
                        "[fz.hao][fz.weifen] [fz.name]" "本宫乏了，[my.cheng]你自便吧。"
                        hide fz
                        hide screen Palacebuttons
                        jump 皇宫界面
            else:
                $ Feizilike_Up(fz,0.8)
    elif fz.xingge == "安静"and fz.xinji < 700:
        $ Feizilike_Up(fz,0.5)
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]安静垂首听着，只偶尔表达自己的意见。）"
        if fz.xingge1 == False:
            "闲聊中，你发现[fz.name]是一个安静的人。"
            $ fz.xingge1 = True
        else:
            $ Feizilike_Up(fz,0.3)
    elif fz.xingge == "势利"and fz.xinji < 700:
        "[fz.hao][fz.weifen] [fz.name]" "既然入了宫，那就是要争得荣华富贵、光耀门楣，不然，还不如在宫外寻个好人家嫁了。"
        if fz.xingge1 == False:
            "闲聊中，你发现[fz.name]字句不离争名夺利。"
            $ Feizilike_Up(fz,0.5)
            $ fz.xingge1 = True
        else:
            $ lucky = renpy.random.randint(0, 4)
            if lucky == 4:
                "[fz.hao][fz.weifen] [fz.name]" "我最看不起那些惺惺作态的人，总是一副淡泊名利的样子，谁知道他们背后是什么嘴脸呢？"
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，你说是吧？"
                menu:
                    "赞同":
                        "[fz.hao][fz.weifen] [fz.name]" "呵呵，英雄所见略同啊。"
                        $ Feizilike_Up(fz,2)
                    "反对":
                        $ fz.like = fz.like -2
                        "[fz.hao][fz.weifen] [fz.name]" "嘁，难道[my.cheng]就是我所说的那种人么？"
                        "[fz.hao][fz.weifen] [fz.name]" "呵，别误会的，我是说[my.cheng]淡泊名利，可不是说你惺惺作态……"
            else:
                $ Feizilike_Up(fz,0.2)
    else:
        "[fz.hao][fz.weifen] [fz.name]" "（聊的很愉快。）"
        $ Feizilike_Up(fz,renpy.random.randint(2, 8)*0.1)

    if fz.xingge1 == False:
        if fz.xinji < my.xinji:
            "你发现[fz.cheng]似乎是个[fz.xingge]的人。"
            $ fz.xingge1 = True
        else:
            $ lucky = (fz.xinji - my.xinji)/100
            $ lucky = round(lucky) + 1
            $ lucky = renpy.random.randint(0, lucky)
            if lucky == 0:
                "你发现[fz.cheng]似乎是个[fz.xingge]的人。"
                $ fz.xingge1 = True
            else:
                pass
    else:
        pass

    if fz.xinji1 == False:
        if fz.xinji < my.xinji and fz.xinji > 700:
            "看似随意的闲谈中，你却察觉到[fz.cheng]的城府深不可测。"
            $ fz.xinji1 = True
        elif fz.xinji < my.xinji and fz.xinji > 400:
            "闲谈几句，你便察觉到[fz.cheng]的心机可见一斑。"
            $ fz.xinji1 = True
        elif fz.xinji < my.xinji:
            "看似随意的闲谈中，你察觉到[fz.cheng]似乎无甚心机。"
            $ fz.xinji1 = True
        else:
            $ lucky = (fz.xinji - my.xinji)/100
            $ lucky = round(lucky) + 1
            $ lucky = renpy.random.randint(0, lucky)
            if lucky == 0:
                "你对[fz.cheng]的心机有所察觉。"
                $ fz.xinji1 = True
            else:
                pass
    else:
        pass
    return

label 妃嫔互动_投诚:

    $ templist = [x for x in my.friends if x in fz.foes]
    if fz == chuhuan:
        楚欢 忧 "[my.cheng]的话，我怎么听不懂啊……"
    elif fz == taoning and fz.like > 50:
        陶凝 笑 "[my.cheng]的恩情，我自不会忘，你我早该站在一起了。"
        $ fz.friends.append(my)
        $ my.friends.append(fz)
    elif fz.qingxiang < 20 and fz.xinji >= fz.like*7:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]的意思本宫不太明白。"
        "（看起来[fz.name]并不喜好后宫拉帮结派、尔虞我诈之事。）"
    elif len(templist) > 0 and  fz.xinji > 700 and fz.xinji > fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "呵呵，在这深宫中，想要左右逢源也好，两面三刀也好，没有点能耐恐怕反而会折了自己。"
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，本宫觉着你还是少花心思在你无法驾驭的事情上。"
    elif len(templist) > 1 and  fz.xinji > 400 and fz.xinji > fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]说得好听，谁知道背后有什么心思呢？"
        "[fz.hao][fz.weifen] [fz.name]" "不是本宫无情，这是身在深宫，不能没有防备之心呐。"
    elif len(templist) > 2:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]说得再好听，可本宫知道咱们不是一路人，你还是别浪费口舌了！"
    elif fz.xinji < fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "你的心意本宫明白。"
        "[fz.hao][fz.weifen] [fz.name]" "本宫又何尝不视你为心腹体己呢？"
        "[fz.hao][fz.weifen] [fz.name]" "身在后宫，若能互相扶持，自是最好不过。"
        $ my.friends.append(fz)
        $ fz.friends.append(my)
        $ my.exp =my.exp + (beifei-fz.level)
        $ fz.exp =fz.exp + (beifei-my.level)
        python:
            for i in fz.foes:
                i.like -= 10
        "（与[fz.cheng]结怨的妃嫔对你的好感下降了。）"
    elif fz.xinji >= fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]听完你的话，眉头微微皱起，在短暂的犹豫后，却是转移了话题，没有答复。）"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]听完你的话，眉头微微皱起，却是转移了话题，婉转拒绝。）"
    return


label 妃嫔互动_拉拢:

    $ templist = [x for x in my.friends if x in fz.foes]
    if fz == chuhuan:
        楚欢 忧 "[my.cheng]的话，嫔妾怎么听不懂啊……"
    elif fz == taoning and fz.like > 50:
        陶凝 笑 "[my.cheng]的恩情，嫔妾自不会忘，只要[my.cheng]开口，嫔妾定然会站在您的身后。"
        $ fz.friends.append(my)
        $ my.friends.append(fz)
    elif fz.qingxiang < 20 and fz.xinji >= fz.like*7:

        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]的意思嫔妾不太明白。"
        "（看起来[fz.name]并不喜好后宫拉帮结派、尔虞我诈之事。）"
    elif len(templist) > 0 and  fz.xinji > 700 and fz.xinji > fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "（莞尔一笑）请恕嫔妾愚钝，不明白您的意思。"
    elif len(templist) > 1 and  fz.xinji > 400 and fz.xinji > fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "嫔妾自认无法堪当重任，恐怕是您看走了眼。"
    elif len(templist) > 2:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]娘娘，我们不是一路人，您不用多费口舌了！"
    elif fz.xinji < fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "（眼底闪过一丝欣喜）您的意思是……"
        "[fz.hao][fz.weifen] [fz.name]" "能够得到您的赏识是嫔妾的福分。"
        "[fz.hao][fz.weifen] [fz.name]" "嫔妾一定尽心尽力！"
        $ my.friends.append(fz)
        $ fz.friends.append(my)
        $ my.exp =my.exp + (beifei-fz.level)
        $ fz.exp =fz.exp + (beifei-my.level)
        python:
            for i in fz.foes:
                i.like -= 10
        "（与[fz.cheng]结怨的妃嫔对你的好感下降了。）"
    elif fz.xinji >= fz.like*10:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]听完你的话，眉头微微皱起，在短暂的犹豫后，却是转移了话题，没有答复。）"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]听完你的话，眉头微微皱起，却是转移了话题，婉转拒绝。）"
    pass
    return

label 妃嫔互动_送礼:
    call screen kufang(fz = fz)
    return

label 妃嫔互动_赏赐:
    call screen kufang(fz = fz)
    return

label 妃嫔互动_挑拨:

    $ templist = []
    python:
        for i in NPC_fz_list:
            if i == my:
                pass
            elif i == fz:
                pass
            else:
                templist.append(i)
    if len(templist) == 0:
        我 "（没有可以挑拨的对象。）"
    else:
        $ thisfz = fz
        call screen choicefz(templist)
        $ tempfz = fz
        $ fz = thisfz
    menu:
        "添油加醋巧言抹黑[tempfz.hao][tempfz.weifen]":
            if fz.like*5+my.xinji*1.5 > fz.xinji*2:
                $ lucky = renpy.random.randint(0, 10)
            elif fz.like*5+my.xinji*1.5 > fz.xinji*1.5:
                $ lucky = renpy.random.randint(0, 30)
            elif fz.like*5+my.xinji*1.5 > fz.xinji:
                $ lucky = renpy.random.randint(0, 50)
            else:
                $ lucky = renpy.random.randint(0, 80)
        "编造亲身经历污蔑[tempfz.hao][tempfz.weifen]":
            if fz.like*15+my.xinji*0.5 > fz.like*20:
                $ lucky = renpy.random.randint(0, 10)
            elif fz.like*15+my.xinji*0.5 > fz.xinji*15:
                $ lucky = renpy.random.randint(0, 30)
            elif fz.like*15+my.xinji*0.5 > fz.xinji*10:
                $ lucky = renpy.random.randint(0, 50)
            else:
                $ lucky = renpy.random.randint(0, 80)
        "算了":
            return
    if fz.xingge == "活泼" or fz.xingge == "娇纵":
        $ lucky = lucky + 5
    elif fz.xingge == "清冷" or fz.xingge == "安静":
        $ lucky = lucky - 5
    else:
        pass
    if lucky < 10:
        if fz.xingge == "活泼" or fz.xingge == "娇纵":
            "[fz.hao][fz.weifen] [fz.name]" "（忿忿）什么？她竟是这种人！真是欺人太甚！"

        elif fz.xingge == "清冷" or fz.xingge == "安静":
            "[fz.hao][fz.weifen] [fz.name]" "（微微皱眉，眼底隐约有一丝怒意）如你所说，此人是断断不能来往的。"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "此人竟如此可恶？！"
        我 "（看起来[fz.hao][fz.weifen]对[tempfz.hao][tempfz.weifen]已经产生了敌意。）"
        $ fz.foes.append(tempfz)
    elif lucky < 60:
        "[fz.hao][fz.weifen] [fz.name]" "（听完你的话，迟疑了片刻）还有这种事情？"
        "[fz.hao][fz.weifen] [fz.name]" "（叫来宫女）去[tempfz.hao][tempfz.weifen]那边打听打听。"
        我 "（看起来[fz.hao][fz.weifen]并没有完全相信我的话。）"
        我 "（或许应该增强自己的心计或是博得[fz.hao][fz.weifen]更多的信任。）"
    else:
        $ fz.like = fz.like -2
        "[fz.hao][fz.weifen] [fz.name]" "（沉默着看了你几眼）[my.cheng]所言是真？"
        我 "自然。"
        if my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "请恕嫔妾直言，以嫔妾所得到的消息，[tempfz.hao][tempfz.weifen]并未做出那般事。"
        else:
            if fz.xinji > 700:
                "[fz.hao][fz.weifen] [fz.name]" "恕本宫直言，以本宫所得到的消息，[tempfz.hao][tempfz.weifen]并未做出那般事。"
                "[fz.hao][fz.weifen] [fz.name]" "虽不知[my.cheng]究竟是何意，但本宫也断断不过做那一叶障目的蠢事。"

            elif fz.xinji > 400:
                "[fz.hao][fz.weifen] [fz.name]" "若[my.cheng]所言非虚，那就是本宫看走眼了。"
                "[fz.hao][fz.weifen] [fz.name]" "不过，本宫还是相信本宫自己并未看错。"
            elif fz.like > 50:
                "[fz.hao][fz.weifen] [fz.name]" "本宫很想相信你。"
                "[fz.hao][fz.weifen] [fz.name]" "只是本宫更愿意相信自己所看到的。"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "呵？还所言是真？漏洞百出！"
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]想把本宫当枪使？本宫劝你还是别白费力气了。"
        我 "（似乎被识破了……）"
        "[fz.hao][fz.weifen][fz.name]对你的好感降低了。"
        我 "（或许应该增强自己的心计或是博得[fz.hao][fz.weifen]更多的信任。）"
        $ tempfz.like = tempfz.like-5
    return

label 妃嫔互动_离间:

    $ templist = []
    python:
        for i in fz.friends:
            if i == my:
                pass
            else:
                templist.append(i)
    if len(templist) == 0:
        我 "（……[fz.cheng]似乎只与我一人交好。）"
    else:
        $ thisfz = fz
        call screen choicefz(templist)
        $ tempfz = fz
        $ fz = thisfz

        menu:
            "[tempfz.hao][tempfz.weifen]背后使诈陷于你不利之地":
                if fz.like*5+my.xinji*1.5 > fz.xinji*2:
                    $ lucky = renpy.random.randint(0, 10)
                elif fz.like*5+my.xinji*1.5 > fz.xinji*1.5:
                    $ lucky = renpy.random.randint(0, 30)
                elif fz.like*5+my.xinji*1.5 > fz.xinji:
                    $ lucky = renpy.random.randint(0, 50)
                else:
                    $ lucky = renpy.random.randint(0, 80)
            "曾听见[tempfz.hao][tempfz.weifen]说你的坏话……":
                if fz.like*15+my.xinji*0.5 > fz.like*20:
                    $ lucky = renpy.random.randint(0, 10)
                elif fz.like*15+my.xinji*0.5 > fz.xinji*15:
                    $ lucky = renpy.random.randint(0, 30)
                elif fz.like*15+my.xinji*0.5 > fz.xinji*10:
                    $ lucky = renpy.random.randint(0, 50)
                else:
                    $ lucky = renpy.random.randint(0, 80)
            "算了":
                return
        if fz.xingge == "活泼" or fz.xingge == "娇纵":
            $ lucky = lucky + 5
        elif fz.xingge == "清冷" or fz.xingge == "安静":
            $ lucky = lucky - 5
        else:
            pass
        if lucky < 10:
            if fz.xingge == "活泼" or fz.xingge == "娇纵":
                "[fz.hao][fz.weifen] [fz.name]" "（忿忿）什么？她竟是这种人！真是看错了她！"

            elif fz.xingge == "清冷" or fz.xingge == "安静":
                "[fz.hao][fz.weifen] [fz.name]" "（微微皱眉，眼底隐约有一丝怒意）如你所说，此人往后再也不能来往了。"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "此人……竟如此可恶？！"
            我 "（看起来[fz.hao][fz.weifen]和[tempfz.hao][tempfz.weifen]不再交好了。）"
            $ fz.friends.remove(tempfz)
        elif lucky < 60:
            "[fz.hao][fz.weifen] [fz.name]" "（听完你的话，迟疑了片刻）还有这种事情？"
            "[fz.hao][fz.weifen] [fz.name]" "（叫来宫女）去[tempfz.hao][tempfz.weifen]那边打听打听。"
            我 "（看起来[fz.hao][fz.weifen]并没有完全相信我的话。）"
            我 "（或许应该增强自己的心计或是博得[fz.hao][fz.weifen]更多的信任。）"
        else:
            $ fz.like = fz.like -2
            "[fz.hao][fz.weifen] [fz.name]" "（沉默着看了你几眼）[my.cheng]所言是真？"
            我 "自然。"
            if my.level < fz.level:
                "[fz.hao][fz.weifen] [fz.name]" "请恕嫔妾直言，以嫔妾所得到的消息，[tempfz.hao][tempfz.weifen]并未做出那般事。"
            else:
                if fz.xinji > 700:
                    "[fz.hao][fz.weifen] [fz.name]" "恕本宫直言，以本宫所得到的消息，[tempfz.hao][tempfz.weifen]并未做出那般事。"
                    "[fz.hao][fz.weifen] [fz.name]" "虽不知[my.cheng]究竟是何意，但本宫也断断不过做那一叶障目的蠢事。"

                elif fz.xinji > 400:
                    "[fz.hao][fz.weifen] [fz.name]" "若[my.cheng]所言非虚，那就是本宫看走眼了。"
                    "[fz.hao][fz.weifen] [fz.name]" "不过，本宫还是相信本宫自己并未看错。"
                elif fz.like > 50:
                    "[fz.hao][fz.weifen] [fz.name]" "本宫很想相信你。"
                    "[fz.hao][fz.weifen] [fz.name]" "只是本宫更愿意相信自己所看到的。"
                else:
                    "[fz.hao][fz.weifen] [fz.name]" "呵？还所言是真？漏洞百出！"
                    "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]想把本宫当枪使？本宫劝你还是别白费力气了。"
            $ tempfz.like = tempfz.like-5
            我 "（似乎被识破了……）"
            "[fz.hao][fz.weifen][fz.name]对你的好感降低了。"
            我 "（或许应该增强自己的心计或是博得[fz.hao][fz.weifen]更多的信任。）"
    return

label 妃嫔互动_品茶:
    if fz.xingge == "娇纵" and fz.love > my.love:
        "[fz.hao][fz.weifen] [fz.name]" "嗯……这茶尚可，但是比起皇上御赐的，仍要逊色几分。"
    elif fz.xingge == "活泼":
        "[fz.hao][fz.weifen] [fz.name]" "咕噜咕噜咕噜……哇，好解渴啊！"
    elif fz.book >= 80:
        "[fz.hao][fz.weifen] [fz.name]" "“碧云引风吹不断，白花浮光凝碗面。一碗喉吻润，两碗破孤闷。三碗搜枯肠，唯有文字五千卷。”"
    elif fz.book >= 50 and fz.like >= 30:
        "[fz.hao][fz.weifen] [fz.name]" "（浅吟）俗人多泛酒，谁解助茶香。"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "嗯……好茶，好茶！"
    if fz.xinji >= 800 or fz.xinji >= my.xinji:
        "[fz.hao][fz.weifen] [fz.name]" "咦……[my.cheng]怎得不喝？"
    $ Feizilike_Up(fz,1)
    if my.anhai["一B"] == 3:
        $ fz.health -= 10
    elif my.anhai["一B"] == 2:
        $ fz.health -=7
    else:
        $ fz.health -= 5

    $ pincha = True

    return


label 妃嫔互动_斡旋:

    $ templist = []
    python:
        for i in fz.foes:
            if i == my:
                pass
            else:
                templist.append(i)

    $ thisfz = fz
    call screen choicefz(templist)
    $ tempfz = fz
    $ fz = thisfz
    $ lucky = renpy.random.randint(0,100)
    $ tempnum = (fz.like + tempfz.like)*my.huashu["一A"]
    if my.level < fz.level:
        $ zicheng = "嫔妾"
    else:
        $ zicheng = "本宫"
    if lucky <= tempnum:
        $ fz.foes.remove(tempfz)
        if fz.like >= 10:
            "[fz.hao][fz.weifen] [fz.name]" "既然是[my.cheng]出面，那[zicheng]就尚且放下成见……"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "[zicheng]也并非蛮不讲理之人，既然[my.cheng]如此诚恳，那[zicheng]便尚且放下成见……但愿她真如[my.cheng]所说，是[zicheng]有所误解。"

        我 笑 "（看起来[fz.cheng]不再同[tempfz.cheng]交恶了。）"
        $ fz.like -= 12 - my.huashu["一A"]*3
        $ fz.qingxiang -= my.huashu["一A"]*3
    else:
        "[fz.hao][fz.weifen] [fz.name]" "[zicheng]与[tempfz.cheng]积怨已深，怕不是误会二字能够说得清的！"
        我 怒 "（看起来[fz.cheng]拒绝放下对[tempfz.cheng]的成见……）"
        $ fz.like -= 12 - my.huashu["一A"]*3
    return

label 妃嫔互动_讨好:


    if fz.xinji>700:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]面露微笑，但并未多言。）"
        $ Feizilike_Up(fz,0.3)
    elif fz.xinji > my.xinji:
        "[fz.hao][fz.weifen] [fz.name]" "（欣喜）[my.cheng]的嘴可真甜啊。"
        $ Feizilike_Up(fz,0.7)
    else:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]这嘴可比吃了蜜还甜呐。（看起来[fz.name]十分高兴。）"
        $ Feizilike_Up(fz,1)
    if fz.xinji < my.xinji and fz.like > 10 and fz.love>my.love:
        $ lucky = renpy.random.randint(0,10)
        if lucky < 3 and my.shiqin == 0:
            "[fz.hao][fz.weifen] [fz.name]" "罢了，我记得[my.cheng]入宫以来还不曾侍寝吧？"
            "[fz.hao][fz.weifen] [fz.name]" "这后宫里最重要便是要得到皇上的喜欢。"
            "[fz.hao][fz.weifen] [fz.name]" "难得你与本宫投缘，本宫若寻了机会，便在皇上面前替你美言几句。"
            $ mustshiqin = mustshiqin + (beifei-fz.level)*2
        elif lucky < 3:
            "[fz.hao][fz.weifen] [fz.name]" "来人，赏[my.cheng]银子。"
            我 "多谢[fz.cheng]！"
            $ money = money +  3 + (beifei-fz.level)
        elif lucky == 0:
            "[fz.hao][fz.weifen] [fz.name]" "难得你与本宫投缘，本宫若寻了机会，便在皇上面前替你美言几句。"
            $ mustshiqin = mustshiqin + (beifei-fz.level)*2
        else:
            pass
    return
label 妃嫔互动_夸奖:

    if fz.xingge == "娇纵" and my.love > 80:
        "[fz.hao][fz.weifen] [fz.name]" "哎哎哎，嫔妾哪有您说的那么好？"
        "[fz.hao][fz.weifen] [fz.name]" "在这宫里，要皇上喜欢才是好的？不是么？"
        "[fz.hao][fz.weifen] [fz.name]" "您若愿意告诉嫔妾如何讨皇上的喜欢，那嫔妾才是感恩戴德了。"
    elif fz.xingge == "娇纵" and my.love < 25:
        "[fz.hao][fz.weifen] [fz.name]" "哎，不是嫔妾无礼，可这宫里，哪儿都是皇上说了算……皇上不喜欢，说得天花乱坠也白搭啊！"
    elif fz.xingge == "娇纵" and fz.like < 50:
        "[fz.hao][fz.weifen] [fz.name]" "哎，您这么说，可是折煞嫔妾了。嫔妾蒲柳之姿，哪儿能跟您比啊。"
    elif fz.xingge == "势利" and my.love < 20:
        "[fz.hao][fz.weifen] [fz.name]" "哎，不是嫔妾无礼，可这宫里，哪儿都是皇上说了算……皇上不喜欢，说得天花乱坠也白搭啊！您还有别的事儿吗？"
    elif fz.xinji>700:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]盈盈笑着，眼神却深邃无波）[my.cheng]谬赞了。"
        $ Feizilike_Up(fz,0.3)
    elif fz.xinji >500:
        "[fz.hao][fz.weifen] [fz.name]" "（欣喜）[my.cheng]谬赞了。"
        $ Feizilike_Up(fz,0.7)
    else:
        "[fz.hao][fz.weifen] [fz.name]" "嫔妾何德何能，能够得到[my.cheng]如此赞誉呢！（看起来[fz.name]十分高兴。）"
        $ Feizilike_Up(fz,1)
    return
label 妃嫔互动_提点:
    if fz.xinji < 200:
        $ fz.xinji = fz.xinji + 4
    elif fz.xinji < 300:
        $ fz.xinji = fz.xinji + 3
    elif fz.xinji < 500:
        $ fz.xinji = fz.xinji + 2
    else:
        $ fz.xinji = fz.xinji + 1
    if fz.qingxiang > 50:
        $ fz.qingxiang = fz.qingxiang - 1 - round(fz.like*0.02)
    elif fz.qingxiang > 0:
        $ fz.qingxiang = fz.qingxiang - 1
    else:
        pass
    if fz.xingge == "娇纵" or fz.xingge == "势利":
        $ fz.like = fz.like - 1
    else:
        pass
    "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]说的是，嫔妾谨遵教诲。"
    return

label 妃嫔互动_训诫:

    $ fz.yali = fz.yali + 5
    call 训诫妃子 (fz=fz) from _call_训诫妃子
    return
label 妃嫔互动_挑衅:

    $ fz.yali = fz.yali + 5
    $ fz.like = fz.like - 5
    $ my.qingxiang = my.qingxiang + 5

    if fz.xinji>700:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]竟仍是面带微笑，只用一双深邃的眼睛凝视着你。）"
    elif fz.xinji >500:
        "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]冷笑着，面色愠怒）好你个[my.name]，可真是伶牙俐齿啊！"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "你！你竟敢这样说！"
    if fz.xinji > fz.like * 10:
        if my in fz.friends:
            $ fz.friends.remove(my)
        elif my not in fz.foes:
            $ fz.foes.append(my)
        else:
            pass

    $ lucky = renpy.random.randint(0, 4)
    if fz.xingge == "娇纵" and lucky > 0 and my not in fz.friends and my.level - fz.level > 3:
        call 被妃子责罚 (fz=fz) from _call_被妃子责罚
    elif fz.xingge != "安静" and lucky > 1 and my in fz.foes and my.level - fz.level > 3:
        call 被妃子责罚 (fz=fz) from _call_被妃子责罚_1
    elif lucky > 3 and my not in fz.friends and my.level - fz.level > 3:
        call 被妃子责罚 (fz=fz) from _call_被妃子责罚_2
    else:
        if mapname == "寝居":
            "[fz.hao][fz.weifen] [fz.name]" "唉，本宫今日原本精神不错，怎的一来了[my.cheng]这里便觉着乏得很。"
            "[fz.hao][fz.weifen] [fz.name]" "本宫先告辞了。"
            hide fz
            hide screen Palacebuttons
            jump 寝居
        else:

            "[fz.hao][fz.weifen] [fz.name]" "唉，本宫今日原本精神不错，怎的[my.cheng]一来便觉着乏得很。"
            "[fz.hao][fz.weifen] [fz.name]" "看来本宫不能奉陪了。来人，送客。"
            hide fz
            "说完，[fz.cheng]转身回了内殿，宫人们将你送出殿外。"
            "你仿佛听到殿内传出一声愤恨的冷笑……"
            hide screen Palacebuttons
            jump 皇宫界面
    return
label 妃嫔互动_争锋:


    $ zhengfeng = True
    call battle (fz=fz) from _call_battle_6











    return

label 妃嫔互动_恭喜其怀孕:
    $ Feizilike_Up(fz,2)

    "[fz.hao][fz.weifen] [fz.name]" "（眉开眼笑）借[my.cheng]吉言，希望这孩子能平平安安地长大。"
    $ gongxi.remove([fz,"怀孕"])
    return

label 妃嫔互动_恭喜其晋位:
    $ Feizilike_Up(fz,2)

    $ gongxi.remove([fz,"晋位"])
    "[fz.hao][fz.weifen] [fz.name]" "（甚喜）多谢[my.cheng]了。"
    return

label 妃嫔互动_恭喜其得嗣:
    $ Feizilike_Up(fz,2)

    $ gongxi.remove([fz,"生产"])
    "[fz.hao][fz.weifen] [fz.name]" "（眉开眼笑）也是多亏了皇上龙恩庇佑，才能平安生下皇嗣。"
    return

label 妃嫔互动_感谢其美言:
    $ Feizilike_Up(fz,2)

    $ ganxie.remove([fz,"美言"])
    "[fz.hao][fz.weifen] [fz.name]" "这点小事，不必挂怀。"
    return

label 妃嫔互动_感谢其提拔:
    $ Feizilike_Up(fz,2)

    $ ganxie.remove([fz,"提拔"])
    "[fz.hao][fz.weifen] [fz.name]" "这点小事，不必挂怀。"
    return

label 妃嫔互动_奚落其小产:
    $ fz.like = fz.like -5

    $ xiluo.remove([fz,"小产"])
    "[fz.hao][fz.weifen] [fz.name]" "（被提及伤心事，隐隐动怒）哼，也不知[my.cheng]有没有这个福气了！"
    return

label 妃嫔互动_奚落其降位:
    $ fz.like = fz.like -5
    $ xiluo.remove([fz,"降位"])
    "[fz.hao][fz.weifen] [fz.name]" "（愠怒）等皇上消了气……一定会将本宫恢复原位的！"
    return

label 妃嫔互动_奚落其失宠:
    $ fz.like = fz.like -5

    $ xiluo.remove([fz,"失宠"])
    "[fz.hao][fz.weifen] [fz.name]" "（愠怒）风水轮流转，你得意什么！"
    return

label 妃嫔互动_离开:
    if my.level < fz.level:
        "[fz.hao][fz.weifen] [fz.name]" "恭送[my.cheng]！"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]慢走。"
    hide fz
    hide screen Palacebuttons
    jump 皇宫界面

label 妃嫔互动_送客:
    if my.level < fz.level:
        "[fz.hao][fz.weifen] [fz.name]" "嫔妾告退。"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "那本宫便先回了。"
    hide fz
    hide screen Palacebuttons
    jump 寝居界面

label 妃嫔互动_关于阿檀……:
    if fz.like - fz.qingxiang > 0:
        $ atan_help.append(0)
        if fz.xingge == "活泼":
            "[fz.hao][fz.weifen] [fz.name]" "（大哭）这天底下居然有如此痴心的女子！"
            "[fz.hao][fz.weifen] [fz.name]" "[fz.Gongnv[0].name]，快去掖廷传本宫的旨意，让他们安排将阿檀姑娘接入后宫！"
        elif fz.xingge == "温婉" or fz.xingge == "清冷" or fz.xingge == "安静":
            "[fz.hao][fz.weifen] [fz.name]" "（听完后沉默了许久）她……还好吧？"
            "[fz.hao][fz.weifen] [fz.name]" "本宫会让掖廷去安排的，去跟她说一声，让她养好身子，以后好好陪着皇上身边。"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "呜……"
            "[fz.hao][fz.weifen] [fz.name]" "罢了罢了，把她接进后宫吧，能不能得皇上欢欣，那便不是本宫能做主的了！"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "故事倒是讲得不错。"
        "[fz.hao][fz.weifen] [fz.name]" "哈，[my.cheng]真想让本宫开口把她接到后宫？那还是算了罢。"
    return


label 被妃子责罚(fz):
    menu:
        "止住话头":
            $ fz.qingxiang = fz.qingxiang + 1
            "[fz.hao][fz.weifen]-[fz.name]" "[my.name]，今天你对本宫说的这些话，最好别让皇上知道。"
            "[fz.hao][fz.weifen]-[fz.name]" "小心治你一个不敬之罪！"
            if fz.level == 0 or fz.palace == my.palace and fz.level < 4:
                if fz.level == 0:
                    "[fz.hao][fz.weifen]-[fz.name]" "本宫身为一宫之主，若任由你在后宫中放肆，若哪日你得罪了皇上、太后，怕本宫也要落得个不敬之罪！"
                else:
                    "[fz.hao][fz.weifen]-[fz.name]" "本宫身为你的主位，若任由你在后宫中放肆，若哪日你得罪了皇上、太后，怕本宫也要落得个不敬之罪！"
                "[fz.hao][fz.weifen]-[fz.name]" "来人，传本宫的命令，[my.cheng]以下犯上，视宫规为无物，即日起禁足三月。"
                hide fz
                show gn at chara
                "[gn.level] [gn.name]" "（冷淡）[my.cheng]，请回吧。"
                hide gn
                hide screen Palacebuttons
                if my.love > 50 and my.love > fz.love and hdxingge != "刚正" and hdxingge !="冷漠"  and hdxingge !="腹黑":
                    scene 寝居
                    show 我的宫女 at chara
                    我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                    我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                    $ fz.like = fz.like - 5
                    $ fz.love = fz.love - 2
                    hide 我的宫女
                    jump 寝居界面
                elif my.love > 80 and my.love > fz.love and hdxingge != "温柔" and hdxingge !="风流":
                    scene 寝居
                    show 我的宫女 at chara
                    我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                    我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                    $ fz.like = fz.like - 5
                    $ fz.love = fz.love - 5
                    hide 我的宫女
                    jump 寝居界面
                else:
                    $ my.tags.append(["禁足三月",0,""])
                    jump 寝居界面
            else:
                "[fz.hao][fz.weifen]-[fz.name]" "[fz.Gongnv[0].name]，送客！"
                hide fz
                show gn at chara
                "[gn.level] [gn.name]" "（冷淡）[my.cheng]，请回吧。"
                hide gn
                hide screen Palacebuttons
                jump 皇宫界面
        "变本加厉":
            $ fz.yali += 5
            $ fz.qingxiang = fz.qingxiang + 2
            if my in fz.friends:
                $ fz.friends.remove(my)
            elif my not in fz.foes:
                $ fz.foes.append(my)
            else:
                pass
            if huaiyun(my) == True:
                "[fz.hao][fz.weifen]-[fz.name]" "到底是有孕在身的人么……本宫现在的确动不了你。"
                "[fz.hao][fz.weifen]-[fz.name]" "不过，你可要小心些了……"
                "[fz.hao][fz.weifen]-[fz.name]" "[fz.Gongnv[0].name]，送客！"
                show gn at chara
                "[gn.level] [gn.name]" "（冷淡）[my.cheng]，请回吧。"
                hide fz
                hide gn
                hide screen Palacebuttons
                jump 皇宫界面
            elif fz.level < 4 and havetag("身受杖责",my) == False:
                "[fz.hao][fz.weifen]-[fz.name]" "本宫不欣赏你别的，就欣赏你这副勇气。"
                "[fz.hao][fz.weifen]-[fz.name]" "真当本宫没脾气么？"
                "[fz.hao][fz.weifen]-[fz.name]" "你以下犯上，本宫给了你勇气，却半点不止悔改！若本宫再容忍你放肆，岂不是置宫规于不顾！"
                "[fz.hao][fz.weifen]-[fz.name]" "来人，将[my.cheng]送到掖庭，杖责二十！"
                hide fz
                show 我的宫女 at chara
                我的宫女 "（跪倒在地）不可！娘娘不可啊！（小声）[my.cheng]，您还是先认个错吧！杖责二十……您千金贵体如何能够承受啊！"
                hide 我的宫女
                show fz at chara
                menu:
                    "求饶":
                        if fz.xingge == "安静" or fz.xingge == "清冷":
                            $ my.yali += 5
                            "[fz.hao][fz.weifen]-[fz.name]" "早知如此，何必当初！"
                            "[fz.hao][fz.weifen]-[fz.name]" "回去抄写宫规百遍，再有下次，本宫直接告知皇上！"
                            "[fz.hao][fz.weifen]-[fz.name]" "[fz.Gongnv[0].name]，送客！"
                            hide fz
                            show gn at chara
                            "[gn.level] [gn.name]" "（冷淡）[my.cheng]，请回吧。"
                            hide gn
                            hide screen Palacebuttons
                            jump 皇宫界面
                        else:
                            $ my.yali += 30
                            "[fz.hao][fz.weifen]-[fz.name]" "现在知道怕了？"
                            "[fz.hao][fz.weifen]-[fz.name]" "可惜，晚了。"
                            "[fz.hao][fz.weifen]-[fz.name]" "来人！"
                            "伴随[fz.cheng]的一声令下，宫人们围上前来，押着你去到掖庭，一路上，引起不少人的注意……"
                            hide screen Palacebuttons
                            scene black
                            with fade
                            show 掖庭太监 at chara
                            "掖庭太监" "哎呀，[my.cheng]，真是得罪了！"
                            hide 掖庭太监
                            "粗重的棍棒一下一下地落在你的身上……"
                            "仿佛过了许久，惩罚终于结束……"
                            "你被宫人送回了自己的寝居之中。"
                            $ my.tags.append(["身受杖责",0,""])
                            $ beizhangze20 = True
                            $ beizhangzetime = 0
                            "（因为被杖责导致身体虚弱，接下来六个回合内，体力会强制减少，最终也不会完全恢复。）"
                            jump 结束本旬
                    "狡辩":

                        $ my.yali += 30
                        hide fz
                        show 我的宫女 at chara
                        我的宫女 "[my.cheng]……"
                        show fz at chara
                        "[fz.hao][fz.weifen]-[fz.name]" "有趣，还真当有不怕死的呢。"
                        "[fz.hao][fz.weifen]-[fz.name]" "本宫已经给我你机会了，你既然不珍惜，也就别怪本宫无情！"
                        "[fz.hao][fz.weifen]-[fz.name]" "来人！"
                        "伴随[fz.cheng]的一声令下，宫人们围上前来，押着你去到掖庭，一路上，引起不少人的注意……"
                        hide screen Palacebuttons
                        scene black
                        with fade
                        show 掖庭太监 at chara
                        "掖庭太监" "哎呀，[my.cheng]，真是得罪了！"
                        hide 掖庭太监
                        "粗重的棍棒一下一下地落在你的身上……"
                        "仿佛过了许久，惩罚终于结束……"
                        "你被宫人送回了自己的寝居之中。"
                        $ my.tags.append(["身受杖责",0,""])
                        $ beizhangze20 = True
                        $ beizhangzetime = 0
                        "（因为被杖责导致身体虚弱，接下来六个回合内，体力会强制减少，最终也不会自然完全恢复。）"
                        jump 结束本旬
            else:
                $ my.yali += 15
                "[fz.hao][fz.weifen]-[fz.name]" "本宫不欣赏你别的，就欣赏你这副勇气。"
                "[fz.hao][fz.weifen]-[fz.name]" "真当本宫没脾气么？"
                "[fz.hao][fz.weifen]-[fz.name]" "你以下犯上，本宫给了你勇气，却半点不止悔改！若本宫再容忍你放肆，岂不是置宫规于不顾！"
                "[fz.hao][fz.weifen]-[fz.name]" "来人，将[my.cheng]拖到殿外，跪上三个时辰。"
                "（[fz.cheng]的宫人走上前来，将你拖出殿外。）"
                hide screen Palacebuttons
                scene 妃嫔寝居外
                with fade
                "[my.cheng]的声音从殿内传来……"
                "[fz.hao][fz.weifen]-[fz.name]" "给本宫看好她！需跪足了才可离开！"
                "宫人们" "是！"
                "你只能跪在粗糙的地面上，整整三个时辰……"
                $ AP = 0
                $ timenum = timenum + 1
                "三个时辰后，你终于能够起身，只觉得双腿酸软无力，难受至极。"
                $ my.health = my.health - 20
                jump 皇宫界面


label 训诫妃子(fz):
    $ zefafeizi = False
    $ suibianzefa = False
    menu:
        "晓之以理":
            if fz.xinji>700 and fz.xingge == "娇纵":
                "[fz.hao][fz.weifen]-[fz.name]" "（微笑）[my.cheng]说的是，嫔妾往后一定谨言慎行。"
                $ suibianzefa = True
                $ zefafeizi = False
            elif fz.xinji >500 and fz.xingge == "娇纵":
                $ fz.like = fz.like - 1
                "[fz.hao][fz.weifen]-[fz.name]" "[my.cheng]说的是，嫔妾明白了。"
                "[fz.hao][fz.weifen]-[fz.name]" "（小声嘲讽）这[my.cheng]是不是闲得慌？咳咳，嫔妾什么也没说，您定是听茬了。"
                $ suibianzefa = True
                $ zefafeizi = True
            elif fz.xinji >500:
                "[fz.hao][fz.weifen]-[fz.name]" "[my.cheng]说的是，嫔妾谨遵教诲。"
                $ zefafeizi = False
                $ suibianzefa = True
            elif fz.xinji >500 and fz.xingge == "娇纵":
                $ fz.like = fz.like - 2
                "[fz.hao][fz.weifen]-[fz.name]" "（看起来不情不愿。）嫔妾明白了。"
                $ suibianzefa = True
                $ zefafeizi = True
            elif fz.xinji <200 and fz.xingge == "娇纵":
                $ fz.like = fz.like - 3
                "[fz.hao][fz.weifen]-[fz.name]" "[my.cheng]有这功夫管教嫔妾，还不如多对自己多上点心思呢。"
                $ zefafeizi = True
                $ suibianzefa = True
            else:
                $ lukcy = renpy.random.randint(0, 3)
                if lucky <3:
                    $ suibianzefa = True
                    $ zefafeizi = False
                    "[fz.hao][fz.weifen]-[fz.name]" "（低垂着头，煞是谦逊）嫔妾受教了。"
                else:
                    $ suibianzefa = False
                    $ zefafeizi = True
                    "[fz.hao][fz.weifen]-[fz.name]" "（看起来不情不愿。）嫔妾明白了。"
        "蛮横指责":
            $ fz.yali = fz.yali + 5
            $ fz.qingxiang = fz.qingxiang + 1
            $ fz.like = fz.like - 4
            if fz.xinji>700:
                $ suibianzefa = True
                $ zefafeizi = False
                "[fz.hao][fz.weifen]-[fz.name]" "（[fz.name]竟仍是面带微笑）[my.cheng]说的是。"
                "[fz.hao][fz.weifen]-[fz.name]" "无论是宫规，还是道义，嫔妾都会铭记于心。"
            elif fz.xinji >500:
                $ suibianzefa = True
                $ zefafeizi = True
                "[fz.hao][fz.weifen]-[fz.name]" "（[fz.name]面色中带着几分愠怒，但仍是竭力强忍着，未失礼数）是，嫔妾知错。"
            else:
                $ zefafeizi = True
                $ suibianzefa = False
                "[fz.hao][fz.weifen]-[fz.name]" "（脸上满是愠怒）[my.cheng]，您这说的是什么话？嫔妾什么时候得罪了您么？"
        "故意挑刺":
            $ fz.yali = fz.yali + 10
            $ fz.qingxiang = fz.qingxiang + 2
            $ fz.like = fz.like - 8
            if fz.xinji>700:
                $ zefafeizi = True
                $ suibianzefa = True
                "[fz.hao][fz.weifen]-[fz.name]" "（[fz.name]竟仍是面带微笑）[my.cheng]说的是。"
                "[fz.hao][fz.weifen]-[fz.name]" "无论是宫规，还是道义，嫔妾都会铭记于心。"
            elif fz.xinji >500:
                $ zefafeizi = True
                $ suibianzefa = True
                "[fz.hao][fz.weifen]-[fz.name]" "（[fz.name]面色中带着几分愠怒，但仍是竭力强忍着，未失礼数）是，嫔妾知错。"
            else:
                $ zefafeizi = True
                $ suibianzefa = False
                if fz.xingge == "娇纵":
                    "[fz.hao][fz.weifen]-[fz.name]" "你！你说什么！[my.cheng]，你不要颠倒黑白，空口污蔑于我！"
                elif fz.xingge == "势利":
                    "[fz.hao][fz.weifen]-[fz.name]" "你！你说什么！[my.cheng]，你仗着自己位分比我高，就故意刁难我，你不觉得自己很可笑么！"
                elif fz.xingge == "安静" or fz.xingge == "温婉":
                    "[fz.hao][fz.weifen]-[fz.name]" "[my.name]，虽然您的位分在嫔妾之上，但若不能以理服人，让外人听去了只会抹黑您自己的名声。"
                else:
                    "[fz.hao][fz.weifen]-[fz.name]" "[my.name]，嫔妾何错之有，还请您明示！"

    menu:
        "就此作罢":
            hide 我的宫女
            我 "（转念一想，只得作罢）"
            我 "本宫不想同你一般见识。[fz.cheng]，你好自为之罢。"
            我 "说完，你转身离去，却听到身后传来愤恨的冷哼声……"

            hide screen Palacebuttons
            jump 皇宫界面
        "仍要责罚" if zefafeizi == True:
            $ fz.qingxiang = fz.qingxiang + 1
            hide fz
            show 我的宫女 at chara
            if suibianzefa == False:
                我的宫女 "[my.cheng]，[fz.cheng]如此无礼，您应当让她长个教训。"
                hide 我的宫女
            else:
                我的宫女 "（忧虑）[my.cheng]，这事儿咱们似乎不太占理，传出去只怕影响您的声誉啊……"
                menu:
                    "作罢":
                        hide 我的宫女
                        我 "（转念一想，只得作罢）"
                        我 "本宫不想同你一般见识。[fz.cheng]，你好自为之罢。"
                        我 "说完，你转身离去，却听到身后传来愤恨的冷哼声……"

                        hide screen Palacebuttons
                        jump 皇宫界面
                    "坚持":
                        pass
    menu:
        "禁足三月" if my.level == 0 or my.level < 4 and my.palace == fz.palace:
            hide 我的宫女
            show fz at chara
            if my.level == 0:
                我 "本宫身为一宫之主，若任由你在后宫中放肆，若哪日你得罪了皇上、太后，怕本宫也要落得个不敬之罪！"
            else:
                我 "本宫身为你的主位，若任由你在后宫中放肆，若哪日你得罪了皇上、太后，怕本宫也要落得个不敬之罪！"
            我 "来人，传本宫的命令，[fz.cheng]以下犯上，视宫规为无物，即日起禁足三月。"
            "[fz.hao][fz.weifen]-[fz.name]" "（似是不甘）嫔妾遵命。"
            hide fz
            if fz.love > 50 and fz.love > my.love and hdxingge != "刚正" and hdxingge !="冷漠"  and hdxingge !="腹黑":
                scene 寝居
                with dissolve
                show 我的宫女 at chara
                我的宫女 "主子，皇上知道[fz.cheng]被您禁足的事情了。"
                我的宫女 "皇上觉得你大题小做，已经免了[fz.cheng]的禁足了。"
                我 "……知道了。"
                $ my.love = my.love - 2
                $ fz.like = fz.like - 5
                hide 我的宫女
                jump 寝居界面
            elif fz.love > 80 and fz.love > my.love and hdxingge != "温柔" and hdxingge !="风流":
                scene 寝居
                with dissolve
                show 我的宫女 at chara
                我的宫女 "主子，皇上知道[fz.cheng]被您禁足的事情了。"
                我的宫女 "皇上觉得你大题小做，已经免了[fz.cheng]的禁足了。"
                我 "……知道了。"
                $ fz.like = fz.like - 5
                $ my.love = my.love - 5
                hide 我的宫女
                jump 寝居界面
            else:
                $ fz.tags.append(["禁足三月",0,""])
                $ fz.like = fz.like - 5
                jump 寝居界面


        "杖责二十" if my.level < 4 and fz.level - my.level > 3 and havetag("身受杖责",fz) == False:
            if my in fz.friends:
                $ fz.friends.remove(my)
            else:
                pass
            if fz in my.friends:
                $ my.friends.remove(fz)
            else:
                pass
            if my not in fz.foes:
                $ fz.foes.append(my)
            else:
                pass
            if fz not in my.foes:
                $ my.foes.append(fz)
            else:
                pass
            $ fz.qingxiang = fz.qingxiang + 2

            $ fz.yali += 30

            if huaiyun(fz) == True or fz.health <= 200 or fz.state == "病重":
                show gn at chara
                "[gn.level] [gn.name]" "[my.cheng]！请您三思啊！[fz.cheng]的身子如何能够承受？就算[fz.cheng]有错在先，也请您看在她的身子的份上，饶了她这一次吧！"
                hide gn
                "然而她话未说完，宫人已经按照你的命令将[fz.cheng]拖了出去。"
            else:
                "宫人按照你的命令将[fz.cheng]拖了出去。"
            $ fz.tags.append(["身受杖责",0,""])
            scene black
            "[fz.cheng]哭喊着求饶的声音传了很远很远……"
            $ feizibeizhangze = True
            $ fz.health = (fz.health - 200)*0.5
            if suibianzefa == True:
                $ fz.like = fz.like - 80
                $ feizibeizhangze = True
            else:

                $ feizibeizhangze = False
                $ fz.like = fz.like - 60
            $ beizhangzefz.insert(0,fz)
            hide screen Palacebuttons
            jump 皇宫界面

        "殿外罚跪" if fz.level - my.level > 3:
            if my in fz.friends:
                $ fz.friends.remove(my)
            elif my not in fz.foes:
                $ fz.foes.append(my)
            else:

                pass
            if fz in my.friends:
                $ my.friends.remove(fz)
            elif fz not in my.foes:
                $ my.foes.append(fz)
            else:
                pass
            我 "给本宫到长庭上跪着！不到三个时辰，不许离开！"
            $ fz.yali += 15
            show fz at chara
            if suibianzefa == True:
                $ fz.like = fz.like - 20
                "[fz.hao][fz.weifen]-[fz.name]" "（虽是不服，奈何身份低微，只得垂首遵命）是。"
            else:
                $ fz.like = fz.like - 10
                "[fz.hao][fz.weifen]-[fz.name]" "[my.cheng]！（心下一惊，但碍于宫规却也只得咬牙）是……"

            $ fz.health = fz.health - 50
            $ fz.qingxiang = fz.qingxiang +5
            hide screen Palacebuttons
            jump 皇宫界面
        "罚抄宫规":


            $ fz.yali += 5
            我 "[fz.cheng]，你以下犯上，无礼于本宫，本宫罚你抄写宫规百遍，你可服气？"
            show fz at chara
            if suibianzefa == True:
                $ fz.like = fz.like - 8
                "[fz.hao][fz.weifen]-[fz.name]" "（虽是不服，奈何身份低微，只得垂首遵命）是。"
            else:
                $ fz.like = fz.like - 4
                "[fz.hao][fz.weifen]-[fz.name]" "（似是长舒了一口气）嫔妾遵命。"
            hide fz
            我 "[fz.cheng]，你好自为之罢。"
            我 "（转身离去。）"
            if fz.like < 20 and my in fz.friends:
                $ fz.friends.remove(my)
            else:
                pass
            if fz.like < 20 and fz in my.friends:
                $ my.friends.remove(fz)
            else:
                pass
            if fz.like < 0 and my not in fz.foes:
                $ fz.foes.append(my)
            else:
                pass
            if fz.like < 0 and fz not in my.foes:
                $ my.foes.append(fz)
            else:
                pass

            hide screen Palacebuttons
            jump 皇宫界面

label 宫中偶遇争锋(fz):

    if my.level >= zhu.level:
        "[fz.hao][fz.weifen] [fz.name]" "倒巧了，正好碰见[my.cheng]。"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "嫔妾见过[my.cheng]。"
    menu:
        "视而不见" if my.level < zhu.level:
            "[fz.hao][fz.weifen] [fz.name]" "……"
            $ fz.like -= 3
            hide fz
        "热络闲聊（增加好感）" if zhu.like >= 0:
            "[fz.cheng]同你闲聊几句，便各自告别离开了。"
            $ Feizilike_Up(fz,1)
            hide fz
        "寒暄几句（争锋）":
            "[fz.cheng]同你闲聊几句，却不想起了口舌争锋……"
            menu:
                "开始争锋":
                    call battle (fz=fz) from _call_battle_7
                "避而不战":












                    python:
                        fz.yali -= 10
                        a = len(yuanweifen)
                        if fz.level == 0: 
                            b = 6
                        elif fz.qinjunum == 1: 
                            b = 5
                        elif fz.level > a-a*0.6:
                            b = 3
                        else:
                            b = 4
                        if my.level == 0: 
                            c = 6
                        elif my.qinjunum == 1: 
                            c = 5
                        elif my.level > a-a*0.6:
                            c = 3
                        else:
                            c = 4
                        tempstory2 ="【争锋】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"意欲向"+ str(my.hao)+str(my.weifen)+str(my.name)+"发起争锋，不战而胜。\n"
                        allstory.insert(0,tempstory2)
                        fz.qingxiang = fz.qingxiang + 1
                        fz.exp += b + (b-c)*2
                    if my.level >= fz.level:
                        $ zicheng = "本宫"
                    else:
                        $ zicheng = "嫔妾"
                    if fz.xingge == "圆滑":
                        "[fz.hao][fz.weifen] [fz.name]" "能屈能伸，非凡俗人，[my.cheng]真是让[zicheng]敬佩呢。"
                    elif fz.xingge == "安静" or fz.xingge == "温婉":
                        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]和善温良，倒是[zicheng]莽撞了，真叫人惭愧。"
                    elif fz.xinji >= 700:
                        "[fz.hao][fz.weifen] [fz.name]" "（收起方才的锋芒，含笑看了你一眼，并未多言。）"
                    elif fz.level >= my.level:
                        "[fz.hao][fz.weifen] [fz.name]" "（一脸得意。）[my.cheng]承让了。"
                    else:
                        "[fz.hao][fz.weifen] [fz.name]" "（一脸得意。）还算有自知之明。"
            if fz.level >= my.level:
                "[fz.hao][fz.weifen] [fz.name]" "嫔妾不多叨扰，先告退了。"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "本宫先走了，[my.cheng]跪安吧。"

            hide fz
            $ AP = AP - 1
            $ timenum = timenum + 1
    return

label 宫中偶遇交好(fz):
    if fz.xingge == "活泼":
        if timenum == 1:
            if fz.level <= my.level:
                if month > 1 and month < 5:
                    $ temptext = "杏果"
                elif month > 4 and month < 8:
                    $ temptext = "枇杷"
                elif month > 7 and month < 11:
                    $ temptext = "柿子"
                else:
                    $ temptext = "冬桃"
                "远远瞧去，便见着[fz.cheng]正在一树下蹦着，不会便手里忽接着了什么，活蹦乱跳的。"
                妃子 "[my.cheng]？怎也这般早。"
                "瞧，这是这树结的果子，[my.cheng]也尝尝喏。"
                "直接将手中的果子递给了你，你仔细看，发觉是[temptext]，婢女帮你剥开后你一尝，味道竟不错。"
                妃子 "唔～好甜！"
            else:
                if month > 1 and month < 5:
                    $ temptext = "杏果"
                elif month > 4 and month < 8:
                    $ temptext = "枇杷"
                elif month > 7 and month < 11:
                    $ temptext = "柿子"
                else:
                    $ temptext = "冬桃"
                "远远瞧去，便见着[fz.cheng]正在一树下蹦着，不会便手里忽接着了什么，活蹦乱跳的。"
                妃子 "见过[my.cheng]。"
                妃子 "瞧，这是这树结的果子，[my.cheng]也尝尝喏。"
                "直接将手中的果子递给了你，你仔细看，发觉是[temptext]，婢女帮你剥开后你一尝，味道竟不错。"
                妃子 "唔～好甜！"
        elif timenum == 2:

            if fz.level <= my.level:
                $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    $ temptext = "花香藕"
                elif lucky == 1:
                    $ temptext = "七翠羹"
                elif lucky == 2:
                    $ temptext = "银芽鸡丝"
                elif lucky == 3:
                    $ temptext = "雪菜黄鱼"
                else:
                    $ temptext = "水晶虾"
                "遥遥看去，便见着一倩影行色匆匆，待人走近。"
                妃子 "[my.cheng]可是要上哪？"
                "与她正打算闲聊一番，却见其奴婢凑上其耳畔。"
                $ gn = fz.Gongnv[0]
                show gn
                "[gn.level] [gn.name]" "主子，还不回去饭菜可要凉喏。"
                hide gn
                show 妃子
                妃子 "哦哦哦对！今儿午膳可有[temptext]呢！"
                妃子 "膳已备好，我便不与你多说咯，得先行回去才是。"
            else:

                $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    $ temptext = "花香藕"
                elif lucky == 1:
                    $ temptext = "七翠羹"
                elif lucky == 2:
                    $ temptext = "银芽鸡丝"
                elif lucky == 3:
                    $ temptext = "雪菜黄鱼"
                else:
                    $ temptext = "水晶虾"
                "遥遥看去，便见着一倩影行色匆匆，待人走近。"
                妃子 "呀！见过[my.cheng]。"
                $ gn = fz.Gongnv[0]
                show gn
                "[gn.level] [gn.name]" "主子，还不回去饭菜可要凉喏。"
                hide gn
                show 妃子
                妃子 "哦哦哦对！今儿午膳可有[temptext]呢！"
                妃子 "那个，嫔妾还得回去用膳，便跪安喏。"
        elif timenum == 3 or timenum == 4:
            if fz.level <= my.level:
                $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    $ temptext = "蟋蟀"
                elif lucky == 1:
                    $ temptext = "毛虫"
                elif lucky == 2:
                    $ temptext = "银芽鸡丝"
                elif lucky == 3:
                    $ temptext = "瓢虫"
                else:
                    $ temptext = "蝈蝈"
                "其蹲在丛边，似在仔细观察着些什么，很是投入，见着你来了，便笑着迎上。"
                妃子 "是[my.cheng]呀。"
                妃子 "快瞧，这有蚂蚁在搬一只[temptext]。"
                我 "噢？嫔妾还未见过喏。"
                "凑近一瞧，那些蚂蚁果真一块驮着那[temptext]，步子还挺快的，不知要搬多久喏。"
            else:
                $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    $ temptext = "蟋蟀"
                elif lucky == 1:
                    $ temptext = "毛虫"
                elif lucky == 2:
                    $ temptext = "银芽鸡丝"
                elif lucky == 3:
                    $ temptext = "瓢虫"
                else:
                    $ temptext = "蝈蝈"
                "其蹲在丛边，似在仔细观察着些什么，很是投入，见着你来了，便笑着迎上。"
                妃子 "见过[my.cheng]。"
                妃子 "快瞧，这有蚂蚁在搬一只[temptext]。"
                我 "噢？我还未见过呢。"
                "凑近一瞧，那些蚂蚁果真一块驮着那[temptext]，步子还挺快的，不知要搬多久喏。"
        elif timenum == 5:
            if fz.level <= my.level:
                "夜已深，可前头却有微光闪烁，待光近些，才发现是[fz.cheng]。其似藏着什么东西，见到是你后，便舒了口气般。"
                妃子 "[my.cheng]怎在这？！"
                我 "那是？"
                妃子 "嘘，莫要声张，只是我去御膳房弄了些吃食，可要来我宫里里头一同尝尝？"
            else:

                "夜已深，可前头却有微光闪烁，待光近些，才发现是[fz.cheng]。其似藏着什么东西，见到是你后，便舒了口气般。"
                妃子 "[my.cheng]？！啊，见过[my.cheng]。"
                我 "那是？"
                妃子 "嘘，莫要声张，只是嫔妾去御膳房弄了些吃食，可要来嫔妾宫里里头一同尝尝？"
        else:
            pass
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
