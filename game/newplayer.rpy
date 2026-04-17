
init python:
    def myname1_func(newstring):
        store.myname1 = newstring


    def myname2_func(newstring):
        store.myname2 = newstring


init:

    default player0 = Gameplayer(code=0,ch="绘卷之人",jieshao="“人生尚且一片空白，但心却未必。”",name="沈氏容儿（可自定）",face = "RE0",age="可自定",jiashi="可自定",zizhi="未知",teshu="无",jingli="她可能是这深宫中的任何一个人，也可以谁也不是。但她一定是你。\n她是怎样一个人，又为何来到这里？答案只有你知道。",story=0,gametip="游戏难度：？？？\n通关要求：寿终正寝\n")
    default player1 = Gameplayer(code=1,ch="绝处逢生",jieshao="“既自尘埃中重生，便不会在尘埃中覆灭。”",name="应氏福遥（可自定）",face = "FY0",age="可自定",jiashi="可自定",zizhi="平庸",teshu="宫中必定有一位势同水火的高位嫔妃",jingli="被人陷害而在冷宫度过了三年岁月。\n从冷宫里出来的那一刻，她想她再也不会来这个鬼地方了。",story=0,gametip="游戏难度：困难\n通关要求：宿敌仍在后宫内的情况下，三年内位份、威望、宠爱均超过宿敌且拥有至少一名皇嗣。\n")
    default player2 = Gameplayer(code=1,ch="赤鸩妖妃",jieshao="“鬼鸩一品红，某个北漠小国独有的一种毒药，无形无味无色，既出必死。”",name="燕氏元照（可自定）",face = "YF0",age="可自定",jiashi="和亲公主",zizhi="出众",teshu="待补",jingli="待补",story=0,gametip="游戏难度：简单\n通关要求：待补\n")
    default playerlist = [player0,player1,player2]
    default myname1 = " "
    default myname2 = " "

    default my_face = ""
    default my_face_Normal = ""
    default my_face_Smile = ""
    default my_face_Think = ""
    default my_face_Cry = ""
    default my_face_Amaze = ""
    default my_face_Angry = ""

    image side my:
        Composite(
        (1600, 416),
        (18, 55), my_face,)
    image side my 常:
        Composite(
        (1600, 416),
        (18, 55), my_face_Normal,)
    image side my 笑:
        Composite(
        (1600, 416),
        (18, 55), my_face_Smile,)
    image side my 泪:
        Composite(
        (1600, 416),
        (18, 55), my_face_Cry,)
    image side my 思:
        Composite(
        (1600, 416),
        (18, 55), my_face_Think,)
    image side my 惊:
        Composite(
        (1600, 416),
        (18, 55), my_face_Amaze,)
    image side my 怒:
        Composite(
        (1600, 416),
        (18, 55), my_face_Angry,)



style newplayer_button is default:
    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"

style newplayer_button_text:
    size 28
    color "#490202"
    hover_color "#B22222"
    font "问藏书房.ttf"



screen choiceplayer:

    frame:
        background None
        add "gui/frame.webp" size (1600,900) xalign 0.5 yalign 0.5
        vbox xalign 0.2 yalign 0.3:
            text "{size=40}请选择初始角色"
            text "{size=20} "
            textbutton "绘卷之人沈氏容儿" action SetVariable("tempnum",0)
            textbutton "绝处逢生应氏福遥" action SetVariable("tempnum",1)
            textbutton "赤鸩妖妃燕氏元照" action SetVariable("tempnum",2)
            textbutton "敬请期待"
        hbox xalign 0.7 yalign 0.3:
            use playerjieshao(player=playerlist[tempnum])


style playerjieshao_text:
    size 25
    font "问藏书房.ttf"

screen playerjieshao(player):
    style_prefix "playerjieshao"
    frame:
        background None
        xysize (600,300)
        has vbox
        text "{size=40}"+ player.ch + player.name
        text "——"+ player.jieshao
        text "初始年龄："+ str(player.age)
        text "家世："+ player.jiashi
        text "资质："+ player.zizhi
        text "经历："+ player.jingli
        text "特殊说明："+ player.teshu
        text player.gametip
        if tempnum == 0:
            textbutton "选定" action Jump("newplayer_0")
        elif tempnum == 1:
            textbutton "选定" action Jump("newplayer_1")
        else:
            textbutton "选定" action Jump("newplayer_2")

screen makenewplayer():
    style_prefix "newplayer"
    frame:
        xysize (1280,720)
        align (0.5,0.5)
        fixed xysize (300,400) xalign 0.05 yalign 0.1:
            add "Feizi/F"+str(my.face)+".webp" align (0.5,1.0)
        vbox xsize 300 xalign 0.05 yalign 0.9 spacing 5:
            if player == 0:
                textbutton "{font=问藏书房.ttf}{size=35}默认形象" action SetVariable("my.face", "RE0") xalign 0.5
            else:
                textbutton "{font=问藏书房.ttf}{size=35}默认形象" action SetVariable("my.face", "FY0") xalign 0.5
            textbutton "{font=问藏书房.ttf}{size=35}更换丹青" action Jump("selectmyface") xalign 0.5

            textbutton "{font=问藏书房.ttf}{size=35}输入编号" action Jump("changemyface") xalign 0.5
            textbutton "{font=问藏书房.ttf}{size=20}妃子立绘库数量" action Jump("changefacenum") xalign 0.5




        if my.family == "暂无":
            text "请先选择家世！":
                align (0.5,0.05)
                size 40
        else:
            text "可用点数：[sxjd]":
                align (0.5,0.05)
                size 40

        frame:
            align (1.0,0.05)
            use choicetags


        textbutton "{font=问藏书房.ttf}{size=35}随机属性":
            action Function(resetshuxing,)
            align (0.5,0.88)

        textbutton "{font=问藏书房.ttf}{size=35}创建完成" action Jump("makenewplayer2"),Hide("makenewplayer"),Hide("text_input_screen"):
            align (0.5,0.98)


        grid 2 3:
            align (0.5,0.2)
            spacing 15
            text "{size=34}{font=问藏书房.ttf}姓名:[myname1][myname2]{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}更改{/font}{/size}" action ToggleScreen("text_input_screen")

            text "{size=34}{font=问藏书房.ttf}年龄:[my.age]{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}更改{/font}{/size}" action Jump("selectmyage")

            text "{size=34}{font=问藏书房.ttf}家世:[my.family]{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}更改{/font}{/size}" action Jump("selectmyfamily")

        grid 2 5:
            xspacing 50
            yspacing 5
            align (0.47,0.7)
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "体质:"
                    if my.health > 200 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.health", my.health-100),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    textbutton my.healthlv + str(my.health)[0] + " ? ?"
                    if my.health < 900 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.health", my.health+100),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "容貌:"
                    if my.beauty> 200 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.beauty", my.beauty-100),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    textbutton my.beautylv + str(my.beauty)[0] + " ? ?"
                    if my.beauty < 800 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.beauty", my.beauty+100),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "气质:"
                    if my.qizhi> 200 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.qizhi", my.qizhi-100),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    textbutton my.qizhilv + str(my.qizhi)[0] + " ? ?"
                    if my.qizhi < 800 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.qizhi", my.qizhi+100),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "魅力:"
                    if my.meili> 200 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.meili", my.meili-100),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    textbutton my.meililv + str(my.meili)[0] + " ? ?"
                    if my.meili < 800 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.meili", my.meili+100),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "心计:"
                    if my.xinji> 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.xinji", my.xinji-100),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    if my.xinji == 0:
                        textbutton my.xinjilv + str(my.xinji)
                    else:
                        textbutton my.xinjilv + str(my.xinji)[0] + " ? ?"
                    if my.xinji < 800 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.xinji", my.xinji+100),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "福缘:"
                    if my.lucky> 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.lucky", my.lucky-10),SetVariable("sxjd", sxjd+1)

                    else:
                        textbutton "↓"
                    if my.lucky < 10:
                        textbutton str(my.lucky)
                    else:
                        textbutton str(my.lucky)[0] + " ?"
                    if my.lucky < 80 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.lucky", my.lucky+10),SetVariable("sxjd", sxjd-1)
                    else:
                        textbutton "↑"

            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "音律:"
                    if my.muzic > 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.muzic", my.muzic-10),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    if my.muzic >= 90 or my.muzic < 10:
                        textbutton my.muziclv
                    else:
                        textbutton my.muziclv + str(my.muzic)[0] + " ?"
                    if my.muzic < 90 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.muzic", my.muzic+10),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "舞蹈:"
                    if my.dance > 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.dance", my.dance-10),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    if my.dance >= 90 or my.dance < 10:
                        textbutton my.dancelv
                    else:
                        textbutton my.dancelv + str(my.dance)[0] + " ?"
                    if my.dance < 90 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.dance", my.dance+10),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "才学:"
                    if my.book > 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.book", my.book-10),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    if my.book >= 90 or my.book < 10:
                        textbutton my.booklv
                    else:
                        textbutton my.booklv + str(my.book)[0] + " ?"
                    if my.book < 90 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.book", my.book+10),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"
            fixed xysize (250,50):
                hbox:
                    spacing 5
                    textbutton "刺绣:"
                    if my.cixiu > 0 and sxjd >= 0:
                        textbutton "↓" action SetVariable("my.cixiu", my.cixiu-10),SetVariable("sxjd", sxjd+1),Function(shuxingmiaoshu,my)

                    else:
                        textbutton "↓"
                    if my.cixiu >= 90 or my.cixiu < 10:
                        textbutton my.cixiulv
                    else:
                        textbutton my.cixiulv + str(my.cixiu)[0] + " ?"
                    if my.cixiu < 90 and sxjd >= 1:
                        textbutton "↑" action SetVariable("my.cixiu", my.cixiu+10),SetVariable("sxjd", sxjd-1),Function(shuxingmiaoshu,my)
                    else:
                        textbutton "↑"





screen makenewplayer_YF():
    style_prefix "newplayer"
    frame:
        xysize (1280,720)
        align (0.5,0.5)
        fixed xysize (300,400) xalign 0.1 yalign 0.2:
            add "Feizi/F"+str(my.face)+".webp" align (0.5,1.0)
        vbox xsize 300 xalign 0.1 yalign 0.9 spacing 5:

            textbutton "{font=问藏书房.ttf}{size=35}默认形象" action SetVariable("my.face", "YF0") xalign 0.5
            textbutton "{font=问藏书房.ttf}{size=35}更换丹青" action Jump("selectmyface_YF") xalign 0.5
            textbutton "{font=问藏书房.ttf}{size=35}输入编号" action Jump("changemyface_YF") xalign 0.5
            textbutton "{font=问藏书房.ttf}{size=20}妃子立绘库数量" action Jump("changefacenum_YF") xalign 0.5
        textbutton "{font=问藏书房.ttf}{size=35}创建完成" action Jump("makenewplayer2"),Hide("makenewplayer_YF"),Hide("text_input_screen"):
            align (0.5,0.95)
        text "创建人物":
            align (0.5,0.05)
            size 40
        grid 2 3:
            align (0.6,0.2)
            spacing 15
            text "{size=34}{font=问藏书房.ttf}姓名:[myname1][myname2]{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}更改{/font}{/size}" action ToggleScreen("text_input_screen")

            text "{size=34}{font=问藏书房.ttf}年龄:[my.age]{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}更改{/font}{/size}" action Jump("selectmyage_YF")


            text "{size=34}{font=问藏书房.ttf}家世:北国和亲公主{/font}{/size}"
            textbutton "{size=34}{font=问藏书房.ttf}固定{/font}{/size}"






screen nofamily():
    frame:
        xysize (800,352)
        align (0.7,0.5)
        text "请选择人物家世。":
            size 40
            align (0.5,0.2)
        textbutton "返回" action Show("makenewplayer"),Hide("nofamily"):
            align (0.5,0.5)

screen noname():
    frame:
        xysize (800,352)
        align (0.7,0.5)
        text "请输入人物姓名。":
            size 40
            align (0.5,0.2)
        textbutton "返回" action Show("makenewplayer"),Hide("noname"):
            align (0.5,0.5)


screen text_input_screen():
    modal True
    frame:

        xysize (300,300)
        align (0.8,0.5)
        has vbox align (0.0,0.0) spacing 30

        hbox:
            text "{size=40}{font=问藏书房.ttf}姓氏：{/font}"
            button:
                id "input_1"
                action NullAction()
                add Input(size=40, color="#000", default=myname1, exclude='{"龙","东方","轩辕","君"}', changed=myname1_func, length=4,copypaste=True,button=renpy.get_widget("text_input_screen","input_1")) yalign 2.0
        hbox:
            text "{size=40}{font=问藏书房.ttf}名字：{/font}"
            button:
                id "input_2"
                action NullAction()
                add Input(size=40, color="#000", default=myname2, changed=myname2_func, length=3,copypaste=True,button=renpy.get_widget("text_input_screen","input_2")) yalign 2.0

        hbox spacing 30:
            textbutton "{size=40}随机" action Function(suijiquming)

            if player == 2:
                textbutton "{size=40}完成" action Hide("text_input_screen")
            else:
                textbutton "{size=40}完成" action Function(czsx),Hide("text_input_screen")

init python:
    def suijiquming():
        global myname1
        global myname2
        myname1 = renpy.random.choice(xing_list)
        myname2 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
        if len(myname2) >= 3:
            myname2 = myname2[0] + myname2[1]
        my.xing = myname1
        my.ming = myname2



    def resetshuxing():
        global sxjd
        choicetags_list = [tags_01,tags_02,tags_03,tags_04,tags_05,tags_06,tags_07,tags_08,tags_09,tags_10,tags_11,tags_12,tags_13]
        choosetags_list = []
        cantchoose_list = []
        czsx()
        tempnum = sxjd *100
        tempnum2 = tempnum/10 + renpy.random.randint(-100,200)
        my.beauty = 400 + tempnum2
        if my.beauty > 800:
            tempnum3  = my.beauty - 800
            my.beauty = 800
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/9 + renpy.random.randint(-100,200)
        my.qizhi = 400 + tempnum2
        if my.qizhi > 800:
            tempnum3  = my.qizhi - 800
            my.qizhi = 800
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/8 + renpy.random.randint(-100,200)
        my.meili = 400 + tempnum2
        if my.meili > 800:
            tempnum3  = my.meili - 800
            my.meili = 800
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/7 + renpy.random.randint(-100,200)
        my.health = 400 + tempnum2
        if my.health > 900:
            tempnum3  = my.health - 900
            my.health = 800
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/6 + renpy.random.randint(-100,200)
        my.xinji = 400 + tempnum2
        if my.xinji > 800:
            tempnum3  = my.xinji - 800
            my.xinji = 800
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        
        tempnum = tempnum *0.1
        
        tempnum2 = tempnum/5 + renpy.random.randint(-10,20)
        my.book = 20 + tempnum2
        if my.book > 90:
            tempnum3  = my.book - 90
            my.book = 90
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/4 + renpy.random.randint(-10,20)
        my.lucky = 30 + tempnum2
        if my.lucky > 80:
            tempnum3  = my.lucky - 80
            my.lucky = 80
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/3 + renpy.random.randint(-10,20)
        my.muzic = 20 + tempnum2
        if my.muzic > 90:
            tempnum3  = my.muzic - 90
            my.muzic = 90
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum/2 + renpy.random.randint(-10,20)
        my.dance = 20 + tempnum2
        if my.dance > 90:
            tempnum3  = my.dance - 90
            my.dance = 90
        else:
            tempnum3 = 0
        tempnum -= tempnum2
        tempnum  += tempnum3
        
        tempnum2 = tempnum
        my.cixiu = 20 + tempnum2
        
        shuxingmiaoshu(my)
        if myname1 == "易" and myname2 == "珊绫":
            sxjd = 130
            money = 1300
        else:
            sxjd = 0
        my.xing = myname1
        my.ming = myname2
        shuxingmiaoshu(my)

    def czsx():
        global sxjd
        global choicetags_list
        global choosetags_list
        global cantchoose_list
        choicetags_list = [tags_01,tags_02,tags_03,tags_04,tags_05,tags_06,tags_07,tags_08,tags_09,tags_10,tags_11,tags_12,tags_13]
        choosetags_list = []
        cantchoose_list = []
        if player == 0:
            sxjd = 20 + renpy.random.randint(0, 3)
        elif player == 1:
            sxjd = 15 + renpy.random.randint(0, 3)
        else:
            pass
        
        if my.familylocation == "义女":
            sxjd += 2
        elif my.familylocation == "庶女":
            sxjd += 1
        else:
            pass
        if my.familylevel == 1:
            sxjd -= 3
        elif my.familylevel == 2:
            sxjd -= 2
        elif my.familylevel == 3:
            sxjd -= 1
        elif my.familylevel == 4:
            pass
        elif my.familylevel == 5:
            pass
        elif my.familylevel == 6:
            pass
        elif my.familylevel == 7:
            pass
        elif my.familylevel == 8:
            sxjd += 1
        elif my.familylevel == 9:
            sxjd += 2
        elif my.familylevel == 10:
            sxjd += 3
        elif my.familylevel == 11:
            sxjd += 4
        elif my.familylevel == 12:
            sxjd += 4
        else:
            sxjd += 4
        if myname1 == "易" and myname2 == "珊绫":
            sxjd = 130
            money = 1300
        else:
            pass
        my.beauty = 400
        my.qizhi = 400
        my.meili = 400
        my.health = 400
        my.xinji = 400
        my.book = 20
        my.lucky = 30
        my.muzic = 20
        my.dance = 20
        my.cixiu = 20
        my.xing = myname1
        my.ming = myname2
        shuxingmiaoshu(my)


label 重置属性:
    $ choicetags_list = [tags_01,tags_02,tags_03,tags_04,tags_05,tags_06,tags_07,tags_08,tags_09,tags_10,tags_11,tags_12,tags_13]
    $ choosetags_list = []
    $ cantchoose_list = []
    $ czsx()

    $ my.medic = 0
    $ my.battle = 0
    $ my.like = 999
    $ my.love = 0
    $ my.xinji1 = True
    $ shuxingmiaoshu(my)
    $ my.xing = myname1
    $ my.ming = myname2

    return

label newplayer_0:
    scene 创建人物
    $ player = 0
    $ yuanweifen = weifen_Normal
    $ sxjd = 1000
    $ my = factory.instantiation_Feizi()
    $ myname1 = "沈"
    $ myname2 = "容儿"
    $ my.xing = myname1
    $ my.ming = myname2
    $ my.age = 15
    $ my.family = "暂无"
    $ my.state = "寻常"
    $ my.shiqin = 0
    $ my.yali = 0
    $ my.exp = 0
    $ my.lucky = 30
    $ my.love = 0
    $ my.year = 0
    $ my.beauty = 400
    $ my.qizhi = 400
    $ my.meili = 400
    $ my.health = 400
    $ my.xinji = 400
    $ my.book = 20
    $ my.muzic = 20
    $ my.dance = 20
    $ my.cixiu = 20
    $ my.tequan1 = -1
    $ my.tequan2 = -1
    $ my.tags = []

    $ my.face = "RE0"
    jump selectmyfamily
    call screen makenewplayer()


label newplayer_1:
    scene 创建人物
    $ player = 1
    $ yuanweifen = weifen_Normal
    $ sxjd = 700
    $ my = factory.instantiation_Feizi()
    $ myname1 = "应"
    $ myname2 = "福遥"
    $ my.xing = myname1
    $ my.ming = myname2
    $ my.age = 20
    $ my.family = "暂无"
    $ my.state = "寻常"
    $ my.shiqin = 1
    $ my.yali = 0
    $ my.exp = 0
    $ my.lucky = 30
    $ my.love = 0
    $ my.year = 4
    $ my.beauty = 400
    $ my.qizhi = 400
    $ my.meili = 400
    $ my.health = 400
    $ my.xinji = 400
    $ my.book = 20
    $ my.muzic = 20
    $ my.dance = 20
    $ my.cixiu = 20
    $ my.tequan1 = -1
    $ my.tequan2 = -1
    $ my.tags = []

    $ my.face = "FY0"
    jump selectmyfamily
    call screen makenewplayer()


label newplayer_2:
    scene 创建人物
    $ player = 2
    $ yuanweifen = weifen_Normal
    $ my = factory.instantiation_Feizi()
    $ myname1 = "燕"
    $ myname2 = "元照"
    $ my.xing = myname1
    $ my.ming = myname2
    $ my.age = 17
    $ my.family = "北国和亲公主"
    $ my.state = "寻常"
    $ my.shiqin = 0
    $ my.yali = 0
    $ my.exp = 0
    $ my.lucky = 20
    $ my.love = 0
    $ my.year = 0
    $ my.beauty = 800
    $ my.qizhi = 450
    $ my.meili = 920
    $ my.health = 500
    $ my.xinji = 500
    $ my.book = 0
    $ my.muzic = 60
    $ my.dance = 60
    $ my.cixiu = 0
    $ my.tequan1 = -1
    $ my.tequan2 = -1
    $ my.tags = []

    $ my.face = "YF0"
    $ my.familylevel = 0
    $ my.fatherduty = "国王"
    $ my.familylocation = '公主'
    $ my.family = "和亲公主"
    call screen makenewplayer_YF()

label selectmyage:
    if player == 0:
        $ my.age = renpy.random.randint(14, 19)
    elif player == 1:
        $ my.age = renpy.random.randint(17, 22)
    else:
        pass
    call screen makenewplayer()
label selectmyage_YF:
    $ my.age = renpy.random.randint(15, 18)

    call screen makenewplayer_YF()

label selectmyfamily:

    $ year = 0
    $ my.tags = []


    $ Feizifamily(my)
    call 重置属性 from _call_重置属性
    call screen makenewplayer()




label selectmyface:
    python:
        my.face = renpy.random.choice(list_femaleface)

    call screen makenewplayer()

label selectmyface_YF:
    python:
        my.face = renpy.random.choice(list_femaleface)

    call screen makenewplayer_YF()

label changemyface:
    show screen makenewplayer()
    python:
        my.face = renpy.input("立绘编号（输入完成后按回车键，不输入则随机挑选）",length=3,allow={"1","2","3","4","5","6","7","8","9","0"})
        my.face = my.face.strip()

        if not my.face:
            my.face = renpy.random.choice(list_femaleface)
        else:
            my.face = int(my.face)
        if my.face > list_femaleface[-1]:
            my.face = list_femaleface[-1]
        else:
            my.face = int(my.face)
    call screen makenewplayer()

label changemyface_YF:
    show screen makenewplayer_YF()
    python:
        my.face = renpy.input("立绘编号（输入完成后按回车键，不输入则随机挑选）",length=3,allow={"1","2","3","4","5","6","7","8","9","0"})
        my.face = my.face.strip()

        if not my.face:
            my.face = renpy.random.choice(list_femaleface)
        else:
            my.face = int(my.face)
        if my.face > list_femaleface[-1]:
            my.face = list_femaleface[-1]
        else:
            my.face = int(my.face)
    call screen makenewplayer_YF()

label changefacenum:
    "不知道怎么用就不要乱改，如果改的太少，选秀或者有宫女变成妃子会报错，需要召见宫女-重置立绘库，并且可能会出现立绘相同的妃子。"
    show screen makenewplayer()
    python:
        tempnum = renpy.input("妃子立绘库数量（输入完成后按回车键，不输入则为默认）",length=9,allow={"1","2","3","4","5","6","7","8","9","0"})
        tempnum = tempnum.strip()



        if not tempnum:
            tempnum = 426
        else:
            tempnum = int(tempnum)
            tempnum = tempnum+1
        list_femaleface = list(range(1,tempnum))
        pre_femaleface = list(range(1,tempnum))
    call screen makenewplayer()


label changefacenum_YF:
    "不知道怎么用就不要乱改，如果改的太少，选秀或者有宫女变成妃子会报错，需要召见宫女-重置立绘库，并且可能会出现立绘相同的妃子。"
    show screen makenewplayer_YF()
    python:
        tempnum = renpy.input("妃子立绘库数量（输入完成后按回车键，不输入则为默认）",length=9,allow={"1","2","3","4","5","6","7","8","9","0"})
        tempnum = tempnum.strip()



        if not tempnum:
            tempnum = 426
        else:
            tempnum = int(tempnum)
            tempnum = tempnum+1
        list_femaleface = list(range(1,tempnum))
        pre_femaleface = list(range(1,tempnum))
    call screen makenewplayer_YF()



label makenewplayer2:
    python:
        if my.health == 900:
            pass
        elif my.health % 100 == 0:
            my.health += renpy.random.randint(0,100)
        else:
            pass


        templist = [my.beauty,my.qizhi,my.meili,my.xinji]
        for i in templist:
            if i == 800:
                pass
            elif i % 100 == 0:
                i+= renpy.random.randint(0,100)
            else:
                pass
        templist = [my.dance,my.muzic,my.book,my.cixiu,my.lucky]
        for i in templist:
            if i == 90:
                pass
            elif i % 10 == 0:
                i+= renpy.random.randint(0,100)
            else:
                pass
        myname1 = myname1.strip()
        myname2 = myname2.strip()
        my.xing = myname1
        my.ming = myname2

    if not myname1:
        if player == 0:
            $ myname1 = "沈"
            $ myname2 = "容儿"

        elif player == 1:
            $ myname1 = "应"
            $ myname2 = "福遥"
        elif player == 2:
            $ myname1 = "燕"
            $ myname2 = "元照"
        else:
            pass
        $ my.xing = myname1
        $ my.ming = myname2
        call screen noname()
    elif not myname2:
        if player == 0:
            $ myname1 = "沈"
            $ myname2 = "容儿"
        elif player == 1:
            $ myname1 = "应"
            $ myname2 = "福遥"
        elif player == 2:
            $ myname1 = "燕"
            $ myname2 = "元照"
        else:
            pass
        $ my.xing = myname1
        $ my.ming = myname2
        call screen noname()

    elif my.family == "暂无":

        call screen nofamily()
    else:
        if player == 2:
            jump newplayerfinish_YF
        else:
            jump newplayerfinish



label newplayerfinish:
    hide screen makenewplayer
    if my.face in list_femaleface:
        $ list_femaleface.remove(my.face)
    $ my.makelucky = renpy.random.randint(900,1400) + my.familylevel*renpy.random.randint(70,85)

    if my.fatherduty == '武将':
        $ my.health = my.health + renpy.random.randint(20, 50)
    elif my.fatherduty == '文官':
        $ my.qizhi = my.qizhi + renpy.random.randint(20, 50)
    elif my.fatherduty == "内侍":
        $ my.meili = my.meili + renpy.random.randint(20, 50)
    else:
        $ my.beauty = my.beauty + renpy.random.randint(20, 50)
    python:
        for i in choosetags_list :
            my.tags.append(i.tags)


    $ mytagslist = [tags_limit_health,tags_limit_lucky,tags_limit_xinji,tags_shuxing,tags_caiyi,tags_xihao]
    if tags_limit_lucky[1] in my.tags:
        $ mytagslist.remove(tags_limit_lucky)
    else:
        pass
    if tags_limit_xinji[2] in my.tags or tags_limit_xinji[3] in my.tags  or tags_limit_xinji[4] in my.tags:
        $ mytagslist.remove(tags_limit_xinji)
    else:
        pass
    if my.health >= 600:
        $ mytagslist.remove(tags_limit_health)
    else:
        pass



    $ lucky = renpy.random.randint(0, 1)
    if lucky == 0:
        pass
    else:
        $ temptaglist = renpy.random.choice(mytagslist)
        $ temptag = renpy.random.choice(temptaglist)
        $ my.tags.append(temptag)
        $ mytagslist.remove(temptaglist)
    $ lucky = renpy.random.randint(0, 1)
    if lucky == 0 or len(my.tags) >= 5:
        pass
    else:
        $ temptaglist = renpy.random.choice(mytagslist)
        $ temptag = renpy.random.choice(temptaglist)
        $ my.tags.append(temptag)
        $ mytagslist.remove(temptaglist)
    $ lucky = renpy.random.randint(0, 1)
    if lucky == 0 or len(my.tags) >= 5:
        pass
    else:
        $ temptaglist = renpy.random.choice(mytagslist)
        $ temptag = renpy.random.choice(temptaglist)
        $ my.tags.append(temptag)
        $ mytagslist.remove(temptaglist)

    $ my.name =  myname1 + myname2
    $ my.xing = myname1
    $ my.ming = myname2
    if my.ming in teshuming:
        $ ming_list.remove(my.ming)

    if len(my.ming) > 1:
        $ aicheng = myname2
    else:
        $ aicheng = myname2 + "儿"

    $ my.taihoulike = (my.beauty +my.meili)/500 + my.qizhi/300 - my.familylevel/4
    $ my.kids = []


    $ my.like = 999
    if player == 0:
        $ my.love = (my.beauty +my.meili+my.qizhi)/250 + my.familylevel/4
        $ my.year = 0
    elif player == 1:
        $ my.love = 0
        $ my.year = 3
    else:
        pass
    $ my.battle = 0
    $ my.medic = 0
    $ my.xingge = "——"
    $ my.xingge1 = True
    $ my.xinji1 = True
    $ my.Gongnv = []
    $ my.qingxiang = 50
    $ my.huaiyun = 0
    $ my.jinzu = 0
    $ my.friends = []
    $ my.foes = []
    $ tags_buff(my)

    if my.face == "FY0":
        $ cloth = "蓝色"
        $ HZ("福遥","蓝色")
    elif my.face == "RE0":
        $ cloth = "默认"
        $ HZ("容儿","默认")
    else:
        $ my_face = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Normal = "Feizi/F" +str(my.face) + ".webp"
        $ my_face_Smile = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Think = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Cry = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Amaze = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Angry = "Feizi/F" +str(my.face)+ ".webp"

    jump 生成皇帝






label newplayerfinish_YF:
    hide screen makenewplayer_YF
    $ my.tags.append(tags_family[0])
    $ my.tags.append(tags_limit_beauty[1])
    $ my.tags.append(tags_limit_meili[2])
    $ my.tags.append(tags_shuxing[2])

    $ my.name =  myname1 + myname2
    $ my.xing = myname1
    $ my.ming = myname2
    if my.ming in teshuming:
        $ ming_list.remove(my.ming)
    if len(my.ming) > 1:
        $ aicheng = myname2
    else:
        $ aicheng = myname2 + "儿"
    $ my.taihoulike = 0
    $ my.kids = []

    $ my.like = 999
    $ my.love = 20
    $ my.year = 0

    $ my.battle = 0
    $ my.medic = 50
    $ my.xingge = "——"
    $ my.xingge1 = True
    $ my.xinji1 = True
    $ my.Gongnv = []
    $ my.qingxiang = 50
    $ my.huaiyun = 0
    $ my.jinzu = 0
    $ my.friends = []
    $ my.foes = []
    if my.face == "YF0":
        $ cloth = "初始"
        $ HZ("妖妃","初始")
    else:
        $ my_face = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Normal = "Feizi/F" +str(my.face) + ".webp"
        $ my_face_Smile = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Think = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Cry = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Amaze = "Feizi/F" +str(my.face)+ ".webp"
        $ my_face_Angry = "Feizi/F" +str(my.face)+ ".webp"


    jump 生成皇帝


label 生成皇帝:

    hide myface
    旁白 "{size=35}是否要自定皇帝以太后人设？{/size}"
    nvl clear
    menu:
        "自定":
            jump 自定皇帝
        "随机":

            jump 随机皇帝

label 随机皇帝:
    python:
        guoxing = renpy.random.choice(["轩辕", "东方","君","龙"])
        emperor = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
        hdage = renpy.random.randint(20,28)
        hdxingge = renpy.random.choice(["冷漠", "腹黑","温柔","风流","刚正"])

        if hdxingge == "冷漠":
            hdface = renpy.random.randint(1,4)
        elif hdxingge == "腹黑":
            hdface = renpy.random.randint(11,14)
        elif hdxingge == "温柔":
            hdface = renpy.random.randint(21,24)
        elif hdxingge == "风流":
            hdface = renpy.random.randint(31,33)
        else:
            hdface = renpy.random.randint(41,43)

        taihouxing = renpy.random.choice(xing_list)
        taihouming = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
        if len(taihouming) >= 3:
            taihouming = taihouming[0] + taihouming[1]
        if taihouming in teshuming:
            ming_list.remove(taihouming)
        taihou = taihouxing + taihouming
        taihouage = renpy.random.randint(40,58)
        taihouxinge = renpy.random.choice(["避世", "宽和","精敏","擅权"])
        taihouface = renpy.random.randint(1,11)

    image 皇帝 = "Male/HD[hdface].webp"
    image 太后 = "Royal/TH[taihouface].webp"
    jump 设定妃阶

label 自定皇帝:



    旁白 "{size=40}请选择国姓——{/size}"
    nvl clear

    $ hdface1 = ""
    $ hdage = renpy.random.randint(20,28)

    nvl clear

    menu:
        "轩辕":
            $ guoxing ="轩辕"
        "东方":

            $ guoxing ="东方"
        "君":

            $ guoxing ="君"
        "龙":

            $ guoxing ="龙"
        "随机":

            $ guoxing = renpy.random.choice(["轩辕", "东方","君","龙"])
        "手动输入":

            $ guoxing = renpy.input("请输入国姓（输入完成后按回车键，不输入则从全部姓氏库中随机）",length=4)
            $ guoxing = guoxing.strip()
            if guoxing == my.xing:
                "国姓不可与玩家姓氏雷同！"
                jump 自定皇帝
            if not guoxing:
                if my.xing in xing_list:
                    $ xing_list.remove(my.xing)
                    $ guoxing = renpy.random.choice(xing_list)
                    $ xing_list.append(my.xing)
                else:
                    $ guoxing = renpy.random.choice(xing_list)

            if guoxing in xing_list:
                $ xing_list.remove(guoxing)







    python:
        emperor = renpy.input("请输入皇帝的名字（输入完成后按回车键，不输入则随机取名）",length=2)
        emperor = emperor.strip()

        if not emperor:
            emperor = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)


    旁白 "{size=40}请选择皇帝的性格{/size}"
    nvl clear

    menu:
        "冷漠":

            $ hdxingge = "冷漠"
            $ temp =""
        "腹黑":
            $ hdxingge = "腹黑"
            $ temp ="1"
        "温柔":

            $ hdxingge = "温柔"
            $ temp ="2"
        "风流":
            $ hdxingge = "风流"
            $ temp ="3"
        "刚正":
            $ hdxingge = "刚正"
            $ temp ="4"
        "随机":
            $ hdxingge = renpy.random.choice(["冷漠", "腹黑","温柔","风流","刚正"])

    if hdxingge == "冷漠":
        $ temp =""
        $ hdface1 = 1
    elif hdxingge == "腹黑":
        $ temp ="1"
        $ hdface1 = 1
    elif hdxingge == "温柔":
        $ temp ="2"
        $ hdface1 = 1
    elif hdxingge == "风流":
        $ temp ="3"
        $ hdface1 = 1
    else:
        $ temp ="4"
        $ hdface1 = 1

    call screen huangdilihui


screen huangdilihui:
    frame:
        background None
        xalign 0.5 yalign 0.5

        has vbox
        if hdface1 == 4:
            textbutton "{size=40}换":
                xalign 0.5
                action SetVariable("hdface1", 1),Show("huangdilihui")
        else:
            textbutton "{size=40}换":
                xalign 0.5
                action SetVariable("hdface1", hdface1+1),Show("huangdilihui")
        add "Male/HD[temp][hdface1].webp" yalign 0.5 xalign 0.5
        textbutton "{size=40}选":
            xalign 0.5
            action SetVariable("hdface1", hdface1),Jump("生成太后")








label 生成太后:
    $ hdface = str(temp) + str(hdface1)
    image hdface = "Male/HD[hdface].webp"
    旁白 "{size=40}请选择太后性格——{/size}"
    nvl clear
    menu:
        "避世":
            $ taihouxinge = "避世"
        "宽和":
            $ taihouxinge = "宽和"
        "精敏":
            $ taihouxinge ="精敏"
        "擅权":
            $ taihouxinge = "擅权"
        "随机":
            $ taihouxinge = renpy.random.choice(["避世", "宽和","精敏","擅权"])
    python:
        taihouxing = renpy.random.choice(xing_list)
        taihouming = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)

        if len(taihouming) >= 3:
            taihouming = taihouming[0] + taihouming[1]
        if taihouming in teshuming:
            ming_list.remove(taihouming)
        taihou = taihouxing + taihouming
        taihouage = renpy.random.randint(40,58)
        taihouface = renpy.random.randint(1,11)

    image thface = "Royal/TH[taihouface].webp"
    jump 设定妃阶

label 设定妃阶:
    旁白 "是否要自定义妃嫔等级？\n（每次开局妃嫔等级都会恢复默认，需要重新设定。）"
    nvl clear
    if renpy.loadable("weifen.txt"):
        $ yusheweifen = True
    else:

        $ yusheweifen =False

    menu:
        "自定":
            $ yusheweifen =False
            nvl clear
            旁白 "{size=30}作者小提示：\n{size=20}更改位份名称为三妃，即为淑妃、德妃、贤妃。\n更改位份名称为四妃，即为贵妃、淑妃、德妃、贤妃。\n更改位份名称为九嫔，即为三昭、三修、三充。\n三妃、四妃和九嫔自动改变人数上限。\n皇宫内暂只有6座宫殿，可供正二品及以上妃嫔位居主位。\n当主殿不够的时候，游戏会出错。\n所以请勿将九嫔放置在正二品以上品级。"
            nvl clear
            call screen Changeweifen
        "默认":
            $ yusheweifen =False
            $ beifei = len(weifen_Normal)-1
            jump 设定完成

        "预设" if yusheweifen == True:
            python:
                import os
                weifenfile=(renpy.file('weifen.txt'))

                weifen_Normal = []
                tempweifen = []
                tempweifenzu = []
                for line in weifenfile:
                    templine=line.strip().split(" ")
                    if templine == ["-------------------------"]:
                        pass
                    else:
                        if len(tempweifen) != 1 :
                            if templine[0] == "-------------------------":
                                pass
                            else:
                                
                                tempweifen.append(templine[0])
                        else:
                            for i in templine:
                                if i == "":
                                    pass
                                else:
                                    tempweifenzu.append(i)
                            if len(tempweifenzu) == 1:
                                tempweifen.append(tempweifenzu[0])
                            else:
                                tempweifen.append(tempweifenzu)
                        if len(tempweifen) == 7:
                            weifen_Normal.append(tempweifen)
                            tempweifen = []
                            tempweifenzu = []
                        else:
                            pass

                weifenfile.close()
                weifen_Normal = list(filter(None, weifen_Normal))
                for i in weifen_Normal:
                    i[0] = int(i[0])
                    i[2] = int(i[2])
                    i[3] = int(i[3])
                    i[4] = int(i[4])
                    i[5] = int(i[5])
                    i[6] = int(i[6])

                beifei = len(weifen_Normal)-1
                weifen_list = []
                for i in weifen_Normal:
                    weifen_list.append(i)

                temptext = ""
                for i in weifen_Normal:
                    temptext = temptext + "\n"
                    if isinstance(i[1],list):
                        for j in i[1]:
                            temptext = temptext + str(j) + "  "
                    else:
                        temptext = temptext + str(i[1]) + "  "
            "[temptext]"


















            jump startgo



label 设定完成:

    if not feipin0:
        $ feipin0 = weifen_Normal[0][1]
    else:
        pass
    if not feipin1:
        $ feipin1 = weifen_Normal[1][1]
    else:
        pass
    if not feipin2:
        $ feipin2 = weifen_Normal[2][1]
    else:
        pass
    if not feipin3:
        $ feipin3 = weifen_Normal[3][1]
    else:
        pass
    if not feipin4:
        $ feipin4 = weifen_Normal[4][1]
    else:
        pass
    if not feipin5:
        $ feipin5 = weifen_Normal[5][1]
    else:
        pass
    if not feipin6:
        $ feipin6 = weifen_Normal[6][1]
    else:
        pass
    if not feipin7:
        $ feipin7 = weifen_Normal[7][1]
    else:
        pass
    if not feipin8:
        $ feipin8 = weifen_Normal[8][1]
    else:
        pass
    if not feipin9:
        $ feipin9 = weifen_Normal[9][1]
    else:
        pass
    if not feipin10:
        $ feipin10 = weifen_Normal[10][1]
    else:
        pass
    if not feipin11:
        $ feipin11 = weifen_Normal[11][1]
    else:
        pass
    if not feipin12:
        $ feipin12 = weifen_Normal[12][1]
    else:
        pass
    if not feipin13:
        $ feipin13 = weifen_Normal[13][1]
    else:
        pass
    if not feipin14:
        $ feipin14 = weifen_Normal[14][1]
    else:
        pass
    if not feipin15:
        $ feipin15 = weifen_Normal[15][1]
    else:
        pass
    if not feipin16:
        $ feipin16 = weifen_Normal[16][1]
    else:
        pass
    $ weifen_list.extend(weifen_Normal)
    $ beifei = len(weifen_Normal)-1

    $ weifen_list[0][1] = feipin0
    $ weifen_list[1][1] = feipin1
    $ weifen_list[2][1] = feipin2
    $ weifen_list[3][1] = feipin3
    $ weifen_list[4][1] = feipin4
    $ weifen_list[5][1] = feipin5
    $ weifen_list[6][1] = feipin6
    $ weifen_list[7][1] = feipin7
    $ weifen_list[8][1] = feipin8
    $ weifen_list[9][1] = feipin9
    $ weifen_list[10][1] = feipin10
    $ weifen_list[11][1] = feipin11
    $ weifen_list[12][1] = feipin12
    $ weifen_list[13][1] = feipin13
    $ weifen_list[14][1] = feipin14
    $ weifen_list[15][1] = feipin15
    $ weifen_list[16][1] = feipin16
    $ weifen_list[0][2] = int(feipinshu0)
    $ weifen_list[1][2] = int(feipinshu1)
    $ weifen_list[2][2] = int(feipinshu2)
    $ weifen_list[3][2] = int(feipinshu3)
    $ weifen_list[4][2] = int(feipinshu4)
    $ weifen_list[5][2] = int(feipinshu5)
    $ weifen_list[6][2] = int(feipinshu6)
    $ weifen_list[7][2] = int(feipinshu7)
    $ weifen_list[8][2] = int(feipinshu8)
    $ weifen_list[9][2] = int(feipinshu9)
    $ weifen_list[10][2] = int(feipinshu10)
    $ weifen_list[11][2] = int(feipinshu11)
    $ weifen_list[12][2] = int(feipinshu12)
    $ weifen_list[13][2] = int(feipinshu13)
    $ weifen_list[14][2] = int(feipinshu14)
    $ weifen_list[15][2] = int(feipinshu15)
    $ weifen_list[16][2] = 9999
    $ a = 0
    python:
        while a < 17:
            if weifen_list[a][1] == "三妃":
                weifen_list[a][1] = ["淑妃","德妃","贤妃"]
                weifen_list[a][2] = 3
            elif weifen_list[a][1] == "四妃":
                weifen_list[a][1] = ["贵妃","淑妃","德妃","贤妃"]
                weifen_list[a][2] = 4
            elif weifen_list[a][1] == "九嫔":
                weifen_list[a][1] = ["昭仪","昭容","昭媛","修仪","修媛","修容","充仪","充媛","充容"]
                weifen_list[a][2] = 9
            else:
                pass
            a = a + 1




    jump startgo





label hajime:
    python:
        my.yuanmao = my.beauty



        Creat_Males(whose = my,how = 0)

        if my.name == "武瞾":
            guoxing = "嬴"
            emperor ="政"

        huangdi ={"国力":0,"政务":0,"军事":0,"暴戾":0,"昏庸":0,}
        huangdi["国力"] = 50
        huangdi["军事"] =50
        huangdi["政务"] = 50
        hd_happy = 50
        hd_health = 80


        if hdxingge == "刚正":
            huangdi["政务"] +=  renpy.random.randint(0,20)
            huangdi["暴戾"] = 20
            huangdi["昏庸"] = 0
        elif hdxingge == "温柔":
            huangdi["军事"] -= renpy.random.randint(0,20)
            huangdi["暴戾"] = 0
            huangdi["昏庸"] = 20
        elif hdxingge == "腹黑":
            huangdi["军事"] += renpy.random.randint(0,10)
            huangdi["政务"] += renpy.random.randint(0,10)
            huangdi["暴戾"] = 50
            huangdi["昏庸"] = 0
        elif hdxingge == "冷漠":
            huangdi["军事"] += renpy.random.randint(0,20)
            huangdi["政务"] -= renpy.random.randint(0,10)
            huangdi["暴戾"] = 70
            huangdi["昏庸"] = 30
        else:
            huangdi["军事"] -= renpy.random.randint(0,10)
            huangdi["政务"] -= renpy.random.randint(0,10)
            huangdi["暴戾"] = 0
            huangdi["昏庸"] = 50


        huangdi["政务"] = renpy.random.randint(40,80)
        huangdi["政务"] = renpy.random.randint(40,80)

        jinshu = False
        AP = 0
        datenum = 3
        timenum = 4
        kaixiao = 0
        zhengfeng = False
        pincha = False
        if player == 0:
            xuanxiutime = 0 
        elif player == 1:
            xuanxiutime = 3
        elif player == 2:
            xuanxiutime = -6
        else:
            xuanxiutime = 0
        cixiujindu = 0
        kufang = []
        NPC_newfz_list =[]
        NPC_fz_dielist = []
        NPC_fz_feilist = []
        NPC_Kids_list = []
        bihuaiyun = []
        xingzi = 50 
        taidu = 50 
        liangxin = 50 

        time_1 = False
        time_2 = False
        time_3 = False
        time_4 = False
        time_5 = False

        gdsj = [] 
        zysj = [] 
        zysj_ready = []
        zysj_end = []
        xdsj = [] 
        xdsj_ready = []
        xdsj_end = []

        shiqinfzlist = []
        weishiqinfzlist = []
        biaoyan = []
        shifoubiaoyan = 0
        huilu = 0
        gongxi = [] 
        xiluo = [] 
        ganxie = [] 
        lenggong = [] 
        lgchuruxuke = False 
        mustshiqin = 0
        pinganmai = 0
        taihoumeet = 0 
        shiqinfz = my
        sidi = None



        ftlcishu =0
        guanxiantai = False
        zhangsi = False
        bujifz = []
        lvxian = False
        lvsicishu = 0


        ygg_like = 0
        ygg = False




        YTGongnv = []
        makeYTGongnv(10,"宫女")
        GN_JJ = False

        yetinghao = ""
        yeting = False


        hd_love_1 = False


        taihou1 = False
        taihou2 =False
        taihou3 = False
        taihou_zczz = False

        fenghoudadian = False


        tyycishu = 0
        xueyi = False
        wenyao = False


        rongyulike = 0
        rongyu = False
        rongyu0 = False 
        rongyu1 = False 
        rongyu2 = False 

        rongyu3 = False 
        rongyu5 = 0 
        rongyu4 = False 
        rongyu6 = False 
        rongyu7 = False 
        rongyu8 = False 
        rongyu9 = False 



        beizhangze20 = False
        beizhangzetime = 0
        zhangzefz = []
        feizibeizhangze = False
        beizhangzefz = []



        manxingdu = []


        usepoison02 = 0 
        suicide = 0 


        chun = Gongnv_sx(name="小春",face="小春",age=14,beauty=300,xingge="单纯",skill=["善于交际"],yexin =0,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
        xia = Gongnv_sx(name="阿夏",face="阿夏",age=16,beauty=700,xingge="机灵",skill=["花言巧语"],yexin =600,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
        qiu = Gongnv_sx(name="秋子",face="秋子",age=18,beauty=500,xingge="聪颖",skill=["见机行事"],yexin =300,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
        dong = Gongnv_sx(name="冬儿",face="冬儿",age=20,beauty=150,xingge="稳重",skill=["心思细腻"],yexin =150,master=None,level="贴身侍女",yexinlv="",beautylv="",like=50,lv=4,state="寻常",shou=60)
        laoji = Gongnv_sx(name="老鸡",face="老鸡",age=61,beauty=920,xingge="聪颖",skill=["鸡卵多毈","刺探情报"],yexin =0,master=None,level="散役",yexinlv="",beautylv="",like=0,lv=5,state="寻常",shou=999)
        yxxiao = Gongnv_sx(name="潇潇",face="潇潇",age=15,beauty=500,xingge="机灵",skill=["横行宫闱","恩承建章"],yexin =300,master=None,level="散役",yexinlv="",beautylv="",like=0,lv=5,state="寻常",shou=999)


        teshugn = []
        chushign = [chun,xia,qiu,dong]


        daixuan_erxi = []
        daixuan_nvxu = []
        taizi = None
        taizi_shili = 0




        atan = factory.instantiation_Feizi()
        atan_0 = False
        atan_1 = 0
        atan_2 = False
        atan_3 = False
        atan_4 = False
        atan_5 = False
        atan_time = 0
        atan_end_1 = 0
        atan_end_2 = 0
        atan_help = []
        atan_help_th = False
        atan_help_hd = False

        chuhuan = factory.instantiation_Feizi()
        chuhuan_time = 0
        chuhuan_0 = False
        chuhuan_1 = False
        chuhuan_2 = False
        chuhuan_3 = False
        chuhuan_come = False
        chuhuan_th = False
        chuhuan_4 = False
        chuhuan_5 = 0
        chuhuan_die = my

        taoning = factory.instantiation_Feizi()
        taoning_0 = False
        taoning_xuanxiu = False
        taoning_fatherup = -1
        taoning_1 = False
        taoning_2 = False
        taoning_3 = False
        taoning_4 = False
        taoning_5 = False




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
 
