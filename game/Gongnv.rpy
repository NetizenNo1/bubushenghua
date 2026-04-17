


init 2 python:
    list_Gongnvface = list(range(1,127))

    class Gongnv_store(object):
        def select_Gongnv(self):
            pass
        
        def Gongnv_order(self,Gongnv_type):
            return self.select_Gongnv(Gongnv_type)

    class NPC_Gongnv_store(Gongnv_store):
        def select_Gongnv(self, Gongnv_type):
            return Gongnv_factory().select_Gongnv_type(Gongnv_type)


    class Gongnv_factory(object):
        
        def select_Gongnv_type(self,Gongnv_type):
            if Gongnv_type == "宫女":
                return NPC_Gongnv()
            else :
                pass

    class Gongnv_sx(object):
        def __init__(self,name,face,age,beauty,xingge,skill,yexin,master,yexinlv,beautylv,level,like,lv,state,shou):
            self.name = name
            self.face = face
            self.age = age
            self.beauty = beauty
            self.beautylv = beautylv
            self.xingge = xingge
            self.skill = skill
            self.yexin = yexin
            self.yexinlv = yexinlv
            self.master = master
            self.level = level
            self.like = like
            self.lv = lv
            self.state = state
            self.shou = shou
        def __eq__(self, other):
            """python中的对象是否相等有两个层面，一个层面是是否是同一个对象，及在内存中是否共用一个内存区域，
            用is判断，另一个是对象的值是否相等，用==判断"""
            return self.__dict__ == other.__dict__
        
        def Gongnv_random(self):
            self.name = renpy.random.choice(ming_list) + renpy.random.choice(ming_list)
            if len(self.name) >= 3:
                self.name = self.name[0] + self.name[1]
            if self.name in teshuming and self.name in ming_list:
                ming_list.remove(self.name)
            self.age = renpy.random.randint(12,20)
            self.face = renpy.random.choice(list_Gongnvface)
            
            lucky = renpy.random.randint(1,20)
            if lucky == 1:
                self.beauty = renpy.random.randint(700,920)
            elif lucky < 5:
                self.beauty = renpy.random.randint(500,700)
            else :
                self.beauty = renpy.random.randint(50,500)
            
            self.xingge =  renpy.random.choice(["单纯","机灵","稳重","聪颖"])
            self.skill =  []
            self.state = "寻常"
            
            if self.xingge == "单纯":
                self.skill.append("善于交际")
            elif self.xingge == "机灵":
                self.skill.append("花言巧语")
            elif self.xingge == "稳重":
                self.skill.append("心思细腻")
            elif self.xingge == "聪颖":
                self.skill.append("见机行事")
            else:
                pass
            
            lucky = renpy.random.randint(1,5)
            if lucky == 1:
                randomgongnvskill = renpy.random.choice(["尽忠职守","寻医问药","刺探情报","散播消息","挑拨离间"])
                self.skill.append(randomgongnvskill)
            else :
                pass
            
            lucky = renpy.random.randint(1,10)
            if lucky == 1:
                self.yexin = renpy.random.randint(700,920)
            elif lucky > 8:
                self.yexin = renpy.random.randint(400,700)
            else :
                self.yexin = renpy.random.randint(50,400)
            
            self.like = 0
            
            self.shou = renpy.random.randint(45,65)


    class NPC_Gongnv(Gongnv_sx):
        """一中学生."""
        def __init__(self):
            Gongnv_sx.Gongnv_random(self)

    NPC_Gongnv_store = NPC_Gongnv_store() 



    NPC_Gongnv_list = [] 


    def makeGongnv(self,num,type,level):
        if type == "宫女":
            num2 = 0
            while num2 <= num-1:
                tempgongnv = NPC_Gongnv_store.Gongnv_order("宫女")
                tempgongnv.level = level
                tempgongnv.master = self
                num2 = num2 +1
                if tempgongnv.level == "长御":
                    tempgongnv.lv = 0
                elif tempgongnv.level == "女官":
                    tempgongnv.lv = 1
                elif tempgongnv.level == "大宫女":
                    tempgongnv.lv = 2
                elif tempgongnv.level == "贴身侍女":
                    tempgongnv.lv = 3
                elif tempgongnv.level == "婢子":
                    tempgongnv.lv = 4
                else:
                    tempgongnv.level = "散役"
                    tempgongnv.lv = 5
                
                if tempgongnv not in NPC_Gongnv_list:
                    self.Gongnv.append(tempgongnv)
                    NPC_Gongnv_list.append(tempgongnv)
        
        
        else :
            pass
        global NPC_Gongnv_list

    def makeYTGongnv(num,type):
        if type == "宫女":
            num2 = 0
            while num2 <= num-1:
                tempgongnv = NPC_Gongnv_store.Gongnv_order("宫女")
                tempgongnv.level = "散役"
                tempgongnv.lv = 5
                tempgongnv.master = ""
                num2 = num2 +1
                
                if tempgongnv not in YTGongnv:
                    YTGongnv.append(tempgongnv)
        
        
        else :
            pass
        global YTGongnv


    def Gongnv_shuxingmiaoshu(self):
        if self.beauty > 2000:
            self.beautylv = "{color=#F7AB00}天人{/color}"
        if self.beauty >900:
            self.beautylv = "{color=#FF3030}绝世{/color}"
        elif self.beauty >700:
            self.beautylv = "{color=#EE00EE}国色{/color}"
        elif self.beauty >400:
            self.beautylv = "{color=#0040FF}花颜{/color}"
        elif self.beauty >200:
            self.beautylv = "{color=#008000}端美{/color}"
        elif self.beauty >100:
            self.beautylv = "{color=#2F4F4F}清秀{/color}"
        else:
            self.beautylv = "{color=#A1A1A1}寻常{/color}"
        
        if self.yexin >900:
            self.yexinlv = "{color=#FF3030}野心勃勃{/color}"
        elif self.yexin >700:
            self.yexinlv = "{color=#EE00EE}追名逐利{/color}"
        elif self.yexin >400:
            self.yexinlv = "{color=#0040FF}八面玲珑{/color}"
        elif self.yexin >200:
            self.yexinlv = "{color=#008000}锋芒未露{/color}"
        elif self.yexin >100:
            self.yexinlv = "{color=#2F4F4F}恪守本分{/color}"
        else:
            self.yexinlv = "{color=#A1A1A1}赤子之心{/color}"








    def Gongnvtofz(self,whose,how):
        
        newfz = factory.instantiation_Feizi()
        newfz.xing = renpy.random.choice(xing_list)
        newfz.ming = self.name
        newfz.name = newfz.xing + newfz.ming
        newfz.beauty = self.beauty
        newfz.yuanmao = newfz.beauty
        newfz.age = self.age
        newfz.familylevel = 12
        newfz.fatherduty = ""
        newfz.familylocation = ''
        newfz.family = "原"+str(whose.name)+"宫中"+str(daixinggn.level)
        newfz.shiqin = 1
        newfz.shou = self.shou
        newfz.face = renpy.random.choice(list_femaleface)
        list_femaleface.remove(newfz.face)
        newfz.exp = 0
        newfz.father = None
        newfz.jiazu = []
        
        
        if self.xingge == "单纯":
            newfz.xingge = renpy.random.choice(["活泼","温婉","安静"])
            newfz.xinji = renpy.random.randint(0,300)
        elif self.xingge == "机灵":
            newfz.xingge = renpy.random.choice(["圆滑","娇纵","势利"])
            newfz.xinji = renpy.random.randint(300,700)
        elif self.xingge == "稳重":
            newfz.xingge = renpy.random.choice(["温婉","清冷","安静"])
            newfz.xinji = renpy.random.randint(500,1000)
        else:
            newfz.xingge = renpy.random.choice(["温婉","圆滑","安静"])
            newfz.xinji = renpy.random.randint(600,900)
        
        newfz.yali = 500 - abs(newfz.xinji-500)
        newfz.yali = newfz.yali*0.1
        
        newfz.year = 0
        newfz.state = "寻常"
        newfz.palace = " "
        newfz.health = renpy.random.randint(400, 920)
        newfz.qizhi = renpy.random.randint(0, 700)
        newfz.meili = renpy.random.randint(0, 920)
        newfz.dance = renpy.random.randint(0, 60)
        newfz.book = renpy.random.randint(0, 60)
        newfz.battle = 0
        newfz.medic = 0
        newfz.muzic = renpy.random.randint(0, 60)
        newfz.cixiu = renpy.random.randint(20, 90)
        newfz.medic = 0
        newfz.battle = 0
        newfz.xinji1 = False
        newfz.xingge1 = False
        newfz.huaiyun = 0
        newfz.lucky = newfz.health*0.03
        newfz.jinzu = 0
        newfz.tequan1 = -1
        newfz.tequan2 = False
        Feizi_skills_random(newfz)
        
        newfz.tags = []
        newfz.tags.append(tags_family[3])
        temptagslist = [tags_limit_beauty,tags_limit_qizhi,tags_limit_meili,tags_limit_health,tags_limit_lucky,tags_limit_xinji,tags_shuxing,tags_caiyi,tags_xihao]
        if newfz.lucky >= 80:
            newfz.tags.append(tags_limit_lucky[1])
            temptagslist.remove(tags_limit_lucky)
        elif newfz.lucky >= 50:
            temptagslist.remove(tags_limit_lucky)
        else:
            pass
        
        if newfz.beauty >= 900:
            newfz.tags.append(tags_limit_beauty[2])
            temptagslist.remove(tags_limit_beauty)
        elif newfz.beauty >= 850:
            newfz.tags.append(tags_limit_beauty[1])
            temptagslist.remove(tags_limit_beauty)
        elif newfz.beauty >= 800:
            newfz.tags.append(tags_limit_beauty[0])
            temptagslist.remove(tags_limit_beauty)
        else:
            pass
        
        if newfz.qizhi >= 900:
            newfz.tags.append(tags_limit_qizhi[2])
            temptagslist.remove(tags_limit_qizhi)
        elif newfz.qizhi >= 850:
            newfz.tags.append(tags_limit_qizhi[1])
            temptagslist.remove(tags_limit_qizhi)
        elif newfz.qizhi >= 800:
            newfz.tags.append(tags_limit_qizhi[0])
            temptagslist.remove(tags_limit_qizhi)
        else:
            pass
        if newfz.meili >= 900:
            newfz.tags.append(tags_limit_meili[2])
            temptagslist.remove(tags_limit_meili)
        elif newfz.meili >= 850:
            newfz.tags.append(tags_limit_meili[1])
            temptagslist.remove(tags_limit_meili)
        elif newfz.meili >= 800:
            newfz.tags.append(tags_limit_meili[0])
            temptagslist.remove(tags_limit_meili)
        else:
            pass
        if newfz.xinji >= 900:
            newfz.tags.append(tags_limit_xinji[2])
            temptagslist.remove(tags_limit_xinji)
        elif newfz.xinji >= 850:
            newfz.tags.append(tags_limit_xinji[1])
            temptagslist.remove(tags_limit_xinji)
        elif newfz.xinji >= 800:
            newfz.tags.append(tags_limit_xinji[0])
            temptagslist.remove(tags_limit_xinji)
        elif newfz.xinji >= 800:
            temptagslist.remove(tags_limit_xinji)
        else:
            pass
        if newfz.health >= 600:
            temptagslist.remove(tags_limit_health)
        else:
            pass
        
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            pass
        else:
            temptaglist = renpy.random.choice(temptagslist)
            temptag = renpy.random.choice(temptaglist)
            newfz.tags.append(temptag)
            temptagslist.remove(temptaglist)
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            pass
        else:
            temptaglist = renpy.random.choice(temptagslist)
            temptag = renpy.random.choice(temptaglist)
            newfz.tags.append(temptag)
            temptagslist.remove(temptaglist)
        
        tags_buff(newfz)
        tags_limitcheck(newfz)
        
        
        newfz.qingxiang = self.yexin*0.1
        newfz.meet = 99
        
        newfz.love = (newfz.beauty +newfz.meili+newfz.qizhi)/250
        newfz.taihoulike = 0
        
        if whose == my:
            if how == True:
                newfz.like = self.like*0.3 + self.yexin*0.1
            else:
                newfz.like = self.like*0.4
        else:
            newfz.like = self.like*0.4
        newfz.exp = newfz.beauty/50 + newfz.qizhi/100 + newfz.meili/100
        
        Feizilevel(newfz)
        
        
        if newfz.level ==0:
            newfz.hao = ""
        
        
        lucky = renpy.random.randint(0, 5)
        if lucky == 0:
            newfz.hao = renpy.random.choice(hao_list)
            hao_list.remove(newfz.hao)
        else :
            newfz.hao = ""
        
        randompalace(newfz)
        
        
        newfz.friends = []
        newfz.foes = []
        newfz.kids = []
        newfz.Gongnv = []
        if how == True:
            newfz.friends.append(whose)
            whose.friends.append(newfz)
            if newfz.beauty +newfz.qizhi +newfz.meili < 1200:
                whose.love = whose.love -5
            elif newfz.beauty +newfz.qizhi +newfz.meili > 1600:
                whose.love = whose.love + 5
            else:
                pass
        else:
            if whose == my:
                if newfz.like <= 50:
                    newfz.foes.append(my)
                    my.foes.append(newfz)
                else:
                    pass
            else:
                newfz.foes.append(whose)
                whose.foes.append(newfz)
        
        ChangeGongnv(newfz)
        
        
        newfz.story = []
        
        if newfz.hao == "":
            tempstory = str(nianhao)+str(year)+"年，由宫女被册为"+str(newfz.weifen)+"。\n"
            newfz.story.append(tempstory)
        else:
            tempstory = str(nianhao)+str(year)+"年，由宫女被册为"+str(newfz.weifen)+"，赐封号"+str(newfz.hao)+",是为"+str(newfz.hao)+str(newfz.weifen)+"。\n"
            newfz.story.append(tempstory)
        
        if newfz.hao =="":
            newfz.cheng = newfz.xing +newfz.weifen
        else:
            newfz.cheng = newfz.hao +newfz.weifen
        tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ str(whose.hao)+str(whose.weifen)+str(whose.name) + "的宫女"+str(newfz.ming)+"被册封为"+str(newfz.cheng)+"。\n"
        allstory.insert(0,tempstory2)
        NPC_fz_list.append(newfz)
        global weifen_list


default chun = Gongnv_sx(name="小春",face="小春",age=14,beauty=300,xingge="单纯",skill=["善于交际"],yexin =0,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
default xia = Gongnv_sx(name="阿夏",face="阿夏",age=16,beauty=700,xingge="机灵",skill=["花言巧语"],yexin =600,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
default qiu = Gongnv_sx(name="秋子",face="秋子",age=18,beauty=500,xingge="聪颖",skill=["见机行事"],yexin =300,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
default dong = Gongnv_sx(name="冬儿",face="冬儿",age=20,beauty=150,xingge="稳重",skill=["心思细腻"],yexin =150,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
default laoji = Gongnv_sx(name="老鸡",face="老鸡",age=61,beauty=920,xingge="聪颖",skill=["刺探情报","散播消息"],yexin =0,master=None,level="散役",yexinlv="",beautylv="",like=0,lv=5,state="寻常",shou=999)
default yxxiao = Gongnv_sx(name="潇潇",face="潇潇",age=15,beauty=500,xingge="机灵",skill=["花言巧语","尽忠职守"],yexin =300,master=None,level="散役",yexinlv="",beautylv="",like=0,lv=5,state="寻常",shou=999)





style YTGongnv_text:
    min_width 50
    text_align 0.5


init python:
    Gongnv_page=0

screen YTGongnv():
    style_prefix "YTGongnv"
    add "gui/frame.webp" xalign 0.45 yalign 0.25
    $ next_Gongnv_page = Gongnv_page + 1
    $ prev_Gongnv_page = Gongnv_page - 1
    $ max_Gongnv_page = round(len(YTGongnv)/10)+1
    $ b = Gongnv_page*10+10

    if b >= len(YTGongnv):
        $ b = len(YTGongnv)
    else:
        pass
    frame:
        background None
        xsize 1200
        ysize 480
        align (0.4,0.3)
        hbox:
            align (0.5, 1.0)
            spacing 0
            if Gongnv_page > 0:
                textbutton "《《" action SetVariable('Gongnv_page', prev_Gongnv_page), Show("YTGongnv")
            else:
                textbutton "《《"
            text "第[next_Gongnv_page]页"
            if Gongnv_page < max_Gongnv_page:
                textbutton "》》" action SetVariable('Gongnv_page', next_Gongnv_page), Show("YTGongnv")
            else:
                textbutton "》》"

        grid 1 11:
            pos (0.15,0.0)
            xsize 1200
            ysize 900
            $ a = 0
            $ next_Gongnv_page = Gongnv_page + 1
            fixed:
                xsize 1200
                ysize 35
                hbox:
                    spacing 50
                    text "操作" align (0.5,0.5)
                    text "名字" align (0.5,0.5)
                    text "年龄" align (0.5,0.5)
                    text "外貌" align (0.5,0.5)
                    text "性格" align (0.5,0.5)
                    text "好感" align (0.5,0.5)
                    text "特长" align (0.5,0.5)

            for i in YTGongnv[Gongnv_page*10:b]:
                if a <= b:
                    fixed:
                        xsize 1200
                        ysize 35
                        hbox:
                            spacing 50
                            python:
                                if i.beauty >900:
                                    i.beautylv = "{color=#FF3030}绝世{/color}"
                                elif i.beauty >700:
                                    i.beautylv = "{color=#EE00EE}国色{/color}"
                                elif i.beauty >400:
                                    i.beautylv = "{color=#0040FF}花颜{/color}"
                                elif i.beauty >200:
                                    i.beautylv = "{color=#008000}端美{/color}"
                                elif i.beauty >100:
                                    i.beautylv = "{color=#2F4F4F}清秀{/color}"
                                else:
                                    i.beautylv = "{color=#A1A1A1}寻常{/color}"

                            textbutton "收用" align (0.5,0.5) action Hide("YTGongnv"),Call("收用宫女",gn = i)

                            text "[i.name]" align (0.5,0.5)
                            text "[i.age]" align (0.5,0.5)
                            text "[i.beautylv]" align (0.5,0.5)
                            text "[i.xingge]" align (0.5,0.5)
                            text "[i.like]" align (0.5,0.5)
                            python:
                                tempskill = ""

                                for i in i.skill:
                                    tempskill = tempskill + i + " "
                            text "{size=20}[tempskill]" align (0.5,0.5)


                    $ a = a + 1
                else:
                    null
            if a < 10:
                for j in range(a, 10):
                    null
    frame:
        background None
        align (0.8,0.7)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("YTGongnv"),Jump("皇宫界面")



screen YTGongnv0():
    style_prefix "Gongnv"
    add "gui/frame.webp" xalign 0.45 yalign 0.25
    vpgrid:
        $ a = len(YTGongnv) +1
        cols 7
        draggable True
        mousewheel True
        scrollbars "both"
        yalign 0.3
        xsize 1000
        ysize 680
        align (0.45,0.25)
        xspacing 5
        yspacing 10

        side_xalign 0.2
        text "  操作  " align (0.5,0.5)
        text "  名字  " align (0.5,0.5)
        text "  年龄  " align (0.5,0.5)
        text "  外貌  " align (0.5,0.5)
        text "  性格  " align (0.5,0.5)
        text "  好感  " align (0.5,0.5)
        text "  特长  " min_width 300 text_align 0.0
        for i in YTGongnv:
            python:
                if i.beauty >900:
                    i.beautylv = "{color=#FF3030}绝世{/color}"
                elif i.beauty >700:
                    i.beautylv = "{color=#EE00EE}国色{/color}"
                elif i.beauty >400:
                    i.beautylv = "{color=#0040FF}花颜{/color}"
                elif i.beauty >200:
                    i.beautylv = "{color=#008000}端美{/color}"
                elif i.beauty >100:
                    i.beautylv = "{color=#2F4F4F}清秀{/color}"
                else:
                    i.beautylv = "{color=#A1A1A1}寻常{/color}"






            textbutton "收用" align (0.5,0.5) action Hide("YTGongnv"),Call("收用宫女",gn = i)

            text "[i.name]" align (0.5,0.5)
            text "[i.age]" align (0.5,0.5)
            text "[i.beautylv]" align (0.5,0.5)
            text "[i.xingge]" align (0.5,0.5)
            text "[i.like]" align (0.5,0.5)
            python:
                tempskill = ""

                for i in i.skill:
                    tempskill = tempskill + i + " "
            text "{size=20}[tempskill]" align (0.5,0.5)

    frame:
        align (0.8,0.8)
        textbutton "返回":
            action Hide("YTGongnv"),Jump("皇宫界面")




label 收用宫女(gn):
    $ gnface = gn.face
    show gn at chara

    if len(my.Gongnv) <= 15:
        "确认收用宫女[gn.name]吗？"
        menu:
            "是":
                "[gn.name]" "奴婢多谢娘娘赏识！"
                hide gn
                $ YTGongnv.remove(gn)
                $ my.Gongnv.append(gn)
                $ gn.master = my
                $ gn.state = "寻常"
                call screen YTGongnv
            "否":

                hide gn
                call screen YTGongnv
    else:
        我 "如今宫中人手已经足够，再收用[gn.name]恐怕会落人口舌。"
        call screen YTGongnv


label 管理宫女(gn):
    $ gn0 = gn.level+" "+gn.name
    show gn at chara
    "[gn0]" "娘娘有什么吩咐？"
    menu:
        "赏赐鸡粮（花费五十两）" if gn == laoji and money >= 50:
            $ money = money -50
            $ gn.like += 15
            "[gn0]" "奴婢多谢娘娘体恤，奴婢就需要这个！"
        "赏赐银两":
            if gn == yxxiao:
                "[gn0]" "无功不受禄，请恕奴婢不能收下！"
            else:
                menu:
                    "二十两" if money>=20:
                        if gn in teshugn and gn not in chushign:
                            $ gn.like =gn.like +5
                        else:
                            $ gn.like =gn.like +10
                        $ money = money -20
                        "[gn0]" "奴婢多谢娘娘体恤。"
                    "十两" if money>=10:
                        if gn in teshugn and gn not in chushign:
                            $ gn.like =gn.like +2.5
                        else:
                            $ gn.like =gn.like +5
                        $ money = money -10
                        "[gn0]" "奴婢多谢娘娘体恤。"
                    "五两" if money>=50:
                        if gn in teshugn and gn not in chushign:
                            $ gn.like =gn.like +1
                        else:
                            $ gn.like =gn.like +2
                        $ money = money -5
                        "[gn0]" "奴婢多谢娘娘体恤。"
                    "算了":
                        pass
        "职位变更":


            python:
                a = len(yuanweifen)
                templist0 = []
                templist1 = []
                templist2 = []
                templist3 = []
                templist4 = []

                for i in my.Gongnv:
                    if i.lv == 0:
                        templist0.append(i)
                    elif i.lv == 1:
                        templist1.append(i)
                    elif i.lv == 2:
                        templist2.append(i)
                    elif i.lv == 3:
                        templist3.append(i)
                    elif i.lv == 4:
                        templist4.append(i)
                    else:
                        pass
            if my.level == 0:
                menu:
                    "长御" if len(templist0) == 0:
                        $ gn.level = "长御"
                        $ gn.lv = 0
                    "女官" if len(templist1) == 0:
                        $ gn.level = "女官"
                        $ gn.lv = 1
                    "大宫女" if len(templist2) < 2:
                        $ gn.level = "大宫女"
                        $ gn.lv = 2
                    "贴身侍女" if len(templist3) < 2:
                        $ gn.level = "贴身侍女"
                        $ gn.lv = 3
                    "婢子" if len(templist4) < 4:
                        $ gn.level = "婢子"
                        $ gn.lv = 4
                    "散役":
                        $ gn.level = "散役"
                        $ gn.lv = 5
                    "算了":
                        pass
            elif my.qinjunum == 1:
                menu:
                    "女官" if len(templist1) == 0:
                        $ gn.level = "女官"
                        $ gn.lv = 1
                    "大宫女" if len(templist2) < 1:
                        $ gn.level = "大宫女"
                        $ gn.lv = 2
                    "贴身侍女" if len(templist3) < 2:
                        $ gn.level = "贴身侍女"
                        $ gn.lv = 3
                    "婢子" if len(templist4) < 3:
                        $ gn.level = "婢子"
                        $ gn.lv = 4
                    "散役":
                        $ gn.level = "散役"
                        $ gn.lv = 5
                    "算了":
                        pass
            elif my.level > round(a-a/3) == 1:
                menu:
                    "贴身侍女" if len(templist3) < 1:
                        $ gn.level = "贴身侍女"
                        $ gn.lv = 3
                    "婢子" if len(templist4) < 1:
                        $ gn.level = "婢子"
                        $ gn.lv = 4
                    "散役":
                        $ gn.level = "散役"
                        $ gn.lv = 5
                    "算了":
                        pass
            else:
                menu:
                    "大宫女" if len(templist2) < 1:
                        $ gn.level = "大宫女"
                        $ gn.lv = 2
                    "贴身侍女" if len(templist3) < 1:
                        $ gn.level = "贴身侍女"
                        $ gn.lv = 3
                    "婢子" if len(templist4) < 2:
                        $ gn.level = "婢子"
                        $ gn.lv = 4
                    "散役":
                        $ gn.level = "散役"
                        $ gn.lv = 5
                    "算了":
                        pass
        "赐名" if gn not in teshugn or gn in chushign:
            python:
                tempname = renpy.input("为宫女赐名（不输入则不改名）",length=3)
                tempname = tempname.strip()

                if not tempname:
                    tempname = gn.name
                gn.name = tempname

        "打发" if len(my.Gongnv)> 1 and gn not in teshugn:
            "确定要将[gn.name]送回掖廷吗？"
            menu:
                "确定":
                    $ my.Gongnv.remove(gn)
                    if gn.level == "散役" or len(my.Gongnv) >= 15:
                        $ YTGongnv.append(gn)
                        "[gn.name]已被送往掖廷。"
                        pass
                    else:
                        $ newgn = renpy.random.choice(YTGongnv)
                        $ YTGongnv.remove(newgn)
                        $ my.Gongnv.append(newgn)
                        $ YTGongnv.append(gn)
                        show 李公公 at chara
                        李公公 "启禀[my.cheng]，掖庭送来了一名新的宫女顶替[gn.name]，还请您自行为她分配职务。"
                        hide 李公公
                    $ timenum = timenum +1
                "算了":

                    pass
        "退下吧":
            "[gn0]" "奴婢遵命。"
    if gn.like >= 200:
        $ gn.like = 200
    else:
        pass

    $ my.Gongnv = sorted(my.Gongnv, key=attrgetter("lv"),reverse = False)
    hide gn
    jump 寝居界面

label 管理别人宫女(gn, fz):
    hide screen myroom
    menu:
        "收买":
            call 收买宫女 (gn=gn, fz=fz) from _call_收买宫女
        "收用" if len(my.Gongnv) <= 15:
            $ my.Gongnv.append(gn)
            $ gn.master = my
            $ gn.state = "寻常"
            $ fz.like = fz.like - 5
            $ fz.Gongnv.remove(gn)
            $ gn.lv = 5
            $ gn.level == "散役"
            "[gn.name]已成为你宫中散役。[fz.cheng]对你的好感降低了。"
        "调离":
            $ gn.state = "寻常"
            $ fz.like = fz.like - 5
            $ fz.Gongnv.remove(gn)
            $ YTGongnv.append(gn)
            "[gn.name]已被送往掖廷。[fz.cheng]对你的好感降低了。"

    menu:
        "[fz.cheng]中的空缺要如何填补？"
        "掖廷安排":
            $ newgn = renpy.random.choice(YTGongnv[:-1])
            $ YTGongnv.remove(newgn)
            $ fz.Gongnv.append(newgn)
            $ newgn.level = "婢子"
            $ newgn.lv = 4
        "亲自安排":

            $ tempgnlist = []
            python:
                for i in my.Gongnv:
                    if i.state != "寻常":
                        pass
                    elif i.level == "婢子":
                        tempgnlist.append(i)
                    else:
                        pass
                tempgnlist = sorted(tempgnlist, key=attrgetter("lv"),reverse = False)
            if len(tempgnlist) == 0:
                我 "（身边并无合适人选，只能让掖廷安排了。）"
                $ newgn = renpy.random.choice(YTGongnv[:-1])
                $ YTGongnv.remove(newgn)
                $ fz.Gongnv.append(newgn)
                $ newgn.level = "婢子"
                $ newgn.lv = 4
            else:
                menu:
                    "[tempgnlist[0].name]" if len(tempgnlist)>0:
                        $ shoumaign = tempgnlist[0]
                    "[tempgnlist[1].name]" if len(tempgnlist)>1:
                        $ shoumaign = tempgnlist[1]
                    "[tempgnlist[2].name]" if len(tempgnlist)>2:
                        $ shoumaign = tempgnlist[2]
                    "[tempgnlist[3].name]" if len(tempgnlist)>3:
                        $ shoumaign = tempgnlist[3]
                    "[tempgnlist[4].name]" if len(tempgnlist)>4:
                        $ shoumaign = tempgnlist[4]
                    "[tempgnlist[5].name]" if len(tempgnlist)>5:
                        $ shoumaign = tempgnlist[5]
                    "[tempgnlist[6].name]" if len(tempgnlist)>6:
                        $ shoumaign = tempgnlist[6]
                $ fz.Gongnv.append(shoumaign)
                $ shoumaign.level = "婢子"
                $ shoumaign.lv = 4
                $ my.Gongnv.remove(shoumaign)
                if shoumaign.like >= 60:
                    "（[shoumaign.name]已自动成为你的内应……）"
                    $ shoumaign.state = "内应"
                else:
                    pass
    if mapname == "寝居":
        hide screen Bigmap
        jump 寝居界面
    else:
        hide screen myroom
        jump 皇宫界面







label 收买宫女(gn, fz):
    hide screen myroom
    $ tempgnlist = []
    python:
        for i in my.Gongnv:
            if i.state != "寻常":
                pass
            else:
                tempgnlist.append(i)
        tempgnlist = sorted(tempgnlist, key=attrgetter("lv"),reverse = False)
    "要派谁去收买此人呢？"
    menu:
        "[tempgnlist[0].name]" if len(tempgnlist)>0:
            $ shoumaign = tempgnlist[0]
        "[tempgnlist[1].name]" if len(tempgnlist)>1:
            $ shoumaign = tempgnlist[1]
        "[tempgnlist[2].name]" if len(tempgnlist)>2:
            $ shoumaign = tempgnlist[2]
        "[tempgnlist[3].name]" if len(tempgnlist)>3:
            $ shoumaign = tempgnlist[3]
        "[tempgnlist[4].name]" if len(tempgnlist)>4:
            $ shoumaign = tempgnlist[4]
        "[tempgnlist[5].name]" if len(tempgnlist)>5:
            $ shoumaign = tempgnlist[5]
        "[tempgnlist[7].name]" if len(tempgnlist)>7:
            $ shoumaign = tempgnlist[7]
        "[tempgnlist[8].name]" if len(tempgnlist)>8:
            $ shoumaign = tempgnlist[8]
        "[tempgnlist[9].name]" if len(tempgnlist)>9:
            $ shoumaign = tempgnlist[9]
        "[tempgnlist[10].name]" if len(tempgnlist)>10:
            $ shoumaign = tempgnlist[10]
        "[tempgnlist[11].name]" if len(tempgnlist)>11:
            $ shoumaign = tempgnlist[11]
        "[tempgnlist[12].name]" if len(tempgnlist)>12:
            $ shoumaign = tempgnlist[12]
        "[tempgnlist[13].name]" if len(tempgnlist)>13:
            $ shoumaign = tempgnlist[13]

        "无人可用，只得作罢" if len(tempgnlist) == 0:
            if mapname == "寝居":
                hide screen Bigmap
                jump 寝居界面
            else:
                hide screen myroom
                jump 皇宫界面



        "算了" if len(tempgnlist)>0:
            if mapname == "寝居":
                hide screen Bigmap
                jump 寝居界面
            else:
                hide screen myroom
                jump 皇宫界面


    $ tempnum = 0

    menu:
        "赏银十两" if money >=10:
            $ money = money -10
            $ tempnum = 1 + (gn.yexin/200)*gn.lv

        "赏银二十" if money >= 20:
            $ money = money - 20
            $ tempnum =   2 + (gn.yexin/100)*gn.lv
        "算了":

            if mapname == "寝居":
                hide screen Bigmap
                jump 寝居界面
            else:
                hide screen myroom
                jump 皇宫界面




    python:
        if shoumaign.like >= 200:
            tempnum += 2
        elif shoumaign.like >= 100:
            tempnum += 1
        else:
            pass
        tempnum += shoumaign.yexin *0.01

        if "花言巧语" in shoumaign.skill:
            if gn.xingge == "单纯" or gn.xingge == "机灵":
                tempnum += 8
            elif gn.xingge == "稳重" or gn.xingge == "聪颖":
                tempnum += 4
            else:
                pass
        else:
            pass

        if "善于交际" in shoumaign.skill:
            if gn.xingge == "单纯" or gn.xingge == "机灵":
                tempnum += 4
            elif gn.xingge == "稳重" or gn.xingge == "聪颖":
                tempnum += 8
            else:
                pass
        else:
            pass





    if fz.fangyu["一B"] == 0:
        pass
    elif fz.fangyu["一B"] == 1:
        $ tempnum = tempnum*0.85
    elif fz.fangyu["一B"] == 2:
        $ tempnum = tempnum*0.7
    elif fz.fangyu["一B"] == 3:
        $ tempnum = tempnum*0.5
    $ gn.like += tempnum
    "[shoumaign.name]领命而去……"
    $ tempnum = int(tempnum)
    "（[gn.name]的好感增加了约[tempnum]）"
    if "尽忠职守" not in gn.skill and  gn.like >= 60 and gn.state != "内应":
        $ gn.state = "内应"
        "未几，[shoumaign.name]回禀，[gn.name]已经向你表明忠心，愿意做你的内应。"
    elif "尽忠职守" in gn.skill and gn.like >= 80 and gn.state != "内应":
        $ gn.state = "内应"
        "未几，[shoumaign.name]回禀，[gn.name]已经向你表明忠心，愿意做你的内应。"
    else:
        pass
    $ shoumaign.state = "任务中"
    $ timenum = timenum +1
    $ AP = AP -1
    if mapname == "寝居":
        hide screen Bigmap
        jump 寝居界面
    else:
        hide screen myroom
        jump 皇宫界面







label 宫女弄坏物品(gn, what):
    scene 寝居
    $ gnface = gn.face
    show 我的宫女 at chara
    我的宫女 "（一脸惶恐地走上前来，身后还跟着[gn.name]）主子……"
    我 "何事？"
    hide 我的宫女
    show gn
    "[gn.level] [gn.name]" "（扑通一声跪了下来）奴婢知错！奴婢知错！主子饶了奴婢这一回吧！"
    hide gn
    show 我的宫女
    我的宫女 "[gn.name]做事毛手毛脚的，方才打扫库房的时候，不慎失手将您的[what.name]给弄坏了。"
    我的宫女 "她虽不是有意的，可到底是犯了错，还请您亲自发落吧。"
    hide 我的宫女
    show gn
    "[gn.level] [gn.name]" "求主子宽恕！"
    menu:
        "温和抚慰":
            我 "本宫还以为是什么要紧事。"
            我 "罢了，往后小心些便是。"
            "[gn.level] [gn.name]" "多谢娘娘宽恕，奴婢往后必定更加小心！"
            $ gn.like += 10
            hide gn
        "生气斥责":

            我 怒 "好你个[gn.name]，成事不足败事有余！"
            "[gn.level] [gn.name]" "奴婢真的知错了……"
            我 怒 "去外头跪三个时辰，今日的饭食也一应免了，再有下次，本宫决不轻饶！"
            "[gn.level] [gn.name]" "是，奴婢遵命……"
            $ gn.yexin += 20
            $ gn.like -= 10
            hide gn
        "掖廷训诫":

            我 "看来你在本宫这里待得太舒服了，以前在掖廷学的那些规矩都忘得干净了是不是？"
            我 "毁了本宫心爱的物件，夺了你这条贱命都赔不起！"
            我 "罢了，你犯下大错，本宫就将你交回掖廷处置。"
            "[gn.level] [gn.name]" "不要啊娘娘，掖廷的人会打死奴婢的！娘娘饶命啊！"
            hide gn
            "不一会儿，掖廷的人就奉命而来，带走了[gn.name]。"
            $ my.Gongnv.remove(gn)
            $ gn.like = gn.like - 50
            $ gn.yexin += 50
            if gn.like >= 20:
                $ gn.like = 20
            else:
                pass
            if gn.level == "散役":
                $ YTGongnv.append(gn)
                pass
            else:
                $ newgn = renpy.random.choice(YTGongnv)
                $ YTGongnv.remove(newgn)
                $ my.Gongnv.append(newgn)
                $ YTGongnv.append(gn)
                show 李公公 at chara
                李公公 "启禀[my.cheng]，掖庭送来了一名新的宫女顶替[gn.name]，还请您自行为她分配职务。"
                hide 李公公
    return


label 宫女私下交际(gn, fz, tempgn):
    if month > 1 and month < 5:
        $ map1 = "春"
    elif month > 4 and month < 8:
        $ map1 = "夏"
    elif month > 7 and month < 11:
        $ map1 = "秋"
    else:
        $ map1 = "冬"

    if timenum == 4:
        $ map2 = "黄昏"
    elif timenum== 5:
        $ map2 = "晚上"
    else:
        $ map2 = "白天"
    scene 皇宫
    $ gnface = gn.face
    if fz.love >= 50 and fz.love > my.love:
        "女子的声音" "你们主子在皇上面前是说得上话的……可不想我那位，眼巴巴看着也没多大指望。唉，[tempgn.name]，我真是羡慕你呢。"
        "另一个女子的声音" "嘘，[gn.name]你说这话可别叫你家主子听去了。"
        "女子的声音" "听到了又如何？与其在我们这些下人身上费心思，还不如多为自己打算打算，不然我们这些下人也跟着遭人白眼，一年两年下去，谁受得了呀？"
        "女子的声音" "巴不得她把我送回掖廷算了，兴许还能谋个更好的主子，就比如[fz.cheng]……"
        "另一个女子的声音" "你可真别说这些了，若叫别人听去了，[fz.cheng]和[my.cheng]心头都不痛快。"
        show 我的宫女 at chara
        我的宫女 "主子，前面好像是[gn.name]……在和[fz.cheng]宫里的[tempgn.name]说话。"
        我 惊 "她竟然敢说这种话……"
        我的宫女 "前头是谁在嚼舌根？"
        hide 我的宫女
        show tempgn
        "[tempgn.level] [tempgn.name]" "奴婢[tempgn.name]见过[my.cheng]。"
        "[tempgn.level] [tempgn.name]" "呀，奴婢想起来[fz.cheng]还给奴婢交待了差事要做，奴婢先退下了。"
        hide tempgn
        show gn
        "[gn.level] [gn.name]" "（一脸忐忑）见过主子，奴婢方才……"
        我 怒 "你说的话，本宫方才都听见了。"
        "[gn.level] [gn.name]" "？！"
        "[gn.level] [gn.name]" "奴、奴婢……"
        menu:
            "好言相劝":
                我 思 "本宫自认待你不薄，却没想在你眼中，本宫却是如此……"
                "[gn.level] [gn.name]" "（羞愧得无地自容）其实奴婢并未对主子有所不满……"
                我 思 "其实是你说的未尝不对。人往高处走，水往低处流。是本宫无能。"
                "[gn.level] [gn.name]" "您别这么说，是奴婢错了，奴婢不该说这种话……"
                我 常 "若你为自己谋了更好的出路，那本宫会放你走的。"
                "[gn.level] [gn.name]" "[my.cheng]您别赶奴婢走，奴婢会好好在您身边做事的！"
                $ gn.like += 10
                hide gn
            "厉声斥责":
                我 怒 "好你个[gn.name]，竟然背着本宫说出这般大逆不道的话！"
                "[gn.level] [gn.name]" "奴婢知错，奴婢知错！还请娘娘宽恕奴婢这一回吧！"
                我 怒 "去外头跪三个时辰，今日的饭食也一应免了，再有下次，本宫决不轻饶！"
                "[gn.level] [gn.name]" "是，奴婢遵命……"
                $ gn.yexin -= 20
                $ gn.like -= 10
                hide gn
            "送入掖廷":
                我 笑 "本宫这里供不起你这尊大佛，但至少还能让你如愿。"
                我 "按你所说，就回掖廷去吧。"
                "[gn.level] [gn.name]" "不要啊娘娘，掖廷的人会打死奴婢的！娘娘饶命啊！"
                hide gn
                我 思 "（不再听其哀求，转身离开。）"
                $ my.Gongnv.remove(gn)
                $ gn.like = gn.like - 50
                $ gn.yexin += 100
                if gn.like >= 20:
                    $ gn.like = 0
                else:
                    pass
                if gn.level == "散役":
                    $ YTGongnv.append(gn)
                    pass
                else:
                    $ newgn = renpy.random.choice(YTGongnv)
                    $ YTGongnv.remove(newgn)
                    $ my.Gongnv.append(newgn)
                    $ YTGongnv.append(gn)
                    show 李公公 at chara
                    李公公 "启禀[my.cheng]，掖庭送来了一名新的宫女顶替[gn.name]，还请您自行为她分配职务。"
                    hide 李公公


    elif fz.love <= 20 and fz.love < my.love:
        "女子的声音" "唉，同人不同命啊。你们主子怕是一年到头连皇上的面也见不到几回，在这宫里还有多少指望呢？"
        "另一个女子的声音" "哼，也不知道你在炫耀什么的。花无百日红，你家主子有能耐一时得皇上欢心并不算什么，有能耐一辈子把皇上的心抓在手里，你再来同我炫耀吧！"
        "女子的声音" "你就是不服气！看你那眼红的样子，嘁，我是不知道[my.cheng]能不能一世荣宠，但我知道[fz.cheng]这辈子恐怕是没机会了。"
        "另一个女子的声音" "你！你！"
        show 我的宫女 at chara
        我的宫女 "主子，前面好像是[gn.name]……在和[fz.cheng]宫里的[tempgn.name]说话。"
        menu:
            "上前":
                我的宫女 "前头是谁在嚼舌根？"
                hide 我的宫女
                show tempgn
                "[tempgn.level] [tempgn.name]" "奴婢[tempgn.name]见过[my.cheng]。"
                "[tempgn.level] [tempgn.name]" "（咬牙）[my.cheng]，你可别再放任自己手下的奴才们在宫里肆意嘴碎了，这般对主子们不敬。若叫别人听去了，可是有损您的声誉啊！"
                menu:
                    "轮得到你一个奴才置喙？":
                        "[tempgn.level] [tempgn.name]" "（愣了愣）还真是什么样的主子就有什么样的奴才……"
                        hide tempgn
                        show gn
                        "[gn.level] [gn.name]" "（得意。）"
                        hide gn
                        show tempgn
                        "[tempgn.level] [tempgn.name]" "（怨愤地看了你们二人一眼）奴婢想起来[fz.cheng]还给奴婢交待了差事要做，这便先退下了。"
                        hide tempgn
                        $ gn.yexin += 50
                        $ tempgn.like -= 20
                        $ fz.like -= 15
                    "[gn.name]对[fz.cheng]不敬，定会严加惩治":
                        "[tempgn.level] [tempgn.name]" "（福身）今日之事奴婢不会外传，但愿[gn.name]往后能谨言慎行，别得罪了不该得罪的人。"
                        "[tempgn.level] [tempgn.name]" "奴婢想起来[fz.cheng]还给奴婢交待了差事要做，这便先退下了。"
                        hide tempgn
                        $ gn.yexin += 50
                        show gn
                        "[gn.level] [gn.name]" "（一脸忐忑）见过主子，奴婢方才……"
                        我 怒 "你说的话，本宫方才都听见了。"
                        "[gn.level] [gn.name]" "？！"
                        "[gn.level] [gn.name]" "奴、奴婢……"
                        menu:
                            "好言相劝":
                                我 思 "先起来罢，本宫今天不想罚你。"
                                "[gn.level] [gn.name]" "是……奴婢知错了。"
                                我 思 "其实是你说的未尝不对，但有些话在宫里，但凡出口，即是错，你明白么？"
                                "[gn.level] [gn.name]" "是，奴婢明白……"
                                我 常 "况且，[fz.cheng]未必就没有青云直上的时候……到时候，可不是你亲手给本宫挖了坑？"
                                "[gn.level] [gn.name]" "奴婢明白了，奴婢不该呈这一时口舌之快的……"
                                $ gn.yexin -= 20
                                $ gn.like += 10
                                hide gn
                            "厉声斥责":
                                我 怒 "好你个[gn.name]，你知道今日之事传出去会是怎样的后果吗？你自己放肆，可是要牵连到本宫的！"
                                "[gn.level] [gn.name]" "奴婢知错，奴婢知错！还请娘娘宽恕奴婢这一回吧！"
                                我 怒 "回去跪三个时辰，今日的饭食也一应免了，再有下次，本宫决不轻饶！"
                                "[gn.level] [gn.name]" "是，奴婢遵命……"
                                $ gn.yexin += 20
                                $ gn.like -= 10
                                hide gn
                            "送入掖廷":
                                我 笑 "[gn.name]，你可知道你今日的言行差点让本宫替你背了骂名？"
                                "[gn.level] [gn.name]" "主子，那[fz.cheng]根本不足为惧，您何必……"
                                我 怒 "你竟还敢如此？"
                                我 "罢了，本宫可不敢留你了。"
                                "[gn.level] [gn.name]" "啊？主子您是要……"
                                我 "回掖廷去好好学学规矩罢。"
                                "[gn.level] [gn.name]" "不要啊娘娘，掖廷的人会打死奴婢的！娘娘饶命啊！"
                                hide gn
                                我 思 "（不再听其哀求，转身离开。）"
                                $ my.Gongnv.remove(gn)
                                $ gn.like = gn.like - 50
                                $ gn.yexin += 100
                                if gn.like >= 20:
                                    $ gn.like = 0
                                else:
                                    pass
                                if gn.level == "散役":
                                    $ YTGongnv.append(gn)
                                    pass
                                else:
                                    $ newgn = renpy.random.choice(YTGongnv)
                                    $ YTGongnv.remove(newgn)
                                    $ my.Gongnv.append(newgn)
                                    $ YTGongnv.append(gn)
                                    show 李公公 at chara
                                    李公公 "启禀[my.cheng]，掖庭送来了一名新的宫女顶替[gn.name]，还请您自行为她分配职务。"
                                    hide 李公公
            "离开":

                我 思 "随她去罢。"
                我的宫女 "可[tempgn.name]若回头在[fz.cheng]跟前说些什么……"
                我 常 "那她又能拿本宫怎样？"
                我 常 "[gn.name]话虽说得直白了些，倒也未必有错。"
                我的宫女 "是……"
                $ gn.yexin += 50
                $ tempgn.like -= 10
                $ fz.like -= 10
    else:

        pass
    return


label 宫女私下交际2(gn, fz, tempgn):
    if month > 1 and month < 5:
        $ map1 = "春"
    elif month > 4 and month < 8:
        $ map1 = "夏"
    elif month > 7 and month < 11:
        $ map1 = "秋"
    else:
        $ map1 = "冬"

    if timenum == 4:
        $ map2 = "黄昏"
    elif timenum== 5:
        $ map2 = "晚上"
    else:
        $ map2 = "白天"
    scene 皇宫
    $ gnface = gn.face
    if fz.love <= 20 and fz.love < my.love:
        "女子的声音" "你们主子在皇上面前是说得上话的……可不想我那位，眼巴巴看着也没多大指望。唉，[gn.name]，我真是羡慕你呢。"
        "另一个女子的声音" "嘘，[tempgn.name]你说这话可别叫你家主子听去了。"
        "女子的声音" "听到了又如何？与其在我们这些下人身上费心思，还不如多为自己打算打算，不然我们这些下人也跟着遭人白眼，一年两年下去，谁受得了呀？"
        "女子的声音" "巴不得她把我送回掖廷算了，兴许还能谋个更好的主子，就比如[my.cheng]……"
        "另一个女子的声音" "你可真别说这些了，若叫别人听去了，[my.cheng]和[fz.cheng]心头都不痛快。"
        show 我的宫女 at chara
        我的宫女 "主子，前面好像是[fz.cheng]宫里的[tempgn.name]……在和[gn.name]说话。"
        hide 我的宫女
        show fz
        妃子 "[tempgn.name]！"
        hide fz
        show tempgn
        "[tempgn.level] [tempgn.name]" "（一脸忐忑）见过主子，奴婢方才……"
        hide tempgn
        show fz
        妃子 "你说的话，本宫方才都听见了。"
        hide fz
        show tempgn
        "[tempgn.level] [tempgn.name]" "？！"
        "[tempgn.level] [tempgn.name]" "奴、奴婢……"
        if fz.qingxiang <= 25 or fz.xingge == "清冷" or fz.xingge == "安静" or fz.xingge == "温婉":
            hide tempgn
            show fz
            妃子 "本宫自认待你不薄，却没想在你眼中，本宫却是如此……"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "（羞愧得无地自容）其实奴婢并未对主子有所不满……"
            hide tempgn
            show fz
            妃子 "其实是你说的未尝不对。人往高处走，水往低处流。是本宫无能。"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "您别这么说，是奴婢错了，奴婢不该说这种话……"
            hide tempgn
            show fz
            妃子 "若你为自己谋了更好的出路，那本宫会放你走的。"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "[fz.cheng]您别赶奴婢走，奴婢会好好在您身边做事的！"
            $ tempgn.yexin -= 10
            hide tempgn
        elif 25 < fz.qingxiang < 75 or fz.xingge == "圆滑" or fz.xingge == "活泼":
            hide tempgn
            show fz
            妃子 "好你个[tempgn.name]，竟然背着本宫说出这般大逆不道的话！"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "奴婢知错，奴婢知错！还请娘娘宽恕奴婢这一回吧！"
            hide tempgn
            show fz
            妃子 "去外头跪三个时辰，今日的饭食也一应免了，再有下次，本宫决不轻饶！"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "是，奴婢遵命……"
            $ tempgn.yexin -= 20
            hide tempgn
        else:
            hide tempgn
            show fz
            妃子 "本宫这里供不起你这尊大佛，但至少还能让你如愿。"
            妃子 "按你所说，就回掖廷去吧。"
            hide fz
            show tempgn
            "[tempgn.level] [tempgn.name]" "不要啊娘娘，掖廷的人会打死奴婢的！娘娘饶命啊！"
            hide tempgn
            $ fz.Gongnv.remove(tempgn)
            $ tempgn.yexin += 100
            if tempgn.level == "散役":
                $ YTGongnv.append(tempgn)
                pass
            else:
                $ newgn = renpy.random.choice(YTGongnv)
                $ YTGongnv.remove(newgn)
                $ fz.Gongnv.append(newgn)
                $ YTGongnv.append(tempgn)
        show fz
        妃子 "[my.cheng]……你怎么也在这里？"
        我 "……"
        我 思 "（因为方才两个宫女闹得这一出，总觉得有些尴尬。）"
        menu:
            "温言安慰":
                if my.level <= fz.level:
                    我 笑 "妹妹莫为这些奴才动气，伤了自个儿身子。"
                    if fz.xingge == "娇纵" or fz.xingge == "清冷":
                        妃子 "（冷笑）到底是娘娘心平气和，嫔妾御下无方，身居帝王后宫，却不能慰侍君心，是万万比不上娘娘您的。"
                        妃子 "嫔妾该回去好好闭门反省了，还请娘娘恕嫔妾失陪了。"
                        $ fz.like -= 5
                        $ fz.qingxiang += 3
                    elif fz.xingge == "势利":
                        妃子 "（苦笑）这宫里的下人么，这副嘴脸嫔妾也是见惯了的，也碍不了什么。"
                        妃子 "打心眼儿里，嫔妾也是羡慕您的，更何况这些奴才呢？"
                        我 笑 "妹妹不必妄自菲薄。"
                        $ fz.qingxiang += 3
                    else:
                        妃子 "是嫔妾御下无方……嫔妾……到底是比不上您的。"
                        我 笑 "妹妹不必妄自菲薄。"
                        $ fz.like += 5
                        $ fz.qingxiang += 1
                else:
                    我 笑 "娘娘莫为这些奴才动气，伤了自个儿身子。"
                    if fz.xingge == "娇纵" or fz.xingge == "清冷":
                        妃子 "（冷笑）到底是[my.cheng]心平气和，本宫御下无方，身居帝王后宫，却不能慰侍君心，是万万比不上你的。"
                        妃子 "看来本宫该回去好好反省一下了，告辞。"
                        $ fz.like -= 5
                        $ fz.qingxiang += 3
                    elif fz.xingge == "势利":
                        妃子 "（苦笑）这宫里的下人么，这副嘴脸本宫也是见惯了的，也碍不了什么。"
                        妃子 "打心眼儿里，本宫也是羡慕您的，更何况这些奴才呢？"
                        我 笑 "娘娘不必妄自菲薄。"
                        $ fz.qingxiang += 3
                    else:
                        妃子 "是本宫御下无方，倒是比不上妹妹你了的。"
                        我 笑 "娘娘不必妄自菲薄。"
                        $ fz.like += 5
                        $ fz.qingxiang += 1
            "笑着解围":
                妃子 "是[tempgn.name]让[my.cheng]见笑了。"
                if fz.xingge == "娇纵" or fz.xingge == "清冷":
                    妃子 "不过左右是个奴才罢了，说出这些蠢话也算是给人寻了点乐子。"
                    $ fz.like += 2
                    $ fz.qingxiang += 2
                elif fz.xingge == "势利":
                    妃子 "[my.cheng]说的是，这点小事儿咱们都别放在心上了。"
                    妃子 "[my.cheng]能得皇上欢心，后宫姐妹都是高兴的，也就是这些鼠目寸光的奴才在后头嚼舌根了，可笑。"
                    $ fz.like += 2
                    $ fz.qingxiang += 2
                else:
                    $ fz.like += 2
                    $ fz.qingxiang += 2
            "无言离去":
                if fz.xingge == "娇纵" or fz.xingge == "清冷":
                    妃子 "（沉声）还真觉着自己一辈子都能占着皇上的心呐？"
                    妃子 "威风得了一时，威风得了一世？看不起谁呢……"
                    $ fz.like -= 8
                    $ fz.qingxiang += 5
                elif fz.xingge == "势利":
                    妃子 "[my.cheng]慢走咯……"
                    $ fz.like -= 3
                    $ fz.qingxiang += 3
                else:
                    妃子 "……"
                    $ fz.like -= 5
                    $ fz.qingxiang += 3
        hide 妃子





    elif fz.love >= 50 and fz.love > my.love:
        "女子的声音" "唉，同人不同命啊。你们主子怕是一年到头连皇上的面也见不到几回，在这宫里还有多少指望呢？"
        "另一个女子的声音" "也不知道你在炫耀什么的。花无百日红，你家主子有能耐一时得皇上欢心并不算什么，有能耐一辈子把皇上的心抓在手里，你再来同我炫耀吧！"
        "女子的声音" "你就是不服气！看你那眼红的样子，嘁，我是不知道[fz.cheng]能不能一世荣宠，但我知道[my.cheng]这辈子恐怕是没机会了。"
        "另一个女子的声音" "收敛些罢，若今日你这些话让别人听去了，可有你好果子吃了。"
        "女子的声音" "别人？你倒是告诉别人啊！"
        "女子的声音" "我先告诉你啊，我家主子可是会罩着我的，况且，我们主子说了，[my.cheng]手底下的人都同她们主子一样没用，不必放在眼里。"
        "女子的声音" "或者……你就去告诉[my.cheng]啊，看看[fz.cheng]会不会给她面子责罚我罢！"
        "另一个女子的声音" "你太过分了！"
        show 我的宫女 at chara
        我的宫女 "主子，前面好像是[fz.cheng]宫里的[tempgn.name]……在和[gn.name]说话。"
        hide 我的宫女
        menu:
            "上前":
                show gn
                "[gn.name]不欲于[fz.cheng]那宫女多言，兀自转身离开，却迎面看到了你。"
                "[gn.level] [gn.name]" "主子？！"
                "[gn.level] [gn.name]" "奴婢……"
                我 "本宫方才都听见了……"
                "[gn.level] [gn.name]" "啊……"
                menu:
                    "是我无能，委屈了你了":
                        "[gn.level] [gn.name]" "您不必这么说……"
                        "[gn.level] [gn.name]" "[tempgn.name]的性子总会让她吃到苦头的。"
                        "[gn.level] [gn.name]" "您放宽心。"
                        hide gn
                        $ gn.yexin -= 10
                        $ gn.like += 5
                    "来日定叫那人后悔":
                        "[gn.level] [gn.name]" "无论如何，奴婢都愿意陪在您身边。"
                        hide gn
                        show tempgn
                        "[tempgn.level] [tempgn.name]" "（并未离开，而是听到了你们的谈话。）"
                        "[tempgn.level] [tempgn.name]" "（小声）呵……真是痴人说梦，叫人好笑。这种趣事可得赶紧回去告诉[fz.cheng]让她也乐一乐。"
                        hide tempgn
                        $ gn.yexin += 20
                        $ fz.like -= 3
            "离开":



                我 思 "随她去罢。"
                我的宫女 "可[gn.name]今日受了这样大的委屈……"
                我 思 "那本宫又能怎样？"
                我 常 "[tempgn.name]说的话……有什么不对么？"
                我的宫女 "是……"
                $ gn.yexin += 50
                $ tempgn.yexin += 50
    else:

        pass
    return
 
