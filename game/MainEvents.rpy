label 初次请安_准备:
    show screen calendar
    $ month = month +1
    $ datenum = 1
    $ timenum = 1
    scene 寝居
    with fade
    show 我的宫女 at chara
    $ mapname = "寝居"
    我的宫女 "[my.cheng]您醒了，让奴婢为你梳妆打扮吧。"
    我的宫女 "这是您第一次去凤仪宫请安，到时候也会见到宫里的高位娘娘。"
    我的宫女 "不知您喜欢什么样的装扮风格呢？"
    menu:
        "明丽":
            if my.beauty > 400:
                $ tempdapei = 0
            else:
                $ tempdapei = 1
        "妩媚":
            if my.meili > 400:
                $ tempdapei = 0
            else:
                $ tempdapei = 2
        "端庄":
            if my.qizhi > 400:
                $ tempdapei = 0
            else:
                $ tempdapei = 3
        "华丽":
            if my.familylevel < 4:
                $ tempdapei = 0
            else:
                $ tempdapei = 4
        "素净":
            if my.familylevel > 6:
                $ tempdapei = 0
            else:
                $ tempdapei = 5
    我的宫女 "奴婢明白。"
    我的宫女 "（梳妆中……）"
    hide 我的宫女
    "收拾了一番后，你看着镜中的自己，满意地朝着凤仪宫走去……"

    python:
        templist = []
        for i in NPC_newfz_list:
            if i.xingge == "娇纵" or i.xingge =="势利" and i.xinji < 600:
                templist.append(i)
            else:
                pass
        templist = sorted(templist, key=attrgetter("qingxiang"),reverse = True)
        if templist != []:
            tempfz = templist[0]
            templist2 = []
            for i in NPC_newfz_list:
                if i.xingge == "安静"  and i.level > tempfz.level:
                    templist2.append(i)
                elif i.xingge =="温婉" and i.level > tempfz.level:
                    templist2.append(i)
                elif i.xingge =="清冷" and i.level > tempfz.level:
                    templist2.append(i)
                elif i.xingge =="活泼" and i.level > tempfz.level:
                    templist2.append(i)
                else:
                    pass
        else:
            pass


    if templist == [] or templist2 == []:
        $ tempbool = False
        $ tempbool2 = False
        $ tempbool3 = False
        $ tempbool4 = False
    else:

        $ tempfz2 = renpy.random.choice(templist2)
        $ templist = NPC_newfz_list
        $ templist.remove(tempfz)
        $ templist.remove(tempfz2)
        $ tempfz3 =  renpy.random.choice(templist)
        $ tempfz4 = NPC_fz_list[1]
        call 初次请安_吃瓜 from _call_初次请安_吃瓜

label 初次请安_殿内:

    scene 凤仪宫内
    with fade
    show screen notify("凤仪宫内")
    "殿内，皇后高坐主位，下首还有几位身份尊贵的嫔妃。"
    show 皇后 at chara
    if tempbool == True and tempbool3 == True:
        menu:
            "（行礼）臣妾给皇后娘娘请安，见过各位娘娘":
                pass
        $ NPC_fz_list[0].like = NPC_fz_list[0].like +renpy.random.randint(2,4)
        皇后 "赐座吧。"
        皇后 "规矩挺好，模样也不错。若能让皇上舒心就更好了。"
        "你入座以后，四下打量一番，却发现自己竟是一众新秀中最先进殿的。{p}皇后和其他高位嫔妃已经到了，其他新人都还在外面。"
        "过了一会儿，新人们才陆陆续续地进来了，无不是恭敬地向皇后请安。"
    elif tempbool3 == True:
        "众新人请安中……"
        "不知为何，皇后的脸色有些不太好看。"
    else:
        pass
        show 皇后 at chara
        menu:
            "（行礼）臣妾给皇后娘娘请安，见过各位娘娘":
                pass
        皇后 "（四下环视一圈）嗯，规矩都挺好。"

    if NPC_fz_list[0].qingxiang < 300:
        皇后 "在座的各位刚刚入宫，若有什么不习惯的，大可来找本宫。"
        皇后 "从今往后，大家都是姐妹，理应互相照拂，而不是勾心斗角，引发争端，明白了吗？"
    elif NPC_fz_list[0].qingxiang < 700:
        皇后 "各位都是万里挑一的名姝佳媛，如今入了宫，本宫只希冀你们能让太后娘娘舒心，为皇上开枝散叶。"
    else:
        皇后 "之前在储秀宫里，嬷嬷已经把你们该知道的都告诉你们了。{p}什么该做，什么不该做，你们应该都清楚了。"
        皇后 "本宫奉劝各位，安分守己，少生事端。{p}如果不做自己该做的，或者做了不该做的，后果可别怪本宫没提醒。"

    $ NPC_fz_list[0].xingge1 = True
    menu:
        "臣妾遵命！":
            pass

    皇后 "（满意地点了点头。）"
    "皇后又说了几句身为六宫之主的客套话。"
    hide 皇后

    python:
        templist = []
        for i in NPC_fz_list:
            if i.xingge == "娇纵" and i.year == 3 and i.level >0:
                templist.append(i)
            elif i.xingge =="势利" and i.year == 3 and i.level >0:
                templist.append(i)
            else:
                pass

        templist2 = []
        for i in NPC_fz_list:
            if i.xingge == "温婉" and i.year == 3 and i.level >0:
                templist2.append(i)
            elif i.xingge =="圆滑" and i.year == 3 and i.level >0:
                templist2.append(i)
            else:
                pass

    if tempdapei != 0 and templist != [] and templist2 != []:
        $ tempbool5 = False
        call 初次请安_被奚落 from _call_初次请安_被奚落
    else:
        $ tempbool5 = False

    show 皇后 at chara
    皇后 "好了，本宫乏了。既然各位已经请过安了，就都退下吧。"
    menu:
        "臣妾告退":
            pass
    hide 皇后
    "妃嫔们一齐起身告辞，随后退出了凤仪宫。"

    scene 凤仪宫外
    with fade
    show screen notify("凤仪宫外")

    if tempbool5 == True and firstfriend != None:
        image 第一个朋友 = "Feizi/F[firstfriend.face].webp"
        "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "[myname2]！"
        show 第一个朋友 at chara
        "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "方才那[tempfz.cheng]当真过分。"
        "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "可吓到你了？"
        "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "我原本想替你说话，可又怕火上浇油，幸好有[tempfz2.cheng]出面，否则看架势，[tempfz.cheng]是不打算轻易放过你了！"
        "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "你啊！以后还是小心些吧！"
        menu:
            "今日的仇怨，今后迟早会报！":
                $ my.xinji = my.xinji -20
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "唉……虽说一早便知道你就是这性子……"
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "你中选入宫我本是高兴的，可是却又担心得很。"
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "罢了，我先回去了。"
            "我会谨慎些的":

                $ my.xinji = my.xinji +20
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "那我便放心了。"
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "往后咱们在宫里也要多多照应。"
                "[firstfriend.hao][firstfriend.weifen]—[firstfriend.name]" "那，我就先回去了，改日再去找你。"
        hide 第一个朋友
        with fade
    else:
        pass

    menu:
        "回到寝居":
            scene 寝居
            with fade
            show screen notify(my.palace+my.qinju)
            "你的后宫之旅，正式开始。接下来，你的未来，就交给你自己了—"
            $ mustshiqin = 20 + (12-my.familylevel)*5
            jump 养成开始








label 初次请安_吃瓜:
    $ tempbool3 = True
    scene 凤仪宫外
    with fade
    show screen notify("凤仪宫外")
    image tempfz = "Feizi/F[tempfz.face].webp"
    image tempfz2 = "Feizi/F[tempfz2.face].webp"
    image tempfz3 = "Feizi/F[tempfz3.face].webp"
    image tempfz4 = "Feizi/F[tempfz4.face].webp"
    "（行至凤仪宫外，却听见不远处有嘈杂的声音。）"
    menu:
        "事不关己，先进殿内":
            "你快步绕行离开了。"
            $ tempbool = True
            jump 初次请安_殿内
        "过去瞧瞧":
            $ tempbool = False
            show 我的宫女 at chara
            我的宫女 "[my.cheng]，好像是[tempfz.cheng]和[tempfz2.cheng]起了争执。"
            hide 我的宫女
            "你走上前去，看到两个穿着宫装的女子正在对峙着。"
            show tempfz at chara
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "[tempfz2.cheng]，你少装成这副样子，明明就是故意对我无礼。方才那般跋扈，这会儿又扮得楚楚可怜，真是可笑。"
            show tempfz2 at chara
            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "[tempfz.cheng]，你何出此言？嫔妾方才礼数已经做足，您说嫔妾失了礼数，实在是欲加之罪。"
            show tempfz3 at chara
            "[tempfz3.hao][tempfz3.weifen]—[tempfz3.name]" "[tempfz.cheng]，今日是咱们这些新秀第一次给皇后娘娘请安，在凤仪宫外面吵吵闹闹，若是惊动了皇后或是其他娘娘，这罪责，谁也担待不起。"
            hide tempfz3
            hide tempfz
            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "（感激地看了[tempfz3.cheng]一眼）[tempfz.cheng]若真觉得嫔妾失礼，等请过安以后再来质问嫔妾也不迟。"
            hide tempfz2
            show tempfz at chara
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "呵，就知道抬出皇后娘娘来？若皇后娘娘在此，目睹了刚才你对我的无礼和敷衍，怕是更要治罪于你！{p}等请完安再处置你，可不是由着你到时候信口雌黄么！"
            hide tempfz
            "眼看着二人之间气氛愈发严峻，若事情闹大，恐怕所有新秀都脱不了干系。"
            "可若上前调停，耽搁了请安，更是……"
            menu:
                "转身离开":
                    "你并不关心事态的发展，而是选择进入殿内。"
                    $ tempbool = True
                    jump 初次请安_殿内
                "坐视不管":
                    "你并不关心事态的发展，而是选择了旁观。"
                    "???" "前方何人喧哗？"
                    "宫人的声音" "[tempfz4.cheng]驾到—"
                    show tempfz4 at chara
                    "众人" "参见[tempfz4.cheng]！"
                    "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "你们为何不进殿，这外头发生了何事？"
                    show tempfz3 at chara
                    "[tempfz3.hao][tempfz3.weifen]—[tempfz3.name]" "回[tempfz4.cheng]，是[tempfz.cheng]同[tempfz2.cheng]发生了争执。"
                    hide tempfz3
                    show tempfz at chara
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "[tempfz4.cheng]，[tempfz2.cheng]对嫔妾无礼怠慢，嫔妾想着今日是咱们第一次来凤仪宫请安，若等会儿她在凤仪宫中失礼，触怒了皇后娘娘可就是犯了大错，故而提醒了几句。可她竟然拒不承认，臣妾这才与她争执了起来……"
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "嫔妾绝非故意闹事，请[tempfz4.cheng]明鉴！"
                    show tempfz2 at chara
                    "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "（抿着嘴唇沉默了半晌）嫔妾没有……"
                    hide tempfz
                    hide tempfz2
                    show tempfz4 at chara
                    "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "在这宫里，你们说有，亦或是没有……{p}都不算。"
                    "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "这里是凤仪宫，谁对谁错，皇后娘娘说了算。要闹，进去闹。"
                    hide tempfz4
                    show tempfz at chara
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "……"
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "这点小事何必惊动皇后娘娘呢？"
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "只要[tempfz2.cheng]在皇后娘娘面前不要失礼，那嫔妾就当作什么事情也没发生过吧。"
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（暗自咬了咬牙。）"
                    hide tempfz
                    $ tempbool2 = True
                    "事情落下帷幕，众人纷纷进入了凤仪宫。"
                    jump 初次请安_殿内
                "走上前去":
                    "看到你前来，位份比你低的新秀都向你行了礼。你也回敬了礼数。"
                    $ my.exp = my.exp + 4
                    show tempfz at chara
                    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（看了你一眼）[my.cheng]有事么？也要为[tempfz2.cheng]求情？"
                    hide tempfz
                    menu:
                        "帮助[tempfz2.cheng]":
                            show tempfz at chara
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "哼……一个个的，都装什么正人君子？{p}[tempfz2.cheng]算你走运！"
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "往后，你可要小心点了！"
                            "（[tempfz.name]愤怒地转身离开了。在经过你身边的时候，狠狠地瞪了你一眼。）"
                            $ tempfz.like = tempfz.like - renpy.random.randint(15,20)
                            $ tempfz2.like = tempfz2.like +renpy.random.randint(8,12)
                            hide tempfz
                            show tempfz2 at chara
                            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "多谢[my.cheng]今日相助。"
                            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "可是这[tempfz.cheng]……往后，恐怕会对你不利。"
                            hide tempfz2
                            $ tempbool1 = True
                            $ tempbool2 = False
                        "赞同[tempfz.cheng]":
                            $ tempfz.like = tempfz.like + renpy.random.randint(15,20)
                            $ tempfz2.like = tempfz2.like - renpy.random.randint(8,12)
                            show tempfz at chara
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（得意）看来还是有明眼人的。"
                            show tempfz2 at chara
                            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "[my.cheng]你并未得知前因后果，又何出此言！"
                            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "你、你们……欺人太甚……"
                            hide tempfz
                            hide tempfz2
                            "???" "前方何人喧哗？"
                            "宫人的声音" "[tempfz4.cheng]驾到—"
                            show tempfz4 at chara
                            "众人" "参见[tempfz4.cheng]！"
                            "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "你们为何不进殿，这外头发生了何事？"
                            show tempfz3 at chara
                            "[tempfz3.hao][tempfz3.weifen]—[tempfz3.name]" "回[tempfz4.cheng]，是[tempfz.cheng]同[tempfz2.cheng]发生了争执。"
                            hide tempfz3
                            show tempfz at chara
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "[tempfz4.cheng]，[tempfz2.cheng]对嫔妾无礼怠慢，嫔妾想着今日是咱们第一次来凤仪宫请安，若等会儿她在凤仪宫中失礼，触怒了皇后娘娘可就是犯了大错，故而提醒了几句。可她竟然拒不承认，臣妾这才与她争执了起来……"
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "嫔妾绝非故意闹事，请[tempfz4.cheng]明鉴！"
                            show tempfz2 at chara
                            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "（抿着嘴唇沉默了半晌）嫔妾没有……"
                            hide tempfz
                            hide tempfz2
                            show tempfz4 at chara
                            "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "在这宫里，你们说有，亦或是没有……{p}都不算。"
                            "[tempfz4.hao][tempfz4.weifen]—[tempfz4.name]" "这里是凤仪宫，谁对谁错，皇后娘娘说了算。要闹，进去闹。"
                            hide tempfz4
                            show tempfz at chara
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "……"
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "这点小事何必惊动皇后娘娘呢？"
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "只要[tempfz2.cheng]在皇后娘娘面前不要失礼，那嫔妾就当作什么事情也没发生过吧。"
                            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（暗自咬了咬牙。）"
                            hide tempfz
                            $ tempbool2 = True
                            $ tempbool1 = False
                    "事情落下帷幕，众人纷纷进入了凤仪宫。"
                    show 我的宫女 at chara
                    if my.Gongnv[0].xingge =="单纯":
                        $ my.xinji = my.xinji - 20
                        我的宫女 "啊，刚才那[tempfz.cheng]好大的架势！"
                        我的宫女 "不过[my.weifen]您也不输给她呢！"
                        我的宫女 "只是……咱们以后是不是也不能太张扬呢？像[tempfz.cheng]那样，会不会树立很多敌人啊？"
                    elif my.Gongnv[0].xingge =="机灵":
                        $ my.xinji = my.xinji - 20
                        我的宫女 "啊，刚才那[tempfz.cheng]好大的架势！"
                        我的宫女 "不过[my.weifen]您也不输给她呢！"
                        我的宫女 "就应该让那些人知道，咱们[my.cheng]不是好招惹的！"
                    else:
                        我的宫女 "[my.cheng]，奴婢斗胆……方才情势未明您便上前，是不是有些草率了？"
                        menu:
                            "寻点乐子罢了":
                                $ my.xinji = my.xinji -10
                                我的宫女 "大约是奴婢过于胆小了。但在这宫里，还是小心谨慎些为好……"
                            "见不惯[tempfz2.cheng]那副惺惺作态的模样" if tempbool2:
                                $ my.xinji = my.xinji -10
                                我的宫女 "这宫里总有些人让您不顺眼，可是凡事还是小心谨慎些为好……"
                            "见不惯[tempfz.cheng]那副娇纵跋扈的模样" if tempbool1:
                                $ my.xinji = my.xinji -10
                                我的宫女 "这宫里总有些人让您不顺眼，可是凡事还是小心谨慎些为好……"
                            "以后会谨慎一些":
                                我的宫女 "这宫里总有些人让您不顺眼，可是凡事还是小心谨慎些为好……"
                                $ my.Gongnv[0].yexin = my.Gongnv[0].yexin - 5

                    我的宫女 "[my.weifen]，我们也进去吧。"
                    menu:
                        "进入凤仪宫":
                            pass
                    jump 初次请安_殿内

label 初次请安_被奚落:
    python:
        templist = sorted(templist, key=attrgetter("qingxiang"),reverse = True)
        tempfz = templist[0]
        tempfz2 = renpy.random.choice(templist2)
    image tempfz = "Feizi/F[tempfz.face].webp"
    image tempfz2 = "Feizi/F[tempfz2.face].webp"
    show tempfz at chara
    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（望向你）诶，这位妹妹……"
    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "(轻笑一声)你这身打扮……啊，本宫不是有意要笑笑话你的。"
    "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "只是……真的很好笑啊。{p}哈哈哈。{p}咳咳，臣妾失态了，皇后娘娘请见谅。"
    $ tempfz.xingge1 = True
    menu:
        "（尴尬得一言不发）":
            $ my.xinji = my.xinji -10
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "唉……"
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "（不再多说什么，只觉得有些无趣。）"
        "娘娘说的是，嫔妾以后一定注意":
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "倒是挺乖顺的。"
            $ my.exp = my.exp - 20/my.level
            $ tempfz.like =tempfz.like + 2
            if tempdapei == 1:
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你说你长得又不算出挑，穿这么明艳，反而衬得这张脸黯然失色了。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "倒也没什么大碍。{p}主要是……皇上肯定不会喜欢。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你若有心，往后改改便是了。"
            elif tempdapei == 2:
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你这身衣服这么妩媚，和你这个人完全不搭啊。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "倒也没什么大碍。{p}主要是……皇上肯定不会喜欢。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你若有心，往后改改便是了。"
            elif tempdapei == 3:
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你说你气质平平，还穿的这么死板，看起来也太奇怪了。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "倒也没什么大碍。{p}主要是……皇上肯定不会喜欢。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你若有心，往后改改便是了。"
            elif tempdapei == 4:
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你穿的这么华丽，若是身居高位也就罢了，可你刚刚入宫，出身又寒微……"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "本宫也是好心提醒你一句，省的有人看你不顺眼了。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你若有心，往后改改便是了。"
            else:
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你这身衣服也太过寒碜了。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "好歹也是[my.family]，也不怕给家族丢了脸面。"
                "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "你若有心，往后改改便是了。"
            "你不知[tempfz.cheng]究竟有没有恶意，却也只能俯首称是。"
            "等她说完，你听到周围有低低的笑声……"
        "娘娘何出此言？":
            $ tempbool5 = True
            $ my.exp = my.exp - 50/my.level
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "呵，倒是挺傲的么……只是本宫也不知道你有没有这个资本傲了。"
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "小小一个[my.weifen]，竟也敢质疑本宫？"
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "皇后娘娘，这个[my.cheng]真是好没规矩。若就此放任不管，往后什么人都敢冒犯臣妾不说，这[my.cheng]怕是要翻了天了！"
            hide tempfz
            show tempfz2 at chara
            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "[tempfz.cheng]，她才刚刚入宫，许多规矩即便是知道了，也难免会触犯。{p}况且，这不过是件小事，何必大动干戈呢？"
            show tempfz at chara
            "[tempfz.hao][tempfz.weifen]—[tempfz.name]" "呵……[tempfz2.cheng]倒是大度呢。显得我似乎很是小肚鸡肠。不过，宫里的规矩就这么任人践踏么？"
            hide tempfz
            "[tempfz2.hao][tempfz2.weifen]—[tempfz2.name]" "既然她没规矩，便让她懂规矩便是了。念在她是初犯，就罚抄宫规十遍，既能让[my.cheng]长点教训，又能显得你宽宏大量，不是两全其美么？"
            $ tempfz2.xingge1 = True
            hide tempfz2
            show 皇后 at chara
            皇后 "行了。"
            皇后 "[my.cheng]刚刚进宫，也不必太过苛责。就按[tempfz2.cheng]说的办。[my.cheng]，不要再有下次了。"
            menu:
                "是":
                    pass
                "……":
                    $ my.xinji = my.xinji -10
    python:
        renpy.return_statement()



label 参加宴会:
    hide screen Bigmap
    scene 宴会
    with fade
    $ canjiayanhui = True
    $ timenum =5
    if month == 6:
        "因是帝王寿辰，有朝中心腹近臣也受邀参加。"
    else:
        "岁末迎新之时，后宫嫔妃齐聚一堂，其乐融融。"
    show 皇帝 at chara
    皇上 "各位今日不必拘束。"
    hide 皇帝
    "众人" "是！"
    "大殿内，歌舞升平，热闹非凡。"
    python:
        templist = []
        for i in NPC_fz_list:
            if i == my:
                pass
            if huaiyun(i) == True or i.state == "病重" or jinzu(i) == True:
                pass
            else:
                templist.append(i)
            if my in templist:
                templist.remove(my)
            else:
                pass
            templist = sorted(templist, key=attrgetter("muzic"),reverse = True)

    if len(templist) == 0:
        pass
    else:
        $ fz = templist[0]
        $ templist.remove(fz)
        image fz = "Feizi/F[fz.face].webp"
        show fz at chara
        "[fz.hao][fz.weifen][fz.name]弹奏乐曲一首，优美动听。"
        hide fz
        $ fz.exp = fz.exp +10+ (fz.muzic*0.12)
        $ fz.love = fz.love +3 + (fz.muzic*0.05)

    if len(templist) == 0:
        pass
    else:
        $ templist = sorted(templist, key=attrgetter("dance"),reverse = True)
        $ fz = templist[0]
        $ templist.remove(fz)
        image fz = "Feizi/F[fz.face].webp"
        show fz at chara
        "[fz.hao][fz.weifen][fz.name]上台表演舞蹈一支，皇上赞不绝口。"
        hide fz
        $ fz.exp = fz.exp + 10 +(fz.dance*0.12)
        $ fz.love = fz.love +3 + (fz.dance*0.05)

    if len(templist) == 0:
        pass
    else:
        $ templist = sorted(templist, key=attrgetter("qingxiang"),reverse = True)
        $ fz = templist[0]
        image fz = "Feizi/F[fz.face].webp"
        show fz at chara
        if fz.muzic >= fz.dance and fz.muzic > 50:
            "[fz.hao][fz.weifen][fz.name]弹奏乐曲一首，优美动听。"
            $ fz.exp = fz.exp +5 + (fz.muzic*0.08)
            $ fz.love = fz.love +2+(fz.muzic*0.04)
        elif fz.muzic >= fz.dance:
            "[fz.hao][fz.weifen][fz.name]弹奏乐曲一首，但曲不成调。"
            "皇上皱着眉头让她退下了。"
            $ fz.exp = fz.exp - 5 - (beifei-fz.level)*3
            $ fz.love = fz.love - 3

        elif fz.muzic < fz.dance and fz.dance > 50:
            "[fz.hao][fz.weifen][fz.name]上台表演舞蹈一支，皇上赞不绝口。"

            $ fz.exp = fz.exp +5 + (fz.dance*0.08)
            $ fz.love = fz.love +2+ (fz.dance*0.04)
        elif fz.muzic < fz.dance:
            "[fz.hao][fz.weifen][fz.name]上台表演舞蹈一支，但舞步跌乱，贻笑大方。"
            "皇上皱着眉头让她退下了。"
            $ fz.exp = fz.exp - 10 - (beifei-fz.level)*3
            $ fz.love = fz.love - 5
        hide fz

    if my in biaoyan:
        $ shifoubiaoyan = 0
        $ biaoyan = []
        "终于轮到你上台……"
        if mybiaoyan.wcd >= 200:
            "一曲[mybiaoyan.name]，发挥完美，令人如痴如醉。"
            if mybiaoyan.leibie == "舞谱":
                $ tempnum = (my.dance*0.12)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp + 10 +tempnum
                $ my.love = my.love + 3+  (my.dance*0.05)
            else:
                $ tempnum = (my.muzic*0.12)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp + 10 +tempnum
                $ my.love = my.love + 3+  (my.muzic*0.05)

        elif mybiaoyan.wcd > 150:
            "一曲[mybiaoyan.name]，炉火纯青，令人如痴如醉。"
            if mybiaoyan.leibie == "舞谱":
                $ tempnum = (my.dance*0.08)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp +5+ tempnum
                $ my.love = my.love +2+ (my.dance*0.04)
            else:
                $ tempnum = (my.muzic*0.08)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp +5+ tempnum
                $ my.love = my.love +2+ (my.muzic*0.04)
        elif mybiaoyan.wcd < 100:
            "你的表演出了些差错，台上皇帝皱了皱眉，挥手让你退下。"
            $ my.exp = my.exp - 5 - (beifei-my.level)*2
            $ my.love = my.love - 3
        elif mybiaoyan.wcd < 50:
            "你的表演毫不熟练，贻笑大方。台上皇帝脸色阴沉，挥手让你退下。"
            $ my.exp = my.exp - 10 - (beifei-my.level)*3
            $ my.love = my.love - 5
        else:
            "一曲[mybiaoyan.name]，中规中矩，未出差错。皇上欣然颔首，让你落座。"
            if mybiaoyan.leibie == "舞谱":
                $ tempnum = (my.dance*0.05)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp + 4+ tempnum
                $ my.love = my.love + 1+ (my.dance*0.03)
            else:
                $ tempnum = (my.muzic*0.05)*(10+mybiaoyan.level*2)*0.1
                $ my.exp = my.exp + 4+tempnum
                $ my.love = my.love + 1+(my.muzic*0.03)
    else:
        pass



    if month == 6:
        python:
            templist = []
            for i in NPC_fz_list:
                if i.state == "病重" or jinzu(i) == True:
                    pass
                else:
                    templist.append(i)
        $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
        if templist[0] == my:
            "是否要向皇上敬酒？"
            menu:
                "举杯":
                    我 "今日皇上龙辰，臣妾敬您一杯。"
                    show 皇帝 at chara
                    皇上 "（大喜）好！"
                    皇上 "朕有佳人如斯，实乃大幸啊！"
                    皇上 "（一饮而尽。）"
                    hide 皇帝 at chara
                    $ my.exp = my.exp + 5 + (beifei-fz.level)*3
                    $ my.love = my.love + 3
                    $ my.skillcosts += 3
                "算了":
                    pass
        else:
            $ fz = templist[0]
            image fz = "Feizi/F[fz.face].webp"
            show fz at chara
            "[fz.hao][fz.weifen][fz.name]起身向皇上敬酒，皇上欣然大喜。"
            hide fz
            $ fz.exp = fz.exp + 5 + (beifei-fz.level)*3
            $ fz.love = fz.love + 3
            $ fz.skillcosts += 3
    else:


        python:
            templist = []
            for i in NPC_fz_list:
                if i.state == "病重" or jinzu(i) == True:
                    pass
                else:
                    templist.append(i)
        $ templist=sorted(templist, key=attrgetter("taihoulike"),reverse = True)
        if templist[0] == my:
            "太后在席间夸奖了你孝心可嘉，皇上听了非常高兴。"
            $ my.exp = my.exp + 5 + (beifei-fz.level)*3
            $ my.skillcosts += 3
        else:
            $ fz = templist[0]
            "太后在席间夸奖了[fz.hao][fz.weifen][fz.name]孝心可嘉，皇上听了非常高兴。"
            $ fz.exp = fz.exp + 5 + (beifei-fz.level)*3
            $ fz.skillcosts += 3

    "宴会落幕，众人散去……"
    jump 结束本旬

label 别人的宴会:
    python:
        templist = []
        for i in NPC_fz_list:
            if i == my:
                pass
            if huaiyun(i) == True or i.state == "病重" or jinzu(i) == True:
                pass
            else:
                templist.append(i)
            if my in templist:
                templist.remove(my)
            else:
                pass
            templist = sorted(templist, key=attrgetter("muzic"),reverse = True)

    if len(templist) == 0:
        pass
    else:
        $ fz = templist[0]
        $ templist.remove(fz)
        $ fz.exp = fz.exp +10+ (fz.muzic*0.12)
        $ fz.love = fz.love +3 + (fz.muzic*0.05)

    if len(templist) == 0:
        pass
    else:
        $ templist = sorted(templist, key=attrgetter("dance"),reverse = True)
        $ fz = templist[0]
        $ templist.remove(fz)
        $ fz.exp = fz.exp + 10 +(fz.dance*0.12)
        $ fz.love = fz.love +3 + (fz.dance*0.05)

    if len(templist) == 0:
        pass
    else:
        $ templist = sorted(templist, key=attrgetter("qingxiang"),reverse = True)
        $ fz = templist[0]
        if fz.muzic >= fz.dance and fz.muzic > 50:
            $ fz.exp = fz.exp +5 + (fz.muzic*0.08)
            $ fz.love = fz.love +2+(fz.muzic*0.04)
        elif fz.muzic >= fz.dance:
            $ fz.exp = fz.exp - 5 - (beifei-fz.level)*3
            $ fz.love = fz.love - 3

        elif fz.muzic < fz.dance and fz.dance > 50:
            $ fz.exp = fz.exp +5 + (fz.dance*0.08)
            $ fz.love = fz.love +2+ (fz.dance*0.04)
        elif fz.muzic < fz.dance:
            $ fz.exp = fz.exp - 10 - (beifei-fz.level)*3
            $ fz.love = fz.love - 5


    if month == 6:
        python:
            templist = []
            for i in NPC_fz_list:
                if i.state == "病重" or jinzu(i) == True:
                    pass
                else:
                    templist.append(i)
        $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
        $ fz = templist[0]

        $ fz.exp = fz.exp + 5 + (beifei-fz.level)*3
        $ fz.love = fz.love + 3
        $ fz.skillcosts += 3
    else:


        python:
            templist = []
            for i in NPC_fz_list:
                if i.state == "病重" or jinzu(i) == True:
                    pass
                else:
                    templist.append(i)
        $ templist=sorted(templist, key=attrgetter("taihoulike"),reverse = True)
        $ fz = templist[0]

        $ fz.exp = fz.exp + 5 + (beifei-fz.level)*3
        $ fz.skillcosts += 3
    return



label 错过表演:
    show 我的宫女 at chara
    我的宫女 "主子……不好了……"
    我的宫女 "太乐坊向皇上禀报了您报名才艺却未赴宴的事情，皇上似是很是生气……"
    我 "……知道了。"
    hide 我的宫女
    $ my.exp = my.exp - 20 - (beifei-my.level)*4
    $ my.love = my.love - 10
    $ biaoyan = []
    $ shifoubiaoyan = 0
    python:
        renpy.return_statement()



label 秀女觐见(fz):
    "宫人" "宣——[fz.family]，[fz.xing]氏[fz.ming]觐见。"
    show fz at chara
    if fz.xingge == "活泼":
        "秀女 [fz.name]" "（只见其脚步轻快地走上前来）臣女参见皇上。"
    elif fz.xingge == "清冷":
        "秀女 [fz.name]" "（只见其低头走上前来，声音清冷）臣女参见皇上。"
    else:
        "秀女 [fz.name]" "臣女参见皇上。"
    hide fz
    show 皇帝 at chara
    if fz.beauty > 900:
        $ tempnum = 15
        皇上 "（为其倾城美貌所震惊，一时未语。）"
    elif fz.qizhi > 900:
        皇上 "（为其谪仙气质所震惊，眼底溢出几分赞叹。）"
        $ tempnum = 15
    elif fz.meili > 900:
        皇上 "（被那媚惑的眼神勾了魂，一时失神。）"
        $ tempnum = 15
    elif fz.beauty > 700:
        皇上 "倒算得上是个美人。"
        $ tempnum = 8
    elif fz.qizhi > 700:
        皇上 "气质上佳，不错。"
        $ tempnum = 8
    elif fz.meili > 700:
        皇上 "摇曳生姿，不错。"
        $ tempnum = 8
    else:
        皇上 "看起来不大出挑，可有才艺？"
        hide 皇帝
        show fz at chara
        if fz.dance > fz.muzic and fz.dance >fz.book and fz.dance > fz.cixiu:
            "秀女 [fz.name]" "臣女善歌舞。"
            "秀女 [fz.name]" "（于大殿之中，轻展衣袖，回旋而舞。）"
            if fz.dance > 80:
                "秀女 [fz.name]" "（体态婀娜，如流风回雪。美目盼兮，如秋水连漪。）"
                $ tempnum = 8
            elif fz.dance > 50:
                "一曲舞毕，无功无过。"
                $ tempnum = 4
            else:
                "一曲舞毕，皇帝兴致缺缺。"
                $ tempnum = 0

        elif fz.muzic > fz.dance and fz.muzic >fz.book and fz.muzic > fz.cixiu:
            "秀女 [fz.name]" "臣女善音律。"
            "秀女 [fz.name]" "（取来一琴，指尖轻动，琴声渐起。）"
            if fz.muzic > 80:
                "秀女 [fz.name]" "（时而如高山流水，时而如小溪潺潺，悲欢缓急，尽付琴中。）"
                $ tempnum = 8
            elif fz.muzic > 50:
                "一曲奏毕，无功无过。"
                $ tempnum = 4
            else:
                "一曲奏毕，皇帝兴致缺缺。"
                $ tempnum = 0


        elif fz.book > fz.dance and fz.book >fz.muzic and fz.book > fz.cixiu:
            "秀女 [fz.name]" "臣女喜诗书。"
            "秀女 [fz.name]" "（取来笔墨，横展纸卷，执笔横书。）"
            if fz.book > 80:
                "秀女 [fz.name]" "（翰墨挥洒，下笔生花。）"
                $ tempnum =8
            elif fz.book > 50:
                "秀女 [fz.name]" "（片刻后呈上纸卷，还算尚可。）"
                $ tempnum = 4
            else:
                "秀女 [fz.name]" "（片刻后呈上纸卷，平平无奇。）"
                $ tempnum = 0
        else:

            "秀女 [fz.name]" "臣女喜刺绣。"
            "秀女 [fz.name]" "(呈上自家中带来的绣图。)"
            if fz.cixiu > 80:
                "秀女 [fz.name]" "（绣图精巧雅致，堪比宫中织女。）"
                $ tempnum = 8

            elif fz.cixiu > 50:
                "秀女 [fz.name]" "（绣图针脚齐平，心思秀巧，算是尚可。）"
                $ tempnum = 4
            else:
                "秀女 [fz.name]" "（绣图平平无奇，难登大雅。）"
                $ tempnum = 0

    hide fz

    python:
        temptext = ""
        for i in fz.sisters:
            if i in NPC_fz_list:
                temptext += str(i.cheng)
    if temptext != "":

        "宫人" "（小声）此秀女是[temptext]的家妹……"

    if fz.familylevel <= 1:
        $ tempnum = tempnum + 20
    elif fz.familylevel < 4:
        $ tempnum = tempnum + 10
    else:
        pass

    if hdxingge == "温柔":
        if fz.meili*0.7+fz.qizhi*0.3 > 1000:
            $ tempnum = tempnum +25
        elif fz.meili*0.7+fz.qizhi*0.3 > 800:
            $ tempnum = tempnum + 12
        else:
            pass
    elif hdxingge == "风流":
        if fz.beauty*0.7 +fz.meili*0.3 >1000:
            $ tempnum = tempnum +25
        elif fz.beauty*0.7 +fz.meili*0.3 >800:
            $ tempnum = tempnum +12
        else:
            pass
    elif hdxingge == "刚正":
        if fz.qizhi*0.7 +fz.beauty*0.3 >1000:
            $ tempnum = tempnum +25
        elif fz.qizhi*0.7 +fz.beauty*0.3 >800:
            $ tempnum = tempnum +12
        else:
            pass
    elif hdxingge == "冷漠":
        if fz.xinji < 100:
            $ tempnum = tempnum +25
        elif fz.xinji < 200:
            $ tempnum = tempnum +12
        elif fz.xinji < 400:
            $ tempnum = tempnum +8
        else:
            pass
    elif hdxingge == "腹黑":
        if fz.xinji > 900:
            $ tempnum = tempnum +25
        elif fz.xinji > 800:
            $ tempnum = tempnum +12
        elif fz.xinji > 600:
            $ tempnum = tempnum +8
        else:
            pass
    else:
        pass

    show 皇帝 at chara
    if my.love > 80:
        $ cheng = aicheng
    elif my.level == 0:
        $ cheng = "皇后"
    else:
        $ cheng = my.cheng
    皇上 "不知[cheng]觉得此女如何？"
    if tempnum >= 30:
        我 "（看起来皇上对[fz.name]十分满意，是必然会让此女入宫了。）"
    elif tempnum >= 20:
        我 "（看起来皇上对[fz.name]颇为欣赏。）"
    elif tempnum <= 10:
        我 "（看起来皇上对[fz.name]并不很感兴趣。）"

    if my.xinji - fz.xinji > 0 or fz.xinji - my.xinji < 100 or my.xinji > 800:
        if fz.xinji < 300:
            我 "（像是个没多大心机的。）"
        elif fz.xinji > 700:
            我 "（此人城府极深。）"
        else:
            pass
        if fz.qingxiang < 50:
            我 "（看起来倒不像是个惹是生非的……）"
        else:
            我 "（看起来便不是个善茬。）"
    else:
        pass


    menu:
        我 "（如何回答？）"
        "可以留用":
            $ tempbool1 = True
            $ fz.like = fz.like + round(my.love*0.2)
            $ tempnum = tempnum + round(my.love*0.1)
        "不宜入宫":
            $ tempbool2 = True
            $ fz.like = fz.like - round(my.love*0.2)
            $ tempnum = tempnum - round(my.love*0.1)
        "但凭皇上心意":
            if tempnum >= 20:
                pass
            else:
                $ tempnum = tempnum + renpy.random.randint(-5, 5)
    if tempnum >= 15 or fz in juqingfei:
        皇上 "（沉吟片刻）留牌子。"
        if tempbool2 == True:
            menu:
                "皇上不可！":
                    $ my.love = my.love - (tempnum-15)*0.5
                    皇上 "（皱眉）[cheng]……"
                    皇上 "也罢，赐花吧。"
                "其女不宜入宫啊":
                    $ tempnum = tempnum - round(my.love*0.1)
                    $ my.love = my.love - (tempnum-15)*0.2
                    $ fz.like = fz.like - (tempnum-15)*0.5
                    皇上 "（犹豫了一番。）"
                    if tempnum >= 15:
                        皇上 "（坚持）留牌子。"
                        $ ruxuan.append(fz)
                    else:

                        皇上 "也罢，赐花吧。"
                "（沉默不语）":
                    $ ruxuan.append(fz)
        else:

            $ ruxuan.append(fz)
    else:


        皇上 "（沉吟片刻）赐花离宫。"
        if tempbool1 == True:
            menu:
                "恳请皇上将她留下！":
                    $ my.love = my.love - (15-tempnum)*0.5
                    $ fz.like = fz.like + (15-tempnum)*0.5
                    皇上 "（皱眉）[cheng]……"
                    皇上 "也罢，那就留下吧。"
                    $ ruxuan.append(fz)
                "如此甚至可惜":



                    $ tempnum = tempnum + round(my.love*0.1)
                    $ my.love = my.love - (15-tempnum)*0.2
                    $ fz.like = fz.like + (15-tempnum)*0.2
                    皇上 "（犹豫了一番。）"
                    if tempnum >= 15:
                        皇上 "也罢，留牌子。"
                        $ ruxuan.append(fz)
                    else:

                        皇上 "（坚持）赐花。"
                "（沉默不语）":


                    pass
        else:

            pass

    $ NPC_newfz_list.remove(fz)
    python:
        if fz not in ruxuan:
            if len(fz.sisters) == 0:
                if fz.father in guanyuan_list:
                    guanyuan_list.remove(fz.father)
                del fz.father
            else:
                temp = fz.father
                temp.feizi.remove(fz)
                for i in fz.sisters:
                    if fz in i.sisters:
                        i.sisters.remove(fz)
        else:
            if len(fz.sisters) == 0:
                pass
            else:
                for i in fz.father.feizi:
                    if fz == i :
                        pass
                    elif fz not in i.sisters:
                        i.sisters.append(fz)
                    else:
                        pass

    hide 皇帝
    python:
        renpy.return_statement()

label 容予结局:
    $ rongyu9 = True
    scene black
    "深夜，你方睡下，却觉得心头一阵悸痛，太阳穴刺痛阵阵，难以入眠。"
    show 容予_duang at chara with Dissolve(2.0)
    我 "是……谁……"
    "???" "……"
    我 "谁……"
    "忽然，你一下子清醒了过来。"
    "脑海里的那个人，注视着你，那样悲伤。"
    "那种感觉充斥了你的全身。"
    "那个人的名字就仿佛一块碎片，扎在你的心里，却让你无法控制地呼喊了出来——"
    我 "容予！！"
    我 "容予，你不要走！！"
    hide 容予_duang at chara with Dissolve(2.0)
    show 寝居 with dissolve
    我 "……"
    我 "（容予，你是不是想告诉我什么？）"
    show 我的宫女 at chara
    我的宫女 "主子，您没事吧？（一脸担忧）是不是梦魇了，要奴婢陪着你吗？"
    我 "…………"
    我的宫女 "（似是自言自语）今晚倒真是邪门儿，方才还听人说奉天楼那边有异光隐现，很是诡异……"
    我 "（猛地回神）你说什么？"
    我的宫女 "奴、奴婢什么也没说。"
    show 寝居 with hpunch
    我 "去奉天楼，快，本宫要去奉天楼！"
    我的宫女 "主子，这么晚了，奉天楼早就进不去了！"
    "你顾不得宫人的阻拦，眼下只有一个念头——一定要见到容予。"
    scene black
    "不知为何，奉天楼的守夜人好像没有看到你一般，任由你闯入。"
    我 "容予……等我。"
    scene 幽宫 with Dissolve(2.0)
    show 掌祀 at chara with dissolve
    掌祀 "哦？"
    掌祀 "好像来了什么不得了的人呢。"
    hide 掌祀
    show 容予_哭 at chara with dissolve
    容予 "……"
    容予 "[aicheng]……"
    "容予像是不敢相信自己的眼睛，任由眼泪自眼眶中涌出。"
    "他想要靠近你，却仿佛有一道无形的墙将二人残忍分隔，再也不能动弹分毫。"
    hide 容予_哭
    show 掌祀 at chara
    掌祀 "（冷漠地看了容予一眼）快同本座进去，莫要误时辰。"
    我 "你休想带他走！"
    掌祀 "哦？"
    掌祀 "[my.cheng]娘娘可想清楚了——他不死，今夜过后，没的可是皇帝了。"
    我 "……"
    hide 掌祀
    show 容予_哭 at chara
    容予 "掌祀大人，请勿为难她。"
    容予 "我同你进去便是了。"
    hide 容予_哭
    show 掌祀 at chara
    掌祀 "嗯，随本座来吧。"
    我 "容予……不要……"
    hide 掌祀
    show 容予_哭 at chara
    容予 "[aicheng]，别哭。"
    容予 "能够再见你一面，我就已经很开心了。"
    我 "我也是……"
    容予 "今生能与你相逢，是我容予最大的幸事。"
    容予 "若有来生……"
    hide 容予_哭
    show 掌祀 at chara
    掌祀 "咳咳，本座必须打断一下，可莫怪本座不解风情——"
    掌祀 "今夜为了镇压魔邪之力，需要的不仅仅是你容予的命，而是你的魂魄。今夜过后，你的魂魄就将被邪神吞噬，永不复存。"
    掌祀 "自然，也不会再有来生。"
    hide 掌祀
    show 容予_哭 at chara
    容予 "永不复存……那又如何？"
    容予 "至少，[aicheng]，你记得我曾经存在过。"
    我 "我……永远也不会忘记。"
    我 "哪怕来生，再来生，我永远不会忘记，有一个叫做容予的男子在我的心里存在过。"
    容予 "谢谢你，[aicheng]。"
    hide 容予_哭
    show 掌祀 at chara
    掌祀 "容予公子，随本座来吧。"
    hide 掌祀
    show 容予_哭 at chara
    容予 "是。"
    hide 容予_哭
    我 "容予！！！"
    if rongyu8 == False:
        scene black with dissolve
        nvl clear
        旁白 "看到容予的身影逐渐消失在我的面前，有那么一瞬间，我似乎体会到了魂飞魄散的感觉。"
        旁白 "或许，如果一开始就不曾相遇，此刻便不会有这么痛了吧？"
        nvl clear
        旁白 "但，能和容予相遇、相识、相恋，我很高兴，也很幸福。"
        nvl clear
        旁白 "哪怕这一场相逢，注定以这样的结局收尾，我也从未后悔过。"
        旁白 "我相信，在容予站在邪神面前的最后一刻，也是这么想的。"
        nvl clear
        旁白 "再也不会有流言中伤，再也不会有冷眼相待，再也不会有人要他做无谓的牺牲。"
        nvl clear
        旁白 "从今以后，容予只在我的心里存在。"
        旁白 "——永远存在。"
        nvl clear
        旁白 "我的灵魂不灭，他便不灭。"
        nvl clear
        pause 2.0
        "再次睁开眼睛，你已经躺在自己的寝居之中。"
        "宫人说你晕倒在奉天楼外，是掌祀大人让人送你回来的。"
        "还托人给你留了一句话——"
        "“仪式既成，世间重得百年安宁。”"
    else:
        "???" "匀褚，站住！"
        show 掌祀 at chara with dissolve
        掌祀 "（身形虚化而至。）"
        "???" "让他们走吧。"
        "???" "……让这姑娘带着她喜欢的人离开这里。"
        hide 掌祀
        show 蒹葭 at chara with dissolve
        "不知道什么时候，一个少女的身影出现在离你不远的地方，站在匀褚的面前。"
        "少女" "听到了么？"
        hide 蒹葭
        show 掌祀 at chara
        掌祀 "蒹葭姑娘，您就别为难在下了。此事，也不是在下能够做主的。"
        hide 掌祀
        show 蒹葭 at chara
        蒹葭 "你不能做主，难道我不能吗？"
        蒹葭 "我说了，让他们走。"
        hide 蒹葭
        show 掌祀 at chara
        掌祀 "——今日镇魔之事……（匀褚好像突然想到了什么闭口不言，仍是一脸为难。）"
        hide 掌祀
        show 蒹葭 at chara
        蒹葭 "（脸上隐约浮现怒意）让他再想别的法子便是了！他若没有办法，那本姑娘亲自出马，难道还不行么？！"
        hide 蒹葭
        show 掌祀 at chara
        掌祀 "（似乎有些哭笑不得）蒹葭姑娘……"
        掌祀 "你可知道，他们一个是被剥夺了身份的天子手足，一个是被囚禁在这宫墙之内的天子后妃。他们从一开始，就不可能善终。"
        掌祀 "即便今日容予不死……"
        hide 掌祀
        show 蒹葭 at chara
        蒹葭 "让你别废话！"
        hide 蒹葭
        show 掌祀 at chara
        掌祀 "蒹葭姑娘！"
        "只见被称为“蒹葭”的少女手中幻化出一道迷离的光，顿时点亮了整个奉天楼——"
        hide 掌祀
        scene 梦幻花海 with Dissolve(2.0)
        我 "这里是……"
        show 容予_忧 at chara with Dissolve(1.0)
        我 "容予！！"
        容予 "[aicheng]……"
        容予 "这里是……邪神降临的幻像吗？"
        hide 容予_忧
        show 容予_笑 at chara
        容予 "若在灵魂消散的最后一刻见到的是你，那倒是甚好。"
        容予 "容予此生无憾了。"
        hide 容予_笑
        show 蒹葭 at chara
        蒹葭 "今生未了，谈何此生无憾？"
        蒹葭 "（看向你们二人）给你们一个机会，抛弃一切，离开这里——所有的一切，包括名字、身份、曾经的一切，你们能拥有的只有彼此，愿不愿意？"
        hide 蒹葭
        show 容予_忧 at chara
        容予 "我……我本便一无所有。"
        容予 "就连这颗心，也早已属于[aicheng]了。"
        hide 容予_忧
        menu:
            "我是天子嫔妃，容予，你我今生注定无缘":
                show 掌祀 at chara
                掌祀 "如何？蒹葭姑娘，收手吧。"
                hide 掌祀 with Dissolve(2.0)
                scene 幽宫 with vpunch
                "一阵剧烈的眩晕袭来——"
                "再回神时，眼前却已经空无一物。"
                我 "容予……"
                "脑海中，还回响着他最后一次呼唤你名字的声音……"
                我 "抱歉……"
                我 "我还有太多东西放不下。"
                scene black
            "我愿意":
                show 蒹葭 at chara
                蒹葭 "如何，匀褚，是我赢了？"
                hide 蒹葭
                show 掌祀 at chara
                掌祀 "（似是无奈）是了，您看着办罢。要是沉央大人怪罪下来，在下可一律不管。"
                hide 掌祀
                show 蒹葭 at chara
                蒹葭 "去送他们一程吧。"
                hide 蒹葭
                show 掌祀 at chara
                掌祀 "是。"
                hide 掌祀
                jump 容予HAPPYEND
    python:
        renpy.return_statement()

label 容予对话:
    if huaiyun(my) == True and rongyulike >= 80:
        $ lucky = 6
    elif rongyulike >= 80:
        $ lucky = renpy.random.randint(0, 5)
    elif rongyulike >= 60:
        $ lucky = renpy.random.randint(0, 4)
    else:
        $ lucky = renpy.random.randint(0, 2)
    if lucky == 0:
        容予 "你问我如果没有学医会做什么？"
        容予 "我也不知。"
        容予 "……倒不是敷衍你，只是觉得这世界上压根没有什么如果，所以也未曾去考虑过。"
        hide 容予
        if rongyulike >= 50:
            show 容予_笑 at chara
            容予 "倒是你，可曾想过没有如果入宫，如今会过着怎样的生活吗？"
            menu:
                "没有如果":
                    容予 "你看，那你方才还问我？"
                    我 "那我下次不问了，哼。"
                "和心爱的人共度余生":
                    我 "我当然会和喜欢的人在一起，白头偕老……"
                    我 "无关他长相是否英俊，家境是否富裕，但他定是世上最爱我之人。"
                    我 "容予，若以后你成亲了，可定要好好对你的妻子。"
                    hide 容予_笑
                    show 容予 at chara
                    容予 "那容予便只能谨遵[my.cheng]之命了。"
                    容予 "……定不负她。"
                "相夫教子，平淡度日":
                    if my.familylevel < 4:
                        我 "若我未能被选入宫，家族也会为我选择门当户对的夫婿。"
                        我 "大概就像寻常的世家主母那样，度过自己的一生吧。"
                        我 "除了不至于落得为妾的境地，倒和嫁给皇帝并无莫大分别，不是么？"
                    elif my.familylevel > 10:
                        我 "若我未能被选入宫，大概会像寻常的官家小姐那样嫁给门当户对的夫婿，度过自己的一生吧。"
                        我 "平平淡淡，倒也不差。"
                    else:
                        我 "若我未能被选入宫，如今大概也有了自己的夫君。"
                        我 "粗茶淡饭，布衣素服，倒也不差。"
    elif lucky == 1:
        "只见容予站于案边，案上放着一些药材。他动作熟练的将面前的药材，按照手里的药方子抓着药。"
        我 笑 "可是打扰到了？"
        容予 "（轻轻摇头，看了你一眼回话后，依旧忙着手头事）无碍。"
        我 "可是在给谁配药？"
        $ lucky = renpy.random.randint(0, 2)
        if lucky == 0:
            python:
                templist = []
                for i in NPC_fz_list:
                    if diwei(i) >= 1:
                        pass
                    elif i.love >= 30:
                        pass
                    elif i.health >= 700:
                        pass
                    else:
                        templist.append(i)
            if len(templist) == 0:
                容予 "是旁的太医接诊的一位娘娘，他眼下忙不过来，我便搭把手按药方抓好药罢了。"
            else:

                $ fz = renpy.random.choice(tempfzlist)
                容予 "是[fz.palace][fz.qinju]的[fz.cheng]，其近日有些风寒，不过现各太医都有其手头之事，我便搭把手按药方抓好药罢了。"
        elif lucky == 1:
            容予 "是太后娘娘的，太后言其近日有些许头疼，太医令不得空，便唤我按药方抓个药罢。"
        else:
            容予 "不过是一在御花园做事的宫女，前不久从这被调过去的，言近日深夜难眠，便帮其配个药助眠。"

    elif lucky == 2:
        "容予手中正看着一书卷，你没有瞧见内容，但其看得倒是认真，兴许是医书吧。"
        我 "可是在看些什么？如此入神。"
        容予 "（微微抬头，又轻轻摇头）不过是本翻烂了的老医书，温故而知新罢。"
    elif lucky == 3:
        容予 "其实父亲当初并不愿意带我进宫。然而娘亲早早去世，父亲无法让年幼的我独自待在家中，这才将我带在身边。"
        容予 "虽然没有、也无法得到正式的职位，但论资历，我也不逊于那几位得力的太医。"
        容予 "私塾？我并未去过……（苦笑）没有老师愿意收我，我这副相貌会吓到其他人的。"
        容予 "若非父亲在太医院德高望重，恐怕此处也容不下我。"
        我 "……"
        我 "（容予这么好的人，为什么要承受那些无妄的流言和非议呢？）"
        我 "（亦或是说，在经历那么多冷言冷语，他却仍然这样温柔地面对身边的一切……）"
    elif lucky == 4:
        我 "（今儿人倒是比平日里还要来得稀少……想来近日应鲜少有人身子不适。）"
        我 "（那容予今日应该闲着吧……）"
        "容予坐于案后，案上正放着一围棋盘，其手中还握着棋子并未放下。"
        我 笑 "容公子可是难得有此闲情雅致，不如手谈一局？"
        容予 "这……虽人不多，但也杂，若是有人进来瞧见.....此举不妥。"
        我 常 "无碍，我让我宫里的宫女代我行棋，我在其一旁便是，如此一来，旁人瞧着不过也就说我在此凑个热闹罢。"
        容予 "（再三思量，微低头，轻叹一声）唉……如此，好吧。"
        "与容予博弈许久……"
        "（才学上升）"
        $ my.book += 1
    elif lucky == 5:
        if month > 1 and month < 5:
            "容予正将水轻轻倒入茶壶之中，而里面所出的清香却与平日里所用的茶香不同。"
            "（浅笑）[my.cheng]尝尝便知。"
            $ lucky = renpy.random.randint(0, 1)
            if lucky == 0:
                我 "（接过茶盏，小小一抿，茶水竟是温的，且入口清凉，味也如此。再尝一口，可觉颈处微凉。）"
                容予 "此茶为薄荷，但平日里宫中多为干薄荷，但这壶里的是方才在太医院里新采下的鲜薄荷。"
            else:
                我 "（接过茶盏，小小一抿，茶水竟是温的，入口甘甜却不腻，闻着却是淡雅清香。）"
                容予 "此茶为茉莉，虽宫中常见，但在其中放入了些许蜂蜜，所味有所不同。"


        elif month > 4 and month < 8:
            "一旁案上有一篮筐，红黄半参，那尽是新采摘下来不久的覆盆子。而你如此了解此，只因儿时好友尤其喜欢这覆盆子，常到夏初便会到集市上买回不少，还不忘唤人来送些上门。"
            容予 "怎了？一直瞧着这覆盆子，可是想尝？"
            我 惊 "（他不说倒是还好，一说便馋了，也是许久未吃过了。）"
            容予 "若是想吃，我这去再采些，洗洗给[my.cheng]带回去一些便是，这些都是太医院的太医们在院中所种，为果甜而带点微酸，又可做药而用。"
            我 笑 "（……）"
        elif month > 7 and month < 11:
            $ lucky = renpy.random.randint(0, 1)
            if lucky == 0:
                "容予手中拴着一本册子，虽仍在搭理你但明显有些敷衍，便不再吭声待其弄完。没一会其便停在某页上，伸手拿出一物。此物是外头的落叶，细看可知乃是梧桐叶，可此叶扁平舒展，叶上的细节清晰可见，尤其好看。"
                容予 "儿时总喜这么玩，秋时的叶最为好看，便去捡了些做来给[my.cheng]罢，可还喜欢？"
                menu:
                    "很喜欢":
                        pass
                容予 "喜欢便好。"
            else:
                "其手中拴着一本册子，虽仍在搭理你但明显有些敷衍，便不再吭声待其弄完。没一会其便停在某页上，伸手拿出一物。此物正是秋时最为好看的银杏叶，但此叶扁平舒展，叶上的细节清晰可见，连叶炳都扁平不少，尤其好看。"
                容予 "儿时总喜这么玩，秋时的银杏叶最为夺目，便去捡了些做来给[my.cheng]罢，可还喜欢？"
                menu:
                    "很喜欢":
                        pass
                容予 "喜欢便好。"
        else:


            我 "说来……唔....哈啾～！"
            "你刚准备开口说些什么，却来了个喷嚏……而你反应也较快，连忙用手轻捂。而你却留意到他眉头微微皱了一下，却很快又舒开，但.....他不会是觉着我.....不容你多想，容予却夺过了你身后宫女帮你拿着的手炉，转身走向别处。"
            我 "这是……？"
            "话音刚落，容予便回来了，一把将你手拉到面前，将手中的手炉轻放于你手上。"
            容予 "一路过来手炉都凉了，里头的炭火都快燃尽了，从后宫至太医院怪远的，得着厚些，[my.cheng]若是不记得，让身后的[my.Gongnv[0].name]记着也不易着凉。现入冬了，若是不注意些，尤其容易得风寒的。"
    elif lucky == 6:
        $ lucky = renpy.random.randint(0, 5)
        if lucky == 0:
            容予 "[my.cheng]现有身孕，不应如此走动才是。"
            我 "但太医们不是说，得多走动走动吗？"
            容予 "唉，[my.cheng]可得听劝才是，况且这走动是在殿外，可不是到太医院这么远，若有什么闪失可不好…….罢了。"
            容予 "（小声）说多也不听。"
        elif lucky == 1:
            "（见你来了便连忙拿一椅子让你坐下，上了热茶还不忘给你把脉。）"
            容予 "[my.cheng]身子（强健等，直接对应身体体质那里的描写），我有可用于有孕之人调理身子的药方，等会抓些给[my.cheng]拿回去，煎来服下便是"
        elif lucky == 2:
            容予 "（小声）不知若是拿着诗书什的，对着这孩子念，其可会听懂记着……"
            我 "嗯？容予方才说什么？"
            容予 "……方才我并未开口，可是[my.cheng]听岔了。"
        elif lucky == 3:
            容予 "听闻若是给有孕之人做些力道中肯的按摩，会缓解些许腰酸等这些不适。"
            我 "真如此？说来近日的确有些腰酸，要不试试？"
            容予 "（惊慌）容予不敢，若是力道不适按错了什么地方，不管如何着实担当不起。"

        elif lucky == 4:
            容予 "（正给你把脉）近日可是吃了什么辛辣之物？"
            我 "（他怎么会知道？莫不是昨儿晚膳唤宫人去御膳房唤人做了点川菜，他路过御膳房看见了？）没有呀……"
            容予 "（若有所思）嗯.....那想来是吃食不够清淡，有些上火，近日可莫要吃辛辣，[my.cheng]身子有些虚，虽平时怀有身孕之人想吃何皆可，但若是腹泻什么的，可就得不偿失了。"
        else:
            容予 "[my.cheng]近日可得多吃些水果，若是有些什么事，来找容予便是。"
            我 "那可太好了，可想吃山楂了。"
            容予 "（惊恐）万万不可！山楂不可食！此物虽为水果但有孕之人不可碰，否则孩子……不仅是山楂，还有桂圆，容易上火的吃食也需少吃。"
    else:


        "剧情待补。先加好感。（当前好感[rongyulike]）"
    $ timenum = timenum +1
    $ AP = AP -1
    $ rongyulike = rongyulike + 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
