
label start_1:
    python:
        import copy
        weifen_list = []
        weifen_list = copy.deepcopy(weifen_Normal)
        yuanweifen = copy.deepcopy(weifen_Normal)
        yuanweifen = tuple(yuanweifen)
        beifei = len(yuanweifen)-1
        global yuanweifen

        for i in yuanweifen:
            if isinstance(i[1],str):
                pass
            else:
                i[1] = tuple(i[1])

        for i in weifen_list:
            if isinstance(i[1],tuple):
                i[1] = list(i[1])

    scene 冷宫内
    with fade
    $ nianhao = "建昭"
    $ money = 0
    $ year = 1
    $ month = renpy.random.randint(4,7)
    call hajime from _call_hajime_1
    $ lucky = renpy.random.randint(5,8)
    $ Creat_Feizi(lucky,0)
    $ sidi = renpy.random.choice(NPC_fz_list)
    $ sidi.like = -50
    if sidi.health <= 500:
        $ sidi.health = 500
    else:
        pass
    if sidi.xinji <= 500:
        $ sidi.xinji = 500
    else:
        pass
    if sidi.qingxiang <= 75:
        $ sidi.qingxiang = 75
    else:
        pass
    $ my.foes.append(sidi)
    $ sidi.foes.append(my)


    python:
        lucky = renpy.random.randint(0,10)
        if lucky > 8:
            lucky = 3
        elif lucky > 6:
            lucky = 2
        elif lucky > 4:
            lucky = 1
        else:
            lucky = 0
        num = 0
        while num < lucky :
            num += 1
            fz = renpy.random.choice(NPC_fz_list)
            Creat_Kids(fz)
            fz.exp += 100
        if lucky == 3:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)
            NPC_Kids_list[2].age = 0

        elif lucky == 2:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)

        elif lucky == 1:
            NPC_Kids_list[0].age = renpy.random.randint(0,3)
        else :
            pass
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("exp"),reverse = True)
        year = 4
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        for i in NPC_Kids_list:
            temptext = str(year-i.age)+"年"+str(month)+"月，为"+str(i.shengmu.name)+"所生。\n"
            i.story.append(temptext)
        for i in NPC_fz_list:
            Feizilevel_first(i)




    $ year = 4
    $ month += 3
    $ xiunvnum = renpy.random.randint(4,8)
    $ Creat_Feizi(xiunvnum,1)


    python:

        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
        Kidsnum = len(NPC_Kids_list)
        for i in NPC_fz_list:
            renpy.call("定义妃子",fz = i,from_current=False)

    image 皇后 = "Feizi/F[NPC_fz_list[0].face].webp"
    show 李公公 at chara
    李公公 "[my.xing]主子。"
    $ my.hao = ""
    $ my.weifen = weifen_list[beifei][1]
    我 惊 "……李公公？"
    我 思 "（他方才……叫我主子？）"
    李公公 "是啊，[my.xing]主子，今日有喜事呢。"
    我 惊 "喜事？"
    李公公 "皇上下旨接您出冷宫了。"
    我 "真、真的么？"
    我 "皇上终于替我昭雪冤屈了吗？"
    李公公 "那倒不是……天降祥瑞之兆，皇上特下旨大赦天下，这其中也包括——"
    我 常 "我？"
    李公公 "（拿出圣旨念了起来。）"

    python:
        my.shou = renpy.random.randint(45,65)
        if my.health < 300:
            my.shou = my.shou - renpy.random.randint(5,10)
        elif my.health > 700:
            my.shou = my.shou + renpy.random.randint(5,10)
        else:
            pass
        if my.beauty > 900:
            my.shou = my.shou - renpy.random.randint(5,10)
        elif my.beauty < 400:
            my.shou = my.shou + renpy.random.randint(5,10)
        else:
            pass

        tempnum = my.dance + my.book + my.cixiu + my.muzic
        tempnum2 = my.familylevel
        if my.familylocation == "义女":
            tempnum2 = my.familylevel + 2
        elif my.familylocation == "庶女":
            tempnum2 = my.familylevel + 1
        else:
            pass

        my.exp = (my.beauty +my.meili+my.qizhi)/250 + my.familylevel/4 + renpy.random.randint(-25, 25)
        if my.exp <= 0:
            my.exp = 0
        else:
            pass
        for i in my.sisters:
            if i.name == "魏锦书":
                pass
            else:
                i.like += renpy.random.randint(-50,80)
        tags_limitcheck(my)
        Feizilevel(my)

        if my.level < 11:
            lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""

        elif my.love > 10 :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""
        else:
            my.hao = ""
        my.story = []

        if my.hao == "":
            tempstory = str(nianhao)+"四年，于大赦天下时被接出冷宫，册为"+str(my.weifen)+"。\n"
            my.story.append(tempstory)
        else:
            tempstory = str(nianhao)+"四年，于大赦天下时被接出冷宫，册为"+str(my.weifen)+"，赐封号"+str(my.hao)+",是为"+str(my.hao)+str(my.weifen)+"。\n"
            my.story.append(tempstory)


        if my.hao =="":
            my.cheng = myname1 +my.weifen
        else:
            my.cheng = my.hao +my.weifen
        randompalace(my)
        NPC_fz_list.append(my)
        NPC_newfz_list.append(my)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
    $ allstory =[]
    $ tempstory = "【大事】"+"4年"+str(month)+"月，皇帝大赦天下。\n"
    $ allstory.insert(0,tempstory)
    李公公 "……着即接出冷宫，册为[my.hao][my.weifen]。"
    我 思 "臣妾……接旨。"
    李公公 "恭喜[my.hao][my.weifen]。"
    "李公公很快走了出去，片刻后便有宫人来替你收拾物什。"
    scene black
    "新帝登基不久，你便被奸人暗害，背上罪名，沦为新帝后宫中第一个被打入冷宫的妃嫔……"
    "一晃，竟已是三年过去了。"
    我 泪 "没有想到，居然我还有离开冷宫的这一天……"
    我 泪 "不知道[sidi.name]你有没有想过呢？"
    $ quick_menu = True
    $ _game_menu_screen = "save"
    $ qinjutu = "寝居1白天"
    scene 寝居
    with dissolve
    show screen notify(my.palace+my.qinju)

    python:

        if len(my.Gongnv) == 1:
            a = len(yuanweifen)
            if my.level == 0: 
                my.Gongnv[0].level = "长御"
                my.Gongnv[0].lv = 0
            elif my == 1: 
                my.Gongnv[0].level = "女官"
                my.Gongnv[0].lv = 1
            elif my.level > round(a-a/3):
                my.Gongnv[0].level = "贴身侍女"
                my.Gongnv[0].lv = 3
            else:
                my.Gongnv[0].level = "大宫女"
                my.Gongnv[0].lv = 2
        else:
            pass
        ChangeGongnv(my)





    if len(my.Gongnv) == 1:
        pass
    else:
        image 我的宫女 = "Gongnv/GN[my.Gongnv[0].face].webp"
        show 我的宫女 at chara
        我的宫女 "奴婢[my.Gongnv[0].name],参见[my.cheng]。以后就由奴婢伺候您的寝居了。"

    我的宫女 "奴婢对您的行事风格还不大清楚。不知[my.cheng]您打算以后如何规划宫里的开销呢？"
    menu:
        "节俭开销":
            $ kaixiao = 1
            我的宫女 "奴婢明白。"
        "正常开销":

            $ kaixiao = 2
            我的宫女 "奴婢明白。"
        "奢侈开销":

            $ kaixiao = 3
            我的宫女 "奴婢明白。"
        "详细解释":

            我的宫女 "节俭开销大概是您月俸的四分之一。{p}是最省钱的方式。{w}不过也会影响您的体质和在外的威信。"
            我的宫女 "普通开销大概是您月俸的一半。{p}对日常起居没有太大的影响。"
            我的宫女 "奢侈开销大概是您月俸的四分之三。{p}开销增大，自然也能让奴婢们多花心思增加为您强健体魄，也能树立起在外的威信。"
            我的宫女 "您打算如何安排呢？"
            menu:
                "节俭开销":
                    $ kaixiao = 1
                    我的宫女 "奴婢明白。"
                "正常开销":

                    $ kaixiao = 2
                    我的宫女 "奴婢明白。"
                "奢侈开销":

                    $ kaixiao = 3
                    我的宫女 "奴婢明白。"


    我的宫女 "您今日也是辛劳了，奴婢服侍您歇息吧。"


    hide screen calender
    scene black
    with fade
    旁白 "一夜过去……"
    python:
        for i in NPC_fz_list:
            i.paixu = beifei - i.level
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
    show screen calendar
    python:
        if my.health > 700:
            AP = 5
        elif my.health > 400:
            AP = 4
        elif my.health > 200:
            AP = 3
        elif my.health > 100:
            AP = 2
        elif my.health > 0:
            AP = 1
        else:
            AP = 0

    $ month = month +1
    $ datenum = 1
    $ timenum = 1
    jump 寝居界面



label start_2:
    python:
        import copy
        weifen_list = []
        weifen_list = copy.deepcopy(weifen_Normal)
        yuanweifen = copy.deepcopy(weifen_Normal)
        yuanweifen = tuple(yuanweifen)
        beifei = len(yuanweifen)-1
        global yuanweifen

        for i in yuanweifen:
            if isinstance(i[1],str):
                pass
            else:
                i[1] = tuple(i[1])

        for i in weifen_list:
            if isinstance(i[1],tuple):
                i[1] = list(i[1])

    scene black
    with fade
    $ nianhao = "建昭"
    $ money = 200
    $ year = 1
    $ month = 1
    call hajime from _call_hajime_2
    $ lucky = renpy.random.randint(5,8)
    $ Creat_Feizi(lucky,2)


    python:
        lucky = renpy.random.randint(0,10)
        if lucky > 8:
            lucky = 3
        elif lucky > 6:
            lucky = 2
        elif lucky > 4:
            lucky = 1
        else:
            lucky = 0
        num = 0
        while num < lucky :
            num += 1
            fz = renpy.random.choice(NPC_fz_list)
            Creat_Kids(fz)
            fz.exp += 100
        if lucky == 3:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)
            NPC_Kids_list[2].age = 0

        elif lucky == 2:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)

        elif lucky == 1:
            NPC_Kids_list[0].age = renpy.random.randint(0,3)
        else :
            pass
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        for i in NPC_Kids_list:
            temptext = "帝登基前，为"+str(i.shengmu.name)+"所生。\n"
            i.story.append(temptext)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("exp"),reverse = True)
        for i in NPC_fz_list:
            Feizilevel_first(i)

    python:

        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
        Kidsnum = len(NPC_Kids_list)
        for i in NPC_fz_list:
            renpy.call("定义妃子",fz = i,from_current=False)

    旁白 "“[aicheng]……”"
    nvl clear
    旁白 "“别怪父皇……”"
    nvl clear
    旁白 "“是父皇对不住你……是父皇无能。”"
    旁白 "“就当是……为了咱们的百姓。”"
    nvl clear
    旁白 "“殿下，你的子民，你的疆土，和[aicheng]究竟有何干系？”"
    nvl clear
    旁白 "“[aicheng]……父皇知道这些年薄待了你。可你的身体中，终究流淌着我北漠的血。”"
    nvl clear
    旁白 "“我这一去，能带来多少年的安宁？”"
    nvl clear
    旁白 "“十年？二十年？五十年……到我死，或是到我失宠的那一天？”"
    nvl clear
    旁白 "“对于一个皇朝，这样的岁月何其短暂？”"
    nvl clear
    旁白 "“而对于我来说，却是一个女子的一生。”"
    nvl clear
    旁白 "……"
    nvl clear
    旁白 "“父皇。这是我第一次这样叫你。”"
    nvl clear
    旁白 "“……女儿遵命。”"
    nvl clear
    $ my.hao = ""
    $ my.weifen = ""
    我 泪 "……"
    "婢女的声音" "公主……公主……"
    "婢女的声音" "我们到了……"

    我 常 "到了？"
    我 "这里就是……皇宫？"
    我 "哈……"
    "华美，却没有一丝人情味。"
    "庄严，压得人喘不过气来。"
    我 思 "我不喜欢这里。"


    python:
        my.shou = 50
        my.exp = weifen_list[0][3]*0.3

        tags_limitcheck(my)
        Feizilevel(my)
        for i in my.sisters:
            if i.name == "魏锦书":
                pass
            else:
                i.like += renpy.random.randint(-50,80)
        if my.level < 11:
            lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""

        elif my.love > 10 :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""
        else:
            my.hao = ""
        my.story = []

        tempstory = str(nianhao)+"元年，和亲入宫，册为"+str(my.hao)+str(my.weifen)+"。\n"
        my.story.append(tempstory)


        if my.hao =="":
            my.cheng = myname1 +my.weifen
        else:
            my.cheng = my.hao +my.weifen
        randompalace(my)
        NPC_fz_list.append(my)
        NPC_newfz_list.append(my)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
    $ allstory =[]
    $ tempstory = "【大事】"+"元年"+str(month)+"月，和亲公主"+str(my.name)+"入宫，册为"+str(my.hao)+str(my.weifen)+"。\n"
    $ allstory.insert(0,tempstory)

    $ quick_menu = True
    $ _game_menu_screen = "save"
    $ qinjutu = "寝居1白天"
    scene 寝居
    with dissolve
    show screen notify(my.palace+my.qinju)

    python:

        if len(my.Gongnv) == 1:
            a = len(yuanweifen)
            if my.level == 0: 
                my.Gongnv[0].level = "长御"
                my.Gongnv[0].lv = 0
            elif my == 1: 
                my.Gongnv[0].level = "女官"
                my.Gongnv[0].lv = 1
            elif my.level > round(a-a/3):
                my.Gongnv[0].level = "贴身侍女"
                my.Gongnv[0].lv = 3
            else:
                my.Gongnv[0].level = "大宫女"
                my.Gongnv[0].lv = 2
        else:
            pass
        ChangeGongnv(my)





    if len(my.Gongnv) == 1:
        pass
    else:
        image 我的宫女 = "Gongnv/GN[my.Gongnv[0].face].webp"
        show 我的宫女 at chara
        我的宫女 "奴婢[my.Gongnv[0].name],参见[my.cheng]。以后就由奴婢伺候您的寝居了。"

    我的宫女 "奴婢对您的行事风格还不大清楚。不知[my.cheng]您打算以后如何规划宫里的开销呢？"
    menu:
        "节俭开销":
            $ kaixiao = 1
            我的宫女 "奴婢明白。"
        "正常开销":

            $ kaixiao = 2
            我的宫女 "奴婢明白。"
        "奢侈开销":

            $ kaixiao = 3
            我的宫女 "奴婢明白。"
        "详细解释":

            我的宫女 "节俭开销大概是您月俸的四分之一。{p}是最省钱的方式。{w}不过也会影响您的体质和在外的威信。"
            我的宫女 "普通开销大概是您月俸的一半。{p}对日常起居没有太大的影响。"
            我的宫女 "奢侈开销大概是您月俸的四分之三。{p}开销增大，自然也能让奴婢们多花心思增加为您强健体魄，也能树立起在外的威信。"
            我的宫女 "您打算如何安排呢？"
            menu:
                "节俭开销":
                    $ kaixiao = 1
                    我的宫女 "奴婢明白。"
                "正常开销":

                    $ kaixiao = 2
                    我的宫女 "奴婢明白。"
                "奢侈开销":

                    $ kaixiao = 3
                    我的宫女 "奴婢明白。"


    我的宫女 "您今日也是辛劳了，奴婢服侍您歇息吧。"
    python:
        for i in NPC_fz_list:
            i.paixu = beifei - i.level
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)


    hide screen calender
    scene black
    with fade
    旁白 "一夜过去……"
    show screen calendar
    python:
        if my.health > 700:
            AP = 5
        elif my.health > 400:
            AP = 4
        elif my.health > 200:
            AP = 3
        elif my.health > 100:
            AP = 2
        elif my.health > 0:
            AP = 1
        else:
            AP = 0

    $ month = month +1
    $ datenum = 1
    $ timenum = 1
    jump 寝居界面



label start_kanxi:
    $ player = -1

    $ yuanweifen = weifen_Normal
    $ my = factory.instantiation_Feizi()
    $ my.face = "YF0"
    $ my.level = 999
    $ my.weifen = "旁观者"
    $ my.shiqin = 1


    python:
        import copy
        weifen_list = []
        weifen_list = copy.deepcopy(weifen_Normal)
        yuanweifen = copy.deepcopy(weifen_Normal)
        yuanweifen = tuple(yuanweifen)
        beifei = len(yuanweifen)-1
        global yuanweifen

        for i in yuanweifen:
            if isinstance(i[1],str):
                pass
            else:
                i[1] = tuple(i[1])

        for i in weifen_list:
            if isinstance(i[1],tuple):
                i[1] = list(i[1])


    $ nianhao = "建昭"
    $ my.skillcosts = 999
    $ money = 9999
    $ year = 1
    $ month = renpy.random.randint(4,7)
    call hajime from _call_hajime_3
    $ lucky = renpy.random.randint(5,8)
    $ Creat_Feizi(lucky,0)

    python:
        lucky = renpy.random.randint(0,10)
        if lucky > 8:
            lucky = 3
        elif lucky > 6:
            lucky = 2
        elif lucky > 4:
            lucky = 1
        else:
            lucky = 0
        num = 0
        while num < lucky :
            num += 1
            fz = renpy.random.choice(NPC_fz_list)
            Creat_Kids(fz)
            fz.exp += 100
        if lucky == 3:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)
            NPC_Kids_list[2].age = 0

        elif lucky == 2:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)

        elif lucky == 1:
            NPC_Kids_list[0].age = renpy.random.randint(0,3)
        else :
            pass
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("exp"),reverse = True)
        year = 4
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        for i in NPC_Kids_list:
            temptext = str(year-i.age)+"年"+str(month)+"月，为"+str(i.shengmu.name)+"所生。\n"
            i.story.append(temptext)
        for i in NPC_fz_list:
            Feizilevel_first(i)


    $ year = 4
    $ xiunvnum = renpy.random.randint(4,8)
    $ Creat_Feizi(xiunvnum,1)


    python:

        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
        Kidsnum = len(NPC_Kids_list)
        for i in NPC_fz_list:
            renpy.call("定义妃子",fz = i,from_current=False)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
    $ allstory =[]
    $ quick_menu = True
    $ _game_menu_screen = "save"
    $ qinjutu = "寝居1白天"
    scene 寝居
    with dissolve
    hide screen calender
    scene black
    with fade
    旁白 "一夜过去……"
    python:
        for i in NPC_fz_list:
            i.paixu = beifei - i.level
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
    show screen calendar
    python:
        if my.health > 700:
            AP = 5
        elif my.health > 400:
            AP = 4
        elif my.health > 200:
            AP = 3
        elif my.health > 100:
            AP = 2
        elif my.health > 0:
            AP = 1
        else:
            AP = 0

    $ month = month +1
    $ datenum = 1
    $ timenum = 1
    jump 寝居界面
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
