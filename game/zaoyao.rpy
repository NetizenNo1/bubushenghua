init python:
    class zaoyao(object):
        def __init__(self,zhu,bei,way,time1,time2,hemou,gn,jilv,state):
            self.zhu = zhu 
            self.bei = bei 
            self.way = way 
            self.time1 = time1 
            self.time2 = time2 
            self.hemou = hemou
            self.gn = gn
            self.state = state 
            self.jilv = jilv 
        def __eq__(self, other):
            """python中的对象是否相等有两个层面，一个层面是是否是同一个对象，及在内存中是否共用一个内存区域，
            用is判断，另一个是对象的值是否相等，用==判断"""
            return self.__dict__ == other.__dict__

    def zaoyaojilv(self):
        if self.zhu == my:
            if diwei(self.zhu) == 0:
                self.jilv += 15
            elif diwei(self.zhu) == 1:
                self.jilv += 10
            elif diwei(self.zhu) == 2:
                self.jilv += 5
            else:
                self.jilv += 0
            self.jilv += round((self.zhu.xinji-500)*0.05)
        else:
            if diwei(self.zhu) == 0:
                self.jilv += 60
            elif diwei(self.zhu) == 1:
                self.jilv += 40
            elif diwei(self.zhu) == 2:
                self.jilv += 30
            else:
                self.jilv += 20
            self.jilv += round((self.zhu.xinji-500)*0.05)
        
        for i in self.hemou:
            if diwei(i) == 0:
                self.jilv += 25
            elif diwei(i) == 1:
                self.jilv += 20
            elif diwei(i) == 2:
                self.jilv += 12
            else:
                self.jilv += 6
            self.jilv += round((i.xinji-500)*0.02)
        
        for i in self.gn:
            self.jilv += i.yexin*0.02
            if "散播消息" in i.skill:
                self.jilv += 20
        if self.jilv >= 100:
            self.jilv = 100
        elif self.jilv <= 0:
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
        if self.bei == chuhuan or self.bei == taoning:
            self.jilv = self.jilv*0.5
        
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
            self.jilv -= self.jilv*0.5
        elif  self.bei.fangyu["二A"] == 2:
            self.jilv -= self.jilv*0.75
        elif  self.bei.fangyu["二A"] == 3:
            self.jilv -= self.jilv
        
        return self.jilv

    def zaoyao_cha(self):
        self.time2 -= 1
        if diwei(self.bei) == 0:
            self.jilv -= 12
        elif diwei(self.bei) == 1:
            self.jilv -= 10
        elif diwei(self.bei) == 2:
            self.jilv -= 8
        else:
            self.jilv -= 4
        if hdxingge == "刚正" or hdxingge == "腹黑":
            self.jilv -= 8
        elif hdxingge == "风流" or hdxingge == "冷漠":
            if self.bei.love >= 80:
                self.jilv -= 10
            elif self.bei.love >= 60:
                self.jilv -= 8
            elif self.bei.love >= 40:
                self.jilv -= 6
            elif self.bei.love >= 20:
                self.jilv -= 4
            else:
                pass
        else:
            self.jilv -= 5
        self.jilv += round((self.zhu.xinji-500)*0.02) + renpy.random.randint(0, 5)
        self.jilv -= round((self.bei.xinji-500)*0.02) + renpy.random.randint(0, 5)



    def zaoyao_cheng(self,skills):
        
        c = int(len(weifen_list)*0.5)
        a = 20*self.way + (weifen_list[c][3])*0.5
        if diwei(self.bei) >= 2:
            a = a*0.75
        elif diwei(self.bei) >= 3:
            a = a*0.5
        else:
            pass
        
        if self.way == 0:
            a = a*0.8
            a = a * (100+skills)*0.01
            if a < 0:
                a = 0
            self.bei.love -= 5
            self.bei.taihoulike -= 5
            self.bei.qingxiang += 2
            self.zhu.qingxiang +=2
            for i in self.hemou:
                i.qingxiang += 2
            self.bei.tags.append(["禁足一月",0,""])
        elif self.way == 1:
            a = a
            a = a * (100+skills)*0.01
            if a < 0:
                a = 0
            self.bei.love -= 10
            self.bei.taihoulike -= 10
            self.bei.qingxiang += 4
            self.zhu.qingxiang +=4
            for i in self.hemou:
                i.qingxiang += 4
            self.bei.tags.append(["禁足三月",0,""])
        elif self.way == 2:
            a = a*1.5
            a = a * (100+skills)*0.01
            if a < 0:
                a = 0
            self.bei.love -= 15
            self.bei.taihoulike -= 15
            self.bei.qingxiang += 6
            self.zhu.qingxiang +=6
            for i in self.hemou:
                i.qingxiang += 6
            self.bei.tags.append(["禁足半年",0,""])
        else:
            pass
        for i in self.zhu.Gongnv:
            if i in self.gn :
                if i.state == "任务中":
                    i.state = "寻常"
        for i in self.hemou:
            for j in i.Gongnv:
                if j in self.gn:
                    if j.state == "任务中":
                        j.state = "寻常"
        if self.bei.love >= 80:
            a = a*0.75
        elif self.bei.love >= 60:
            a = a*0.8
        elif self.bei.love >= 40:
            a = a*0.9
        else:
            pass
        a = int(a)
        self.bei.exp -= a
        if tags[4] in self.bei.tags:
            self.bei.tags.remove(tags[4])
        else:
            pass
        zysj.remove(self)
        zysj_end.insert(0,self)
        self.state = 0


    def zaoyao_bai(self,skills):
        self.state = 1
        c = int(len(weifen_list)*0.5)
        a = 20*self.way + (weifen_list[c][3])*0.5
        if diwei(self.zhu) >= 2:
            a = a*0.75
        elif diwei(self.zhu) >= 3:
            a = a*0.5
        else:
            pass
        
        
        if self.way == 0:
            a = a*0.5
            self.bei.qingxiang += 2
            self.zhu.qingxiang -=2
            for i in self.hemou:
                i.qingxiang -= 2
        elif self.way == 1:
            a = a*0.8
            self.bei.qingxiang += 4
            self.zhu.qingxiang -=4
            for i in self.hemou:
                i.qingxiang -= 4
        elif self.way == 2:
            a = a
            self.bei.qingxiang += 6
            self.zhu.qingxiang -=6
            for i in self.hemou:
                i.qingxiang -= 6
        else:
            pass
        if diwei(self.bei) == 0 or self.bei.love >= 80:
            a = a*1.5
        elif diwei(self.bei) == 1 or self.bei.love >= 60:
            a = a*1.25
        elif diwei(self.bei) == 2 or self.bei.love >= 40:
            a = a
        else:
            a = 0.8*a
        a = int(a)
        self.bei.exp += 0.1*a
        a = a * (100+skills)*0.01
        if a < 0:
            a = 0
        self.zhu.exp -= a
        self.zhu.love = self.zhu.love - self.way*2 - a*0.1
        self.zhu.taihoulike -= 5 + self.bei.taihoulike*0.1
        if self.zhu == my:
            self.bei.like -= 10 + a*0.1
        if self.zhu not in self.bei.foes:
            self.bei.foes.append(self.zhu)
        if self.zhu in self.bei.friends:
            self.bei.friends.remove(self.zhu)
        if self.bei not in self.zhu.foes:
            self.zhu.foes.append(self.bei)
        if self.bei in self.zhu.friends:
            self.zhu.friends.remove(self.bei)
        for i in self.zhu.Gongnv:
            if i in self.gn :
                self.zhu.Gongnv.remove(i)
        for i in self.hemou:
            i.exp -= 0.5*a
            i.tags.append(["禁足一月",0,""])
            i.love -= a*0.05
            i.taihoulike -= a*0.05
            for j in i.Gongnv:
                if j in self.gn:
                    i.Gongnv.remove(j)
            if self.bei not in i.foes:
                i.foes.append(self.bei)
            if self.bei in i.friends:
                i.friends.remove(self.bei)
            if i not in self.bei.foes:
                self.bei.foes.append(i)
            if i in self.bei.friends:
                self.bei.friends.remove(i)
        self.bei.exp += 0.1*a
        if skills < -50:
            pass
        elif skills < 0:
            self.zhu.tags.append(["禁足一月",0,""])
        else:
            self.zhu.tags.append(["禁足三月",0,""])
        
        if tags[4] in self.bei.tags:
            self.bei.tags.remove(tags[4])
        else:
            pass
        zysj.remove(self)
        zysj_end.insert(0,self)



    def myzaoyao_gc(sj):
        global AP
        global timenum
        tempnum = round((sj.zhu.xinji-500)*0.02) + renpy.random.randint(0, 5) + 5 - diwei(my)
        if tempnum<= 1:
            tempnum = 1
        elif tempnum >= 25:
            tempnum = 25
        else:
            pass
        if sj.zhu == my and sj.bei.xingge1 == False:
            tempnum = tempnum*0.5
        if sj.zhu == my and sj.bei.xinji1 == False:
            tempnum = tempnum*0.5
        
        sj.jilv += tempnum
        if sj.jilv >= 200:
            sj.jilv = 200
        elif sj.jilv <= 0:
            sj.jilv = 0
        else:
            pass
        AP -= 1
        timenum += 1
        if AP <= 0 or timenum >= 5:
            renpy.jump("结束本旬")
        else:
            pass
        return






label NPC造谣准备:
    python:
        tempfzlist = []
        for i in NPC_fz_list:
            if i.state == "病重" or jinzu(i) == True or i.qingxiang < 50 or i == my  or tags[4] in i.tags or yuli(i) == False or fengfei(i) == True:
                pass
            else:
                tempfzlist.append(i)
        tempfzlist = sorted(tempfzlist, key=attrgetter("qingxiang"),reverse = True)
        if len(tempfzlist) == 0:
            pass
        else:
            fz1 = renpy.random.choice(tempfzlist)
            tempfzlist2 = []
            for i in NPC_fz_list:
                if i.state == "病重" or jinzu(i) == True or tags[4] in i.tags or fengfei(i) == True:
                    pass
                elif i == fz1:
                    pass
                elif i == my and fz1.like >= fz1.qingxiang:
                    pass
                elif i in fz1.friends:
                    pass
                else:
                    tempfzlist2.append(i)
            if fz1 in tempfzlist2:
                tempfzlist2.remove(i)
            else:
                pass
            tempfzlist2 = sorted(tempfzlist2, key=attrgetter("love"),reverse = True)
            tempnum = renpy.random.randint(0,50)
            if tempnum <= fz1.qingxiang*0.1:
                pass
            else:
                tempfzlist2 = []
            if len(tempfzlist2) == 0:
                pass
            else:
                fz2 = renpy.random.choice(tempfzlist2)
                newzysj = zaoyao(zhu= fz1,bei= fz2,way=0,time1=0,time2=0,hemou=[],gn=[],jilv=0,state=999)
                a = len(yuanweifen)
                if fz1.level == 0: 
                    newzysj.way = renpy.random.choice([0,0,0,0,0,1,1,1,1,2,2,2])
                elif fz1.qinjunum == 1: 
                    newzysj.way = renpy.random.choice([0,0,0,0,1,1,1,2,2])
                elif fz1.level > round(a-a/3):
                    newzysj.way = renpy.random.choice([0,0,0,0,0,0,0,1,1,1,1,1,2])
                else:
                    newzysj.way = renpy.random.choice([0,0,0,0,0,1,1,1,2,2])
                if newzysj.way == 0:
                    newzysj.time1 = 3
                    newzysj.time2 = 4
                elif newzysj.way == 1:
                    newzysj.time1 = 6
                    newzysj.time2 = 7
                else:
                    newzysj.time1 = 9
                    newzysj.time2 = 10
                
                newzysj.state = 999
                for i in fz1.friends:
                    if i in fz2.foes or fz2 in i.foes:
                        if i in newzysj.hemou :
                            pass
                        else:
                            lucky = renpy.random.randint(0,10)
                            if lucky <= i.qingxiang*0.1:
                                newzysj.hemou.append(i)
                            else:
                                pass
                for i in fz2.foes:
                    if i in fz1.friends or fz1 in i.friends:
                        if i in newzysj.hemou :
                            pass
                        else:
                            lucky = renpy.random.randint(0,10)
                            if i.qingxiang >= 50 and lucky <= i.qingxiang*0.1:
                                newzysj.hemou.append(i)
                            else:
                                pass
                if fz1.level == 0: 
                    if len(newzysj.hemou)>= 3:
                        newzysj.hemou = [newzysj.hemou[0],newzysj.hemou[1],newzysj.hemou[2]]
                    else:
                        pass
                elif fz1.qinjunum == 1: 
                    if len(newzysj.hemou)>= 2:
                        newzysj.hemou = [newzysj.hemou[0],newzysj.hemou[1]]
                    else:
                        pass
                elif fz1.level > round(a-a/3):
                    if len(newzysj.hemou)>= 0:
                        newzysj.hemou = []
                    else:
                        pass
                else:
                    if len(newzysj.hemou)>= 1:
                        newzysj.hemou = [newzysj.hemou[0]]
                    else:
                        pass
                tempgnlist = []
                for j in newzysj.zhu.Gongnv:
                    if j == newzysj.zhu.Gongnv[0]:
                        pass
                    else:
                        tempgnlist.append(j)
                for i in newzysj.hemou :
                    for j in i.Gongnv:
                        if j == i.Gongnv[0]:
                            pass
                        else:
                            tempgnlist.append(j)
                if fz1.level == 0: 
                    if len(tempgnlist)>= 4:
                        newzysj.gn = [tempgnlist[0],tempgnlist[1],tempgnlist[2],tempgnlist[3]]
                    else:
                        newzysj.gn = tempgnlist
                elif fz1.qinjunum == 1: 
                    if len(tempgnlist)>= 3:
                        newzysj.gn = [tempgnlist[0],tempgnlist[1],tempgnlist[2]]
                    else:
                        newzysj.gn = tempgnlist
                elif fz1.level > round(a-a/3):
                    if len(tempgnlist)>= 1:
                        newzysj.gn = [tempgnlist[0]]
                    else:
                        newzysj.gn = tempgnlist
                else:
                    if len(tempgnlist)>= 2:
                        newzysj.gn = [tempgnlist[0],tempgnlist[1]]
                    else:
                        newzysj.gn = tempgnlist
                if len(newzysj.gn) == 0 :
                    pass
                else:
                    if my in newzysj.hemou :
                        renpy.call("造谣合谋邀请",self = newzysj,from_current=False)
                    newzysj.jilv = zaoyaojilv(newzysj)
                    zysj_ready.append(newzysj)
                    gdsj.append(newzysj)
                
                
                
                global zysj_ready
    return

label 造谣合谋邀请(self):
    $ fz = self.zhu
    $ tempfz = self.bei
    $ temptext = zyfs[self.way]
    scene 寝居
    show 我的宫女 at chara
    我的宫女 "主子……[fz.cheng]来了。"
    hide 我的宫女
    show fz with fade
    妃子 "（快步走进殿内，神情有些反常。）"
    if fz.level < my.level:
        妃子 "今日不必多礼了，本宫找你有要事相商。"
        我 "娘娘请讲。"
        妃子 "最近有人叫本宫不太愉快，又听闻此人和妹妹也有过节……"
    else:
        妃子 "嫔妾今日贸然来访，还请娘娘见谅。"
        我 "妹妹为何事而来？"
        妃子 "是[tempfz.cheng]……让嫔妾受了莫大的委屈，可凭一人之力也难以挫她的威风……"
        妃子 "罢了，怕是宫里有的是人容不下她呢。"

    "谈话之间，[fz.cheng]竟透露出，自己意欲捏造谣言，让[tempfz.cheng]背上[temptext]的污名……"
    if fz.level < my.level:
        妃子 "不知道妹妹是否愿意借本宫一臂之力呢？"
    else:
        妃子 "不知道娘娘意下如何？"
    menu:
        "答应":
            if fz.level < my.level:
                妃子 "（诡谲一笑）你我果真是同道中人。"
                妃子 "本宫先走了。"
            else:
                妃子 "此事嫔妾定会好好筹备，有您相助，那人这次可是要吃苦头了。"
                妃子 "嫔妾告辞。"
        "婉拒":


            if fz.level < my.level:
                妃子 "本以为妹妹是有胆识之人，莫不是怕了？"
                if fz.xinji >= 700:
                    妃子 "也罢，本宫也不过是随口一说，倒也不会存心去害她。"
                else:
                    妃子 "罢了，即便妹妹不帮本宫，想让她吃点苦头也是轻而易举。"
                妃子 "本宫先走了。"
            else:
                if fz.xinji >= 700:
                    妃子 "嫔妾知道您向来为人宽和，小心谨慎，嫔妾也只是随口一提，您不必放在心上。"
                else:
                    妃子 "罢了，虽然嫔妾不及您威高权重，但想让她吃点苦头也是轻而易举。"
                妃子 "嫔妾告辞。"
            $ self.hemou.remove(my)

    hide fz
    return





label 造谣通知_1(self):
    $ temptext = zyfs[self.way]
    show 我的宫女 at chara
    我的宫女 "主子，如今宫里的人都在议论呢，说是[self.bei.cheng]暗地里[temptext]，就连皇上也知道了。"
    我的宫女 "皇上已经派掖庭的人彻查此事了。"
    menu:
        "知道了":
            pass
    hide 我的宫女
    python:
        renpy.return_statement()

label 造谣通知_2(self):
    $ temptext = zyfs[self.way]
    show 我的宫女 at chara
    我的宫女 "主子，不好了，宫里突然风声四起，都说您[temptext]呢……"
    if my.love >50:
        hide 我的宫女
        "宫人" "皇上到——"
        show 皇帝 at chara with dissolve
        我 "臣妾参见陛下……"
        皇上 "（面色比起平日里有几分沉重）那些流言蜚语，你都听到了罢？"
        我 "既然皇上已知那是流言蜚语，那臣妾也没什么可担心的了。"
        皇上 "嗯，朕自是信你。可若不派人彻查此事，也难以服众，反而会致你于后宫难以立足。"
        我 "臣妾明白。"
        皇上 "此事朕会叮嘱掖庭仔细调查，若有人污蔑于你，朕绝不姑息！"
        我 "谢皇上！"
        皇上 "现下先委屈了，朕还有政事要处理，就先走了。"
        hide 皇帝
    else:
        我的宫女 "不过这些莫须有的事情，咱们也不必过于忧心，皇上已经派掖庭彻查此事，一定会替您讨个清白的。"
        hide 我的宫女
    python:
        renpy.return_statement()

label 造谣通知_3(self):
    show 赵公公 at chara
    赵公公 "[my.cheng]，皇上有旨，还请跟奴才走一趟吧。"
    我 "……是。"
    hide 赵公公
    scene 圣宸宫内
    show screen notify("圣宸宫")
    show 皇帝 at chara
    我 "臣妾参见皇上。"
    皇上 "听说最近宫里有人搬弄是非，污蔑旁人，你怎么说？"
    我 "臣妾……"
    我 "（看样子皇上已经知道[self.bei.cheng]的谣言是我散布……）"
    $ lucky = 0
    menu:
        "承认":
            if hdxingge == "冷漠" or hdxingge == "刚正":
                皇上 "算你识相，没有颠倒黑白，死不认账！"
                $ lucky = lucky + 1
            else:
                皇上 "朕就知道是你。"
        "否认":
            if hdxingge == "温柔" or hdxingge == "风流":
                皇上 "若不是你，那又会是谁？"
                $ lucky = lucky + 1
            else:
                皇上 "朕若非得了确凿的证据，也不会叫你来见朕！"
        "求饶":
            if my.love > tempfz.love:
                皇上 "朕……应当饶你这一次吗？"
                $ lucky = lucky + 1
            else:
                皇上 "早日如此，又何必做出这等卑劣之事？"
    if my.love > tempfz.love:
        $ lucky = lucky +1
    else:
        pass
    if my.familylevel < 4:
        $ lucky = lucky +1
    else:
        pass
    皇上 "朕，对你真的很失望。"
    if my.love >= 20:
        皇上 "够了，先退下，听候发落。"
        我 "是……"
    else:
        皇上 "朕……不想看见你！"
        皇上 "来人，把这个罪妇拖下去！"
    hide 皇帝

    $ YNTD = YouNan(self.zhu)
    $ renpy.call("有难同当",who = self.zhu,from_current=False)
    $ LHDY = LiHua(self.zhu)
    $ renpy.call("梨花带雨",who = self.zhu,from_current=False)
    $ LJXS = LuoJing(self.zhu)
    $ renpy.call("落井下石",who = self.zhu,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.zhu,from_current=False)



    python:
        zaoyao_bai(self,skills)
        renpy.return_statement()

label 造谣通知_4(self):
    $ temptext = zyfs[self.way]
    show 我的宫女 at chara
    我的宫女 "主子，掖庭那边已经查清楚了！"
    我的宫女 "那些说您[temptext]的谣言纯属空穴来风。"
    我的宫女 "而背后……正是[self.zhu.cheng]在搞鬼！"
    我 "居然是她……"
    if my.love >50:
        hide 我的宫女
        "宫人" "皇上到——"
        show 皇帝 at chara with dissolve
        我 "臣妾参见皇上！"
        皇上 "宫里那些谣言，朕都听说了。"
        皇上 "[self.zhu.cheng]用心险恶，此番是委屈你了。"
        我 "还好未能让她得逞，臣妾不委屈。"
        皇上 "你放心，朕不会让你蒙受冤屈。"
        我 "谢陛下！"
        皇上 "朕还有政事要忙，得空了再来看你。"
        我 "是，臣妾恭送陛下。"
        hide 皇帝
    else:
        我的宫女 "皇上已经叫人将[self.zhu.cheng]送到圣宸宫了，一定会好好发落她的！"
        hide 我的宫女
    $ YNTD = YouNan(self.zhu)
    $ renpy.call("有难同当",who = self.zhu,from_current=False)
    $ LHDY = LiHua(self.zhu)
    $ renpy.call("梨花带雨",who = self.zhu,from_current=False)
    $ LJXS = LuoJing(self.zhu)
    $ renpy.call("落井下石",who = self.zhu,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.zhu,from_current=False)

    python:
        zaoyao_bai(self,skills)
        renpy.return_statement()

label 造谣通知_5(self):
    $ temptext = zyfs[self.way]
    show 我的宫女 at chara
    我的宫女 "主子，掖庭那边已经查清楚了，关于之前[self.bei.cheng][temptext]的谣言纯属空穴来风。"
    我的宫女 "而背后……正是[self.zhu.cheng]在搞鬼！"
    我 "居然是她……"
    $ YNTD = YouNan(self.zhu)
    $ renpy.call("有难同当",who = self.zhu,from_current=False)
    $ LHDY = LiHua(self.zhu)
    $ renpy.call("梨花带雨",who = self.zhu,from_current=False)
    $ LJXS = LuoJing(self.zhu)
    $ renpy.call("落井下石",who = self.zhu,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.zhu,from_current=False)

    python:
        zaoyao_bai(self,skills)
        renpy.return_statement()


label 造谣通知_6(self):
    show 我的宫女 at chara
    我的宫女 "主子，听说皇上如今正为[self.bei.cheng]的事情大发雷霆呢。"
    我 "哦？"
    我 "（看样子皇上彻查无果，已经坐实了[self.bei.cheng]的罪名。）"
    我的宫女 "掖庭的人方才已经请了[self.bei.cheng]去圣宸宫了，不知皇上会如何发落。"
    $ YNTD = YouNan(self.bei)
    $ renpy.call("有难同当",who = self.bei,from_current=False)
    $ LHDY = LiHua(self.bei)
    $ renpy.call("梨花带雨",who = self.bei,from_current=False)
    $ LJXS = LuoJing(self.bei)
    $ renpy.call("落井下石",who = self.bei,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.bei,from_current=False)

    python:
        zaoyao_cheng(self,skills)
        renpy.return_statement()

label 造谣通知_7(self):
    "由于皇上彻查无果，你之前承担的诬名并未被澄清……"
    $ YNTD = YouNan(self.bei)
    $ renpy.call("有难同当",who = self.bei,from_current=False)
    $ LHDY = LiHua(self.bei)
    $ renpy.call("梨花带雨",who = self.bei,from_current=False)
    $ LJXS = LuoJing(self.bei)
    $ renpy.call("落井下石",who = self.bei,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.bei,from_current=False)


    python:
        zaoyao_cheng(self,skills)
        renpy.return_statement()

label 造谣通知_8(self):
    $ temptext = zyfs[self.way]
    show 我的宫女 at chara
    我的宫女 "主子，听说皇上如今正为[self.bei.cheng]的事情大发雷霆呢。"
    我的宫女 "掖廷彻查结果已经坐实了其[temptext]的罪名。"
    我的宫女 "掖庭的人方才已经请了[self.bei.cheng]去圣宸宫了，不知皇上会如何发落。"
    $ YNTD = YouNan(self.bei)
    $ renpy.call("有难同当",who = self.bei,from_current=False)
    $ LHDY = LiHua(self.bei)
    $ renpy.call("梨花带雨",who = self.bei,from_current=False)
    $ LJXS = LuoJing(self.bei)
    $ renpy.call("落井下石",who = self.bei,from_current=False)
    $ skills = -(YNTD+LHDY)+LJXS
    $ renpy.call("不言而信",who = self.bei,from_current=False)


    python:
        zaoyao_cheng(self,skills)
        renpy.return_statement()



label 主角造谣:
    $ fz = my
    $ myzysj = zaoyao(zhu=my,bei=fz,way=0,time1=0,time2=0,hemou=[],gn=[],jilv=0,state=999)

    call screen makeyaoyan()



label 主角造谣_完成:
    python:
        for i in myzysj.gn:
            i.state = "任务中"
        myzysj.jilv = zaoyaojilv(myzysj)
        if myzysj.way == 0:
            myzysj.time1 = 3
            myzysj.time2 = 4
            myzysj.jilv = myzysj.jilv*0.3
        elif myzysj.way == 1:
            myzysj.time1 = 6
            myzysj.time2 = 7
            myzysj.jilv = myzysj.jilv*0.2
        else:
            myzysj.time1 = 9
            myzysj.time2 = 10
            myzysj.jilv = myzysj.jilv*0.1


        zysj_ready.append(myzysj)
        gdsj.append(myzysj)
    hide screen makeyaoyan
    jump 寝居界面


init python:
    def zy_fz():
        global tempfzlist
        tempfzlist = []
        for i in NPC_fz_list:
            if i == my:
                pass
            elif jinzu(i) == True or fengfei(i) == True or tags[4] in i.tags:
                pass
            else:
                tempfzlist.append(i)
    def zy_gn():
        global tempgnlist
        tempgnlist = []
        for i in my.Gongnv:
            if i != my.Gongnv[0] and i.state == "寻常":
                tempgnlist.append(i)
            else:
                pass
        for i in myzysj.hemou :
            for j in i.Gongnv:
                if j == i.Gongnv[0]:
                    pass
                else:
                    tempgnlist.append(j)
    def zy_hemou(who):
        global tempfzlist
        tempfzlist = []
        for i in my.friends:
            if i in who.foes or who in i.foes:
                if i in myzysj.hemou or i in tempfzlist or i.level == beifei:
                    pass
                else:
                    tempfzlist.append(i)
        
        for i in who.foes:
            if i in my.friends or my in i.friends:
                if i in myzysj.hemou or i in tempfzlist or i.level == beifei:
                    pass
                else:
                    tempfzlist.append(i)


screen makeyaoyan():
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
        text "准备散布谣言……"
        hbox spacing 50:

            text "造谣对象"
            if myzysj.bei == my:
                textbutton "{size=25}选择" action Function(zy_fz,),SetVariable("myzysj.hemou",[]),ShowTransient("zy_0")
            else:
                textbutton "{size=25}"+myzysj.bei.hao + myzysj.bei.weifen + myzysj.bei.name action Function(zy_fz,),SetVariable("myzysj.hemou",[]),ShowTransient("zy_0")
        hbox spacing 30:
            text "造谣内容"
            if myzysj.way == 2:
                textbutton "{size=25}"+str(zyfs[myzysj.way]) action SetVariable("myzysj.way",0)
            else:
                textbutton "{size=25}"+str(zyfs[myzysj.way]) action SetVariable("myzysj.way",myzysj.way+1)
        hbox spacing 30:
            text "合谋妃嫔"
            if my.level == 0:
                if len(myzysj.hemou)<= 3:
                    textbutton "{size=25}添加" action Function(zy_hemou,who = myzysj.bei),ShowTransient("zy_1")

                else:
                    textbutton "{size=25}添加"
            elif diwei(my) == 1:
                if len(myzysj.hemou)<= 2:
                    textbutton "{size=25}添加" action Function(zy_hemou,who = myzysj.bei),ShowTransient("zy_1")
                else:
                    textbutton "{size=25}添加"
            elif diwei(my) == 2:
                if len(myzysj.hemou)<= 1:
                    textbutton "{size=25}添加" action Function(zy_hemou,who = myzysj.bei),ShowTransient("zy_1")
                else:
                    textbutton "{size=25}添加"
            else:
                textbutton "{size=25}添加"

            for i in myzysj.hemou:
                textbutton "{size=20}" + i.hao + i.weifen + i.name action RemoveFromSet(myzysj.hemou,i)
        hbox spacing 30:
            for i in myzysj.gn:
                $ temptext2 += i.level+i.name
                $ temptext2 +="  "
            text "派出宫女"
            if my.level == 0:
                if len(myzysj.gn)<= 4:
                    textbutton "{size=25}添加" action Function(zy_gn),ShowTransient("zy_2")
                else:
                    textbutton "{size=25}添加"
            elif diwei(my) == 1:
                if len(myzysj.gn)<= 3:
                    textbutton "{size=25}添加" action Function(zy_gn),ShowTransient("zy_2")
                else:
                    textbutton "{size=25}添加"
            elif diwei(my) == 2:
                if len(myzysj.gn)<= 2:
                    textbutton "{size=25}添加" action Function(zy_gn),ShowTransient("zy_2")
                else:
                    textbutton "{size=25}添加"
            else:
                if len(myzysj.gn)<= 1:
                    textbutton "{size=25}添加" action Function(zy_gn),ShowTransient("zy_2")
                else:
                    textbutton "{size=25}添加"
            for i in myzysj.gn:
                textbutton "{size=20}" + i.level + i.name action RemoveFromSet(myzysj.gn,i)


        hbox spacing 30:
            if myzysj.bei == my or len(myzysj.gn) == 0:
                textbutton "完成"
            else:
                textbutton "完成" action Call("主角造谣_完成")
            textbutton "算了" action Hide("makeyaoyan"),Jump("寝居界面")
            textbutton "说明" action ShowTransient("zy_explain")

screen zy_explain:
    frame:
        background None

        add "gui/frame.webp" zoom 1.5 align (0.5,0.5)
        align (0.5,0.2)
        xsize 1080
        ysize 720
        viewport:
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            has vbox
            text "  " align (0.5,0.02)
            text "造谣对象：已死亡的妃子、冷宫庶人、禁足中妃子、疑罪未名的妃子、疯妃、自己均不可被造谣。"
            text ""
            text "造谣内容：目前已有造谣方式按罪名严重程度分为：欺凌宫人、妄议朝政、不敬先祖。罪名越严重，散播的难度就越大，被造谣者受到的惩罚越严重，如果造谣失败，付出的代价也越大。"
            text ""
            text "合谋妃子：不同地位的妃嫔可以拉拢的人数有不同限制，当“添加”变为灰色不可选择时说明人数已经达到上限，点击已加入合谋的妃子名字，可将其从同谋中删去。\n合谋条件：和被造谣妃子为敌且与玩家交好。\n合谋妃子的地位、心计均能为你提供助益的（当然，也可能成为你的累赘。"
            text ""
            text "派出宫女：不同地位的妃嫔可以派出的宫女人数有不同限制，当“添加”变为灰色不可选择时说明人数已经达到上限，点击已加入委派的宫女名字，可将其删去。\n名字前面带有++的宫女说明她的技能能够提供巨大的增益。"
            text ""
            text "造谣成功与否的判定非常复杂，需要多加琢磨。大体上与造谣者（包括同谋）的心机、地位、宫女的能力以及被造谣者的心机和地位都有关。\n需要注意的是，如果不知道被造谣者的心机和性格的话，难度会增加许多。"
            text ""
            text "计划好谣言时间后，需要一段时间来准备。经过一段时间的调查后，可能会被查出罪名纯属捏造，也可能会落实被造谣者的罪名。"
            text ""
            text ""
            text ""

        textbutton "知道了" action Hide("zy_explain") align (0.5,1.0)



screen zy_0:
    style_prefix "choicemianban"

    $ a = (len(tempfzlist))/3 + 1
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


            for i in tempfzlist:
                $ shuxingmiaoshu(i)
                textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action SetVariable("myzysj.bei",i),Hide("zy_0")
            if len(tempfzlist) - 3*a == 1:
                textbutton ""
            elif len(tempfzlist) - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("zy_0") align (0.5,1.0)


screen zy_1:
    style_prefix "choicemianban"
    $ a = (len(tempfzlist)-1)/3 + 1
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


            for i in tempfzlist:
                if i == my:
                    pass
                else:
                    $ shuxingmiaoshu(i)
                    textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action AddToSet(myzysj.hemou,i),Hide("zy_1")
            if len(tempfzlist)-1 - 3*a == 1:
                textbutton ""
            elif len(tempfzlist)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("zy_1") align (0.5,1.0)

screen zy_2:
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
                if "散播消息" in i.skill:
                    textbutton "{size=25}++"+i.level+i.name action AddToSet(myzysj.gn,i),Hide("zy_2")
                else:
                    textbutton "{size=25}"+i.level+i.name action AddToSet(myzysj.gn,i),Hide("zy_2")
            if len(tempgnlist)-1 - 3*a == 1:
                textbutton ""
            elif len(tempgnlist)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        textbutton "关闭" action Hide("zy_2") align (0.5,1.0)


label 造谣_助_贿赂(what):
    menu:
        "二十两" if money >= 20:
            $ money -= 20
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 1
        "五十两" if money >= 50:
            $ money -= 50
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 2.5
        "一百两" if money >= 50:
            $ money -= 100
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 5
        "算了":
            jump 寝居界面
    $ what.jilv -= int(tempnum)
    if tempnum >= 0:
        "在收到银两后，掖廷的宫人加紧了对此传言的调查，很快就有了新的收获……"
    else:
        "在收到银两后，掖廷的宫人加紧了对此传言的调查，然而被一股强大的势力所察觉，导致适得其反……"
    $ timenum += 1
    jump 寝居界面


label 造谣_委派(what, how):
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
        tempnum = len(tempgnlist)
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
        $ what.jilv -= tempnum
        "在[gn.name]的行动之下，掖廷的调查进度增加了[tempnum]。"
    else:
        $ what.jilv += tempnum
        "在[gn.name]的行动之下，掖廷的调查进度减缓了[tempnum]。"

    $ timenum += 1
    jump 寝居界面



label 造谣_阻_贿赂(what):
    menu:
        "二十两" if money >= 20:
            $ money -= 20
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 1
        "五十两" if money >= 50:
            $ money -= 50
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 2.5
        "一百两" if money >= 100:
            $ money -= 100
            $ tempnum = (my.xinji-what.zhu.xinji)*0.01 + 5
        "算了":
            jump 寝居界面
    $ what.jilv += int(tempnum)
    if tempnum <= 0:
        "在收到银两后，掖廷的宫人故意放慢了对此传言的调查，还收集了一些伪造的证据，然而被一股强大的势力所察觉，导致适得其反……"
    else:
        "在收到银两后，掖廷的宫人故意放慢了对此传言的调查，还收集了一些伪造的证据…………"


    $ timenum += 1
    jump 寝居界面
 
