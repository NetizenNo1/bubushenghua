


label 妃嫔被责罚后续(fz):
    scene 圣宸宫内
    with fade
    show 皇帝 at chara
    if my.love < 60:
        "[guoxing][emperor]站在殿内，一脸凝重。当看到你的时候，眼底闪过一丝怒意。"
    else:
        "[guoxing][emperor]站在殿内，一脸凝重。当看到你的时候，眼底浮现一丝愤怒，以及其他说不清的复杂情绪。"
    我 "臣妾参见皇上。"
    皇上 "跪下。"
    皇上 "你可知错？"
    menu:
        "知错":
            皇上 "（长叹一声……）"
        "不知":

            if my.love < 60:
                皇上 "不知？！"
                皇上 "那你知不知道，她人已经没了！"
            else:
                皇上 "你说不知，那朕就相信你不知。"
                皇上 "其实朕也不知你错在何处。"
                皇上 "朕只知道，朕的爱妃，朕的[aicheng]，杀了[fz.cheng]！"
    if huaiyun(fz) == True:
        if suibianzefa == True:
            皇上 "你明知[fz.cheng]有孕在身，却为何还要责罚她？！"
            皇上 "——不必多言，我已经问清楚，[fz.cheng]本无大错，是你！是你步步紧逼，故意挑衅，将她送到掖庭！"
            皇上 "她到底做错了什么？你若不满，为何不向朕禀报？"
            皇上 "你，不仅杀了[fz.cheng]，还杀了朕的孩子啊！"
            $ my.exp = my.exp - 50 - (17-my.level)*30
        else:
            皇上 "你明知[fz.cheng]有孕在身，却为何还要责罚她？！"
            皇上 "[fz.cheng]错了再多，朕的孩子总归是无辜的！"
            皇上 "而你，却亲手杀了朕的孩子！"
            $ my.exp = my.exp - 50 - (17-my.level)*20
        皇上 "（面色悲愤）这一次，朕无法原谅你！"
        皇上 "你先出去，朕现在不想见到你！"
        if huaiyun(my) == True:
            皇上 "来人，送[my.cheng]回宫，听候发落！"
        else:
            皇上 "来人，传朕旨意，将[my.cheng]禁足三月，听候发落！"
            $ my.state = "禁足"
    elif fz.health <= 200 or fz.state == "病重":
        皇上 "你明知[fz.cheng]身子虚弱，却为何还要责罚她？！"
        皇上 "——不必多言，我已经问清楚，[fz.cheng]本无大错，是你！是你步步紧逼，故意挑衅，将她送到掖庭！"
        皇上 "她到底做错了什么？你若不满，为何不向朕禀报？"
        皇上 "你——让朕真的很失望。"
        if huaiyun(my) == True:
            皇上 "（面色颓然）好了，让朕静一静。你也是有孕的身子，好好回去休养吧。"
        else:
            皇上 "（面色颓然）好了，让朕静一静。你先回去，接下来这三个月，好好在寝宫里反省自己的罪过。"
            $ my.state = "禁足"
        皇上 "也让朕好好想想，该如何处置你。"
        $ my.exp = my.exp - 50 - (17-my.level)*15
    else:
        pass
    $ feizibeizhangze = False
    $ suibianzefa = False
    $ timenum = timenum + 1
    $ AP = AP + 1
    jump 寝居界面






label 造谣妃子(fz):

    if zaoyaoshijian == []:
        $ tempgnlist = []
        python:
            for i in my.Gongnv:
                if i.state != "寻常":
                    pass
                elif i.level == "贴身侍女" or i.level == "婢子":
                    tempgnlist.append(i)
                else:
                    pass
            tempgnlist = sorted(tempgnlist, key=attrgetter("lv"),reverse = False)
        hide screen myroom
        "要派谁去办此事呢？"
        menu:
            "[tempgnlist[0].name]" if len(tempgnlist)>0:
                $ zaoyaogn = tempgnlist[0]
            "[tempgnlist[1].name]" if len(tempgnlist)>1:
                $ zaoyaogn = tempgnlist[1]
            "[tempgnlist[2].name]" if len(tempgnlist)>2:
                $ zaoyaogn = tempgnlist[2]
            "[tempgnlist[3].name]" if len(tempgnlist)>3:
                $ zaoyaogn = tempgnlist[3]
            "[tempgnlist[4].name]" if len(tempgnlist)>4:
                $ zaoyaogn = tempgnlist[4]
            "[tempgnlist[5].name]" if len(tempgnlist)>5:
                $ zaoyaogn = tempgnlist[5]
            "[tempgnlist[6].name]" if len(tempgnlist)>6:
                $ zaoyaogn = tempgnlist[6]
            "无人可用，只得作罢" if len(tempgnlist) == 0:
                if mapname == "寝居":
                    hide screen Bigmap
                    jump 寝居界面
                else:
                    jump 皇宫界面


            "算了" if len(tempgnlist)>0:
                if mapname == "寝居":
                    hide screen Bigmap
                    jump 寝居界面
                else:
                    jump 皇宫界面



        "散播何种谣言？"
        menu:
            "欺凌宫人":
                $ zaoyaoyy = 1
            "妄议朝政":
                $ zaoyaoyy = 2
            "不敬先祖":
                $ zaoyaoyy = 3
            "再做打算":


                if mapname == "寝居":
                    hide screen Bigmap
                    jump 寝居界面
                else:
                    jump 皇宫界面


        "[zaoyaogn.name]领命而去……"
        $ zaoyaogn.state = "任务中"
        $ zhudongzaoyao = 1
        $ beizaoyao = fz
        $ zaoyaozhe = my
        $ zaoyaocishu = 1
        $ zaoyaoshijian = [fz,zaoyaogn,zaoyaoyy]
        $ timenum = timenum + 1
        $ AP = AP + 1
        if mapname == "寝居":
            hide screen Bigmap
            jump 寝居界面
        else:
            jump 皇宫界面
    else:

        "本旬已经派人去办事了，再生谣言恐怕会引人猜忌……"
        if mapname == "寝居":
            hide screen Bigmap
            jump 寝居界面
        else:
            jump 皇宫界面

label 管理宫务:
    menu:
        "妃嫔位份" if diwei(my) <= 1:
            if my.tequan1 != 0:
                我 "最近似乎不宜再变动妃嫔位份了……"
            elif my.level == 0:
                call screen choicefz(NPC_fz_list)
                call 管理妃嫔位份 (fz=fz) from _call_管理妃嫔位份
            else:
                python:
                    templist = []
                    for i in NPC_fz_list:
                        if i == my:
                            pass
                        elif i.palace == my.palace:
                            templist.append(i)
                call screen choicefz(templist)
                call 管理妃嫔位份 (fz=fz) from _call_管理妃嫔位份_1

        "妃嫔封号" if my.level == 0:
            python:
                templist = []
                for i in NPC_fz_list:
                    if i == my:
                        pass
                    elif i.hao == "":
                        templist.append(i)
            call screen choicefz(templist)
            call 管理妃嫔封号 (fz=fz) from _call_管理妃嫔封号
        "迁宫" if diwei(my) <= 1:
            python:
                templist = []
                for i in NPC_fz_list:
                    if i == my or i.level == 0 or i.qinjunum == 1:
                        pass
                    else:
                        templist.append(i)
            call screen choicefz(templist)
            if my.level == 0:
                "要将[fz.cheng]的寝居迁到何处？"
                call screen qiangong(fz)
                "迁宫完成"
            elif fz.palacenum == my.palacenum:
                "要将[fz.cheng]迁到哪个宫？"
                menu:
                    "[palaces[0][0][0]] " if fz.palacenum != 0 and 0 in shengyucedian_list:
                        $ a = 0
                    "[palaces[1][0][0]]" if fz.palacenum != 1 and 1 in shengyucedian_list:
                        $ a = 1
                    "[palaces[2][0][0]]" if fz.palacenum != 2 and 2 in shengyucedian_list:
                        $ a = 2
                    "[palaces[3][0][0]]" if fz.palacenum != 3 and 3 in shengyucedian_list:
                        $ a = 3
                    "[palaces[4][0][0]]" if fz.palacenum != 4 and 4 in shengyucedian_list:
                        $ a = 4
                    "[palaces[5][0][0]]" if fz.palacenum != 5 and 5 in shengyucedian_list:
                        $ a = 5
                show 我的宫女
                if str(palaces[a][1][1]) == "":
                    $ temptext = palaces[a][0][0]
                    我的宫女 "因[temptext]主殿空置，无需征得主位同意，迁宫已完成。"
                    $ qiangong_out(fz,a)
                    我的宫女 "[fz.cheng]会被安置在[fz.palace][fz.qinju]。"
                else:
                    $ tempfz = palaces[a][1][1]
                    if tempfz in my.foes or my in tempfz.foes:
                        我的宫女 "[tempfz.cheng]听说是您的意思，想也不想就拒绝了……"
                    elif fz in tempfz.friends or tempfz in fz.friends:
                        我的宫女 "[tempfz.cheng]听说要把[fz.cheng]迁到她的宫里，很高兴地同意了。"
                        $ qiangong_out(fz,a)
                        我的宫女 "[fz.cheng]会被安置在[fz.palace][fz.qinju]。"
                    elif tempfz.like >= 50 and fz not in tempfz.foes:
                        我的宫女 "[tempfz.cheng]听说是您的意思，很爽快地答应了。"
                        $ qiangong_out(fz,a)
                        我的宫女 "[fz.cheng]会被安置在[fz.palace][fz.qinju]。"
                    else:
                        $ lucky = renpy.random.randint(0,100)
                        if lucky <= tempfz.like:
                            我的宫女 "[tempfz.cheng]在考虑了片刻以后同意让[fz.cheng]迁过去了。"
                            $ qiangong_out(fz,a)
                            我的宫女 "[fz.cheng]会被安置在[fz.palace][fz.qinju]。"
                        else:
                            我的宫女 "[tempfz.cheng]在考虑了片刻以后还是拒绝了。"
                hide 我的宫女
            else:
                show 我的宫女
                if my.palacenum not in shengyucedian_list:
                    我的宫女 "娘娘，[my.palace]已经没有空余的宫室了。"
                elif str(palaces[fz.palacenum][1][1]) == "":
                    $ temptext = palaces[fz.palacenum][1][1]
                    我的宫女 "因[temptext]主殿空置，无需征得主位同意，要将[fz.cheng]安置在何处呢？"
                    call screen qiangong_in(fz,my.palacenum)
                    我的宫女 "是，奴婢这就安排人吩咐下去，将[fz.cheng]会被安置到[fz.palace][fz.qinju]。"
                else:
                    $ tempfz = palaces[fz.palacenum][1][1]
                    if tempfz in my.foes or my in tempfz.foes:
                        我的宫女 "[tempfz.cheng]听说是您的意思，想也不想就拒绝了……"
                    elif tempfz.like >= 80:
                        我的宫女 "[tempfz.cheng]听说是您的意思，很爽快地答应了。"
                        我的宫女 "要将[fz.cheng]安置在何处呢？"
                        call screen qiangong_in(fz,my.palacenum)
                        我的宫女 "是，奴婢这就安排人吩咐下去，将[fz.cheng]会被安置到[fz.palace][fz.qinju]。"
                    else:
                        $ lucky = renpy.random.randint(0,100)
                        if lucky <= tempfz.like:
                            我的宫女 "[tempfz.cheng]在考虑了片刻以后同意了您的安排。"
                            我的宫女 "要将[fz.cheng]安置在何处呢？"
                            call screen qiangong_in(fz,my.palacenum)
                            我的宫女 "是，奴婢这就安排人吩咐下去，将[fz.cheng]会被安置到[fz.palace][fz.qinju]。"
                        else:
                            我的宫女 "[tempfz.cheng]在考虑了片刻以后还是拒绝了。"
                hide 我的宫女
        "算了":
            jump 寝居界面
    $ timenum += 1
    jump 寝居界面

label 管理皇嗣:
    menu:
        "皇嗣婚配":
            jump 皇嗣婚配
        "子嗣过继":
            jump 子嗣过继

screen qiangong(who):
    style_prefix "meetNPC"
    frame:
        has vbox
        $ palacenum = 0
        $ qinjunum = 2
        for i in palaces:

            text i[0][0]
            grid 4 2:

                for j in i[2:]:
                    if str(j[1]) == "":
                        textbutton j[0] action Function(qiangong,who = who,a=palacenum,b=qinjunum),Return()
                    else:
                        textbutton j[0]
                    $ qinjunum += 1

            $ palacenum +=  1
            $ qinjunum = 2

screen qiangong_in(who, a):
    style_prefix "palace"
    frame:
        background None
        yalign 0.2 xalign 0.6



        has grid 2 4
        xspacing 60
        yspacing 30
        yalign 0.45 xalign 0.5
        $ templist = list(range(2,10))
        for i in templist:
            if str(palaces[a][i][1]) ==  "":
                textbutton palaces[a][i][0] action Function(qiangong,who = who,a=a,b=i),Return()
            else:
                textbutton palaces[a][i][0]

init python:
    def qiangong(who,a,b):
        Changeqinju(who)
        palaces[a][0][1] = palaces[a][0][1] +1
        palaces[a][b][1] = who
        who.palacenum = a
        who.qinjunum = b
        who.palace =  palaces[a][0][0]
        who.qinju =  palaces[a][b][0]
        tempnum = 0
        for j in palaces[a][2:]:
            if str(j[1]) == "":
                tempnum += 1
            else:
                pass
        if tempnum <= 0 :
            shengyucedian_list.remove(a)
    def qiangong_out(who,a):
        Changeqinju(who)
        templist = []
        tempnum = 2
        for j in palaces[a][2:]:
            if str(j[1]) == "":
                templist.append(tempnum)
            else:
                pass
            tempnum += 1
        b = renpy.random.choice(templist)
        palaces[a][0][1] = palaces[a][0][1] +1
        who.qinju =palaces[a][b][0]
        palaces[a][b][1] = who
        who.palacenum = a
        who.qinjunum = b
        who.palace =  palaces[a][0][0]
        tempnum = 0
        for j in palaces[a][2:]:
            
            if str(j[1]) == "":
                tempnum += 1
            else:
                pass
        if tempnum <= 0 :
            shengyucedian_list.remove(a)




label 管理妃嫔位份(fz):
    hide screen myroom
    我 "要如何变更此人的位份？"
    $ pretext = str(fz.hao)+str(fz.weifen)+str(fz.name)
    $ preweifen = str(fz.weifen)
    $ tempcheng = fz.cheng
    $ tempnum2 = int(fz.exp)
    $ tempnum = int(fz.level)
    call screen guanlifz(fz = fz)
    python:
        for i in yuanweifen:
            if isinstance(i[1],tuple):
                if preweifen in i[1]:
                    a = i[0]
                    if isinstance(weifen_list[a][1],list) and preweifen not in weifen_list[a][1]:
                        weifen_list[a][1].append(preweifen)
                    else:
                        pass
                else:
                    pass
            else:
                pass

        a = fz.level
        if isinstance(weifen_list[a][1],list):
            if weifen_list[a][1] != []:
                weifen_list[a][1].remove(fz.weifen)
            else:
                pass
    $ weifen_list[tempnum][5] = weifen_list[tempnum][5]-1
    $ weifen_list[a][5] = weifen_list[a][5]+1
    $ fz.exp = weifen_list[a][3] + (weifen_list[a][4]-weifen_list[a][3])*0.5
    if tempnum > 3 and a < 4:
        $ fz.tequan1 = -1
        $ Changeqinju(fz)
        $ randompalace(fz)
    elif tempnum < 4 and a > 3:
        $ fz.tequan1 = 0
        $ Changeqinju(fz)
        $ randompalace(fz)
    else:

        pass
    $ ChangeGongnv(fz)
    if fz.level < tempnum:
        $ temptext = "来人，替本宫传话给掖廷，立即奏请皇上拟旨将"+tempcheng+"晋为"+fz.weifen+"！"
        $ my.tequan1 = 6 - my.huashu["一B"] - fz.huashu["一B"]
    else:
        $ my.tequan1 = 6
        $ temptext = "来人，替本宫传话给掖廷，立即奏请皇上拟旨将"+tempcheng+"降为"+fz.weifen+"！"
    $ ChangeGongnv(fz)
    我 "[temptext]"
    "（因为你的行为，[fz.name]在后宫的威望和对你的态度产生了巨大的变化。）"
    $ fz.like+= (fz.exp - tempnum2)/25
    if fz.level < tempnum:
        $ tempstory = str(year)+"年"+str(month)+"月，由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请晋为"+str(fz.weifen)+"。\n"
        $ tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext+"由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请晋为"+str(fz.weifen)+"。\n"
    else:
        $ tempstory = str(year)+"年"+str(month)+"月，由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请降为"+str(fz.weifen)+"。\n"
        $ tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext+"由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请降为"+str(fz.weifen)+"。\n"
    $ fz.story.append(tempstory)
    $ allstory.insert(0,tempstory2)
    $ changecheng(fz)
    if mapname == "寝居":
        hide screen Bigmap
        jump 寝居界面
    else:
        jump 皇宫界面


label 管理妃嫔封号(fz):
    $ temphao1 = renpy.random.choice(hao_list)
    $ temphao2 = renpy.random.choice(hao_list)
    $ temphao3 = renpy.random.choice(hao_list)
    menu:
        "[temphao1]":
            $ fz.hao = temphao1
            $ hao_list.remove(temphao1)
        "[temphao2]":
            $ fz.hao = temphao2
            $ hao_list.remove(temphao2)
        "[temphao3]":
            $ fz.hao = temphao3
            $ hao_list.remove(temphao3)
        "手动输入":
            python:
                temphao = renpy.input("为[fz.name]选择封号（不输入则赐号[temphao1]）",length=2)
                temphao = temphao.strip()

                if not temphao:
                    temphao = temphao1
                fz.hao = temphao
        "改日再议":

            我 "此事还是另议吧。"
            jump 寝居界面
    $ changecheng(fz)
    $ tempstory = str(year)+"年"+str(month)+"月，由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请赐号"+str(fz.hao)+"。\n"
    $ tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ str(fz.hao)+str(fz.weifen)+str(fz.name)+"由"+str(my.hao)+str(my.weifen)+str(my.name)+"上请赐号"+str(fz.hao)+"。\n"
    $ fz.story.append(tempstory)
    $ allstory.insert(0,tempstory2)
    $ timenum += 1
    jump 寝居界面


label 管理妃子_算了:
    我 "此事还需从长计议。"
    if mapname == "寝居":
        hide screen Bigmap
        jump 寝居界面
    else:
        jump 皇宫界面

init python:
    def fzgaoweitequan(self,fz):
        global tempweifenlist
        tempweifenlist = []
        del tempweifenlist
        tempweifenlist = []
        
        b = int(fz.level)
        a = beifei
        c = 50+int(self.exp*0.1)
        while fz.exp + c > weifen_list[a][4] and a > 0 :
            if weifen_list[a][5] == weifen_list[a][2]:
                pass
            elif a > b:
                pass
            else:
                tempweifenlist.append(a)
            a = a - 1
        tempweifenlist = sorted(tempweifenlist, reverse = False)
        if huaiyun(fz) == True:
            pass
        else:
            a = beifei - 1
            while fz.exp-c < weifen_list[a][3] and a < beifei:
                if weifen_list[a][5] == weifen_list[a][2]:
                    pass
                elif a < b:
                    pass
                else:
                    tempweifenlist.append(a)
                a = a - 1
        
        if beifei in tempweifenlist:
            tempweifenlist.remove(beifei)
        else:
            pass
        if b in tempweifenlist:
            tempweifenlist.remove(b)
        else:
            pass

screen guanlifz(fz):
    python:
        tempweifenlist = []
        b = int(fz.level)
        a = beifei
        c = 50+int(my.exp*0.1)
        while fz.exp + c > weifen_list[a][4] and a > 0 :
            if weifen_list[a][5] == weifen_list[a][2]:
                pass
            elif a > fz.level:
                pass
            else:
                tempweifenlist.append(a)
            a = a - 1
        tempweifenlist = sorted(tempweifenlist, reverse = False)
        if huaiyun(fz) == True:
            pass
        else:
            a = 0
            while fz.exp-c < weifen_list[a][3] and a < beifei:
                if weifen_list[a][5] == weifen_list[a][2]:
                    pass
                elif a <= fz.level:
                    pass
                else:
                    tempweifenlist.append(a)
                a = a + 1

        if beifei in tempweifenlist:
            tempweifenlist.remove(beifei)
        else:
            pass
    style_prefix "choicemianban"

    $ tempnum = (len(tempweifenlist)-1)/3 + 1
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


            for i in tempweifenlist:
                if weifen_list[i][0] < fz.level:
                    if isinstance(weifen_list[i][1],list):
                        for j in weifen_list[i][1]:
                            textbutton "{size=25}（晋位）"+ j action SetVariable("fz.weifen",j),SetVariable("fz.level",weifen_list[i][0]),Hide("guanlifz"),Return()
                    else:
                        textbutton "{size=25}（晋位）"+ weifen_list[i][1] action SetVariable("fz.weifen",weifen_list[i][1]),SetVariable("fz.level",weifen_list[i][0]),Hide("guanlifz"),Return()
                elif weifen_list[i][0] == fz.level:
                    if isinstance(weifen_list[i][1],list):
                        for j in weifen_list[i][1]:
                            textbutton "{size=25}（原级）"+ j
                    else:
                        textbutton "{size=25}（原级）"+ weifen_list[i][1]

                else:
                    if isinstance(weifen_list[i][1],list):
                        for j in weifen_list[i][1]:
                            textbutton "{size=25}（降位）"+ j action SetVariable("fz.weifen",j),SetVariable("fz.level",weifen_list[i][0]),Hide("guanlifz"),Return()
                    else:
                        textbutton "{size=25}（降位）"+ weifen_list[i][1] action SetVariable("fz.weifen",weifen_list[i][1]),SetVariable("fz.level",weifen_list[i][0]),Hide("guanlifz"),Return()
            if len(tempweifenlist)-1 - 3*a == 1:
                textbutton ""
            elif len(tempweifenlist)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        vbox align (0.5,1.0):
            textbutton "{size=45}算了" action Jump("管理妃子_算了")


label 家族事宜:
    menu:
        "接济银两" if my.familylevel != 0:
            menu:
                "可通过接济银两助益母族的发展。"
                "接济五百两" if money >= 500:
                    $ tempnum = 500
                "接济两百两" if money >= 200:
                    $ tempnum = 200
                "接济一百两" if money >= 100:
                    $ tempnum = 100
                "算了":
                    $ tempnum = 0
            if tempnum == 0:
                我 "如今本宫自个手头也不宽裕……还是以后再说吧。"
                jump 寝居界面
            else:
                "命宫人送了[tempnum]两银子到家中。"
                $ my.father.exp += tempnum*0.01*my.familylevel
                $ money -= tempnum
                $ timenum += 1
                jump 寝居界面
        "算了":


            jump 寝居界面
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
