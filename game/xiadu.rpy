init python:
    class xiadu(object):
        def __init__(self,zhu,bei,way,time1,time2,gn,jieguo,jilv,state,xiaochan,xianyi,zuiren):
            self.zhu = zhu 
            self.bei = bei 
            self.way = way 
            self.time1 = time1 
            self.time2 = time2 
            self.gn = gn
            self.state = state 
            self.jieguo = jieguo 
            self.jilv = jilv 
            self.xiaochan = xiaochan
            self.xianyi = xianyi
            self.zuiren = zuiren
        
        def __eq__(self, other):
            """python中的对象是否相等有两个层面，一个层面是是否是同一个对象，及在内存中是否共用一个内存区域，
            用is判断，另一个是对象的值是否相等，用==判断"""
            return self.__dict__ == other.__dict__

    def xiadujieguo(self):
        self.jieguo = diwei(self.bei) - diwei(self.zhu)
        self.jieguo = self.jieguo * 10
        
        self.jieguo += round((self.zhu.xinji-self.bei.xinji)*0.1)
        
        for i in self.gn:
            tempnum = i.yexin*0.02
            if i.lv == 0:
                self.jieguo += tempnum*1.5
            elif i.lv == 1:
                self.jieguo += tempnum*1.2
            elif i.lv == 2:
                self.jieguo += tempnum
            elif i.lv == 3:
                self.jieguo += tempnum*0.75
            elif i.lv == 4:
                self.jieguo += tempnum*0.5
            else:
                self.jieguo += tempnum*0.2
            if i.xingge == "稳重" :
                self.jieguo += 4
            if "尽忠职守" in i.skill:
                self.jieguo -= 10
        if self.zhu.anhai["二A"] != 0:
            self.jieguo += 7.5*self.zhu.anhai["二A"]
        if self.zhu == self.bei:
            self.jieguo = 1
        elif self.jieguo >= 100 or self.way == 3:
            self.jieguo = 1 
        elif self.jieguo <= 0:
            self.xianyi.append([self.zhu,0-self.jieguo])
            self.jieguo = -1 
        
        else:
            lucky = renpy.random.randint(0,100)
            if lucky <= self.jieguo:
                self.xianyi.append([self.zhu,100-self.jieguo])
                self.jieguo = 1
            
            else:
                self.jieguo = 0  
        
        if self.bei.fangyu["二A"] != 0:
            if self.bei.fangyu["二A"] == 1:
                tempnum = 15
            elif self.bei.fangyu["二A"] == 2:
                tempnum = 30
            elif self.bei.fangyu["二A"] == 3:
                tempnum = 50
            if len(self.xianyi) == 0:
                self.xianyi.append([self.zhu,tempnum])
            else:
                self.xianyi[0][1] = tempnum
        JieDao(self)
        
        
        return self.jieguo

    def xiadujilv(self):
        self.jilv = diwei(self.zhu) - diwei(self.bei)
        self.jilv = self.jilv * 10
        
        self.jilv += round((self.bei.xinji-self.zhu.xinji)*0.5)
        tempnum = 0
        for i in self.gn:
            if self.zhu == my:
                tempnum = i.yexin *0.02
                
                if i.like >= 200:
                    tempnum += 20
                else:
                    tempnum += i.like*0.1
            else:
                tempnum = i.yexin *0.04
            
            if i.lv == 0:
                self.jilv += tempnum*1.5
            elif i.lv == 1:
                self.jilv += tempnum*1.2
            elif i.lv == 2:
                self.jilv += tempnum
            elif i.lv == 3:
                self.jilv += tempnum*0.75
            elif i.lv == 4:
                self.jilv += tempnum*0.5
            else:
                self.jilv += tempnum
            
            if i.xingge == "单纯" :
                self.jilv -= 20
            elif i.xingge == "聪颖":
                self.jilv += 20
        
        if self.zhu.anhai["二A"] != 0:
            self.jilv += 15*self.zhu.anhai["二A"]
        
        self.jilv -= self.bei.medic
        
        if self.jilv <= 0:
            self.jilv = 0
        else:
            self.jilv = int(self.jilv)
        
        if self.zhu.huashu["三级"] != 0:
            for i in self.zhu.friends:
                if i not in NPC_fz_list:
                    pass
                else:
                    self.jilv += 5*self.zhu.huashu["三级"]
        
        if self.zhu == my and self.bei.xingge1 == False:
            self.jilv = self.jilv*0.5
        if self.zhu == my and self.bei.xinji1 == False:
            self.jilv = self.jilv*0.5
        if self.zhu == taoning:
            self.jilv =self.jilv*1.5
        if  self.bei == chuhuan or self.bei == taoning:
            self.jilv = self.jilv*0.5
        if self.zhu == chuhuan :
            self.jilv = 200
        
        if self.zhu.anhai["一A"] == 0:
            pass
        elif  self.zhu.anhai["一A"] == 1:
            self.jilv += self.jilv*0.08
        elif  self.zhu.anhai["一A"] == 2:
            self.jilv += self.jilv*0.18
        elif  self.zhu.anhai["一A"] == 3:
            self.jilv += self.jilv*0.3
        
        if self.bei.fangyu["二A"] == 0:
            pass
        elif  self.bei.fangyu["二A"] == 1:
            self.jilv -= self.jilv*0.15
        elif  self.bei.fangyu["二A"] == 2:
            self.jilv -= self.jilv*0.3
        elif  self.bei.fangyu["二A"] == 3:
            self.jilv -= self.jilv*0.5
        
        
        if self.way == 3 and self.jilv <= 100:
            self.jilv = 200
        
        return self.jilv

    def xiadu_cha(self):
        self.time2 -= 1
        if self.way == 3 :
            pass
        else:
            for i in self.xianyi:
                if i[1] < 0:
                    self.xianyi.remove(i)
                elif i[1] >= 100:
                    self.zuiren = i[0]
                    return
                if len(self.xianyi) == 0:
                    pass
                else:
                    who = renpy.random.choice(self.xianyi)
                    tempnum = 0
                    if diwei(self.bei) == 0:
                        tempnum += 30
                    elif diwei(self.bei) == 1:
                        tempnum += 25
                    elif diwei(self.bei) == 2:
                        tempnum += 20
                    else:
                        tempnum += 15
                    if hdxingge == "腹黑":
                        if who[0] == self.zhu:
                            tempnum += 15
                        else:
                            pass
                    elif hdxingge == "风流" or hdxingge == "冷漠":
                        if who[0].love >= 80:
                            tempnum -= 10
                        elif who[0].love >= 60:
                            tempnum -= 8
                        elif who[0].love >= 40:
                            tempnum -= 4
                        elif who[0].love >= 20:
                            tempnum -= 3
                        else:
                            tempnum -= 0
                    else:
                        pass
                    
                    if hdxingge == "刚正" or hdxingge == "腹黑":
                        tempnum += 5
                    elif hdxingge == "风流" or hdxingge == "冷漠":
                        if self.bei.love >= 80:
                            tempnum += 6
                        elif self.bei.love >= 60:
                            tempnum += 4
                        elif self.bei.love >= 40:
                            tempnum += 3
                        elif self.bei.love >= 20:
                            tempnum += 2
                        else:
                            pass
                    else:
                        tempnum += 3
                    
                    tempnum += int((who[0].xinji-self.bei.xinji)*0.01)
                    if self.bei.fangyu["二A"] == 0:
                        pass
                    elif  self.bei.fangyu["二A"] == 1:
                        tempnum -= tempnum*0.15
                    elif  self.bei.fangyu["二A"] == 2:
                        tempnum -= tempnum*0.3
                    elif  self.bei.fangyu["二A"] == 3:
                        tempnum -= tempnum*0.5
                    who[1] += int(tempnum)
                    if who[1] <= 0:
                        self.xianyi.remove(who)
                    elif who[1] >= 100:
                        self.zuiren = who[0]







    def xiadu_0(self): 
        self.zhu.qingxiang += 5
        if self.way == 0:
            self.zhu.lucky = self.zhu.lucky - 3
            self.bei.qingxiang += 5
        
        elif self.way == 1 and huaiyun(self.bei) == True:
            self.zhu.lucky = self.zhu.lucky - 10
            self.bei.qingxiang += 15
            self.xiaochan = True
        
        
        elif self.way == 1 and huaiyun(self.bei) == False:
            self.zhu.lucky = self.zhu.lucky - 5
            self.bei.qingxiang += 10
        
        elif self.way == 2 or self.way == 3:
            self.zhu.lucky = self.zhu.lucky - 15
            pass
        
        else:
            pass
        xianyi = []
        for i in self.xianyi:
            xianyi.append(i[0])
        
        for i in NPC_fz_list:
            if i in xianyi:
                pass
            elif len(self.xianyi) >= 3:
                pass
            elif jinzu(i) == True or havetag("失心成疯",i) == True:
                pass
            elif self.bei in i.foes:
                xianyi.append(i)
                self.xianyi.append([i,0])
            else:
                pass
        
        
        
        
        
        self.state = 0



    def xiadu_1(self,skills): 
        self.state = 1
        
        c = int(len(weifen_list)*0.5)
        a = 50*self.way + (weifen_list[c][3])
        if diwei(self.zuiren) >= 2:
            a = a*0.75
        elif diwei(self.zuiren) >= 3:
            a = a*0.5
        else:
            pass
        
        if self.way == 0:
            a = a
        elif self.way == 1:
            if self.xiaochan == True:
                a = a*1.5
            else:
                a = a *2
        elif self.way == 2:
            a = a*3
        else:
            pass
        
        if self.zhu == self.zuiren:
            if self.way == 0:
                self.zhu.qingxiang -=3
            elif self.way == 1:
                self.zhu.qingxiang -=5
            elif self.way == 2:
                self.zhu.qingxiang -=10
            else:
                pass
        else:
            if self.way == 0:
                self.zhu.qingxiang +=3
            elif self.way == 1:
                self.zhu.qingxiang +=5
            elif self.way == 2:
                self.zhu.qingxiang +=10
            else:
                pass
        
        if diwei(self.bei) == 0 or self.bei.love >= 80:
            a = a*1.5
        elif diwei(self.bei) == 1 or self.bei.love >= 60:
            a = a*1.2
        elif diwei(self.bei) == 2 or self.bei.love >= 40:
            a = a
        else:
            a = 0.8*a
        
        if diwei(self.zuiren) == 0 :
            a = a*1.8
        elif diwei(self.zuiren) == 1 :
            a = a*1.5
        elif diwei(self.zuiren) == 2 :
            a = a
        else:
            a = 0.8*a
        if self.jieguo == -1 :
            a = 0.5*a
        
        self.bei.exp += 0.1*a
        a = a * (100+skills)*0.01
        if a < 0:
            a = 0
        a = int(a)
        self.zuiren.exp -= a
        self.zuiren.love -= (self.way*5 + a*0.01)
        self.zuiren.taihoulike -= self.way*5 + self.bei.taihoulike*0.2
        if self.zuiren == my :
            self.bei.like -= 10 + a*0.01
        if self.zuiren not in self.bei.foes:
            self.bei.foes.append(self.zuiren)
        if self.zuiren in self.bei.friends:
            self.bei.friends.remove(self.zuiren)
        if self.bei not in self.zuiren.foes:
            self.zuiren.foes.append(self.bei)
        if self.bei in self.zuiren.friends:
            self.zuiren.friends.remove(self.bei)
        for i in self.zuiren.Gongnv:
            if i in self.gn :
                self.zuiren.Gongnv.remove(i)
        
        if self.way == 0:
            self.zuiren.tags.append(["禁足一月",0,""])
        elif self.way == 0 :
            self.zuiren.tags.append(["禁足三月",0,""])
        else:
            self.zuiren.tags.append(["禁足半年",0,""])
        xdsj.remove(self)
        xdsj_end.insert(0,self)

    def myxiadu_gc(sj):
        global AP
        global timenum
        tempnum = round((sj.zhu.xinji-500)*0.02) + renpy.random.randint(0, 5) + 3 - diwei(my)
        if tempnum<= 1:
            tempnum = 1
        elif tempnum >= 10:
            tempnum = 10
        else:
            pass
        sj.jilv += tempnum
        if sj.jilv >= 100:
            sj.jilv = 100
        elif sj.jilv <= 0:
            sj.jilv = 0
        else:
            pass
        AP -= 1
        timenum += 1
        if AP <= 0 or timenum >= 5:
            renpy.jump("寝居界面")
        else:
            pass
        return






label NPC下毒准备:
    python:
        tempfzlist = []
        for i in NPC_fz_list:
            if i.state == "病重" or jinzu(i) == True or i.qingxiang < 50 or diwei(i) == 3 or i == my or tags[4] in i.tags or yuli(i) == False:
                pass
            else:
                tempfzlist.append(i)
        tempfzlist = sorted(tempfzlist, key=attrgetter("qingxiang"),reverse = True)
        if len(tempfzlist) == 0:
            pass
        else:
            fz1 = renpy.random.choice(tempfzlist)
            tempfzlist2 = []
            if fz1 == chuhuan:
                for i in NPC_fz_list:
                    if i.state == "病重" or jinzu(i) == True or tags[4] in i.tags :
                        pass
                    elif i == fz1:
                        pass
                    elif chuhuan not in i.foes:
                        pass
                    elif i == my :
                        pass
                    else:
                        tempfzlist2.append(i)
            else:
                for i in NPC_fz_list:
                    if i.state == "病重" or jinzu(i) == True or tags[4] in i.tags :
                        pass
                    elif i == fz1:
                        pass
                    elif i in fz1.friends:
                        pass
                    elif i == my and fz1.like >= fz1.qingxiang:
                        pass
                    else:
                        tempfzlist2.append(i)
            
            if fz1 in tempfzlist2:
                tempfzlist2.remove(i)
            else:
                pass
            tempfzlist2 = sorted(tempfzlist2, key=attrgetter("love"),reverse = True)
            tempnum = renpy.random.randint(0,100)
            if tempnum <= fz1.qingxiang*0.1 and len(tempfzlist2) != 0:
                fz2 = renpy.random.choice(tempfzlist2)
                a = len(yuanweifen)
                tempitem = []
                if fz1.anhai["初始"] >= 1:
                    tempitem.append(0)
                if fz1.anhai["初始"] >= 2:
                    tempitem.append(1)
                if fz1.anhai["初始"] >= 3:
                    tempitem.append(2)
                if tags[6] in fz2.tags and 1 in tempitem:
                    tempitem.remove(1)
                if len(tempitem) == 0:
                    tempfzlist2 = []
                else:
                    tempitem =  sorted(tempitem, reverse = True)
                    tempway = tempitem[0]
            
            
            else:
                tempfzlist2 = []
            
            if len(tempfzlist2) == 0 :
                pass
            else:
                
                newxdsj = xiadu(zhu=fz1,bei=fz2,way=tempway,time1=0,time2=0,gn=[],jieguo=0,jilv=0,state=999,xiaochan = False,xianyi=[],zuiren=None)
                
                
                
                newxdsj.time1 = 1
                newxdsj.time2 = 7
                tempgnlist = []
                for i in newxdsj.bei.Gongnv:
                    if newxdsj.bei == my and i.yexin <= 200:
                        pass
                    elif i.yexin <= 400:
                        pass
                    elif i in teshugn :
                        pass
                    else:
                        tempgnlist.append(i)
                tempgnlist = sorted(tempgnlist, key=attrgetter("yexin"),reverse = True)
                
                if fz1.level == 0: 
                    a = renpy.random.randint(1,3)
                elif fz1.qinjunum == 1: 
                    a = renpy.random.randint(1,2)
                else:
                    a = 1
                if a >= len(tempgnlist):
                    a = len(tempgnlist)
                else:
                    pass
                if len(tempgnlist) == 0 :
                    newxdsj.gn = []
                elif  a == 1:
                    newxdsj.gn = [tempgnlist[0]]
                elif a == 2:
                    newxdsj.gn = [tempgnlist[0],tempgnlist[1]]
                else:
                    newxdsj.gn = [tempgnlist[0],tempgnlist[1],tempgnlist[2]]
                if len(newxdsj.gn) == 0 and newxdsj.zhu.anhai["二A"] == 0:
                    pass
                else:
                    newxdsj.jilv = xiadujilv(newxdsj)
                    newxdsj.jieguo =xiadujieguo(newxdsj)
                    xdsj_ready.append(newxdsj)
                    gdsj.append(newxdsj)
                
                
                global xdsj_ready
    return

label 下毒无事发生(self):
    if self.way == 0:
        $ temptext = poison01.name
    elif self.way == 1:
        $ temptext = poison02.name
    elif self.way == 2:
        $ temptext = poison03.name
    elif self.way == 3:
        $ temptext = poison04.name
    "[self.bei.cheng]宫中的内应深夜暗中来报，[self.bei.cheng]并未服下那[temptext]……但她也并未察觉出什么异样。"
    python:
        renpy.return_statement()


label 下毒未遂通知(self):
    if self.bei != my:
        "傍晚，[self.bei.cheng]的居处传来一阵喧闹声……"
        show 我的宫女 at chara
        我的宫女 "主子，听说[self.bei.cheng]那里发现了毒药！"
        我的宫女 "还是在[self.bei.cheng]身边宫人身上发现的……不过那宫人投毒未遂，因此[self.bei.cheng]并没有什么大碍。"
        if self.way == 0:
            我的宫女 "太医查验过后发现那毒药能致人容颜禁毁。"
            我的宫女 "哪有女子不爱惜自己容貌的？更何况是宫里的后妃，那下毒之人可真是狠毒啊！"

        elif self.way == 1 and huaiyun(self.bei) == True:
            我的宫女 "太医查验过后发现那毒药能致孕者滑胎！"
            我的宫女 "哪有女子不爱惜自己孩子的？更何况是宫里的后妃，那下毒之人可真是狠毒啊！"

        elif self.way == 1 and huaiyun(self.bei) == False:
            我的宫女 "太医查验过后发现那毒药能致女子不孕！"
            我的宫女 "这宫里的后妃若是不能生育，那境遇可谓是……那下毒之人可真是狠毒啊！"
        else:

            我的宫女 "太医查验过后发现那毒药能夺人性命！"
            我的宫女 "那下毒之人可真是狠毒啊！"
        我的宫女 "涉事的宫人如今已经被带到掖庭了，希望最后能查明真凶是谁。"
        我的宫女 "否则这样的人藏在宫里，可真是叫人害怕。"
    else:
        scene 寝居
        if len(self.gn) != 0:
            $ my.Gongnv.remove(self.gn[0])
            $ gn = self.gn[0]
            $ newgn = renpy.random.choice(YTGongnv)
            $ YTGongnv.remove(newgn)
            $ my.Gongnv.append(newgn)
            $ newgn.level = gn.level
            $ newgn.lv = gn.lv
            show 我的宫女 at chara
            我的宫女 "主子，今日御膳房的饭菜已经呈上来了。"
            hide 我的宫女
            "你正打算用膳，却看到不远处[gn.name]的身影鬼鬼祟祟地闪过……"
            我 "站住！"
            $ gnface = gn.face
            show gn at chara
            "[gn.level] [gn.name]" "奴婢见过主子……"
            我 "你鬼鬼祟祟地干什么？"
            "[gn.level] [gn.name]" "奴、奴婢没有啊！"
            我 "……等等，你袖子里是什么？"
            "[gn.level] [gn.name]" "奴、奴婢……奴婢知错了！奴婢知错了！奴婢一时鬼迷心窍……"
            hide gn
            "你派人告知掖廷，很快，[gn.name]就被拖了下去。"
            if my.love >50:
                show 我的宫女 at chara
                我的宫女 "主子，皇上来了！"
                hide 我的宫女
                show 皇帝 at chara with dissolve
                我 "臣妾参见皇上……皇上……臣妾好怕……"
                皇上 "（叹气）朕都听说了。"
                皇上 "别怕，朕会保护你。"
                我 "陛下……"
                皇上 "朕还有政事要忙，得空了再来看你。放心，有朕在，没人敢动你。"
                我 "是，臣妾恭送陛下……"
                hide 皇帝
            else:
                pass
        else:


            show 我的宫女 at chara
            我的宫女 "主子，今日御膳房的饭菜已经呈上来了。"
            hide 我的宫女
            "你正打算用膳，[my.Gongnv[0].name]突然面色有异……"
            我的宫女 "主子……这饭菜好像有问题……"
            我 "怎么了？"
            我的宫女 "奴婢还是让太医院的大人过来看一看罢。"
            hide 我的宫女
            "片刻后……"
            show 我的宫女
            我的宫女 "主子，这饭菜里竟被人下了毒！"
            我的宫女 "奴婢已经报至掖廷，让他们着手调查了！"
            我 惊 "这是怎么一回事？毒药又是何？"

        if self.way == 0:
            我的宫女 "主子，太医已经查验过了，那毒药能致人容颜禁毁。"
            我的宫女 "哪有女子不爱惜自己容貌的？更何况是宫里的后妃，那下毒之人可真是狠毒啊！"

        elif self.way == 1 and huaiyun(self.bei) == True:
            我的宫女 "主子，太医已经查验过了，那毒药能致孕者滑胎！"
            我的宫女 "哪有女子不爱惜自己孩子的？更何况是宫里的后妃，那下毒之人可真是狠毒啊！"

        elif self.way == 1 and huaiyun(self.bei) == False:
            我的宫女 "主子，太医已经查验过了，那毒药能致女子不孕！"
            我的宫女 "这宫里的后妃若是不能生育，那境遇可谓是……那下毒之人可真是狠毒啊！"
        else:

            我的宫女 "主子，太医已经查验过了，那毒药能夺人性命！"
            我的宫女 "那下毒之人可真是狠毒啊！"
        我的宫女 "幸好您这次无碍……"
        我的宫女 "希望掖庭的人能早日查明真凶。"
        我的宫女 "否则这样的人藏在宫里，可真是叫人害怕。"


    $ tempstory = str(year)+"年"+str(month)+"月，险些为"+str(xdwp[self.way])+"所害，所幸发现及时，并未中毒。\n"
    $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+ str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+ "险些为"+str(xdwp[self.way])+"所害，所幸发现及时，并未中毒。\n"
    $ self.bei.story.append(tempstory)
    $ allstory.insert(0,tempstory2)
    python:
        renpy.return_statement()

label 下毒成功通知(self):
    if self.way == 0:
        $ self.bei.health = self.bei.health -50
        $ self.bei.beauty = (self.bei.beauty -100)*0.5
        if self.bei == my:
            scene 寝居
            "这日用过晚膳，你突然觉得脸上奇痒无比，难受至极。"
            我 "[my.Gongnv[0].name]……[my.Gongnv[0].name]……"
            show 我的宫女 at chara
            我的宫女 "主子，奴婢在……主子？！主子、你的脸……你的脸怎么会……"
            我 "我的脸……怎么了？"
            我的宫女 "主子，您别急，奴婢这就去请太医！"
            hide 我的宫女
            "仿佛过了很久……太医终于赶到。"
            "经过太医的诊治，你的状况终于好转。"
            "却被告知脸上留了印记，容貌已经大不如从前了。"
            if my.love >50:
                show 我的宫女 at chara
                我的宫女 "主子，皇上来了！"
                hide 我的宫女
                show 皇帝 at chara with dissolve
                我 "臣妾参见皇上……皇上……不要看臣妾的脸……"
                皇上 "（叹气）朕都听说了。"
                我 "臣妾好害怕……到底是谁要害臣妾……"
                皇上 "别怕，朕会保护你。"
                我 "陛下……"
                皇上 "朕还有政事要忙，得空了再来看你。你好好休养，按照太医说的来用药，这阵子都小心些。"
                我 "是，臣妾恭送陛下……"
                hide 皇帝
            else:
                pass
        else:
            "这日夜里，[self.bei.cheng]的寝居突然传来一阵喧闹声。"
            show 我的宫女 at chara
            我的宫女 "[my.cheng]，听说[self.bei.cheng]用过晚膳后突然脸上奇痒无比，难受至极。去请了太医来看后，折腾了许久终于好转了些……"
            我的宫女 "不过奴婢听说，[self.bei.cheng]的脸上留了印记，容貌已经大不如从前了。"
            hide 我的宫女
        $ tempstory = str(year)+"年"+str(month)+"月，身中奇毒，容貌被毁。\n"
        $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+ str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+ "身中奇毒，容貌被毁。\n"
        $ self.bei.story.append(tempstory)
        $ allstory.insert(0,tempstory2)
    elif self.way == 1 and huaiyun(self.bei) == True:
        python:
            for j in self.bei.tags:
                if "身怀皇嗣" in j:
                    j[1] = 0
                    self.bei.tags.remove(j)
            self.bei.state = "抱恙"
            self.bei.huaiyun = 0
            self.bei.health = (self.bei.health-100)*0.8
            xiluo.append([self.bei,"小产"])
            renpy.call("不幸小产",fz = self.bei,from_current=False)
    elif self.way == 1 and huaiyun(self.bei) == False:
        if tags[6] not in self.bei.tags:
            $ self.bei.tags.append(tags[6])
        $ self.bei.health = (self.bei.health-100)*0.8
        $ self.bei.lucky -= 20
        if self.bei.lucky >= -20:
            $ self.bei.lucky = -20
        else:
            pass
        "这日夜里，[self.bei.cheng]的寝居突然传来一阵喧闹声。"
        show 我的宫女 at chara
        我的宫女 "[my.cheng]，听说[self.bei.cheng]用过晚膳后突然腹痛不止。去请了太医来看后，才知是饭菜里被人下了麝香……"
        我的宫女 "[self.bei.cheng]以后恐怕再难有孕了……"
        hide 我的宫女
        $ tempstory = str(year)+"年"+str(month)+"月，被下麝香，难再有孕。\n"
        $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+ str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+ "被下麝香，难再有孕。\n"
        $ self.bei.story.append(tempstory)
        $ allstory.insert(0,tempstory2)
    else:

        if self.bei == my:
            jump 非正常死亡
        else:
            python:
                tempstory = str(year)+"年"+str(month)+"月，于寝宫暴毙。\n"
                tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+ "于寝宫暴毙。\n"
                Killfz(self.bei)
                renpy.call("有人死了",fz = self.bei,from_current=False)
    python:
        renpy.return_statement()

label 下毒调查通知(self):
    "掖庭来报——"
    if self.bei == my:
        $ tempcheng = "你"
    else:
        $ tempcheng = self.bei.cheng
    if self.jieguo == 1 and self.zuiren != my:
        if self.way == 0:
            "[tempcheng]身中奇毒、容貌被毁之事已经查明……幕后主使之人乃是[self.zuiren.hao][self.zuiren.weifen][self.zuiren.name]……"
        elif self.way == 1 and self.xiaochan == True:
            "[tempcheng]被麝香所害滑胎之事已经查明……幕后主使之人乃是[self.zuiren.hao][self.zuiren.weifen][self.zuiren.name]……"
        elif self.way == 1 and self.xiaochan == False:
            "[tempcheng]被麝香所害难再有孕之事已经查明……幕后主使之人乃是[self.zuiren.hao][self.zuiren.weifen][self.zuiren.name]……"
        else:
            "[tempcheng]暴毙寝宫之事已经查明……幕后主使之人乃是[self.zuiren.hao][self.zuiren.weifen][self.zuiren.name]……"
    elif self.jieguo == -1 and self.zuiren != my:
        "有人向[tempcheng]投毒未遂之事已经查明……幕后主使之人乃是[self.zuiren.hao][self.zuiren.weifen][self.zuiren.name]……"
    elif self.way < 2 and self.zuiren == my:
        scene 寝居
        $ fz = self.bei
        image fz = "Feizi/F[fz.face].webp"
        show 赵公公 at chara
        赵公公 "[my.cheng]，皇上有旨，还请跟奴才走一趟吧。"
        我 "……是。"
        hide 赵公公
        scene 圣宸宫内
        show screen notify("圣宸宫")
        show 皇帝 at chara
        我 "臣妾参见皇上。"
        hide 皇帝
        show fz at chara
        "[fz.hao][fz.weifen] [fz.name]" "你这个毒妇！"
        hide fz
        show 皇帝 at chara
        皇上 "[my.cheng]，你应当知道朕为什么会召见你。"
        我 "臣妾……"
        hide 皇帝
        show fz at chara
        if self.jieguo == 1 and self.way == 0:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒，致使我容貌被毁！你简直恶毒至极！"
        elif self.jieguo == 1 and self.way == 1 and self.xiaochan == True:

            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒，致使我滑胎！你简直恶毒至极！"
        elif self.jieguo == 1 and self.way == 1 and self.xiaochan == False:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒，致使我再难有孕！你简直恶毒至极！"
        elif self.jieguo == 0 and self.way == 0:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒，想将我的容貌毁去！皇上，如果不是臣妾发现即时，如今臣妾这张脸就已经……就已经……（泣不成声。）"
        elif self.jieguo == 0 and self.way == 1:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒！皇上，如果不是臣妾发现即时，如今后果简直不堪设想啊！（泣不成声。）"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，皇上已经查明，就是你买通了宫人暗中下毒，想取我性命！皇上，如果不是臣妾发现即时，如今臣妾已经……已经再不能陪伴在您身侧了呀！（泣不成声。）"
        hide fz
        show 皇帝 at chara
        皇上 "（望向你）你……还有什么话可说？"
        menu:
            "求饶":
                $ my.qingxiang -= 5
                if hdxingge == "温柔" or hdxingge == "刚正" or hdxingge == "风流":
                    皇上 "（长叹一声）早知如此，何必当初？"
                elif hdxingge == "冷漠":
                    皇上 "朕不想听你这些鬼话！"
                else:
                    皇上 "（幽幽看了你一眼）你在背后只手遮天的时候可曾想过如今可怜乞求的样子？"
            "狡辩":
                $ my.qingxiang += 5
                if hdxingge == "温柔" or hdxingge == "刚正" or hdxingge == "风流":
                    皇上 "事到如今，你说这些还有何用？朕不蠢……[my.cheng]，你真的够了！"
                elif hdxingge == "冷漠":
                    皇上 "你以为掖庭的人都是傻子么？还是说，你把朕当傻子了？！"
                else:
                    皇上 "（似笑非笑）哦，想不到朕的[my.cheng]到了这种时候，还有功夫狡辩呢？"
            "承认":
                皇上 "既然你已承认，那朕也没什么可说的了。"

        皇上 "来人，传朕旨意，将[my.cheng]带回寝宫，听候发落。"
        hide 皇帝
    elif self.way == 2 and self.jieguo == 1 and self.zuiren == my:
        show 赵公公 at chara
        赵公公 "[my.cheng]，皇上有旨，还请跟奴才走一趟吧。"
        我 "……是。"
        hide 赵公公
        scene 圣宸宫内
        show screen notify("圣宸宫")
        show 皇帝 at chara
        我 "臣妾参见皇上。"
        show 皇帝 at chara
        皇上 "[my.cheng]，你应当知道朕为什么会召见你。"
        我 "臣妾……"
        皇上 "朕已经查明，就是你买通了宫人，让她给[self.bei.cheng]下毒，致使她……撒手人寰。"
        if my.love >= 80:
            皇上 "为什么偏偏是你……"
        elif my.love >= 50:
            皇上 "朕真是看错了你……"
        else:
            皇上 "朕不想再听任何解释！"
        皇上 "来人，传朕旨意，将[my.cheng]带回寝宫，听候发落！"
    else:
        pass
    hide 皇帝
    if self.jieguo == 1:
        if self.way == 0:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：毁其容貌者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，以奇毒毁"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"容貌，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以奇毒毁"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"之容貌者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        elif self.way == 1 and self.xiaochan == True:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：致其小产者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"小产，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"小产者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        elif self.way == 1:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：致其难孕者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"不孕，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"不孕者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        else:

            $ tempstory = str(year)+"年"+str(month)+"月，经查：致其丧命者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，以剧毒致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"丧命，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以剧毒致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"丧命者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
    else:
        if self.way == 0:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：意欲毁其容貌者而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，意欲以奇毒毁"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"容貌而未遂，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以奇毒毁"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"之容貌而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        elif self.way == 1 and huaiyun(self.bei) == True:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：意欲致其小产者而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，意欲以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"小产而未遂，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"小产而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        elif self.way == 1:
            $ tempstory = str(year)+"年"+str(month)+"月，经查：意欲致其不孕而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，意欲以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"不孕而未遂，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以麝香致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"不孕而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)
        else:

            $ tempstory = str(year)+"年"+str(month)+"月，经查：意欲使其丧命而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ self.bei.story.append(tempstory)
            $ tempstory = str(year)+"年"+str(month)+"月，意欲以剧毒致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"丧命而未遂，后被查出。\n"
            $ self.zuiren.story.append(tempstory)
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，经查：以剧毒致"+str(self.bei.hao)+str(self.bei.weifen)+str(self.bei.name)+"丧命而未遂者为"+str(self.zuiren.hao)+str(self.zuiren.weifen)+str(self.zuiren.name)+"。\n"
            $ allstory.insert(0,tempstory2)


    $ YNTD = YouNan(self.zuiren)
    $ renpy.call("有难同当",who = self.zuiren,from_current=False)
    $ LHDY = LiHua(self.zuiren)
    $ renpy.call("梨花带雨",who = self.zuiren,from_current=False)
    $ LJXS = LuoJing(self.zuiren)
    $ renpy.call("落井下石",who = self.zuiren,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.zuiren,from_current=False)

    python:
        xiadu_1(self,skills)
        renpy.return_statement()


label 有难同当(who):
    if jinzu(my) == True or my.level == beifei:
        pass
    elif my.huashu["二B"] != 0  and who.like >= 80 or my.huashu["二B"] != 0 and who  in my.friends:
        我 "是否要发动【话术技能——有难同当】营救[who.cheng]？"
        menu:
            "是":
                $ lucky =  renpy.random.randint(0,100)
                $ tempnum = my.xinji*0.1
                if lucky <= tempnum:
                    $ YNTD += 10 + (my.huashu["二B"]-1)*20
                    $ who.like += my.huashu["二B"]*5
                    "【话术技能——有难同当发动成功！】"
                else:
                    "【话术技能——有难同当发动失败。】"
            "否":

                pass
    else:
        pass
    python:
        renpy.return_statement()


label 落井下石(who):
    if my.meishu["二A"] != 0  and who  != my and jinzu(my) == False and my.level != beifei:
        我 "是否要发动【媚术技能——落井下石】让皇上从重处罚？"
        menu:
            "是":
                $ lucky =  renpy.random.randint(0,100)
                $ tempnum = my.love
                if lucky <= tempnum:
                    $ LJXS += my.meishu["二A"]*25
                    $ my.love -= (1000-my.meili)*0.05
                    $ who.like -= my.meishu["二A"]*5
                    "【媚术技能——落井下石发动成功！】"
                else:
                    "【媚术技能——落井下石发动失败。】"
            "否":

                pass
    else:
        pass
    python:
        renpy.return_statement()

label 梨花带雨(who):
    if who == my:
        $ temptext = "为自己开脱"
    else:
        $ temptext = "营救" + who.cheng
    if my.meishu["二B"] != 0  and who.like >= 80 or my.meishu["二B"] != 0 and who  in my.friends or my.meishu["二B"] != 0 and who  == my:
        我 "是否要发动【媚术技能——梨花带雨】[temptext]？"
        menu:
            "是":
                $ lucky =  renpy.random.randint(0,100)
                $ tempnum = my.love
                if lucky <= tempnum:
                    $ my.love -= (1000-my.meili)*0.05
                    $ LHDY += my.meishu["二B"]*25
                    if who != my:
                        $ who.like += my.meishu["二B"]*5
                    "【媚术技能——梨花带雨发动成功！】"
                else:
                    "【媚术技能——梨花带雨发动失败。】"
            "否":

                pass
    else:
        pass
    python:
        renpy.return_statement()

label 不言而信(who):
    if who.fangyu["三级"] != 0 and who != my:
        $ tempnum = 50 + 25*(who.fangyu["三级"] -1)
        $ skills -= tempnum
        $ who.fangyu["三级"] = 0
        "[who.cheng]发动了【自保技能——不言而信】保全自身。"
    elif my.fangyu["三级"] != 0  and who.like >= 80 or my.fangyu["三级"] != 0 and who  in my.friends or my.fangyu["三级"] != 0 and who == my:
        if who == my:
            我 "是否要发动【自保技能——不言而信】保全自身？"
        else:
            我 "是否要发动【自保技能——不言而信】保全[who.cheng]？"
        menu:
            "是":
                $ tempnum = 50 + 25*(my.fangyu["三级"] -1)
                $ skills -= tempnum
                $ my.fangyu["三级"] = 0
                "【自保技能——不言而信已发动。】"
            "否":

                pass
    else:
        python:
            for i in who.friends:
                lucky = renpy.random.randint(0,100)
                if lucky >= i.qingxiang and i != my and i.fangyu["三级"] != 0 and jinzu(i) == False and i.level != beifei:
                    tempnum = 50 + 25*(i.fangyu["三级"] -1)
                    skills -= tempnum
                    i.fangyu["三级"] = 0
                    temptext = i.cheng + "发动了【自保技能——不言而信】保全"+who.cheng+"。"
                    renpy.say(None, temptext)
                else:
                    pass
    python:
        renpy.return_statement()


label 主角下毒:
    $ myxdsj = xiadu(zhu=my,bei=my,way=999,time1=1,time2=7,gn=[],jieguo=0,jilv=0,state=999,xiaochan = False,xianyi=[],zuiren=None)
    call screen makexiadu()





label 主角下毒_完成:
    python:
        for i in myxdsj.gn:
            i.state = "任务中"
        myxdsj.jilv = xiadujilv(myxdsj)
        myxdsj.jieguo =xiadujieguo(myxdsj)
        xdsj_ready.append(myxdsj)
        gdsj.append(myxdsj)
        if myxdsj.way == 0:
            kufang.remove(poison01)
        elif myxdsj.way == 1:
            kufang.remove(poison02)
        elif myxdsj.way == 2:
            kufang.remove(poison03)
        elif myxdsj.way == 3:
            kufang.remove(poison04)
        else:
            pass
    hide screen makexiadu
    if my.anhai["二B"] != 0:
        menu:
            "是否要发动【暗害技能——借刀杀人】指定嫁祸一名妃子？"
            "是":
                python:
                    templist = []
                    for i in NPC_fz_list:
                        if i == my or i == myxdsj.bei:
                            pass
                        elif jinzu(i)== True or havetag("失心成疯",i) == True:
                            pass
                        else:
                            templist.append(i)
                call screen choicefz(templist)
                if my.anhai["二B"] == 1:
                    $ tempnum = 15
                elif my.anhai["二B"] == 2:
                    $ tempnum = 30
                else:
                    $ tempnum = 50
                $ myxdsj.xianyi.append([fz,tempnum])
            "否":
                pass
    if len(myxdsj.gn) == 0:
        $ AP -= 3
    jump 寝居界面


init python:
    def xd_gn():
        global tempgnlist
        tempgnlist = []
        for i in myxdsj.bei.Gongnv:
            if i.state == "内应" :
                tempgnlist.append(i)
            else:
                pass

screen makexiadu():
    style_prefix "gdjm"
    add "gui/frame.webp" zoom 1 xalign 0.45 yalign 0.25
    $ temptext = ""
    $ temptext2 =""
    frame:
        background None
        xsize 900
        ysize 480
        align (0.45,0.3)
        has vbox spacing 50
        text "准备下毒……"
        hbox spacing 50:
            text "下毒对象"
            if myxdsj.bei == my:
                textbutton "{size=25}选择" action ShowTransient("xd_0")
            else:
                textbutton "{size=25}"+myxdsj.bei.hao + myxdsj.bei.weifen + myxdsj.bei.name action ShowTransient("xd_0")
        hbox spacing 30:
            text "使用毒药"
            if myxdsj.way == 999:
                textbutton "{size=25}选择" action ShowTransient("xd_1")

            else:
                textbutton "{size=25}"+str(xdwp[myxdsj.way]) action ShowTransient("xd_1")

        hbox spacing 30:
            for i in myxdsj.gn:
                $ temptext2 += i.level+i.name
                $ temptext2 +="  "
            text "内应宫女"
            if my.level == 0:
                if len(myxdsj.gn)<= 3:
                    textbutton "{size=25}添加" action Function(xd_gn),ShowTransient("xd_2")
                else:
                    textbutton "{size=25}添加"
            elif diwei(my) == 1:
                if len(myxdsj.gn)<= 2:
                    textbutton "{size=25}添加" action Function(xd_gn),ShowTransient("xd_2")
                else:
                    textbutton "{size=25}添加"
            else:
                if len(myxdsj.gn)<= 1:
                    textbutton "{size=25}添加" action Function(xd_gn),ShowTransient("xd_2")
                else:
                    textbutton "{size=25}添加"
            for i in myxdsj.gn:
                textbutton "{size=20}" + i.level + i.name action RemoveFromSet(myxdsj.gn,i)


        hbox spacing 30:
            if myxdsj.bei == my:
                textbutton "完成"
            elif len(myxdsj.gn) == 0 and my.anhai["二A"] == 0:
                textbutton "完成"
            else:
                textbutton "完成" action Call("主角下毒_完成")
            textbutton "算了" action Hide("makexiadu"),Jump("寝居界面")


screen xd_0:
    style_prefix "choicemianban"
    $ a = (len(NPC_fz_list)-1)/3 + 1
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


            for i in NPC_fz_list:
                if i == my:
                    pass
                else:
                    $ shuxingmiaoshu(i)
                    textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action SetVariable("myxdsj.bei",i),Hide("xd_0")
            if len(NPC_fz_list)-1 - 3*a == 1:
                textbutton ""
            elif len(NPC_fz_list)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("xd_0") align (0.5,1.0)


screen xd_1:
    style_prefix "choicemianban"
    $ b = 0
    for i in kufang:
        if i.leibie == "毒药":
            $ b += 1
    $ a = (b-1)/3 + 1
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


            for i in kufang:
                if i == poison01:
                    textbutton "{size=25}"+i.name action SetVariable("myxdsj.way",0),Hide("xd_1")
                elif i == poison02:
                    textbutton "{size=25}"+i.name action SetVariable("myxdsj.way",1),Hide("xd_1")
                elif i == poison03:
                    textbutton "{size=25}"+i.name action SetVariable("myxdsj.way",2),Hide("xd_1")
                elif i == poison04:
                    textbutton "{size=25}"+i.name action SetVariable("myxdsj.way",3),Hide("xd_1")
                else:
                    pass
            if b-1 - 3*a == 1:
                textbutton ""
            elif b-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("xd_1") align (0.5,1.0)

screen xd_2:
    style_prefix "choicemianban"
    $ a = len(tempgnlist)/3 + 1
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


            for i in tempgnlist:
                textbutton "{size=25}"+i.level+i.name action AddToSet(myxdsj.gn,i),Hide("xd_2")
            if len(tempgnlist)-1 - 3*a == 1:
                textbutton ""
            elif len(tempgnlist)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("xd_2") align (0.5,1.0)



label 下毒_助_贿赂(what):
    menu:
        "二十两" if money >= 20:
            $ money -= 20
            $ tempnum = (my.xinji-what[0].xinji)*0.01 + 1
        "五十两" if money >= 50:
            $ money -= 50
            $ tempnum = (my.xinji-what[0].xinji)*0.01 + 2.5
        "一百两" if money >= 100:
            $ money -= 100
            $ tempnum = (my.xinji-what[0].xinji)*0.01 + 5
        "算了":
            jump 寝居界面
    $ what[1] += int(tempnum)
    if tempnum >= 0:
        "在收到银两后，掖廷的宫人搜集了一些对[what[0].cheng]不利的证据……"
    else:
        "在收到银两后，掖廷的宫人试图搜集了一些对[what[0].cheng]不利的证据，然而被一股强大的势力所察觉，导致适得其反……"
    $ timenum += 1
    jump 寝居界面

label 下毒_委派(what, how):
    python:
        tempgnlist = []
        for i in my.Gongnv[1:]:
            if i.state != "寻常":
                pass
            else:
                tempgnlist.append(i)
        tempgnlist = sorted(tempgnlist, key=attrgetter("lv"),reverse = False)
        templist = []
        temptext = ""
        for i in tempgnlist:
            tempnum = i.yexin *0.01
            if i.lv <= 5:
                
                tempnum = tempnum*0.5
            elif i.lv == 4 :
                tempnum = tempnum*0.8
            elif i.lv == 3:
                pass
            elif i.lv == 2:
                tempnum = tempnum*1.2
            else:
                tempnum = tempnum*1.5
            if i.like <= 100:
                pass
            elif 100 < i.like <= 150 :
                tempnum = tempnum * 1.2
            elif i.like >=  150:
                tempnum = tempnum * 1.5
            tempnum = int(tempnum)
            temptext = i.name + "（" + str(tempnum) + "）"
            templist.append([temptext,i])
    "委派的宫女好感越高、职位越高、野心越高，效果越好。"
    call screen choice_zy_gn(list = templist)
    $ tempnum = gn.yexin *0.01
    $ gn.state = "任务中"
    if gn.lv <= 5:
        $ tempnum = tempnum*0.5
    elif gn.lv == 4:
        $ tempnum = tempnum*0.8
    elif gn.lv == 3:
        pass
    elif gn.lv == 2:
        $ tempnum = tempnum*1.2
    else:
        $ tempnum = tempnum*1.5
    if gn.like <= 100:
        pass
    elif 100 < gn.like <= 150:
        $ tempnum = tempnum * 1.2
    elif gn.like >=  150:
        $ tempnum = tempnum * 1.5
    $ tempnum = int(tempnum)
    if how == 0:
        $ what[1] += tempnum
        "在[gn.name]的行动之下，搜集到了一些对[what[0].cheng]不利的证据……其嫌疑增加[tempnum]。"
    else:
        $ what[1] -= tempnum
        "在[gn.name]的行动之下，搜集到了一些能够佐证[what[0].cheng]清白的证据……其嫌疑下降[tempnum]。"

    $ timenum += 1
    jump 寝居界面



label 下毒_阻_贿赂(what):
    menu:
        "二十两" if money >= 20:
            $ money -= 20
            $ what[1] -= 2
        "五十两" if money >= 50:
            $ money -= 50
            $ what[1] -= 5
        "一百两" if money >= 100:
            $ money -= 100
            $ what[1] -= 10
        "算了":
            jump 寝居界面

    "在收到银两后，掖廷的宫人搜集了一些能够佐证[what[0].cheng]清白的证据……"
    $ timenum += 1
    jump 寝居界面
 
