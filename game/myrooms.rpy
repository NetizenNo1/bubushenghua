screen myshuxing:
    style_prefix "myroom"
    $ shuxingmiaoshu(my)
    python:
        my.kidsnum = len(my.kids)
        my.Gongnvnum = len(my.Gongnv)

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" pos (100,0)

    fixed xsize 1280 ysize 720 align (0.5,0.5):

        add "gui/frame.webp" zoom 1.2 xalign 0.5 yalign 0.5
        side "tr bl":
            spacing 1280
            add "flower.webp"
            add "flower.webp"

    fixed xysize (345,450) xalign 0.2 yalign 0.25:
        if my.face not in pre_femaleface:
            add "Feizi/F[my.face].webp" maxsize (380,600) align (0.5,1.0)
        else:
            add "Feizi/F[my.face].webp" align (0.5,1.0)







    $ barexp = my.exp - weifen_list[my.level][3]
    $ barrange = weifen_list[my.level][4]  - weifen_list[my.level][3]
    text "{font=问藏书房.ttf}{size=35}威望:" pos (320,600)
    bar value AnimatedValue(value=barexp,range = barrange) xmaximum 0.1 pos (410,600)
    text str(int(my.exp))+"/"+ str(weifen_list[my.level][4]) pos (410,600)
    textbutton "技能" pos (320,650) action Show("myskills_1")
    textbutton "特殊人物属性" pos (320,700) action Hide("myshuxing"),Show("specialNPC")



    text "{font=问藏书房.ttf}{size=35}〈[my.hao][my.weifen]〉[my.name]" pos (570,180):
        outlines [ (absolute(1), "#8abad2", absolute(1), absolute(0.5)) ]
    text "{font=问藏书房.ttf}{size=25}年龄:" + str(my.age) pos (585,230)
    text "{font=问藏书房.ttf}{size=25}资历:" + str(my.year)+"年" pos (740,230)
    text "{font=问藏书房.ttf}{size=25}银两:[money]" pos (585,270)
    text "{font=问藏书房.ttf}{size=25}状态:" + str(my.state) pos (740,270)
    textbutton "{font=问藏书房.ttf}体质:[my.healthlv]":
        pos (585,310)
        action NullAction()
        hovered Show("scrtt",tt=int(my.health))
        unhovered [Hide("scrtt")]
    textbutton "{font=问藏书房.ttf}容貌:[my.beautylv]":
        pos (750,340)
        action NullAction()
        hovered Show("scrtt",tt=int(my.beauty))
        unhovered [Hide("scrtt")]
    textbutton "{font=问藏书房.ttf}气质:[my.qizhilv]":
        pos (585,370)
        action NullAction()
        hovered Show("scrtt",tt=int(my.qizhi))
        unhovered [Hide("scrtt")]
    textbutton "{font=问藏书房.ttf}魅力:[my.meililv]":
        pos (750,400)
        action NullAction()
        hovered Show("scrtt",tt=int(my.meili))
        unhovered [Hide("scrtt")]
    textbutton "{font=问藏书房.ttf}圣宠:[my.lovelv]":
        pos (585,430)
        action NullAction()
        hovered Show("scrtt",tt=int(my.love))
        unhovered [Hide("scrtt")]
    textbutton "{font=问藏书房.ttf}心计:[my.xinjilv]":
        pos (750,460)
        action NullAction()
        hovered Show("scrtt",tt=int(my.xinji))
        unhovered [Hide("scrtt")]

    textbutton "{size=28}{font=问藏书房.ttf}音律:[my.muziclv] ":
        pos (585,530)
        action NullAction()
        hovered Show("scrtt",tt=int(my.muzic))
        unhovered [Hide("scrtt")]
    textbutton "{size=28}{font=问藏书房.ttf}舞蹈:[my.dancelv]":
        pos (765,530)
        action NullAction()
        hovered Show("scrtt",tt=int(my.dance))
        unhovered [Hide("scrtt")]
    textbutton "{size=28}{font=问藏书房.ttf}才学:[my.booklv]":
        pos (585,580)
        action NullAction()
        hovered Show("scrtt",tt=int(my.book))
        unhovered [Hide("scrtt")]
    textbutton "{size=28}{font=问藏书房.ttf}刺绣:[my.cixiulv]":
        pos (765,580)
        action NullAction()
        hovered Show("scrtt",tt=int(my.cixiu))
        unhovered [Hide("scrtt")]
    if my.medic == 0:
        pass
    else:
        textbutton "{size=28}{font=问藏书房.ttf}医术:[my.mediclv]":
            pos (585,630)
            action NullAction()
            hovered Show("scrtt",tt=int(my.medic))
            unhovered [Hide("scrtt")]


    vbox align (0.65,0.2):
        text "金兰挚友" align (0.5,0.5)
        for i in NPC_fz_list:
            if i.like >= 80 and i != my:
                text "{size=20}【"+i.hao+i.weifen+"】"+i.name align (0.5,0.5)
            else:
                pass
    vbox align (0.8,0.2):
        text "志同道合" align (0.5,0.5)
        for i in my.friends:
            text "{size=20}【"+i.hao+i.weifen+"】"+i.name align (0.5,0.5)
    vbox align (0.8,0.55):
        text "结怨仇敌" align (0.5,0.5)
        for i in my.foes:
            text "{size=20}【"+i.hao+i.weifen+"】"+i.name align (0.5,0.5)
    vbox align (0.65,0.55):
        text "不共戴天" align (0.5,0.5)
        for i in NPC_fz_list:
            if i.like < -20:
                text "{size=20}【"+i.hao+i.weifen+"】"+i.name align (0.5,0.5)
            else:
                pass




style myroom_button is default:
    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"


screen specialNPC:
    style_prefix "myroom"
    fixed xsize 1280 ysize 720 align (0.5,0.5):
        add "gui/frame.webp" zoom 1.2 xalign 0.5 yalign 0.5
        side "tr bl":
            spacing 1280
            add "flower.webp"
            add "flower.webp"
    frame:
        xsize 1280
        ysize 720
        align (0.5,0.5)
        background None
        grid 2 2:
            xspacing 50
            align (0.5,0.5)
            vbox spacing 5:
                text "【皇帝 [guoxing][emperor]】"
                text "年龄:[hdage]"
                text "性格:[hdxingge]"
                text "国力："+str(huangdi["国力"])
                text "政务："+str(huangdi["政务"])
                text "军事："+str(huangdi["军事"])


                hbox:
                    text "暴戾"
                    bar value AnimatedValue(value=100 - huangdi["暴戾"],range = 100) xmaximum 0.1 ymaximum 0.05
                    text "宽宏"
                hbox:
                    text "昏庸"
                    bar value AnimatedValue(value=100 -huangdi["昏庸"],range = 100) xmaximum 0.1 ymaximum 0.05
                    text "贤明"
            vbox:
                text "【[太后]】"
                text "年龄:[taihouage]"
                text "性格:[taihouxinge]"
                text "好感:[my.taihoulike]"
            vbox:
                text "【父亲 [my.father.name]】"
                text "年龄：[my.father.age]"
                text "容貌：[my.father.beauty]"
                text "忠诚：[my.father.zhong]"
                text "能力："+str(int(my.father.neng))
                text "势力："+str(int(my.father.shili))
                text "功勋："+str(int(my.father.exp))
            null
        textbutton "关闭" align (0.5,0.8) action Hide("specialNPC"),Show("myshuxing")



screen myroom:
    style_prefix "myroom"


    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        align (0.5,0.5)
        xsize 960
        ysize 540

        hbox xalign 0.5 yalign 0.3:
            spacing 40
            if AP == 0:
                textbutton "练习音律"
                textbutton "训练舞技"
                textbutton "研读诗书"
                textbutton "女红刺绣"
            else:
                textbutton "练习音律" action Hide("myroom"),Jump("练习音律")
                textbutton "训练舞技" action Hide("myroom"),Jump("训练舞技")
                textbutton "研读诗书" action Hide("myroom"),Jump("研读诗书")
                textbutton "女红刺绣" action Hide("myroom"),Jump("女红刺绣")


        hbox xalign 0.5 yalign 0.5:
            spacing 40
            textbutton "请平安脉" action Hide("myroom"),Jump("请平安脉")
            textbutton "殿内休息" action Jump("寝居休息"),Hide("myroom")
            if jinzu(my) == True:
                textbutton "离开寝居"
            else:
                textbutton "离开寝居" action Hide("myroom"),Hide("fz_jm"),Hide("myshuxing"),Jump("皇宫界面")
            textbutton "结束本旬" action Hide("myroom"),Jump("结束本旬")


        hbox xalign 0.5 yalign 0.75:
            spacing 40
            textbutton "{size=40}宫廷事务" action Show("gdjm_ready"),Hide("myroom")
            textbutton "{font=问藏书房.ttf}{size=40}库房管理" action Show("kufang",fz = my),Hide("myroom")
            if len(NPC_Kids_list)== 0:
                textbutton "{font=问藏书房.ttf}{size=40}查看皇嗣"
            elif len(my.kids) == 0:
                textbutton "{font=问藏书房.ttf}{size=40}查看皇嗣" action Show("kids",list = NPC_Kids_list),Hide("myroom")
            else:
                textbutton "{font=问藏书房.ttf}{size=40}查看皇嗣" action Show("kids",list = my.kids),Hide("myroom")

            textbutton "{font=问藏书房.ttf}{size=40}宫女管理" action Show("myGongnv"),Hide("myroom")
    add "flower.webp" align (0.19,0.85)





screen gdjm2():
    add "gui/frame.webp" zoom 1 xalign 0.5 yalign 0.5
    default gdjm = "all"
    viewport:
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        xsize 600
        ysize 400
        align (0.5,0.5)
        has vbox
        for i in zysj:
            $ tempnum = 100 - i.jilv
            fixed xysize (600,200):
                vbox:
                    if i.time1 > -1:
                        text "（准备中）"+str(i.time1)
                    else:
                        text "（调查中）"+str(i.time2)
                    text "当事人:"+i.bei.hao + i.bei.weifen + i.bei.name + "  事件:" +str(i.way)
                    text "发起人:" + i.zhu.hao + i.zhu.weifen + i.zhu.name
                    text "参与者:妃嫔" + str(len(i.hemou)) + "人 宫女" + str(len(i.gn)) + "人 "
                    text "剩余调查回合:" + str(i.time2)
                    text "调查成功几率:" + str(tempnum)
                    text ""

screen allstory():
    add "gui/frame.webp" zoom 1.2 xalign 0.5 yalign 0.5
    default storylist = "近事"
    default textlist = ""

    viewport:
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        xsize 950
        ysize 600
        align (0.5,0.5)
        has vbox

        if storylist == "近事":
            for i in allstory[0:150]:
                $ textlist = textlist + i
                if i[0:4] =="【圣旨】" or i[0:4] =="【前朝】":
                    text i:
                        color "#FF8C00"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【大事】":
                    text i:
                        color "#990000"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【讣告】":
                    text i:
                        color "#ABABAB"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【闲言】":
                    text i:
                        color "#000000"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【争锋】":
                    pass

                else:
                    pass
        elif storylist == "全部":
            for i in allstory:
                $ textlist = textlist + i
                if i[0:4] =="【圣旨】" or i[0:4] =="【前朝】":
                    text i:
                        color "#FF8C00"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【大事】":
                    text i:
                        color "#990000"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【讣告】":
                    text i:
                        color "#ABABAB"
                        size 22
                        font "问藏书房.ttf"
                if i[0:4] =="【闲言】":
                    text i:
                        color "#000000"
                        size 22
                        font "问藏书房.ttf"
                else:
                    pass


        elif storylist == "圣旨":
            for i in allstory:
                if i[0:4] =="【圣旨】" or i[0:4] =="【前朝】":
                    $ textlist = textlist + i
                    text i[4:-1]:
                        size 25
                        color "#000000"
                        font "问藏书房.ttf"

                else:
                    pass
        elif storylist == "大事":
            for i in allstory:
                if i[0:4] =="【大事】":
                    $ textlist = textlist + i
                    text i[4:-1]:
                        color "#000000"
                        size 25
                        font "问藏书房.ttf"
                elif i[0:4] =="【讣告】":
                    $ textlist = textlist + i
                    text i[4:-1]:
                        color "#ABABAB"
                        size 25
                        font "问藏书房.ttf"
                else:
                    pass
        elif storylist == "闲言":
            for i in allstory:
                if i[0:4] =="【闲言】":
                    $ textlist = textlist + i
                    text i[4:-1]:
                        color "#000000"
                        size 25
                        font "问藏书房.ttf"

                else:
                    pass
        elif storylist == "争锋":
            for i in allstory:
                if i[0:4] =="【争锋】":
                    $ textlist = textlist + i
                    text i[4:-1]:
                        color "#000000"
                        size 25
                        font "问藏书房.ttf"

                else:
                    pass
        else:
            pass


        text ""
        text ""
        text ""
    vbox xalign 0.85 yalign 0.25:
        textbutton "{size=40}{font=问藏书房.ttf}近事" action SetScreenVariable("storylist","近事"),SetScreenVariable("textlist","")
        textbutton "{size=40}{font=问藏书房.ttf}圣旨" action SetScreenVariable("storylist","圣旨"),SetScreenVariable("textlist","")
        textbutton "{size=40}{font=问藏书房.ttf}大事" action SetScreenVariable("storylist","大事"),SetScreenVariable("textlist","")
        textbutton "{size=40}{font=问藏书房.ttf}闲言" action SetScreenVariable("storylist","闲言"),SetScreenVariable("textlist","")
        textbutton "{size=40}{font=问藏书房.ttf}争锋" action SetScreenVariable("storylist","争锋"),SetScreenVariable("textlist","")
        textbutton "{size=40}{font=问藏书房.ttf}全部" action SetScreenVariable("storylist","全部"),SetScreenVariable("textlist","")

    textbutton "{size=20}{font=问藏书房.ttf}复制" align (0.82,0.7) action Function(scrubs, textlist)
    imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
        align (0.85,0.85)
        action Hide("allstory")






screen mystory():
    add "gui/frame.webp" xalign 0.45 yalign 0.25
    viewport:
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        xsize 800
        ysize 480
        align (0.45,0.25)
        has vbox
        text my.family+"。":
            pos (80,80)
        text my.story:
            pos (80,105)


    imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
        align (0.6,0.6)
        action Hide("mystory")


screen mykids2(list):

    frame:
        xysize (1280,850)
        align (0.5,0.5)


        viewport:
            draggable True
            mousewheel True
            scrollbars "horizontal"
            xsize 1200
            ysize 820
            align (0.5,0.5)



            has vbox spacing 10
            for i in list:
                python:
                    health = int(i.health)
                    beauty = int(i.beauty)
                    wen = int(i.wen)
                    wu = int(i.wu)
                    duli = int(i.duli)
                    qinmian = int(i.qinmian)
                    like = int(i.like)

                fixed xmaximum 1000 ymaximum 263:
                    hbox spacing 20:
                        add "images/Kid/[i.face].webp" maxsize (188,263) align (0.5,1.0)
                        vbox yalign 0.5:
                            text "[i.cheng] [i.name]" align (0.5,0.5)
                            text "母妃:" align (0.5,0.5)
                            text "[i.mother.hao][i.mother.weifen][i.mother.name]" align (0.0,0.5)
                            text "生母:" align (0.5,0.5)
                            text "[i.shengmu.hao][i.shengmu.weifen] [i.shengmu.name]" align (0.5,0.5)

                        vbox:
                            text "{size=25}年龄:[i.age]岁" align (0.0,0.5)
                            text "{size=25}好感:[like]" align (0.0,0.5)
                            if i.marry != []:
                                text "{size=35}（已离宫）" align (0.5,0.5)
                                text "{size=25}[i.fenghao]（配偶:[i.marry[0].family][i.marry[0].name]）"
                            elif i.age >= 5 and timenum <= 3:
                                textbutton "{size=35}（上课中）" align (0.5,0.5)
                            elif timenum == 5:
                                textbutton "{size=35}（已歇息）" align (0.5,0.5)
                            else:
                                textbutton "{size=35}召见" align (0.5,0.5) action Hide("kids"),Call("召见子嗣",kid = i)
                        vbox:
                            text "{size=25}体质:[health]  容貌:[beauty]" align (0.0,0.5)
                            if i.sex == "皇子":
                                text "{size=25}学识:[wen]  武艺:[wu]" align (0.0,0.5)
                            else:
                                text "{size=25}学识:[wen]  才艺:[wu]" align (0.0,0.5)
                            text "{size=25}独立:[duli] 勤勉:[qinmian]" align (0.0,0.5)


                            if i.age >= 5:
                                text "{size=25}性格:[i.xingqing]" align (0.0,0.5)
                                text "{size=25}评价:[i.pingjia]" align (0.0,0.5)

                            else:
                                text "{size=25}性格:[i.xingge]" align (0.0,0.5)
                                text "{size=25}评价:暂无" align (0.0,0.5)
                            text "{size=25}天资:[i.iq]" align (0.0,0.5)
                            if persistent.ycsz == False:
                                text "{size=25}器重:[i.hdlike]"
                            else:
                                pass
                            if i.age >= 5 and i.marry == []:
                                text "{size=25}培养方式:[i.plan]"
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


        vbox align (1.0,0.0):
            textbutton "我的" action Hide("kids"),Show("kids",list = my.kids)
            textbutton "全部" action Hide("kids"),Show("kids",list = NPC_Kids_list)
        textbutton "关闭":
            align (1.0,1.0)
            action Hide("kids"),Show("myroom")













screen myGongnv():
    style_prefix "Gongnv"
    add "gui/frame.webp" zoom 1.5 xalign 0.45 yalign 0.25
    $ a = len(my.Gongnv) + 1
    frame:
        background None
        xsize 1350
        ysize 480
        align (0.4,0.3)
        has grid 1 a
        pos (0.05,0.0)
        xsize 1350
        ysize 900
        fixed:
            xsize 1350
            ysize 40
            hbox:
                spacing 25
                text "操作"
                text "职位"
                text "名字"
                text "年龄"
                text "外貌"
                text "性格"
                text "野心"
                text "好感"
                text "特长"

        for i in my.Gongnv:
            fixed:
                xsize 1350
                ysize 40
                align (0.5,1.0)
                hbox yalign 1.0:
                    spacing 30
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

                        if i.yexin >900:
                            i.yexinlv = "{color=#FF3030}野心勃勃{/color}"
                        elif i.yexin >700:
                            i.yexinlv = "{color=#EE00EE}追名逐利{/color}"
                        elif i.yexin >400:
                            i.yexinlv = "{color=#0040FF}八面玲珑{/color}"
                        elif i.yexin >200:
                            i.yexinlv = "{color=#008000}锋芒未露{/color}"
                        elif i.yexin >100:
                            i.yexinlv = "{color=#2F4F4F}恪守本分{/color}"
                        else:
                            i.yexinlv = "{color=#A1A1A1}赤子之心{/color}"

                    if i.state == "寻常":
                        textbutton "{font=问藏书房.ttf}召见" action Hide("myGongnv"),Call("管理宫女",gn = i)
                    else:
                        textbutton "{font=问藏书房.ttf}{size=20}任务中"

                    text "[i.level]"
                    text "[i.name]"
                    text "[i.age]"
                    text "[i.beautylv]"
                    text "[i.xingge]"
                    text "[i.yexinlv]"
                    text "[i.like]"
                    python:
                        tempskill = ""

                        for i in i.skill:
                            tempskill = tempskill + i + " "

                    text "{size=20}[tempskill]" align (0.5,0.5)


    imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
        align (0.9,0.8)
        action Hide("myGongnv"),Show("myroom")


style Gongnv_text:
    size 25
    min_width 100
    text_align 0.5



style kufang_text:
    min_width 400
    text_align 0.5


init python:
    item_page=0


screen kufang(fz):
    style_prefix "kufang"
    $ next_item_page = item_page + 1
    $ prev_item_page = item_page - 1
    $ max_item_page = round(len(kufang)/6)
    $ b = item_page*6+6

    if b >= len(kufang):
        $ b = len(kufang)
    else:
        pass

    frame:

        xsize 1200
        ysize 480
        align (0.4,0.3)
        hbox:
            align (0.5, 1.0)
            spacing 0
            if item_page > 0:
                textbutton "《《" action SetVariable('item_page', prev_item_page), Show("kufang",fz = fz)
            else:
                textbutton "《《"
            text "第[next_item_page]页"
            if item_page < max_item_page:
                textbutton "》》" action SetVariable('item_page', next_item_page), Show("kufang",fz = fz)
            else:
                textbutton "》》"
        grid 3 2:
            pos (0.07,0.0)
            xsize 800
            ysize 400
            $ a = 0
            $ next_item_page = item_page + 1
            for i in kufang[item_page*6:b]:
                if a <= b:
                    fixed:
                        xsize 311
                        ysize 176
                        if mapname == "寝居":
                            imagebutton idle "gui/物品.webp" hover "gui/物品2.webp":
                                action Call("使用物品",item = i)
                        else:
                            if i.leibie != "舞谱" and i.leibie != "曲谱" and i.leibie != "毒药":
                                imagebutton idle "gui/物品.webp" hover "gui/物品2.webp":
                                    action Call("赠送物品",item = i,fz = fz)
                            else:
                                imagebutton idle "gui/物品.webp" hover "gui/物品.webp"
                        text "{size=40}{font=问藏书房.ttf}[i.name]{/outlinecolor}" align (0.5, 0.3):
                            outlines [ (absolute(1), "#F8F8FFaa", absolute(0), absolute(0)) ]
                        text "{font=问藏书房.ttf}{size=20}类别:[i.leibie]\n{font=问藏书房.ttf}{size=20}风格:[i.fengge] " align (0.5, 0.7)

                    $ a = a + 1
                else:
                    null
            if a < 6:
                for j in range(a, 6):
                    null

        hbox align (1.0,1.0):
            if mapname == "寝居":
                imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
                    action Hide("kufang"),Show("myroom")
            else:
                imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
                    action Hide("kufang"), Return()
 
