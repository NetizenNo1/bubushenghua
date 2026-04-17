

label 有人死了(fz):
    "[fz.palace]突然响起一阵啼哭声……"
    show 我的宫女 at chara
    我的宫女 "[fz.hao][fz.weifen][fz.name]没了！"
    我的宫女 "只不过那边一片混乱，奴婢也不太清楚是什么情况。估计还得明天早上才知道。"
    menu:
        "大快人心" if fz in my.foes or fz.like < -10:
            $ my.lucky = my.lucky - 3
            $ my.yali = my.yali - 10
            我 "人在做天在看，她那般的人，早早去了也是该的。"
        "悲痛欲绝" if fz.like > 50:
            $ my.lucky = my.lucky + fz.like*0.1
            $ my.yali = my.yali + 10
            我 "怎么会这样……好端端的，怎么就抛下我去了呢……"
        "知道了":
            pass
    hide 我的宫女
    python:
        renpy.return_statement()


label 有人被打入冷宫(fz):
    if fz == my:
        scene 寝居
        "这日清晨，外头传来一阵嘈杂的响声。"
        "宫人们也竟是被支走了，寝居内各种物什被人搬离。"
        show 李公公 at chara
        李公公 "[pretext]，皇上已经下旨，将您送入冷宫。"
        我 "什么？！"
        李公公 "走吧，[my.xing]氏，如今你已经是庶人之身了。"
        hide 李公公
        show 我的宫女 at chara
        我的宫女 "主子！让奴婢陪你一起走吧！"
        hide 我的宫女
        show 李公公 at chara
        李公公 "罢了，宫里的规矩，若宫女自愿随行，冷宫中的庶人也可由一名婢子伺候。"
        李公公 "赶紧动身吧，莫耽搁了！"
        hide 李公公
        $ my.Gongnv[0].level = "婢子"
        $ my.Gongnv[0].lv = 4
        $ kufang = []
        $ money = 0

        python:
            renpy.return_statement()
    else:
        show 我的宫女 at chara
        我的宫女 "主子，奴婢听说皇上方才下了一道旨意，说是将[pretext]送入冷宫了……"
        menu:
            "大快人心" if fz in my.foes or fz.like < -10:
                $ my.lucky = my.lucky - 1.5
                $ my.yali -= 3
                我 "皇上是个明眼人，她留在宫里只会徒生祸端。"
            "怎会如此" if fz.like > 50:
                $ my.lucky = my.lucky + fz.like*0.05
                $ my.yali += 3
                我 "怎么会这样……皇上竟然让[fz.ming]去那样的地方……"
            "知道了":
                pass
        hide 我的宫女
        python:
            renpy.return_statement()

label 有人出冷宫了(fz):
    show 我的宫女 at chara
    我的宫女 "主子，奴婢听说皇上方才下了一道旨意，说是将[pretext]接出冷宫……"
    menu:
        "喜不自胜" if fz.like > 50:
            $ fz.like = fz.like + 2
            $ my.yali -= 3
            我 "太好了，我就知道总有一天皇上会原谅她的！"
        "知道了":
            pass
    hide 我的宫女
    python:
        renpy.return_statement()


label 有人侍寝时失宠(fz):
    show 我的宫女 at chara
    我的宫女 "主子，奴婢听说[fz.hao][fz.weifen][fz.name]在侍寝时触怒了龙颜，这会儿已经被送回寝宫禁足了。"
    我 "……知道了。"
    hide 我的宫女
    python:
        renpy.return_statement()


label 有人侍寝时得宠(fz):
    show 我的宫女 at chara
    我的宫女 "主子，奴婢听说昨日皇上临幸[fz.hao][fz.weifen][fz.name]时龙颜大悦，特别赏赐了[fz.cheng]留宿圣宸宫呢。"
    我 "……知道了。"
    hide 我的宫女
    python:
        renpy.return_statement()

label 有人侍寝时说我坏话(fz):
    show 我的宫女 at chara
    if huaiyun(shiqinfz) == False:
        我的宫女 "主子，奴婢听说[fz.hao][fz.weifen][fz.name]侍寝时在皇上面前抹黑了您……"
    else:
        我的宫女 "主子，奴婢听说[fz.hao][fz.weifen][fz.name]在皇上面前抹黑了您……"
    我的宫女 "皇上似乎很不高兴。"
    我 "……知道了。"
    hide 我的宫女
    python:
        renpy.return_statement()

label 有人侍寝时说我好话(fz):
    show 我的宫女 at chara
    if huaiyun(shiqinfz) == False:
        我的宫女 "主子，奴婢听说[fz.hao][fz.weifen][fz.name]侍寝时在皇上面前替您美言了几句……"
    else:
        我的宫女 "主子，奴婢听说[fz.hao][fz.weifen][fz.name]在皇上面前替您美言了几句……"
    我的宫女 "皇上听了很是高兴呢。"
    我 "知道了。"
    hide 我的宫女
    python:
        renpy.return_statement()

label 宫女代幸(fz):
    python:
        global tempgnlist
        tempgnlist = []
        for i in fz.Gongnv:
            if i!= fz.Gongnv[0] and i.level != "散役" and i.beauty > 200 and i.age >=14 and i.age <= hdage + 5 and i not in teshugn:
                tempgnlist.append(i)
            else:
                pass
        tempnum = renpy.random.randint(0, 1)
        if tempnum == 0 :
            tempgnlist = sorted(tempgnlist, key=attrgetter("beauty"),reverse = True)
        else: 
            tempgnlist = sorted(tempgnlist, key=attrgetter("yexin"),reverse = True)
        if len(tempgnlist) == 0:
            pass
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
        scene 寝居
        with fade
        show 我的宫女 at chara
        我的宫女 "主子，奴婢听说昨夜皇上留宿[fz.palace][fz.qinju]，不知怎的，竟临幸了一个宫女……"
        我 "皇上临幸了[fz.cheng]的宫女？"
        $ makeGongnv(fz,1,"宫女",daixinggn.level)
        if daixinggn in fz.Gongnv:
            $ fz.Gongnv.remove(daixinggn)
        else:
            pass
        $ temptext = str(daixinggn.level)

        if daixinggn.yexin < 600 or tempnum==0:
            $ Gongnvtofz(daixinggn,fz,True)
        else:
            $ fz.yali += 20
            $ Gongnvtofz(daixinggn,fz,False)
        我 "……知道了，退下吧。"
        hide 我的宫女
    else:
        pass
    python:
        renpy.return_statement()

label 主角侍寝:
    hide screen myroom
    hide screen Bigmap
    scene 侍寝
    with fade
    show 皇帝 at chara with dissolve
    if my.shiqin  == 0:
        if hdxingge == "冷漠":
            皇上 "（站在床头，冷冷睨你一眼。）[my.xing]氏？愣着做什么，要朕迎你不成？"
            if my.beauty > 800:
                皇上 "没想到竟是个木头美人。（眉头一松）过来。"
            elif my.qizhi >800:
                皇上 "（打量你一番，冰冷的眼神有些许的柔和）过来。"
            elif my.meili>800:
                皇上 "（眼神冰冷却又带着几分玩味）过来。"
            else:
                皇上 "（不曾正眼瞧你）过来。"
            menu:
                我 "……"
                "大方上前":
                    皇上 "（低声）同那些庸脂俗粉也没什么不同。"
                "羞涩不语":
                    皇上 "你若不想侍寝，那朕这就叫人送你回去。"
            hide 皇帝
            "转眼间，你已经被[guoxing][emperor]抱在怀里。"
            "他的胸膛竟是一片冰冷。"
            show 皇帝 at chara
            皇上 "是不是觉得很冷？"
            皇上 "放心，朕会让你习惯的。"
            皇上 "睡吧。"
            $ mustshiqin = round(my.love-10/1)
            $ my.love = my.love +2
        elif hdxingge == "腹黑":
            "[guoxing][emperor]站在殿内，并未说话，一双平静而柔和的眼眸静静望着你。"
            我 "臣妾参见皇上。"
            皇上 "爱妃免礼。"
            皇上 "过来，别怕。"
            hide 皇帝
            "[guoxing][emperor]将你拥入怀中，二人同床共枕。"
            "他如同冬日融化的雪水，清澈却又冰冷。"
            "被他拥抱的感觉，温暖，却似即若离。"
            $ mustshiqin = round(my.love*0.5/1)
            $ my.love = my.love +2
        elif hdxingge == "温柔":
            我 "臣妾参见皇上。"
            "你正欲行礼，却被一双温柔的手挽住。"
            皇上 "[my.cheng]免礼。"
            皇上 "（仔细端详你一阵，抱你到了榻上。）"
            hide 皇上
            "[guoxing][emperor]的每一个动作都细腻温柔到了极致，让人感觉被细心呵护关爱着……"
            "芙蓉帐外，寂静无声。"
            if my.meili*0.7+my.qizhi*0.3 > 900:
                $ mustshiqin = 30
                $ my.love = my.love +5
            else:
                $ my.love = my.love +2
                $ mustshiqin = 10
        elif hdxingge == "风流":
            我 "臣妾参见皇上。"
            皇上 "爱妃免礼。"
            if my.beauty > 800:
                皇上 "（仔细端详你一阵，面露欣喜，抱你到了榻上。）"
                皇上 "（含笑看着你）别怕，朕会温柔些。"
            else:
                皇上 "（含笑看着你）别怕，朕会温柔些。"
            hide 皇上
            "[guoxing][emperor]的每一个动作都游刃有余，一时间令人分不清虚实……"
            if my.beauty*0.7 +my.meili*0.3 >900:
                $ mustshiqin = 40
                $ my.love = my.love +5
            else:
                $ my.love = my.love +2
                $ mustshiqin = 0
        else:
            皇上 "（沉默无话打量着你，英俊面容虽不苟言笑，却并不让人感到冰冷。）"
            我 "臣妾参见皇上。"
            皇上 "[my.cheng]免礼。"
            hide 皇上
            "[guoxing][emperor]将你抱至榻上。"
            if my.qizhi > 800:
                "二人都是无话，然而每一个动作之间，能流露着无限的柔情。"
            else:
                pass
            "枕着他的臂弯，你沉沉睡去。"
            if my.qizhi*0.7 +my.beauty*0.3 >900:
                $ mustshiqin = 35
                $ my.love = my.love +5
            else:
                $ my.love = my.love +2
                $ mustshiqin = 25
        $ my.shiqin += 1
    else:
        $ shiqinlist = ["吟诗作对","醉酒当歌","献舞一曲","轻语闲聊","欲拒还迎","倚帐调情","褪衣入梦"]
        $ aifei = hdchenghu()
        $ shiqinlabel = "褪衣入梦"
        $ xingzhi = round(my.love*0.1)
        if my.meishu["一A"] == 0:
            pass
        else:
            $ xingzhi *= (100 + my.meishu["一A"]*10)*0.01
            $ xingzhi = round(xingzhi)
            $ my.meili += 0.15 +0.25*(my.meishu["一A"]-1)
            $ my.health -= 5

        if hdxingge == "冷漠":
            $ xingzhi += round(my.love*0.5/1)
            皇上 "（神情漠然地看着你）过来。"
        elif hdxingge == "腹黑":
            if my.love > 80:
                "[guoxing][emperor]站在殿内，仿佛等候已久一般。"
                皇上 "[aifei]，你来了。"
            else:
                皇上 "[aifei]，你来了。"
            $ xingzhi += round(my.love*0.3/1)
        elif hdxingge == "温柔":
            "你正欲行礼，却被一双温柔的手挽住。"
            皇上 "[aifei]免礼。"
            if my.meili*0.7 +my.qizhi*0.3 >900:
                $ xingzhi += 30
            else:
                $ xingzhi += 10
        elif hdxingge == "风流":
            if my.beauty*0.7 +my.meili*0.3 >900:
                $ xingzhi += 40
            else:
                $ xingzhi += 0
            我 "臣妾参见皇上。"
            皇上 "[aifei]免礼。"
        else:
            if my.beauty*0.7 +my.meili*0.3 >900:
                $ xingzhi += 30
            else:
                $ xingzhi += 15
            皇上 "（沉默无话打量着你，英俊面容虽不苟言笑，却并不让人感到冰冷。）"
            我 "臣妾参见皇上。"
            皇上 "[aifei]免礼。"
        $ mysqfail = False
        $ mysqnice = False
        if xingzhi < 0:
            $ xingzhi = 0
        elif xingzhi >= 80:
            $ xingzhi  = 80
        else:
            pass

        while len(shiqinlist) > 4 and xingzhi >= 0 and xingzhi < 100:
            call screen shiqin()
            call expression shiqinlabel from _call_expression_1

        if xingzhi < 0:
            $ mysqfail = True
        elif xingzhi >= 100:
            $ mysqnice = True
        else:
            pass
        jump 褪衣入梦

    jump 结束本旬




label 主角晋位:
    scene 寝居
    show 李公公 at chara
    李公公 "圣旨到——"
    if my.love > 80:
        李公公 "“[pretext]，柔嘉淑顺，风姿雅悦，端庄淑睿，克令克柔，诚侍君侧，示慰君心有功，{w}着即[temptext][my.hao][my.weifen]。”"
    elif my.taihoulike > 60:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，禀乘皇太后慈谕，{w}着即[temptext][my.hao][my.weifen]。”"
    elif len(my.kids) > 0:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，诞育皇嗣有功，{w}着即[temptext][my.hao][my.weifen]。”"
    elif my.year > 10:
        李公公 "“[pretext]，久侍宫闱，恪肃敬孝，德毓后庭，敬慎居心，性资敏慧，率礼不越，{w}着即[temptext][my.hao][my.weifen]。”"
    else:
        李公公 "[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，性行温良，克娴内则，淑德含章，{w}着即[temptext][my.hao][my.weifen]。”"
    menu:
        "臣妾谢恩！":
            pass
    if my.level == 0 and fenghoudadian == False:
        hide 李公公
        $ fenghoudadian = True
        $ bg("宣政殿外")
        "礼官" "大典开始！"
        "文武百官与众妃皆跪下。"
        "你缓缓行至皇上跟前，一步步走上大殿前的台阶，终行至皇上与太后跟前。"
        "你搭着皇上的手，缓缓转身面相文武百官以及众妃嫔。此时，一太监又端上一物，掀开那布，那端着的，正是凤印……"
        show 皇帝
        皇上 "如今，这凤印便交于皇后了。"
        menu:
            "接过凤印":
                pass
        我 "多谢皇上，臣妾定不辜负您的重望……"
        hide 皇帝
        "众臣" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
        "众妃" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
    else:

        李公公 "奴才恭喜娘娘了。"
        李公公 "奴才还要回去复命，就先告辞了。"
        hide 李公公

    python:
        renpy.return_statement()


label 主角晋位赐号:
    scene 寝居
    show 李公公 at chara
    李公公 "圣旨到——"
    if my.love > 80:
        李公公 "“[pretext]，柔嘉淑顺，风姿雅悦，端庄淑睿，克令克柔，诚侍君侧，示慰君心有功，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，特赐封号[my.hao]，以示嘉赏。”"
    elif my.taihoulike > 60:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，禀乘皇太后慈谕，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，特赐封号[my.hao]，以示嘉赏。”"
    elif len(my.kids) > 0:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，诞育皇嗣有功，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，特赐封号[my.hao]，以示嘉赏。”"
    elif my.year > 10:
        李公公 "“[pretext]，久侍宫闱，恪肃敬孝，德毓后庭，敬慎居心，性资敏慧，率礼不越，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，特赐封号[my.hao]，以示嘉赏。”"
    else:
        李公公 "[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，性行温良，克娴内则，淑德含章，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，特赐封号[my.hao]，以示嘉赏。”"
    menu:
        "臣妾谢恩！":
            pass
    if my.level == 0 and fenghoudadian == False:
        hide 李公公
        $ fenghoudadian = True
        $ bg("宣政殿外")
        "礼官" "大典开始！"
        "文武百官与众妃皆跪下。"
        "你缓缓行至皇上跟前，一步步走上大殿前的台阶，终行至皇上与太后跟前。"
        "你搭着皇上的手，缓缓转身面相文武百官以及众妃嫔。此时，一太监又端上一物，掀开那布，那端着的，正是凤印……"
        show 皇帝
        皇上 "如今，这凤印便交于皇后了。"
        menu:
            "接过凤印":
                pass
        我 "多谢皇上，臣妾定不辜负您的重望……"
        hide 皇帝
        "众臣" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
        "众妃" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
    else:

        李公公 "奴才恭喜娘娘了。"
        李公公 "奴才还要回去复命，就先告辞了。"
        hide 李公公
    python:
        renpy.return_statement()

label 主角晋位改号:
    scene 寝居
    show 李公公 at chara
    李公公 "圣旨到——"
    if my.love > 80:
        李公公 "“[pretext]，柔嘉淑顺，风姿雅悦，端庄淑睿，克令克柔，诚侍君侧，示慰君心有功，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，改号[my.hao]，钦此。”"
    elif my.taihoulike > 60:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，禀乘皇太后慈谕，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，改号[my.hao]，钦此。”"
    elif len(my.kids) > 0:
        李公公 "“[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，克娴内则，淑德含章，诞育皇嗣有功，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，改号[my.hao]，钦此。”"
    elif my.year > 10:
        李公公 "“[pretext]，久侍宫闱，恪肃敬孝，德毓后庭，敬慎居心，性资敏慧，率礼不越，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，改号[my.hao]，钦此。”"
    else:
        李公公 "[pretext]，淑慎性成，勤勉柔顺，雍和粹纯，性行温良，克娴内则，淑德含章，{w}着即[temptext][my.weifen]。”"
        李公公 "“另，改号[my.hao]，钦此。”"
    menu:
        "臣妾谢恩！":
            pass
    if my.level == 0 and fenghoudadian == False:
        hide 李公公
        $ fenghoudadian = True
        $ bg("宣政殿外")
        "礼官" "大典开始！"
        "文武百官与众妃皆跪下。"
        "你缓缓行至皇上跟前，一步步走上大殿前的台阶，终行至皇上与太后跟前。"
        "你搭着皇上的手，缓缓转身面相文武百官以及众妃嫔。此时，一太监又端上一物，掀开那布，那端着的，正是凤印……"
        show 皇帝
        皇上 "如今，这凤印便交于皇后了。"
        menu:
            "接过凤印":
                pass
        我 "多谢皇上，臣妾定不辜负您的重望……"
        hide 皇帝
        "众臣" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
        "众妃" "贺喜皇后！恭贺皇后！皇后千岁千岁千千岁。"
    else:

        李公公 "奴才恭喜娘娘了。"
        李公公 "奴才还要回去复命，就先告辞了。"
        hide 李公公
    python:
        renpy.return_statement()

label 主角降位:
    scene 寝居
    show 李公公 at chara
    李公公 "圣旨到——"
    李公公 "“[pretext]，妇行有亏，疏悉礼仪，懈怠不工，不思敬仪，{w}今[temptext][my.weifen]，望尔自省其身，莫负皇恩。”"
    李公公 "（叹气）您接旨吧。"
    menu:
        "臣妾接旨":
            pass
    李公公 "奴才还要回去复命，就先告辞了。"
    hide 李公公
    python:
        renpy.return_statement()

label 主角降位去号:
    scene 寝居
    show 李公公 at chara
    李公公 "圣旨到——"
    李公公 "“[pretext]，妇行有亏，疏悉礼仪，懈怠不工，不思敬仪，{w}今褫夺封号，[temptext][my.weifen]，望尔自省其身，莫负皇恩。”"
    李公公 "（叹气）您接旨吧。"
    menu:
        "臣妾接旨":
            pass
    李公公 "奴才还要回去复命，就先告辞了。"
    hide 李公公
    python:
        renpy.return_statement()

label 主角被造谣1(fz):
    scene 寝居
    show 我的宫女 at chara
    $ my.yali += 5
    我的宫女 "[my.cheng]，这宫里突然有人说您欺凌下人，已经传得沸沸扬扬了，估计不知道什么时候就叫皇上知道了，恐怕对您不利啊……"
    我 "派人去查查吧。"
    我的宫女 "是！"
    hide 我的宫女
    "未过多久……"
    show 我的宫女 at chara
    我的宫女 "主子，奴婢已经查明，此事是[fz.cheng]所为！证据确凿！"
    menu:
        "禀告皇上":
            我 "把这些证据都送到皇上那儿吧。"
            $ fz.exp = fz.exp - 10 - (beifei - my.level)
            $ fz.like = fz.like - 20
            $ fz.foes.append(my)
            $ my.foes.append(fz)
            $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+str(fz1.hao)+(fz.weifen)+str(fz.name) +"在宫里散布关于"+str(my.hao)+(my.weifen)+str(my.name) +"欺凌宫人的谣言，二人结下仇怨。\n"
            $ allstory.insert(0,tempstory2)
        "就此作罢":
            我 "这次就先罢了。都退下吧。"

    我的宫女 "是。"
    hide 我的宫女
    python:
        renpy.return_statement()


label 主角被造谣2(fz):
    scene 寝居
    show 我的宫女 at chara
    $ my.yali += 10
    我的宫女 "[my.cheng]，这宫里突然有人说您妄议朝政，已经传得沸沸扬扬了，估计不知道什么时候就叫皇上知道了，恐怕对您不利啊……"
    我 "派人去查查吧。"
    我的宫女 "是！"
    hide 我的宫女
    "未过多久……"
    show 我的宫女 at chara
    我的宫女 "主子，奴婢已经查明，此事是[fz.cheng]所为！证据确凿！"
    menu:
        "禀告皇上":
            我 "把这些证据都送到皇上那儿吧。"
            $ fz.exp =  fz.exp - 20 - (beifei - my.level)*3
            $ fz.love = fz.love - 10
            $ fz.taihoulike = fz.taihoulike -5
            $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"在宫中散布关于"+str(fz2.hao)+(fz2.weifen)+str(fz2.name) +"的谣言，皇上得知后大怒。二人结下仇怨。\n"
            $ allstory.insert(0,tempstory2)
            $ tempstory =str(year)+"年"+str(month)+"月，在宫中散布谣言，引起皇上大怒。\n"
            $ fz.story.append(tempstory)
            $ my.foes.append(fz)
            $ fz.foes.append(my)
            $ my.exp = my.exp + beifei - fz.level
            if my.love >50:
                我的宫女 "是！"
                hide 我的宫女
                "未过多久……"
                show 我的宫女 at chara
                我的宫女 "主子，皇上来了！"
                hide 我的宫女
                show 皇帝 at chara with dissolve
                我 "臣妾参见皇上！"
                皇上 "宫里那些谣言，朕都听说了。"
                皇上 "[fz.cheng]用心险恶，此番是委屈你了。"
                我 "还好未能让她得逞，臣妾不委屈。"
                皇上 "你放心，朕不会让你蒙受冤屈。"
                我 "谢陛下！"
                皇上 "朕还有政事要忙，得空了再来看你。"
                我 "是，臣妾恭送陛下。"
                hide 皇帝
            else:
                pass
        "就此作罢":

            我 "这次就先罢了。都退下吧。"

    我的宫女 "是。"
    hide 我的宫女
    python:
        renpy.return_statement()



label 主角被造谣3(fz):
    scene 寝居
    show 我的宫女 at chara
    $ my.yali += 15
    我的宫女 "[my.cheng]，这宫里突然有人说您妄议朝政，已经传得沸沸扬扬了，估计不知道什么时候就叫皇上知道了，恐怕对您不利啊……"
    我 "派人去查查吧。"
    我的宫女 "是！"
    hide 我的宫女
    "未过多久……"
    show 我的宫女 at chara
    我的宫女 "主子，奴婢已经查明，此事是[fz.cheng]所为！证据确凿！"
    menu:
        "禀告皇上":
            我 "把这些证据都送到皇上那儿吧。"
            $ fz.exp = fz.exp - 50 - (beifei - my.level)*5
            $ fz.love = fz.love - 10
            $ fz.taihoulike = fz.taihoulike -5
            $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"在宫中散布关于"+str(fz2.hao)+(fz2.weifen)+str(fz2.name) +"的谣言，皇上得知后大怒。二人结下仇怨。\n"
            $ allstory.insert(0,tempstory2)
            $ tempstory =str(year)+"年"+str(month)+"月，在宫中散布谣言，引起皇上大怒。\n"
            $ fz.story.append(tempstory)
            $ my.foes.append(fz)
            $ fz.foes.append(my)
            if my.love >50:
                我的宫女 "是！"
                hide 我的宫女
                "未过多久……"
                show 我的宫女 at chara
                我的宫女 "主子，皇上来了！"
                hide 我的宫女
                show 皇帝 at chara with dissolve
                我 "臣妾参见皇上！"
                皇上 "宫里那些谣言，朕都听说了。"
                皇上 "[fz.cheng]用心险恶，此番是委屈你了。"
                我 "还好未能让她得逞，臣妾不委屈。"
                皇上 "你放心，朕不会让你蒙受冤屈。"
                我 "谢陛下！"
                皇上 "朕还有政事要忙，得空了再来看你。"
                我 "是，臣妾恭送陛下。"
                hide 皇帝
            else:
                pass
        "就此作罢":

            我 "这次就先罢了。都退下吧。"

    我的宫女 "是。"
    hide 我的宫女
    python:
        renpy.return_statement()

label 早产事件(fz):
    if fz == my:
        "虽未足月，但不知道为何，今日腹中却莫名不适……"
        "这种感觉愈发强烈，你顿时有一种预感，很快太医赶到，却急召了稳婆入宫。"
    else:
        show 我的宫女
        我的宫女 "主子，[fz.palace][fz.qinju]那位怕是要生了……"
        我 "不是尚未足月么？"
        我的宫女 "奴婢也不知为何，只是方才请了太医过去，之后便召稳婆入宫了。"
    scene black
    with fade
    python:
        fz.health -= renpy.random.randint(int(100-fz.lucky), int(300-fz.lucky*2))
        lucky = renpy.random.randint(0, 900)
        if lucky-200 > fz.health:
            renpy.call("难产事件",fz = fz,from_current=False)
        else:
            renpy.call("生产事件",fz = fz,from_current=False)
    return

label 生产事件_前(fz):
    if fz ==my:
        "十月怀胎，你终于到了临产之际。"
        "稳婆进入了你的寝宫，疼痛令人神志不清……"
    else:
        "眼看着到了[fz.hao][fz.weifen][fz.name]临产的日子……"
        "稳婆进入了她的寝宫……"
    scene black
    with fade
    python:
        lucky = renpy.random.randint(0, 900)
        if lucky-200 > fz.health:
            renpy.call("难产事件",fz = fz,from_current=False)
        else:
            renpy.call("生产事件",fz = fz,from_current=False)
    return

label 难产事件(fz):
    if fz.lucky <= 0:
        $ lucky = 0
    else:
        $ lucky = renpy.random.randint(0, 100)
    if lucky == 0 and fz != my:
        $ tempstory = str(year)+"年"+str(month)+"月，难产，母子俱损。\n"
        $ tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+ "难产，母子俱损。\n"
        $ Killfz(fz)
        python:
            for i in fz.tags:
                if "身怀皇嗣" in i:
                    fz.tags.remove(i)
        show 我的宫女
        我的宫女 "不好了……主子，说是[fz.cheng]没了！"
        我的宫女 "当时[fz.cheng]出血不止，人便昏迷了过去，皇嗣也未能保住……"
        menu:
            "大快人心" if fz in my.foes or fz.like < -10:
                $ my.lucky = my.lucky - 3
                $ my.yali = my.yali - 10
                我 "她本便没这个福气。"
            "悲痛欲绝" if fz.like > 50:
                $ my.lucky = my.lucky + fz.like*0.1
                $ my.yali = my.yali + 10
                我 "怎么会这样……好端端的，怎么就抛下我去了呢……"
            "知道了":
                pass
        hide 我的宫女

    elif lucky < fz.lucky:
        $ lucky = renpy.random.randint(0, 1)
        if lucky == 0 and fz != my:
            show 我的宫女
            我的宫女 "不好了……主子，说是[fz.cheng]没了！"
            我的宫女 "生下皇嗣后便[fz.cheng]出血不止，太医也回天无力了。"
            hide 我的宫女
            $ lucky = renpy.random.randint(0,150 - int(fz.lucky))
            if lucky == 0:
                $ tempnum = 2
                $ kequming = True
                $ Creat_Kids(fz)
                $ newkid = NPC_Kids_list[-1]
                $ Creat_Kids(fz)
                $ newkid2 = NPC_Kids_list[-1]
                $ temptext = str(year)+"年"+str(month)+"月，为"+str(newkid.shengmu.hao)+str(newkid.shengmu.weifen)+str(newkid.shengmu.name)+"所生。\n"
                $ newkid2.story.append(temptext)
                $ newkid.story.append(temptext)
            else:
                $ tempnum = 1
                $ kequming = True
                $ Creat_Kids(fz)
                $ newkid = NPC_Kids_list[-1]
                $ temptext = str(year)+"年"+str(month)+"月，为"+str(newkid.shengmu.hao)+str(newkid.shengmu.weifen)+str(newkid.shengmu.name)+"所生。\n"
                $ newkid.story.append(temptext)
            python:
                for i in fz.tags:
                    if "身怀皇嗣" in i:
                        fz.tags.remove(i)
                tempstory = str(year)+"年"+str(month)+"月，诞下"+str(tempnum)+"位皇嗣\n"
                tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"诞下"+str(tempnum)+"位皇嗣。\n"
                fz.story.append(tempstory)
                allstory.insert(0,tempstory2)
                tempstory = str(year)+"年"+str(month)+"月，产后血崩而亡。\n"
                tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+ "产后血崩而亡。\n"
                Killfz(fz)
        else:

            $ fz.health -= renpy.random.randint(200,400)
            if fz == my:
                "然而，却被告知你诞下了一个死胎……"
            else:
                show 我的宫女
                我的宫女 "主子，[fz.cheng]那边……说是生下来就没气了……"
                hide 我的宫女

            $ tempstory = str(year)+"年"+str(month)+"月，诞下死胎。\n"
            $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"诞下死胎。\n"
            $ fz.story.append(tempstory)
            $ allstory.insert(0,tempstory2)
            $ lucky = renpy.random.randint(0, 1000)
            if lucky > fz.health:
                if tags[6] not in fz.tags:
                    $ fz.tags.append(tags[6])
            python:
                for i in fz.tags:
                    if "身怀皇嗣" in i:
                        fz.tags.remove(i)
    else:


        $ fz.love += 10
        if persistent.expspeed == 1:
            $ fz.exp = fz.exp + 50
        elif persistent.expspeed == 0:
            $ fz.exp = fz.exp + 25
        else:
            $ fz.exp = fz.exp + 100
        if fz ==my:
            "整个人如同被撕裂成块一般。"
            if my.love >= 60:
                "伴随宫人们绝望的哭喊，意识几近消散。"
            else:

                "伴随一声尖利的“皇上到——”和宫人们绝望的哭喊，意识几近消散。"
            with vpunch
            "稳婆" "[my.cheng]难产！快！快！"
            python:
                my.health -= renpy.random.randint(200, 400)
                renpy.call("生产事件",fz = fz,from_current=False)
            $ lucky = renpy.random.randint(0, 1000)
            if lucky > fz.health:
                if tags[6] not in fz.tags:
                    $ fz.tags.append(tags[6])
                "此番虽然化险为夷，但太医道，你往后再难有孕了……"
        else:
            python:
                renpy.call("生产事件",fz = fz,from_current=False)
            $ lucky = renpy.random.randint(0, 1000)
            if lucky > fz.health:
                if tags[6] not in fz.tags:
                    $ fz.tags.append(tags[6])
                "此番虽然化险为夷，但太医道，[fz.cheng]往后再难有孕了……"
    return


label 生产事件(fz):
    $ lucky = renpy.random.randint(0,150 - int(fz.lucky))
    if lucky == 0:
        $ tempnum = 2
        $ kequming = True
        $ Creat_Kids(fz)
        $ newkid = NPC_Kids_list[-1]

        $ Creat_Kids(fz)
        $ newkid2 = NPC_Kids_list[-1]
        $ temptext = str(year)+"年"+str(month)+"月，为"+str(newkid.shengmu.hao)+str(newkid.shengmu.weifen)+str(newkid.shengmu.name)+"所生。\n"
        $ newkid.story.append(temptext)
        $ newkid2.story.append(temptext)
    else:
        $ tempnum = 1
        $ kequming = True
        $ Creat_Kids(fz)
        $ newkid = NPC_Kids_list[-1]
        $ temptext = str(year)+"年"+str(month)+"月，为"+str(newkid.shengmu.hao)+str(newkid.shengmu.weifen)+str(newkid.shengmu.name)+"所生。\n"
        $ newkid.story.append(temptext)
    if persistent.expspeed == 1:
        $ fz.exp = fz.exp + 80 * tempnum
    elif persistent.expspeed == 0:
        $ fz.exp = fz.exp + 40 * tempnum
    else:
        $ fz.exp = fz.exp + 160 * tempnum
    $ fz.yali -= 20
    python:
        for i in fz.tags:
            if "身怀皇嗣" in i:
                fz.tags.remove(i)
    $ tempstory = str(year)+"年"+str(month)+"月，诞下"+str(tempnum)+"位皇嗣。\n"
    $ tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"诞下"+str(tempnum)+"位皇嗣。\n"
    if fz ==my:
        "也不知过了多久，你听到了婴儿的啼哭声。"
        "（成功诞下[tempnum]位皇嗣。）"
        $ lucky = 10 - round(my.love*0.1)
        if my.level == 0:
            $ lucky -= 5
        elif my.qinjunum == 1:
            $ lucky -= 3
        else:
            pass
        if my.familylevel <= 4:
            $ lucky -= 5
        else:
            pass
        if lucky <= 0:
            $ lucky = 0
        else:
            $ lucky = renpy.random.randint(0,lucky)
        if lucky == 0 and kequming == True:
            show 我的宫女 at chara
            我的宫女 "主子，皇上说您诞育皇嗣有功，[newkid.cheng]的名字便由您来取了。"
            我 "那就取名为……"
            if newkid.sex == "皇子":
                $ tempname1 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
                $ tempname2 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
                $ tempname3 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
            else:
                $ tempname1 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname1) >= 3:
                    $ tempname1 = tempname1[0] + tempname1[1]

                if tempname1 in teshuming:
                    $ ming_list.remove(tempname1)

                $ tempname2 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname2) >= 3:
                    $ tempname2 = tempname2[0] + tempname2[1]
                if tempname2 in teshuming:
                    $ ming_list.remove(tempname2)


                $ tempname3 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname3) >= 3:
                    $ tempname3 = tempname3[0] + tempname3[1]
                if tempname3 in teshuming:
                    $ ming_list.remove(tempname3)

            menu:
                我 "那就取名为……"
                "[tempname1]":
                    $ newkid.name = tempname1
                "[tempname2]":
                    $ newkid.name = tempname2
                "[tempname3]":
                    $ newkid.name = tempname3
                "手动输入":
                    python:
                        tempname = renpy.input("为[newkid.sex]取名（不输入则取名为[tempname1]）",length=3)
                        tempname = tempname.strip()

                        if not tempname:
                            tempname = tempname1
                        newkid.name = tempname
            我 "孩子，以后你就叫[newkid.name]了。"

        if my.level == 0:
            $ lucky -= 5
        elif my.qinjunum == 1:
            $ lucky -= 3
        else:
            pass
        if my.familylevel <= 4:
            $ lucky -= 5
        else:
            pass
        if tempnum == 1:
            $ lucky = 1
        elif lucky <= 0:
            $ lucky = 0
        else:
            $ lucky = renpy.random.randint(0,lucky)
        if lucky == 0 and kequming == True:
            show 我的宫女 at chara
            我的宫女 "主子，皇上说您诞育皇嗣有功，[newkid2.cheng]的名字便由您来取了。"
            我 "那就取名为……"
            if newkid2.sex == "皇子":
                $ tempname1 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
                $ tempname2 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
                $ tempname3 = renpy.random.choice(malename_list) + renpy.random.choice(malename2_list)
            else:
                $ tempname1 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname1) >= 3:
                    $ tempname1 = tempname1[0] + tempname1[1]
                if tempname1 in teshuming:
                    $ ming_list.remove(tempname1)


                $ tempname2 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname2) >= 3:
                    $ tempname2 = tempname2[0] + tempname2[1]
                if tempname2 in teshuming:
                    $ ming_list.remove(tempname2)

                $ tempname3 = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
                if len(tempname3) >= 3:
                    $ tempname3 = tempname3[0] + tempname3[1]
                if tempname3 in teshuming:
                    $ ming_list.remove(tempname3)

            menu:
                我 "那就取名为……"
                "[tempname1]":
                    $ newkid2.name = tempname1
                "[tempname2]":
                    $ newkid2.name = tempname2
                "[tempname3]":
                    $ newkid2.name = tempname3
                "手动输入":
                    python:
                        tempname = renpy.input("为[newkid2.sex]取名（不输入则取名为[tempname1]）",length=3)
                        tempname = tempname.strip()

                        if not tempname:
                            tempname = tempname1
                        newkid2.name = tempname
            我 "孩子，以后你就叫[newkid2.name]了。"


        python:
            fz.love =  fz.love + 10 + fz.love*0.1*tempnum + (beifei-fz.familylevel)*0.5*tempnum
            fz.taihoulike = fz.taihoulike + 10*tempnum
            fz.state = "寻常"
            fz.huaiyun = 0
            gongxi.append([fz,"生产"])
            fz.story.append(tempstory)
            allstory.insert(0,tempstory2)
    else:

        "不久以后，伴随着婴儿的啼哭，[fz.cheng]诞下[tempnum]位皇嗣的消息传遍了后宫。"
        python:
            fz.love =  fz.love + 10 + fz.love*0.1*tempnum + (beifei-fz.familylevel)*0.5*tempnum
            fz.taihoulike = fz.taihoulike + 10*tempnum
            fz.state = "寻常"
            fz.huaiyun = 0
            tempstory = str(year)+"年"+str(month)+"月，诞下"+str(tempnum)+"位皇嗣。\n"
            tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"诞下"+str(tempnum)+"位皇嗣。\n"
            gongxi.append([fz,"生产"])
            fz.story.append(tempstory)
            allstory.insert(0,tempstory2)
    return

label 不幸小产(fz):
    $ fz.health = fz.health -100
    $ fz.yali += 50
    if fz ==my:
        "睡梦之中，你突然感觉到腹部一阵绞痛……"
        我 "来人，来人……"
        "还未来得及看到宫女出现在你的面前，你就昏迷了过去……"
        scene black
        with fade
        "再次睁开眼睛，你却被告知肚子里的孩子已经没了……"
    else:
        "后宫某处突然乱成一团。"
        "很快，[fz.hao][fz.weifen][fz.name]小产的消息便传了出来……"
    "此事甚为蹊跷，掖廷已经着手开始调查。"
    $ lucky = renpy.random.randint(0, 900)
    if lucky-200 > fz.health:
        if tags[6] not in fz.tags:
            $ fz.tags.append(tags[6])
        "并且太医还道，往后再难有孕了……"
        python:
            tempstory = str(year)+"年"+str(month)+"月，蹊跷小产，痛失骨肉，且再难有孕。\n"
            tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"蹊跷小产，且再难有孕。\n"
            fz.story.append(tempstory)
            xiluo.append([fz,"小产"])
            allstory.insert(0,tempstory2)
    else:
        python:
            tempstory = str(year)+"年"+str(month)+"月，蹊跷小产，痛失骨肉。\n"
            tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"蹊跷小产。\n"
            fz.story.append(tempstory)
            xiluo.append([fz,"小产"])
            allstory.insert(0,tempstory2)
    python:
        renpy.return_statement()


label 强制小产_假孕(fz):
    "产期将至……然而你本未怀孕，因此现今必须宣称小产了……"
    "因为未及时作出准备，只能对外称是自身不慎所致。"
    "皇上听闻甚是不悦……"
    $ my.love -= 20

    $ my.meishu["三级"] = 0

    python:
        renpy.return_statement()



label 不幸小产_假孕(fz):

    if fz == my:
        $ timenum = 5
        我 "（要借此嫁祸于谁呢？）"
        $ newxdsj = xiadu(zhu=my,bei=my,way=1,time1=0,time2=7,gn=[],jieguo=1,jilv=100,state=0,xiaochan = True,xianyi=[],zuiren=None)
        python:
            if fz.meishu["三级"] == 1:
                tempnum = 15
            elif fz.meishu["三级"] == 2:
                tempnum = 30
            else:
                tempnum = 50
            templist = []
            tempfzlist= []
            for i in NPC_fz_list:
                if  havetag("失心成疯",i) == False and jinzu(i) == False and i.state != "病重"  and i != my :
                    templist.append(i)
        call screen choicefz_dx(templist,tempfzlist,3)
        python:
            for i in tempfzlist:
                newxdsj.xianyi.append([i,tempnum])
        $ gdsj.append(newxdsj)
        $ xdsj.append(newxdsj)

        "你筹备好了一切……"
        我 "来人，来人……"
        "趁着宫女出现在你的面前，你就假装昏迷了过去……"
        scene black
        with fade
        "一切滴水不漏，你“小产”的消息传了出去，因背后多有蹊跷，掖廷已经着手开始调查。"
        $ timenum += 1
        $ my.meishu["三级"] = 0
        $ my.jiayun = False
        python:
            for j in my.tags:
                if "身怀皇嗣" in j:
                    my.tags.remove(j)
    else:

        $ newxdsj = xiadu(zhu=fz,bei=fz,way=1,time1=0,time2=7,gn=[],jieguo=1,jilv=100,state=0,xiaochan = True,xianyi=[],zuiren=None)
        python:
            if fz.meishu["三级"] == 1:
                tempnum = 15
            elif fz.meishu["三级"] == 2:
                tempnum = 30
            else:
                tempnum = 50
            templist = sorted(fz.foes, key=attrgetter("love"),reverse = True)
            for i in templist:
                if len(newxdsj.xianyi) < 3 and havetag("失心成疯",i) == False and jinzu(i) == False and i.state != "病重" and i in NPC_fz_list:
                    newxdsj.xianyi.append([i,tempnum])
            if len(newxdsj.xianyi) < 3:
                templist = sorted(NPC_fz_list, key=attrgetter("love"),reverse = True)
                for i in templist:
                    if len(newxdsj.xianyi) < 3 and havetag("失心成疯",i) == False and jinzu(i) == False and i.state != "病重"  and i != fz and i not in fz.friends :
                        newxdsj.xianyi.append([i,tempnum])

        $ gdsj.append(newxdsj)
        $ xdsj.append(newxdsj)
        $ fz.meishu["三级"] = 0
        "后宫某处突然乱成一团。"
        "很快，[fz.hao][fz.weifen][fz.name]小产的消息便传了出来……"
        "此事甚为蹊跷，掖廷已经着手开始调查。"

    python:
        tempstory = str(year)+"年"+str(month)+"月，蹊跷小产，痛失骨肉。\n"
        tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"蹊跷小产。\n"
        fz.story.append(tempstory)
        xiluo.append([fz,"小产"])
        allstory.insert(0,tempstory2)

    python:
        renpy.return_statement()

label 不幸小产_随机(fz):
    $ fz.health = fz.health -100
    $ fz.yali += 50
    if fz ==my:
        "睡梦之中，你突然感觉到腹部一阵绞痛……"
        我 "来人，来人……"
        "还未来得及看到宫女出现在你的面前，你就昏迷了过去……"
        scene black
        with fade
        "再次睁开眼睛，你却被告知肚子里的孩子已经没了……"
    else:
        "后宫某处突然乱成一团。"
        "很快，[fz.hao][fz.weifen][fz.name]小产的消息便传了出来……"
    $ lucky = renpy.random.randint(0, 900)
    if lucky-200 > fz.health:
        if tags[6] not in fz.tags:
            $ fz.tags.append(tags[6])
        "并且太医还道，往后再难有孕了……"
        python:
            tempstory = str(year)+"年"+str(month)+"月，意外小产，痛失骨肉，且再难有孕。\n"
            tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"小产，且再难有孕。\n"
            fz.story.append(tempstory)
            xiluo.append([fz,"小产"])
            allstory.insert(0,tempstory2)
    else:
        python:
            tempstory = str(year)+"年"+str(month)+"月，意外小产，痛失骨肉。\n"
            tempstory2 = "【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+str(fz.weifen)+str(fz.name)+"小产。\n"
            fz.story.append(tempstory)
            xiluo.append([fz,"小产"])
            allstory.insert(0,tempstory2)
    python:
        renpy.return_statement()

label 废后事件(self):
    "这日，后宫中议论纷纷……"
    "听闻皇上在早朝时提及皇后德行有缺，有意废后，朝中一片哗然。"
    "下朝后，皇上直奔太后的建章宫而去……"
    "不久，废后的诏书便传了出来。"
    python:
        if self.hao == "":
            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"。\n"
            tempstory2 ="【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext + temptext +str(self.weifen)+"。\n"
            self.story.append(tempstory)
            allstory.insert(0,tempstory2)
            xiluo.append([self,"降位"])
            ChangeGongnv(self)
            if self.hao =="":
                self.cheng = self.xing +self.weifen
            else:
                self.cheng = self.hao +self.weifen
            
            if self == my:
                renpy.jump("主角降位")
            else :
                pass
        else :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                hao_list.append(self.hao)
                self.hao = ""
                tempstory = str(year)+"年"+str(month)+"月，褫夺封号，"+temptext+str(self.weifen)+"。\n"
                tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext + "被褫夺封号，"+temptext+str(self.weifen)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                xiluo.append([self,"降位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                
                if self == my:
                    renpy.jump("主角降位去号")
                else :
                    pass
            
            else :
                tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.hao) + str(self.weifen)+"。\n"
                tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.hao) + str(self.weifen)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                xiluo.append([self,"降位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                
                if self == my:
                    renpy.jump("主角降位")
                else :
                    pass
        renpy.return_statement()

label 立后事件(self):
    "这日，后宫中议论纷纷……"
    "听闻皇上在早朝时提及后宫一日不可无后，朝中大臣纷纷赞同。"
    "下朝后，皇上直奔太后的建章宫而去……"
    "不久，立后的诏书便传了出来。"
    python:
        if self.hao == "":
            lucky = renpy.random.randint(0, 1)
            if lucky == 0 or yetinghao != "":
                if yetinghao != ""  and self == my:
                    self.hao = yetinghao
                    yetinghao = ""
                else:
                    self.hao = renpy.random.choice(hao_list)
                    hao_list.remove(self.hao)
                    lucky = renpy.random.randint(0, 4)
                    if lucky == 0 and self.love >= 20:
                        temphao = renpy.random.choice(hao_list)
                        hao_list.remove(temphao)
                        self.hao += temphao
                    else:
                        pass
                tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"，赐号"+str(self.hao)+"。\n"
                tempstory2 ="【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext  +temptext+str(self.weifen)+"，赐号"+str(self.hao)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                gongxi.append([self,"晋位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                
                if self == my:
                    renpy.jump("主角晋位赐号")
                else :
                    renpy.return_statement()
            else :
                tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"。\n"
                tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext  +temptext+str(self.weifen)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                gongxi.append([self,"晋位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                if self == my:
                    renpy.jump("主角晋位")
                else :
                    renpy.return_statement()
        else :
            lucky = renpy.random.randint(0, 4)
            
            
            
            
            if self == my and yetinghao != "":
                lucky = 0
            else:
                pass
            if lucky == 0:
                temphao = self.hao
                if yetinghao != "" and self == my:
                    hao_list.append(temphao)
                    self.hao = yetinghao
                    yetinghao = ""
                else:
                    self.hao = renpy.random.choice(hao_list)
                    hao_list.remove(self.hao)
                    if len(temphao) >= 2:
                        for i in temphao:
                            hao_list.append(i)
                    else:
                        hao_list.append(temphao)
                    lucky = renpy.random.randint(0, 2)
                    if lucky == 0 and self.love >= 20:
                        temphao = renpy.random.choice(hao_list)
                        hao_list.remove(temphao)
                        self.hao += temphao
                    else:
                        pass
                tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"，改号"+str(self.hao)+"。\n"
                tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.weifen)+"，改号"+str(self.hao)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                gongxi.append([self,"晋位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                
                if self == my:
                    renpy.jump("主角晋位改号")
                else :
                    renpy.return_statement()
            
            else :
                tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.hao)+str(self.weifen)+"。\n"
                tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.hao)+str(self.weifen)+"。\n"
                self.story.append(tempstory)
                allstory.insert(0,tempstory2)
                gongxi.append([self,"晋位"])
                ChangeGongnv(self)
                if self.hao =="":
                    self.cheng = self.xing +self.weifen
                else:
                    self.cheng = self.hao +self.weifen
                
                if self == my:
                    renpy.jump("主角晋位")
                else :
                    renpy.return_statement()


        renpy.return_statement()


label 有人疯了(fz):
    "[fz.palace]突然响起一阵喧闹声……"
    show 我的宫女 at chara
    我 "发生什么了？"
    我的宫女 "主子，奴婢听说……听说[fz.hao][fz.weifen][fz.name]积郁成疾，方才突然发作了一场，太医过去瞧了，说是疯了！"
    menu:
        "大快人心" if fz in my.foes or fz.like < -10:
            $ my.lucky = my.lucky - 3
            $ my.yali = my.yali - 10
            我 "自作孽不可活。"
        "悲痛欲绝" if fz.like > 50:
            $ my.lucky = my.lucky + fz.like*0.1
            $ my.yali = my.yali + 10
            我 "怎么会这样……好端端的，怎么会失心疯了呢……"
        "知道了":
            pass
    hide 我的宫女
    $ fz.yali = 0
    $ fz.xinji = 0
    $ fz.qizhi = 100
    $ fz.meili = 100
    $ fz.book = 0
    $ fz.cixiu = 0
    $ fz.dance = 0
    $ fz.muzic = 0
    $ fz.qingxiang = 0
    $ fz.tags.append(tags_yali[2])
    $ fz.friends = []
    $ fz.foes = []
    $ fz.meishu = {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
    $ fz.huashu =  {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
    $ fz.anhai =  {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
    $ fz.fangyu = {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
    python:
        renpy.return_statement()

label 压力满了(fz):
    $ lucky = renpy.random.randint(0,10)
    if lucky == 0 and fz != my:
        $ templist = ["活泼","温婉","圆滑","安静","清冷","娇纵","势利"]
        $ templist.remove(fz.xingge)
        $ fz.xingge = renpy.random.choice(templist)
        show 我的宫女 at chara
        我的宫女 "主子，奴婢听说……听说[fz.hao][fz.weifen][fz.name]不知怎的在寝居中突然大发脾气，随后便性情大变了……"
        menu:
            "知道了":
                pass
        hide 我的宫女
        python:
            renpy.return_statement()
    elif lucky <= 5:
        $ lucky = renpy.random.randint(0,1)
        if lucky == 1:
            $ fz.qingxiang -= 30
        else:
            $ fz.qingxiang += 30
    else:
        $ lucky = renpy.random.randint(0,1)
        if lucky == 1:
            $ fz.xinji -= 300
        else:
            $ fz.xinji += 300
    if fz != my:
        show 我的宫女 at chara
        我的宫女 "主子，奴婢听说……听说[fz.hao][fz.weifen][fz.name]不知怎的在寝居中突然大发脾气，随后便和往日有些不太一样了……"
        menu:
            "知道了":
                pass
        hide 我的宫女
        python:
            renpy.return_statement()
    else:
        "这日不知为何，你感觉心中异常烦躁。平日里积蓄的压力在一瞬间爆发了出来……"
        "平静下来以后你隐隐听到宫人们在低声议论，你与平日有些不大一样了。"
        python:
            renpy.return_statement()


label 被高位晋位(self):
    show 我的宫女 at chara
    if self.level == 0:
        $ temptext = "中宫之权"
    else:
        $ temptext = "主位之权"
    我的宫女 "主子，奴婢听说[self.cheng]已经命人通报了掖廷，以[temptext]晋了您的位份，如今您已经是[my.weifen]了！"
    "未几，掖廷的人果然传来了旨意。"
    python:
        renpy.return_statement()

label 被高位降位(self):
    show 我的宫女 at chara
    if self.level == 0:
        $ temptext = "中宫之权"
    else:
        $ temptext = "主位之权"
    我的宫女 "主子，奴婢听说[self.cheng]已经命人通报了掖廷，以[temptext]降了您的位份，如今您是[my.weifen]了……"
    "未几，掖廷的人果然传来了旨意。"
    python:
        renpy.return_statement()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
