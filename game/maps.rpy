init python:
    def ClearScreens():
        renpy.scene(layer='screens')
        renpy.scene(layer='transient')
        renpy.scene(layer='master')
        renpy.scene(layer='overlay')



screen Bigmap:

    if map1 == "冬":
        add "Snow" align (0.5,0.5)
    else:
        pass

    add "gui/按钮底图2.webp" pos (810, 320)
    textbutton "{size=30}宣政殿":
        pos (815, 375)
        text_style "maps_button"
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        action Jump("宣政殿")

    add "gui/按钮底图2.webp" pos (888, 90)
    if timenum >=5:
        textbutton "{size=30}圣宸宫":
            pos (890, 145)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("圣宸宫_late")
    else:
        textbutton "{size=30}圣宸宫":
            pos (890, 145)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("圣宸宫")

    add "gui/按钮底图2.webp" pos (1170, 50)
    if timenum >= 5:
        textbutton "{size=30}建章宫":
            pos (1172, 105)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("建章宫_late")
    elif taihoumeet == 0:
        textbutton "{size=30}建章宫":
            pos (1172, 105)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("建章宫_first")
    elif atan_time < 11 and atan_end_1 == 1 and 2 not in atan_help and atan_help_th == False:
        textbutton "{size=30}建章宫":
            pos (1172, 105)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("建章宫_阿檀")
    elif chuhuan in NPC_fz_list and chuhuan_th == False and chuhuan.year == 0:
        textbutton "{size=30}建章宫":
            pos (1172, 105)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("建章宫_楚欢")
    else:
        textbutton "{size=30}建章宫":
            pos (1172, 105)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("建章宫_"+taihouxinge)


    add "gui/按钮底图2.webp" pos (750, 10)
    if weifen_list[0][5] == 0:
        textbutton "{size=30}凤仪宫":
            pos (752, 65)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("没有皇后")
    else:
        textbutton "{size=30}凤仪宫":
            pos (752, 65)
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            text_style "maps_button"
            action Call("拜访妃子",fz = NPC_fz_list[0])

    add "gui/按钮底图2.webp" pos (1530, 570)
    textbutton "{size=30}重华宫":
        pos (1532, 625)
        text_style "maps_button"
        action Jump("重华宫")

    add "gui/按钮底图2.webp" pos (1040, 20) zoom 1.5
    textbutton "{size=40}后 宫":
        pos (1050, 100)
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        text_style "maps_button"
        action SetVariable("mapname","后宫"),Show("palaces"),Hide("Bigmap")

    add "gui/按钮底图2.webp" pos (370, 235) zoom 1.1
    textbutton "{size=35}掖 庭":
        pos (373, 300)
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        text_style "maps_button"
        action Jump("掖廷")

    add "gui/按钮底图2.webp" pos (100, 335)
    textbutton "{size=30}太乐坊":
        pos (102, 380)
        text_style "maps_button"
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        action Jump("太乐坊")

    add "gui/按钮底图2.webp" pos (150, 475)
    if tyycishu < 3:
        textbutton "{size=30}太医院":
            pos (152, 520)
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            text_style "maps_button"
            action Jump("太医院_before3")
    else:
        textbutton "{size=30}太医院":
            pos (152, 520)
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            text_style "maps_button"
            action Jump("太医院")









    add "gui/按钮底图2.webp" pos (450, 35) zoom 1.2
    textbutton "{size=38}御花园":
        pos (455, 105)
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        text_style "maps_button"
        action Jump("御花园")

    add "gui/按钮底图2.webp" pos (370, 55) zoom 0.9
    textbutton "{size=26}太液池":
        pos (372, 105)
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        text_style "maps_button"
        action Jump("太液池")

    add "gui/按钮底图2.webp" pos (290, 85)
    textbutton "{size=30}上林苑":
        pos (292, 135)
        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        text_style "maps_button"
        action Jump("上林苑")















    add "gui/按钮底图2.webp" pos (1350, 235) zoom 1.1
    if timenum == 5:
        textbutton "{size=35}奉天楼":
            pos (1352, 285)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("奉天楼_late")
    elif guanxiantai == False and month != 12:
        textbutton "{size=35}奉天楼":
            pos (1352, 285)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("望仙殿")
    else:
        textbutton "{size=35}奉天楼":
            pos (1352, 285)
            text_style "maps_button"
            activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
            action Jump("奉天楼")



    add "gui/按钮底图2.webp" pos (1250, 0) zoom 0.8
    textbutton "{size=27}锦寒宫":
        pos (1249, 37)
        text_style "maps_button"

        activate_sound "Audio/se_maoudamashii_se_switch02.ogg"
        action Jump("锦寒宫")










screen Normalbuttons:
    style_prefix "Normalbuttons"
    vbox xalign 0.0 yalign 0.3:
        imagebutton idle "gui/button/返回寝居_idle.webp" hover "gui/button/返回寝居_hover.webp" action Hide("fz_jm"),Hide("myshuxing"),Hide("fz_sx"),Hide("allstory"),Jump("寝居界面")
        imagebutton idle "gui/button/查看属性_idle.webp" hover "gui/button/查看属性_hover.webp" action ToggleScreen("myshuxing")

        imagebutton idle "gui/button/后宫嫔妃_idle.webp" hover "gui/button/后宫嫔妃_hover.webp" action ToggleScreen("fz_jm", name = "妃嫔列表", list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True))
        imagebutton idle "gui/button/宫廷纪事_idle.webp" hover "gui/button/宫廷纪事_hover.webp" action Show("allstory")

screen Myroombuttons:
    style_prefix "Normalbuttons"
    zorder -1
    vbox xalign 0.0 yalign 0.3:
        if jinzu(my) == True or my.level == beifei or player == -1:
            pass
        else:
            imagebutton idle "gui/button/离开寝居_idle.webp" hover "gui/button/离开寝居_hover.webp" action Hide("myroom"),Hide("myshuxing"),Hide("fz_jm"),Hide("myshuxing"),Jump("皇宫界面")
        imagebutton idle "gui/button/查看属性_idle.webp" hover "gui/button/查看属性_hover.webp" action ToggleScreen("myroom"),ToggleScreen("myshuxing")
        imagebutton idle "gui/button/召见宫女_idle.webp" hover "gui/button/召见宫女_hover.webp" action Hide("myroom"),Hide("fz_jm"),Hide("myshuxing"),Call("召见宫女",mapname = "myroom")
        imagebutton idle "gui/button/后宫嫔妃_idle.webp" hover "gui/button/后宫嫔妃_hover.webp" action ToggleScreen("fz_jm", name = "妃嫔列表", list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)),Hide("fz_sx")
        imagebutton idle "gui/button/宫廷纪事_idle.webp" hover "gui/button/宫廷纪事_hover.webp" action Show("allstory")



screen Palacebuttons:
    style_prefix "Normalbuttons"
    zorder -1
    vbox xalign 0.0 yalign 0.3:
        imagebutton idle "gui/button/离开寝居_idle.webp" hover "gui/button/离开寝居_hover.webp" action Hide("Palacebuttons"),Hide("fz_sx2"),Hide("myshuxing"),Hide("allstory"),Jump("皇宫界面")
        imagebutton idle "gui/button/查看属性_idle.webp" hover "gui/button/查看属性_hover.webp" action ToggleScreen("myshuxing")
        imagebutton idle "gui/button/后宫嫔妃_idle.webp" hover "gui/button/嫔妃信息_hover.webp" action ToggleScreen("fz_sx2", fz = fz)
        imagebutton idle "gui/button/宫廷纪事_idle.webp" hover "gui/button/宫廷纪事_hover.webp" action Show("allstory")

style Normalbuttons_button:
    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_switch02.ogg"

style maps_button:
    vertical True
    font "问藏书房.ttf"
    color "#B22222"
    hover_color "#E6E6FA"
    outlines [ (absolute(1), "#8abad2", absolute(0), absolute(1)) ]








screen palaces:
    style_prefix "choice"
    add "Maps/后宫.webp" xalign 0.0 yalign 0.0
    if month > 1 and month < 5:
        $ map1 = "春"
    elif month > 4 and month < 8:
        $ map1 = "夏"
    elif month > 7 and month < 11:
        $ map1 = "秋"
    else:
        $ map1 = "冬"
    if map1 == "冬":
        add "Snow" align (0.5,0.5)
    else:
        pass
    frame:
        background None
        yalign 0.25 xalign 0.5
        has vbox
        spacing 50
        for i in palaces:
            textbutton "{size=40}{font=问藏书房.ttf}【" + i[0][0] +"{size=20}（" + str(i[0][1]) + "人）{size=40}】" xalign 0.5:

                action ShowTransient("palace", a = i),Hide("palaces")
        textbutton "{size=40}{font=问藏书房.ttf}离开" xalign 0.5:

            action SetVariable("mapname", "皇宫"),Show("Bigmap"),Hide("palaces")


screen palace(a):
    style_prefix "palace"
    add "Maps/后宫.webp" xalign 0.0 yalign 0.0
    frame:
        background None
        yalign 0.2 xalign 0.6
        textbutton "{size=40}{font=问藏书房.ttf}离开":
            yalign 0.9 xalign 0.5
            action Show("palaces"),Hide("palace")
        vbox:
            yalign 0.15 xalign 0.5
            if a[1][1] != "":
                textbutton "{color=#B22222}{size=35}{font=问藏书房.ttf} " + a[1][0] +" {size=25}{font=问藏书房.ttf}"+a[1][1].hao+a[1][1].weifen+" "+a[1][1].name + " ":
                    yalign 0.2 xalign 0.5
                    action Call("拜访妃子",fz = a[1][1] ),Hide("palace")
            else:
                textbutton "{size=40}{font=问藏书房.ttf} " + a[1][0] +  " " yalign 0.5 xalign 0.5

        grid 2 4:
            xspacing 60
            yspacing 30
            yalign 0.45 xalign 0.5
            $ templist = list(range(2,10))
            for i in templist:
                if a[i][1] != "":
                    textbutton "{size=35}{font=问藏书房.ttf} " + a[i][0] +" {size=25}{font=问藏书房.ttf}"+a[i][1].hao+a[i][1].weifen+" "+a[i][1].name + " ":
                        align (0.5,0.5)
                        action Call("拜访妃子",fz = a[i][1] ),Hide("palace")

                else:
                    textbutton "{size=40}{font=问藏书房.ttf} " + a[i][0] +  " ":
                        align (0.5,0.5)


init python:
    lenggong_page=0



screen lenggong():


    $ next_lenggong_page = lenggong_page + 1
    $ prev_lenggong_page = lenggong_page - 1
    $ max_lenggong_page = round(len(NPC_fz_feilist)/6)
    $ b = lenggong_page*6+6

    if b >= len(NPC_fz_feilist):
        $ b = len(NPC_fz_feilist)
    else:
        pass

    frame:
        align (0.5, 0.8)
        xsize 300
        ysize 50
        has hbox
        spacing 0
        yalign 0.45 xalign 0.5
        if lenggong_page > 0:
            textbutton "《《" action SetVariable('lenggong_page', prev_lenggong_page), Show("lenggong")
        else:
            textbutton "《《"
        text "第[next_lenggong_page]页"
        if lenggong_page < max_lenggong_page:
            textbutton "》》" action SetVariable('lenggong_page', next_lenggong_page), Show("lenggong")
        else:
            textbutton "》》"
    frame:
        style_prefix "palace"
        background None
        yalign 0.2 xalign 0.6
        xsize 800
        ysize 780
        grid 2 3:
            align (0.5, 0.5)
            xspacing 60
            yspacing 30
            $ a = 0
            $ next_lenggong_page = lenggong_page + 1
            for i in NPC_fz_feilist[lenggong_page*6:b]:
                if a <= b:
                    textbutton "{size=40}{font=问藏书房.ttf} {size=40}"+i.hao+i.weifen+" "+i.name + " ":
                        align (0.5,0.5)
                        action Call("冷宫妃子",fz = i ),Hide("lenggong")

                    $ a = a + 1
                else:
                    null
            if a < 6:
                for j in range(a, 6):
                    null

        frame:
            background None
            yalign 0.8 xalign 0.5
            textbutton "{size=40}{font=问藏书房.ttf}离开":
                yalign 0.9 xalign 0.5
                action Hide("lenggong"),Jump("皇宫界面")



style palace_button_text is default:
    properties gui.button_text_properties("palace_button")
    min_width 350


style palace_button is button:
    idle_background "gui/button/palace_idle_background.webp"
    insensitive_background "gui/button/palace_idle_background.webp"
    hover_background "gui/button/palace_hover_background.webp"
    properties gui.button_properties("palace_button")
    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"





screen meetNPC(place):
    style_prefix "meetNPC"

    vbox align (0.45,0.25):

        if tempnum == 0:
            pass
        else:
            $ renshu = len(Npcmeet)
            if lucky ==0 and timenum>1:
                $ renshu= renshu + 1
            elif taihouxinge == "擅权" and my.taihoulike > 50 and taihou2 == False and timenum < 5:
                $ renshu= renshu + 1
            elif taihouxinge == "避世" and my.taihoulike > 50 and taihou2 == False and timenum < 5:
                $ renshu= renshu + 1
            else:
                pass
            if (renshu % 2) == 0:
                $ gridnum = renshu/2
            else:
                $ gridnum = (renshu + 1)/2
            grid 4 gridnum:
                xspacing 0
                yspacing 20
                if lucky == 0 and timenum>1:
                    add "Male/HD[hdface].webp" zoom 0.4 xalign 1.0 yalign 1.0
                    textbutton "{size=30}{font=问藏书房.ttf}{color=#F7AB00}皇帝 [guoxing][emperor]" action Call("偶遇皇上",place = place):
                        align (0.0,0.5)
                elif taihouxinge == "擅权" and my.taihoulike > 50 and taihou2 == False and len(Npcmeet)> 0 and timenum < 5:
                    add "Royal/TH[taihouface].webp" zoom 0.4 xalign 1.0 yalign 1.0
                    textbutton "{size=30}{font=问藏书房.ttf}{color=#F7AB00}太后 [taihou]" action Call("擅权太后剧情2",place = place):
                        align (0.0,0.5)
                elif taihouxinge == "避世" and my.taihoulike > 50 and taihou2 == False and timenum < 5:
                    add "Royal/TH[taihouface].webp" zoom 0.4 xalign 1.0 yalign 1.0
                    textbutton "{size=30}{font=问藏书房.ttf}{color=#F7AB00}太后 [taihou]" action Call("避世太后剧情2",place = place):
                        align (0.0,0.5)

                else:
                    pass

                for i in Npcmeet:
                    add "Feizi/F[i.face].webp" zoom 0.4 xalign 1.0 yalign 1.0
                    textbutton "{size=30}{font=问藏书房.ttf}"+i.hao +i.weifen+" " + i.name action Call("偶遇妃子",fz = i,place =place):
                        xalign 0.0 yalign 0.5

                if (renshu % 2) == 0:
                    pass
                elif renshu <2:
                    text ""
                    text ""
                else:
                    text ""
                    text ""
    vbox align (0.5,0.9):
        spacing 25
        textbutton "{size=30}{font=问藏书房.ttf}独自闲逛" action Call("后宫游玩",place =place) align (0.5,0.5)

        textbutton "{size=30}{font=问藏书房.ttf}离   开" action Jump("皇宫界面") align (0.5,0.5)

style meetNPC_button_text:
    min_width 262
    text_align 0.5

style meetNPC_button is button:
    idle_background "gui/namebox2.webp"
    insensitive_background "gui/namebox2.webp"
    hover_background "gui/namebox2.webp"
    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"






screen feipindengji(mapname):
    frame:
        xysize (800,800)
        align (0.5,0.5)
        vbox xalign 0.5:
            text ""
            text "妃阶设定" align (0.5,0.5)
        grid 3 18 align (0.5,0.5) xspacing 100:
            text "品级"
            text "位份"
            text "已有/上限"
            text "中宫"
            text "[feipin0]"
            text "[weifen_list[0][5]]人/[weifen_list[0][2]]人"
            text "正一品"
            text "[feipin1]"
            text "[weifen_list[1][5]]人/[weifen_list[1][2]]人"
            text "从一品"
            text "[feipin2]"
            text "[weifen_list[2][5]]人/[weifen_list[2][2]]人"
            text "正二品"
            text "[feipin3]"
            text "[weifen_list[3][5]]人/[weifen_list[3][2]]人"
            text "从二品"
            text "[feipin4]"
            text "[weifen_list[4][5]]人/[weifen_list[4][2]]人"
            text "正三品"
            text "[feipin5]"
            text "[weifen_list[5][5]]人/[weifen_list[5][2]]人"
            text "从三品"
            text "[feipin6]"
            text "[weifen_list[6][5]]人/[weifen_list[6][2]]人"
            text "正四品"
            text "[feipin7]"
            text "[weifen_list[7][5]]人/[weifen_list[7][2]]人"
            text "从四品"
            text "[feipin8]"
            text "[weifen_list[8][5]]人/[weifen_list[8][2]]人"
            text "正五品"
            text "[feipin9]"
            text "[weifen_list[9][5]]人/[weifen_list[9][2]]人"
            text "从五品"
            text "[feipin10]"
            text "[weifen_list[10][5]]人/[weifen_list[10][2]]人"
            text "正六品"
            text "[feipin11]"
            text "[weifen_list[11][5]]人/[weifen_list[11][2]]人"
            text "从六品"
            text "[feipin12]"
            text "[weifen_list[12][5]]人/[weifen_list[12][2]]人"
            text "正七品"
            text "[feipin13]"
            text "[weifen_list[13][5]]人/[weifen_list[13][2]]人"
            text "从七品"
            text "[feipin14]"
            text "[weifen_list[14][5]]人/[weifen_list[14][2]]人"
            text "正八品"
            text "[feipin15]"
            text "[weifen_list[15][5]]人/[weifen_list[15][2]]人"
            text "从八品"
            text "[feipin16]"
            text "[weifen_list[16][5]]人/[weifen_list[16][2]]人"

        hbox:
            align (0.5,1.0)
            textbutton "完成" action Hide("feipindengji"),Call("召见宫女",mapname = mapname)






screen feipindengji2(mapname):
    frame:
        xysize (800,800)
        align (0.5,0.5)
        vbox xalign 0.5:
            text ""
            text "妃阶设定" align (0.5,0.5)
        $ a = len(weifen_list) + 1
        grid 3 a align (0.2,0.2):
            text "品级"
            text "位份"
            text "已有/上限"
            for i in yuanweifen:
                $ templevel = i[0]
                $ tempnum = weifen_list[templevel][5]
                $ tempnum2 = weifen_list[templevel][2]
                text "[templevel]"
                if isinstance(i[1],tuple):
                    $ tempweifenzu = i[1]
                    $ tempweifen = ""
                    for j in tempweifenzu:
                        $ tempweifen = tempweifen + j
                    text "[tempweifen]"
                else:
                    text "[i[1]]"
                text "[tempnum]人/[tempnum2]人"


        hbox:
            align (0.5,1.0)
            textbutton "完成" action Hide("feipindengji2"),Call("召见宫女",mapname = mapname)









screen mapbeijing:

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

    add "Maps/地图-[map1]-[map2].webp" xalign 0.0 yalign 0.0
    if map1 == "冬":
        add "Snow" align (0.5,0.5)
    else:
        pass



label 召见宫女(mapname):
    if mapname == "bigmap":
        hide screen bigmap
        show screen mapbeijing
    else:
        hide screen myroom
        scene 寝居
    show 我的宫女 at chara
    我的宫女 "主子，您有什么吩咐？"
    menu:
        "*0.5版本常见问题*":
            call screen tips
        "调整开销" if my.level != 17:
            我的宫女 "您打算如何调整呢？"
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
        "妃嫔等级":
            hide 我的宫女
            if yusheweifen ==False:
                call screen feipindengji(mapname = mapname)
            else:
                call screen feipindengji2(mapname = mapname)
        "官员表":
            call screen guanyuanbiao
        "换装" if my.face == "YF1" or my.face == "YF2" or my.face == "YF0":
            我 "要换成什么装扮呢……"
            menu:
                "旧衣" if my.face != "YF0":
                    $ cloth = "初始"
                    $ my.face = "YF0"
                    $ HZ("妖妃","初始")

                "奢华" if my.face != "YF1":
                    $ cloth = "华丽"
                    $ my.face = "YF1"
                    $ HZ("妖妃","华丽")

                "幽雅" if my.face != "YF2":
                    $ cloth = "素雅"
                    $ my.face = "YF2"
                    $ HZ("妖妃","素雅")

        "换装" if my.face == "FY1" or my.face == "FY2" or my.face == "FY0":
            我 "要换成什么装扮呢……"
            menu:
                "清雅" if my.face != "FY0":
                    $ cloth = "蓝色"
                    $ my.face = "FY0"
                    $ HZ("福遥","蓝色")
                "秀美" if my.face != "FY1":
                    $ cloth = "红色"
                    $ my.face = "FY1"
                    $ HZ("福遥","红色")
                "典雅" if my.face != "FY2" and diwei(my) <= 1:
                    $ cloth = "仙鹤"
                    $ my.face = "FY2"
                    $ HZ("福遥","仙鹤")
        "重置妃子图库":











            $ list_femaleface = []
            python:
                for i in pre_femaleface:
                    list_femaleface.append(i)
        "无事":



















            pass
    hide 我的宫女

    if mapname == "bigmap":
        hide screen mapbeijing
        jump 皇宫界面
    else:
        jump 寝居界面
 
