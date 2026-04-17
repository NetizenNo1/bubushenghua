



init -98 python:
    from operator import attrgetter

    class Gameplayer(object):
        def __init__(self,ch,face,code,jieshao,name,age,jiashi,zizhi,teshu,jingli,story,gametip):
            self.code = name
            self.ch = ch
            self.face = face
            self.jieshao = jieshao
            self.story = story
            self.name = name
            self.age = age
            self.jiashi = jiashi
            self.jingli =jingli
            self.zizhi = zizhi
            self.teshu = teshu
            self.gametip = gametip
        def __eq__(self, other):
            return self.__dict__ == other.__dict__




style fzjm_button:
    size 35
    font "问藏书房.ttf"
    color "#B22222"
    hover_color "#E6E6FA"
    outlines [ (absolute(1), "#8abad2", absolute(0), absolute(1))]


screen fz_jm(name, list):
    modal True
    frame:
        xsize 350
        ysize 500
        align (0.05,0.15)
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        hbox align (0.1,0.0):
            textbutton " 后宫 ":
                text_style "fzjm_button"
                action ShowTransient("fz_jm", name = "后宫", list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False))
            textbutton " 冷宫 ":
                text_style "fzjm_button"
                action ShowTransient("fz_jm", name = "冷宫", list = NPC_fz_feilist)
            textbutton " 已逝 ":
                text_style "fzjm_button"
                action ShowTransient("fz_jm", name = "殁逝", list = NPC_fz_dielist)
        viewport:
            xinitial 200
            xsize 500
            ysize 380
            align (1.0,0.6)
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            has vbox
            text " "
            $ colornum = "990000"
            $ colornum2 = "990000"
            for i in list:
                if i.level == beifei:
                    $ colornum = "A1A1A1"
                elif diwei(i) == 0:
                    $ colornum = "FF3030"
                    $ colornum2 = "FF3030"
                elif diwei(i) == 1:
                    $ colornum = "EE00EE"
                    $ colornum2 = "EE00EE"
                elif diwei(i) == 2:
                    $ colornum = "0040FF"
                    $ colornum2 = "0040FF"
                else:
                    $ colornum = "008000"
                    $ colornum2 = "008000"
                if i == my:
                    textbutton "{size=28}{color=#[colornum]}{font=问藏书房.ttf}    [i.hao][i.weifen] {color=#F08080}[i.name]    {/font}{/size}" align (0.0,0.5):
                        action ShowTransient("fz_sx", fz = i)
                else:
                    textbutton "{size=28}{color=#[colornum]}{font=问藏书房.ttf}    [i.hao][i.weifen] {color=#490202}[i.name]    {/font}{/size}" align (0.0,0.5):


                        action ShowTransient("fz_sx", fz = i)
            text ""
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            align (1.0,1.0)
            action Hide("fz_jm"),Hide("fz_sx")





screen fz_sx(fz):
    style_prefix "myroom"
    $ shuxingmiaoshu(fz)
    frame:
        background None
        align (0.9,0.5)


        add "gui/frame.webp" size (1080,600) xalign 0.55 yalign 0.3
        fixed xysize (300,400) xalign 0.25 yalign 0.2:
            if fz.face not in pre_femaleface:
                add "Feizi/F[fz.face].webp" maxsize (400,400) align (0.5,1.0)
            else:
                add "Feizi/F[fz.face].webp" maxsize (250,352) align (0.5,1.0)

        add "namebox.webp" xalign 0.26 yalign 0.55
        textbutton "{color=#FF3030}{size=35}{font=问藏书房.ttf}[fz.hao][fz.weifen]-[fz.name]{/font}{/size}{/color}" xalign 0.26 yalign 0.55
        fixed:
            xmaximum 200 ymaximum 200 xalign 0.26 yalign 0.75
            vbox:
                for i in fz.tags:
                    textbutton "{size=25}{font=问藏书房.ttf}"+i[0]:
                        action NullAction()
                        hovered Show("scrtt",tt=i[1])
                        unhovered [Hide("scrtt")]

        python:
            if fz == my:
                fz.kidsnum = len(my.kids)
                fz.Gongnvnum = len(my.Gongnv)
            else:
                fz.kidsnum = len(fz.kids)
                fz.Gongnvnum = len(fz.Gongnv)
            if fz.xingge1 == False :
                tempxingge = "未知"
            else:
                tempxingge = fz.xingge
            weiwang = int(fz.exp)
            health = int(fz.health)
            beauty = int(fz.beauty)
            qizhi = int(fz.qizhi)
            meili = int(fz.meili)
            like = int(fz.like)
            love = int(fz.love)
            if fz.xinji1 == False:
                xinji = "???"
            else:
                xinji = int(fz.xinji)

            fuyuan = int(fz.lucky)


        viewport:
            python:
                neiying = 0
                for i in fz.Gongnv:
                    if i.state == "内应":
                        neiying = neiying +1
                    else:
                        pass

            xsize 540
            ysize 420
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            align (0.65,0.35)
            vbox:
                spacing 15
                text "{size=30}{font=问藏书房.ttf}等级：[fz.level] 威望:[weiwang]" + "  资历:[fz.year]年{/size}"
                text "{size=30}{font=问藏书房.ttf}年龄:" + str(fz.age)  +" 状态:" + str(fz.state)
                text "{size=30}{font=问藏书房.ttf}家世:" + fz.family
                text "{size=30}{font=问藏书房.ttf}住所:" + fz.palace +fz.qinju
                text "{size=25}{font=问藏书房.ttf}体质:[fz.healthlv]([health])     容貌:[fz.beautylv]([beauty])"
                text "{size=25}{font=问藏书房.ttf}气质:[fz.qizhilv]([qizhi])     魅力:[fz.meililv]([meili])"
                text "{size=25}{font=问藏书房.ttf}好感:[fz.likelv]([like])     圣宠:[fz.lovelv]([love])"
                text "{size=25}{font=问藏书房.ttf}性格:[tempxingge]     心计:[fz.xinjilv]([xinji])"
                if persistent.ycsz == False:
                    text "{size=25}{font=问藏书房.ttf}倾向:"+str(int(fz.qingxiang))+" 福缘:[fuyuan]  压力:[fz.yali]"
                else:
                    pass
                text "{size=25}{font=问藏书房.ttf}侍寝:[fz.shiqin]次"
                textbutton "{size=25}{font=问藏书房.ttf}子嗣:[fz.kidsnum]" action ToggleScreen("feipinhuangsi", name = fz.name, list = fz.kids)
                text "{size=25}{font=问藏书房.ttf}交好:"
                python:
                    textlist = str(fz.hao+fz.weifen+fz.name+"\n家世:"+fz.family+"年龄:"+ str(fz.age) +"（入宫"+str(fz.year)+"年）\n住所:"+fz.palace+fz.qinju)
                    textlist = textlist + "\n体质:"+str(health)+"\n容貌:"+str(beauty)+"\n气质:"+str(qizhi)+"\n魅力:"+str(meili)+"\n"
                    textlist = textlist +"\n好感:"+str(like)+"\n圣宠:"+str(love)+"\n性格:"+str(fz.xingge)+"\n心机:"+str(xinji)+"\n倾向:"+str(int(fz.qingxiang))+"\n福缘:"+str(fuyuan)+"侍寝:"+str(fz.shiqin)+"次\n"
                    textlist = textlist + "交好:\n"
                    a = ""
                    for i in fz.friends:
                        a = a + i.hao+i.weifen+i.name+"  "
                    textlist = textlist + a +"\n"
                text "{size=20}{font=问藏书房.ttf}" + a
                text "{size=25}{font=问藏书房.ttf}交恶:"
                python:
                    textlist = textlist + "交恶:\n"
                    a = ""
                    for i in fz.foes:
                        a = a + i.hao+i.weifen+i.name+"  "
                    textlist = textlist + a+"\n"
                text "{size=20}{font=问藏书房.ttf}" + a

                text "{size=25}{font=问藏书房.ttf}族亲:"
                python:
                    textlist = textlist + "族亲:\n"
                    a = ""
                    for i in fz.sisters:
                        a = a + i.hao+i.weifen+i.name+"  "
                    textlist = textlist + a+"\n"
                text "{size=20}{font=问藏书房.ttf}" + a


                text "{size=25}{font=问藏书房.ttf}经历:"
                python:
                    a = ""
                    for i in fz.story:
                        a = a + i
                    textlist = textlist +  "经历:\n" +a
                text "{size=20}{font=问藏书房.ttf}" + a


                textbutton "{size=20}{font=问藏书房.ttf}复制人物履历" action Function(scrubs, textlist)
        textbutton "关闭":
            align (0.8,0.75)
            action Hide("fz_sx")


        vbox align (0.8,0.5):
            if fz == my:
                pass
            elif fz in NPC_fz_dielist:
                pass
            elif fz in NPC_fz_feilist:
                pass
            else:

                if mapname =="后宫" or jinzu(my) == True or my.level == beifei:
                    pass
                else:
                    textbutton "拜访" action Hide("myroom"),Hide("fz_jm"),Hide("fz_sx"),Hide("Bigmap"),Call("拜访妃子",fz = fz)
                if my.level < fz.level and mapname == "寝居" and jinzu(my) == False and my.level != beifei:
                    textbutton "召见" action Hide("fz_jm"),Hide("fz_sx"),Call("召见邀约",fz = fz)
                elif mapname == "寝居" and jinzu(my) == False and my.level != beifei:
                    textbutton "邀约" action Hide("fz_jm"),Hide("fz_sx"),Call("召见邀约",fz = fz)
                else:
                    pass
                textbutton "技能" action ToggleScreen("fzskills", fz = fz)
                textbutton "宫女" action ToggleScreen("feipinGongnv", gn = i,fz = fz,name = fz.name, list = fz.Gongnv)



screen fz_sx2(fz):
    $ shuxingmiaoshu(fz)
    add "gui/frame.webp" size (1080,600) xalign 0.55 yalign 0.3

    fixed xysize (300,400) xalign 0.25 yalign 0.2:
        if fz.face not in pre_femaleface:
            add "Feizi/F[fz.face].webp" maxsize (400,500) align (0.5,1.0)
        else:
            add "Feizi/F[fz.face].webp" maxsize (250,352) align (0.5,1.0)

    add "namebox.webp" xalign 0.26 yalign 0.55
    textbutton "{color=#FF3030}{size=35}{font=问藏书房.ttf}[fz.hao][fz.weifen]-[fz.name]{/font}{/size}{/color}" xalign 0.26 yalign 0.55
    fixed:
        xmaximum 200 ymaximum 200 xalign 0.26 yalign 0.75
        vbox:
            for i in fz.tags:
                textbutton "{size=25}{font=问藏书房问藏书房.ttf}"+i[0]:
                    action NullAction()
                    hovered Show("scrtt",tt=i[1])
                    unhovered [Hide("scrtt")]

    python:
        if fz == my:
            fz.kidsnum = len(my.kids)
            fz.Gongnvnum = len(my.Gongnv)
        else:
            fz.kidsnum = len(fz.kids)
            fz.Gongnvnum = len(fz.Gongnv)
        if fz.xingge1 == False :
            tempxingge = "未知"
        else:
            tempxingge = fz.xingge
        weiwang = int(fz.exp)
        health = int(fz.health)
        beauty = int(fz.beauty)
        qizhi = int(fz.qizhi)
        meili = int(fz.meili)
        like = int(fz.like)
        love = int(fz.love)
        if fz.xinji1 == False:
            xinji = "???"
        else:
            xinji = int(fz.xinji)

        fuyuan = int(fz.lucky)


    viewport:
        python:
            neiying = 0
            for i in fz.Gongnv:
                if i.state == "内应":
                    neiying = neiying +1
                else:
                    pass

        xsize 540
        ysize 420
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        align (0.65,0.35)
        vbox:
            spacing 15
            text "{size=30}{font=问藏书房.ttf}等级：[fz.level] 威望:[weiwang]" + "  资历:[fz.year]年{/size}"
            text "{size=30}{font=问藏书房.ttf}年龄:" + str(fz.age)  +" 状态:" + str(fz.state)
            text "{size=30}{font=问藏书房.ttf}家世:" + fz.family
            text "{size=30}{font=问藏书房.ttf}住所:" + fz.palace +fz.qinju
            text "{size=25}{font=问藏书房.ttf}体质:[fz.healthlv]([health])     容貌:[fz.beautylv]([beauty])"
            text "{size=25}{font=问藏书房.ttf}气质:[fz.qizhilv]([qizhi])     魅力:[fz.meililv]([meili])"
            text "{size=25}{font=问藏书房.ttf}好感:[fz.likelv]([like])     圣宠:[fz.lovelv]([love])"
            text "{size=25}{font=问藏书房.ttf}性格:[tempxingge]     心计:[fz.xinjilv]([xinji])"
            if persistent.ycsz == False:
                text "{size=25}{font=问藏书房.ttf}倾向:"+str(int(fz.qingxiang))+" 福缘:[fuyuan]  压力:[fz.yali]"
            else:
                pass
            text "{size=25}{font=问藏书房.ttf}侍寝:[fz.shiqin]次"
            textbutton "{size=25}{font=问藏书房.ttf}子嗣:[fz.kidsnum]" action ToggleScreen("feipinhuangsi", name = fz.name, list = fz.kids)
            text "{size=25}{font=问藏书房.ttf}交好:"
            python:
                a = ""
                for i in fz.friends:
                    a = a + i.hao+i.weifen+i.name+"  "
            text "{size=20}{font=问藏书房.ttf}" + a
            text "{size=25}{font=问藏书房.ttf}交恶:"
            python:
                a = ""
                for i in fz.foes:
                    a = a + i.hao+i.weifen+i.name+"  "
            text "{size=20}{font=问藏书房.ttf}" + a
            text "{size=25}{font=问藏书房.ttf}族亲:"
            python:
                a = ""
                for i in fz.sisters:
                    a = a + i.hao+i.weifen+i.name+"  "
            text "{size=20}{font=问藏书房.ttf}" + a

            text "{size=25}{font=问藏书房.ttf}经历:"
            python:
                a = ""
                for i in fz.story:
                    a = a + i
            text "{size=20}{font=问藏书房.ttf}" + a
    vbox align (0.8,0.5):
        if fz == my:
            pass
        else:
            if mapname == "冷宫":
                pass
            else:
                textbutton "技能" action ToggleScreen("fzskills", fz = fz)

    textbutton "关闭":
        align (0.8,0.75)
        action Hide("fz_sx2")



screen feipinhuangsi(name, list):
    viewport:
        xsize 200
        ysize 200
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        align (0.8,0.8)
        has vbox
        text "[name]的皇嗣"
        for i in list:
            text "{size=20}{font=问藏书房.ttf}[i.sex][i.name]{/font}{/size}"


label 介绍子嗣(fz):
    "[fz.name]当前有[fz.kidsnum]个皇嗣。"
    python:
        for i in fz.kids:
            "[i.sex][i.name]"

screen feipinGongnv(gn, fz, name, list):
    style_prefix "Gongnv"
    add "gui/frame.webp" zoom 1.5 xalign 0.45 yalign 0.25
    $ a = len(list) + 1
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

        for i in list:
            fixed:
                xsize 1350
                ysize 40
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
                    if my.level == beifei:
                        textbutton "——"


                    elif my.level == 0 and i.level == "婢子" or my.qinjunum == 1 and fz.palacenum == my.palacenum and i.level == "婢子":
                        textbutton "{size=25}管理" action Hide("fz_jm"),Hide("feipinGongnv"),Call("管理别人宫女",gn = i,fz = fz)
                    else:
                        textbutton "{size=25}收买" align (0.5,0.5) action Hide("fz_jm"),Hide("feipinGongnv"),Call("收买宫女",gn = i,fz = fz)
                    text "[i.level]"
                    text "[i.name]"
                    text "[i.age]"
                    text "[i.beautylv]"
                    text "[i.xingge]"
                    text "[i.yexinlv]"
                    text str(int(i.like))
                    python:
                        tempskill = ""

                        for i in i.skill:
                            tempskill = tempskill + i + " "

                    text "{size=20}[tempskill]" align (0.5,0.5)


    imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
        align (0.9,0.8)
        action Hide("feipinGongnv")
 
