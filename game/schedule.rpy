label 结束本旬:

    hide screen gdjm_ready
    hide screen gdjm
    hide screen gdjm_end
    scene black



    $ timenum = 5
    $ zhengfeng = False
    $ pincha = False
    $ time_1 = False
    $ time_2 = False
    $ time_3 = False
    $ time_4 = False
    $ time_5 = False
    if shiqinfzlist == []:
        python:
            renpy.call("侍寝事件检测",from_current=False)
    else:
        pass


    if rongyu4 == True:
        $ rongyu5 =rongyu5 + 1
    else:
        pass
    if rongyu7 == True and rongyu9 == False:
        python:
            renpy.call("容予结局",from_current=False) 
    else:
        pass



    $ yeting = False

    if ygg_like >= 20:
        $ lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            $ ygg = True
        else:
            $ ygg = False
    else:
        $ ygg = False

    if 1 <= atan_time < 12:
        $ atan_time += 1
    if 1 <= chuhuan_time < 5:
        $ chuhuan_time += 1
    if chuhuan_5 == 2 and jinzu(my) == False:
        $ chuhuan_5 = 0
        call 楚欢_女主被罚 (fz=chuhuan_die) from _call_楚欢_女主被罚_1
    if chuhuan_5 == 1:
        $ chuhuan_5 = 3




    "一旬过去……（下一次侍寝的可能性为：[mustshiqin]）"
    if datenum == 3:
        $ gongxi = []
        $ xiluo = []
        $ ganxie = []
    else:
        pass
    $ yucilist = []
    $ liwulist = []
    $ datenum = datenum + 1
    $ timenum = 1
    $ yanhuitixingcishu = 0
    if my.level != beifei and len(my.Gongnv) == 1:
        $ newgn = renpy.random.choice(YTGongnv)
        $ YTGongnv.remove(newgn)
        $ my.Gongnv.append(newgn)
    else:
        pass



    if len(shiqinfzlist) == 0:
        pass
    elif shiqinfz == my:
        pass
    else:

        if hdxingge == "冷漠":
            $ lucky =  renpy.random.randint(0,30)
        elif hdxingge == "腹黑" or hdxingge == "温柔":
            $ lucky =  renpy.random.randint(0,50)
        elif hdxingge == "风流":
            $ lucky =  renpy.random.randint(0,52)
        else:
            $ lucky =  renpy.random.randint(0,40)
        if shiqinfz.meishu["一A"] == 0:
            pass
        else:
            $ shiqinfz.meili += 0.15 +0.25*(shiqinfz.meishu["一A"]-1)
            $ shiqinfz.health -= 5
            $ lucky =  renpy.random.randint(0,10)
            if lucky <= shiqinfz.meishu["一A"]:
                $ lucky = 30
            else:
                $ lucky = 1
        if lucky == 0 and huaiyun(shiqinfz) == False and shiqinfz not in juqingfei:
            $ shiqinfz.love = shiqinfz.love*0.8 - 5
            $ shiqinfz.exp = shiqinfz.exp - 15 - (beifei-shiqinfz.level)*3
            $ shiqinfz.tags.append(["禁足三月",0,""])

            $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在侍寝时言行无状，触怒龙颜，被禁足三月。\n"
            $ allstory.insert(0,tempstory2)
            $ xiluo.append([shiqinfz,"失宠"])
            if shiqinfz != my:
                python:
                    renpy.call("有人侍寝时失宠",fz = shiqinfz,from_current=False)
        elif lucky == 30 or lucky == 40 or lucky > 49:
            if huaiyun(shiqinfz) == False:
                $ shiqinfz.love = shiqinfz.love + 5
                $ shiqinfz.exp = shiqinfz.exp + 10 + (beifei-shiqinfz.level)*2
                $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在侍寝时博得帝心，皇上大悦，特允其留宿。\n"
                $ allstory.insert(0,tempstory2)
                if shiqinfz != my:
                    python:
                        renpy.call("有人侍寝时得宠",fz = shiqinfz,from_current=False)
            else:
                python:
                    renpy.call("宫女代幸",fz = shiqinfz,from_current=False)
        elif shiqinfz.love > 50 and shiqinfz.qingxiang > 70 and shiqinfz!= my and shiqinfz.state == "寻常":
            if len(shiqinfz.foes) == 0:
                python:
                    templist = []
                    for i in NPC_fz_list:
                        if i == shiqinfz:
                            pass
                        else:
                            templist.append(i)
                $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
                $ tempfz = templist[0]
                if tempfz == shiqinfz:
                    $ tempfz = templist[1]
                else:
                    pass
                if shiqinfz.meishu["一A"] == 0:
                    $ tempfz.love -= shiqinfz.love*0.1
                    $ tempfz.exp -= shiqinfz.love*0.1
                else:
                    $ tempfz.love -= shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01
                    $ tempfz.exp -= shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01

                $ shiqinfz.love = shiqinfz.love -  1
                if huaiyun(shiqinfz) == False:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在侍寝时说了"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"的坏话。\n"
                else:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在皇上面前说了"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"的坏话。\n"

                $ allstory.insert(0,tempstory2)
                if tempfz == my:
                    python:
                        renpy.call("有人侍寝时说我坏话",fz = shiqinfz,from_current=False)
                else:
                    pass
            else:
                $ tempfz = renpy.random.choice(shiqinfz.foes)
                if shiqinfz.meishu["一A"] == 0:
                    $ tempfz.love -= shiqinfz.love*0.1
                    $ tempfz.exp -= shiqinfz.love*0.1
                else:
                    $ tempfz.love -= shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01
                    $ tempfz.exp -= shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01
                $ shiqinfz.love = shiqinfz.love -  1
                if huaiyun(shiqinfz) == False:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在侍寝时说了"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"的坏话。\n"
                else:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在皇上面前说了"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"的坏话。\n"
                $ allstory.insert(0,tempstory2)
                if tempfz == my:
                    python:
                        renpy.call("有人侍寝时说我坏话",fz = shiqinfz,from_current=False)
                else:
                    pass


        elif shiqinfz.love > 50 and shiqinfz.qingxiang < 30 and shiqinfz!= my and shiqinfz.state == "寻常":
            if len(shiqinfz.friends) == 0:
                pass
            else:
                $ tempfz = renpy.random.choice(shiqinfz.friends)
                if shiqinfz.meishu["一A"] == 0:
                    $ tempfz.love += shiqinfz.love*0.1
                    $ tempfz.exp += shiqinfz.love*0.1
                else:
                    $ tempfz.love += shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01
                    $ tempfz.exp += shiqinfz.love*0.1*(100+ (shiqinfz.meishu["一A"]+1)*25)*0.01
                $ shiqinfz.love = shiqinfz.love -  1
                if huaiyun(shiqinfz) == False:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在侍寝时替"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"美言几句。\n"
                else:
                    $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "在皇上面前替"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"美言几句。\n"
                $ allstory.insert(0,tempstory2)
                if tempfz == my:
                    $ ganxie.append([shiqinfz,"美言"])
                    python:
                        renpy.call("有人侍寝时说我好话",fz = shiqinfz,from_current=False)
                else:
                    pass
        else:
            pass


    if len(shiqinfzlist) != 0 and huaiyun(shiqinfz) == False and tags[6] not in shiqinfz.tags:
        python:
            tempnum = 0
            for i in shiqinfz.kids:
                if i.shengmu != shiqinfz:
                    pass
                else:
                    tempnum += 1
        $ tempnum -= 1
        if tempnum <= 0:
            $ tempnum = 0
        else:
            pass
        if shiqinfz.lucky >= 100 and tempnum == 0:
            $ lucky =  0
        elif shiqinfz.lucky < 0 or shiqinfz.health < 100:
            $ lucky =  1
        elif shiqinfz.age > 35 or hdage > 50:
            $ lucky =  1
        else:
            $ tempnum2 = 10 - round(shiqinfz.lucky*0.1) + 10 - round(shiqinfz.health*0.01) + tempnum*5

            if tempnum2 <= 1:
                $ lucky = 1
            else:
                $ lucky = renpy.random.randint(0,tempnum2)

        if shiqinfz == my and my.meishu["三级"] != 0:
            我 "（是否要发动【假孕】技能？）"
            menu:
                "立即准备":
                    $ my.jiayun = True
                    $ lucky = 0
                "日后再议":
                    pass
        elif shiqinfz.meishu["三级"] != 0:
            $ tempnum = 10 - int(shiqinfz.qingxiang*0.1)
            if tempnum <= 0:
                $ shiqinfz.jiayun = True
            else:
                $ tempnum3 = renpy.random.randint(0,tempnum)
                if tempnum3 == 0:
                    $ shiqinfz.jiayun = True
                else:
                    pass


        if lucky == 0:

            if shiqinfz == my:
                "太医例行来为你把脉，随后面色异常地跪了下来，口中高喊“恭喜[my.cheng]！贺喜[my.cheng]！您有孕了！”"
                "此事很快传遍了后宫……"
            else:
                "太医院传来消息，[shiqinfz.hao][shiqinfz.weifen][shiqinfz.name]有孕了……"
            $ tempstory = str(year)+"年"+str(month)+"月，有孕。\n"
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+ str(shiqinfz.hao)+str(shiqinfz.weifen)+str(shiqinfz.name) + "被诊出怀有龙嗣。\n"
            $ shiqinfz.story.append(tempstory)
            $ allstory.insert(0,tempstory2)
            $ shiqinfz.tags.append(["身怀皇嗣",0,""])
            if persistent.expspeed == 1:
                $ shiqinfz.exp = shiqinfz.exp + 20 + (16-shiqinfz.level)*3
            elif persistent.expspeed == 0:
                $ shiqinfz.exp = shiqinfz.exp + 10 + (16-shiqinfz.level)*1.5
            else:
                $ shiqinfz.exp = shiqinfz.exp + 40 + (16-shiqinfz.level)*6
            $ shiqinfz.taihoulike = shiqinfz.taihoulike + 5
            $ shiqinfz.love =  shiqinfz.love + shiqinfz.love*0.1 + 10
            $ gongxi.append([shiqinfz,"怀孕"])
        else:

            if shiqinfz.shiqin ==1:
                $ shiqinfz.exp = shiqinfz.exp + 3 + (shiqinfz.familylevel-5)*0.5
            else:
                pass
    else:
        pass
    $ mysqfail = False
    $ shiqinfzlist = []
    $ mysqnice = False
    $ weishiqinfzlist= []



    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
    if xuanxiutime == 36 and NPC_fz_list[0] != my:
        $ NPC_newfz_list = []
        $ xiunvnum = renpy.random.randint(5,8)
        $ Creat_Feizi(xiunvnum,1)
        $ xuanxiutime = 0
        $ tempnum = len(NPC_newfz_list)
        $ tempstory = "【大事】"+str(year)+"年"+str(month)+"月，新秀入宫，共"+str(xiunvnum)+"人。\n"
        $ allstory.insert(0,tempstory)
        "选秀之日已至，又有数名新秀入宫。"
    else:
        pass
    call 过月事件检测 from _call_过月事件检测
    python:
        pinganmai = 0
        zaoyaocishu = 0

        if beizhangze20 == True:
            if beizhangzetime == 0:
                my.health = (my.health - 100)*0.5
            elif beizhangzetime < 6:
                my.helath = my.health *1.1
            else:
                beizhangze20 = False
                beizhangzetime = 0
        else:
            pass


        for i in my.Gongnv:
            if i.state == "任务中":
                i.state = "寻常"
            elif i.like >= 50 or yxxiao in my.Gongnv:
                pass
            else:
                i.like = i.like + 0.5



        if datenum == 2 or datenum == 3 :
            pass
        else:
            xuanxiutime =  xuanxiutime+1
            datenum = 1
            month = month+1
            for i in NPC_fz_list:
                if i.tequan1 == -1 or i.tequan1 == 0:
                    pass
                else:
                    i.tequan1 -= 1
            for i in guanyuan_list:
                if i.marry == False:
                    lucky = renpy.random.randint(0,100)
                    if lucky == 0:
                        i.marry = True
            for i in daixuan_erxi:
                lucky = renpy.random.randint(0,100)
                if lucky == 0 or i.age > 18:
                    daixuan_erxi.remove(i)
            if chun in my.Gongnv:
                my.health= my.health + renpy.random.randint(2,4)
            elif xia in my.Gongnv:
                my.beauty= my.beauty + renpy.random.randint(1,2)
                my.meili= my.meili + renpy.random.randint(1,2)
                money = money - (beifei-my.level)*(xia.yexin/200)*0.2
            elif qiu in my.Gongnv:
                my.qizhi= my.qizhi + renpy.random.randint(2,4)
            elif dong in my.Gongnv:
                money = money + (1000-dong.yexin)/200*(beifei-my.level)*0.2
                lucky =  renpy.random.randint(1,4)
                if lucky ==  1:
                    my.muzic = my.muzic + (1000-dong.yexin)/500
                elif lucky ==  2:
                    my.muzic = my.muzic + (1000-dong.yexin)/500
                elif lucky ==  3:
                    my.book = my.book + (1000-dong.yexin)/500
                else:
                    my.cixiu = my.cixiu + (1000-dong.yexin)/500
            else:
                pass
            
            
            
            if kaixiao == 1 and my.level != beifei:
                zhichu = int(weifen_list[my.level][6]*0.25)
                my.health = my.health - renpy.random.randint(0,2)
                my.exp = my.exp - (beifei-my.level)*renpy.random.randint(8,12)/15
            elif kaixiao == 2 and my.level != beifei:
                zhichu = int(weifen_list[my.level][6]*0.5)
            elif kaixiao == 3 and my.level != beifei:
                zhichu = int(weifen_list[my.level][6]*0.75)
                my.health = my.health + renpy.random.randint(1,3)
                my.exp = my.exp + (beifei-my.level)*renpy.random.randint(8,12)/10
            else:
                zhichu = 0
            if my.level == 0 and len(my.Gongnv)>10:
                zhichu = zhichu + len(my.Gongnv)*3 - 10*3
            elif my.level == 0:
                pass
            elif my.level < 4  and len(my.Gongnv)>7:
                zhichu = zhichu + len(my.Gongnv)*3 - 7*3
            elif my.level < 4:
                pass
            elif my.level < 8  and len(my.Gongnv)>4:
                zhichu = zhichu + len(my.Gongnv)*3 - 4*3
            elif my.level < 8:
                pass
            elif my.level < 13  and len(my.Gongnv)>3:
                zhichu = zhichu + len(my.Gongnv)*3 - 3*3
            elif my.level < 13:
                pass
            elif len(my.Gongnv)>2:
                zhichu = zhichu + len(my.Gongnv)*2 - 10*2
            else:
                pass
            money = money - zhichu


    python:
        if month < 13:
            pass

        else:
            month = 1
            year = year + 1
            taihouage = taihouage + 1
            hdage = hdage + 1
            for i in NPC_fz_list:
                i.skillcosts += 3
                i.year = i.year+ 1
                i.age = i.age + 1
                if i == taoning:
                    i.skillcosts += 3
                if i in taoning.friends:
                    i.skillcosts += 3
                if i.year >=10:
                    i.exp = i.exp + 20
                for j in i.Gongnv:
                    j.age = j.age + 1
                if i.father == "" or isinstance(i.father,NoneType) == True:
                    pass
                elif i.father in guanyuan_list:
                    pass
                else:
                    i.father.age += 1
            for i in NPC_fz_feilist:
                i.year = i.year+ 1
                i.age = i.age + 1
                if i.father == "" or isinstance(i.father,NoneType) == True:
                    pass
                elif i.father in guanyuan_list:
                    pass
                else:
                    i.father.age += 1
            for i in NPC_fz_dielist:
                if i.father == "" or isinstance(i.father,NoneType) == True:
                    pass
                elif i.father in guanyuan_list:
                    pass
                else:
                    i.father.age += 1
            for i in guanyuan_list:
                i.age += 1
            for i in NPC_Kids_list:
                if i.live == -1:
                    pass
                else:
                    i.age = i.age + 1
                    if i.age == 4 and i.sex == "皇子":
                        i.face = "B" +  str(renpy.random.choice(range(101,125)))
                    elif i.age == 4 and i.sex == "公主":
                        i.face = "G" +  str(renpy.random.choice(range(101,131)))
                    elif i.age == 15 and i.sex == "皇子":
                        i.face = "B" +  str(renpy.random.choice(range(201,239)))
                    elif i.age == 15 and i.sex == "公主":
                        i.face = "G" +  str(renpy.random.choice(range(201,229)))
                    else:
                        pass
            for i in YTGongnv:
                i.age = i.age + 1
                if i.age >= 25 and i not in teshugn:
                    YTGongnv.remove(i)
                else:
                    pass
            makeYTGongnv(10,"宫女")


        if year == 8 and player == 1:
            if sidi in NPC_fz_list:
                if my.level >= sidi.level or my.exp <= sidi.level or my.love <= sidi.love or len(my.kids) == 0:
                    renpy.call("应福遥结局_失败",from_current=False)
                else:
                    renpy.call("应福遥结局_成功",from_current=False)
            else:
                renpy.call("应福遥结局_成功",from_current=False)
        else:
            pass




    if datenum == 2 or datenum == 3:
        pass
    elif my.level != beifei:
        $ huilu = 0
        $ wenyao = False
        if my.love <0:
            $ lucky =  renpy.random.randint(0,3)
            if lucky == 0:
                $ newmoney = 0
                "本月没有收到月俸……"
            elif lucky == 3:
                $ newmoney = int(weifen_list[my.level][6]*0.5)
                "本月俸禄只收到了[newmoney]两……似乎是被掖廷的宫人克扣了。"
            else:
                $ newmoney = int(weifen_list[my.level][6])
                "本月收到了俸禄[newmoney]两。"
        elif my.love < 10:
            $ lucky =  renpy.random.randint(0,3)
            if lucky == 0:
                $ newmoney = int(weifen_list[my.level][6]*0.7)
                "本月俸禄只收到了[newmoney]两……似乎是被掖廷的宫人克扣了。"
            else:
                $ newmoney = int(weifen_list[my.level][6])
                "本月收到了俸禄[newmoney]两。"
        elif my.love > 50:
            $ lucky =  renpy.random.randint(0,3)
            if lucky == 0:
                $ newmoney = int(weifen_list[my.level][6]*1.2)
                "本月俸禄收到了[newmoney]两……似乎是掖廷的宫人有意讨好。"
            else:
                $ newmoney = int(weifen_list[my.level][6])
                "本月收到了俸禄[newmoney]两。"
        elif my.love > 80:
            $ lucky =  renpy.random.randint(0,3)
            if lucky == 0:
                $ newmoney = int(weifen_list[my.level][6]*1.5)
                "本月俸禄收到了[newmoney]两……似乎是掖廷的宫人有意讨好。"
            elif lucky == 3:
                $ newmoney = int(weifen_list[my.level][6]*1.3)
                "本月俸禄收到了[newmoney]两……似乎是掖廷的宫人有意讨好。"
            else:
                $ newmoney = int(weifen_list[my.level][6])
                "本月收到了俸禄[newmoney]两。"
        else:
            $ newmoney = int(weifen_list[my.level][6])
            "本月收到了俸禄[newmoney]两。"


        $ money = money + newmoney
    else:
        pass

    if month > 1 and month < 5:
        $ map1 = "春"
    elif month > 4 and month < 8:
        $ map1 = "夏"
    elif month > 7 and month < 11:
        $ map1 = "秋"
    else:
        $ map1 = "冬"

    python:
        for i in NPC_fz_list:
            i.paixu = beifei - i.level
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
    $ NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("paixu"),reverse = False)
    $ my.Gongnv = sorted(my.Gongnv, key=attrgetter("lv"),reverse = False)
    python:
        if my.level == beifei:
            for i in my.Gongnv:
                if i.lv == 5:
                    my.Gongnv.remove(i)
                else:
                    pass
        else:
            pass
        for i in  NPC_fz_list:
            i.foes  = set(i.foes)
            i.foes = list(i.foes)
            i.friends = set(i.friends)
            i.friends = list(i.friends)
            for j in i.foes:
                if j in NPC_fz_dielist:
                    i.foes.remove(j)
            for j in i.friends:
                if j in NPC_fz_dielist:
                    i.friends.remove(j)
            i.kids = sorted(i.kids, key=attrgetter("paixu"),reverse = False)
        templist = []
        templist = sorted(NPC_fz_list, key=attrgetter("love"),reverse = True)
        if len(templist) == 0:
            pass
        else:
            if templist[0].love >= 80:
                for i in templist[1:-1]:
                    if i.love >= 80:
                        i.love = 80



    python:
        my.ap = AP
        for i in NPC_fz_list:
            if i.AP < 0 :
                i.health = i.health - 20
            else:
                pass
            if huaiyun(i) == True and i.jiayun == False or i.state == "抱恙" or i.state == "病重":
                if i.health > 700:
                    i.AP = i.AP+3
                
                else:
                    i.AP = i.AP+ 1
            else:
                if i.health > 900:
                    i.AP = i.AP + 5
                elif i.health > 700:
                    i.AP = i.AP + 4
                elif i.health > 400:
                    i.AP =i.AP + 3
                elif i.health > 200:
                    i.AP =i.AP + 2
                elif i.health > 100:
                    i.AP = i.AP + renpy.random.randint(1,2)
                else:
                    i.AP = 1
            if havetag("生性懒惰",i) == True :
                if i.health <= 800:
                    i.health += 0.5
                if i.AP > 0:
                    i.AP -= 1
            if havetag("夙兴夜寐",i) == True :
                if i.health > 200:
                    i.health -= 0.5
                i.AP += 1
            if havetag("嗜甜之人",i) == True :
                if i.health <= 800:
                    i.health += 0.5
                if i.beauty > 200:
                    i.beauty -= 0.5
            if havetag("喜食辛辣",i) == True :
                if i.health > 200:
                    i.health -= 0.5
                if i.beauty <= 800:
                    i.beauty += 0.5
            if i.AP > 5:
                i.AP = 5
            else:
                pass

        AP =my.AP

    jump 寝居界面


screen practice(list):
    style_prefix "choice"
    $ next_choice_page = choice_page + 1
    $ prev_choice_page = choice_page - 1
    $ max_choice_page = int(math.modf(len(list)/6)[1])
    $ b = choice_page*6+6
    $ c = list[next_choice_page*6:next_choice_page*6+6]


    if b >= len(list):
        $ b = len(list)
    else:
        pass

    vbox:
        for i in list[choice_page*6:b]:
            textbutton i.name + "（熟练度："+str(int(i.wcd))+"）" action SetVariable('choice_page', 0),SetVariable("puzi",i),Hide("practice"),Return()
        textbutton "练习基本功" action SetVariable('choice_page', 0),SetVariable("puzi",None),Hide("practice"),Return()
        if choice_page > 0:
            textbutton "上一页" action SetVariable('choice_page', prev_choice_page)
        if choice_page < max_choice_page and max_choice_page > 1 and len(c)>0:
            textbutton "下一页" action SetVariable('choice_page', next_choice_page)


label 练习音律:
    if havetag("声音嘶哑",my) == True:
        $ lv = 0.5
    elif havetag("声如莺啼",my) == True:
        $ lv = 1
    else:
        $ lv = 0.75
    if my.meishu["初始"] == 1:
        $ lv *= 1.15
    if my.meishu["初始"] == 2:
        $ lv *= 1.3
    if my.meishu["初始"] == 3:
        $ lv *= 1.5
    if my.meishu["初始"] == 1:
        $ my.meili += 0.15
        $ AP -= 1
    if my.meishu["初始"] == 2:
        $ my.meili += 0.3
        $ AP -= 1
    if my.meishu["初始"] == 3:
        $ my.meili += 0.5
        $ AP -= 1
    show 练习音律 at cg
    python:
        templist = []
        for i in kufang:
            if i.leibie == "曲谱":
                templist.append(i)
            else:
                pass
    call screen practice(templist)
    if puzi == None:
        if my.muzic > 80:
            $ my.muzic = my.muzic + 0.5*lv
            $ my.qizhi = my.qizhi + my.qizhi*0.001*lv
            "对音律的感悟有所提升。"
        elif my.muzic > 50:
            $ my.qizhi = my.qizhi + my.qizhi*0.001*lv
            $ my.muzic = my.muzic + renpy.random.randint(4,8)*0.1*lv
            "练习卓有成效。"
        else:
            $ my.qizhi = my.qizhi + my.qizhi*0.001*lv
            $ my.muzic = my.muzic + renpy.random.randint(6,12)*0.1*lv
            "进步显著。"
    else:
        if puzi.wcd >= 200:
            $ puzi.wcd =200
            "练习已达完美，无法再继续提升。"
        elif puzi.wcd >= 100+my.muzic*lv:
            $ puzi.wcd = 100+my.muzic*lv
            "练习达到了瓶颈，需要再进一步提升技艺方可有所突破。"
        else:
            if my.muzic > 80:
                $ my.muzic = my.muzic + (puzi.level*0.1)*lv
                $ puzi.wcd  = puzi.wcd + (45-puzi.level*5)*lv
            elif my.muzic >50:
                $ my.muzic = my.muzic + (puzi.level*0.2)*lv
                $ puzi.wcd  = puzi.wcd + (40-puzi.level*5)*lv
            elif my.muzic > 30:
                $ my.muzic = my.muzic + (puzi.level*0.3)*lv
                $ puzi.wcd  = puzi.wcd + (35-puzi.level*5)*lv
            elif my.muzic >15:
                $ my.muzic = my.muzic + (puzi.level*0.4)*lv
                $ puzi.wcd  = puzi.wcd + (30-puzi.level*5)*lv
            elif my.muzic >5:
                $ my.muzic = my.muzic + (puzi.level*0.5)*lv
                $ puzi.wcd  = puzi.wcd + (25-puzi.level*5)*lv
            else:
                $ my.muzic = my.muzic + (puzi.level*0.6)*lv
                $ puzi.wcd  = puzi.wcd + (20-puzi.level*5)*lv
            if puzi.wcd >= 200:
                $ puzi.wcd =200
                "练习已达完美，无法再继续提升。"
                if puzi == music09:
                    $ my.qizhi = my.qizhi + 2
                    "气质有所提升。"
            elif puzi.wcd >= 100+my.muzic*lv  and puzi != music09:
                $ puzi.wcd = 100+my.muzic*lv
                "练习达到了瓶颈，需要再进一步提升技艺方可有所突破。"
            else:
                "熟练度上升。"


    hide 练习音律
    $ tags_limitcheck(my)
    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum + 1
        $ AP = AP - 1
        jump 寝居界面


label 训练舞技:
    if havetag("身姿曼妙",my) == True:
        $ lv = 1
    elif havetag("四肢崎拙",my) == True:
        $ lv = 0.5
    else:
        $ lv = 0.75
    if my.meishu["初始"] == 1:
        $ lv *= 1.15
    if my.meishu["初始"] == 2:
        $ lv *= 1.3
    if my.meishu["初始"] == 3:
        $ lv *= 1.5
    if my.meishu["初始"] == 1:
        $ my.meili += 0.15
        $ AP -= 1
    if my.meishu["初始"] == 2:
        $ my.meili += 0.3
        $ AP -= 1
    if my.meishu["初始"] == 3:
        $ my.meili += 0.5
        $ AP -= 1
    show 训练舞技 at cg
    python:
        templist = []
        for i in kufang:
            if i.leibie == "舞谱":
                templist.append(i)
            else:
                pass
    call screen practice(templist)
    if puzi == None:
        if my.dance > 80:
            $ my.dance = my.dance + 0.5*lv
            $ my.meili += my.meili*0.001*lv
            "对舞蹈的感悟有所提升。"

        elif my.dance > 50:
            $ my.meili += my.meili*0.001*lv
            $ my.dance = my.dance + renpy.random.randint(4,8)*0.1*lv
            "练习卓有成效。"
        else:
            $ my.meili +=  my.meili*0.001*lv
            $ my.dance = my.dance + renpy.random.randint(6,12)*0.1*lv
            "进步显著。"
    else:
        if puzi.wcd >= 200:
            $ puzi.wcd =200
            "练习已达完美，无法再继续提升。"
        elif puzi.wcd >= 100+my.dance*lv:
            $ puzi.wcd = 100+my.dance*lv
            "练习达到了瓶颈，需要再进一步提升技艺方可有所突破。"
        else:
            if my.dance > 80:
                $ my.dance = my.dance + (puzi.level*0.1)*lv
                $ puzi.wcd  = puzi.wcd + (45-puzi.level*5)*lv
            elif my.dance >50:
                $ my.dance = my.dance + (puzi.level*0.2)*lv
                $ puzi.wcd  = puzi.wcd + (40-puzi.level*5)*lv*lv
            elif my.dance > 30:
                $ my.dance = my.dance + (puzi.level*0.3)*lv
                $ puzi.wcd  = puzi.wcd + (35-puzi.level*5)*lv
            elif my.dance >15:
                $ my.dance = my.dance + (puzi.level*0.4)*lv
                $ puzi.wcd  = puzi.wcd + (30-puzi.level*5)*lv
            elif my.dance >5:
                $ my.dance = my.dance + (puzi.level*0.5)*lv
                $ puzi.wcd  = puzi.wcd + (25-puzi.level*5)*lv
            else:
                $ my.dance = my.dance + (puzi.level*0.6)*lv
                $ puzi.wcd  = puzi.wcd + (20-puzi.level*5)*lv
            if puzi.wcd >= 200:
                $ puzi.wcd =200
                "练习已达完美，无法再继续提升。"
                if puzi == dance09:
                    $ my.meili = my.meili + 2
                    "魅力有所提升。"
            elif puzi.wcd >= 100+my.dance*lv and puzi != dance09:
                $ puzi.wcd = 100+my.dance*lv
                "练习达到了瓶颈，需要再进一步提升技艺方可有所突破。"
            else:
                "熟练度上升。"
    hide 训练舞技
    $ tags_limitcheck(my)
    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum + 1
        $ AP = AP - 1
        jump 寝居界面

label 研读诗书:
    if huaiyun(my) == True and my.love >= 20 and my.book >= 80:
        $ lucky = renpy.random.randint(0,30)
        if lucky == 0:
            jump 太后考才艺
        else:
            pass

    if havetag("耳聪目明",my) == True:
        $ lv = 0.7
    elif havetag("木讷愚钝",my) == True:
        $ lv = 1.2
    else:
        $ lv = 1
    if my.fangyu["初始"] == 0:
        pass
    elif my.fangyu["初始"] == 1:
        $ lv *=1.1
        $ my.xinji += 0.1
    elif my.fangyu["初始"] == 2:
        $ lv *=1.2
        $ my.xinji += 0.2
    elif my.fangyu["初始"] == 3:
        $ lv *=1.3
        $ my.xinji += 0.3
    show 研读诗书 at cg
    "在寝居中研读诗书。"
    if my.book > 80:
        $ lucky = renpy.random.randint(0,10)
        if lucky < 20:
            $ my.book = my.book + lv* 0.5
            "从研读中又学到了新的知识。"
        else:
            $ my.book = my.book + lv* 0.3
            "研读陷入瓶颈，没有太大效果。"

    elif my.book > 50:
        $ my.book = my.book + lv* renpy.random.randint(4,8)*0.1
        "在研读之中有许多新的感悟。"
    else:

        $ my.book = my.book + lv* renpy.random.randint(6,12)*0.1
        "在研读之中收获颇丰。"

    hide 研读诗书
    $ tags_limitcheck(my)

    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum + 1
        $ AP = AP - 1
        jump 寝居界面



label 女红刺绣:
    if havetag("心细手巧",my) == True:
        $ lv = 0.7
    elif havetag("粗枝大叶",my) == True:
        $ lv = 1.2
    else:
        $ lv = 1
    show 女红刺绣 at cg
    "在寝居中刺绣。"
    if cixiujindu == 0 and my.cixiu > 80:
        $ newcixiu = renpy.random.randint(5,10)
    elif cixiujindu == 0 and my.cixiu > 50:
        $ newcixiu = renpy.random.randint(5,12)
    elif cixiujindu == 0 and my.cixiu > 30:
        $ newcixiu = 9
    elif cixiujindu == 0 and my.cixiu > 15:
        $ newcixiu = renpy.random.randint(7,10)
    elif cixiujindu == 0 and my.cixiu <=15:
        $ newcixiu = renpy.random.randint(5,12)
    else:
        pass

    if my.cixiu > 80:
        $ lucky = renpy.random.randint(0,10)
        if lucky < 20:
            $ my.cixiu = my.cixiu + lv* 0.5
            $ cixiujindu = cixiujindu + lv* 1
            "今日刺绣的成果可谓是精美绝伦。"
        else:
            $ cixiujindu = cixiujindu + lv* 2
            "认真制作绣品，未有太大进步，但绣品愈发完善。"
    elif my.cixiu > 50:
        $ cixiujindu = cixiujindu + lv* 1
        $ my.cixiu = my.cixiu + lv* renpy.random.randint(4,8)*0.1
        "刺绣手艺精进不少。"
    else:
        $ cixiujindu = cixiujindu + lv* 1
        $ my.cixiu = my.cixiu + lv* renpy.random.randint(6,12)*0.1
        "学到了新的刺绣手法。"
    hide 女红刺绣

    if my.cixiu > 50 and cixiujindu >= newcixiu and newcixiu< 7:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "双面云纹囊完成。（已放入库房）"
            $ kufang.append(xiupin04)
        else:
            "双莲并蒂图完成。（已放入库房）"
            $ kufang.append(xiupin03)
    elif my.cixiu > 50 and cixiujindu >= newcixiu and newcixiu< 9:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "金缕蝶纹袋完成。（已放入库房）"
            $ kufang.append(xiupin05)
        else:
            "宝相花纹袋完成。（已放入库房）"
            $ kufang.append(xiupin06)
    elif my.cixiu > 50 and cixiujindu >= newcixiu:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "凤凰于飞图完成。（已放入库房）"
            $ kufang.append(xiupin07)
        else:
            "望舒御月图完成。（已放入库房）"
            $ kufang.append(xiupin08)
    elif my.cixiu > 50 and cixiujindu >= newcixiu:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "凤凰于飞图完成。（已放入库房）"
            $ kufang.append(xiupin07)
        else:
            "望舒御月图完成。（已放入库房）"
            $ kufang.append(xiupin08)
    elif my.cixiu > 30 and cixiujindu >= newcixiu:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "金缕蝶纹袋完成。（已放入库房）"
            $ kufang.append(xiupin05)
        else:
            "宝相花纹袋完成。（已放入库房）"
            $ kufang.append(xiupin06)
    elif my.cixiu > 15 and cixiujindu >= newcixiu:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "双面云纹囊完成。（已放入库房）"
            $ kufang.append(xiupin04)
        else:
            "双莲并蒂图完成。（已放入库房）"
            $ kufang.append(xiupin03)
    elif my.cixiu > 5 and cixiujindu >= newcixiu:
        $ cixiujindu = 0
        $ lucky =  renpy.random.randint(0,1)
        if lucky == 0:
            "牡丹丝巾完成。（已放入库房）"
            $ kufang.append(xiupin01)
        else:
            "荷纹丝巾完成。（已放入库房）"
            $ kufang.append(xiupin02)
    else:

        pass

    $ tags_limitcheck(my)
    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum +  1
        $ AP = AP - 1
        jump 寝居界面

label 请平安脉:
    if pinganmai == 0:
        $ pinganmai = 1

        if rongyu == True and rongyu4 == False:
            $ lucky = renpy.random.randint(0, 2)
        else:
            $ lucky = 1
        if lucky == 0:
            $ rongyulike = rongyulike + 2
            show 容予 at chara
            容予 "见过[my.cheng]。"
            我 "有劳了。"
            hide 容予
            "片刻后……"
            if my.health > 900:
                $ lucky = renpy.random.randint(0,10)
                if lucky < 20:
                    $ my.health = my.health + 1
                    "虽然你的身体已经非常康健，但容予又给你开了一些强身健体的方子。"
                else:
                    $ my.health = my.health + 0.5
                    "容予告知你你的身体非常康健，只需要保持现状即可。"
            elif my.health > 400:
                $ my.health = my.health + renpy.random.randint(2,5)
                "容予为你把脉，并给了你一些强身健体的方子。"
            else:
                $ my.health = my.health + renpy.random.randint(4,8)
                "容予为你把脉，并告知你如何让身体变得康健。"
            if rongyulike >= 100:
                $ lucky = 1
            else:
                $ lucky = (110-rongyulike)*0.1
            $ lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                if rongyulike > 80 and medic04 not in kufang:
                    show 容予 at chara
                    容予 "这[medic04.name]对身体有好处，你收下吧。"
                    hide 容予
                    "未等你道谢，容予已经起身离。"
                    $ kufang.append(medic04)
                    "得到了[medic04.name]×1。"
                elif rongyulike > 60:
                    show 容予 at chara
                    容予 "这[medic03.name]对身体有好处，你收下吧。"
                    hide 容予
                    "未等你道谢，容予已经起身离开。"
                    $ kufang.append(medic03)
                    "得到了[medic03.name]×1。"
                elif rongyulike > 40:
                    show 容予 at chara
                    容予 "这[medic02.name]对身体有好处，你收下吧。"
                    hide 容予
                    "未等你道谢，容予已经起身离开。"
                    $ kufang.append(medic02)
                    "得到了[medic02.name]×1。"
                elif rongyulike > 20:
                    show 容予 at chara
                    容予 "这[medic01.name]对身体有好处，你收下吧。"
                    hide 容予
                    "未等你道谢，容予已经起身离开。"
                    $ kufang.append(medic01)
                    "得到了[medic01.name]×1。"
                else:
                    pass
            else:
                pass
        else:




            show 请平安脉 at cg
            "你请了太医来为自己把脉。"

            if my.health > 900:
                $ lucky = renpy.random.randint(0,10)
                if lucky < 20:
                    $ my.health = my.health + 0.5
                    "虽然你的身体已经非常康健，但太医又给你开了一些强身健体的方子。"
                else:
                    "太医告知你你的身体非常康健，只需要保持现状即可。"
            elif my.health > 400:
                $ my.health = my.health + renpy.random.randint(1,2)
                "太医为你把脉，并给了你一些强身健体的方子。"
            else:
                $ my.health = my.health + renpy.random.randint(2,4)
                "太医为你把脉，并告知你如何让身体变得康健。"

        hide 请平安脉
        $ tags_limitcheck(my)
        if timenum == 5:
            jump 结束本旬
        else:
            $ timenum = timenum + 1
            jump 寝居界面
    else:
        show 我的宫女 at chara
        我的宫女 "[my.cheng]，您今天已经请过平安脉了。"
        hide 我的宫女
        jump 寝居界面




label 寝居休息:
    hide screen myroom

    "在寝居中休息了一段时间……"
    "体力有所恢复。"

    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum + 1
        $ AP = AP + 1
        jump 寝居界面
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
