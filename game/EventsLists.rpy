





label 过月事件检测:
    hide screen myroom



    if month == 6  and datenum == 3 and canjiayanhui == False:
        python:
            renpy.call("别人的宴会",from_current=False)

    elif month == 12  and datenum == 3 and canjiayanhui == False:
        python:
            renpy.call("别人的宴会",from_current=False)
    else:
        $ canjiayanhui = False




    if atan_time == 11:
        if atan_end_1 == 1 and len(atan_help) > 0:
            call 阿檀 from _call_阿檀
        elif atan_end_2 >= 7:
            call 阿檀_出宫 from _call_阿檀_出宫
        else:
            call 阿檀_去世 from _call_阿檀_去世

    if chuhuan_time == 5 and chuhuan_1 == False and chuhuan_come == False:
        if hdxingge == "温柔" or hdxingge == "风流" or hdxingge == "刚正":
            $ chuhuan_come = True
            call 楚欢 from _call_楚欢
            call 楚欢_自动进宫 from _call_楚欢_自动进宫
        else:

            pass
    elif chuhuan_time == 5  and chuhuan_2 == True and chuhuan_come == False:
        $ chuhuan_come = True
        call 楚欢 from _call_楚欢_1
        call 楚欢_进宫 from _call_楚欢_进宫
    elif chuhuan in juqingfei and chuhuan.foes != []:
        $ chuhuan.foes = []
    elif chuhuan_5 == 2 and jinzu(my) == False:
        $ chuhuan_5 = 0
        call 楚欢_女主被罚 (fz=chuhuan_die) from _call_楚欢_女主被罚
    elif chuhuan_5 == 3:
        $ bg("寝居")
        show 我的宫女
        我的宫女 "主子，奴婢方才在外头碰到了[chuhuan.cheng]的宫女……哭着求着说让您去[chuhuan.palace]见[chuhuan.cheng]一面，您看这？"
        我 思 "那便去看看吧。"
        jump 楚欢_最后一面
    else:
        pass

    if diwei(taoning) <= 1 and taoning_3 == True and taoning_fatherup == -1:
        $ taoning_fatherup = 0
        $ guanyuan_levelchange(taoning.father,sheng =True)
    if 0 <= taoning_fatherup <= 3:
        $ taoning_fatherup += 1




    call 前朝演变 from _call_前朝演变
    call 子嗣演变 from _call_子嗣演变

    python:
        templist = NPC_fz_list + NPC_fz_feilist
        for i in templist:
            for j in i.tags:
                if "身怀皇嗣" in j:
                    if 3 <= j[1] < 25:
                        if i.jiayun == False:
                            lucky = round(i.lucky+i.health*0.2+30)
                            if lucky <= 1:
                                lucky = 1
                            lucky = renpy.random.randint(0,lucky)
                            if lucky == 0 :
                                i.state = "抱恙"
                                j[1] = 0
                                i.health = (i.health-100)*0.8
                                i.tags.remove(j)
                                renpy.call("不幸小产_随机",fz = i,from_current=False)
                            else:
                                j[1] = j[1] + 1
                        else:
                            if j[1] == 24:
                                lucky = 0
                            else:
                                lucky = renpy.random.randint(0,24 - j[1])
                            if lucky == 0 and i != my:
                                i.jiayun = False
                                i.tags.remove(j)
                                renpy.call("不幸小产_假孕",fz = i,from_current=False)
                            else:
                                j[1] = j[1] + 1
                    
                    elif j[1] >= 30 :
                        
                        j[1] = 0
                        i.tags.remove(j)
                        renpy.call("生产事件_前",fz = i,from_current=False)
                    
                    elif j[1] >= 25 : 
                        if i == my and my.jiayun == True:
                            i.jiayun = False
                            i.tags.remove(j)
                            renpy.call("强制小产_假孕",fz = i,from_current=False)
                        else:
                            lucky = renpy.random.randint(0, 900)
                            if lucky - 200 > fz.health:
                                renpy.call("早产事件",fz = i,from_current=False)
                            else:
                                j[1] = j[1] + 1
                    
                    elif j[1] < 3:
                        j[1] = j[1] + 1
                    else:
                        pass
                if "禁足一月" in j:
                    j[1] = j[1] + 1
                    i.yali += 5
                    if j[1] >= 4 :
                        i.tags.remove(j)
                if "禁足三月" in j:
                    j[1] = j[1] + 1
                    i.yali += 5
                    if j[1] >= 10 :
                        i.tags.remove(j)
                if "禁足半年" in j:
                    j[1] = j[1] + 1
                    i.yali += 5
                    if j[1] >= 19 :
                        i.tags.remove(j)
                if "身受杖责" in j:
                    i.state = "病重"
                    j[1] = j[1] + 1
                    if j[1] >= 4 :
                        i.tags.remove(j)

        for i in NPC_fz_feilist:
            i.jinzu = i.jinzu + 1
            if i.familylevel <3:
                i.exp = i.exp + 1
            elif i.familylevel < 8:
                i.exp = i.exp +0.6
            else:
                i.exp = i.exp + 0.3
            i.qingxiang = i.qingxiang - renpy.random.randint(1,3)*0.1
            if i.love < 0:
                i.health = i.health + i.love*0.3
                i.love = i.love + 0.1
            elif i.love > 10:
                i.exp = i.exp + (i.love-10)
                i.love = 10
            else:
                i.exp = i.exp + i.love*0.1
                i.health = i.health - renpy.random.randint(-2,5)*0.3
            if i.jinzu > 72 and i.love >= 0 and i.exp >= 0:
                Feizishengjiang(i)
            elif i.jinzu > 90:
                i.exp = i.exp + 0.5
                if i.love < 0:
                    i.love = i.love + 0.5
                else:
                    pass
            else:
                pass
            tags_limitcheck(i)
        for i in lenggong:
            if i.level == beifei:
                pass
            else:
                lenggong.remove(i)
        for i in manxingdu:
            if i[0] in NPC_fz_dielist :
                manxingdu.remove(i)
            elif i[0] in NPC_Kids_list and i[0].live == -1:
                manxingdu.remove(i)
            else:
                i[0].shou -= i[1]*0.15
        for i in NPC_fz_list + NPC_fz_feilist:
            if i.like < 0 and i in my.friends:
                my.friends.remove(i)
            elif i.like < 0 and my in i.friends:
                i.friends.remove(my)
            else:
                pass
            if i.like > 50 and i in my.foes:
                my.foes.remove(i)
            elif i.like > 50 and my in i.foes:
                i.foes.remove(my)
            else:
                pass
        for i in NPC_fz_list:
            if i in bujifz:
                if i.exp < 1500:
                    i.exp = 0
                else:
                    i.exp = (i.exp-1500)*0.5
                tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，奉天楼来报，"+str(i.hao)+(i.weifen)+str(i.name) +"流年不吉，有冲撞龙体、危及社稷之兆。\n"
                allstory.insert(0,tempstory2)
                tempstory =str(year)+"年"+str(month)+"月，奉天楼来报，其流年不吉，有冲撞龙体、危及社稷之兆。\n"
                i.story.append(tempstory)
                bujifz.remove(i)
            else:
                pass
            for j in i.Gongnv:
                if i == my:
                    pass
                elif j.level == "散役":
                    i.Gongnv.remove(j)
                    YTGongnv.append(j)
                else:
                    pass
                if i.fangyu["一B"] == 0:
                    pass
                elif i.fangyu["一B"] == 1:
                    j.yexin -= 0.3
                elif i.fangyu["一B"] == 2:
                    j.yexin -= 0.5
                elif i.fangyu["一B"] == 3:
                    j.yexin -= 1
            i.Gongnv = sorted(i.Gongnv, key=attrgetter("lv"),reverse = False)
            if i.health < 100:
                lucky =  renpy.random.randint(0,10)
                if lucky < 3:
                    i.state = "病重"
                elif lucky < 5:
                    i.state = "抱恙"
                elif jinzu(i) == True:
                    i.health = i.health + renpy.random.randint(5,15)
                else:
                    i.state = "寻常"
                    i.health = i.health + renpy.random.randint(5,15)
            
            elif i.health < 200:
                lucky =  renpy.random.randint(0,10)
                if lucky == 0:
                    i.state = "病重"
                elif lucky < 2:
                    i.state = "抱恙"
                elif jinzu(i) == True:
                    i.health = i.health + renpy.random.randint(5,15)
                else:
                    i.state = "寻常"
                    i.health = i.health + renpy.random.randint(5,15)
            elif i.health > 900:
                i.state = "寻常"
            else:
                lucky =  round(i.health/10)
                lucky =  renpy.random.randint(0,lucky*2)
                if lucky == 0:
                    i.state = "抱恙"
                elif huaiyun(i) == True:
                    i.state = "寻常"
                    i.health = i.health + renpy.random.randint(-1,1)
                elif jinzu(i) == True:
                    i.state = "寻常"
                    i.health = i.health + renpy.random.randint(-1,1)
                else:
                    i.state = "寻常"
                    i.health = i.health + renpy.random.randint(-1,1)
            if i.state == "抱恙":
                i.health = i.health + i.love*0.5  -15
            elif i.state == "病重":
                i.health = i.health +i.love - 30
            else:
                pass
            if i.beauty > 999:
                i.beauty = 999
            else:
                pass
            if i.health >999:
                i.health = 999
            else:
                pass
            if i.qizhi > 999:
                i.qizhi = 999
            else:
                pass
            if i.meili > 999:
                i.meili = 999
            else:
                pass
            
            if i.love > 100:
                i.love = 100
            elif i.love < -100:
                i.love = -100
            elif i.love < -20:
                i.love = i.love + 0.3 + (10-i.familylevel)*0.1
            else:
                pass
            if i.xinji > 999:
                i.xinji = 999
            if i.taihoulike > 100:
                i.taihoulike = 100
            else:
                pass
            if i.muzic > 100:
                i.muzic = 100
            else:
                pass
            if i.dance > 100:
                i.dance = 100
            else:
                pass
            if i.book > 100:
                i.book = 100
            else:
                pass
            if i.cixiu > 100:
                i.cixiu = 100
            else:
                pass
            if i.medic > 100:
                i.medic = 100
            else:
                pass
            if i.battle > 100:
                i.battle = 100
            else:
                pass
            if i.lucky > 100:
                i.lucky = 100
            elif i.lucky < -100:
                i.lucky = -100
            if i.like > 100 and i != my:
                i.like = 100
            elif player == 1 and i == sidi and i.like >= 0:
                i.like = 0
            elif i.like < -100:
                i.like = -100
            else:
                pass
            if i.qingxiang > 100:
                i.qingxiang = 100
            elif i.qingxiang < 0:
                i.qingxiang = 0
            else:
                pass
            if i.exp >= yuanweifen[0][3]*2:
                i.exp = yuanweifen[0][3]*2
            elif i.exp <= - 200:
                i.exp = -200
            else:
                pass
            
            
            
            if i.yali >= 100:
                i.yali = 0
                if havetag("郁结于心",i) == True :
                    i.tags.remove(tags_yali[0])
                else:
                    pass
                if havetag("心衰力竭",i) == True :
                    i.tags.remove(tags_yali[1])
                else:
                    pass
                if i == my:
                    renpy.call("压力满了",fz = my,from_current=False)
                else:
                    lucky = renpy.random.randint(0,10)
                    if lucky == 0:
                        renpy.call("有人疯了",fz = i,from_current=False)
                    else:
                        renpy.call("压力满了",fz = i,from_current=False)
            elif i.yali >= 80:
                if havetag("郁结于心",i) == True :
                    i.tags.remove(tags_yali[0])
                else:
                    pass
                if havetag("心衰力竭",i) == True :
                    if i.xinji >= 900 or i.xinji < 100:
                        i.yali = i.yali - 5
                    elif i.xinji >= 700 or i.xinji < 300:
                        i.yali = i.yali - 4
                    else:
                        i.yali = i.yali - 3
                else:
                    i.tags.append(tags_yali[1])
            elif i.yali >= 60:
                if havetag("心衰力竭",i) == True :
                    i.tags.remove(tags_yali[1])
                else:
                    pass
                if havetag("郁结于心",i) == True :
                    if i.xinji >= 900 or i.xinji < 100:
                        i.yali = i.yali - 4
                    elif i.xinji >= 700 or i.xinji < 300:
                        i.yali = i.yali - 3
                    else:
                        i.yali = i.yali - 2
                else:
                    i.tags.append(tags_yali[0])
            elif i.yali <= 0:
                i.yali = 0
            else:
                if havetag("郁结于心",i) == True :
                    i.tags.remove(tags_yali[0])
                else:
                    pass
                if havetag("心衰力竭",i) == True :
                    i.tags.remove(tags_yali[1])
                else:
                    pass
                if i.xinji >= 900 or i.xinji < 100:
                    i.yali = i.yali - 3
                elif i.xinji >= 700 or i.xinji < 300:
                    i.yali = i.yali - 2
                else:
                    i.yali = i.yali - 1
        tempfzlist = []
        for i in NPC_fz_list:
            if i.level == beifei:
                pass
            elif i == my:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重":
                pass
            elif   tags[4] in i.tags:
                pass
            elif tags_yali[2] in i.tags:
                pass
            else:
                tempfzlist.append(i)
        for i in tempfzlist:
            tags_NPCyangcheng(i)
            lucky =  renpy.random.randint(0,4)
            if lucky == 0:
                i.beauty += renpy.random.randint(0,2)
            elif lucky == 1:
                i.qizhi += renpy.random.randint(0,2)
            elif lucky == 2:
                i.meili += renpy.random.randint(0,2)
            elif lucky == 3:
                i.xinji += renpy.random.randint(0,2)
            else:
                i.health += renpy.random.randint(0,2)
            lucky =  renpy.random.randint(0,10)
            if lucky ==  1:
                if i.dance > 80:
                    lucky = renpy.random.randint(0,10)
                    if lucky < 4:
                        i.dance = i.dance + 0.1
                    else:
                        pass
                elif i.dance > 50:
                    i.dance = i.dance + renpy.random.randint(1,3)*0.1
                else:
                    i.dance = i.dance + renpy.random.randint(3,8)*0.1
            elif lucky == 2:
                if i.muzic > 80:
                    lucky = renpy.random.randint(0,10)
                    if lucky < 4:
                        i.muzic = i.muzic + 0.1
                    else:
                        pass
                elif i.muzic > 50:
                    i.muzic = i.muzic + renpy.random.randint(1,3)*0.1
                else:
                    i.muzic = i.muzic + renpy.random.randint(3,8)*0.1
            elif lucky == 3:
                if i.book > 80:
                    lucky = renpy.random.randint(0,10)
                    if lucky < 4:
                        i.book = i.book + 0.1
                    else:
                        pass
                elif i.book > 50:
                    i.book = i.book + renpy.random.randint(1,3)*0.1
                else:
                    i.book = i.book + renpy.random.randint(3,8)*0.1
            elif lucky == 4:
                if i.cixiu > 80:
                    lucky = renpy.random.randint(0,10)
                    if lucky < 20:
                        i.cixiu = i.cixiu + 0.1
                    else:
                        pass
                elif i.cixiu > 50:
                    i.cixiu = i.cixiu + renpy.random.randint(1,3)*0.1
                else:
                    i.cixiu = i.cixiu + renpy.random.randint(3,8)*0.1
            else:
                pass
            if i.huashu["初始"] == 0:
                lucky = renpy.random.randint(0,6)
            elif i.huashu["初始"] == 1:
                lucky = renpy.random.randint(0,5)
            elif i.huashu["初始"] == 2:
                lucky = renpy.random.randint(0,4)
            else:
                lucky = renpy.random.randint(0,3)
            if lucky == 0:
                tempnum = renpy.random.randint(0,3)
                Taihoulike_Up(i,tempnum)
            
            else:
                pass

        if persistent.expspeed == 1:
            for i in NPC_fz_list:
                if jinzu(i) == True or tags[4] in i.tags or tags_yali[2] in i.tags:
                    pass
                else:
                    if i.love>80:
                        i.exp = i.exp + 0.6
                    elif i.love>50:
                        i.exp = i.exp +0.3
                    elif i.love>20:
                        i.exp = i.exp +0.1
                    elif i.love < -100:
                        i.exp-= 5
                        i.love += 0.1
                    elif i.love < -50:
                        i.exp -= 2
                        i.love += 0.1
                    elif i.love < -20:
                        i.exp -= 1
                        i.love += 0.1
                    elif i.love < 0:
                        i.exp -= 0.3
                    else:
                        pass
                    if i.taihoulike >80:
                        i.exp = i.exp + 0.8
                    elif i.taihoulike>50:
                        i.exp = i.exp +0.4
                    else:
                        pass
                    if i.familylevel < 4:
                        i.exp = i.exp +0.4
                    else:
                        pass
                    for j in i.friends:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp + 0.3
                        elif j.level < 4  or j.love > 50:
                            i.exp =i.exp + 0.2
                        elif j.level < 8  or j.love > 30:
                            i.exp =i.exp + 0.1
                        else:
                            pass
                    for j in i.foes:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp - 0.3
                        elif j.level < 4 or j.love > 50:
                            i.exp =i.exp - 0.2
                        elif j.level < 8 or j.love > 30:
                            i.exp =i.exp - 0.1
                        else:
                            pass
                
                tags_limitcheck(i)
        elif persistent.expspeed == 0:
            for i in NPC_fz_list:
                if jinzu(i) == True or tags[4] in i.tags or tags_yali[2] in i.tags:
                    pass
                else:
                    if i.love>80:
                        i.exp = i.exp + 0.3
                    elif i.love>50:
                        i.exp = i.exp +0.2
                    elif i.love>20:
                        i.exp = i.exp +0.05
                    elif i.love < -100:
                        i.exp-= 2.5
                        i.love += 0.1
                    elif i.love < -50:
                        i.exp -= 1
                        i.love += 0.1
                    elif i.love < -20:
                        i.exp -= 0.5
                        i.love += 0.1
                    elif i.love < 0:
                        i.exp -= 0.15
                    else:
                        pass
                    if i.taihoulike >80:
                        i.exp = i.exp + 0.4
                    elif i.taihoulike>50:
                        i.exp = i.exp +0.2
                    else:
                        pass
                    if i.familylevel < 4:
                        i.exp = i.exp +0.2
                    else:
                        pass
                    for j in i.friends:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp + 0.15
                        elif j.level < 4  or j.love > 50:
                            i.exp =i.exp + 0.1
                        elif j.level < 8  or j.love > 30:
                            i.exp =i.exp + 0.05
                        else:
                            pass
                    for j in i.foes:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp - 0.15
                        elif j.level < 4 or j.love > 50:
                            i.exp =i.exp - 0.1
                        elif j.level < 8 or j.love > 30:
                            i.exp =i.exp - 0.05
                        else:
                            pass
                
                tags_limitcheck(i)
        else:
            for i in NPC_fz_list:
                if jinzu(i) == True or tags[4] in i.tags or tags_yali[2] in i.tags:
                    pass
                else:
                    if i.love>80:
                        i.exp = i.exp + 1.2
                    elif i.love>50:
                        i.exp = i.exp +0.6
                    elif i.love>20:
                        i.exp = i.exp +0.2
                    elif i.love < -100:
                        i.exp-= 10
                        i.love += 0.1
                    elif i.love < -50:
                        i.exp -= 4
                        i.love += 0.1
                    elif i.love < -20:
                        i.exp -= 2
                        i.love += 0.1
                    elif i.love < 0:
                        i.exp -= 0.6
                    else:
                        pass
                    if i.taihoulike >80:
                        i.exp = i.exp + 1.6
                    elif i.taihoulike>50:
                        i.exp = i.exp +0.8
                    else:
                        pass
                    if i.familylevel < 4:
                        i.exp = i.exp +0.8
                    else:
                        pass
                    for j in i.friends:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp + 0.6
                        elif j.level < 4  or j.love > 50:
                            i.exp =i.exp + 0.4
                        elif j.level < 8  or j.love > 30:
                            i.exp =i.exp + 0.2
                        else:
                            pass
                    for j in i.foes:
                        if j.level == 0 or j.love > 80:
                            i.exp = i.exp - 0.6
                        elif j.level < 4 or j.love > 50:
                            i.exp =i.exp - 0.4
                        elif j.level < 8 or j.love > 30:
                            i.exp =i.exp - 0.2
                        else:
                            pass
                
                tags_limitcheck(i)






        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            if randomfz() == my:
                pass
            else:
                zhu = randomfz()
                if zhu.qingxiang < 30 or zhu == my or zhu in juqingfei:
                    pass
                else:
                    bei = randomfz()
                    if bei == my or bei == zhu or bei in juqingfei:
                        pass
                    else:
                        randombattle(zhu,bei)
        else:
            pass
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            if randomfz() == my:
                pass
            else:
                zhu = randomfz()
                if zhu.qingxiang < 30 or zhu == my or zhu in juqingfei:
                    pass
                else:
                    bei = randomfz()
                    if bei == my or bei == zhu or bei in juqingfei:
                        pass
                    else:
                        randombattle(zhu,bei)
        else:
            pass


        tempfzlist = []
        for i in NPC_fz_list:
            if i.level == beifei:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重":
                pass
            elif   tags[4] in i.tags:
                pass
            elif tags_yali[2] in i.tags:
                pass
            elif i == my:
                pass
            else:
                tempfzlist.append(i)
        for i in NPC_fz_list:
            if my in i.foes and i.like > 80:
                i.foes.remove(my)
            if i in i.foes:
                i.foes.remove(i)
            else:
                pass


        for i in tempfzlist:
            if i.anhai["三级"] != 0:
                lucky =renpy.random.randint(0, 50)
                if lucky == 0 and len(i.foes) > 0:
                    fz = renpy.random.choice(i.foes)
                    if fz == i:
                        pass
                    elif fz in juqingfei:
                        pass
                    else:
                        manxingdu.append([fz,i.anhai["三级"]])
                        i.anhai["三级"] = 0
            
            if i.huashu["一A"] != 0:
                lucky =renpy.random.randint(0, 20)
                if lucky == 0:
                    tempfz = renpy.random.choice(tempfzlist)
                    if tempfz == i or fz == i:
                        pass
                    elif tempfz in i.foes :
                        pass
                    elif len(tempfz.foes) == 0:
                        pass
                    else:
                        
                        fz = renpy.random.choice(tempfz.foes)
                        lucky = renpy.random.randint(0,100)
                        tempnum = i.huashu["一A"]*30
                        if lucky <= tempnum and fz not in i.foes:
                            tempfz.foes.remove(fz)
                            tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，在"+i.hao+i.weifen+i.name +"的劝说下，"+tempfz.hao+tempfz.weifen+tempfz.name +"不再与"+fz.hao+fz.weifen+fz.name+"交恶了。\n"
                            allstory.insert(0,tempstory2)
                            tempfz.qingxiang -= i.huashu["一A"]
                        else:
                            pass
            if i.huashu["一B"] != 0:
                lucky =renpy.random.randint(0, 20)
                if lucky == 0:
                    fz = renpy.random.choice(tempfzlist)
                    if fz == i:
                        pass
                    elif fz == my:
                        pass
                    elif fz in i.friends:
                        pass
                    else:
                        fz.health -= (i.anhai["一B"]*2-1)
            
            
            if i.xingge == "娇纵" or i.xingge =="势利":
                lucky =renpy.random.randint(0, 20)
                if lucky == 0:
                    tempfz = renpy.random.choice(tempfzlist)
                    if tempfz == i:
                        pass
                    elif tempfz in i.friends:
                        pass
                    elif tempfz in i.foes:
                        pass
                    else:
                        i.foes.append(tempfz)
                        tempfz.foes.append(i)
                        tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+i.hao+i.weifen+i.name +"与"+tempfz.hao+tempfz.weifen+tempfz.name +"在宫中偶遇，二人话不投机，不欢而散。\n"
                        allstory.insert(0,tempstory2)
                lucky =renpy.random.randint(0, 9)
            if i.xingge == "活泼" or i.xingge =="圆滑":
                lucky =renpy.random.randint(0, 20)
                if lucky == 0:
                    tempfz = renpy.random.choice(tempfzlist)
                    if tempfz == i:
                        pass
                    elif tempfz in i.foes:
                        pass
                    elif tempfz in i.friends:
                        pass
                    else:
                        i.friends.append(tempfz)
                        tempfz.friends.append(i)
                        tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+i.hao+i.weifen+i.name +"与"+tempfz.hao+tempfz.weifen+tempfz.name +"在宫中偶遇，二人相谈甚欢，意犹未尽。\n"
                        allstory.insert(0,tempstory2)







        tempfzlist = []
        for i in NPC_fz_list:
            if i.level == beifei:
                pass
            elif i == my:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重":
                pass
            elif   tags[4] in i.tags:
                pass
            elif tags_yali[2] in i.tags:
                pass
            else:
                tempfzlist.append(i)
        for i in tempfzlist:
            if i.level == 0 or i.qinjunum == 1:
                fz = i
                if i.tequan1 != 0 or i == my:
                    pass
                else:
                    lucky =renpy.random.randint(0, 1)
                    
                    
                    
                    
                    
                    
                    
                    
                    if lucky == 0: 
                        if i.qingxiang >= 75:
                            if len(i.foes) == 0:
                                fz = renpy.random.choice(tempfzlist)
                            else:
                                fz = renpy.random.choice(i.foes)
                        
                        else:
                            if len(i.foes) == 0:
                                fz = i
                            else:
                                fz = renpy.random.choice(i.foes)
                        if fz == i:
                            pass
                        elif fz in i.friends:
                            pass
                        elif fz not in NPC_fz_list:
                            pass
                        elif fz.level <= i.level:
                            pass
                        elif fz.level == beifei - 1:
                            pass
                        elif i.level > 0 and i.qinjunum != fz.qinjunum:
                            pass
                        else:
                            fzgaoweitequan(self = i,fz=fz)
                            for j in tempweifenlist:
                                if weifen_list[j][0] <= fz.level:
                                    tempweifenlist.remove(j)
                                else:
                                    pass
                            if len(tempweifenlist) == 0:
                                pass
                            else:
                                a = renpy.random.choice(tempweifenlist)
                                pretext = str(fz.hao)+str(fz.weifen)+str(fz.name)
                                preweifen = str(fz.weifen)
                                b = int(fz.level)
                                if a <= b :
                                    pass
                                else:
                                    for x in yuanweifen:
                                        if isinstance(x[1],tuple):
                                            if preweifen in x[1]:
                                                y = x[0]
                                                if isinstance(weifen_list[y][1],list) and preweifen not in weifen_list[y][1]:
                                                    weifen_list[y][1].append(preweifen)
                                                else:
                                                    pass
                                        else:
                                            pass
                                    if isinstance(weifen_list[a][1],list):
                                        fz.weifen = renpy.random.choice(weifen_list[a][1])
                                        weifen_list[a][1].remove(fz.weifen)
                                        fz.level = weifen_list[a][0]
                                    else:
                                        fz.weifen = weifen_list[a][1]
                                        fz.level = weifen_list[a][0]
                                    weifen_list[b][5] = weifen_list[b][5]-1
                                    weifen_list[a][5] = weifen_list[a][5]+1
                                    fz.exp = weifen_list[a][3] + (weifen_list[a][4]-weifen_list[a][3])*0.5
                                    tempstory = str(year)+"年"+str(month)+"月，由"+str(i.hao)+str(i.weifen)+str(i.name)+"上请降为"+str(fz.weifen)+"。\n"
                                    tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext+"由"+str(i.hao)+str(i.weifen)+str(i.name)+"上请降为"+str(fz.weifen)+"。\n"
                                    fz.story.append(tempstory)
                                    allstory.insert(0,tempstory2)
                                    changecheng(fz)
                                    if fz not in i.foes:
                                        i.foes.append(fz)
                                    else:
                                        pass
                                    if i not in fz.foes:
                                        fz.foes.append(i)
                                    else:
                                        pass
                                    if b < 4 and a > 3:
                                        fz.tequan1 = -1
                                        Changeqinju(fz)
                                        randompalace(fz)
                                    else:
                                        pass
                                    ChangeGongnv(fz)
                                    i.tequan1 = 6
                                    if fz == my:
                                        renpy.call("被高位降位",self = i,from_current=False)
                                    else:
                                        pass
                    
                    elif lucky == 1:
                        if len(i.friends) == 0:
                            fz == i
                        else:
                            fz = renpy.random.choice(i.friends)
                        if fz == i:
                            pass
                        elif fz not in NPC_fz_list:
                            pass
                        elif fz in i.foes:
                            pass
                        elif fz.level <= i.level:
                            pass
                        elif i.level > 0 and i.qinjunum != fz.qinjunum:
                            pass
                        else:
                            fzgaoweitequan(self = i,fz=fz)
                            for j in tempweifenlist:
                                if weifen_list[j][0] >= fz.level:
                                    tempweifenlist.remove(j)
                                else:
                                    pass
                            if len(tempweifenlist) == 0:
                                pass
                            else:
                                a = renpy.random.choice(tempweifenlist)
                                pretext = str(fz.hao)+str(fz.weifen)+str(fz.name)
                                preweifen = str(fz.weifen)
                                b = int(fz.level)
                                if a >= b :
                                    pass
                                else:
                                    for x in yuanweifen:
                                        if isinstance(x[1],tuple):
                                            if preweifen in x[1]:
                                                y = x[0]
                                                if isinstance(weifen_list[y][1],list) and preweifen not in weifen_list[y][1]:
                                                    weifen_list[y][1].append(preweifen)
                                                else:
                                                    pass
                                        else:
                                            pass
                                    if isinstance(weifen_list[a][1],list):
                                        fz.weifen = renpy.random.choice(weifen_list[a][1])
                                        weifen_list[a][1].remove(fz.weifen)
                                        fz.level = weifen_list[a][0]
                                    else:
                                        fz.weifen = weifen_list[a][1]
                                        fz.level = weifen_list[a][0]
                                    weifen_list[b][5] = weifen_list[b][5]-1
                                    weifen_list[a][5] = weifen_list[a][5]+1
                                    fz.exp = weifen_list[a][3] + (weifen_list[a][4]-weifen_list[a][3])*0.5
                                    tempstory = str(year)+"年"+str(month)+"月，由"+str(i.hao)+str(i.weifen)+str(i.name)+"上请晋为"+str(fz.weifen)+"。\n"
                                    tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext+"由"+str(i.hao)+str(i.weifen)+str(i.name)+"上请晋为"+str(fz.weifen)+"。\n"
                                    fz.story.append(tempstory)
                                    allstory.insert(0,tempstory2)
                                    i.tequan1 = 6 - (i.huashu["一B"] + fz.huashu["一B"])
                                    if b > 3 and a < 4:
                                        Changeqinju(fz)
                                        randompalace(fz)
                                        fz.tequan1 = 0
                                    else:
                                        pass
                                    ChangeGongnv(fz)
                                    changecheng(fz)
                                    if fz == my:
                                        renpy.call("被高位晋位",self = i,from_current=False)
                                    else:
                                        pass
                    else:
                        pass






    $ lucky = renpy.random.randint(0,3)
    if lucky == 0:
        call NPC造谣准备 from _call_NPC造谣准备
    else:
        pass
    python:
        for i in zysj_ready:
            if i.zhu not in NPC_fz_list:
                zysj_ready.remove(i)
            
            elif i.time1 <= 0 or i.jilv >= 100:
                zysj.append(i)
                zysj_ready.remove(i)
                i.time1 = -1
                i.time2 -= 1
                i.bei.tags.append(tags[4])
                if i.way == 0 :
                    temptext = "欺凌宫人"
                    tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，有传闻称"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"在寝宫中随意欺凌宫人，惨叫声令人胆寒，皇帝下令彻查。\n"
                    allstory.insert(0,tempstory2)
                elif i.way == 1 :
                    temptext = "妄议朝政"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，有传闻称"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"不知分寸，妄议朝政，皇帝下令彻查。\n"
                    allstory.insert(0,tempstory2)
                elif i.way == 2 :
                    temptext = "不敬先祖"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，有传闻称"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"大逆不道，不敬先祖，皇帝下令彻查。\n"
                    allstory.insert(0,tempstory2)
                else:
                    pass
                if i.zhu == my:
                    renpy.call("造谣通知_1",self = i,from_current=False)
                elif i.bei == my :
                    renpy.call("造谣通知_2",self = i,from_current=False)
                else:
                    renpy.call("造谣通知_1",self = i,from_current=False)
            else  :
                i.time1 -= 1


        for i in zysj:
            zaoyao_cha(i)
            if i.jilv < 0: 
                i.time2 = -1
                if len(i.hemou) >= 1:
                    temptext2= "等人"
                else:
                    temptext2 = ""
                if i.way == 0 :
                    temptext = "欺凌宫人"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"欺凌宫人一事，经查为"+str(i.zhu.hao)+(i.zhu.weifen)+str(i.zhu.name)+str(temptext2)+"捏造。\n"
                elif i.way == 1 :
                    temptext = "妄议朝政"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"妄议朝政一事，经查为"+str(i.zhu.hao)+(i.zhu.weifen)+str(i.zhu.name)+str(temptext2)+"捏造。\n"
                elif i.way == 2 :
                    temptext = "不敬先祖"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"不敬先祖一事，经查为"+str(i.zhu.hao)+(i.zhu.weifen)+str(i.zhu.name)+str(temptext2)+"捏造。\n"
                else:
                    pass
                allstory.insert(0,tempstory2)
                tempstory =""+str(year)+"年"+str(month)+"月，被"+str(i.zhu.hao)+(i.zhu.weifen)+str(i.zhu.name)+str(temptext2)+"捏造"+str(zyfs[i.way])+"之谣言，但证得清白。\n"
                i.bei.story.append(tempstory)
                tempstory =""+str(year)+"年"+str(month)+"月，在宫中散布谣言，污蔑"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name)+"捏造"+str(zyfs[i.way])+"之谣言，后被查出。\n"
                i.zhu.story.append(tempstory)
                for j in i.hemou:
                    tempstory =""+str(year)+"年"+str(month)+"月，参与"+str(i.zhu.hao)+(i.zhu.weifen)+str(i.zhu.name)+"散布谣言，污蔑"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name)+str(zyfs[i.way])+"之事。\n"
                    j.story.append(tempstory)
                if i.zhu == my:
                    renpy.call("造谣通知_3",self = i,from_current=False)
                elif i.bei == my :
                    renpy.call("造谣通知_4",self = i,from_current=False)
                else:
                    renpy.call("造谣通知_5",self = i,from_current=False)
            elif i.time2 < 1 and i.jilv > 0:
                if i.way == 0 :
                    temptext = "欺凌宫人"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"欺凌宫人一事，经查证据确凿，皇帝大怒。\n"
                elif i.way == 1 :
                    temptext = "妄议朝政"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"妄议朝政一事，经查证据确凿，皇帝大怒。\n"
                elif i.way == 2 :
                    temptext = "不敬先祖"
                    tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(i.bei.hao)+(i.bei.weifen)+str(i.bei.name) +"不敬先祖一事，经查证据确凿，皇帝大怒。\n"
                else:
                    pass
                allstory.insert(0,tempstory2)
                tempstory =""+str(year)+"年"+str(month)+"月，"+str(zyfs[i.way])+"证据确凿，皇帝大怒。\n"
                i.bei.story.append(tempstory)
                if i.zhu == my:
                    for j in i.gn:
                        j.state = "寻常"
                    renpy.call("造谣通知_6",self = i,from_current=False)
                elif i.bei == my :
                    renpy.call("造谣通知_7",self = i,from_current=False)
                else:
                    renpy.call("造谣通知_8",self = i,from_current=False)
            else:
                pass

    $ lucky = renpy.random.randint(0,3)
    if lucky == 0:
        call NPC下毒准备 from _call_NPC下毒准备
    else:
        pass

    python:
        for i in xdsj_ready:
            if i.jieguo == 0:
                xdsj_ready.remove(i)
                if i.zhu == my:
                    renpy.call("下毒无事发生",self = i,from_current=False)
            
            elif i.jieguo == -1:
                i.time1 = -1
                i.time2 -= 1
                i.state = 0
                xdsj.append(i)
                xdsj_ready.remove(i)
                renpy.call("下毒未遂通知",self = i,from_current=False)
            elif i.jieguo == 1:
                xiadu_0(i)
                xdsj.append(i)
                xdsj_ready.remove(i)
                i.time1 = -1
                i.time2 -= 1
                renpy.call("下毒成功通知",self = i,from_current=False)
            else:
                pass


        for i in xdsj:
            xiadu_cha(i)
            if i.zuiren != None: 
                i.time2 = -1
                renpy.call("下毒调查通知",self = i,from_current=False)
            
            elif i.time2 < 1 :
                for j in i.xianyi:
                    if j[1] >= 100:
                        i.zuiren = j[0]
                if i.zuiren != None:
                    
                    i.time2 = -1
                    renpy.call("下毒调查通知",self = i,from_current=False)
                else:
                    xdsj.remove(i)
                    xdsj_end.insert(0,i)
            else:
                pass





    if beizhangze20 == True and beizhangzetime == 0:
        $ beizhangzetime = beizhangzetime  + 1
        if my.health < 500:
            $ my.health = my.health * 0.5
        else:
            $ my.health = (my.health-300) * 0.5
        $ AP = 1
    elif beizhangze20 == True and beizhangzetime < 6:
        $ beizhangzetime = beizhangzetime  + 1
        $ my.health = my.health + my.health*0.2
    elif beizhangze20 == True and beizhangzetime == 6:
        $ beizhangzetime = 0
        $ beizhangze20 = False
        $ my.health = my.health + my.health*0.1
    else:
        pass

    python:
        for i in NPC_fz_list:
            tags_limitcheck(i)
            Feizishengjiang(i)
            if 0 < i <= 3 and diwei(i) != 1 and len(shengyuzhengdian_list) >0:
                a = renpy.random.choice(shengyuzhengdian_list)
                shengyuzhengdian_list.remove(a)
                palaces[a][0][1] = palaces[a][0][1] +1
                palaces[a][1][1] = self
                i.palacenum = i
                i.qinjunum = 1
                i.palace =  palaces[a][0][0]
                i.qinju =  palaces[a][1][0]
            
            if i.hao == "":
                i.cheng = i.xing + i.weifen
            else:
                i.cheng = i.hao + i.weifen


    if usepoison02 == 1:
        python:
            for j in my.tags:
                if "身怀皇嗣" in j:
                    j[1] = 0
                    my.tags.remove(j)
            usepoison02 = 0
            my.state = "抱恙"
            my.huaiyun = 0
            my.health = (my.health-100)*0.8
            xiluo.append([my,"小产"])
            renpy.call("不幸小产",fz = my,from_current=False)
    else:
        pass
    if suicide == 1:
        $ suicide = 0
        jump 非正常死亡
    else:
        pass
    python:
        templist = []
        for i in NPC_fz_list:
            templist.append(i)
        for i in NPC_fz_feilist:
            templist.append(i)


        for i in templist:
            
            
            tempnum = round(i.health*3+i.xinji+i.lucky*3-i.love*i.level*0.5)
            
            if tempnum < 100 :
                tempnum = 100
            else:
                pass
            lucky = renpy.random.randint(0,tempnum*2)
            if i in juqingfei :
                lucky = 1
            
            if i.health < -99:
                lucky = 0
            elif i.health < 0:
                lucky = renpy.random.randint(0,1)
            
            if player == 1 and i == sidi:
                lucky = 1
            if i.age > int(i.shou):
                lucky = 0
            if i.age == int(i.shou):
                lucky = renpy.random.randint(0,20)
            
            
            if lucky == 0 : 
                lucky = renpy.random.randint(0,10)
                if i.level == beifei:
                    if i in lenggong:
                        lenggong.remove(i)
                    else:
                        pass
                    if i != my:
                        tempstory = str(year)+"年"+str(month)+"月，在冷宫身亡。\n"
                        tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，冷宫罪妃"+str(i.name)+ "身亡。\n"
                        Killfz(i)
                        renpy.call("有人死了",fz = i,from_current=False)
                    else:
                        pass
                elif i.age >= int(i.shou) :
                    if i != my:
                        tempstory = str(year)+"年"+str(month)+"月，于寝殿内寿终正寝。\n"
                        tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(i.hao)+str(i.weifen)+str(i.name)+ "于寝殿内寿终正寝。\n"
                        Killfz(i)
                        renpy.call("有人死了",fz = i,from_current=False)
                    
                    else:
                        renpy.jump("寿终正寝")
                elif i.health < 0:
                    if i != my:
                        tempstory = str(year)+"年"+str(month)+"月，因身体虚弱，久病不愈，病故。\n"
                        tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(i.hao)+str(i.weifen)+str(i.name)+ "，因身体虚弱而病故。\n"
                        Killfz(i)
                        renpy.call("有人死了",fz = i,from_current=False)
                    else:
                        pass
                elif i.health < 300 and i != my:
                    tempstory = str(year)+"年"+str(month)+"月，因身患隐疾发作，病故。\n"
                    tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(i.hao)+str(i.weifen)+str(i.name)+ "，因身患隐疾发作，病故。\n"
                    Killfz(i)
                    renpy.call("有人死了",fz = i,from_current=False)
                elif 0 < i.familylevel < 4 and lucky < 4 and i != my and len(i.sisters) == 0:
                    i.family = "罪臣之女"
                    tempstory = str(year)+"年"+str(month)+"月，因家族重罪自裁于寝宫。\n"
                    tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(i.hao)+str(i.weifen)+str(i.name)+ "，因家族重罪自裁于寝宫。\n"
                    guanyuan_list.remove(i.father)
                    Killfz(i)
                    renpy.call("有人死了",fz = i,from_current=False)
                elif i != my:
                    tempstory = str(year)+"年"+str(month)+"月，突发疾病，不治身亡。\n"
                    tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(i.hao)+str(i.weifen)+str(i.name)+ "，突发疾病，不治身亡。\n"
                    Killfz(i)
                    renpy.call("有人死了",fz = i,from_current=False)
                else:
                    pass
            
            else :
                pass

    return



label 临时事件检测:
    hide screen myroom


    if xuanxiutime == 36 and timenum == 1 and jinzu(my) != True:
        if my.level == 0 or NPC_fz_list[0] == my:

            $ bg("寝居")
            show 赵公公 at chara
            赵公公 "参见[my.cheng]，今日乃是选秀之日。按例，该由您陪同皇上，莅临殿选。"
            hide 李公公
            menu:
                "前往储秀宫":
                    pass
            scene 储秀宫
            with dissolve
            show screen notify("储秀宫")
            $ NPC_newfz_list = []
            $ Creat_Xiunv(10)

            $ xuanxiutime = 0
            $ ruxuan = []
            python:
                for i in NPC_newfz_list:
                    tempbool1 = False
                    tempbool2 = False
                    renpy.call("秀女觐见",fz = i,from_current=True)



            if len(ruxuan) == 0:
                "选秀结束，无人入选。"
                $ tempstory = "【大事】"+str(year)+"年"+str(month)+"月，新秀入宫，但无人入选\n"
            else:
                $ tempnum = len(ruxuan)
                "选秀结束，共[tempnum]人入选。"
                $ tempstory = "【大事】"+str(year)+"年"+str(month)+"月，新秀入宫，共"+str(tempnum)+"人。\n"
            python:
                for i in ruxuan:
                    Xiunv_cefeng(i)
            $ allstory.insert(0,tempstory)
            $ bg("寝居")
        else:




            $ NPC_newfz_list = []
            $ global weifen_list
            $ xiunvnum = renpy.random.randint(4,7)
            $ Creat_Feizi(xiunvnum,1)
            $ xuanxiutime = 0
            $ tempstory = "【大事】"+str(year)+"年"+str(month)+"月，新秀入宫，共"+str(xiunvnum)+"人。\n"
            $ allstory.insert(0,tempstory)
            "选秀之日已至，又有数名新秀入宫。"
    else:

        pass



    if timenum == 1:
        python:
            for i in NPC_Kids_list:
                if i.age >= 16 and i.wen > 50 and i.wu > 50 and i.hdlike < 50 and i.live == 0:
                    Kids_fenghao(i)
                    i.plan = "顺其自然"
                    Kids_hunpei_HD(i)
                    i.live = 1
                
                elif i.age >= 18 and i.hdlike >= 80 and i.live == 0:
                    lucky = renpy.random.randint(0,100)
                    if lucky  == 0:
                        Kids_fenghao(i)
                        i.plan = "顺其自然"
                        Kids_hunpei_HD(i)
                        i.live = 1
                else:
                    pass
                if i.age > 18 and i.live == 0:
                    Kids_fenghao(i)
                    i.plan = "顺其自然"
                    Kids_hunpei_HD(i)
                    i.live = 1
                else:
                    pass
    else:
        pass






    if my.love > 20 and my.shiqin > 0 and my.level !=beifei and money < 100 and hdxingge == "冷漠":
        $ lucky = round(my.love*0.25)
        $ lucky = renpy.random.randint(0, 100-lucky)
        if lucky == 0:
            show 我的宫女 at chara
            我的宫女 "[my.cheng]，方才圣宸宫那里送来了些银两，说是给咱们补贴宫用。"
            "获得了一百两银子。"
            $ money += 100
            hide 我的宫女
        else:
            pass

    elif my.love > 20 and my.shiqin > 0 and my.level !=beifei and money < 100 and hdxingge == "温柔":
        $ lucky = round(my.love*0.25)
        $ lucky = renpy.random.randint(0, 100-lucky)
        if lucky == 0:
            show 我的宫女 at chara
            我的宫女 "[my.cheng]，方才圣宸宫那里送来了些银两，说是给咱们补贴宫用。"
            "获得了一百两银子。"
            $ money += 100
            hide 我的宫女
        else:
            pass
    else:
        pass

    if my.love > 20 and my.shiqin > 0 and my.level !=beifei:
        $ lucky = round(my.love*0.4)
        if [my,"怀孕"] in gongxi:
            $ lucky = lucky + 5
        elif [my,"生产"] in gongxi:
            $ lucky = lucky + 5
        elif [my,"晋位"] in gongxi:
            $ lucky = lucky + 5
        elif huaiyun(my) == True:
            $ lucky = lucky + 3
        else:
            pass
        $ lucky = renpy.random.randint(0, 100-lucky)
        if lucky == 0:
            if my.level == 0:
                $ yucilist = presents + presents_hign
            elif my.level < 4:
                $ yucilist = presents
                $ yucilist = presents + presents
            elif my.level < 8:
                $ yucilist = presents + presents_low + presents_hign
            elif my.level < 12:
                $ yucilist = presents + presents_low
            else:
                $ yucilist = presents + presents_low + presents_low
            $ lucky =  renpy.random.randint(1, 3)
            if mapname == "寝居":
                $ bg("寝居")
            else:
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
            show 我的宫女 at chara
            if lucky == 1:
                $ yuci1 = renpy.random.choice(yucilist)
                $ kufang.append(yuci1)
                我的宫女 "[my.cheng]，方才圣宸宫那里送来了些赏赐，已经为您收进库房了。"
                hide 我的宫女
                "得到了[yuci1.name]×1。"

            elif lucky == 2:
                $ yuci1 = renpy.random.choice(yucilist)
                $ yuci2 = renpy.random.choice(yucilist)
                $ kufang.append(yuci1)
                $ kufang.append(yuci2)
                我的宫女 "[my.cheng]，方才圣宸宫那里送来了些赏赐，已经为您收进库房了。"
                hide 我的宫女
                "得到了[yuci1.name]×1、[yuci2.name]×1。"
            else:

                $ yuci1 = renpy.random.choice(yucilist)
                $ yuci2 = renpy.random.choice(yucilist)
                $ yuci3 = renpy.random.choice(yucilist)
                $ kufang.append(yuci1)
                $ kufang.append(yuci2)
                $ kufang.append(yuci3)
                我的宫女 "[my.cheng]，方才圣宸宫那里送来了些赏赐，已经为您收进库房了。"
                hide 我的宫女
                "得到了了[yuci1.name]×1、[yuci2.name]×1、[yuci3.name]×1。"
        else:
            pass
    else:
        pass


    python:
        tempfzlist = []
        for i in NPC_fz_list:
            if i.level == beifei:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重":
                pass
            elif   tags[4] in i.tags:
                pass
            elif tags_yali[2] in i.tags:
                pass
            elif i == my:
                pass
            elif i.like <= 30 and i.xingge != "娇纵":
                pass
            elif i.like < 50:
                pass
            else:
                tempfzlist.append(i)
    if len(tempfzlist) == 0 or my.level ==beifei:
        pass
    else:
        $ lucky = len(tempfzlist)*3
        if [my,"怀孕"] in gongxi:
            $ lucky = lucky + 25
        elif [my,"生产"] in gongxi:
            $ lucky = lucky + 25
        elif [my,"晋位"] in gongxi:
            $ lucky = lucky + 25
        else:
            pass
        $ lucky = renpy.random.randint(0, 100-lucky)
        if lucky == 0:
            $ fz = renpy.random.choice(tempfzlist)
            if fz.level == 0:
                $ liwulist = presents + presents_hign
            elif fz.level < 4:
                $ liwulist = presents
                $ liwulist = presents + presents
            elif fz.level < 8:
                $ liwulist = presents + presents_low + presents_hign
            elif fz.level < 12:
                $ liwulist = presents + presents_low
            else:
                $ liwulist = presents + presents_low + presents_low
            $ liwu = renpy.random.choice(liwulist)
            $ kufang.append(liwu)
            if mapname == "寝居":
                $ bg("寝居")
            else:
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
            show 我的宫女 at chara

            我的宫女 "[my.cheng]，方才[fz.palace]的[fz.cheng]给您送了一件[liwu.name]，已经为您收进库房了。"
            hide 我的宫女
            "得到了[liwu.name]×1。"
        else:

            pass


    if my.love > 50 or my.familylevel < 4 or my.year < 3 and my.love > 0:
        $ lucky = round(my.love*0.1)
        $ lucky = renpy.random.randint(0, 60-lucky)
        if lucky == 0 and mapname== "寝居" and jinzu(my) == False:
            python:
                tempfzlist = []
                for i in NPC_fz_list :
                    list2 = []
                    for j in i.foes:
                        if j in my.friends:
                            list2.append(j)
                        else:
                            pass
                    if i == my:
                        pass
                    elif i.qingxiang <30:
                        pass
                    elif i.xingge == "清冷":
                        pass
                    elif i.like < 0:
                        pass
                    elif len(list2) >= 2:
                        pass
                    elif   tags[4] in i.tags:
                        pass
                    elif tags_yali[2] in i.tags:
                        pass
                    
                    elif i in my.friends :
                        pass
                    elif i in my.foes:
                        pass
                    elif i.state == "病重" or jinzu(i) == True or i.state == "抱恙":
                        pass
                    else:
                        tempfzlist.append(i)
                    global tempfzlist
            if len(tempfzlist) == 0:
                pass
            else:
                $ fz = renpy.random.choice(tempfzlist)
            if fz == my or fz in my.friends or fz in my.foes or fz not in NPC_fz_list or fz in juqingfei:
                pass
            else:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "主子，[fz.cheng]来了。"
                if my.level >= fz.level:
                    $ temptext = "前去迎接"
                else:
                    $ temptext = "让她进来"
                menu:
                    "推脱不见" if fz.level > my.level:
                        我的宫女 "是。"
                        hide 我的宫女
                        if fz.xingge == "娇纵" and fz.xinji < 300:
                            "没过多久，[my.Gongnv[0].name]前来回禀，[fz.cheng]已经离开了，面色似乎有些难看……"
                            $ fz.like = fz.like - 10
                        elif fz.xingge == "势利" and fz.xinji < 300:
                            "没过多久，[my.Gongnv[0].name]前来回禀，[fz.cheng]已经离开了，临走前也是恭恭敬敬的，还说改日再来拜访。"
                            $ fz.like = fz.like - 10
                        else:
                            $ fz.like = fz.like - 5
                    "[temptext]":
                        hide 我的宫女
                        show fz at chara with dissolve
                        if my.level >= fz.level:
                            我 "[fz.cheng]安，今日怎么有空上这[my.qinju]来了？"
                            "[fz.hao][fz.weifen] [fz.name]" "（微笑落座）[my.cheng]不必多礼，本宫也只是闲来无事，过来看看。"
                            "[fz.cheng]始终面带笑容，言辞款款，表面上客气寒暄，却隐隐有想要拉拢你的心思……"
                        else:
                            "[fz.hao][fz.weifen] [fz.name]" "嫔妾给[my.cheng]请安。"
                            我 "[fz.cheng]今日前来，所为何事？"
                            "[fz.cheng]始终面带笑容，言辞款款，表面上客气寒暄，却隐隐有想要投靠于你的心思……"
                        if my.love > 50 and my.level > 4:
                            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]深得皇上喜爱，假日时日，不愁在宫中没有立足之地。若能生下皇嗣，那福气可真叫人羡慕不来呢。"
                        elif my.familylevel < 4 and my.level < 4:
                            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]出身高贵，一眼看着便是个高华不俗之人，旁人学都不学来。也难怪皇上敬重你呢。"
                        elif my.familylevel < 4:
                            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]出身高贵，一眼看着便是个高华不俗之人，假以时日，在宫里稳住了地位，皇上自然也会敬重你呢。"
                        else:
                            pass
                        if my.level >= fz.level:
                            $ temptext = "本宫"
                            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]是聪明人，应当知道，在这宫里多一份倚靠，便多一条生路，也多一条退路，不是么？"
                        else:
                            $ temptext = "嫔妾"
                            "[fz.hao][fz.weifen] [fz.name]" "嫔妾在宫里孤苦无依，只想为自己寻个倚仗，也多了几分指望。"
                        menu:
                            "闪烁其词":
                                if fz.xingge != "势利":
                                    $ fz.like = fz.like - 5

                                    "[fz.hao][fz.weifen] [fz.name]" "……是[temptext]唐突了，[my.cheng]不必放在心上。"
                                    "[fz.hao][fz.weifen] [fz.name]" "[temptext]不打扰[my.cheng]了，这便告辞。"
                                else:
                                    $ fz.like = fz.like - 10
                                    "[fz.hao][fz.weifen] [fz.name]" "（压低了声音）哼，惺惺作态之人……最是可恨。算我看走了眼！"
                                    "[fz.hao][fz.weifen] [fz.name]" "[temptext]不打扰[my.cheng]了，这便告辞。"
                                hide fz with dissolve
                                $ timenum = timenum +1
                                $ AP = AP -1
                                $ fz.AP -= 1
                            "当即拒绝":
                                if fz.xingge == "娇纵":
                                    "[fz.hao][fz.weifen] [fz.name]" "（压低了声音）哼，瞧不起谁呢……"
                                    $ fz.like = fz.like - 10
                                elif fz.xinji < 300:
                                    $ fz.like = fz.like - 5
                                    "（[fz.cheng]似是一愣，随即站起身来）既然如此那[temptext]自是不敢强求，只希望来日[my.cheng]不要后悔。"
                                    "[fz.hao][fz.weifen] [fz.name]" "[temptext]告辞。"
                                else:
                                    $ fz.like = fz.like - 5
                                    "既然如此那[temptext]自是不敢强求，只不过还是有些惋惜罢了……"
                                    "[fz.hao][fz.weifen] [fz.name]" "[temptext]告辞。"
                                hide fz with dissolve
                                $ timenum = timenum +1
                                $ AP = AP -1
                                $ fz.AP -= 1
                            "欣然答应":

                                if fz.xinji < 300:
                                    $ fz.like = fz.like +15
                                    if my.level >= fz.level:
                                        "[fz.hao][fz.weifen] [fz.name]" "（喜不自胜）往后你我相互倚仗，在宫里再也没有什么可怕的了。"
                                    else:
                                        "[fz.hao][fz.weifen] [fz.name]" "（喜不自胜）嫔妾多谢[my.cheng]赏识！往后必定为您当牛做马，赴汤蹈火！"
                                else:
                                    $ fz.like = fz.like +10
                                    "[fz.hao][fz.weifen] [fz.name]" "（喜不自胜）[temptext]早就知道，[temptext]与[my.cheng]必然是合得来的。"
                                    "[fz.hao][fz.weifen] [fz.name]" "至于之后的事情，还得从长计议。"
                                python:
                                    for i in fz.foes:
                                        i.like -= 5
                                "（与[fz.cheng]结怨的妃嫔对你的好感下降了。）"
                                "[fz.hao][fz.weifen] [fz.name]" "时候不早了，[temptext]先告辞了。"
                                hide fz with dissolve
                                $ my.friends.append(fz)
                                $ fz.friends.append(my)
                                $ timenum = timenum +1
                                $ AP = AP -1
                                $ fz.AP -= 1
    else:

        pass


    if my.love > 30 and my.level > 4 and my.state !="病重"  and mapname== "寝居" and jinzu(my) == False:
        $ lucky = round(my.love*0.1)
        $ lucky = renpy.random.randint(0, 15-lucky)
        if lucky == 0:
            python:
                tempfzlist = []
                for i in NPC_fz_list:
                    if i.level == beifei:
                        pass
                    elif jinzu(i) == True:
                        pass
                    elif i.state == "病重":
                        pass
                    elif   tags[4] in i.tags:
                        pass
                    elif tags_yali[2] in i.tags:
                        pass
                    elif i.qingxiang <= 30:
                        pass
                    elif i.xingge == "清冷" or i.xingge == "安静" or i.xingge == "温婉" :
                        pass
                    elif i.like > 20:
                        pass
                    elif i in my.friends :
                        pass
                    elif i.level > my.level:
                        pass
                    elif i == my:
                        pass
                    else:
                        pass



            if len(tempfzlist) == 0:
                pass
            else:
                $ fz = renpy.random.choice(tempfzlist)
            if len(tempfzlist) == 0 or fz.level >= my.level or fz.level >4 or fz.like > 20 or fz in my.friends or fz not in NPC_fz_list:
                pass
            else:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "主子，[fz.cheng]来了。"

                menu:
                    "前去迎接":
                        $ timenum = timenum +1
                        $ AP = AP -1
                        $ fz.AP -= 1
                        hide 我的宫女
                        show fz at chara with dissolve

                        我 "[fz.cheng]安，今日怎么有空上这[my.qinju]来了？"
                        "[fz.hao][fz.weifen] [fz.name]" "（微笑落座）免礼，本宫听说[my.cheng]最近很得皇上欢心呢。"
                        menu:
                            "故意炫耀":
                                $ my.xinji = my.xinji -10
                                if my.love < fz.love:
                                    我 "皇上最近的确对嫔妾多有垂爱呢。不过娘娘也不是无宠之人，今日总不是来责问嫔妾夺去您宠爱的吧？"
                                elif my.huaiyun > 1:
                                    我 "嫔妾如今有了身子，皇上自然宠爱嫔妾。难道娘娘还要为此责问嫔妾么？"
                                elif len(my.kids)>0:
                                    我 "嫔妾养育皇嗣有功，皇上自然会对嫔妾多上点心喏。难道娘娘还要为此责问嫔妾么？"
                                else:
                                    我 "皇上最近的确对嫔妾多有垂爱呢。难道娘娘还要为此责问嫔妾么？。"
                                "[fz.hao][fz.weifen] [fz.name]" "（冷笑）你！你这是在挑衅本宫？！"
                                我 "嫔妾不敢呢。"
                                if fz.level == 0 or fz.palace == my.palace and fz.level < 4 and fz.xinji > 400:
                                    "[fz.hao][fz.weifen]-[fz.name]" "好你个[my.cheng]，仗着自己得宠居然如此骄横！若皇上再宠你几日，岂不是要翻了天了？！"
                                    "[fz.hao][fz.weifen]-[fz.name]" "来人，传本宫的命令，[my.cheng]以下犯上，视宫规为无物，即日起禁足三月。"
                                    "[fz.hao][fz.weifen]-[fz.name]" "（说完，愤然离开。）"
                                    hide fz
                                    if my.love > 50 and my.love > fz.love and hdxingge != "刚正" and hdxingge !="冷漠"  and hdxingge !="腹黑":
                                        "片刻后……"
                                        show 我的宫女 at chara
                                        我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                                        我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                                        $ fz.like = fz.like - 5
                                        $ fz.love = fz.love - 2
                                        hide 我的宫女
                                        jump 寝居界面
                                    elif my.love > 80 and my.love > fz.love and hdxingge != "温柔" and hdxingge !="风流":
                                        "片刻后……"
                                        show 我的宫女 at chara
                                        我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                                        我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                                        $ fz.like = fz.like - 5
                                        $ fz.love = fz.love - 5
                                        hide 我的宫女
                                        jump 寝居界面
                                    else:
                                        $ my.tags.append(["禁足三月",0,""])
                                        $ my.jinzu = 1
                                        jump 寝居界面
                                elif fz.xinji < 400:
                                    "[fz.hao][fz.weifen]-[fz.name]" "不敢？我看你什么都敢！若皇上再宠你几日，岂不是要翻了天了？！"
                                    "[fz.hao][fz.weifen]-[fz.name]" "来人，传本宫的命令，[my.cheng]以下犯上，掌嘴二十！"
                                    hide fz
                                    show 我的宫女 at chara
                                    我的宫女 "[fz.cheng]娘娘，不可啊！"
                                    我的宫女 "（一把被[fz.cheng]的宫女推开）啊！娘娘，您若毁了[my.cheng]的脸，她如何侍奉皇上？到时候皇上怪罪下来……"
                                    hide 我的宫女
                                    show fz at chara
                                    "[fz.hao][fz.weifen]-[fz.name]" "闭嘴！侍奉皇上？她也配？！"
                                    hide fz
                                    "[fz.cheng]的宫女走上前来，说了声“得罪了，[my.cheng]”，便狠狠地掌掴起你来。"
                                    "很快，你的脸就高高肿起，惨不忍睹。"
                                    show fz at chara
                                    "[fz.hao][fz.weifen]-[fz.name]" "呵呵呵，真漂亮，希望皇上以后还会宠爱你。（说完，得意地离开。）"
                                    hide fz
                                    show 我的宫女 at chara
                                    我的宫女 "主子，您没事吧……（心疼不已）[fz.cheng]这也太过分了！"
                                    $ my.beauty = my.beauty - 100
                                    $ my.health = my.health -20
                                    if my.love > fz.love or hdxingge == "刚正" or hdxingge == "温柔":
                                        "片刻后……"
                                        show 我的宫女 at chara
                                        我的宫女 "主子，皇上知道您被[fz.cheng]娘娘掌嘴的事情了。"
                                        我的宫女 "皇上心疼您，觉得[fz.cheng]实在是小肚鸡肠，已经狠狠地斥责了她，还令她禁足三月，闭门思过呢。"
                                        我的宫女 "不过……只怕她以后是更嫉恨您了。"
                                        我的宫女 "对了，皇上还赐了[medic02.name]给咱们呢。主子您赶紧用了，容颜很快就能恢复了！"
                                        "得到[medic02.name]×1。"
                                        $ kufang.append(medic02)
                                        $ fz.like = fz.like - my.love*0.2
                                        $ fz.foes.append(my)
                                        $ my.foes.append(fz)
                                        $ fz.tags.append(["禁足三月",0,""])
                                        $ fz.love = fz.love - my.love*0.1
                                        hide 我的宫女
                                        jump 寝居界面
                                    else:
                                        pass
                                else:

                                    hide fz
                            "大方承认":

                                if my.love < fz.love:
                                    我 "如今皇上宠爱嫔妾，但也比不过您的圣恩浓厚啊。"
                                elif my.huaiyun > 1:
                                    我 "嫔妾如今有了身子，皇上才多上心了几分罢了。"
                                elif len(my.kids)>0:
                                    我 "嫔妾有幸养育皇嗣，皇上才多上心了几分罢了。"
                                else:
                                    我 "能得皇上宠爱，嫔妾自知是三生修来的福分了。"
                                "[fz.hao][fz.weifen] [fz.name]" "（冷笑）皇上宠爱你，是你的福气，至于这福气能在手里捏多久，可就要看你的本事了。"
                                我 "嫔妾谨遵[fz.cheng]教诲。"
                                "[fz.hao][fz.weifen] [fz.name]" "好了，本宫本便是顺路过来看看，眼下还有事，便离了。"
                                我 "恭送[fz.cheng]。"
                                hide fz
                            "谦卑否认":

                                $ my.xinji = my.xinji + 10
                                if my.love < fz.love:
                                    我 "娘娘说笑了，嫔妾蒲柳之姿，又如何与您相比呢？皇上到底对您更为上心，至于嫔妾，不过是图个新鲜罢了。"
                                elif my.huaiyun > 1:
                                    我 "娘娘说笑了，嫔妾蒲柳之姿，又如何与您相比呢？不过嫔妾如今有了身子，皇上才多上心了几分罢了。"
                                elif len(my.kids)>0:
                                    我 "娘娘说笑了，嫔妾蒲柳之姿，又如何与您相比呢？不过嫔妾有幸养育皇嗣，皇上才多上心了几分罢了。"
                                else:
                                    我 "娘娘说笑了，皇上不过对嫔妾不过是图个新鲜，比不上您在宫中美誉传遍，更得皇上敬重呢。"
                                "[fz.hao][fz.weifen] [fz.name]" "你倒还算是有点自知之明。"
                                if fz.level == 0 or fz.palace == my.palace and fz.level < 4 and fz.xinji < 400:
                                    "[fz.hao][fz.weifen]-[fz.name]" "（冷笑着压低了声音）惺惺作态……就是用这副可怜兮兮的面孔去勾引皇上的？"
                                    "[fz.hao][fz.weifen]-[fz.name]" "啧，既然你如此有自知之明，就该好好待在宫里，能到有资格陪伴皇上之后再承宠，不是吗？"
                                    "[fz.hao][fz.weifen]-[fz.name]" "来人，传本宫的命令，[my.cheng]以下犯上，视宫规为无物，即日起禁足三月。"
                                    "[fz.hao][fz.weifen]-[fz.name]" "（说完，愤然离开。）"
                                    hide fz
                                    if my.love > 50 and my.love > fz.love and hdxingge != "刚正" and hdxingge !="冷漠"  and hdxingge !="腹黑":
                                        "片刻后……"
                                        show 我的宫女 at chara
                                        我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                                        我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                                        $ fz.like = fz.like - 5
                                        $ fz.love = fz.love - 2
                                        hide 我的宫女
                                        jump 寝居界面
                                    elif my.love > 80 and my.love > fz.love and hdxingge != "温柔" and hdxingge !="风流":
                                        "片刻后……"
                                        show 我的宫女 at chara
                                        我的宫女 "主子，皇上知道您被[fz.cheng]娘娘禁足的事情了。"
                                        我的宫女 "皇上心疼你，觉得[fz.cheng]大题小做，已经免了您的禁足了。"
                                        $ fz.like = fz.like - 5
                                        $ fz.love = fz.love - 5
                                        hide 我的宫女
                                        jump 寝居界面
                                    else:
                                        $ my.tags.append(["禁足三月",0,""])
                                        $ my.jinzu = 1
                                        jump 寝居界面
                                else:
                                    hide fz
    else:




        pass



    if my.level != beifei and jinzu(my) == False:
        $ lucky = renpy.random.randint(0, 100)
        if lucky <= 2:
            python:
                tempfzlist = []
                for i in NPC_fz_list:
                    if i.level == beifei:
                        pass
                    elif jinzu(i) == True:
                        pass
                    elif i.state == "病重":
                        pass
                    elif   tags[4] in i.tags:
                        pass
                    elif tags_yali[2] in i.tags:
                        pass
                    elif i.level >= my.level:
                        pass
                    elif i.like >= -20:
                        pass
                    elif i not in my.foes and my in i.friends:
                        pass
                    elif i == my:
                        pass
                    else:
                        tempfzlist.append(i)

            if len(tempfzlist) == 0:
                pass
            else:
                $ fz = renpy.random.choice(tempfzlist)
                show 我的宫女 at chara
                我的宫女 "主子，[fz.cheng]传您过去呢。"
                menu:
                    "前往":
                        pass
                scene 妃嫔寝居内
                show screen notify(fz.palace+fz.qinju)
                show fz at chara
                我 "给[fz.cheng]请安。"
                $ lucky = renpy.random.randint(0, 2)
                if lucky == 0:
                    妃子 "（并不看你，同贴身侍女说这话）这茶凉了，替本宫换壶新的。"
                    "（宫女很快换上了新茶。一来一回，你仍屈膝站在殿内。）"
                    menu:
                        "噤声站定":
                            妃子 "（淡淡看你一眼，眼底带着笑意）瞧本宫这记性，怎忘了[my.cheng]还站在这儿呢？快，赐座吧。"
                            妃子 "站了这么久也没个声儿气，若传出去，还说本宫苛待了你。"
                            妃子 "[my.cheng]，本宫当真不是有意的，你不会放在心上吧？"
                            menu:
                                "自然不会":
                                    $ my.yali += 10
                                    妃子 "嗯，那便好。别叫本宫听到宫里有什么风言风语。"
                                    妃子 "否则，拿你是问。"
                                    $ timenum = timenum +1
                                    $ AP = AP -1
                                    $ fz.AP -= 1
                                "不是有意的？" if my.xinji<200:
                                    $ my.yali += 10
                                    妃子 "哦，你觉得本宫有意刁难你，是么？"
                                    妃子 "[my.cheng]，谁给了你胆儿，以下犯上，质问本宫？"
                                    妃子 "来人，给本宫备好笔墨。"
                                    妃子 "[my.cheng]就在这里，给本宫将宫规抄写十遍，抄完方可离开。"
                                    $ timenum = timenum +2
                                    $ AP = AP -2
                                    $ fz.AP -= 1
                                "发起争锋":
                                    call battle (fz=fz) from _call_battle
                                    $ timenum = timenum +1
                                    $ AP = AP -1
                                    $ fz.AP -= 1
                        "出言提醒":















                            妃子 "（面带怒色）本宫没道免礼，有你说话的份儿吗？"
                            妃子 "本宫为何不叫你起来，你不知？"
                            menu:
                                "嫔妾知错":
                                    $ my.yali += 5
                                    妃子 "啧，好一副委屈巴巴的样儿啊。"
                                    妃子 "既然知错，那边要知错就改。别让本宫听到宫里有什么风言风语，说本宫无事苛待了你。"
                                    $ timenum = timenum +1
                                    $ AP = AP -1
                                    $ fz.AP -= 1
                                "嫔妾不知":
                                    $ my.yali += 10
                                    妃子 "不知？不知那便继续在这里站着，想好了再答吧。"
                                    妃子 "本宫没免了你的礼数，[my.cheng]可别站直咯，否则，那就是以下犯上，该按照宫规伺候了。"
                                    妃子 "（懒懒）本宫乏了。（唤来宫女）扶本宫进殿小憩。"
                                    $ timenum = timenum +2
                                    $ AP = AP -2
                                    $ fz.AP -= 1
                                "发起争锋":
                                    call battle (fz=fz) from _call_battle_1
                                    $ timenum = timenum +1
                                    $ AP = AP -1
                                    $ fz.AP -= 1














                elif lucky == 1:
                    妃子 "（笑意盈盈的看着你）[my.cheng]来啦？喏，来尝尝本宫这儿的绿豆酥。"
                    "不等你回答，宫人已经将小碟子送到了你的面前。"
                    menu:
                        "隐忍吃下":
                            我 "（难吃至极。）"
                            $ my.yali += 20
                        "发起争锋":
                            call battle (fz=fz) from _call_battle_2
                            $ timenum = timenum +1
                            $ AP = AP -1
                            $ fz.AP -= 1















                    $ timenum = timenum +1
                    $ AP = AP -1
                    $ fz.AP -= 1
                elif lucky == 2:
                    $ my.yali += 5
                    妃子 "[my.cheng]免礼，赐座。"
                    "有一句每一句地同你闲聊着，言辞中却极尽凉薄讽刺。"
                    if huaiyun(my) != True and len(my.kids) == 0 and huaiyun(fz) == True:
                        妃子 "唉，这肚子大了，整个人都不爽利了。"
                        妃子 "不过一想到有些人求也求不来这样的福气，便又觉得舒坦多了。"
                    elif my.familylevel - fz.familylevel > 3:
                        妃子 "本宫记得，[my.cheng]似乎是[my.family]？"
                        妃子 "哟，那岂不是还比不上本宫的宫女[fz.Gongnv[0].name]么？"
                    elif fz.love - my.love > 20:
                        妃子 "其实本宫早就想找[my.cheng]过来聊聊，只是皇上时常过来探望，本宫很难得空。"
                        妃子 "咳，本宫无疑炫耀，[my.cheng]可别放在心上。"
                    elif fz.beauty - my.beauty > 100:
                        妃子 "[my.cheng]得空也该多捯饬捯饬自己呀，这副样子皇上见了是不会喜欢的。"
                        妃子 "要不要本宫送你些胭脂水粉？"
                        妃子 "噢，不过即便和本宫用同样的胭脂，你大抵也比不上本宫的。"
                    elif fz.qizhi - my.qizhi >100:
                        妃子 "身为后妃，体态仪度最是马虎不得。"
                        妃子 "[my.cheng]，你也该好好学着点。"
                    else:
                        pass
                    menu:
                        "隐忍不言":
                            妃子 "（煞是得意。）"
                            $ fz.yali -= 10
                            $ my.yali += 10
                        "发起争锋":
                            call battle (fz=fz) from _call_battle_3
                            $ timenum = timenum +1
                            $ AP = AP -1
                            $ fz.AP -= 1














                    $ timenum = timenum +1
                    $ AP = AP -1
                    $ fz.AP -= 1
                hide fz
                $ bg("寝居")
        elif lucky == 3:
            python:
                tempfzlist = []
                for i in NPC_fz_list:
                    if i.level == beifei:
                        pass
                    elif jinzu(i) == True:
                        pass
                    elif i.state == "病重":
                        pass
                    elif   tags[4] in i.tags:
                        pass
                    elif tags_yali[2] in i.tags:
                        pass
                    elif i.level >= my.level:
                        pass
                    elif i.level != 0 or i.qinjunum != 1 or i.palacenum != my.palacenum :
                        pass
                    elif i.like >= -20:
                        pass
                    elif i not in my.foes and my in i.friends:
                        pass
                    elif i == my:
                        pass
                    else:
                        tempfzlist.append(i)
                tempgnlist = []

                for i in my.Gongnv:
                    if i.state != "寻常":
                        pass
                    elif i.level == "婢子":
                        tempgnlist.append(i)
                    else:
                        pass


            if len(tempfzlist) == 0 or len(tempgnlist)== 0:
                pass
            else:
                $ fz = renpy.random.choice(tempfzlist)
                $ gn = renpy.random.choice(tempgnlist)
                show 我的宫女 at chara
                我的宫女 "主子，不好了！"
                我的宫女 "方才[gn.name]在外头碰见[fz.cheng]，好端端的却被拦下来刁难羞辱了一番……"
                我的宫女 "[fz.cheng]还小题大做，将她送到掖廷杖责五十，人已经没了！"
                我 "[gn.name]……"
                "未几，掖廷送来了新的宫女顶替[gn.name]的位置……"
                $ my.Gongnv.remove(gn)
                $ newgn = renpy.random.choice(YTGongnv)
                $ YTGongnv.remove(newgn)
                $ my.Gongnv.append(newgn)
                $ newgn.lv = 4
                $ newgn.level = "婢子"
                hide 我的宫女
        else:
            pass
    else:
        pass




    if my.level != beifei and jinzu(my) != True and mapname== "寝居" and jinzu(my) == False:
        $ lucky = renpy.random.randint(0, 50)
        if lucky == 0:
            python:
                for i in NPC_fz_list:
                    if i == my:
                        pass
                    elif i.state == "病重" or jinzu(i) == True or i.state == "抱恙":
                        pass
                    elif   tags[4] in i.tags:
                        pass
                    elif tags_yali[2] in i.tags:
                        pass
                    elif i.like > 50:
                        tempfzlist.append(i)
                    elif i in my.friends and i not in my.foes:
                        tempfzlist.append(i)
                    else:
                        pass
                    global tempfzlist
            if len(tempfzlist) == 0:
                pass
            else:
                $ fz = renpy.random.choice(tempfzlist)
                if fz in my.foes or fz not in NPC_fz_list:
                    pass
                else:
                    $ bg("寝居")
                    show 我的宫女 at chara
                    我的宫女 "主子，[fz.cheng]来了。"
                    if my.level >= fz.level:
                        $ temptext = "前去迎接"
                    else:
                        $ temptext = "让她进来"
                    menu:
                        "推脱不见" if fz.level > my.level:
                            我的宫女 "是。"
                            hide 我的宫女
                            if fz.xingge == "娇纵" and fz.xinji < 300:
                                "没过多久，[my.Gongnv[0].name]前来回禀，[fz.cheng]已经离开了，面色似乎有些难看，嘴里还嘀咕着什么“方才还听见说话的声儿呢怎就说不在呢？”"
                                $ fz.like = fz.like - 3
                            elif fz.xingge == "势利" and fz.xinji < 300:
                                "没过多久，[my.Gongnv[0].name]前来回禀，[fz.cheng]已经离开了，临走前也是恭恭敬敬的，还说改日再来拜访。"
                                $ fz.like = fz.like - 3
                            elif fz.like > 80:
                                pass
                            else:
                                $ fz.like = fz.like - 1
                        "[temptext]":
                            hide 我的宫女
                            show fz at chara with dissolve
                            if my.level >= fz.level:
                                我 "[fz.cheng]安，今日怎么有空上这[my.qinju]来了？"
                                "[fz.hao][fz.weifen] [fz.name]" "（微笑落座）你还同我讲这些虚礼做什么？"
                                "[fz.hao][fz.weifen] [fz.name]" "在宫里闲着也是闲着，来看看你不成？"
                                我 "当然，我这[my.qinju]自然是随时欢迎你的。"
                            else:
                                "[fz.hao][fz.weifen] [fz.name]" "嫔妾给[my.cheng]请安。"
                                if fz.xingge == "活泼":
                                    "[fz.hao][fz.weifen] [fz.name]" "啊啊，我不想讲哪些虚礼了！[aicheng]，你不会怪罪吧？宫里好闷啊，我就想过来找点乐子。"
                                else:
                                    我 "快免礼吧，今日怎么有空上这[my.qinju]来了？"
                                    "[fz.hao][fz.weifen] [fz.name]" "嫔妾一个人在屋子里闷得发慌，又懒得去御花园啊那些地方走动，索性便来这儿了。"
                            我 "（欣然莞尔，同[fz.cheng]落座。）"
                            if fz.xingge == "活泼" or fz.like >= 50:
                                $ cheng = aicheng
                            else:
                                $ cheng = my.cheng
                            if fz.like >= 80:
                                $ zicheng = "我"
                            elif my.level >= fz.level:
                                $ zicheng = "嫔妾"
                            else:
                                $ zicheng = "本宫"
                            python:
                                templist = []
                                for i in my.foes:
                                    if i not in fz.foes:
                                        templist.append(i)

                            if fz.huashu["一A"] != 0 and len(templist) > 0:
                                $ lucky = renpy.random.randint(0, 3)
                            else:
                                $ lucky = renpy.random.randint(0, 2)
                            if lucky== 3:
                                $ tempfz = renpy.random.choice(templist)
                                妃子 "说起来，[zicheng]听说，[cheng]似乎和[tempfz.cheng]之间有些恩怨？"
                                if my.level >= fz.level:
                                    妃子 "唉，这人呀，各有各的性子，彼此间会芥蒂也是常事。只是倒头来还是堵了自己的气呐。"
                                    妃子 "同别人过不去，倒头来也是跟自己过不去。[cheng]是聪明人，应当能看得通透这其中的道理。"
                                else:
                                    妃子 "当然了，[zicheng]知道此事多半都是那些多嘴多舌的下人们胡乱编造的。[cheng]的性情和心怀[zicheng]向来是清楚的。"
                                    妃子 "都说同别人过不去，倒头来也是跟自己过不去。[cheng]自然不会如此，对吗？"
                                menu:
                                    "点头称是":
                                        "（你不再与[tempfz.cheng]交恶了。）"
                                        $ my.foes.remove(tempfz)

                                    "承认交恶" if fz.huashu["一A"] != 3:
                                        if my.level >= fz.level:
                                            我 "[fz.cheng]的意思嫔妾明白，但积怨已深，也不是说放就放得下的。"
                                        else:
                                            我 "兴许吧，这些事情并非看得通透就能说得清楚。"
                                        妃子 "（遗憾）那便是无法了……"

                            elif len(fz.foes) > 0 and lucky == 0:
                                $ tempfz = renpy.random.choice(fz.foes)
                                if tempfz in my.friends:
                                    妃子 "说起来，[cheng]似乎和[tempfz.cheng]走得颇近呢。"
                                    if my.level >= fz.level:
                                        妃子 "都说“近朱者赤，近墨者黑”，[cheng]往后还是不要同她往来了，免得引火烧身，追悔莫及呀。"
                                    else:
                                        妃子 "[cheng]莫怪臣妾多嘴了，都说“近朱者赤，近墨者黑”，您还是不要同她往来了。"
                                    menu:
                                        "答应":
                                            "（你不再与[tempfz.cheng]交好了。）"
                                            $ my.friends.remove(tempfz)
                                            if my in tempfz.friends:
                                                $ tempfz.friends.remove(my)
                                            else:
                                                pass
                                        "拒绝":
                                            if my.level >= fz.level:
                                                我 "[fz.cheng]的意思臣妾明白，不过臣妾觉得她并非如您所说那般不堪。"
                                            else:
                                                我 "本宫倒觉得她并非如你所说那般不堪，倒是妹妹你……说这些挑拨离间的话是为了什么呢？"
                                            if fz.xingge == "清冷" or fz.xingge == "娇纵" or fz.xinji <= 200:
                                                $ lucky = renpy.random.randint(0, 1)
                                                $ fz.like -= 8
                                            else:
                                                $ fz.like -= 15
                                                $ lucky = renpy.random.randint(0, 2)
                                            if lucky == 0:
                                                $ fz.like -= 5
                                                if my.level < fz.level:
                                                    妃子 "是么？原是臣妾自作多情了。"
                                                    妃子 "可惜臣妾对[tempfz.cheng]恨之入骨，却不想您信的是她……"
                                                else:
                                                    妃子 "呵……是本宫看错了你……"
                                                妃子 "既然如此，也没什么可说的了。"
                                                "（与[fz.cheng]结下了仇怨……）"
                                                if fz in my.friends:
                                                    $ my.friends.remove(fz)
                                                if my in fz.friends:
                                                    $ fz.friends.remove(my)
                                                $ my.foes.append(fz)
                                                $ fz.foes.append(my)
                                            elif lucky == 1:
                                                if my.level >= fz.level:
                                                    妃子 "是么？原是臣妾自作多情了，看来您同臣妾并不是一路人呢。"
                                                else:
                                                    妃子 "你若不信本宫，那本宫也没什么可说的了。"
                                                "（与[fz.cheng]不再交好了……）"
                                                if fz in my.friends:
                                                    $ my.friends.remove(fz)
                                                if my in fz.friends:
                                                    $ fz.friends.remove(my)
                                            else:
                                                妃子 "（迟疑了一下，默然地叹了口气，脸上虽是不悦，却也没多说什么。）"


                                elif tempfz not in my.foes:
                                    妃子 "说起来，[cheng]觉得[tempfz.cheng]此人如何？"
                                    "[fz.cheng]颇为怨愤地在你面前数落了[tempfz.hao][tempfz.weifen][tempfz.name]一通……"
                                    妃子 "依我看，此人是断断不能来往的。"
                                    我 思 "（应当如何表态呢……）"
                                    menu:
                                        "赞同":
                                            我 惊 "她竟是如此可恶之人，往后[zicheng]决计不会同她往来。"
                                            妃子 "是啊，我们倒不如联起手来，让她吃点苦头！"
                                            "（与[tempfz.cheng]结下了仇怨……）"
                                            $ Feizilike_Up(fz,5)
                                            $ tempfz.like -= 15
                                            if tempfz.like >= 80:
                                                $ tempfz.like = 80
                                            $ my.foes.append(tempfz)
                                        "反对" if tempfz not in my.foes:
                                            我 常 "[zicheng]倒觉得她并非如你所说那般，这其中恐怕有什么误会。"
                                            $ fz.like -= 15
                                            妃子 "呵……"
                                            妃子 "难不成是我污蔑她吗？"
                                            if fz.like <= 20 and fz in my.friends:
                                                "（[fz.cheng]不再同你交好了。）"
                                                if my in fz.friends:
                                                    $ fz.friends.remove(my)
                                                $ my.friends.remove(fz)
                                        "含糊":
                                            我 思 "真是如此吗，[zicheng]竟不知道呢。"
                                            妃子 "……"
                                            $ fz.like -= 8
                                            "（[fz.cheng]对你的态度并不很满意，但也没有多说什么。）"
                                else:
                                    pass
                            else:
                                "闲聊了许久，[fz.cheng]方离去。"
                                if fz.xingge == "活泼":
                                    $ my.yali -= 5
                                    $ fz.yali -= 5
                                else:
                                    $ my.yali -= 3
                                    $ fz.yali -= 3



                            hide fz
                            $ Feizilike_Up(fz,2)
                            $ timenum = timenum +1
                            $ AP = AP -1
                            $ fz.AP -= 1
    else:

        pass


    $ tempnum = len(my.kids)
    $ lucky = renpy.random.randint(0, 25 + tempnum*3)
    if lucky < tempnum and len(my.kids) != 0:
        $ kid = renpy.random.choice(my.kids)
        if 0<= kid.age <= 1 and mapname == "寝居":
            $ lucky = renpy.random.randint(0, 3)
            if lucky == 0:
                "奶娘正好抱着刚睡着的[kid.cheng][kid.name]站在廊下。"
                menu:
                    "让奶娘抱回去接着睡":
                        "奶娘" "奴婢告退。"
                    "轻轻摸摸他的脸":
                        "不知是因为感受到了你的触碰还是正在做着什么好梦，[kid.name]的小脸上露出了甜甜的笑容。"
                        $ kid.health += 0.5
                        $ kid.like += 0.5
                        $ kid.duli -= 0.5
                        $ timenum += 1
                    "扯了扯他的脸颊":
                        show 孩子
                        孩子 "（惊醒）哇……哇……哇……"
                        我 惊 "这……"
                        "一时手足无措，幸好奶娘赶紧把[kid.name]哄睡着了……"
                        "[kid.name]虽然又安静了下来，但是看着睡得不如之前安稳了……"
                        hide 孩子
                        $ kid.health -= 0.5
                        $ kid.like -= 0.5
                        $ kid.duli += 0.5
                        $ kid.qinmian += 0.5
                        $ timenum += 1
            elif lucky == 1:
                "奶娘正好抱着[kid.cheng][kid.name]站在廊下，轻声哼歌哄着[kid.cheng]。"
                menu:
                    "不去打扰他们":
                        "[kid.cheng]许是睡着了，奶娘抱着[kid.cheng]回屋了。"
                    "走过去":
                        show 孩子
                        孩子 "（哼唧了两声，好奇的看着你。）"
                        menu:
                            "温柔的笑":
                                孩子 "（也朝着你笑起来。）"
                                $ kid.like += 0.5
                                $ kid.qingxiang -= 1
                            "做个鬼脸":
                                孩子 "（高兴得笑起来。）"
                                $ taidu += 3
                                $ kid.like += 0.5
                                $ kid.duli += 0.5
                            "抱过来哄一哄":
                                孩子 "（虽然可能并未听懂，但看起来仍然很开心。）"
                                $ kid.like += 0.5
                                $ kid.iq += 0.1
                        hide 孩子
                        $ timenum += 1
            elif lucky == 2:
                "奶娘正好抱着[kid.cheng][kid.name]站在廊下，轻声哼歌哄着[kid.cheng]。"
                menu:
                    "不去打扰他们":
                        "[kid.cheng]许是睡着了，奶娘抱着[kid.cheng]回屋了。"
                    "走过去":
                        show 孩子
                        孩子 "（朝你伸出手似乎想抓什么）"
                        menu:
                            "伸手给他":
                                孩子 "（抓住了你的手，咿咿呀呀的说了些你听不懂的话。）"
                                $ kid.like += 0.5
                                $ kid.duli -= 0.5
                            "避开他的手，揉他脸":
                                孩子 "（大哭）哇……哇……哇！"
                                $ taidu += 3
                                $ kid.like -= 0.5
                                $ kid.duli += 0.5
                            "抓着他的手晃一晃":
                                if kid.xingge == "外向":
                                    孩子 "（挠了挠你的手心，吐了吐舌头。）"
                                elif kid.xingge == "内向":
                                    孩子 "（似乎被吓着了，一动不动的定在奶娘怀里。）"
                                else:
                                    孩子 "（他缩了缩手，不安的望着你。）"
                                $ kid.like += 0.5
                        hide 孩子
                        $ timenum += 1
            elif lucky == 3:
                if kid.xingge == "外向":
                    show 孩子
                    孩子 "啊啊哦！啊啊哦！"
                    我 惊 "[kid.name]这是在做什么？"
                    hide 孩子
                    show 我的宫女
                    我的宫女 "主子，[kid.cheng]是想引起您的注意呢。"
                    hide 我的宫女
                    show 孩子
                    menu:
                        我 "（……）"
                        "陪[kid.name]玩":
                            孩子 "（高兴得手舞足蹈，嘴里啦啦得像是唱戏一般，滑稽又可爱。）"
                            $ kid.like += 1
                            $ kid.duli -= 0.5
                            $ kid.qinmian += 0.5
                        "不理[kid.name]":
                            孩子 "（自顾自地叫着，像是唱戏一样。）"
                            $ kid.like -= 0.5
                            $ kid.duli += 0.5
                elif kid.xingge == "内向":
                    show 孩子
                    孩子 "（一个人在榻上玩着几个偶人，时不时发出可爱的笑声。）"
                    menu:
                        "陪[kid.name]玩":
                            孩子 "（喜出望外地拉着你）玩……玩……"
                            "度过了无忧无虑的一段时光。"
                            $ kid.like += 1
                            $ kid.duli -= 0.5
                            $ kid.qinmian += 0.5
                        "不理[kid.name]":
                            孩子 "（自顾自地玩着。）"
                            $ kid.duli += 0.5
                else:
                    show 孩子
                    孩子 "（拿着两个玩具，眼睛朝着你望来）嘿嘿……嘻嘻……"
                    我 惊 "[kid.name]这是在做什么？"
                    hide 孩子
                    show 我的宫女
                    我的宫女 "主子，[kid.cheng]是想引起您的注意呢。"
                    hide 我的宫女
                    show 孩子
                    menu:
                        我 "（……）"
                        "陪[kid.name]玩":
                            孩子 "（高兴得手舞足蹈，拉着你玩得很开心）"
                            $ kid.like += 1
                            $ kid.duli -= 0.5
                            $ kid.qinmian += 0.5
                        "不理[kid.name]":
                            孩子 "（有些失落，仍然自顾自地咯咯笑着。）"
                            $ kid.like -= 0.5
                            $ kid.duli += 0.5
                hide 孩子
            else:
                pass
        else:
            pass
    else:







        pass

    if player == 0 and year == 4 and month == 9 and datenum == 1 and timenum == 1:
        $ bg("寝居")
        show 我的宫女 at chara
        我的宫女 "参见[my.cheng]。"
        我 "何事？"
        我的宫女 "奴婢今早在[my.qinju]外发现了这个……"
        "[my.Gongnv[0].name]将一个小布包递了上来。"
        我 "莫不是有人遗落的？……可我刚刚入宫，又谁会来[my.qinju]附近呢？"
        我的宫女 "可这上面还有您的名字，落款写着……弦歌容锦？这是谁啊？"
        我 "……"
        "布包里面还有一张字条，上面写着：{p}在已结束的宫廷事件界面有一些字样实际上是按钮哦~想要知道真凶的话不妨试试吧。这个能力在以后的版本需要达到其他条件才可以拥有，还请且用且珍惜~"
        我 "这东西实在可疑，先收进库房吧。"
        我的宫女 "是。"
        hide 我的宫女
        "获得了毒药[poison04.name]×1。"
        $ kufang.append(poison04)
        $ timenum = timenum + 1
    else:
        pass

    if my.familylevel == 10 or my.familylevel < 4 and  my.level !=beifei:
        $ lucky = renpy.random.randint(0, 150)
        if my.familylevel == 10 and lucky < 3 and timenum == 1:
            $ lucky = renpy.random.randint(0, 120)
            if lucky == 120:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "参见[my.cheng]。"
                我的宫女 "（面露喜色）您家里送东西来了！"
                我 "是爹爹送来的？"
                我的宫女 "是啊，说是经营有方，连连盈利，又挂念着您在宫里怕是多有花销呢。奴婢先替您收起来吧。"
                "（收到了500两银子。）"
                hide 我的宫女
                $ money = money +500
            elif lucky >= 100:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "参见[my.cheng]。"
                我的宫女 "（面露喜色）您家里送东西来了！"
                我 "是爹爹送来的？"
                我的宫女 "是啊，说是经营有方，颇有盈利，又挂念着您在宫里怕是多有花销呢。奴婢先替您收起来吧。"
                "（收到了100两银子。）"
                hide 我的宫女
                $ money = money +100
            elif lucky <= my.father.neng:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "参见[my.cheng]。"
                我的宫女 "（面露喜色）您家里送东西来了！"
                我 "是爹爹送来的？"
                我的宫女 "奴婢先替您收起来吧。"
                "（收到了50两银子。）"
                hide 我的宫女
                $ money = money +50
            else:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "参见[my.cheng]。"
                我的宫女 "（面容忐忑）您家里捎了信来，说今年家中经营不利，希望您能接济些许……"
                menu:
                    我 "这……"
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
                else:
                    我 "去库里送[tempnum]两银子给爹爹吧。"
                    $ my.father.exp += tempnum*0.1
                    $ money -= tempnum

                hide 我的宫女


        elif my.familylevel < 4 and lucky == 0 and timenum == 1 and my.father.zhong <= 50 and my.father.neng >= 50:
            $ lucky = renpy.random.randint(0, 10)
            $ bg("寝居")
            show 我的宫女 at chara
            我的宫女 "参见[my.cheng]。"
            我的宫女 "（面露喜色）您家里送东西来了！"
            我 "这是什么？"
            我的宫女 "奴婢也不知道，不过送东西那个人神神秘秘的，说让您小心取用。"
            我 "好，我知道了，先收起来吧。"
            hide 我的宫女
            if lucky < 2:
                "获得了[poison01.name]×1，[poison02.name]×1。"
                $ kufang.append(poison01)
                $ kufang.append(poison02)
            elif lucky < 4:
                "获得了[poison02.name]×1，[poison03.name]×1。"
                $ kufang.append(poison02)
                $ kufang.append(poison03)
            elif lucky < 7:
                "获得了[poison01.name]×2。"
                $ kufang.append(poison01)
                $ kufang.append(poison01)
            else:
                "获得了[poison01.name]×1，[poison03.name]×1。"
                $ kufang.append(poison01)
                $ kufang.append(poison03)
        else:
            pass
    else:
        pass

    if my.book >= 80 and  my.level !=beifei and my.state != "病重" and jinzu(my) != True and huaiyun(my) == False and mapname == "寝居":
        $ lucky = renpy.random.randint(0, 75)
        if lucky <= 1 and timenum > 1 and timenum < 5 and my.love >= 0:
            $ bg("寝居")
            show 赵公公 at chara
            赵公公 "奴才给[my.cheng]娘娘请安了。"
            我 "赵公公今日何事前来？"
            赵公公 "皇上今日甚有兴致，知道娘娘善诗善书，故而想来请您一幅字。"
            menu:
                "欣然答应":
                    pass
            我 "既然如此，还请公公稍等片刻。"
            赵公公 "[my.cheng]娘娘不急，您写完差人送来圣宸宫便是了。"
            hide 赵公公
            show 研读诗书 at cg
            "于寝居中书字一幅，送往圣宸宫。"
            $ AP = AP - 1
            $ timenum = timenum + 1
            hide 研读诗书
            "未几，宫人回禀，皇上甚是满意。"
            $ mustshiqin = mustshiqin + 20
            $ my.love = my.love + 1
            $ my.exp = my.exp + 4
            $ yuci = renpy.random.choice([acc10,acc11,acc15,set10,set11,set15])
            show 我的宫女 at chara
            我的宫女 "主子，圣宸宫送来了[yuci.name]，已经为您收到库房了。"
            hide 我的宫女
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
        elif lucky  <= 3 and timenum < 5 and my.taihoulike >= 0:
            $ bg("寝居")
            show 莲稚 at chara
            莲稚 "奴婢给[my.cheng]娘娘请安。"
            我 "莲稚姑娘今日何事前来？"
            莲稚 "太后娘娘今日甚有兴致，知道娘娘善诗善书，故而想来请您一幅字。"
            menu:
                "欣然答应":
                    pass
            我 "既然如此，还请姑娘稍等片刻。"
            莲稚 "[my.cheng]娘娘不急，您写完差人送来建章宫便是了。"
            hide 莲稚
            show 研读诗书 at cg
            "于寝居中书字一幅，送往建章宫。"
            $ AP = AP - 1
            $ timenum = timenum + 1
            hide 研读诗书
            "未几，宫人回禀，太后甚是满意。"
            $ Taihoulike_Up(my,1)
            $ my.exp = my.exp + 6
            $ yuci = renpy.random.choice(presents_hign)
            show 我的宫女 at chara
            我的宫女 "主子，建章宫送来了[yuci.name]，已经为您收到库房了。"
            hide 我的宫女
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
        else:

            pass
    else:
        pass


    $ lucky = renpy.random.randint(0, 60)
    if lucky == 0 and timenum > 1 and jinzu(my) == False:
        if randomfz() == my:
            pass
        else:
            $ zhu = randomfz()
            if zhu.like >= 60 and zhu != my:
                $ lucky = renpy.random.randint(0, 3)
                if lucky == 0 and mapname == "皇宫":
                    $ renpy.call("宫中偶遇交好",fz = fz,from_current=False)
                else:
                    pass
            elif zhu.qingxiang < 30 or zhu.like > 80 or zhu == my or zhu in juqingfei:
                pass
            else:
                if mapname == "寝居":
                    $ bg("寝居")
                    show 我的宫女 at chara
                    我的宫女 "主子，[zhu.cheng]来了。"
                    if my.level >= zhu.level:
                        $ temptext = "前去迎接"
                    else:
                        $ temptext = "让她进来"
                    menu:
                        "推脱不见" if zhu.level > my.level:
                            我的宫女 "是。"
                            hide 我的宫女
                            if zhu.xingge == "娇纵" and zhu.xinji < 300:
                                "没过多久，[my.Gongnv[0].name]前来回禀，[zhu.cheng]已经离开了，面色似乎有些难看……"
                                $ zhu.like = zhu.like - 6
                            elif zhu.xingge == "势利" and zhu.xinji < 300:
                                "没过多久，[my.Gongnv[0].name]前来回禀，[zhu.cheng]已经离开了，临走前也是恭恭敬敬的，还说改日再来拜访。"
                                $ zhu.like = zhu.like - 6
                            else:
                                $ zhu.like = zhu.like - 3
                        "[temptext]":
                            $ fz = zhu
                            hide 我的宫女
                            show fz at chara with dissolve
                            if my.level >= fz.level:
                                我 "[fz.cheng]安，今日怎么有空上这[my.qinju]来了？"
                                "[fz.hao][fz.weifen] [fz.name]" "（微笑落座）[my.cheng]不必多礼，本宫也只是闲来无事，过来看看。"
                            else:
                                "[fz.hao][fz.weifen] [fz.name]" "嫔妾给[my.cheng]请安。"
                                我 "[fz.cheng]今日前来，所为何事？"
                            "[fz.cheng]同你闲聊几句，却不想起了口舌争锋……"
                            menu:
                                "开始争锋":
                                    call battle (fz=fz) from _call_battle_4
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
                else:
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
                    hide screen Bigmap
                    scene 皇宫
                    "远远便看见一道倩影……"
                    $ fz = zhu
                    show fz at chara with dissolve
                    $ renpy.call("宫中偶遇争锋",fz = fz,from_current=False)
    else:


        pass



    python:
        tempgnlist = []
        for i in my.Gongnv:
            if "刺探情报" in i.skill:
                tempgnlist.append(i)
            else:
                pass
        a = len(tempgnlist)
        tempfzlist = []
        for i in NPC_fz_list:
            if i.xingge1 == False or i.xinji1 == False:
                tempfzlist.append(i)
            else:
                pass
        b = len(tempfzlist)
    if a == 0 or b == 0:
        pass
    else:
        $ lucky = renpy.random.randint(0, 30-a*2)
        if lucky == 0 and my.level != beifei and mapname == "寝居":
            $ gn = renpy.random.choice(tempgnlist)
            $ fz = renpy.random.choice(tempfzlist)
            $ bg("寝居")
            $ gnface = gn.face
            show gn at chara
            if fz.xingge1 == False:
                $ fz.xingge1 = True
                "[gn.level] [gn.name]" "主子，奴婢听说，[fz.cheng]是一个[fz.xingge]之人。"
            else:
                $ fz.xinji1 = True
                $ shuxingmiaoshu(fz)
                "[gn.level] [gn.name]" "主子，奴婢听说，[fz.cheng]的心思十分[fz.xinjilv]……"

            hide gn
        else:
            pass




    $ lucky = renpy.random.randint(0, 30)
    if laoji in my.Gongnv and laoji.like >= 114 and month == 8 and datenum == 1 and timenum == 1:
        $ gn = laoji
        show gn
        宫女 "哟呵~奴婢来给[my.cheng]请安噜。"
        我 笑 "无事献殷勤？"
        宫女 "您怎么这么能说奴婢呢~奴婢对主子如何，您还不明白嘛~"
        宫女 "这是奴婢的一点心意~还请[my.cheng]务必收下。"
        hide gn
        "得到了[goldenegg.name]。"
        $ kufang.append(goldenegg)
        $ timenum += 1
    elif lucky == 0 and mapname == "寝居" and my.level != beifei and len(my.Gongnv) > 2:
        python:
            gn = renpy.random.choice(my.Gongnv[1:-1])
            if gn.xingge == "单纯" and gn not in teshugn:
                templist = []
                for i in kufang:
                    if i.leibie == "摆件" or i.leibie == "首饰":
                        templist.append(i)
                if len(templist) > 0:
                    tempitem = renpy.random.choice(templist)
                    kufang.remove(tempitem)
                    renpy.call("宫女弄坏物品",gn = gn,what = tempitem,from_current=False)
                else:
                    pass
    elif lucky <= 1 and mapname == "皇宫" and my.level != beifei and len(my.Gongnv) > 2:
        $ gn = renpy.random.choice(my.Gongnv[1:-1])
        if gn.xingge == "机灵" and  gn not in teshugn:
            if len(NPC_fz_list) <= 1:
                pass
            else:
                python:
                    tempfz = renpy.random.choice(NPC_fz_list)
                    tempgn = renpy.random.choice(tempfz.Gongnv)
                    renpy.call("宫女私下交际",gn = gn,fz = tempfz,tempgn = tempgn,from_current=False)
        else:
            pass
    elif 2 <= lucky <= 4 and  mapname == "皇宫" and my.level != beifei and len(my.Gongnv) > 2:
        $ gn = renpy.random.choice(my.Gongnv[1:-1])
        if gn.xingge == "聪颖" and  gn not in teshugn:
            if len(NPC_fz_list) <= 1:
                pass
            else:
                python:
                    templist = []
                    for i in NPC_fz_list:
                        if i == my:
                            pass
                        else:
                            for j in i.Gongnv:
                                if j.yexin >= 400 and j.lv < 5 and j.xingge == "机灵":
                                    templist.append([i,j])
                    if len(templist) == 0:
                        pass
                    else:
                        temptext = renpy.random.choice(templist)
                        renpy.call("宫女私下交际2",gn = gn,fz = temptext[0],tempgn = temptext[1],from_current=False)
        else:

            pass
    else:

        pass



    python:
        tempgnlist = []
        tempnum = 100
        for i in my.Gongnv:
            if "寻医问药" in i.skill:
                tempgnlist.append(i)
                tempnum = tempnum - 20
            else:
                pass
        if my.anhai["初始"] != 0:
            tempnum -= 5*my.anhai["初始"]

        if tempnum <= 20:
            tempnum = 20
        else:
            pass
    $ lucky = renpy.random.randint(0, tempnum)
    if lucky == 0 and timenum == 1 and my.level != beifei:
        if len(tempgnlist) == 0:
            $ gn = renpy.random.choice(my.Gongnv)
        else:
            $ gn = renpy.random.choice(tempgnlist)
        $ bg("寝居")

        $ gnface = gn.face
        show gn at chara
        "[gn.level] [gn.name]" "主子……"
        我 "怎么了，这么神神秘秘的？"
        "[gn.level] [gn.name]" "这是奴婢偶然得到的，还请您收好，小心取用。"
        我 "好……本宫知道了。"
        hide gn
        $ lucky = renpy.random.randint(0, 10)
        if lucky < 4:
            "获得了[poison01.name]×1。"
            $ kufang.append(poison01)
        elif lucky < 8:
            "获得了[poison02.name]×1。"
            $ kufang.append(poison02)
        else:
            "获得了[poison03.name]×1。"
            $ kufang.append(poison03)
    else:
        pass







    if mapname == "寝居":
        if huaiyun(my) == True and my.love > 20 and timenum == 3 and tags[4] not in my.tags and jinzu(my) == False:
            $ lucky = renpy.random.randint(0, 300)
            if lucky < my.love:
                show 我的宫女 at chara
                我的宫女 "（面有喜色）[my.cheng]，皇上来看您了！"
                hide 我的宫女
                "宫人" "皇上到——"
                show 皇帝 at chara
                我 "臣妾参见皇上。"
                if hdxingge != "冷漠":
                    皇上 "爱妃快快请起。"
                    皇上 "如今你身怀皇嗣，不必多礼。"
                    我 "是。"
                else:
                    皇上 "免礼。"
                    皇上 "你身怀皇嗣，所以朕才来看看你。"
                    我 "是。"
                皇上 "身体可还好吧？"
                我 "回皇上，太医说臣妾这胎还算安稳。"
                皇上 "嗯，那便好。"
                皇上 "（揽着你在桌前坐下，陪伴了许久方才离开。）"
                hide 皇帝
                $ timenum = timenum +1
                $ AP = AP -1
            else:
                pass
        elif jinzu(my) != True and my.love > 50 and timenum == 3:
            $ lucky = renpy.random.randint(0, 300)
            if lucky < my.love:
                show 我的宫女 at chara
                我的宫女 "（面有喜色）[my.cheng]，皇上来了！"
                hide 我的宫女
                "宫人" "皇上到——"
                show 皇帝 at chara
                我 "臣妾参见皇上。"
                if hdxingge != "冷漠":
                    皇上 "爱妃请起。"
                else:
                    皇上 "免礼。"
                皇上 "今日朕政务忙完了，所以过来看看你。"
                我 "多谢皇上。"
                皇上 "嗯，陪朕坐坐。"
                menu:
                    "献舞一曲":
                        if my.dance > 80:
                            if hdxingge == "风流":
                                皇上 "好！大好！"
                                皇上 "爱妃好舞艺，今日实在是令朕大饱眼福啊！"
                                $ my.love = my.love + 2
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，看着你舞完一曲，颔首微笑。）此舞甚好。"
                            elif hdxingge == "冷漠":
                                $ my.love = my.love + 1
                                皇上 "朕常听人说起你舞艺超群，如今看来也不过尔尔。罢了，朕知道你有心了。"
                            else:
                                $ my.love = my.love + 1
                                皇上 "爱妃舞技炉火纯青，着实让朕为之倾倒。"
                        elif my.dance >50:
                            if hdxingge == "风流":
                                皇上 "好！"
                                皇上 "爱妃此舞真是令朕大饱眼福啊！"
                                $ my.love = my.love + 1
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，看着你舞完一曲，颔首微笑。）此舞甚好。"
                            elif hdxingge == "冷漠":
                                皇上 "不过尔尔。罢了，朕知道你有心了。"
                                $ my.love = my.love + 0.5
                            else:
                                皇上 "爱妃舞技出众，令人赏心悦目。"
                                $ my.love = my.love + 0.5
                        else:
                            if hdxingge == "风流":
                                皇上 "（抱你入怀）爱妃往后陪着朕便是，不必献舞。"
                                我 "（怀疑）皇上的意思……"
                                皇上 "（似是忍着笑）好了好了，朕知道爱妃的用心，朕怕你累着。"
                                我 "（委屈）皇上这是在取笑臣妾？"
                                $ my.love = my.love - 1
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，看着你舞完一曲，颔首微笑。）此舞甚好。"
                            elif hdxingge == "冷漠":
                                皇上 "难看。以后不必再跳了。"
                                我 "皇上……"
                                皇上 "朕想看跳舞自会吩咐太乐坊安排，又何必来你这里？"
                                皇上 "太蠢。"
                                menu:
                                    "臣妾不是有意让皇上见笑的":
                                        皇上 "朕自然知道。"
                                    "让臣妾多陪伴您，或许能有些长进":
                                        皇上 "但愿吧。"
                                $ my.love = my.love + 2
                            else:
                                皇上 "爱妃这份心意已经足以让朕欣悦了。"
                    "献曲一首":
                        if my.muzic > 80:
                            if hdxingge == "风流":
                                皇上 "好！大好！"
                                皇上 "爱妃此曲正可谓是“此曲只应天上有，人间能得几回闻”啊！"
                                $ my.love = my.love + 2
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，颔首微笑。）此曲甚好。"
                            elif hdxingge == "冷漠":
                                $ my.love = my.love + 1
                                皇上 "朕常听人说起你极擅音律，如今看来也不过尔尔。罢了，朕知道你有心了。"
                            else:
                                $ my.love = my.love + 1
                                皇上 "爱妃此曲炉火纯青，着实让朕为之倾倒。"
                        elif my.muzic >50:
                            if hdxingge == "风流":
                                皇上 "好！"
                                皇上 "爱妃此曲真是令朕大饱耳福啊！"
                                $ my.love = my.love + 1
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，颔首微笑。）此曲甚好。"
                            elif hdxingge == "冷漠":
                                皇上 "不过尔尔。罢了，朕知道你有心了。"
                                $ my.love = my.love + 0.5
                            else:
                                皇上 "爱妃此曲甚好，令人心旷神怡。"
                                $ my.love = my.love + 0.5
                        else:
                            if hdxingge == "风流":
                                皇上 "（抱你入怀）爱妃往后陪着朕便是，不必献曲。"
                                我 "（怀疑）皇上的意思……"
                                皇上 "（似是忍着笑）好了好了，朕知道爱妃的用心，朕怕你累着。"
                                我 "（委屈）皇上这是在取笑臣妾？"
                                $ my.love = my.love - 1
                            elif hdxingge == "腹黑":
                                皇上 "（坐于桌前，手执茶盏，颔首微笑。）此曲甚好。"
                            elif hdxingge == "冷漠":
                                皇上 "难听。以后不必再唱了。"
                                我 "皇上……"
                                皇上 "朕想听曲时自会吩咐太乐坊安排，又何必来你这里？"
                                皇上 "太蠢。"
                                menu:
                                    "臣妾不是有意让皇上见笑的":
                                        皇上 "朕自然知道。"
                                    "让臣妾多陪伴您，或许能有些长进":
                                        皇上 "但愿吧。"
                                $ my.love = my.love + 2
                            else:
                                皇上 "爱妃这份心意已经足以让朕欣悦了。"
                    "温柔陪伴":

                        if hdxingge == "腹黑":
                            $ my.love = my.love + 2
                        elif hdxingge == "冷漠":
                            pass
                        else:
                            $ my.love = my.love + 1
                    "嬉笑逗趣":
                        if hdxingge == "腹黑":
                            pass
                        elif hdxingge == "冷漠":
                            $ my.love = my.love + 2
                        else:
                            $ my.love = my.love + 1

                皇上 "（陪伴你许久方才离开。）"
                hide 皇帝
                $ timenum = timenum +1
                $ AP = AP -1
            else:
                pass
        elif mapname == "寝居" and ygg_like == 15 and my.level != beifei and jinzu(my) == False:
            $ lucky = renpy.random.randint(0, 1)
            if lucky == 0:
                "外头传来一阵喧闹声……"
                show 我的宫女
                我的宫女 "主子，那个叫来福的小太监在外面，说是要见您……"
                我 "？！"
                我 "来福？他怎么来了？"
                我的宫女 "不知道，哭着喊着要见您，像是受了多大委屈似的。"
                我 "（叹了口气）让他进来罢。"
                hide 我的宫女
                show 来福
                来福 "呜呜呜呜，美女姐姐！"
                来福 "你帮帮来福吧！"
                "来福的小胖脸上挂着泪痕，眼睛哭得红红肿肿，看起来煞是可怜。"
                我 "这是怎么了？坐下来慢慢说。"
                来福 "呜呜呜，姑姑不知道中了什么邪，最近喜欢上了那些大红大紫的配色，还有那些晃得人眼疼的纹样。"
                来福 "她按着自己的喜好进了一大批货物，结果全都卖不出去。"
                来福 "连来福的口粮都被克扣了！"
                来福 "来福吃不饱饭，只能说了实话，结果，姑姑还要打来福的屁股！"
                来福 "呜呜呜呜！"
                "来福又是一阵嚎啕大哭，怎么劝也劝不住。"
                我 "（这可怎么是好……）"
                hide 来福
                show 我的宫女
                我的宫女 "主子，外头又来了个……"
                hide 我的宫女
                "[my.Gongnv[0].name]的话还未说完，就听到一个女子嘹亮的声音。"
                "？？？" "来福！来福！"
                来福 "啊？不好，姑姑来了！"
                show 月姑姑
                月姑姑 "来福！"
                hide 月姑姑

                show 我的宫女
                我的宫女 "（她怎么直接就进来了……）"
                hide 我的宫女
                show 月姑姑
                月姑姑 常 "来福！"
                hide 月姑姑
                show 来福
                "来福害怕地往你身后躲。"
                hide 来福
                show 月姑姑
                月姑姑 怒 "来福，快过来！"
                我 "您就是来福所说的那位月姑姑吧？"
                月姑姑 常 "是的，[my.cheng]娘娘，替我劝劝来福罢。"
                我 "来福？"
                hide 月姑姑
                show 来福
                来福 "呜呜呜，姑姑，来福错了……您别打来福，也别让来福饿肚子了！来福再也不敢说您品味次了！"
                我 "……"
                hide 来福
                show 月姑姑
                月姑姑 怒 "你！"
                月姑姑 常 "唉，好了好了，这件事是姑姑不对。"
                hide 月姑姑
                show 来福
                来福 "唔……"
                hide 来福
                show 月姑姑
                月姑姑 笑 "行了，来福，快过来，姑姑不会打你，也不会再让你饿着了，不过，你也不许再说姑姑的眼光有问题了！"
                hide 月姑姑
                show 来福
                来福 "姑姑……"
                我 "（看到姑姑将来福抱了过去，也忍不住会心一笑。）"
                hide 来福
                show 月姑姑
                月姑姑 常 "对了，[my.cheng]娘娘，之前便听闻您为人宽和大方，今日见得，果真如此。"
                我 "姑姑客气，举手之劳罢了。"
                月姑姑 思 "唉，可惜了最近时运不济……不过，方才京城有位豪富已经买下了我之前的存货，眼前的难关可算度过了。"
                hide 月姑姑
                show 来福
                来福 "（怪不得姑姑突然原谅我了……）"
                hide 来福
                show 月姑姑
                月姑姑 笑 "不仅如此，我还大赚了一笔，嘿嘿。"
                hide 月姑姑
                show 来福
                来福 "（有钱人的眼光可真不一般。）"
                hide 来福
                show 月姑姑
                月姑姑 笑 "当然了，也多亏了[my.cheng]您之前借我那一百五十两银子，如今可是翻了好几番了！"
                月姑姑 常 "来福，[my.cheng]前后总计给了你多少银子来着？"
                hide 月姑姑
                show 来福
                来福 "好像是三百两。"
                hide 来福
                show 月姑姑
                月姑姑 笑 "好，那这三百两我今天还是还给[my.cheng]罢。"
                menu:
                    "欣然接受":
                        $ money += 300
                        $ ygg_like += 5
                        "获得了三百两银子。"
                    "婉言回拒":

                        $ ygg_like += 10
                        月姑姑 笑 "（赞许地看了你一眼）[my.cheng]果然大气，你这个朋友我交定了。"
                月姑姑 常 "说起来也真是失礼，还未正式报过家门呢。"
                月姑姑 "宫里人都叫我月姑姑。"
                月姑姑 "您从来福那儿也该听说过，我从事宫里宫外的买卖。当然了，这事儿有皇室默许，责怪不到咱们头上来。"
                月姑姑 笑 "若您往后有需要——库房冗积，亦或是想寻些新奇玩意儿，也可来掖廷寻我。"
                月姑姑 "当然，有时候寻不见人，那便是亲自去采买了。"
                menu:
                    "原是如此":
                        pass
                月姑姑 "啊，今日还有些事儿，便不多叨扰了。"
                月姑姑 "来福，我们回去罢。"
                hide 月姑姑
                show 来福
                来福 "知道啦，姑姑。"
                hide 来福
            else:




                pass
        else:
            pass
    else:

        pass






    if mapname == "皇宫":

        $ lucky = renpy.random.randint(0, 3)
        if money >= 100 and lucky == 0 and ygg_like == 0:
            $ huanggong()
            scene 皇宫 with hpunch
            "？？？" "唉哟！"
            show 我的宫女
            我的宫女 "（反应迅速地护在你的身前）小心！"
            hide 我的宫女
            show 来福
            小太监 "啊啊啊痛死了！"
            hide 来福
            show 我的宫女
            我的宫女 "哪里来的小太监这么不小心？主子，你没事吧？"
            我 "我没事……不过他……"
            hide 我的宫女
            "那小太监一路风风火火地在宫道上狂奔，也不顾路上还有旁人，就这么迎面撞了过来，被[my.Gongnv[0].name]挡了一下，狼狈不堪地摔倒在地。"
            "方才便小心翼翼地捧着手里的一个木盒子，这下子盒子摔落在地，里面装得钗环首饰之类的玩意儿尽皆散落而出。"
            show 我的宫女
            我的宫女 "还不跟我家主子道歉？"
            hide 我的宫女
            show 来福
            小太监 "（像是没听到似的看着面前这一地狼藉）惨了……惨了……"
            小太监 "（用手扒拉着其中一块碎成两半的玉佩）完了，这是姑姑最中意的一块玉佩，我要被姑姑打死了！"
            menu:
                "询问缘由":
                    pass
            我 "你一个小太监，带着这么多宝物在这宫里乱跑是怎么一回事？你说的姑姑又是何人？"
            小太监 "（泪眼婆娑，一脸无辜地望着你）姑姑就是姑姑，这些东西都是姑姑托我送到宫门的……唉，本以为跑快些能赶上时辰，却没想到反而彻底把事情搞砸了。"
            小太监 "呜呜呜……"
            hide 来福
            show 我的宫女
            我的宫女 "主子，奴婢倒是听说，这宫里的确有宫人偷运宫中首饰到宫外贩卖一事。"
            我的宫女 "咱们是否要将这小太监送往掖廷，道明情况？"
            我 "奇怪，若真如你所说，那这小太监又怎敢大摇大摆地在宫道上带着那些物什飞奔？事情败露竟也不曾惊慌？"
            我的宫女 "嗯……奴婢也觉得奇怪，不过看他也不太聪明的样子……"
            hide 我的宫女
            show 来福
            小太监 "美女姐姐！"
            hide 我的宫女
            show 我的宫女
            我的宫女 "大胆！你做什么？"
            hide 我的宫女
            我 "（？！）"
            show 来福
            "这小太监居然抓住了你的裙摆，一把鼻涕一把泪地哭了起来。"
            我 "你……在叫本宫？"
            小太监 "（点头）美女姐姐，帮帮我吧，一看您就人美心善……"
            我 "帮你？怎么帮你？"
            小太监 "姑姑叫我把这些首饰送到宫外，我就办砸了事情，回去肯定难以交待的。"
            小太监 "幸好今天这些首饰不算贵重，统共加起来也就值个五十两银子……"
            我 "你的意思是……"
            menu:
                "帮他一把（失去五十两）":
                    "失去了五十两银子。"
                    $ money -= 50
                    我 "行了，别往本宫裙子上抹鼻涕了。起来罢。[my.Gongnv[0].name]，回去包五十两银子给他。"
                    小太监 "（感恩戴德地谢过）谢谢美女姐姐！您人真好！"
                    小太监 "回头我就跟姑姑说，东西还没送到宫门，就被一个美女姐姐买下了，姑姑也就不会追究了。"
                    我 "……"
                    hide 来福
                    show 我的宫女
                    我的宫女 "太无礼了！这是皇上的[my.cheng]，什么美女姐姐！"
                    hide 我的宫女
                    show 来福
                    小太监 "哦哦，好的，原来您是[my.cheng]啊！"
                    我 "对了，你说的那个姑姑……"
                    小太监 "啊！突然想起来姑姑叫我办完事赶紧回去的，肯定还有要事交待，我得马上回去才行！"
                    小太监 "对了，您那五十两银子等会儿送到掖廷，说是给月姑姑的就行了！"
                    小太监 "谢谢你，美女姐姐！"
                    hide 来福
                    "小太监的身影一下子就没影了……"
                    我 "月姑姑？"
                    show 我的宫女
                    我的宫女 "可要奴婢去调查一二？"
                    我 "嗯，倒是可疑得很。"
                    hide 我的宫女
                    $ ygg_like = 5
                "拒绝":
                    我 "此事是你自己冒失导致，我可不会帮你。"
                    我 "就当长个教训吧。"
                    小太监 "呜呜呜呜……"
                    hide 来福
                    $ ygg_like = -999
        elif money >= 150 and lucky == 0 and ygg_like == 5:
            $ huanggong()
            scene 皇宫 with hpunch
            "？？？" "美女姐姐！"
            show 我的宫女
            我的宫女 "主子，又是上次那个小太监……"
            hide 我的宫女
            我 "别乱跑，小心又像上次那样……"
            show 来福
            小太监 "（扑过来抱住你的胳膊）美女姐姐！"
            我 "……"
            我 "（哭笑不得。）"
            我 "这次又闯什么祸了？"
            小太监 "呜呜呜，姑姑的生辰要到了，来福想给姑姑买礼物……"
            我 "来福？"
            我 "哦……你就是来福吧？"
            来福 "是啊，之前没跟您说过么？"
            来福 "哎呀，这没什么要紧的，要紧的是姑姑的生日礼物……"
            来福 "呜呜呜……还差……还差一百两银子，来福实在没办法了！"
            我 "（惊）一百两？！"
            来福 "美女姐姐，帮帮来福吧！"
            来福 "姑姑一直想要京城最好的那家首饰铺子里的簪子，来福想给她买一支做礼物！"
            我 "嗯……"
            来福 "呜呜呜……能凑的钱都凑了，之前姑姑送的那些小玩意儿都拿去还了钱……"
            我 "这还差一百两？你都凑了多少钱？"
            来福 "呜呜呜……五两……"
            我 "……"
            来福 "美女姐姐，来福不会白白要你的银子的！"
            来福 "上次去太乐坊的时候，璇音阁的大姐姐给了来福一支曲谱，来福用它和你换，可以么？"
            menu:
                "同意（失去一百两）":
                    $ money -= 100
                    来福 "谢谢美女姐姐！"
                    来福 "太好了，姑姑一定会很开心的！"
                    来福 "谱子一会儿来福会给您送去的。"
                    hide 来福
                    show 我的宫女
                    我的宫女 "奇怪，璇音阁怎么会送你曲谱？"
                    hide 我的宫女
                    show 来福
                    来福 "嘿嘿，其实那谱子早已遗失，是姑姑让璇音阁帮忙去寻的，真寻到了却又懒得练，就叫璇音阁自己处置了。"
                    来福 "璇音阁的姐姐们说，宫中不时兴这样的乐曲了，所以见来福可爱，就送给来福了。"
                    来福 "（虽说曲谱不如那些金银首饰换钱方便，不过也大有用处，果然没想错，嘻嘻，来福我真是太聪明了！）"
                    来福 "好啦，来福要去给姑姑买簪子了！"
                    "来福的身影又一溜烟跑远了……"
                    hide 来福
                    "得到了曲谱[music09.name]。"
                    $ kufang.append(music09)
                    $ ygg_like = 10
                "拒绝":
                    $ ygg_like = -999
                    我 "一百两可不是个小数目，你还是自己想办法吧！"
                    我 "再说了，送礼物靠的是心意，没必要送这么贵重的东西，相信姑姑能理解你的。"
                    来福 "呜呜呜……"
                    hide 来福
                    "来福失落地离开了。"
        elif money >= 200 and lucky == 0 and ygg_like == 10:
            $ huanggong()
            scene 皇宫 with hpunch
            show 来福
            来福 "美女姐姐！"
            我 "来福？"
            我 "上次你买的簪子送给姑姑了吗？"
            来福 "送了，姑姑可高兴了！"
            来福 "姑姑还问我哪里来的这么多钱，我如实告诉她了。"
            我 "嗯……"
            来福 "姑姑听了也很感谢您呢！"
            来福 "姑姑还说，如果您乐意的话，能不能借她一百五十两银子急用。"
            来福 "而且，是不用还的那种。"
            我 "？！"
            来福 "虽说不知道姑姑要用来干什么，不过……"
            menu:
                "同意（失去一百五十两）":
                    $ money -= 150
                    来福 "来福先替姑姑谢谢您了！"
                    "来福拿了银子一路跑远了……"
                    hide 来福

                    $ ygg_like = 15
                "拒绝":
                    $ ygg_like = -999
                    来福 "果然，来福也觉得不行……"
                    hide 来福
                    "来福失落地离开了。"
        else:
            pass




    if chuhuan not in juqingfei and month > 4 and month < 8 and my.love >= 50 and mapname == "寝居" and chuhuan_0 == False:
        $ chuhuan_time = 1
        $ chuhuan_0 = True
        $ bg("寝居")
        show 我的宫女
        我的宫女 "主子，奴婢方才在外头碰到了赵公公……"
        我 "赵公公？这会儿怎得不在圣宸宫伺候皇上？"
        我的宫女 "赵公公说皇上现在正烦心呢，他还说您得皇上欢心，若是您说的话，皇上兴许能听得进去。"
        我 "本宫知道了……"
        hide 我的宫女
    elif chuhuan not in juqingfei and month > 4 and month < 8 and mapname == "寝居" and chuhuan_0 == False:
        $ lucky  = renpy.random.randint(0, 30)
        if lucky == 0:
            $ chuhuan_time = 1
            $ chuhuan_0 = True
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，奴婢方才在外头碰到了赵公公……"
            我 "赵公公？这会儿怎得不在圣宸宫伺候皇上？"
            我的宫女 "赵公公说皇上现在正烦心呢，也不晓得是为什么。"
            hide 我的宫女
        else:
            pass
    elif chuhuan in juqingfei and chuhuan.year == 0 and month == 8 and datenum == 3:
        python:
            for i in NPC_fz_list:
                if i == chuhuan or i == my:
                    pass
                elif i.xingge == "娇纵" and chuhuan not in i.foes:
                    i.foes.append(chuhuan)
                    i.qingxiang += 10
                elif i.qingxiang > 50 and chuhuan not in i.foes:
                    i.foes.append(chuhuan)
                    i.qingxiang += 10
                else:
                    pass
    elif chuhuan in juqingfei and chuhuan.year == 0 and month == 8 and datenum == 2:
        if timenum == 5 and jinzu(my) == False:
            show 我的宫女
            我的宫女 "主子，[chuhuan.cheng]在御花园办了赏月家宴，邀请阖宫妃嫔前往，咱们可要去？"
            menu:
                "去":
                    call 楚欢_中秋宴会 from _call_楚欢_中秋宴会
                    $ AP -= 1
                    $ timenum += 1
                "不去":
                    pass
        else:

            pass
    elif chuhuan in NPC_fz_list and chuhuan.love < my.love and my.love >= 80 and mapname == "皇宫" and chuhuan_3 == False:
        $ chuhuan_3 = True
        $ bg("皇宫")
        show 楚欢 at zuo
        show 皇帝 at you
        楚欢 盯 "皇上……最近政务很繁忙吗？"
        皇上 "尚还有余裕，怎么了，寻朕有事？"
        楚欢 笑 "倒没什么要紧的事，就是怕您政务劳累，欢儿身在后宫，一介妇人之身，无法同您分忧，实在惭愧。"
        if hdxingge == "温柔"  or hdxingge == "腹黑" or hdxingge == "风流":
            皇上 "欢儿多虑了。"
            皇上 "朕只希望你能在朕的庇佑下幸福平静地度过余生，于此，朕便安心了。"
            楚欢 思 "幸福吗……欢儿会尽力的。"
        elif hdxingge == "刚正":
            皇上 "是朕有愧于你，你无需感到有愧于朕。"
            皇上 "[chuhuan.cheng]只需要顾好自己便是了，身为天子，朝政再繁重都是朕的职责。"
        else:
            皇上 "你的事情，朕不会多过问。"
            皇上 "所以，朕的事情你也不必多过问，懂了吗？"
        楚欢 思 "欢儿知道……"
        楚欢 常 "只是欢儿看到后宫里的姐妹们不是能歌善舞，便是冰雪聪明，都能为您解忧，欢儿却什么能不会……"
        楚欢 思 "虽然欢儿每每想起以前的事情，都会觉得如今的一切都美好得有些不现实，毕竟在之前，能够见您一面便是奢望，可如今，欢儿却离您这么近。"
        楚欢 "但是仔细一想，却又感觉还是很远……"
        楚欢 "果然，只有[my.cheng]那样的女子，才配得上与您并肩而行吧。"
        楚欢 笑 "欢儿先告退了。"
        hide 楚欢
        皇上 "……"
        hide 皇帝
    else:


        pass


    if xuanxiutime == 35 and diwei(my) <= 1 and mapname == "寝居" and taoning_0 == False:
        $ taoning_0 = True
        $ bg("寝居")
        show 我的宫女
        我 "说起来，选秀的日子快到眼前了，宫里应该置办妥当了吧？"
        我的宫女 "听掖廷那边说是没出什么差错。对了，主子，说起这个，昨个儿奴婢就在[my.palace]外头碰着个秀女。"
        我 惊 "秀女怎么会在[my.palace]？"
        我的宫女 "听说是教引姑姑带她们熟悉后宫，那秀女不知道怎得便同其他秀女走散了，可着急坏了。"
        我的宫女 "瞧着是个胆小但也知礼的，奴婢便给她指了回储秀宫的路。"
        我的宫女 "也不知道她回去挨了教引姑姑的训话没有。"
        menu:
            "让掖廷将她逐出宫去":
                我 "身为秀女却如此不小心，往后如何侍奉皇上？"
                我 "让掖廷别留着她了，若之后面圣时出了差错，可别扫了皇上的兴。"
                我的宫女 "是。"
            "知道了":

                $ taoning_xuanxiu = True
                我 "若她往后能被皇上看中，倒也和本宫多了几分缘分。"
                我 "可问过她的名字了？"
                我的宫女 "那秀女说自己名叫陶凝。"
                我 "陶凝……好，本宫记下了。"
        hide 我的宫女
    else:
        pass

    if taoning in NPC_fz_list and jinzu(taoning) == False and havetag("失心成疯",taoning) == False and taoning.year < 3 and diwei(taoning) >= 2 and month == 7 and taoning_2 == False and mapname == "皇宫":
        python:
            templist = []
            for i in NPC_fz_list:
                if jinzu(i) == True or havetag("失心成疯",i) == True or i.love <= 20 or i == taoning or i == my or i.level >= taoning.level:
                    pass
                else:
                    templist.append(i)

        if len(templist) == 0:
            pass
        else:
            $ lucky =  renpy.random.randint(0,1)
            if lucky == 0:
                $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
            else:
                $ templist = sorted(templist, key=attrgetter("level"),reverse = False)
            $ fz =templist[0]
            $ taoning_2 = True
            call 偶遇陶凝_2 (fz) from _call_偶遇陶凝_2

    if taoning in NPC_fz_list and jinzu(taoning) == False and havetag("失心成疯",taoning) == False  and diwei(taoning) >= 2 and taoning_3 == False and mapname == "皇宫" and taoning.love < 20:
        python:
            templist = []
            for i in NPC_fz_list:
                if jinzu(i) == True or havetag("失心成疯",i) == True or i.love <= 50 or i == taoning or i == my or i in taoning.friends or taoning in i.friends:
                    pass
                elif i.xingge != "娇纵" and  i.xingge != "势利" and taoning not in i.foes:
                    pass
                else:
                    templist.append(i)

        if len(templist) == 0:
            pass
        else:
            $ lucky =  renpy.random.randint(0,1)
            $ templist = sorted(templist, key=attrgetter("xinji"),reverse = True)
            $ fz =templist[0]
            $ taoning_3 = True
            call 陶凝_黑化 (fz) from _call_陶凝_黑化
    else:
        pass






    if month == 12 and timenum == 1  and jinzu(my) != True and my.level !=beifei and lvxian == False:
        $ lvxian = True

        $ bg("寝居")
        show 我的宫女 at chara
        我的宫女 "主子，今日开始便是本年的最后一月了。按照我朝的习俗，宫中会在观仙台举行旅祀大典，持续一月。"
        我的宫女 "听说前往观仙台祈愿尤其灵验。"
        我的宫女 "若您对天意有所求，可前去一试，不过大典势高路远，需要花费一整天的时间，如今又正是天寒地冻的时节，主子还请小心身子。"
        menu:
            "（参加旅祀大典需要花费三个行动点和一整天的时间。）"
            "知道了":
                pass
        hide 我的宫女

    if my in biaoyan and month == 6 and datenum == 3 and timenum == 1 and yanhuitixingcishu == 0:

        show 我的宫女 at chara
        我的宫女 "主子，今晚便是皇上的诞辰宴了。您之前在太乐坊报了才艺上去，白日里可要保持好体力。"
        menu:
            "知道了":
                hide 我的宫女
                $ yanhuitixingcishu = 1

    elif my in biaoyan and month ==12 and datenum == 3 and timenum == 1 and yanhuitixingcishu == 0:
        show 我的宫女 at chara
        我的宫女 "主子，今晚便是除夕家宴了。您之前在太乐坊报了才艺上去，白日里可要保持好体力。"
        menu:
            "知道了":
                hide 我的宫女
                $ yanhuitixingcishu = 1
    else:
        pass

    if month == 6 and timenum > 3 and datenum == 3 and jinzu(my) != True and my.level !=beifei:
        menu:
            "前往宴会":
                python:
                    renpy.call("参加宴会",from_current=False)
    elif month == 12 and timenum > 3 and datenum == 3 and jinzu(my) != True and my.level !=beifei:
        menu:
            "前往宴会":
                python:
                    renpy.call("参加宴会",from_current=False)
    else:

        pass

    if month == 1  and datenum == 1 and shifoubiaoyan == 1:
        python:
            renpy.call("错过表演",from_current=False)

    elif month == 7 and datenum == 1  and shifoubiaoyan == 1:
        python:
            renpy.call("错过表演",from_current=False)
    else:


        pass




    if feizibeizhangze == True:
        $ fz = beizhangzefz[0]
        show 我的宫女 at chara
        我的宫女 "[my.cheng]，掖庭那边来说，[fz.cheng]的杖责已经结束了……"
        if huaiyun(fz) == True:
            $ my.lucky = my.lucky - 6
            $ tempstory = str(year)+"年"+str(month)+"月，被"+str(my.name)+"杖责二十，伤重而亡，一尸两命，帝大悲。\n"
            $ tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(fz.hao)+str(fz.weifen)+str(fz.name)+"被"+str(my.name)+"杖责二十，伤重而亡，一尸两命，帝大悲。\n"
            $ Killfz(fz)
            我的宫女 "[fz.cheng]被杖责后出血不止，太医说……一尸两命，已经没了。"
            我的宫女 "皇上这会儿正召见您呢……"
            call 妃嫔被责罚后续 (fz=beizhangzefz[0] ) from _call_妃嫔被责罚后续
        elif fz.health <= 200 or fz.state == "病重":
            $ my.lucky = my.lucky - 4
            $ tempstory = str(year)+"年"+str(month)+"月，被"+str(my.name)+"杖责二十，伤重而亡。\n"
            $ tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(fz.hao)+str(fz.weifen)+str(fz.name)+"被"+str(my.name)+"杖责二十，伤重而亡。\n"
            $ Killfz(fz)
            我的宫女 "[fz.cheng]被杖责后昏迷不醒，状况很不好，刚才人已经没了……"
            if suibianzefa == True:
                我的宫女 "皇上这会儿正召见您呢……"
                call 妃嫔被责罚后续 (fz=beizhangzefz[0] ) from _call_妃嫔被责罚后续_1
            else:
                我的宫女 "宫里的人这会儿都在说您胡乱责罚低位嫔妃，个个都惶恐不安……"
                "（在宫里的威望受到了影响）"
                $ my.exp = my.exp - 20 - (beifei-my.level)*2

        elif fz.love > 60 and suibianzefa == True:
            $ fz.tags.append(["身受杖责",0,""])
            我的宫女 "奴婢打听到皇上宠爱[fz.cheng]，听说被您责罚，这会儿很不高兴呢……"
            "（宠爱降低，并且在宫里的威望也受到了影响）"
            $ my.exp = my.exp- (beifei-my.level)*2
            $ my.love = my.love - fz.love/5
        elif fz.love > 60:
            $ fz.tags.append(["身受杖责",0,""])
            我的宫女 "奴婢打听到皇上宠爱[fz.cheng]，听说被您责罚，而且还听说了[fz.cheng]其实并没有犯什么大错，这会儿很不高兴呢……"
            "（宠爱降低，并且在宫里的威望也受到了影响）"
            $ my.love = my.love - fz.love/10
            $ my.exp = my.exp- (beifei-my.level)
        elif suibianzefa == True:
            $ fz.tags.append(["身受杖责",0,""])
            我的宫女 "宫里的人这会儿都在说您胡乱责罚低位嫔妃，个个都惶恐不安……"
            "（在宫里的威望受到了影响）"
            $ my.exp = my.exp- (beifei-my.level)*2
        else:
            $ fz.tags.append(["身受杖责",0,""])
            hide 我的宫女
            show myface at chara
            我 "知道了。"
            hide my face
        $ feizibeizhangze = False
        $ beizhangzefz= []
    else:
        pass



    if player == 0 and year >= 4 and my.love < 30 and month >= 11 and timenum == 1 and rongyu0 == False:
        $ rongyu0 = True
        $ bg("寝居")
        with dissolve
        我 "咳咳……"
        show 我的宫女 at chara
        我的宫女 "主子，您怎么了？ "
        我 "应当没有大碍，只是嗓子觉得有些不舒服。"
        我的宫女 "这几日天气转凉，您可要小心身子，莫要着凉了。"
        menu:
            我的宫女 "奴婢替您去太医院请太医来瞧瞧吧？"
            "去吧":
                我的宫女 "是，奴婢立即就去。"
                window show
                hide 我的宫女
                $ bg("寝居")
                with dissolve
                "片刻后，[my.Gongnv[0].name]回来了，身后却跟着个未曾见过的男子，打扮也与其他太医不同。"
                show 容予 at chara with dissolve
                "{color=#6495ED}男子" "见过……"
                hide 容予
                show 我的宫女 at chara
                我的宫女 "我们主子是[my.cheng]。"
                hide 我的宫女
                show 容予 at chara
                "{color=#6495ED}男子" "见过[my.cheng]。"
                我 "太医大人免礼。"
                hide 容予
                show 我的宫女 at chara
                我的宫女 "主子，这位……不是太医……"
                我 "（惊）[my.Gongnv[0].name]你这是何意？"
                我的宫女 "主子，近日天寒，宫里感染风寒者不在一二，再加上今日太医院有资历的太医都被召往建章，如此一来，人手更是不够。"
                menu:
                    我的宫女 "奴婢去太医院时，当值的只有几个入职不久的小医官……可奴婢担心您的身子，不得已请了容公子来。"
                    "容公子？":
                        pass
                    "不是太医为何会在太医院？":
                        pass
                hide 我的宫女
                show 容予 at chara
                "{color=#6495ED}男子" "恕在下唐突，在下名容予，家父为太医令，现下跟随家父学习医术，但并未入职太医院，一般也并不为后宫问诊。"
                容予 "今日在下见您的宫女着急，故而答应前来。"
                hide 容予
                show 我的宫女 at chara
                menu:
                    我的宫女 "（小声）主子放心，奴婢在太医院听那几个小医官说起，容予公子天赋异禀，医术超群，如今整个太医院里，论医术只在太医令大人之下，奴婢这才放心请他过来。"
                    "外人不得出入后宫，此举还是不妥":
                        pass
                    "原是如此":
                        pass
                我的宫女 "奴婢还听太医院的人说了，容予公子虽非太医，但因为太医令在宫中德高望重，因此对于容予公子的事情，各方都是默许了的，您不必担心。"
                我的宫女 "再者……今天太医大多去了建章宫，皇上早朝后肯定也会过去的，无人会顾忌此事，您且放心吧。"
                我的宫女 "现下还是您的身子要紧。"
                hide 我的宫女
                show 容予 at chara
                我 "那便有劳了。"
                容予 "是。"
                "把脉后……"
                menu:
                    容予 "并无大碍，待在下开个药方，连服三日即可。"
                    "多谢了":
                        pass
                容予 "（起身）[my.cheng]心头顾虑在下明白，便先告退了，让您的宫女跟在下去太医院一趟便是。"
                容予 "（不待你回应，行礼过后便朝外走去。）"
                hide 容予
                show 我的宫女 at chara
                我的宫女 "主子，那奴婢去了。"
                hide 我的宫女
                我 "（我的顾虑……？）"
                我 "（有这么明显吗……）"
                "未几，[my.Gongnv[0].name]带着药回来了，服下后确实感觉嗓子舒服了许多。"
                我 "（这位容予公子的医术还当真了得……）"
                "（体质上升。）"
                window hide
                $ rongyulike = rongyulike + 10
                $ my.health = my.health + 30
                $ timenum = timenum + 1
            "不必了":
                我的宫女 "那奴婢去给您烹一壶化痰润嗓的热茶吧。"
                hide 我的宫女
    else:


        pass

    if year>= 6 and mapname == "皇宫" and timenum > 1 and timenum < 5 and rongyu2 == True and rongyulike >= 30 and rongyu3 == False:
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
        $ rongyu3 = True
        "远远看到一个身影……"
        show 我的宫女 at chara
        我的宫女 "主子，太后娘娘在前边儿呢。"
        我 "上去问声安吧。"
        hide 我的宫女
        "你走近了些，太后正一心同莲稚说着话，并未察觉。"
        show 莲稚 at chara
        莲稚 "太后娘娘，您别忧心了，担心身子。"
        hide 莲稚
        show 太后 at chara
        太后 "白发，异瞳……那可不就是……"
        太后 "让哀家如何不忧心？"
        太后 "唉……哀家……"
        太后 "莲稚，哀家去奉天楼，现在便去！"
        hide 太后
        show 莲稚 at chara
        莲稚 "是，奴婢这就陪您去。"
        hide 莲稚
        我 "……"
        if my.xinji >500:
            我 "（白发……异瞳……）"
        else:
            我 "（还是改日再去建章宫请安吧。）"
    else:

        pass

    if my.love > 80 and taihou_zczz == False and jinzu(my) == False and huaiyun(my) == False:
        $ taihou_zczz = True
        call 太后_专宠指责 from _call_太后_专宠指责

    return




label 侍寝事件检测:
    hide screen myroom
    if timenum == 5 and shiqinfzlist == []:
        python:

            templist = []
            for i in NPC_Kids_list:
                if i.live == 0:
                    templist.append(i)
                else:
                    pass
            if len(templist) == 0 :
                pass
            else:
                tempkid = renpy.random.choice(templist)
                if tempkid.iq > 80 and tempkid.wen > 80 and tempkid.wu > 80:
                    tempkid.hdlike = tempkid.hdlike + 1
                elif tempkid.iq > 60 and tempkid.wen > 60 and tempkid.wu > 60:
                    tempkid.hdlike = tempkid.hdlike + 0.6
                elif tempkid.iq > 80 or tempkid.wen > 80 or tempkid.wu > 80:
                    tempkid.hdlike = tempkid.hdlike + 0.3
                else:
                    pass
                if tempkid.duli < 30 or tempkid.duli > 70:
                    tempkid.hdlike = tempkid.hdlike - 1
                else:
                    pass
                lucky = renpy.random.randint(0, 8)
                if lucky == 0:
                    templist = sorted(templist, key=attrgetter("age"),reverse = True)
                    templist[0].hdlike = templist[0].hdlike + 0.5
                elif lucky == 1:
                    templist = sorted(templist, key=attrgetter("iq"),reverse = True)
                    templist[0].hdlike = templist[0].hdlike + 0.5
                elif lucky == 2:
                    templist = sorted(templist, key=attrgetter("wen"),reverse = True)
                    templist[0].hdlike = templist[0].hdlike + 0.5
                elif lucky == 3:
                    templist = sorted(templist, key=attrgetter("mother.love"),reverse = True)
                    templist[0].hdlike = templist[0].hdlike + 0.5
                elif lucky == 4:
                    templist = sorted(templist, key=attrgetter("mother.level"),reverse = False)
                    templist[0].hdlike = templist[0].hdlike + 0.5
                elif lucky == 5 or lucky == 6 or lucky == 7:
                    tempkid = renpy.random.choice(templist)
                    tempkid.hdlike = tempkid.hdlike + 0.5
                else:
                    pass


            for i in NPC_fz_list:
                if i.love < -20:
                    pass
                elif jinzu(i) == True:
                    pass
                elif tags_yali[2] in i.tags:
                    pass
                elif tags[4] in i.tags:
                    pass
                elif i.state == "寻常"  or huaiyun(i) == True :
                    shiqinfzlist.append(i)
                else:
                    pass

            shiqinfzlist = sorted(shiqinfzlist, key=attrgetter("love"),reverse = True)
            for i in shiqinfzlist:
                if i.shiqin == 0 :
                    weishiqinfzlist.append(i)
                else:
                    pass


            if mustshiqin >=100  and my.love >= -20 and my in shiqinfzlist :
                shiqinfz = my
            elif len(shiqinfzlist) ==0:
                pass
            else:
                if hdxingge =="刚正":
                    lucky = renpy.random.randint(0,12)
                elif hdxingge == "风流":
                    lucky = renpy.random.randint(0,18)
                else:
                    lucky = renpy.random.randint(0,15)
                if len(shiqinfzlist) == 0:
                    pass
                elif lucky < 5:
                    if len(shiqinfzlist) ==0:
                        pass
                    elif len(shiqinfzlist) <= lucky:
                        a = len(shiqinfzlist)-1
                        shiqinfz = shiqinfzlist[a]
                    else:
                        if len(shiqinfzlist) < lucky:
                            shiqinfzlist = []
                        else:
                            a = lucky
                            shiqinfz = shiqinfzlist[a]
                
                elif lucky ==5 :
                    shiqinfz = shiqinfzlist[0]
                elif lucky ==6 :
                    shiqinfzlist = sorted(shiqinfzlist, key=attrgetter("level"),reverse = False)
                    shiqinfz = shiqinfzlist[0]
                elif lucky == 7 :
                    shiqinfzlist = []
                
                elif lucky < 10:
                    if len(weishiqinfzlist) == 0:
                        shiqinfz = renpy.random.choice(shiqinfzlist)
                    else:
                        weishiqinfzlist = sorted(weishiqinfzlist, key=attrgetter("familylevel"),reverse = False)
                        shiqinfz = weishiqinfzlist[0]
                else:
                    shiqinfz = renpy.random.choice(shiqinfzlist)



        if len(shiqinfzlist) == 0:
            pass
        else:

            $ shiqinfz.exp = shiqinfz.exp + 3
            if hdxingge =="风流":
                $ shiqinfz.love = shiqinfz.love + 2 +(shiqinfz.familylevel*0.1)
            else:
                $ shiqinfz.love = shiqinfz.love + 1 +(shiqinfz.familylevel*0.1)
            python:
                for i in NPC_fz_list:
                    if i == shiqinfz:
                        pass
                    else:
                        if hdxingge =="风流"  and i.love > 0 :
                            i.love = i.love - 0.6
                        else:
                            pass
                        if i.familylevel < 4 and i.love > 0:
                            pass
                        elif i.familylevel < 8 and i.love > 0:
                            i.love = i.love - 0.1
                        elif   i.love > 0:
                            i.love = i.love - 0.2
                        else:
                            pass
                        if i.love > 80:
                            i.love = i.love - 1.5
                        elif i.love > 50:
                            i.love = i.love - 0.75
                        elif i.love > 20:
                            i.love = i.love - 0.3
                        elif i.love> 10:
                            i.love = i.love - 0.1
                        else:
                            pass
                        if jinzu(i) == True:
                            i.love -= 1

        if chuhuan_time <= 4 and chuhuan_0 == True and chuhuan_1 == False:
            $ shiqinfzlist = []



        if len(shiqinfzlist) == 0:
            pass
        elif shiqinfz == my:
            if huaiyun(my) == True:
                $ bg("寝居")
                show 我的宫女 at chara
                我的宫女 "（面有喜色）[my.cheng]，皇上来看您了！"
                hide 我的宫女
                "宫人" "皇上到——"
                show 皇帝 at chara
                我 "臣妾参见皇上。"
                if hdxingge != "冷漠":
                    皇上 "爱妃快快请起。"
                    皇上 "如今你身怀皇嗣，不必多礼。"
                    我 "是。"
                else:
                    皇上 "免礼。"
                    皇上 "你身怀皇嗣，所以朕才来看看你。"
                    我 "是。"
                皇上 "身体可还好吧？"
                我 "回皇上，太医说臣妾这胎还算安稳。"
                皇上 "嗯，那便好。"
                皇上 "朕今晚留下来陪你。"
                $ my.exp = my.exp +5
                $ mustshiqin = 0
                python:
                    tempgnlist = []
                    for i in my.Gongnv:
                        if i.state != "寻常" and i== my.Gongnv[0] and i.level == "散役" and i.beauty < 100:
                            pass
                        elif i in teshugn:
                            pass
                        elif i.age < 14:
                            pass
                        else:
                            tempgnlist.append(i)
                    tempgnlist = sorted(tempgnlist, key=attrgetter("beauty"),reverse = True)
                menu:
                    "防BUG跳过":
                        皇上 "早些歇息。"
                    "多谢皇上":
                        皇上 "早些歇息。"
                        hide 皇帝
                        python:
                            global tempgnlist
                            tempgnlist = []
                            for i in my.Gongnv:
                                if i.state != "寻常" or i== my.Gongnv[0] or i.level == "散役" or i.yexin < 500 or i.yexin*0.1- i.like*0.5 < 70 or i.beauty < 200:
                                    pass
                                elif i.age > hdage + 5 or i.age <= 14:
                                    pass
                                elif i in teshugn:
                                    pass
                                else:
                                    tempgnlist.append(i)
                            tempgnlist = sorted(tempgnlist, key=attrgetter("yexin"),reverse = True)
                            if len(tempgnlist) == 0:
                                lucky = 1
                            else:
                                daixinggn = tempgnlist[0]
                                if hdxingge == "冷漠":
                                    lucky = renpy.random.randint(0, 30)
                                elif hdxingge == "风流":
                                    lucky = renpy.random.randint(0, 10)
                                else:
                                    lucky = renpy.random.randint(0, 20)
                                lucky = lucky - round(daixinggn.beauty/100)
                        if lucky == 0:
                            $ makeGongnv(my,1,"宫女",daixinggn.level)
                            $ my.Gongnv.remove(daixinggn)
                            $ Gongnvtofz(daixinggn,my,False)
                            "翌日……"
                            $ bg("寝居")
                            with fade
                            show 我的宫女 at chara
                            我的宫女 "主子！"
                            我 "发生什么事了……怎么没见[daixinggn.name]？"
                            我的宫女 "昨夜皇上留宿[my.qinju]，不知怎的，竟临幸了[daixinggn.name]……"

                            $ my.yali += 20
                            我 "怎么会这样……"
                        else:
                            pass

                    "宫女代幸" if tempgnlist>0:
                        menu:
                            "[tempgnlist[0].name]" if len(tempgnlist)>0:
                                $ daixinggn = tempgnlist[0]
                            "[tempgnlist[1].name]" if len(tempgnlist)>1:
                                $ daixinggn = tempgnlist[1]
                            "[tempgnlist[2].name]" if len(tempgnlist)>2:
                                $ daixinggn = tempgnlist[2]
                            "[tempgnlist[3].name]" if len(tempgnlist)>3:
                                $ daixinggn = tempgnlist[3]
                            "[tempgnlist[4].name]" if len(tempgnlist)>4:
                                $ daixinggn = tempgnlist[4]
                            "[tempgnlist[5].name]" if len(tempgnlist)>5:
                                $ daixinggn = tempgnlist[5]
                            "[tempgnlist[6].name]" if len(tempgnlist)>6:
                                $ daixinggn = tempgnlist[6]
                        $ gn = daixinggn
                        我 "臣妾有孕在身，不能侍奉皇上……不如……"
                        皇上 "爱妃有话直言。"
                        我 "臣妾身边有一位宫女，名叫[daixinggn.name]，清秀可人，不如让她今日代替臣妾侍奉皇上可好？"
                        if hdxingge == "冷漠":
                            $ lucky = renpy.random.randint(4, 6)
                        elif hdxingge == "风流":
                            $ lucky = renpy.random.randint(0, 6)
                        else:
                            $ lucky = renpy.random.randint(0, 10)
                        if lucky <= 5:
                            皇上 "爱妃既然有心如此，朕也不好拂了你的心意。"
                            我 "[daixinggn.name]。"
                            hide 皇帝
                            show gn at chara
                            if daixinggn.yexin < 700:
                                "[daixinggn.level] [daixinggn.name]" "（惶恐）主子……"
                            else:
                                "[daixinggn.level] [daixinggn.name]" "（欣喜）奴婢参见皇上……"
                            hide gn
                            show 皇帝 at chara
                            皇上 "过来。"
                            scene black
                            with fade

                            $ makeGongnv(my,1,"宫女",daixinggn.level)
                            $ my.Gongnv.remove(daixinggn)
                            $ Gongnvtofz(daixinggn,my,True)

                            $ my.exp = my.exp +10
                        else:
                            皇上 "（皱眉）朕今日没有兴致，不必多此一举。"
                            我 "是。"
                            hide 皇帝
                jump 结束本旬
            else:




                "敬事房报——"
                "今日[my.cheng]侍寝！"
                menu:
                    "前往侍寝":
                        python:
                            renpy.call("主角侍寝",from_current=False)
        else:

            if huaiyun(shiqinfz) == True or havetag("失心成疯",shiqinfz) == True:
                $ mustshiqin = mustshiqin +1
                "敬事房报——"
                "今日皇上看望[shiqinfz.hao][shiqinfz.weifen][shiqinfz.name]！"
            else:
                $ mustshiqin = mustshiqin +1
                "敬事房报——"
                $ shiqinfz.shiqin = shiqinfz.shiqin +1
                $ shiqinfz.exp = shiqinfz.exp + 4
                $ shiqinfz.love = shiqinfz.love + 2
                "今日[shiqinfz.hao][shiqinfz.weifen][shiqinfz.name]侍寝！"
                if hdxingge == "温柔":
                    if shiqinfz.meili*0.7+shiqinfz.qizhi*0.3 > 900:
                        $ shiqinfz.love = shiqinfz.love +8
                    elif shiqinfz.meili*0.7+shiqinfz.qizhi*0.3 > 700:
                        $ shiqinfz.love = shiqinfz.love +6
                    else:
                        $ shiqinfz.love = shiqinfz.love +4
                elif hdxingge == "风流":
                    if shiqinfz.beauty*0.7 +shiqinfz.meili*0.3 >900:
                        $ shiqinfz.love = shiqinfz.love +10
                    elif shiqinfz.beauty*0.7 +shiqinfz.meili*0.3 >700:
                        $ shiqinfz.love = shiqinfz.love +7
                    else:
                        $ shiqinfz.love = shiqinfz.love +5
                elif hdxingge == "刚正":
                    if shiqinfz.qizhi*0.7 +shiqinfz.beauty*0.3 >900:
                        $ shiqinfz.love = shiqinfz.love +6
                    elif shiqinfz.qizhi*0.7 +shiqinfz.beauty*0.3 >700:
                        $ shiqinfz.love = shiqinfz.love +4
                    else:
                        $ shiqinfz.love = shiqinfz.love +2
                elif hdxingge == "冷漠":
                    if shiqinfz.xinji < 100:
                        $ shiqinfz.love = shiqinfz.love +5
                    elif shiqinfz.xinji < 200:
                        $ shiqinfz.love = shiqinfz.love +4
                    elif shiqinfz.xinji < 400:
                        $ shiqinfz.love = shiqinfz.love +3
                    else:
                        $ shiqinfz.love = shiqinfz.love +3
                elif hdxingge == "腹黑":
                    if shiqinfz.xinji > 900:
                        $ shiqinfz.love = shiqinfz.love +5
                    elif shiqinfz.xinji > 800:
                        $ shiqinfz.love = shiqinfz.love +4
                    elif shiqinfz.xinji > 600:
                        $ shiqinfz.love = shiqinfz.love +3
                    else:
                        $ shiqinfz.love = shiqinfz.love +2
                else:
                    pass
    else:


        pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
