label 宣政殿:
    $ bg("宣政殿外")
    show screen notify("宣政殿")
    if timenum == 1:
        "如今正是早朝的时间……"
        "在宣政殿外等待了一会儿，到了下朝的时间，官员们鱼贯而出，但并未看到[guoxing][emperor]的身影。"
        $ timenum = timenum +1
        $ AP = AP -1
    else:

        "宣政殿空无一人，殿外有侍卫把守。"

    jump 皇宫界面


label 圣宸宫_late:
    $ bg("圣宸宫外")
    show screen notify("圣宸宫")
    show 赵公公 at chara
    赵公公 "哎哟，这不是[my.cheng]么？您怎么这时候来了？还是请回吧！"
    jump 皇宫界面

label 圣宸宫:
    $ bg("圣宸宫外")
    show screen notify("圣宸宫")
    show 赵公公 at chara
    if my.love < 11:

        赵公公 "见过[my.cheng]。"
    elif my.love < 51:
        赵公公 "见过[my.cheng]，不知您今日前来，所为何事？"
    else:
        赵公公 "诶唷，[my.cheng]，奴才见过[my.cheng]！"

    menu:
        "贿赂公公" if huilu == 0 and my.state == "寻常":
            $ huilu = 1
            我 "皇上进来忙于政务，公公您也多有操劳。"
            赵公公 "多谢[my.cheng]挂念，哎哟，您这是……"
            我 "（要打点什么给赵公公呢？）"
            menu:
                "二十两银子" if money >= 20:
                    $ money = money -20
                    $ mustshiqin = mustshiqin +15
                "十两银子" if money >= 10:
                    $ money = money -10
                    $ mustshiqin = mustshiqin +7
                "一个香囊":
                    $ mustshiqin = mustshiqin+renpy.random.randint(0, 3)
            我 "一点心意罢了，还请收下。"
            赵公公 "唉，您可真是客气。"
            赵公公 "那奴才就多谢[my.cheng]了。"
            if my.shiqin == 0:
                我 "自我入宫以后还未得陛下垂青……"
                我 "公公是陛下跟前的红人，还请公公多多美言几句。"
                赵公公 "瞧您说的，以您的资质，迟早会得到皇上宠爱的！"
                $ mustshiqin = mustshiqin+renpy.random.randint(5, 10)
                赵公公 "不过，既然您这么说了，那奴才自然尽力而为。"
            else:
                pass
        "面见圣上" if timenum > 1:
            if chuhuan_time <= 4 and chuhuan_0 == True and chuhuan_1 == False:
                赵公公 "[my.cheng]，皇上正烦心呢，请随奴才来吧。"
                jump 皇帝互动
            elif my.shiqin == 0 and my.level > 4:
                赵公公 "这……"
                我 "公公……"
                赵公公 "说实话的，皇上都没有临幸过您，又怎么会见您呢？"
                我 "公公的意思是……"
                赵公公 "圣宸宫非正二品以上，无召不得入，这是宫里的规矩，奴才也没有办法。"
                赵公公 "[my.cheng]，您还是请回吧。"
            elif my.level > 4 and my.love < 50:
                赵公公 "这……"
                赵公公 "圣宸宫非正二品以上，无召不得入，这是宫里的规矩，奴才也没有办法。"
                赵公公 "[my.cheng]，您还是请回吧。"
            elif my.level >4:
                赵公公 "按照规矩，圣宸宫非正二品以上，无召不得入。"
                赵公公 "不过既然是您，那奴才还是进去禀报一声。"
                "过了一会儿……赵公公走上前来。"
                $ lucky = round(my.love/10)
                $ lucky = abs(10 - lucky)
                $ lucky = renpy.random.randint(0,lucky)
                if lucky == 0:
                    赵公公 "[my.cheng]，请随奴才来吧。"
                    jump 皇帝互动
                else:
                    赵公公 "[my.cheng]，皇上这会儿正在处理政务，您请回吧。"
            else:

                赵公公 "奴才这就进去通禀一声。"
                if my.love >50:
                    $ lucky = renpy.random.randint(0,1)
                elif my.love > 0:
                    $ lucky = renpy.random.randint(0,3)
                else:
                    $ lucky = renpy.random.randint(0,8)
                if lucky == 0:
                    赵公公 "[my.cheng]，请随奴才来吧。"
                    jump 皇帝互动
                else:
                    赵公公 "[my.cheng]，皇上这会儿正在处理政务，您请回吧。"
        "送点吃食":

            if my.shiqin == 0:
                赵公公 "这……"
                我 "公公……"
                赵公公 "说实话的，皇上都没有临幸过您，又怎么会用您送来的吃食呢？"
                我 "公公的意思是……"
                赵公公 "唉……（犹豫）"
                if my.familylevel < 4:
                    赵公公 "毕竟也是您的一片心意，奴才就替您送这一回吧。"
                    我 "既然如此那边多谢公公了！"
                    赵公公 "您以后若能得到陛下的宠爱，可别忘了奴才啊。"
                    我 "这是自然。"
                    我 "不打扰公公了，告辞。"
                    $ mustshiqin = mustshiqin + renpy.random.randint(5,8)
                else:
                    赵公公 "皇上忙于政事，奴才也不敢贸然打扰。"
                    赵公公 "[my.cheng]，您还是请回吧。"
            elif my.love > 50:
                赵公公 "奴才这就替您把吃食送去。"
                赵公公 "皇上要是知道您对他如此上心，一定会很高兴的。"
                我 "那便有劳公公了。"
                $ mustshiqin = mustshiqin + round(my.love*0.1)
            elif my.level < 4:
                赵公公 "奴才遵命。"
                我 "那便有劳公公了。"
            else:
                $ lucky = renpy.random.randint(3,my.level)
                if lucky == 3:
                    赵公公 "奴才这就替您把吃食送去。"
                    我 "那便有劳公公了。"
                    $ mustshiqin = mustshiqin + round(my.love*0.1)
                else:
                    赵公公 "（面有难色）唉，[my.cheng]您这会儿来的不是时候哇。"
                    赵公公 "皇上现在不想被打扰。请恕奴才不能提您将东西送进去了。"
                    赵公公 "您请回吧。"
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面



label 奉天楼:
    $ bgm("FTL")
    $ bg("奉天楼")
    show screen notify("奉天楼")
    menu:
        "望仙殿":
            jump 望仙殿
        "观仙台" if guanxiantai == True:
            jump 观仙台
        "旅祀大典" if month == 12 and lvxian == True:
            jump 旅祀大典
        "陪伴阿檀" if 0 < atan_time <= 10 and 1 <= atan_end_2 < 7:
            jump 陪伴阿檀

label 陪伴阿檀:
    $ bg("观仙台")
    with fade
    if atan_end_2 == 1:
        show 阿檀
        阿檀 "[my.cheng]娘娘……"
        我 笑 "可感觉好些了？"
        阿檀 "（点头）可是您……"
        我 "观仙台地势险峻，但站在这里，却给人超脱俗世之感。"
        我 "有时候，本宫甚至会有一种错觉……"
        阿檀 "觉得自己好像变成了飞鸟？"
        我 "哦，阿檀为何得知？莫非，你也如此想过？"
        阿檀 笑 "阿檀不想做飞鸟。"
        阿檀 笑 "不过，听旁的人说过相似的话罢了。"
        我 "还有别人？是宫里的嫔妃么？"
        阿檀 常 "是……一个有缘人罢。"
        我 "有缘人？"
        阿檀 "同您一样，是阿檀的有缘人。"
        我 笑 "陪本宫走走可好？"
        阿檀 "是。"
    elif atan_end_2 == 2:
        show 阿檀
        我 "阿檀知道我会来？"
        阿檀 "是。"
        我 "咦……修行人都有这样的能力，可以预知他人的言行？"
        阿檀 "不，大抵只是您与阿檀有缘罢了。"
    elif atan_end_2 == 3:
        show 阿檀
        阿檀 思 "阿檀的师尊么……"
        阿檀 "真是个让人不知道该如何去形容的存在呢。"
        阿檀 常 "听人说，先帝尚且年幼之时，因当年国乱不断，皇帝才下旨在宫中修建了奉天楼，而师尊盛名在外，便被皇帝请来做了掌祀。"
        阿檀 "不过师尊不喜欢待在皇宫里，时常在外游历……等到匀褚师兄能够独当一面以后便辞去了职务，离开了皇宫，迄今也逾十载了。"
        阿檀 "按照传闻推断，师尊的年纪没有上百也是鲐背高龄了。不过在阿檀的记忆里，他却是隽逸绝伦，貌若青年呢。"
        阿檀 笑 "所以，师尊或许已经活了几百岁了也说不定。"
        我 笑 "（噗呲）"
        我 "（那不是成仙了？）"
        阿檀 常 "不过阿檀一直觉得很奇怪，以师尊的性子，居然肯顺应当时天子的请求，入宫任职。尤其是想起他将掌祀之物一应交给匀褚师兄时那如释重负的表情……"
        阿檀 "若如此厌恶皇宫禁苑，一开始便拒了便是。他若不愿，怕是绑也绑不来。"
        我 "谁知道那种老神仙心里在想什么呢。"
        阿檀 "他以前好像说过，他在等一个人，然而等了很多年也没有等到，最终才离去了。"
        我 "你师尊在宫里待了那么多年都没有等到，若他等的是凡人，怕的确是一生无缘了。"
        阿檀 "嗯……不过，前不久师兄还说过，师尊现在恐怕是后悔莫及了。"
        我 "后悔什么？"
        阿檀 "大抵是后悔离宫，同那人错过了罢。"
    elif atan_end_2 == 4:
        show 阿檀
        我 "阿檀，你在奉天楼待了这么久，可曾见过神仙么？"
        阿檀 思 "嗯……"
        我 "难道你真的见过，但是不能透露？"
        阿檀 笑 "有什么不能同您讲的？"
        阿檀 笑 "可惜阿檀没有见过。"
        我 "啊……"
        阿檀 常 "或许见过呢，或许您也见过。"
        阿檀 "只是不知道罢了。"
        我 "若是真能见到神仙降世，怎么可能不知呢？"
        阿檀 "阿檀曾经问过师尊，修行一世，是否亲眼见过神迹。"
        阿檀 "师尊说，神明从不刻意隐藏行踪，也不吝于给与凡世怜悯。阿檀幼时病重，也是神明指引，才让师尊与阿檀相遇。"
        我 "（等阿檀好些以后还是少来这里吧，免得变得神神叨叨的。）"
    elif atan_end_2 == 5:
        show 阿檀
        阿檀 笑 "阿檀见过[my.cheng]娘娘。"
        我 "不必拘礼了。今日气色看起来好多了。"
        阿檀 "有您福泽庇佑，阿檀哪敢不好呢？"
        我 "你呀……（试探）可看开了？"
        阿檀 "看不看开，那些人和事都摆在那里。"
        阿檀 "有缘无缘，终究也是斑驳在这尘世间罢了。"
        阿檀 "多少人求之不得，多少人得而复失……身处凡世，便安于尘世，等到机缘际会之日，自有心魂解脱之时。"
    else:
        show 阿檀 出宫
        阿檀 出宫 笑 "[my.cheng]娘娘！"
        我 笑 "阿檀近日又知道本宫会来？"
        阿檀 "是阿檀在等……"
        阿檀 "今日有话对您说。"
        我 常 "嗯，你说。"
        阿檀 出宫 常 "阿檀……想同你告别。"
        我 "（？！）"
        我 "你要去哪儿？"
        阿檀 "太后娘娘心怀百姓，早几年便命人安排，在各州各地修建奉神之所，如今不少已经落成。"
        阿檀 "阿檀在奉天楼久蒙神佑，这次便自请出宫，到其他州县向百姓们倾传神意，助他们享恩沐泽。"
        我 "……"
        我 笑 "这是好事，阿檀。"
        阿檀 "（退后两步，于你身前双膝跪地）阿檀跪谢娘娘救命之恩。"
        我 "（看着眼前这个女子……仿佛看到了圣洁而无私的神女。）"
        我 "（突然明白了为何她的师尊曾告诉她“神明从不刻意隐藏行踪，也不吝于给与凡世怜悯。”）"
        我 "（对于那些以后将被阿檀无私地伸出援手的疾苦之人来说，阿檀已然同神明无异。）"
        hide 阿檀 with fade




    $ atan_end_2 += 1
    $ timenum = timenum + 2
    $ AP = AP -2
    jump 皇宫界面

label 旅祀大典:
    $ bg("旅祀大典")
    if guanxiantai == False:
        show 掌祀 at chara with dissolve
        "？？？" "奉天楼掌祀匀褚，见过[my.cheng]。"
        掌祀 "今日您前来大典，可是有求于上天，有求于神明？"
        我 "掌祀大人这是何意？"
        掌祀 "若您真的被琐事烦扰，想借上天之力达成心愿，在下愿意助您一臂之力。在下虽非神明，但可借神明之名，替您得偿所愿也说不定呢……"
        我 "得偿所愿……"
        掌祀 "奉天楼掌祀一职，乃是司皇家观星、祭祀之事，向皇帝、太后传达神明之意，以确保顺遂天意，社稷安康。"
        掌祀 "[my.cheng]可知，若在下观测星相，传听神意，得知宫中某人流年不吉，那人会是什么后果么？"
        我 "……（莫名悚然。）"
        掌祀 "哪怕位居中宫，若冲撞了皇帝、太后，也是会被废黜。更不要说其他微末之人……"
        我 "本宫不明白。"
        掌祀 "噫，既然您会这么说，那大概是明白在下的意思了。"
        掌祀 "在下虽是这世上离神明最近之人，但毕竟也并非神明，而是俗人。"
        掌祀 "有钱能使鬼推磨，这话放在奉天楼，也是行得通的。"
        掌祀 "若有人叫您看不顺眼了，带上银两来寻在下，在下必将为您分忧。"
        我 "任何人都可以么？"
        掌祀 "那倒不是。需得是您的结怨之人。"
        我 "这是为何？"
        掌祀 "（诡谲轻笑）冤有头债有主——若上头怪罪下来，在下也不过是个从犯，不是么？不过若您执意相求，倒也不是不可——不过，得付双倍的价钱。"
        我 "……（上头？该不会是……）"
        我 "除了银两，当真没有别的代价和风险么？"
        掌祀 "谁知道呢。"
        掌祀 "选择权在您。"
        掌祀 "起价一千两，四千银子封顶，非结怨之人双倍。若您起了心思，来观仙台找在下便是。"
        hide 掌祀 with dissolve
        "只感觉一阵风吹过，那个男子的身影转眼便消失不见……"
        $ zhangsi = True
        if guanxiantai == False:
            $ guanxiantai = True
            "地图 奉天楼-观仙台 已开放。"
        else:
            pass
    else:




        pass
    menu:
        "祈愿":
            menu:
                "愿圣恩常伴":
                    $ my.love = my.love + (100-my.love)*0.05
                "愿芳华永筑":
                    $ my.health = my.health + renpy.random.randint(5, 15)
                    $ my.beauty = my.beauty + renpy.random.randint(5, 15)
                    $ my.qizhi = my.qizhi + renpy.random.randint(5, 15)
                    $ my.meili = my.meili + renpy.random.randint(5, 15)
                "愿儿女聪慧" if len(my.kids) > 0:
                    python:
                        for i in my.kids:
                            if i.like <= 0:
                                pass
                            i.iq = i.iq + i.like*0.05
            "当你许下愿望之后，隐隐约约一个声音，仿佛来自天边，又近在耳畔，空灵缥缈，不知是男是女，是老是少，甚至连话语也听不分明。"
            "但只觉得心境莫名平静祥和。"
            $ lvsicishu = lvsicishu + 1
            if lucky < 0:
                $ lucky = lucky + 2
            else:
                $ lucky = lucky + 4
            $ AP = AP - 3
            $ timenum = 5
        "离开":
            pass
    jump 皇宫界面






label 观仙台:
    $ bg("观仙台")
    show screen notify("观仙台")
    if zhangsi == False and month != 12:
        "观仙台外，一个诡丽的身影翩然而至。"
        show 掌祀 at chara with dissolve
        掌祀 "见过[my.cheng]。在下就知道，你一定会来。"
        我 "你上次所说之事，究竟是何意？"
        掌祀 "呵呵……上次在下已经介绍过了，在下乃是奉天楼掌祀，司皇家观星、祭祀之事，向皇帝、太后传达神明之意，以确保顺遂天意，社稷安康。"
        掌祀 "[my.cheng]可知，若在下观测星相，传听神意，得知宫中某人流年不吉，那人会是什么后果么？"
        我 "……（莫名悚然。）"
        掌祀 "哪怕位居中宫，若冲撞了皇帝、太后，也是会被废黜。更不要说其他微末之人……"
        我 "本宫不明白。"
        掌祀 "噫，既然您会这么说，那大概是明白在下的意思了。"
        掌祀 "在下虽是这世上离神明最近之人，但毕竟也并非神明，而是俗人。"
        掌祀 "有钱能使鬼推磨，这话放在奉天楼，也是行得通的。"
        掌祀 "若有人叫您看不顺眼了，带上银两来寻在下，在下必将为您分忧。"
        我 "任何人都可以么？"
        掌祀 "那倒不是。需得是您的结怨之人。"
        我 "这是为何？"
        掌祀 "（诡谲轻笑）冤有头债有主——若上头怪罪下来，在下也不过是个从犯，不是么？不过若您执意相求，倒也不是不可——不过，得付双倍的价钱。"
        我 "……（上头？该不会是……）"
        我 "除了银两，当真没有别的代价和风险么？"
        掌祀 "谁知道呢。"
        掌祀 "选择权在您。"
        掌祀 "起价一千两，四千银子封顶，非结怨之人双倍。若您起了心思，来观仙台找在下便是。"
        hide 掌祀 with dissolve
        "只感觉一阵风吹过，那个男子的身影转眼便消失不见……"
        $ zhangsi = True
        $ timenum = timenum +2
        $ AP = AP -2
        jump 皇宫界面
    elif year >= 8 and rongyulike >= 60 and zhangsi == True and month != 12 and rongyu3 == True and rongyu4 == False and rongyu5 == 0:
        $ rongyu5 = 1
        $ rongyu = False
        "走到观仙台，远远便看到一个身穿华服的身影，显然并非此处的神职者。"
        show 我的宫女 at chara
        我的宫女 "主子，太后娘娘好像在前面。"
        我的宫女 "太后娘娘在同人说话，咱们还是先不要贸然打扰吧。"
        hide 我的宫女
        show 太后 at chara
        太后 "掌祀大人那边可有说法了？"
        "奉天楼祭祀" "掌祀大人说，那人的确是先帝血脉，其血其魂，与陛下同效。"
        "奉天楼祭祀" "此事，可成。"
        太后 "（沉默了半晌，似仍是纠结犹豫。）"
        "奉天楼祭祀" "掌祀大人还说，此事需尽快准备，若是迟了，陛下的命可就……"
        太后 "哀家知道了。告诉你们掌祀，尽快处理妥当。"
        "奉天楼祭祀" "是。"
        太后 "为了皇上，哀家可惜牺牲一切……"
        "太后叹着气，转身朝着观仙台外走去。"
        show 莲稚 at chara
        莲稚 "太后娘娘……"
        hide 莲稚
        show 太后 at chara
        太后 "唉，莲稚，哀家明白。皇上不仅仅是哀家的儿子，更是天下之主！"
        太后 "能为皇上牺牲，也算是那人的荣幸！"
        show 莲稚 at chara
        莲稚 "（看出太后是在劝说自己的内心，却不知如何开口）太后娘娘说的是……"
        莲稚 "此事是否要告诉皇上呢？"
        hide 莲稚
        show 太后 at chara
        太后 "不必了，皇上政务繁忙，这事哀家处理，就当什么都没有发生过吧。"
        太后 "（又是一叹）皇上亲政爱民，若得知自己的亲弟弟要替自己而死，即便深明大义理解哀家的用心，恐怕心里也难免有所芥蒂。"
        太后 "莲稚，此事只有哀家、奉天楼、太医令和容予还有你知道，不可告诉任何人，哪怕是建章宫其他宫人。"
        show 莲稚 at chara
        莲稚 "太后放心。太医令那边奴婢也会打点好，不会让他说出去半个字。"
        hide 莲稚
        show 太后 at chara
        太后 "太医令的为人哀家放心，况且他就算说出此事，对他也没有半分好处。"
        太后 "他当初苦苦哀求，才得了这个养子，如今也算是为国尽忠了。等过些日子，哀家让皇上赏赐他一番，让他出宫安度晚年去吧。"
        show 莲稚 at chara
        莲稚 "您向来是宅心仁厚的。"
        hide 莲稚
        show 太后 at chara
        太后 "（阖眸，似是在回忆往昔。）"
        if taihouxinge == "擅权":
            太后 "当初先帝独宠容予的母妃，哀家容不下他们母子，便让太医令替哀家将二人除去。"
            太后 "只是本该再那妖妃生产时一尸两命，不知为何，这孽种竟活了下来。"
            太后 "哀家让太医令斩草除根，他却不肯。哀家看在他曾在哀家生皇上时救了哀家一命，这才答应，留下容予的性命，给他抚养。"
            太后 "没想到一时的妇人之仁，如今竟救了我儿一命，哀家理应高兴才是。"
            "太后自我安慰一般笑了笑，快步离开了观仙台。"
        else:
            太后 "当初先帝独宠容予的母妃，先太后等人容不下他们母子，暗中命太医令在安胎药中做了手脚，意图让其一尸两命。"
            太后 "不知为何，这孩子竟活了下来。"
            太后 "先太后让哀家替她斩草除根，哀家只能寻了太医令。太医令却说自从手上沾染了鲜血以后便日夜不宁，不肯再做夺人性命之事。哀家看在他曾在哀家生皇上时救了哀家一命，这才答应，留下容予的性命，给他抚养，不可叫先太后等人知道容予还活着。"
            太后 "没想到一时的妇人之仁，如今竟救了我儿一命，哀家理应高兴才是。"
            "太后自我安慰一般笑了笑，快步离开了观仙台。"
        hide 太后
        我 "（怎么会……容予居然是先皇之子，皇上的亲兄弟？！）"
        我 "（而且……太后说……）"
        我 "（要让容予替皇上……）"
        我 "这究竟是怎么一回事？！"
    elif year>= 8 and rongyulike >= 60 and 0 < rongyu5 <= 6 and rongyu7 == False:
        $ rongyu7 = True
        $ rongyu = False
        我 "（急匆匆地闯进观仙台。）"
        show 掌祀 at chara with dissolve
        掌祀 "在下奉天楼掌祀恭迎娘娘。在下早便听到您的脚步声了。"
        我 "容予……容予在哪里？"
        掌祀 "[my.cheng]知道自己在说什么吗？若太后此刻在这里，恐怕您的命便要和他一起没了。"
        我 "你们真的要容予的命……"
        掌祀 "我们？"
        掌祀 "娘娘折煞，这是天意。"
        我 "天意……天意怎么会偏偏要容予的命？"
        掌祀 "（嘲讽一般地笑着）天机不可泄露。"
        hide 掌祀
        "一名祭司走了过来，恭敬地朝着匀褚行礼。"
        "祭司" "掌祀大人，宿戒已经准备完备。还请您示下。"
        show 掌祀 at chara
        掌祀 "此事必得万无一失，稍后本座会亲自一一验过。"
        掌祀 "先下去罢。"
        掌祀 "顺带，送[my.cheng]离开。"
        hide 掌祀
        "祭司" "是。"
        我 "至少，让我再见容予一面吧！"
        我 "我可以给你钱！要多少都可以！"
        "然而匀褚的身影在转瞬间便如风般消散。"
        "祭司默念着咒语，片刻的眩晕袭来。"
        scene black
        "再度清醒过来的时候，你已经离开了观仙台。"
        $ bg("奉天楼")
        with fade
        我 "（容予……你现在究竟怎么样了？）"
        我 "（为什么他们口口声声说是天意，天意为何要你去死呢？）"
        "回过神来，你看到前方不远处站着一个男子，衣着服饰与奉天楼祭司们相似，只是更显缥缈。"
        menu:
            "是否要向其打听？"
            "上前":
                $ rongyu8 = True
                show 沉央 at chara with Dissolve(1.0)
                我 "这位公子，您可在奉天楼见过一位……白发异瞳的男子？"
                "???" "见过。"
                我 "您可知道他在哪里？如今怎么样了？可……可有法子见到他？"
                "???" "……"
                我 "（急切）请您告诉我！"
                "???" "奉天楼密典所载——"
                "???" "上古有魔邪，穷凶暴虐，且不死不灭，非以天家血脉相祭，则无镇压之法。魔邪百年降世，一出既乱阴阳、破太平，饮人血、食人命，国破人亡，世无宁日。"
                "他没有开口，却有声音在你的脑海中响起。"
                我 "非以天家血脉相祭……"
                我 "所以，才会是容予……"
                我 "只因身在皇家，容予生来便没了母妃。只因身在皇家，就要替从未以兄弟相称的皇上去死，哪怕，他一日也不曾拥有过皇家的待遇……反而背上不详之名，遭人冷眼排挤。"
                我 "若这便是天意，天意又为何如此不公？"
                我 "他明明什么也没有做错，为何偏偏要如此苛待容予？"
                我 "你们奉天楼就只有让容予牺牲这一个法子么？！"
                "面对你的质问，男子并未回答。"
                "只听脑海中一声沉沉的叹息，眼前的身影便化为了一片虚无。"
                hide 沉央 with Dissolve(2.0)
            "离开":
                我 "事到如今，恐怕一切皆是徒劳。"
                我 "容予……"
                我 "今生的缘分，就等来生再续吧。"
        $ timenum = timenum + 1
        $ AP = AP - 1
        jump 皇宫界面
    else:


        pass
    menu:
        "找匀褚商量阿檀的事" if atan_time < 11 and atan_end_1 == 1 and 3 not in atan_help:
            show 掌祀 at chara
            我 "阿檀身为奉天楼司祝，若被册为嫔妃，恐怕会让陛下、太后内心不安……"
            掌祀 "若是在下出面，替阿檀寻个由头，便无此忧——您是想这么说？"
            我 "是。"
            掌祀 "好说好说，阿檀与在下是同门师兄妹，若娘娘觉着阿檀入宫是个好的归宿，在下也为她高兴呢。"
            掌祀 "娘娘愿意倾囊，那在下便愿意相助。"
            menu:
                "答应":
                    $ atan_help.append(3)
                    我 "那便这样说定了。"
                    掌祀 "[my.cheng]真的愿意如此帮助阿檀？"
                    我 "怎么，你又反悔了？"
                    掌祀 "是……"
                    掌祀 "阿檀能遇上您，真是她三生有幸。"
                    掌祀 "如此，在下身为阿檀的同门师兄，却要收您的银子，倒是令人羞愧了。"
                    我 "你是说……"
                    掌祀 "在下这次不收您的银子，阿檀的事，在下会出面相助的。"
                    我 "如此甚好。"
                    掌祀 "那在下便去跟阿檀说一声，叫她养好身子，方可陪伴陛下。"
                "算了":
                    我 "呵，本宫另寻法子便是了。"
        "面见掌祀" if month!= 12:
            if len(bujifz) == 1:
                "候了良久，却未见人至，后听几个小厮说起其正为旁的事情忙碌。"
                jump 观仙台
            else:
                show 掌祀 at chara with dissolve
                掌祀 "可想好了？"
                $ templist = []
                python:
                    for i in NPC_fz_list :
                        if i == my:
                            pass
                        else:
                            templist.append(i)
                call screen choicefz(templist)


                $ tempfz = fz

                if tempfz.level == 0:
                    $ tempnum = 4000
                elif tempfz.level < 4:
                    $ tempnum = 2400
                elif tempfz.level < 8:
                    $ tempnum = 1500
                else:
                    $ tempnum = 1000
                if tempfz not in my.foes or my not in tempfz.foes:
                    $ tempnum = tempnum*2
                else:
                    pass
                掌祀 "您可想好了，确是[tempfz.cheng]？只需[tempnum]两银子便是了。"
                menu:
                    "确定" if money >= tempnum:
                        $ money = money - tempnum
                        $ bujifz.append(tempfz)
                        掌祀 "在下明白。您且等着便是。"
                        hide 掌祀 with dissolve
                        $ my.shou = my.shou - 2
                        $ timenum = timenum + 2
                        $ AP = AP -2
                        jump 皇宫界面
                    "算了":


                        掌祀 "您慢慢考虑。"
                        hide 掌祀 with dissolve
                        jump 观仙台


        "占卜（50两）" if month != 12:
            menu:
                "问天命" if money>=50:
                    $ tempnum = int(my.shou - my.age)
                    "你跪在观仙台外，按照祭祀的要求在心中默问。"
                    if tempnum <= 0:
                        "未几，祭祀走上前来，朝着你拜了一拜，随即一言不发地转身离开了。"
                        "但，沐浴在奉天楼的肃穆气息之下，你内心隐约有种预感。"
                    else:
                        "未几，祭祀递过来一张带着香火味的小笺，上面写着“[tempnum]”。"
                    $ timenum = timenum + 2
                    $ AP = AP -2
                    jump 皇宫界面
                "问子嗣" if money>=50:
                    "你跪在观仙台外，按照祭祀的要求在心中默问。"
                    python:
                        tempnum2 = 0
                        for i in my.kids:
                            if i.shengmu != my:
                                pass
                            else:
                                tempnum2 += 1
                    if tempnum2 <= 0:
                        $ tempnum2 = 0
                    else:
                        pass
                    if my.lucky >= 100 and tempnum2 == 0:
                        $ tempnum =  "必"
                        "未几，祭祀递过来一张带着香火味的小笺，上面写着“[tempnum]”。"
                    elif my.lucky < 0 or my.health < 100 or tags[6] in my.tags:
                        $ tempnum =  "无"
                        "未几，祭祀递过来一张带着香火味的小笺，上面写着“[tempnum]”。"
                    elif my.age > 35 or hdage > 50:
                        $ tempnum =  "无"
                        "未几，祭祀递过来一张带着香火味的小笺，上面写着“[tempnum]”。"
                    else:
                        $ tempnum = 10 - round(my.lucky*0.1) + 10 - round(my.health*0.01) + tempnum2*5
                        $ tempnum = int(tempnum+1)
                        "未几，祭祀递过来一张带着香火味的小笺，上面写着“[tempnum]”。"
                        "（有1/[tempnum]的几率得孕。）"


                    $ timenum = timenum + 2
                    $ AP = AP -2
                    jump 皇宫界面
                "算了":
                    jump 观仙台
        "闲逛":




            "这里有一些特殊剧情，但是还没有做，先加点福缘吧。"
            $ my.lucky = my.lucky + renpy.random.randint(30, 50)*0.1
            $ lucky = renpy.random.randint(0, 100)
            if lucky == 0:
                $ kufang.append(poison04)
                "顺便再送你一个[poison04.name]。"
            elif lucky ==1:
                $ kufang.append(medic04)
                "顺便再送你一个[medic04.name]。"
            elif lucky == 3:
                $ kufang.append(acc08)
                "顺便再送你一个[acc08.name]。"
            elif lucky ==4:
                $ kufang.append(acc12)
                "顺便再送你一个[acc12.name]。"
            else:
                pass


    $ timenum = timenum + 2
    $ AP = AP -2
    jump 皇宫界面





label 望仙殿:
    $ bg("望仙殿")
    show screen notify("望仙殿")
    $ lucky = renpy.random.randint(0, 20)
    if lucky == 0:
        show 莲稚 at chara
        莲稚 "见过[my.cheng]。"
        hide 莲稚
        show 太后 at chara
        太后 "这不是[my.cheng]吗？也是来望仙殿祈福的？"
        我 "臣妾给太后请安。回太后，臣妾今日是来望仙殿祈福的。"
        太后 "（赞许的点点头）好孩子，过来，同哀家一起吧。"
        我 "是，臣妾遵命。"
        $ Taihoulike_Up(my,2)
        hide 太后
        "同太后一起在望仙殿为国运祈福。"
        "感觉心平气和，浑身轻盈。"
        $ mustshiqin = mustshiqin + renpy.random.randint(5, 10)
        $ timenum = timenum + 2
        $ AP = AP -2
        $ ftlcishu = ftlcishu+1
        jump 皇宫界面
    elif lucky == 1:
        $ tempfzlist = []
        python:
            for i in NPC_fz_list:
                if i == my:
                    pass
                elif i.xingge == "娇纵" or i.xingge == "势利":
                    pass
                elif jinzu(i) == True:
                    pass
                else:
                    tempfzlist.append(i)
        if len(tempfzlist)== 0:
            pass
        else:
            $ fz = renpy.random.choice(tempfzlist)
            show fz at chara
            "[fz.hao][fz.weifen] [fz.name]" "这不是[my.cheng]么？"
            if my.level < fz.level:
                "[fz.hao][fz.weifen] [fz.name]" "嫔妾见过[my.cheng]。"
            else:
                我 "[fz.cheng]安。"
            "[fz.hao][fz.weifen] [fz.name]" "没想到[my.cheng]今天也来望仙殿祈福，倒是巧了。"
            $ Feizilike_Up(fz,2)
            if fz.lucky > 0:
                $ fz.lucky = fz.lucky + 2
            else:
                $ fz.lucky = fz.lucky + 0.5
            "闲聊几句，各自前往殿中祈福。"
            hide fz
    else:
        pass



    menu:
        "祈求皇帝龙体安康，国事顺遂":
            "跪于殿中祈福，感觉心平气和，浑身轻盈。"
            $ mustshiqin = mustshiqin + renpy.random.randint(5, 10)
            $ timenum = timenum + 2
            $ AP = AP -2
            $ ftlcishu = ftlcishu+1
            if atan_0 == True:
                $ atan_1 += 1
        "祈求自己身体康健，子嗣兴旺":
            "跪于殿中祈福，感觉心平气和，浑身轻盈。"
            if my.lucky > 0:
                $ my.lucky = my.lucky + 2
            else:
                $ my.lucky = my.lucky + 0.5
            $ ftlcishu = ftlcishu+1
            $ my.health = my.health + 4
            $ timenum = timenum + 2
            $ AP = AP -2
        "离开":
            pass

    if ftlcishu == 6 and zhangsi == False:
        show 掌祀 at chara with dissolve
        "？？？" "……请留步。"
        我 "……你是？"
        "？？？" "在下，奉天楼掌祀匀褚，见过[my.cheng]。"
        我 "（奉天楼掌祀？）"
        掌祀 "[my.cheng]似乎时常前来奉天楼？"
        我 "是，常来奉天楼祈福罢了。"
        掌祀 "（哈哈一笑）[my.cheng]说笑了，在下任职奉天楼已久。又何尝不知，来此处之人有几个是真心祈福的？不过是有求于上天，有求于神明罢了。"
        我 "掌祀大人这是何意？"
        掌祀 "此地人多耳杂，在下不便说得过于分明。若您真的被琐事烦扰，想借上天之力达成心愿，倒不如来观仙台找在下，在下虽非神明，但可借神明之名，替您得偿所愿也说不定呢……"
        我 "得偿所愿……"
        hide 掌祀 with dissolve
        "你还未反应过来，那人的身影却已消失不见。"
        我 "奉天楼掌祀？观仙台？"
        我 "此人究竟是何意？"
        if guanxiantai == False:
            $ guanxiantai = True
            "地图 奉天楼-观仙台 已开放。"
        else:
            pass
    elif ftlcishu >= 10 and atan_0 == False:
        scene 望仙殿 with fade
        $ atan_0 = True
        "祈福完毕，正当要离去，却听得个轻泠女声，若山涧溪流，煞是动听。"
        "女子的声音" "是，那便都备好了。"
        show 阿檀 常
        with dissolve
        "女子" "明个一早送到掌祀大人那里请他过目便是。"
        "女子" "太后娘娘的经文也已经替她备好了，你晚些送到建章宫去。"
        show 阿檀 思
        "女子" "等掌祀大人确认无误，再去圣宸宫跑一趟……"
        "女子" "照掌祀大人的意思……请陛下亲临。"
        show 阿檀 常
        "女子" "剩下的，我会处理妥当的。"
        hide 阿檀
        我 思 "以前怎未见过她……"
        show 我的宫女
        我的宫女 "看模样，应是奉天楼的人。"
        我 "嗯，倒是标致……和其他人不大一样。"
        hide 我的宫女
    elif atan_1 == 5 and atan_2 == False:
        $ atan_2 = True
        show 阿檀 常
        with dissolve
        "女子" "您是……[my.cheng]娘娘吧？"
        我 "（是之前见过的那个女子……）"
        "女子" "（走到你面前，福了福身）奉天楼司祝阿檀见过[my.cheng]。"
        我 "阿檀……"
        阿檀 笑 "请恕阿檀冒昧，近日见您常来，都是为陛下祈福？"
        menu:
            "是":
                pass
        阿檀 "阿檀能感知到您对皇上的一片真心。"
        阿檀 "想必，神灵在上，亦能助您祈愿灵验。"
        menu:
            "那便是我所愿":
                阿檀 笑 "心诚则灵，您和陛下都会天命顺遂，得神明庇佑的。"
            "你又怎知我是真心的？":
                阿檀 常 "难道不是么……"
                阿檀 常 "您为陛下前来祈福，不辞劳苦，亦未声张，不求陛下知道您的用心……"
                阿檀 "若非真心，又是为何？"
        阿檀 "这世间真心难求，有您这样的佳人在侧，本便是陛下之福了。"
        menu:
            "皇上九五之尊，此话叫人难以担待":
                阿檀 笑 "能伴君侧，是福。能得您真心，亦是福。"
                阿檀 "天子为尊，真心为贵，却是天作之合，为何不能担待？"
                我 "（为何总觉得她眼底似有几分艳羡和酸涩……）"
            "又与你何干？":
                阿檀 "是阿檀唐突了……"
                阿檀 "还请[my.cheng]恕罪，阿檀只是对您与陛下的情谊有所感触……"
        show 阿檀 at you
        show 掌祀 at zuo
        掌祀 "阿檀，你今日说得够多了。"
        阿檀 思 "掌祀大人……"
        阿檀 思 "您今日不是……"
        阿檀 思 "您都听见了？"
        掌祀 "饶是胆大妄为如本座，也不敢像你这般在望仙殿里口出诳语。"
        我 "（……）"
        掌祀 "[my.cheng]莫怪，这阿檀……（别有意味地看她一眼）是动了不该动的心思。"
        阿檀 常 "……"
        掌祀 "陛下近来鲜少过问奉天楼的事，你便思而不得了？"
        阿檀 思 "您说这些话，让阿檀困惑了。"
        掌祀 "你的惑，不该本座来解。你自己心里拎清了，别叫[my.cheng]瞧了笑话。"
        掌祀 "不……若改日换了别人，便不仅仅落得个笑话。"
        阿檀 闭眼 "……"
        掌祀 "阿檀，若心乱了，便回屋抄经静思。"
        阿檀 常 "是。"
        hide 阿檀
        hide 掌祀
        show 掌祀
        我 "掌祀大人方才的话是什么意思？"
        我 "那阿檀……"
        掌祀 "阿檀犯了大忌，动了痴心。"
        menu:
            "大忌？":
                掌祀 "修行之人，唯有弃了凡俗的心性才可有大成。"
                掌祀 "本便是福浅命薄之人，托了这奉天楼的风水才得了几分福泽，却贪心起帝王心来了……"
                掌祀 "您说，这是不是犯了大忌？"
                掌祀 "她若再这么下去，怕是自寻了绝路。"
            "痴心？":
                掌祀 "也不知是着了什么疯魔。"
                掌祀 "若她与奉天楼或是旁的人的人生了情，要是懂得孝敬，本座倒也可以放她还俗。"
                掌祀 "偏偏对皇上动了心……真是叫人气得想处置了她。"
        我 "她……"
        掌祀 "唉……本是个与神明有缘的，偏生出了这遭。"
        掌祀 "若迷途知返，断了这心思，本座还能护得了她。"
        我 "可若不然呢？"
        掌祀 "神明座下，也容不下她了。"
        hide 掌祀
    elif atan_1 == 6 and atan_3 == False:
        $ atan_3 = True
        "路过的司祝" "哎，这几日都没瞧见阿檀，也不知道她怎么样了。"
        "另一位司祝" "听送饭的那丫头说，阿檀怕是不妙了……"
        我 "（他们在说……阿檀？）"
        我 "（阿檀发生什么事了？）"
        "路过的司祝" "那掌祀大人那边……"
        "另一位司祝" "咳咳！"
        show 掌祀
        掌祀 "见过[my.cheng]，今日又是来祈福的？"
        menu:
            "阿檀怎么了？":
                $ atan_4 = True
                掌祀 "（笑）[my.cheng]还真是关心阿檀呢。阿檀知道定会心存感激的。"
                我 "她现下到底如何了？"
                掌祀 "（突然叹了口气。）"
                我 "难道阿檀……"
                掌祀 "没什么，只是看见您对她如此忧心，倒真的有些感觉……阿檀或许还有救呢。"
                掌祀 "阿檀的状况实在不能叫人宽心。"
                掌祀 "她从小体弱，身患重病，求医难治，前任掌祀在外历练之时受其父母所托，养在身边，才逐渐好了起来，虽说不上康健，倒也至少不再像个药罐子一般。"
                掌祀 "谁知道染了心病，更是无人可治。"
                我 "心病……倒也并非无人可治。"
                掌祀 "但本座也帮不了她了，兴许她同这俗世本就没多少缘分。唉，眼下只能靠她自个儿，或者，兴许还有旁人同她有缘，就像昔日师尊那般将她留在了这凡世之中……"
            "告辞离开":
                我 "（还是不要多管闲事得好……）"
                我 "嗯，祈福已毕，本宫先回去了。"
                掌祀 "恭送娘娘。"
        hide 掌祀
    elif atan_1 == 10 and atan_4 == True and atan_5 == False:
        $ atan_5 = True
        我 "祈福完毕，正欲离开，却看到一个熟悉的身影。"
        menu:
            "阿檀！":
                pass
        show 阿檀
        阿檀 常 "……"
        "显然，她也看到了你。亦或是早就一直在看着你。但四目相对时，她的眼神之中却带着迟疑和退怯。"
        我 "阿檀……"
        阿檀 思 "今日奉天楼还有要事未筹备妥当，请恕阿檀失陪了。"
        我 "嗯……"
        我 "（匀褚应该让阿檀养好身子才是……）"
        我 "（？！）"
        hide 阿檀
        我 "阿檀！"
        "望仙殿司祝" "阿檀？"
        "望仙殿司祝" "阿檀她晕倒了？！"
        "正在众人察觉却皆是无措之时，一道身影突然出现在阿檀的身旁。"
        show 掌祀 at zuo
        with dissolve
        show 阿檀 闭眼 at you
        with dissolve
        掌祀 "真是受够了……"
        我 "匀褚，你快看看阿檀怎么了。"
        我 "好端端的，突然便晕倒了……"
        掌祀 "……"
        掌祀 "（施法中）"
        阿檀 思 "……"
        阿檀 "（！）"
        阿檀 常 "掌祀大人……"
        掌祀 "本座允许你外出走动，你就是这么报答本座的？"
        掌祀 "你这几日天未亮便来望仙殿祈福，深夜才回房，真以为本座不知道？"
        掌祀 "阿檀，你觉得你的身子还撑得了多久？"
        阿檀 "……"
        阿檀 哭 "阿檀怕以后再没有机会了……"
        掌祀 "倒是很有觉悟，但你也别死在这望仙殿了，你倒是潇洒解脱了，你让本座怎么跟这头上三尺的神仙交待？"
        阿檀 "是阿檀的错……"
        掌祀 "阿檀，一个人能决定自己命运的机会可不多。现在这个机会就摆在你自己面前，是去是留，你自己好好想想。"
        掌祀 "你要真不想活了，记得跟本座知会一声，本座替你准备一场法事，免得别人说本座亏待了你。"
        阿檀 闭眼 "……是。"
        掌祀 "（递了个眼神，身后两个小侍走上前来，将阿檀扶了出去。）"
        hide 阿檀
        hide 掌祀
        我 "（阿檀的状况着实不太妙，这样下去，恐怕是真的时日不多了……）"
        menu:
            "多来陪陪她，兴许能让她看开些":
                我 "这些日子多来奉天楼看看她吧。"
                $ atan_time = 1
                $ atan_end_2 = 1
            "阿檀痴恋至此，或许后宫才是最好的归宿":
                $ atan_time = 1
                $ atan_end_1 = 1
                我 "阿檀，若能以嫔妃的身份陪伴在皇上身边，会让你的余生幸福么……"
                if my.level == 0:
                    我 笑 "本宫身为六宫之主，就帮你这一把罢。"
                    $ atan_help.append(0)
                elif weifen_list[0][5] == 0:
                    我 "如今后宫无主，此事还得请示皇上或太后，再不济，让匀褚出面……"
                else:
                    我 "不过此事还得请示皇后或皇上、太后，再不济，让匀褚出面……"
    elif taihouxinge == "宽和" and my.taihoulike>80 and taihou3 == False:
        $ taihou3 = True
        "你才把香插上香炉，便闻身后有声，连忙回首看去，竟是太后娘娘。"
        show 太后 at chara with dissolve
        我 "臣妾参见太后娘娘。"
        太后 "[aicheng]也来祈福？这儿平日里，都不见着几个妃嫔。"
        太后 "[aicheng]是来祈福什么的？"
        menu:
            "祈福神明保佑国泰民安":
                pass
            "祈福神明保佑皇嗣安康":
                pass
            "祈福神明保佑太后容华":
                太后 "净拿哀家打趣，真是胡扯，你这调皮的小胚子。"
                太后 "（说罢还用手轻掐了一下你的脸。）"
                太后 "罚你随哀家一同祈福。"
                我 "（偷笑）臣妾领罚。"
                hide 太后
                $ Taihoulike_Up(my,2)
                jump 皇宫界面
        太后 "想不到[aicheng]有这份心，哀家回头呀，定要跟皇上提上几句，别的妃嫔可得多些学着你才是。"
        python:
            global templist
            templist = []
            for i in NPC_fz_list:
                if i == my:
                    pass
                elif i.state != "寻常":
                    pass
                elif i.taihoulike >50:
                    pass
                elif i.xingge == "娇纵":
                    templist.append(i)
                else:
                    pass
        if len(templist) == 0:
            太后 "过来同哀家一起祈福吧。"
            我 "臣妾遵命。"
            $ Taihoulike_Up(my,2)
        else:
            $ fz = renpy.random.choice(templist)
            太后 "说来方才路上远远的就听见[fz.cheng]在吵吵嚷嚷的，似乎是在训斥宫女，真是闹得人心烦。"
            menu:
                "安慰太后几句":
                    太后 "罢了罢了，还不如祈福，以平心乱，[aicheng]随哀家一同罢。"
                    我 "臣妾遵命。"
                    $ fz.taihoulike = fz.taihoulike - 3
                    $ Taihoulike_Up(my,1)
                "说些趣事惹太后乐呵":
                    太后 "你呀你，总是那么油嘴滑舌，总能把哀家说得乐呵，来来来，随哀家一同祈福罢。"
                    $ fz.taihoulike = fz.taihoulike - 2
                    $ Taihoulike_Up(my,2)
            我 "臣妾遵命。"
        hide 太后
        "同太后一起祈福。"
        jump 皇宫界面
    else:

        pass
    jump 皇宫界面


label 奉天楼_late:
    "深夜望仙殿闭门打扫，并不开放。"
    jump 皇宫界面









label 御花园:
    $ bgm("YHY")
    $ bg("御花园")
    with dissolve
    show screen notify("御花园")
    show screen Normalbuttons
    python:
        Npcmaymeet = []
        Npcmeet = []
        if timenum == 1 or timenum >=4:
            lucky = 1
        else:
            lucky = renpy.random.randint(0, 3)
        for i in NPC_fz_list:
            if i == my:
                pass
            elif i == shiqinfz:
                pass
            elif jinzu(i) == True:
                pass
            elif tags_yali[2] in i.tags:
                pass
            elif i.state == "寻常":
                Npcmaymeet.append(i)
            else:
                pass
        if timenum ==1 or timenum ==5 :
            tempnum = renpy.random.randint(0, 2)
        elif month == 1 or  month == 11 or month == 12:
            tempnum = renpy.random.randint(0, 3)
        else:
            tempnum = renpy.random.randint(0, 6)
        if tempnum >  len(Npcmaymeet):
            tempnum = len(Npcmaymeet)
        else:
            pass
        Npcmeet = renpy.random.sample(Npcmaymeet,tempnum)
        lucky = renpy.random.randint(0, 4)
    menu:
        "千鲤池":
            $ my.meili =my.meili + 1
            $ bg("千鲤池")
            python:
                renpy.call("景地事件",place = "千鲤池",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "千鲤池",from_current=False)
            else:
                pass
            show screen notify("千鲤池")
            call screen meetNPC("千鲤池")
        "莲韵池":
            $ my.meili =my.meili + 1
            $ bg("莲韵池")
            python:
                renpy.call("景地事件",place = "莲韵池",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "莲韵池",from_current=False)
            else:
                pass
            show screen notify("莲韵池")
            call screen meetNPC("莲韵池")
        "玉烟亭":
            $ my.meili =my.meili + 1
            $ bg("玉烟亭")
            python:
                renpy.call("景地事件",place = "玉烟亭",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "玉烟亭",from_current=False)
            else:
                pass
            show screen notify("玉烟亭")
            call screen meetNPC("玉烟亭")
        "花间阁":
            $ my.meili =my.meili + 1
            $ bg("花间阁")
            python:
                renpy.call("景地事件",place = "花间阁",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "花间阁",from_current=False)
            else:
                pass
            show screen notify("花间阁")
            call screen meetNPC("花间阁")
        "闲逛":
            $ my.meili =my.meili + 1
            python:
                renpy.call("景地事件",place = "御花园",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "御花园",from_current=False)
            else:
                pass
            call 后宫游玩 ("御花园") from _call_后宫游玩

label 上林苑:
    $ bgm("SLY")
    $ bg("上林苑")
    with dissolve
    show screen notify("上林苑")
    show screen Normalbuttons
    python:
        Npcmaymeet = []
        Npcmeet = []
        if timenum == 1 or timenum >=4:
            lucky = 1
        else:
            lucky = renpy.random.randint(0, 4)
        for i in NPC_fz_list:
            if i == my:
                pass
            elif i == shiqinfz:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "寻常":
                Npcmaymeet.append(i)
            else:
                pass
        if timenum ==1 or timenum ==5 :
            tempnum = renpy.random.randint(0, 2)
        elif month == 1 or  month == 11 or month == 12:
            tempnum = renpy.random.randint(0,5)
        else:
            tempnum = renpy.random.randint(0,3)
        if tempnum >  len(Npcmaymeet):
            tempnum = len(Npcmaymeet)
        else:
            pass
        Npcmeet = renpy.random.sample(Npcmaymeet,tempnum)
        lucky = renpy.random.randint(0, 4)
    menu:
        "紫竹林":
            $ my.health = my.health +1
            $ bg("紫竹林")
            python:
                renpy.call("景地事件",place = "紫竹林",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "紫竹林",from_current=False)
            else:
                pass
            show screen notify("紫竹林")
            call screen meetNPC("紫竹林")
        "疏影园":
            $ my.health = my.health +1
            $ bg("疏影园")
            python:
                renpy.call("景地事件",place = "疏影园",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "疏影园",from_current=False)
            else:
                pass
            show screen notify("疏影园")
            call screen meetNPC("疏影园")
        "清羽台":
            $ my.health = my.health +1
            $ bg("清羽台")
            python:
                renpy.call("景地事件",place = "清羽台",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "清羽台",from_current=False)
            else:
                pass
            show screen notify("清羽台")
            call screen meetNPC("清羽台")
        "闲逛":
            python:
                renpy.call("景地事件",place = "上林苑",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "上林苑",from_current=False)
            else:
                pass
            $ my.health = my.health +1
            call 后宫游玩 ("上林苑") from _call_后宫游玩_1

label 太液池:
    $ bgm("TYC")
    $ bg("太液池")
    with dissolve
    show screen notify("太液池")
    show screen Normalbuttons
    python:
        Npcmaymeet = []
        Npcmeet = []

        if timenum == 1 or timenum >=4:
            lucky = 1
        else:
            lucky = renpy.random.randint(0, 5)
        for i in NPC_fz_list:
            if i == my:
                pass
            elif i == shiqinfz:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "寻常":
                Npcmaymeet.append(i)
            else:
                pass
        if timenum ==1 or timenum ==5 :
            tempnum = renpy.random.randint(0,1)
        else:
            tempnum = renpy.random.randint(0,3)
        if tempnum >  len(Npcmaymeet):
            tempnum = len(Npcmaymeet)
        else:
            pass
        Npcmeet = renpy.random.sample(Npcmaymeet,tempnum)
        lucky = renpy.random.randint(0, 4)
    menu:
        "流云榭":
            $ my.qizhi =my.qizhi +1
            $ bg("流云榭")
            python:
                renpy.call("景地事件",place = "流云榭",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "流云榭",from_current=False)
            else:
                pass
            show screen notify("流云榭")
            call screen meetNPC("流云榭")
        "涵虚泽":
            $ my.qizhi =my.qizhi +1
            $ bg("涵虚泽")
            python:
                renpy.call("景地事件",place = "涵虚泽",from_current=False)
            if lucky == 0:
                python:
                    renpy.call("妃子主动互动",place = "涵虚泽",from_current=False)
            else:
                pass
            show screen notify("涵虚泽")
            call screen meetNPC("涵虚泽")
        "蓬莱岛":
            $ my.qizhi =my.qizhi +1
            $ bg("蓬莱岛")
            python:
                renpy.call("景地事件",place = "蓬莱岛",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "蓬莱岛",from_current=False)
            else:
                pass
            show screen notify("蓬莱岛")
            call screen meetNPC("蓬莱岛")
        "萋霜亭":
            $ my.qizhi =my.qizhi +1
            $ bg("萋霜亭")
            python:
                renpy.call("景地事件",place = "萋霜亭",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "萋霜亭",from_current=False)
            else:
                pass
            show screen notify("萋霜亭")
            call screen meetNPC("萋霜亭")
        "闲逛":
            python:
                renpy.call("景地事件",place = "太液池",from_current=False)
            if lucky == 4:
                python:
                    renpy.call("妃子主动互动",place = "太液池",from_current=False)
            else:
                pass
            $ my.qizhi =my.qizhi +1
            call 后宫游玩 ("太液池") from _call_后宫游玩_2




label 后宫游玩(place):
    python:
        renpy.call("闲逛事件",place = place,from_current=False)

    hide screen Normalbuttons


    if place == "御花园":
        "御花园的美景可谓是宫中独有，堪称天下一绝。"
    elif place == "千鲤池":
        我 "看着池里无拘无束地游动着的鱼儿们……"
        我 "感觉内心也多了一分自由的喜悦。"
    elif place == "莲韵池"  and month > 4 and month < 8:
        我 "未花叶自香，既花香更别。雨过吹细风，独立池上月。"
        我 "此处景致实在是美。"
    elif place == "莲韵池":
        我 "莲叶凋谢，失去了盛夏的光景，此处景致已经了无趣味。"
    elif place == "玉烟亭":
        我 "当在御花园中散步疲惫后，便可至玉烟亭中休憩。"
        我 "不同于御花园中各种繁华的景色，清凉静雅的玉烟亭也是别有独特之处。"
    elif place == "花间阁":
        我 "天下花卉之珍奇者，皆在御花园。御花园花卉之珍奇者，皆在花间阁。"
    elif place == "上林苑":
        我 "不同于百花争艳的御花园，上林苑环境清幽。更能让人得到内心的一片宁静。"
    elif place == "紫竹林":
        我 "宫中的紫竹不仅美观，对人的身心也有很大的疗效。"
    elif place == "殊影园":
        我 "疏影横斜水清浅，暗香浮动月黄昏。"
        我 "这便是殊影园名字的由来。"
    elif place == "殊影园" and month > 10:
        我 "不与百花争春，冬日凌寒自妍。"
        我 "此处的梅花真的好美啊。"
    elif place == "清羽台":
        我 "清羽台地处偏僻，然而景色却十分宏伟。"
        我 "设计此地的人真是别具匠心。"

    elif place == "太液池":
        我 "太液池是宫中第一大湖泊。"
        我 "一望无际，水流清澈，景致宏伟大气。让人陶醉其中。"
    elif place == "涵虚泽":
        我 "远处的河水和天空渐渐融为了一体。这是怎样神奇的景色啊……"
    elif place == "蓬莱岛":
        我 "蓬莱岛是太祖登基后按照梦中的蓬莱仙洲建造的。的确宛如仙境一般梦幻飘渺……"
    elif place == "萋霜亭":
        我 "萋霜亭的空气中都弥漫着花的馥郁馨香。"
        我 "然而看着水面漂浮的落花，却让心中又不禁生出几分感伤。"
    else:


        我 "随意闲逛，心情愉快。"
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面


label 偶遇皇上(place):
    $ Npcmeet = sorted(Npcmeet, key=attrgetter("love"),reverse = True)
    if len(Npcmeet) >0  and Npcmeet[0].love > 50:
        $ fz = Npcmeet[0]
        我 "（正欲上前，却被宫人拦下。）"
        show 赵公公 at chara
        赵公公 "[my.cheng]，如今皇上正在陪同[fz.cheng]游玩呢。无关人等，不得打扰。"
        if my.love < Npcmeet[0].love:
            我 "……那本宫便不打扰皇上雅兴了。"
            hide 赵公公
            我 "（黯然离去。）"
            call 后宫游玩 (place=place) from _call_后宫游玩_3
        else:
            "当你同赵公公说话时，一道目光却朝你投来。"
            show 皇帝 at chara
            皇上 "爱妃也在这里。"
            我 "（走上前去）臣妾给皇上请安。"
            hide 皇帝
            show fz at chara
            if my.level < fz.level:
                妃子 "给[my.cheng]娘娘请安。"
            else:
                我 "见过[fz.cheng]。"
            hide fz
            show 皇帝 at chara
            皇上 "今日凑巧，便与朕同游吧。"
            我 "（欣喜）臣妾遵命。"
            hide 皇帝
            show fz at chara
            妃子 "皇上……"
            hide fz
            hide 皇帝
            "三人同游[place]……"

            $ my.love = my.love + 2
            $ fz.love = fz.love+ 2
            $ fz.like =fz.like - 2
            $ mustshiqin = mustshiqin + 30
    else:
        $ Npcmeet = sorted(Npcmeet, key=attrgetter("qingxiang"),reverse = True)
        if len(Npcmeet) >0  and Npcmeet[0].qingxiang > 75:
            $ fz = Npcmeet[0]
            我 "（正准备上前，却被人抢先一步。）"
            show fz at chara
            妃子 "皇上……"
            hide fz
            我 "（是否仍要上前？）"
            menu:
                "上前":
                    我 "臣妾参见皇上。"
                    show fz at chara
                    if my.level < fz.level:
                        妃子 "（看到你似乎楞了一下。）给[my.cheng]娘娘请安。"
                    else:
                        我 "见过[fz.cheng]。"
                    if my.love >= fz.love:
                        show 皇帝 at chara
                        皇上 "[my.cheng]也在？"
                        皇上 "今日凑巧，便与朕同游吧。"
                        我 "（欣喜）臣妾遵命。"
                        hide 皇帝
                        show fz at chara
                        妃子 "皇上……（愤恨不甘地看了你一眼。）"
                        hide fz
                        hide 皇帝
                        "三人同游[place]……"
                        $ my.love = my.love + 2
                        $ fz.love = fz.love+ 2
                        $ fz.like =fz.like - 2
                        $ mustshiqin = mustshiqin + 30
                    else:
                        show 皇帝 at chara
                        皇上 "噢，是[my.cheng]啊。"
                        if fz.xingge == "温婉" or fz.xingge == "圆滑":
                            show fz at chara
                            妃子 "今日倒是凑巧，皇上，就让臣妾和[my.cheng]陪您一同游玩把。"
                            hide fz
                            皇上 "也罢。（揽过[fz.cheng]的肩头）若后宫人人都能有你一半识大体，朕不知道能有多高兴。"
                            show fz at chara
                            妃子 "皇上，您谬赞了。"
                            hide fz
                            hide 皇帝
                            "三人同游[place]……但你总感觉自己的出现有些不合时宜。"
                            $ my.love = my.love + 1
                            $ fz.love = fz.love+ 3
                            $ fz.like =fz.like - 2
                            $ mustshiqin = mustshiqin + 15
                        elif fz.xingge == "清冷" or fz.xingge == "安静":
                            show 皇帝 at chara
                            皇上 "今日凑巧，便与朕同游吧。"
                            皇上 "（看向[fz.cheng]）爱妃不会介意吧？"
                            show fz at chara
                            妃子 "但凭皇上的意思。"
                            hide fz
                            皇上 "也罢。（揽过[fz.cheng]的肩头）若后宫人人都能有你一半识大体，朕不知道能有多高兴。"
                            show fz at chara
                            妃子 "皇上，您谬赞了。"
                            hide fz
                            hide 皇帝
                            "三人同游[place]……但你总感觉自己的出现有些不合时宜。"
                            $ my.love = my.love + 1
                            $ fz.love = fz.love+ 3
                            $ fz.like =fz.like - 2
                            $ mustshiqin = mustshiqin + 15
                        else:
                            hide 皇帝
                            show fz at chara
                            妃子 "真巧，[my.cheng]你也在这里。"
                            妃子 "（揽着[guoxing][emperor]，不再看你）您政务繁忙，难得有空出来走走，就让臣妾陪着您吧。"
                            hide fz
                            show 皇帝 at chara
                            皇上 "（欣然点头）走罢。"
                            hide 皇帝
                            "（二人亲昵的身影很快消失在远方。）"
                            我 "（黯然离开。）"
                            call 后宫游玩 (place=place) from _call_后宫游玩_4
                "离开":

                    我 "（默然离开。）"
                    call 后宫游玩 (place=place) from _call_后宫游玩_5
        else:

            我 "臣妾参见皇上。"
            show 皇帝 at chara
            皇上 "免礼。"
            if hdxingge == "冷漠":
                if my.love > 80:
                    皇上 "（睇了你一眼，哂笑）又找宫人打听了朕的行踪是不是？"
                    我 "臣妾没有……"
                    皇上 "那就真的是与朕心意相通？"
                    皇上 "（抱你入怀）过来，陪朕走走。"
                    我 "是。"
                elif my.love >50:
                    皇上 "（抱你入怀）过来，陪朕走走。"
                    我 "是。"
                else:
                    皇上 "有事么？"
                    menu:
                        "没……没有……":
                            $ my.qingxiang = my.qingxiang - 2
                            我 "臣妾没什么事儿，就是来给您请个安。"
                            皇上 "（皱眉看着你，似乎有些惊疑）给朕请安？那既然已经请过了，就退下吧。"
                            我 "是……"
                            皇上 "站住。"
                            皇上 "你还真走了？"
                            我 "不是皇上吩咐了……"
                            皇上 "（无奈地朝着你招手）过来。"
                            我 "啊？臣、臣妾是不是做错了什么……"
                            皇上 "来都来了，陪朕走走。"
                            我 "是……"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ mustshiqin = 100
                        "臣妾想陪皇上走走":
                            $ my.qingxiang = my.qingxiang + 2
                            皇上 "（迟疑片刻）想陪朕走走？那就安安静静地跟着朕，别扰了朕清净。"
                            我 "是……"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ mustshiqin = mustshiqin + 20
                            $ my.love = my.love + 1
            elif hdxingge == "腹黑":
                if my.love > 50:
                    皇上 "过来，陪朕走走。"
                    我 "（欣喜）是……"
                    $ my.love = my.love + 1
                else:
                    皇上 "原来是[my.cheng]，何事？"
                    menu:
                        "没……没有……":
                            $ my.qingxiang = my.qingxiang - 2
                            我 "臣妾没什么事儿，就是来给您请个安。"
                            皇上 "（温柔一笑）[my.cheng]有心了，既然安已经请过，那边退下吧。"
                            我 "是……"
                            皇上 "（轻笑）行了，朕又不是小孩子，真以为朕不知道你想做什么？"
                            皇上 "过来，陪朕走走。"
                            我 "（欣喜）臣妾遵命。"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ my.love = my.love + 1
                        "臣妾想陪皇上走走":
                            $ my.qingxiang = my.qingxiang + 2
                            皇上 "（轻轻点了点头）那边同朕散会儿步吧。"
                            我 "是……"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ my.love = my.love + 1
            elif hdxingge == "温柔":
                if my.love > 50:
                    皇上 "没想到在这儿碰到爱妃。"
                    我 "臣妾与皇上心意相通……"
                    皇上 "（抱你入怀）过来，陪朕走走。"
                    我 "是。"
                else:
                    皇上 "原来是[my.cheng]，何事？"
                    menu:
                        "没……没有……":
                            $ my.qingxiang = my.qingxiang - 2
                            我 "臣妾没什么事儿，就是来给您请个安。"
                            皇上 "（温柔一笑）[my.cheng]有心了，朕今日心境的确比往日安宁一些。"
                            皇上 "陪朕走走吧。"
                            我 "是……"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ my.love = my.love + 1
                            $ mustshiqin = mustshiqin + 20
                        "臣妾想陪皇上走走":
                            $ my.qingxiang = my.qingxiang + 2
                            皇上 "（轻轻点了点头）那边同朕散会儿步吧。"
                            我 "是……"
                            hide 皇上
                            "二人一起在[place]漫步片刻。"
                            $ my.love = my.love + 1
                            $ mustshiqin = mustshiqin + 20
            elif hdxingge == "风流":
                皇上 "陪朕走走。"
                我 "是。"
                hide 皇上
                "二人一起在[place]漫步片刻。"
                $ my.love = my.love + 1
                $ mustshiqin = mustshiqin + 20
            else:
                皇上 "陪朕走走。"
                我 "是。"
                hide 皇上
                "二人一起在[place]漫步片刻。"
                $ my.love = my.love + 1
                $ mustshiqin = mustshiqin + 20
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面








label 偶遇妃子(fz, place):
    hide screen Normalbuttons
    show screen Palacebuttons
    image fz = "Feizi/F[fz.face].webp"
    show fz at chara
    if my in fz.foes:
        "[fz.hao][fz.weifen][fz.name]假装没有看到你，转头就走……"
        hide fz
        我 "（独自游玩，并不尽兴。）"
        $ timenum = timenum +1
        $ AP = AP -1
        jump 皇宫界面
    elif fz.xingge == "" and fz.like >= 50:
        if place in hejing:
            $ renpy.call("偶遇交好妃子_河景",fz = fz,tempgn = tempgn,from_current=False)
            $ Feizilike_Up(fz,1)
            $ fz.yali -= 5
            $ my.yali -= 5
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        elif place in yuanlin:
            $ renpy.call("偶遇交好妃子_园林",fz = fz,tempgn = tempgn,from_current=False)
            $ Feizilike_Up(fz,1)
            $ fz.yali -= 5
            $ my.yali -= 5
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        else:
            pass

    elif my in fz.friends:
        "[fz.hao][fz.weifen] [fz.name]" "(远远地看到了你，笑着走上前来。)"
    else:
        pass
    if my.level >= fz.level:
        "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，真是巧呢。"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "见过[my.cheng]。"

    if fz.xingge1 == False:
        if fz.xinji < my.xinji:
            "你发现[fz.cheng]似乎是个[fz.xingge]的人。"
            $ fz.xingge1 = True
        else:
            $ lucky = (fz.xinji - my.xinji)/100
            $ lucky = round(lucky) + 1
            $ lucky = renpy.random.randint(0, lucky)
            if lucky == 0:
                "你发现[fz.cheng]似乎是个[fz.xingge]的人。"
                $ fz.xingge1 = True
            else:
                pass

    if [my,"怀孕"] in gongxi:
        if fz.like > 0 and fz.xingge!= "娇纵" and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "听说[my.cheng]身怀龙嗣，这可是件大喜事啊！{p}嫔妾先恭喜[my.cheng]了，预祝您能平安生下皇嗣。"
        elif fz.like > 0 and fz.xingge!= "娇纵" and my.level > fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "听说[my.cheng]身怀龙嗣，这可是件大喜事啊！{p}本宫先恭喜[my.cheng]了，预祝你能平安生下皇嗣。"
        elif fz.like < 20 and fz.xingge== "娇纵":
            "[fz.hao][fz.weifen] [fz.name]" "哎，这不是[my.cheng]吗？如今怀着皇嗣，怎还出来走动，可不该安心待在宫里养胎？"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "哎，这不是[my.cheng]吗？如今怀着皇嗣，怎还出来走动，可不该安心待在宫里养胎？"
    elif [my,"晋位"] in gongxi:
        if fz.like > 0 and fz.xingge!= "娇纵" and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "前日里皇上晋了您的位份，嫔妾在这里恭贺[my.cheng]了。"
        elif fz.like > 0 and fz.xingge!= "娇纵" and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "前日里皇上晋了您的位份，这可是件喜事啊！"
        elif fz.like < 20 and fz.xingge== "娇纵":
            "[fz.hao][fz.weifen] [fz.name]" "前日里皇上才晋了[my.cheng]的位份呐……可真叫人羡慕得紧。（看着你，眼底有几分嫉恨。）"
        else:
            pass

    elif [my,"生产"] in gongxi:
        if fz.like > 0 and fz.xingge!= "娇纵" and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "虽说迟了些，不过嫔妾还是要恭贺[my.cheng]喜得皇嗣。"
        elif fz.like > 0 and fz.xingge!= "娇纵" and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "虽说迟了些，不过本宫还是要恭贺[my.cheng]喜得皇嗣。你是个有福气的。"
        elif fz.like < 20 and fz.xingge== "娇纵":
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]诞下皇嗣，如今是皇上眼前的红人儿，这福气可真叫人羡慕得紧。（看着你，眼底有几分嫉恨。）"
        else:
            pass

    elif [my,"美言"] in ganxie:
        $ Feizilike_Up(fz,2)
        if my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "嫔妾听说您之前在皇上面前替嫔妾美言了几句？"
            "[fz.hao][fz.weifen] [fz.name]" "您的大恩大德，嫔妾没齿难忘啊！"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "本宫听说您之前在皇上面前替本宫美言了几句？"
            "[fz.hao][fz.weifen] [fz.name]" "你的心思，本宫都会记着。"

    elif [my,"提拔"] in ganxie:
        $ Feizilike_Up(fz,2)
        "[fz.hao][fz.weifen] [fz.name]" "您提拔嫔妾的事情，嫔妾还没来得及感谢您……"
        "[fz.hao][fz.weifen] [fz.name]" "（跪下）嫔妾多谢[my.cheng]。"

    elif [my,"小产"] in xiluo:
        if fz.like >50 and my.level > fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "（幽幽叹了口气）你也是个可怜人儿……才没了孩子，还是好好休养一阵时日吧。"
        elif fz.like >50 and my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "（面色忧虑，又怕提及你的伤心事）[my.cheng]……您，您今天身子好些了？"
        elif fz.like < 0 or fz.xingge == "娇纵" or fz.xingge == "势利":
            "[fz.hao][fz.weifen] [fz.name]" "哎，本以为[my.cheng]会消沉好一阵子呢。如今看来似乎好得很呐。"
            "[fz.hao][fz.weifen] [fz.name]" "有些人呐，天生便是没福气的，也强求不得。是吧？"
        else:
            pass


    if place == "千鲤池"and fz.qingxiang < 25:
        "[fz.hao][fz.weifen] [fz.name]" "有时候感觉，比起做后宫中的嫔妃，还不如这池子里的鱼儿自在。"
    elif place == "千鲤池"and fz.qingxiang > 75:
        "[fz.hao][fz.weifen] [fz.name]" "（叫宫人取了鱼食来，看池中锦鲤们争相抢食）。"
        "[fz.hao][fz.weifen] [fz.name]" "鱼尚且弱肉强食，又何止是人呢？"
    elif place == "千鲤池":
        "[fz.hao][fz.weifen] [fz.name]" "千鲤池的景色随不如那些花花草草优美，但总能让人感觉格外充满生机。"
    elif place == "莲韵池"and fz.love < 20:
        "[fz.hao][fz.weifen] [fz.name]" "夏天过了，莲花盛开，这里总是热闹纷纷。而时节一过，便人迹凋零。"
        "[fz.hao][fz.weifen] [fz.name]" "呵，帝王的恩宠，不也是如此么？"
    elif place == "莲韵池"and fz.xinji > 700:
        "[fz.hao][fz.weifen] [fz.name]" "莲出淤泥而不染，濯清涟而不妖……"
        "[fz.hao][fz.weifen] [fz.name]" "然而在这世上又有多少人能做到呢？"
    elif place == "莲韵池"and fz.xingge == "活泼":
        "[fz.hao][fz.weifen] [fz.name]" "嘻嘻，荷花虽然好看，不过……还是莲藕更好吃！"
    elif place == "莲韵池":
        "[fz.hao][fz.weifen] [fz.name]" "听说前朝有一位宠妃，可在莲韵池凌波起舞，可后来被陷害失宠，便投池自尽了。"
        "[fz.hao][fz.weifen] [fz.name]" "倒真是叫人唏嘘啊。"
        我 "（不寒而栗。）"
    elif place == "玉烟亭":
        "[fz.hao][fz.weifen] [fz.name]" "据说玉烟亭是先帝为宠妃建造的。如今这儿却是落寞寂寥了。"
    elif place == "花间阁" and fz.qingxiang > 80 and fz.level > 0:
        "[fz.hao][fz.weifen] [fz.name]" "都说只有牡丹堪称国色，花间阁里的这些奇珍花卉却都不逊色。"
    elif place == "花间阁" and fz.xingge == "清冷":
        "[fz.hao][fz.weifen] [fz.name]" "这些花儿美则美矣，见多了也便觉得是庸脂俗粉，馥浓厌人。"
        "[fz.hao][fz.weifen] [fz.name]" "比不得冬日疏影园中的梅花。"
    elif place == "花间阁" and fz.xingge == "势利":
        "[fz.hao][fz.weifen] [fz.name]" "这些花儿开得再艳，也只有牡丹才能堪称国色，不是吗？"
    elif place == "花间阁" and fz.xingge == "温婉":
        "[fz.hao][fz.weifen] [fz.name]" "一枝梨花压海棠。如今见了此景，才知道名不虚传。"
    elif place == "花间阁" and fz.xingge == "圆滑":
        "[fz.hao][fz.weifen] [fz.name]" "各花各入眼，花间阁里群芳争艳，真是难分高低呢。"
    elif place == "花间阁" and fz.xingge == "安静":
        "[fz.hao][fz.weifen] [fz.name]" "花间阁的花香太过浓郁，竟叫人感觉有些心浮气躁……"
    elif place == "花间阁" and fz.xingge == "活泼":
        "[fz.hao][fz.weifen] [fz.name]" "嘻嘻，改天趁这儿没人，我要偷偷折几支回去插在花瓶里……"
        "[fz.hao][fz.weifen] [fz.name]" "咦咦……咳咳，[my.cheng]你可什么都没听到。"
    elif place == "花间阁" and fz.xingge == "娇纵":
        "[fz.hao][fz.weifen] [fz.name]" "看来看去，还是蔷薇花最明艳动人了。"
        "[fz.hao][fz.weifen] [fz.name]" "小时候，总有人将我的美貌同蔷薇相比呢。"
    elif place == "御花园":
        "[fz.hao][fz.weifen] [fz.name]" "御花园的景致真是白看不腻。"
    elif place == "紫竹林" or place == "疏影园" or place == "上林苑"  or place == "清羽台":
        "[fz.hao][fz.weifen] [fz.name]" "此处比御花园幽静许多。"
        "[fz.hao][fz.weifen] [fz.name]" "心情烦闷的时候来散散心，就叫人心情舒缓不少。"
    elif place == "太液池" or place == "流云榭" or place == "涵虚泽"  or place == "蓬莱岛" or place == "萋霜亭":
        "[fz.hao][fz.weifen] [fz.name]" "太液池的一望无际，反而让人的心情变得更加封闭了。"
    else:
        pass

    if fz.xinji1 == False:
        if fz.xinji < my.xinji and fz.xinji > 700:
            "看似随意的闲谈中，你却察觉到[fz.cheng]的城府深不可测。"
            $ fz.xinji1 = True
        elif fz.xinji < my.xinji and fz.xinji > 400:
            "闲谈几句，你便察觉到[fz.cheng]的心机可见一斑。"
            $ fz.xinji1 = True
        elif fz.xinji < my.xinji:
            "看似随意的闲谈中，你察觉到[fz.cheng]似乎无甚心机。"
            $ fz.xinji1 = True
        else:
            $ lucky = (fz.xinji - my.xinji)/100
            $ lucky = round(lucky) + 1
            $ lucky = renpy.random.randint(0, lucky)
            if lucky == 0:
                "你对[fz.cheng]的心机有所察觉。"
                $ fz.xinji1 = True
            else:
                pass
    else:
        pass

    hide fz
    我 "（随意聊了几句，便各自离去了。）"
    $ Feizilike_Up(fz,renpy.random.randint(3, 10)*0.2)
    $ fz.meet = fz.meet + 1

    if my.xinji > 900:
        $ fz.xinji = fz.xinji + 2
    elif my.xinji > 700:
        $ fz.xinji = fz.xinji + 1.5
    elif my.xinji > 400:
        $ fz.xinji = fz.xinji + 1
    elif my.xinji > 200:
        $ fz.xinji = fz.xinji + 0.5
    else:
        pass

    if fz.xinji > 900:
        $ my.xinji = my.xinji + 2
    elif fz.xinji > 700:
        $ my.xinji = my.xinji + 1.5
    elif fz.xinji > 400:
        $ my.xinji = my.xinji + 1
    elif fz.xinji > 200:
        $ my.xinji = my.xinji + 0.5
    else:
        pass


    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面

label 偶遇交好妃子_河景(fz):
    if fz.xingge == "活泼":
        if fz.level <= my.level:
            python:
                templist = []
                for i in fz.friends:
                    if i == my:
                        pass
                    else:
                        templist.append(i)
            if len(templist) == 0:
                pass
            else:
                $ tempfz = renpy.random.choice(templist)
                妃子 "是[aicheng]呀，瞧这可是[tempfz.cheng]前些日子赠我的，你瞧这钗子好看吗？我倒是觉着手艺挺好的。"
                我 "您戴着的确好看，特别那光撒过时，波光粼粼的。"
                妃子 "真的？[aicheng]可真有眼光～"
                我 "怎有，这眼光定是不如你的。"
                妃子 "好啦，莫要一同打趣啦，走，随我一同去划船。"
        else:
            妃子 "见过[my.cheng]姐姐。"
            妃子 "姐姐您瞧，这钗子怎么样？好看吗？"
            "一眼便瞧见其头上那未见过的发钗，那钗子着实挺好看的，设计独到却又简单不繁复。"
            我 "挺好看的，挺适合你的。"
            妃子 "真的吗？[my.cheng]可喜欢这钗子？改日得了个就也给[my.cheng]送个。"
            妃子 "[my.cheng]姐姐可要陪嫔妾一同去蓬莱岛划船？"







label 偶遇交好妃子_园林(fz):
    if fz.xingge == "活泼":
        if fz.level <= my.level:
            $ lucky =renpy.random.randint(0, 1)
            if lucky == 0:
                妃子 "[aicheng]快来！可要一同吃些？"
                "只见亭中案上有不少吃食，还有一壶热茶，你缓缓坐其身旁，有说有笑。"
                妃子 "幸好[aicheng]来了，不然我一个人就这么坐着，怪无趣的。"
                我 "这不正巧，被嫔妾碰上了这等好事。"
                妃子 "来来来吃多些，莫要跟我客气喏。"
            elif lucky == 1:
                "[fz.cheng]正不知在花坛中捣鼓什么，你缓缓走近刻意掩盖住了脚步声，还示意一旁的宫女们莫要吭声。"
                我 "这是在做什么呀？"
                "只见她被你吓了一跳，手里的东西都掉了 你仔细一看拿东西，竟是一竹藤编制的小箩。"
                "妃子：呀！[aicheng]？你可是要把我吓坏喏！"
                我 "看有人在这鬼鬼祟祟的，嫔妾便想吓唬吓唬，没想到却吓着了[fz.ming]了，倒是给赔个不是才是。"
                妃子 "好啦好啦，你瞧眼便知。"
                "看去，只见其手中正揪着一蚯蚓，而其身旁的宫女手里头，也有些泥泞，竟是帮着抓蚯蚓的。"
                妃子 "怕吗？我跟你讲，千鲤池里头的鱼儿可喜欢这鱼饵了，钓了就送去御膳房，给点银两加个菜，可香了。就是丫头们不够经验，我得亲自来才行。"
            else:
                pass
        else:
            $ lucky =renpy.random.randint(0, 1)
            if lucky == 0:
                "行至一亭边，只见亭中案上有不少吃食，还有一壶热茶，而[fz.cheng]嘴里正被塞得满满的，手里还有拿着的。抬首见着你，便连忙把口中的嚼了嚼咽下。"
                妃子 "唔.....见过[my.cheng]，[my.cheng]可要一同吃吃？"
                我 "若是妹妹邀请的话，自然一同。"
                妃子 "好呀，嫔妾一人在这可无聊了，[my.cheng]一同的话，可就有趣不少了～"
                妃子 "来来来吃多些，莫要跟嫔妾客气喏，虽然[my.cheng]吃得比嫔妾这儿丰盛，但美味面前皆平等呀。"
            elif lucky == 1:
                "[fz.cheng]正不知在花坛中捣鼓什么，你缓缓走近刻意掩盖住了脚步声，还示意一旁的宫女们莫要吭声。"
                我 "这是在做什么呀？"
                "只见她被你吓了一跳，手里的东西都掉了。"
                "妃子：呀！见过[my.cheng]？姐姐这般可是要把嫔妾吓坏喏！"
                我 "看有人在这鬼鬼祟祟的，本宫便想吓唬吓唬，没想到却吓着了[fz.ming]了，倒是给赔个不是才是。"
                妃子 "好啦好啦，姐姐瞧眼便知。"
                "看去，只见其手中正揪着一蚯蚓，而其身旁的宫女手里头，也有些泥泞，竟是帮着抓蚯蚓的。"
                妃子 "怕吗？我跟你讲，千鲤池里头的鱼儿可喜欢这鱼饵了，钓了就送去御膳房，给点银两加个菜，可香了。就是丫头们不够经验，我得亲自来才行。"
            else:
                pass






label 宫门:
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
    "大门紧闭着，由御林军严密把守，小门偶尔有宫人、侍卫出入。"
    show 我的宫女 at chara
    我的宫女 "娘娘，除非有皇上圣谕允许出宫省亲，后宫的妃嫔一般都是无法出宫的。"
    我的宫女 "我们回去吧。"
    我 "嗯。"
    hide 我的宫女
    jump 皇宫界面


label 没有皇后:
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
    "凤仪宫如今空置，只有几个宫人在打扫。"
    jump 皇宫界面


label 皇帝互动:
    $ bg("圣宸宫内")
    show 皇帝 at chara
    if my.level <=3:
        if xuanxiutime>= 12:
            $ tiyixuanxiu = True
        elif xuanxiutime >= 32:
            $ tiyixuanxiu = False
        elif len(NPC_Kids_list) < 5 and xuanxiutime >= 6:
            $ tiyixuanxiu = True
        elif len(NPC_fz_list) < 10 and xuanxiutime >= 6:
            $ tiyixuanxiu = True
        elif len(NPC_fz_list) < 5 and xuanxiutime >= 3:
            $ tiyixuanxiu = True
        else:
            $ tiyixuanxiu = False
    else:
        $ tiyixuanxiu = False




    if my.love <10:
        皇上 "[my.cheng]……？见朕何事？"
    else:
        皇上 "爱妃见朕何事？"
    menu:
        "奉天楼的阿檀……" if atan_time < 11 and atan_end_1 == 1 and 1 not in atan_help and atan_help_hd == False:
            $ atan_help_hd = True
            if my.love < 50:

                皇上 "（听完你的话，皱眉思考了片刻，神情却十分凝重）那阿檀身在奉天楼，那是侍奉神明之人，高洁神圣，纳入后宫，岂不是要遭天怒？"
                皇上 "此事不要再提。"
            else:
                $ atan_help.append(1)
                皇上 "（听完你的话，皱眉思考了片刻）竟有这样的事……"
                皇上 "怪不得近日朕入夜难寐，总觉得心里有一处，隐隐作痛。"
                皇上 "这莫非是神意暗示朕莫负了那阿檀的一片痴心？"
                我 "臣妾本觉得此事不妥，但眼瞧着她因痴恋陛下而形消骨瘦，若真的就此没了性命……对陛下的福泽也是折损啊。"
                皇上 "嗯，朕立即派人通知掖廷，准备接她入宫的事宜。"
        "皇上为何事烦心？" if chuhuan_time <= 4 and chuhuan_0 == True and chuhuan_1 == False:
            call 楚欢_皇上烦心 (place="圣宸宫内") from _call_楚欢_皇上烦心
        "陪伴":

            if my.love < 10:
                皇上 "[my.cheng]有心了，不过朕如今想安心处理政务，你无事便退下吧。"
                我 "（失落）是，臣妾告退。"
                $ mustshiqin = mustshiqin + renpy.random.randint(8, 16)
                $ timenum = timenum +1
                $ AP = AP -1
                jump 皇宫界面
            elif my.love <50:
                皇上 "（轻轻颔首，并未言语。）"
            elif hdxingge == "腹黑":
                皇上 "好啊，有爱妃陪伴在侧，朕处理起政务来也事半功倍。平日里朕没白疼你。"
            elif hdxingge == "冷漠":
                皇上 "别以为朕不知道你那些小心思。"
                皇上 "想待在朕身边？那就安安分分的。"
            elif hdxingge == "风流":
                皇上 "有爱妃陪伴，朕的劳累似乎都一扫而光的。"
            elif hdxingge == "刚正":
                皇上 "朕现下忙着政务，无法陪伴爱妃。爱妃自便吧。"
            else:
                皇上 "朕最近政务繁忙，疏忽了爱妃，爱妃可是怨朕了？"
            menu:
                "按摩肩膀":
                    我 "（走到他的身后，轻轻揉着他的肩膀。）"
                    我 "皇上政务繁忙，臣妾也分担不了什么。只能尽一己之力，希望皇上不要过于疲惫。"
                "撒娇讨好":
                    我 "皇上……"
                    皇上 "（无奈地看你一眼）朕知道，可朕不能弃国事于不顾。"
                    皇上 "等朕忙完，一定多多陪你。"
                "安静研墨":
                    "你站在龙案一侧，为[guoxing][emperor]。殿内寂静无声，一片岁月静好。"
        "诉苦":
            $ templist = []
            python:
                for i in NPC_fz_list + NPC_fz_feilist:
                    if i == my:
                        pass
                    else:
                        templist.append(i)
            if len(templist) == 0:
                "没有可以诉苦的妃子。"
            else:
                call screen choicefz(templist)

                $ tempfz = fz
                if tempfz.love > my.love:
                    皇上 "（听完你的叙述，眉头蹙起。）朕倒觉得她并非那样的人。恐怕其中有什么误会。"
                    皇上 "朕会派人去提点她两句。你也不必过于介怀。"
                    $ tempfz.love = tempfz.love -2
                    $ my.love=my.love-1
                elif my.love - tempfz.love < 10:
                    皇上 "此事若真是如此，那便是她的不是了。"
                    皇上 "朕改日好好教训她一番。"
                    $ tempfz.love = tempfz.love - 2
                    $ tempfz.exp = tempfz.exp - 5-(beifei-tempfz.level)*2
                elif my.love - tempfz.love < 20:
                    皇上 "此事若真是如此，那便是她的不是了。"
                    皇上 "朕改日好好教训她一番。"
                    $ tempfz.love = tempfz.love - 3
                    $ tempfz.exp = tempfz.exp - 10- (beifei-tempfz.level)*3
                elif my.love - tempfz.love < 30:
                    皇上 "此事若真是如此，那便是她的不是了。"
                    皇上 "朕改日好好教训她一番。"
                    $ tempfz.love = tempfz.love - 4
                    $ tempfz.exp = tempfz.exp - 15 -(beifei-tempfz.level)*4
                else:
                    皇上 "岂有此理！"
                    皇上 "朕定要好好责罚她一番！"
                    $ tempfz.love = tempfz.love - 5
                    $ tempfz.exp = tempfz.exp - 15-(beifei-tempfz.level)*5
        "美言":
            $ templist = []
            python:
                for i in NPC_fz_list + NPC_fz_feilist:
                    if i == my:
                        pass
                    else:
                        templist.append(i)
            if len(templist) == 0:
                "没有可以美言的妃子。"
            else:
                call screen choicefz(templist)
                $ tempfz = fz
                $ tempfz.exp = tempfz.exp + my.love*0.1 + (beifei-my.level)*0.5
                $ tempfz.love = tempfz.love + 2
                "（在你的美言之下，[tempfz.cheng]的宠爱和威望提高了。[tempfz.cheng]对你的好感增加了。）"
        "冷宫里的……" if len(lenggong)>0:
            menu:
                "[lenggong[0].name]" if len(lenggong) > 0:
                    $ tempfz = lenggong[0]
                "[lenggong[1].name]" if len(lenggong) > 1:
                    $ tempfz = lenggong[1]
                "[lenggong[2].name]" if len(lenggong) > 2:
                    $ tempfz = lenggong[2]
                "[lenggong[3].name]" if len(lenggong) > 3:
                    $ tempfz = lenggong[3]
                "[lenggong[4].name]" if len(lenggong) > 4:
                    $ tempfz = lenggong[4]
                "[lenggong[5].name]" if len(lenggong) > 5:
                    $ tempfz = lenggong[5]
            if tempfz.love < 0:
                $ tempfz.love = tempfz.love + my.love*0.1
            else:
                $ tempfz.exp = tempfz.exp + my.love*0.1 + (beifei-my.level)*0.5

            if tempfz.exp >= 0 and tempfz.love >= 0:
                皇上 "（蹙眉沉思片刻，却是温和一笑）朕知道了。"
                $ Feizishengjiang(tempfz)
            else:
                皇上 "[tempfz.xing]氏罪大恶极，此事还需从长计议。"
        "提议选秀" if tiyixuanxiu == True:
            if my.level  == 0 or NPC_fz_list[0] == my:
                $ tempnum = 10
            elif my.level == 1:
                $ tempnum = 6
            elif my.level == 2:
                $ tempnum = 3
            else:
                $ tempnum = 0
            $ tempnum = tempnum + round(my.love*0.2)
            if len(NPC_Kids_list) < 5:
                $ tempnum = tempnum + 5 - len(NPC_Kids_list)
            else:
                pass
            if len(NPC_fz_list) < 10 and xuanxiutime >= 6:
                $ tempnum = tempnum + 10 - len(NPC_fz_list)
            else:
                pass
            if len(NPC_fz_list) < 5 and xuanxiutime >= 3:
                $ tempnum = tempnum + 10
            else:
                pass
            if len(NPC_fz_list) > 20 and tempnum <20:
                皇上 "如今六宫妃嫔众多，无需选秀。"
            elif tempnum < 15:
                皇上 "此事改日再议吧。"
            else:
                $ xuanxiutime = 35
                皇上 "（沉吟片刻）来人——传朕旨意，命掖廷择日进选新秀入宫。"

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面



label 拜访妃子(fz):
    if fz == my:
        jump 寝居界面
    else:
        if fz.level == 0:
            $ bg("凤仪宫外")
            with fade
        else:
            $ bg("妃嫔寝居外")
            with fade

        $ mapname= "皇宫"
        show screen Palacebuttons
        show screen notify(fz.palace)
        image fz = "Feizi/F[fz.face].webp"
        image gn = "Gongnv/GN[gn.face].webp"
        $ gn = fz.Gongnv[0]

        $ temptext = fz.Gongnv[0].level+"-"+fz.Gongnv[0].name

        show gn at chara
        "[temptext]" "见过[my.cheng]。"

        if timenum >=4 and fz == shiqinfz:
            if fz.state == "有孕":
                "[temptext]" "[my.cheng]，皇上方才来看望我家主子，您还是请回吧。"
            else:
                "[temptext]" "[my.cheng]，我家主子如今正被皇上召幸呢。"
            hide screen Palacebuttons
            jump 皇宫界面
        elif my.level > fz.level:
            if fz.state == "抱恙" or fz.state == "病重":
                "[temptext]" "[my.cheng]，我家主子如今抱病在身，无法见客，您还是请回吧。"
                hide screen Palacebuttons
                jump 皇宫界面

            elif jinzu(fz) == True:
                "[temptext]" "[my.cheng]，我家主子被禁足在寝宫，没有皇上的允许，任何人不得来探望。您还是请回吧……"
                hide screen Palacebuttons
                jump 皇宫界面
            elif fz.xingge == "清冷" or fz.xingge == "安静":
                if fz.like < 10:
                    $ lucky = renpy.random.randint(0, 3)
                elif fz.like > 80:
                    $ lucky = 1
                elif fz.like < 25:
                    $ lucky = renpy.random.randint(0, 2)
                elif fz.like < 50:
                    $ lucky = renpy.random.randint(0, 1)
                else:
                    $ lucky = lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    "[temptext]" "[my.cheng]，我家主子今天不想见客，您还是请回吧……"
                    hide gn
                    "（无奈你只得离开。）"
                    "（你尚未走远，却听到从寝殿之中传出女子的一声轻叹……）"
                    hide screen Palacebuttons
                    jump 皇宫界面
                else:
                    pass
            elif fz.xingge == "势利" and fz.level >0:
                if my.love + fz.like  < 20:
                    $ lucky = renpy.random.randint(0, 3)
                elif my.love+ fz.like < 50:
                    $ lucky = renpy.random.randint(0, 2)
                elif my.love+ fz.like < 100:
                    $ lucky = renpy.random.randint(0,1)
                else:
                    $ lucky = renpy.random.randint(0, 4)
                if lucky == 0:
                    "[temptext]" "[my.cheng]，真不凑巧，我家主子方才出去了，您还是改日再来吧。"
                    hide gn
                    "（无奈你只得离开。）"
                    "（你尚未走远，却听到从寝殿之中传出女子的一声冷笑，似乎还说着些“懒得在那种无名之辈身上浪费时间”之类的话。）"
                    hide screen Palacebuttons
                    jump 皇宫界面
                else:
                    pass
            else:
                $ tempnum = my.level-fz.level - fz.like*0.1
                $ tempnum =round(tempnum*0.2)
                $ tempnum =abs(tempnum)
                $ lucky = renpy.random.randint(0,tempnum)
                if lucky > 0 and fz.level >0:
                    "[temptext]" "[my.cheng]，真不凑巧，我家主子方才出去了，您还是改日再来吧。"
                    hide gn
                    我 "看来只有择日再来了。"
                    hide screen Palacebuttons
                    jump 皇宫界面
                else:
                    pass

            "[temptext]" "请容奴婢进去通禀一声。"
            hide gn
            "片刻后……"
            show gn at chara
            "[temptext]" "[my.cheng]，请随奴婢来。"
            hide gn
            if fz.level == 0:
                $ bg("凤仪宫内")
                with fade
            else:
                $ bg("妃嫔寝居内")
                with fade
            $ timenum =  timenum +1
            $ AP = AP - 1
            show screen notify(fz.palace+fz.qinju)

            if fz == chuhuan and chuhuan not in my.foes and chuhuan.like >= 0:
                show 楚欢 笑
            elif fz == chuhuan:
                show 楚欢
            elif fz == taoning:
                show 陶凝
            else:
                show fz at chara
            if fz.like > 50 and fz.xingge =="活泼":
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你又来找我玩啦？嘻嘻，等你好久了！哎……免了那些虚礼了，快说说，今天又有什么乐子？"
            elif fz.like > 30 and fz.xingge =="活泼":
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你终于来啦！我一直盼着你呐！"
            elif fz.like > 80 and fz.xingge =="清冷":
                "[fz.hao][fz.weifen] [fz.name]" "我就知道是[aicheng]你来了……除了你，宫里再无旁人愿意来见我罢。快坐。"
            elif fz.like > 50 and fz.book > 80:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你来了？坐吧，我正在看书，还未来得及整衣理妆，你别见外。"
            elif fz.like > 50 and fz.muzic > 80:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你来了？坐吧，我正在练舞，瞧我这浑身是汗的样子……你别见外。"
            elif fz.like > 50 and fz.muzic > 80:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你来了？坐吧，我正在练曲，一时出了神，没来得及出来迎接……你别见外。"
            elif fz.like > 50 and fz.cixiu > 80:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你来了？坐吧，正好我在玩弄些刺绣的玩意儿，你来替我瞧瞧。"
            elif fz.like > 80:
                "[fz.hao][fz.weifen] [fz.name]" "（她笑着上前来迎接你，看得出来很是高兴。）"
            elif fz.like > 50:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]，不必拘礼，坐罢。"
            elif fz.like > 25:
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]？你今日怎的有空过来，快坐罢。"
            elif fz.like <= 20 and fz.xingge == "娇纵" and fz.love >= 30 and fz.love >= my.love:
                "一进殿便看见[fz.cheng]手里把玩着一件首饰，见你进来，便交予了身后宫人。"
                "[fz.hao][fz.weifen] [fz.name]" "替本宫收好了，这可是皇上御赐之物呢。"
                "[fz.hao][fz.weifen] [fz.name]" "（看向你，笑意盈盈）[my.cheng]来了？"
            elif fz.like <= 20 and fz.xingge == "娇纵" and fz.love <= 30 and fz.love <= my.love:
                "还未进殿便听到有陶瓷碎裂的声音和女子的怒骂，走进便见[fz.cheng]一脸懊怒地坐在椅上，脚边几个小宫女正埋头收拾着地上的狼藉。"
                "[fz.hao][fz.weifen] [fz.name]" "（见你进来，撑着笑容）[my.cheng]来了？"
            elif fz.like <0 and fz.xinji < 700:
                "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]的表情看起来似乎并不是很想看到你。）"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]？既然来了，便坐罢。"
                "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]坐在椅子上，等着你说明来意。）"
            $ hudongcishu = 0
            $ qingancishu = 0
            $ shihaocishu = 0
            $ fz.meet = fz.meet +1
            call 拜访妃子2 (fz=fz) from _call_拜访妃子2
        elif jinzu(fz) == True:
            "[temptext]" "[my.cheng]，我家主子被禁足在寝宫，没有皇上的允许，任何人不得来探望。您还是请回吧……"
            hide screen Palacebuttons
            jump 皇宫界面
        else:
            "[temptext]" "([fz.name]的宫女恭敬地将你迎入了内殿。)"
            hide gn
            if fz.level == 0:
                $ bg("凤仪宫内")
                with fade
            else:
                $ bg("妃嫔寝居内")
                with fade

            $ timenum =  timenum +1
            $ AP = AP - 1
            show screen notify(fz.palace+fz.qinju)
            if fz == chuhuan and chuhuan not in my.foes and chuhuan.like >= 0:
                show 楚欢 笑
            elif fz == chuhuan:
                show 楚欢
            else:
                show fz at chara
            if fz.like > 50 and fz.xingge =="活泼":
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你又来找我玩啦？嘻嘻，等你好久了！快说说，今天又有什么乐子？"
            elif fz.like > 25 and fz.xingge =="活泼":
                "[fz.hao][fz.weifen] [fz.name]" "[aicheng]你终于来啦！我一直盼着你呐！哎……我又忘记宫里的礼数了，不过我知道[aicheng]定然不会介意的，嘿嘿。"
            elif fz.like > 80 and fz.xingge =="清冷":
                "[fz.hao][fz.weifen] [fz.name]" "嫔妾恭迎[my.cheng]……（压低了声音）除了你，宫里再无旁人愿意来见我罢。"
            elif fz.like > 50:
                "[fz.hao][fz.weifen] [fz.name]" "给[my.cheng]请安。"
                "[fz.hao][fz.weifen] [fz.name]" "（在行过礼后，她微笑着看着你，似是心情愉快。）"
            elif fz.like > 25:
                "[fz.hao][fz.weifen] [fz.name]" "给[my.cheng]请安。"
                "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]今日前来有什么事情吗？"
            elif fz.like <= 20 and fz.xingge == "娇纵" and fz.love >= 30 and fz.love >= my.love:
                "一进殿便看见[fz.cheng]手里把玩着一件首饰，见你进来，便交予了身后宫人。"
                "[fz.hao][fz.weifen] [fz.name]" "替本宫收好了，这可是皇上御赐之物呢。"
                "[fz.hao][fz.weifen] [fz.name]" "（看向你，笑意盈盈）给[my.cheng]请安。"
            elif fz.like <= 20 and fz.xingge == "娇纵" and fz.love <= 30 and fz.love <= my.love:
                "还未进殿便听到有陶瓷碎裂的声音和女子的怒骂，走进便见[fz.cheng]一脸懊怒地坐在椅上，脚边几个小宫女正埋头收拾着地上的狼藉。"
                "[fz.hao][fz.weifen] [fz.name]" "（见你进来，撑着笑容）给[my.cheng]请安。"
            elif fz.like <0 and fz.xinji < 700:
                "[fz.hao][fz.weifen] [fz.name]" "给[my.cheng]请安。"
                "[fz.hao][fz.weifen] [fz.name]" "（[fz.name]的表情看起来似乎并不是很想看到你。）"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "给[my.cheng]请安。"
                "[fz.hao][fz.weifen] [fz.name]" "不知[my.cheng]前来有何贵干？"
            $ hudongcishu = 0
            $ qingancishu = 0
            $ fz.meet = fz.meet +1
            $ shihaocishu = 0

            call 拜访妃子2 (fz=fz) from _call_拜访妃子2_1

label 拜访妃子2(fz):

    $ fzhd = []
    $ hudongcishu = 0
    $ fzhdlabel = "闲聊"

    if fz == chuhuan and fz.meet == 1:
        call 楚欢_初次见面 from _call_楚欢_初次见面
        if mapname == "召见邀约":
            jump 寝居界面
        else:
            jump 皇宫界面

    if fz == taoning and fz.meet == 1:
        call 陶凝_初次见面 from _call_陶凝_初次见面
        $ hudongcishu += 1
        $ fz = taoning
    if fz == taoning and fz.like > 50 and taoning_4 == False:
        call 陶凝_家中事 from _call_陶凝_家中事
        $ hudongcishu += 1
        $ fz = taoning
    if fz == taoning and fz.like > 80 and 0<taoning_fatherup <= 3 and taoning_5 == False:
        call 陶凝_好事 from _call_陶凝_好事
        $ hudongcishu += 1
        $ fz = taoning

    if my.level > fz.level:
        $ fzhd.append("请安")
        $ fzhd.append("闲聊")
        if zhengfeng == False and fz not in juqingfei:
            $ fzhd.append("争锋")
        $ fzhd.append("送礼")
        $ fzhd.append("讨好")
    else:
        $ fzhd.append("问好")
        $ fzhd.append("闲聊")
        if zhengfeng == False and fz not in juqingfei:
            $ fzhd.append("争锋")
        $ fzhd.append("赏赐")
        $ fzhd.append("夸奖")




    if my.level > fz.level and fz not in my.friends and fz not in my.foes:
        $ fzhd.append("投诚")

    if my.level <= fz.level and fz not in my.friends and fz not in my.foes:
        $ fzhd.append("拉拢")

    if my not in fz.foes and fz not in my.foes and fz.like >= 30:
        $ fzhd.append("挑拨")

    if len(fz.friends) > 0 and my not in fz.foes and fz.like > 30:
        $ fzhd.append("离间")

    if fz.like >= 20 and my.level < fz.level:
        $ fzhd.append("提点")

    if my.level < fz.level:
        $ fzhd.append("训诫")

    if my.level >= fz.level:
        $ fzhd.append("挑衅")

    if my.huashu["一A"] !=0 and len(fz.foes) > 0:
        $ fzhd.append("斡旋")

    if my.anhai["一B"] !=0 and mapname == "召见邀约" and pincha == False:
        $ fzhd.append("品茶")


    if [fz,"怀孕"] in gongxi:
        $ fzhd.append("恭喜其怀孕")

    if [fz,"晋位"] in gongxi:
        $ fzhd.append("恭喜其晋位")

    if [fz,"生产"] in gongxi:
        $ fzhd.append("恭喜其得嗣")

    if [fz,"美言"] in ganxie:
        $ fzhd.append("感谢其美言")

    if [fz,"提拔"] in ganxie:
        $ fzhd.append("感谢其提拔")

    if [fz,"小产"] in xiluo:
        $ fzhd.append("奚落其小产")

    if [fz,"降位"] in xiluo:
        $ fzhd.append("奚落其降位")

    if [fz,"失宠"] in xiluo:
        $ fzhd.append("奚落其失宠")

    if fz.level == 0 and atan_time < 11 and atan_end_1 == 1 and 0 not in atan_help:
        $ fzhd.append("关于阿檀……")


    if mapname != "召见邀约":
        $ fzhd.append("离开")
    else:
        $ fzhd.append("送客")

    while hudongcishu <= 3:
        $ hudongcishu += 1
        call screen feizihudong()
        call expression fzhdlabel from _call_expression

    if my.xinji > 900:
        $ fz.xinji = fz.xinji + 4
    elif my.xinji < 700:
        $ fz.xinji = fz.xinji + 3
    elif my.xinji < 400:
        $ fz.xinji = fz.xinji + 2
    elif my.xinji < 200:
        $ fz.xinji = fz.xinji + 1
    else:
        pass

    if fz.xinji > 900:
        $ my.xinji = my.xinji + 4
    elif fz.xinji < 700:
        $ my.xinji = my.xinji + 3
    elif fz.xinji < 400:
        $ my.xinji = my.xinji + 2
    elif fz.xinji < 200:
        $ my.xinji = my.xinji + 1
    else:
        pass


    if mapname == "召见邀约":
        if my.level < fz.level:
            "[fz.hao][fz.weifen] [fz.name]" "时候不早了，嫔妾先告退了。"
        else:

            "[fz.hao][fz.weifen] [fz.name]" "时候不早了，本宫先回去了。"
            我 "[fz.cheng]走好。"
        hide fz
        hide screen Palacebuttons
        hide screen fz_sx2
        scene black

        jump 寝居界面
    else:
        if my.level <= fz.level:
            show 我的宫女 at chara
            我的宫女 "[my.cheng]，我们似乎已经在[fz.qinju]待得够久了……"
            hide 我的宫女
            hide fz
            我 "（好像是的……）"
            我 "那本宫今天就先走了。"
            show fz at chara
            "[fz.hao][fz.weifen] [fz.name]" "恭送[my.cheng]！"
        else:

            "[fz.hao][fz.weifen] [fz.name]" "本宫乏了。"
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]，你跪安罢。"
            我 "嫔妾告退。"
            hide fz
        hide screen Palacebuttons
        hide screen fz_sx2
        scene black

        jump 皇宫界面


label 太乐坊:
    $ bg("太乐坊")
    show screen notify("太乐坊")
    menu:
        "大司乐":
            jump 大司乐
        "璇音阁主":

            jump 璇音阁主
        "霓裳阁主":
            jump 霓裳阁主
        "离开":
            jump 皇宫界面

label 大司乐:
    show 司乐 at chara
    if month == 3 or month == 9:

        if huaiyun(my) == True:
            司乐 "[my.cheng]可是要报名宴会表演？您如今身怀皇嗣，还是安心养胎得好，若因为献艺而出了什么差池，太乐坊可担待不起。"
            hide 司乐
            jump 皇宫界面
        elif my not in biaoyan:
            司乐 "[my.cheng]可要报名宴会表演？"
            menu:
                "舞蹈":
                    menu:
                        "表演《春归》" if dance01 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance01
                        "表演《引蝶》" if dance02 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance02
                        "表演《剑器行》" if dance03 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance03
                        "表演《胡旋》" if dance04 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance04
                        "表演《塞外雪》" if dance05 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance05
                        "表演《贵妃醉酒》" if dance06 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance06
                        "表演《掌上舞》" if dance07 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance07
                        "表演《惊鸿》" if dance08 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance08
                        "表演《明月》" if dance09 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = dance09
                        "再做考虑":
                            司乐 "报名宴会表演仅限本月，请您尽快做出决定。"
                            jump 大司乐

                    $ shifoubiaoyan = 1
                    司乐 "已为您记录在册，接下来三个月还请您多加准备。"
                    "（提示：若宴会当日没有赴宴或是完成度不足100，都会造成负面效果。）"
                    hide 司乐
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
                "音律":

                    menu:
                        "表演《梁祝》" if music01 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music01
                        "表演《采莲》" if music02 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music02
                        "表演《山鬼》" if music03 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music03
                        "表演《湘女》" if music04 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music04
                        "表演《求凰》" if music05 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music05
                        "表演《凤兮》" if music06 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music06
                        "表演《羲和》" if music07 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music07
                        "表演《无绝》" if music08 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music08
                        "表演《锦瑟》" if music09 in kufang:
                            $ biaoyan.append(my)
                            $ mybiaoyan = music09
                        "再做考虑":
                            司乐 "报名宴会表演仅限本月，请您尽快做出决定。"
                            jump 大司乐
                    $ shifoubiaoyan = 1
                    司乐 "已为您记录在册，接下来三个月还请您多加准备。"
                    "（提示：若宴会当日没有赴宴或是完成度不足100，都会造成负面效果。）"
                    $ timenum = timenum +2
                    $ AP = AP -1
                    hide 司乐
                    jump 皇宫界面
                "再做考虑":

                    司乐 "报名宴会表演仅限本月，请您尽快做出决定。"
                    jump 太乐坊
        else:
            司乐 "您已经报名过了下一次宴会的才艺表演。还请多加准备。"
            jump 太乐坊
    else:
        司乐 "[my.cheng]，现下并非报名宴会表演的时间。"
        hide 司乐
        jump 太乐坊



label 璇音阁主:
    show 璇音 at chara
    璇音 "璇音阁如今有这些曲谱……"
    menu:
        "《梁祝》" if my.muzic>15 and music01 not in kufang:
            $ kufang.append(music01)
            "曲谱《梁祝》已收入库房。"
        "《采莲》" if my.muzic>5 and my.qizhi >600 and music02 not in kufang:
            $ kufang.append(music02)
            "曲谱《采莲》已收入库房。"
        "《山鬼》" if my.muzic>30 and music03 not in kufang:
            $ kufang.append(music03)
            "曲谱《山鬼》已收入库房。"
        "《湘女》" if my.muzic>15 and my.qizhi >700 and music04 not in kufang:
            $ kufang.append(music04)
            "曲谱《湘女》已收入库房。"
        "《求凰》" if my.muzic>50 and music05 not in kufang:
            $ kufang.append(music05)
            "曲谱《求凰》已收入库房。"
        "《凤兮》" if my.muzic>30 and my.qizhi >800 and music06 not in kufang:
            $ kufang.append(music06)
            "曲谱《凤兮》已收入库房。"
        "《羲和》" if my.muzic>80 and music07 not in kufang:
            $ kufang.append(music07)
            "曲谱《羲和》已收入库房。"
        "《无绝》" if my.muzic>50 and my.qizhi >900 and music08 not in kufang:
            $ kufang.append(music08)
            "曲谱《无绝》已收入库房。"
        "没有合适曲谱":
            pass
    璇音 "恭送[my.cheng]。"
    hide 璇音
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面

label 霓裳阁主:
    show 霓裳 at chara
    霓裳 "霓裳阁如今有这些舞谱……"
    menu:
        "《春归》" if my.dance>15 and dance01 not in kufang:
            $ kufang.append(dance01)
            "舞谱《春归》已收入库房。"
        "《引蝶》" if my.dance>5 and my.meili >600 and dance02 not in kufang:
            $ kufang.append(dance02)
            "舞谱《引蝶》已收入库房。"
        "《剑器行》" if my.dance>30 and dance03 not in kufang:
            $ kufang.append(dance03)
            "舞谱《剑器行》已收入库房。"
        "《胡旋》" if my.dance>15 and my.meili >700 and dance04 not in kufang:
            $ kufang.append(dance04)
            "舞谱《胡旋》已收入库房。"
        "《塞外雪》" if my.dance>50 and dance05 not in kufang:
            $ kufang.append(dance05)
            "舞谱《塞外雪》已收入库房。"
        "《贵妃醉酒》" if my.dance>30 and my.meili >800 and dance06 not in kufang:
            $ kufang.append(dance06)
            "舞谱《贵妃醉酒》已收入库房。"
        "《掌上舞》" if my.dance>80 and dance07 not in kufang:
            $ kufang.append(dance07)
            "舞谱《掌上舞》已收入库房。"
        "《惊鸿》" if my.dance>50 and my.meili >900 and dance08 not in kufang:
            $ kufang.append(dance08)
            "舞谱《惊鸿》已收入库房。"
        "没有合适舞谱":
            pass
    霓裳 "恭送[my.cheng]。"
    hide 霓裳
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面

label 掖廷:
    $ bg("掖廷")
    show screen notify("掖廷")
    if yeting == False and laoji not in YTGongnv and laoji not in teshugn:
        $ laoji.like += my.lucky*0.1 + 1
    if yeting == False and yxxiao.like >= 0 and yxxiao not in teshugn:
        $ yxxiao.like += (100-my.lucky)*0.1 + 1
    $ yeting = True

    if yxxiao.like >= 50 and yxxiao not in teshugn:
        $ teshugn.append(yxxiao)
        $ gn = yxxiao
        $ yxxiao.like = 50
        $ yxxiao.beauty=500
        with hpunch
        "？？？" "今天就让你们尝尝我姑奶奶的厉害！"
        "？？？" "谁敢再让我吃馊了的馒头，我就把你们的脸打成馒头！"
        show 我的宫女
        我的宫女 "主子小心！"
        我 惊 "（？！）"
        "只见一个隐约散发着酸臭味的馒头朝这边飞来……"
        "若非[my.Gongnv[0].name]反应及时，替你挡了下来，否则你怕是难逃此“劫”。"
        hide 我的宫女
        show 李公公 at you
        李公公 "哎哟！[my.cheng]，恭迎[my.cheng]，没……没惊到您吧？"
        menu:
            "掖廷一天天都乌烟瘴气的":
                $ xingzi += 5
                李公公 "[my.cheng]教训的是……"
            "无碍":
                $ xingzi -= 5
                李公公 "（长舒了一口气）您没事便好。"
        李公公 "游潇潇！"
        show gn at zuo
        "女孩儿" "吼那么大声干嘛，我没聋！"
        李公公 "你看你又闯祸了！"
        "女孩儿" "我说了我没聋！"
        我 怒 "……（耳朵疼）"
        李公公 "（气急败坏）饿了你一顿你还不长记性，仍是这般作威作福，还当这是在建章宫吗？"
        "女孩儿" "说了饿我一顿，凭什么还要给我臭馒头！别以为我不知道是你指使的！"
        "女孩儿" "不就是昨天不小心往你身上泼了一桶水吗？真小气！"
        李公公 "你你你！"
        李公公 "你还敢这么理直气壮！"
        "女孩儿" "我不仅理直气壮！{p}我还要把你打成臭馒头！"
        李公公 "（狠狠挨了几下）诶唷……诶唷！"
        李公公 "[my.cheng]，救救奴才！救救奴才！"
        menu:
            "这宫女好生放肆":
                "女孩儿" "（悻悻停手）哼……"
            "（袖手旁观，兴致盎然）":
                李公公 "哎哟，错了错了，潇潇姑娘饶了奴才这一回吧！别打了！别打了！"
                我 常 "（真想不到李公公居然被一个小宫女欺负成这样。掖廷还真是奇人多。）"
                李公公 "你就看在[my.cheng]的份上饶了奴才吧！"
                李公公 "[my.cheng]今日来掖廷想来是有要事，你把奴才打死了，可耽搁了娘娘的正事！"
                "女孩儿" "（悻悻停手）哼……"
        李公公 "还不见过[my.cheng]。"
        "女孩儿" "奴婢见过[my.cheng]。"
        我 常 "这宫女是……"
        "游潇潇" "奴婢游潇潇，原在建章宫当差。"
        我 "建章宫？"
        李公公 "[my.cheng]有所不知，她本是在建章宫当差，可做事实在莽撞无礼，才被送来掖廷管教……"
        李公公 "可谁知，这丫头性子太烈，又仗着太后惯着她，肆无忌惮，把整个掖廷搞的鸡飞狗跳。"
        李公公 "您说奴才该怎么办呢？太后当初将她送来掖廷，还让奴才好好管教着，又不能打她板子，还能如何管教呢？"
        "游潇潇" "（小声）哼……等太后娘娘气消了，你还有胆子说要管教本姑娘？"
        hide gn
        show 我的宫女 at zuo
        我的宫女 "娘娘，奴婢倒是想起来了，前阵子太后娘娘的陪嫁宫女年老出宫了，然后送了自家闺女进来。"
        我的宫女 "那姑娘名义上是建章宫的宫女，可太后娘娘喜欢得不得了，说是当成自己亲女儿也不为过……"
        我的宫女 "结果上次不知怎的，和莲稚姑娘大动干戈，太后不得已将她送来掖廷管教。"
        我的宫女 "应当就是这位潇潇姑娘了。"
        hide 我的宫女
        show gn at zuo
        "游潇潇" "嗐，我和莲稚那就是个误会！"
        "游潇潇" "我都跟她说清楚了！可是呢，太后娘娘总怕莲稚觉着她偏心了，才把我给送到这儿来了。其实人家根本没有。"
        "游潇潇" "太后娘娘的担心真是太多余了！"
        menu:
            我 "这游潇潇倒是有趣……"
            "收为己用":
                我 "既然如此，不如就到本宫宫里伺候吧。"
                李公公 "（惊）"
                "游潇潇" "真……真的么？{p}您愿意让我去您宫里伺候？"
                "游潇潇" "那太好了！您放心，我、啊不，奴婢一定为娘娘赴汤蹈火、肝脑涂地……"
                "游潇潇" "唉……在建章宫里太后娘娘老是这也不许干，那也不许说，莲稚也跟个老婆子似的逼逼叨叨，真是无聊死了！"
                我 "好啦好啦，收拾好你的物什，稍后来[my.palace]见本宫吧！"
                "宫人" "太后娘娘驾到——"
                "（众人齐齐请安。）"
                hide 李公公
                show 太后 at you
                太后 "好了，都免礼罢。"
                "游潇潇" "太后娘娘！"
                太后 "潇潇在掖廷可还好？"
                "游潇潇" "好！好着呢！（煞是得意）您瞧，[my.cheng]慧眼识人，赏识潇潇，让潇潇去她宫里当差呢！"
                太后 "[my.cheng]？"
                太后 "这……哀家还想着，之前不该让你来掖廷受委屈，打算给你娘亲赐个命妇之位，再替你指个顶好的人家……"
                "游潇潇" "（不耐）那有什么好的？就让潇潇去[my.cheng]宫里吧，往后有空还能去建章宫看您，您也不怕建章宫被搞的鸡飞狗跳了。"
                太后 "你还在生哀家的气呐……"
                太后 "莲稚都给哀家说清楚了，之前是哀家错怪你了，行了，先跟哀家回建章宫吧。"
                太后 "（给你使了个眼色）"
                menu:
                    "让潇潇听太后的话":
                        我 "潇潇，太后娘娘的安排自然是妥当的。"
                        "游潇潇" "（叹气）本以为同[my.cheng]有缘呢。那潇潇就但凭太后娘娘做主了。"
                        太后 "（赞许地看了你一眼）同哀家走吧。"
                        "游潇潇" "（朝你拜了一拜）潇潇告辞了。"
                        $ Taihoulike_Up(my,10)
                        "太后扶起游潇潇，很快离开了掖廷。"
                        $ yxxiao.like = -999
                    "请求让潇潇留下":
                        $ my.Gongnv.append(yxxiao)
                        $ yxxiao.master = my
                        $ yxxiao.state = "寻常"
                        $ my.taihoulike -= 2
                        我 "太后娘娘，您既觉着潇潇性子需要管束，又不舍得她在掖廷受委屈，不如便把她交给臣妾吧。"
                        太后 "（迟疑）也罢……别让潇潇累着伤着，往后有空多带潇潇来建章宫陪伴哀家。"
                        我 "臣妾遵命。"
                        "游潇潇" "（大喜过望）多谢太后娘娘成全！"
                    "（给潇潇使眼色）" if my.xinji >= 700:
                        $ my.Gongnv.append(yxxiao)
                        $ yxxiao.master = my
                        $ yxxiao.state = "寻常"
                        $ Taihoulike_Up(my,2)
                        "游潇潇" "（撒娇）太~~后~~娘~~娘~~"
                        太后 "（抚额）行了行了。"
                        太后 "哀家知道你的意思了。"
                        太后 "不过哀家丑话先说在前头，潇潇性子不是一般的莽撞，[my.cheng]日后可别后悔了。"
                        "游潇潇" "（眉飞色舞）太后娘娘可真是言重了~"
                        太后 "（严厉）你可别给[my.cheng]添乱！"
            "事不关己":


                "宫人" "太后娘娘驾到——"
                "（众人齐齐请安。）"
                hide 李公公
                show 太后 at you
                太后 "好了，都免礼罢。"
                "游潇潇" "太后娘娘！呜呜呜！"
                "游潇潇" "您是来看潇潇的吗？潇潇错了，您把潇潇接走吧！掖廷这些坏蛋让人饿肚子，还让人吃臭馒头……"
                太后 "潇潇……唉，是哀家不好，这掖廷哪里是你待得的地方？"
                太后 "只是你这性子……本就不该入宫。"
                太后 "罢了，随哀家走吧。"
                太后 "等哀家给你娘亲赐个命妇之位，再替你指个顶好的人家。"
                太后 "潇潇是断然不可受委屈的！"
                "游潇潇" "（感动）潇潇谢太后娘娘！"
                "太后扶起游潇潇，很快离开了掖廷。"
                $ yxxiao.like = -999
        $ AP -= 1
        $ timenum += 1
        jump 皇宫界面




    if laoji.like >= 50  and laoji not in teshugn:
        $ teshugn.append(laoji)
        $ gn = laoji

        "鸡叫声" "咕！"
        "鸡叫声" "咕咕咕！"
        我 惊 "……"
        show 我的宫女
        我的宫女 "这……掖廷怎么会有鸡叫……"
        hide 我的宫女
        "只见不远处鸡叫声传来的方向，几只颜色艳丽的雉鸡在尖叫逃窜。"
        "又听见一阵急促的脚步声，一个身影追逐着它们而去。"
        show gn with fade
        "？？？" "唉哟，你们今个儿这是怎么了……一个个的这么不老实？不就是拿了你们几个蛋嘛……还没习惯吗？"
        hide gn
        show 我的宫女
        我的宫女 "主子……那个人……好美啊……"
        我 惊 "是啊……这掖廷居然有如此绝色美人！"
        hide 我的宫女
        show gn
        "？？？" "哟喂，讨厌死了~这么说人家也会不好意思的~"
        hide gn
        show 李公公 at you
        李公公 "鸡嬷嬷！唉，跟你说了多少次了，你在掖廷养鸡就算了，把它们放出来干什么！掖廷都被你搞的不得安宁！"
        show gn at zuo
        "美貌女子" "李公公你这么凶做什么？人家也是不小心的，这不是在想办法让它们回去么！"
        李公公 "快点快点，要是冲撞了哪位主子，咱们这些奴才可担待不起。"
        "美貌女子" "是啦~你放心吧，我的鸡都很乖的，今天……只是意外。"
        李公公 "鸡嬷嬷，要我说，您这一把年纪了什么时候才肯出宫去享清福啊，留在掖廷这么久了，也没哪个宫肯收你呀！"
        "美貌女子" "哼，李公公，看看奴家的脸，奴家明明风华正茂，这种话你也说得出来。奴家已经叫人把奴家的名字给放到名簿上了，定有慧眼识珠的娘娘会带奴家走的，不劳您费心了啊~"
        "说完，这位绝色美女便吆喝着那几只鸡消失在了长廊的尽头。"
        hide gn
        hide 李公公
        show 李公公 with fade
        李公公 "哟，[my.cheng]来啦，奴才见过[my.cheng]。"
        李公公 "方才那几只贱禽没惊了您吧？"
        $ YTGongnv.append(laoji)
        $ laoji.like = 0
        menu:
            "方才那女子是……":
                pass
        李公公 "噢……她呀，是掖廷一个杂役宫女，名叫老鸡。"
        李公公 "她的事情也是说来话长了……"
        李公公 "您今日来掖廷是为了……？"
        hide 李公公







    menu:
        "挑选宫女":
            call screen YTGongnv
        "找月姑姑" if ygg == True:
            show 月姑姑
            月姑姑 "[my.cheng]安。"

            $ kemai = []
            python:
                if my.anhai["初始"] >= 1:
                    kemai.append(poison01)
                if my.anhai["初始"] >= 2:
                    kemai.append(poison02)
                if my.anhai["初始"] >= 3:
                    kemai.append(poison03)
                lucky = renpy.random.randint(9,18)

                templist = renpy.random.sample( ygg_items, lucky)
                kemai =kemai +     templist



            jump 掖廷_月姑姑
        "关于妃嫔封号之事……":

            我 "（后宫妃嫔的仪制皆由掖廷打理，妃嫔封号也是先让掖廷的拟好了给皇上过目的。若花钱打点，便可在下次晋升时得个自己喜欢的赐字。）"
            menu:
                "花费五百两银子打点" if money >=500:
                    $ money = money - 500
                    python:
                        yetinghao = renpy.input("想要什么封号",length=2)
                        yetinghao = yetinghao.strip()

                        if not yetinghao:
                            yetinghao = ""

                    if yetinghao in prehao_list and yetinghao not in hao_list:
                        "已经有妃嫔使用此封号了。"
                        "五百两已退还。"
                        $ money = money + 500
                        jump 掖廷
                    elif yetinghao == "":
                        "五百两已退还。"
                        $ money = money + 500
                        jump 掖廷
                    else:
                        if yetinghao in hao_list:
                            $ hao_list.remove(yetinghao)
                        else:
                            pass
                        python:
                            global yetinghao
                        $ yetinghao = yetinghao
                        我 "已打点完毕。"
                        $ timenum = timenum +1
                        $ AP = AP -1
                        jump 皇宫界面
                "再做打算":
                    jump 掖廷

label 掖廷_月姑姑:
    "（找月姑姑做什么呢？）"
    menu:
        "出售":
            $ sell_list = []
            $ buy_list = []
            $ itemsjiage = 0
            call screen sell()
            月姑姑 "[my.cheng]这里还真有不少好东西呢。"
            if ygg_like >= 100:
                $ ygg_like = 100
            $ tempnum = round(ygg_like)
            "月姑姑当前好感：[tempnum]"
            jump 掖廷_月姑姑
        "购买":
            $ sell_list = []
            $ buy_list = []
            $ itemsjiage = 0
            call screen buy()
            月姑姑 "多谢[my.cheng]赏脸了。"
            if ygg_like >= 100:
                $ ygg_like = 100
            $ tempnum = round(ygg_like)
            "月姑姑当前好感：[tempnum]"
            jump 掖廷_月姑姑
        "离开":
            月姑姑 "[my.cheng]慢走。正好我也该去采买新的货物了。"
    $ ygg = False
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面




label 召见邀约(fz):
    $ mapname= "召见邀约"
    hide screen myroom
    show screen Palacebuttons
    image fz = "Feizi/F[fz.face].webp"
    show 我的宫女 at chara
    if timenum >=4 and fz == shiqinfz:
        我的宫女 "[my.cheng]，[fz.cheng]如今正在伴驾。"
        hide screen Palacebuttons
        jump 寝居界面
    elif fz.state == "抱恙" or fz.state == "病重":
        我的宫女 "[my.cheng]，[fz.cheng]如今抱病在身，不便外出。"
        hide screen Palacebuttons
        jump 寝居界面
    elif jinzu(fz) == True:
        我的宫女 "[my.cheng]，[fz.cheng]如今被皇上禁足，无法前来。"
        hide screen Palacebuttons
        jump 寝居界面
    elif my.level > fz.level:
        if fz.xingge == "清冷" or fz.xingge == "安静":
            if fz.like < 10:
                $ lucky = renpy.random.randint(0, 3)
            elif fz.like > 80:
                $ lucky = 1
            elif fz.like < 25:
                $ lucky = renpy.random.randint(0, 2)
            elif fz.like < 50:
                $ lucky = renpy.random.randint(0, 1)
            else:
                $ lucky = lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                我的宫女 "[my.cheng]，[fz.cheng]说她今日不想外出走动。"
                hide screen Palacebuttons
                jump 寝居界面
            else:
                pass
        elif fz.xingge == "势利" and fz.level >0:
            if my.love + fz.like  < 20:
                $ lucky = renpy.random.randint(0, 3)
            elif my.love+ fz.like < 50:
                $ lucky = renpy.random.randint(0, 2)
            elif my.love+ fz.like < 100:
                $ lucky = renpy.random.randint(0,1)
            else:
                $ lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                我的宫女 "[my.cheng]，[fz.cheng]今日似乎不在寝居内，奴婢未能将她请来。"
                hide screen Palacebuttons
                jump 寝居界面
            else:
                pass
        elif fz.like < 0:
            我的宫女 "（欲言又止）[my.cheng]，[fz.cheng]今日似乎不在寝居内，奴婢未能将她请来。"
            hide screen Palacebuttons
            jump 寝居界面
        else:
            $ tempnum = my.level-fz.level - fz.like*0.1
            $ tempnum =round(tempnum*0.2)
            $ tempnum =abs(tempnum)
            $ lucky = renpy.random.randint(0,tempnum)
            if lucky > 0 and fz.level >0:
                我的宫女 "[my.cheng]，[fz.cheng]今日似乎不在寝居内，奴婢未能将她请来。"
                hide screen Palacebuttons
                jump 寝居界面
            else:
                pass
    else:
        pass

    $ timenum =  timenum +1
    hide 我的宫女
    "片刻后……"

    if fz == chuhuan and chuhuan not in my.foes and chuhuan.like >= 0:
        show 楚欢 笑
    elif fz == chuhuan:
        show 楚欢
    else:
        show fz at chara
    with fade
    if fz.like > 80:
        "[fz.hao][fz.weifen] [fz.name]" "（笑着走进殿内，看得出来很是高兴。）[aicheng]，今日找我何事？"
    elif fz.like > 50:
        "[fz.hao][fz.weifen] [fz.name]" "[aicheng]，今日可是有事找我？"
    else:
        if fz.level > my.level:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]召嫔妾何事？"
        else:
            "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]请本宫前来，所为何事？"
    $ hudongcishu = 0
    $ qingancishu = 0
    $ shihaocishu = 0
    $ fz.meet = fz.meet +1
    call 拜访妃子2 (fz=fz) from _call_拜访妃子2_2

label 锦寒宫:
    show screen notify("锦寒宫")
    hide screen Bigmap
    $ bg("锦寒宫")
    if my.level > 12:
        "刚刚走到锦寒宫门口，就被几个侍卫拦下。"
        show 我的宫女 at chara
        我的宫女 "主子，咱们还是走吧，按宫规，只有皇上、太后、皇后可出入冷宫。"
        hide 我的宫女
        jump 皇宫界面
    elif my.level == 0:
        pass
    else:
        if lgchuruxuke == False:
            "刚刚走到锦寒宫门口，就被几个侍卫拦下。"
            show 我的宫女 at chara
            我的宫女 "主子，咱们还是走吧，按宫规，只有皇上、太后、皇后可出入冷宫。"
            hide 我的宫女
            我 "（你正打算离开，一个侍卫却走上前来。）"
            "侍卫" "微臣参见这位娘娘，您可是想去冷宫探望哪位故人？"
            我 "本宫可不想触犯宫规。"
            "侍卫" "嘿嘿，只要咱们这些看守冷宫的侍卫不说，又有谁知道您来过呢？"
            我 "你的意思是……"
            "侍卫" "（比了个手指）只要花这个数，嘿嘿……"
            我 "（花费十两银子即可进入冷宫？）你……这样可稳妥？"
            "侍卫" "这您就放心吧，一万个稳妥！谁会跟钱过不去呢？您要信不过，就自个想法子吧……等做了皇后，自然是想进就进咯。"
            我 "……本宫知道了。"
            $ lgchuruxuke =True
        else:
            pass

    menu:
        "进入" if money >= 10 or my.level == 0:
            if my.level == 0:
                pass
            else:
                $ money = money -10
        "离开":
            jump 皇宫界面

    call screen lenggong


label 冷宫妃子(fz):
    $ bg("冷宫内")
    "冷宫年久失修，阴暗潮湿，角落里蜷缩着一个人影。"
    $ fz.meet = fz.meet +1
    show fz at chara
    if fz.like < 0:
        "[fz.weifen] [fz.name]" "哼……[my.name]，如今我已经是庶人之身，你还来见我做什么？！"
    elif fz.like > 80:
        "[fz.weifen] [fz.name]" "（抬头看见你，不敢相信自己的眼睛）[aicheng]，你怎么来了？"
    elif fz.like > 50:
        "[fz.weifen] [fz.name]" "[aicheng]……？"
    else:
        "[fz.weifen] [fz.name]" "[my.cheng]……？"

    if fz.jinzu > 108 and fz.like >= 0 and len(lenggong)< 6 and fz not in lenggong:
        $ tempnum = round(fz.jinzu/36)
        $ tempnum = int(tempnum)
        "[fz.weifen] [fz.name]" "一晃竟然已经[tempnum]年了……我已经在这里待了[tempnum]年了……"
        "[fz.weifen] [fz.name]" "一个女子的一生又有多少个[tempnum]年可以蹉跎呢？"
        menu:
            "人至少活着便多一分希望":
                "[fz.weifen] [fz.name]" "是啊……活着……我这样，还算是活着么？"
                "[fz.weifen] [fz.name]" "哈哈哈……"
            "会想办法让你出去":
                "[fz.weifen] [fz.name]" "真、真的么……"
                "[fz.weifen] [fz.name]" "太好了！你……你一定要想办法让我出去啊，我真的不想再待在这里了！"
                $ lenggong.append(fz)

    menu:
        "安慰":
            我 "日子还长，皇上终究没要了你的性命。假以时日，等皇上气消了，你总有办法出去。"
            if fz.like < 0:
                "[fz.weifen] [fz.name]" "呵……惺惺作态，令人作呕！"
                $ Feizilike_Up(fz,1)
                $ fz.health = fz.health + 10

            elif fz.like > 80:
                "[fz.weifen] [fz.name]" "（泣不成声）[aicheng]，有你这个好姐妹，是我一生的幸事。"
                $ Feizilike_Up(fz,0.5)
                $ fz.health = fz.health + 20
            elif fz.like > 50:
                "[fz.weifen] [fz.name]" "（泣不成声，抱着你不肯撒手。）"
                $ Feizilike_Up(fz,0.7)
                $ fz.health = fz.health + 15
            else:
                "[fz.weifen] [fz.name]" "（沉默不语，眼底一片晶莹。）"
                $ Feizilike_Up(fz,1)
                $ fz.health = fz.health + 15
        "奚落":
            我 "早日如此，何必当初？若不是坏事做尽，天理难容，也不会遭皇上厌弃，落到这般田地！"
            if fz.like < 0:
                "[fz.weifen] [fz.name]" "呵……想必没了我，[my.cheng]在后宫里过得仍然很不如意吧？否则，又何苦上冷宫寻乐子。"
                "[fz.weifen] [fz.name]" "既然来了，倒不如别走了？（说完，她狰狞一笑，宛如厉鬼。）"
                $ fz.like = fz.like - 5
                $ fz.health = fz.health - 30

            elif fz.like > 80:
                "[fz.weifen] [fz.name]" "呵……所谓人情冷暖，原来也不过如此。"
                $ fz.like = fz.like -20
                $ fz.health = fz.health - 50
            elif fz.like > 50:
                "[fz.weifen] [fz.name]" "呵……所谓人情冷暖，原来也不过如此。"
                $ fz.like = fz.like - 10
                $ fz.health = fz.health - 30
            else:
                "[fz.weifen] [fz.name]" "呵……那又与你何干？"
                $ fz.like = fz.like - 10
                $ fz.health = fz.health -30
        "替其了断" if poison03 in kufang or poison04 in kufang:
            menu:
                "鹤顶红" if poison03 in kufang:
                    $ kufang.remove(poison03)
                "鬼鸩一品红" if poison04 in kufang:
                    $ kufang.remove(poison04)
            if fz.like < 0:
                "[fz.weifen] [fz.name]" "我如今被困在冷宫，好死不如赖活着，倒是要谢谢你送我上路。"
                "[fz.weifen] [fz.name]" "若人死真有魂魄，那我必然夜夜入你梦境，做你的梦魇！"

            elif fz.like > 80:
                "[fz.weifen] [fz.name]" "我如今被困在冷宫，好死不如赖活着，若是你亲手送我上路，我倒是乐得欢喜。"
                "[fz.weifen] [fz.name]" "若有来生……你我还能做好姐妹么……"
            else:
                "[fz.weifen] [fz.name]" "解脱了……也好。"
            "[fz.weifen] [fz.name]" "（说完，她口中吐出一口鲜血……）"
            $ fz.health = -100
            show 我的宫女 at chara
            我的宫女 "这……主子，我们快走吧……"
            hide 我的宫女
        "赠送补品" if medic01 in kufang or medic02 in kufang or medic03 in kufang or medic04 in kufang:
            menu:
                "[medic01.name]" if medic01 in kufang:
                    $ tempmedic = medic01
                    $ kufang.remove(medic01)
                "[medic02.name]" if medic02 in kufang:
                    $ tempmedic = medic02
                    $ kufang.remove(medic02)
                "[medic03.name]" if medic03 in kufang:
                    $ tempmedic = medic03
                    $ kufang.remove(medic03)
                "[medic04.name]" if medic04 in kufang:
                    $ tempmedic = medic04
                    $ kufang.remove(medic04)

            if fz.like < 0:
                "[fz.weifen] [fz.name]" "（不可思议地看着你）你……你这又安的是什么心思？！"
                我 "放心吧，没毒。"
                "[fz.weifen] [fz.name]" "（或许因为冷宫里吃不饱穿不暖，她犹豫惊惧之下还是收下了你送来的[tempmedic.name]）"
            elif fz.like > 50:
                "[fz.weifen] [fz.name]" "（动容）[aicheng]……多谢……"
            else:
                "[fz.weifen] [fz.name]" "（满脸欣喜）[my.cheng]……你这是？！"
            python:
                if tempmedic == medic01:
                    Feizilike_Up(fz,5)
                    fz.beauty = fz.beauty + 10
                    fz.health = fz.health + 10
                    fz.lucky = fz.lucky + 2
                elif tempmedic == medic02:
                    Feizilike_Up(fz,10)
                    fz.beauty = fz.beauty + 30
                elif tempmedic == medic03:
                    Feizilike_Up(fz,15)
                    fz.beauty = fz.beauty+ 20
                    fz.health = fz.health + 20
                    fz.lucky = fz.lucky + 10
                elif tempmedic == medic04:
                    Feizilike_Up(fz,20)
                    fz.bauty = fz.beauty + 50
                    fz.health = fz.health + 50
                    fz.qizhi = fz.qizhi + 30
                    fz.meili = fz.meili + 30
                    fz.lucky = fz.lucky + 20
                else:
                    pass
    hide fz
    if my.level == 0:
        "侍卫" "（在门外高喊）皇后娘娘，您千金贵体，可不要在此处久留啊！"
        我 "本宫知道。"
    else:
        "侍卫" "（在门外高喊）[my.cheng]，您该走了！"
        我 "……知道了。"


    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面



label 妃子主动互动(place):
    if len(Npcmeet) == 0:
        pass
    else:
        $ lucky = renpy.random.randint(0, 6)
        $ fz = renpy.random.choice(Npcmeet)
        if fz.like > 50:
            pass
        elif fz.qingxiang < 30 and my not in fz.foes:
            pass
        else:
            $ zhu = fz
            show fz at chara with dissolve
            if my.level >= zhu.level:
                "[fz.hao][fz.weifen] [fz.name]" "倒巧了，正好碰见[my.cheng]。"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "嫔妾见过[my.cheng]。"
            menu:
                "视而不见" if my.level < zhu.level:
                    "[fz.hao][fz.weifen] [fz.name]" "……"
                    $ fz.like -= 3
                "热络闲聊（增加好感）" if zhu.like >= 0:
                    "[fz.cheng]同你闲聊几句，便各自告别离开了。"
                    $ Feizilike_Up(fz,1)
                    hide fz
                "寒暄几句（争锋）":
                    "[fz.cheng]同你闲聊几句，却不想起了口舌争锋……"
                    menu:
                        "开始争锋":
                            call battle (fz=fz) from _call_battle_5
                            $ timenum = timenum +1
                            $ AP = AP -1
                            hide fz
                            jump 皇宫界面
                        "自动争锋":

                            if zidongbattle(zhu = fz,bei=my)>= 10:
                                $ fz.yali -= 5
                                $ my.yali += 5
                                "[fz.hao][fz.weifen] [fz.name]" "（欣喜）是我赢了！"
                            elif zidongbattle(zhu = fz,bei=my)<= -10:
                                $ fz.yali += 5
                                $ my.yali -= 5
                                "[fz.hao][fz.weifen] [fz.name]" "（黯然）是我输了……"
                            else:
                                "并未分出胜负……"
                            $ timenum = timenum +1
                            $ AP = AP -1
                            hide fz
                            jump 皇宫界面
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
                            hide fz
                            python:
                                renpy.return_statement()
    hide fz
    return

label 景地事件(place):


    if timenum == 5 and chuhuan_time <= 4 and chuhuan_0 == True and chuhuan_1 == False:
        "寂静的夜，不远处却传来一声男子的叹息。"
        "远处依稀站着一个男人的身影。"
        我 惊 "（是皇上？）"
        menu:
            "上前":
                我 "臣妾参见皇上。"
                show 皇帝
                皇上 "噢，是[my.cheng]啊。"
                皇上 "朕想一个人走走。"
                我 "皇上，更深露重，小心着凉。您是天子，更要担心龙体受损。"
                皇上 "身子康健，心头郁结，又该如何？"
                我 "皇上为何事烦心？"
                call 楚欢_皇上烦心 (place=place) from _call_楚欢_皇上烦心_1
            "离开":
                我 "（得罪了皇上可担待不起……）"
        return

    if place in hejing and chuhuan in juqingfei and chuhuan in NPC_fz_list and jinzu(chuhuan) == False and havetag("失心成疯",chuhuan) == False and chuhuan_4 == False and chuhuan.year >= 3:
        $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("love"),reverse = True)
        if NPC_fz_list[0] == my:
            python:
                templist = []
                for i in NPC_fz_list:
                    if jinzu(i) == True or havetag("失心成疯",i) == True or i.level == 0 or i.love <= 30 or i.like <= 50 or i == my or i == chuhuan:
                        pass
                    else:
                        templist.append(i)
            if len(templist) == 0:
                pass
            else:
                $ fz = renpy.random.choice(templist)
                call 楚欢_落水 (fz, place) from _call_楚欢_落水
    else:
        pass

    if place in yuhuayuan and  taoning in NPC_fz_list and jinzu(taoning) == False and havetag("失心成疯",taoning) == False and taoning.year == 0 and taoning_1 == False:
        python:
            templist = []
            for i in NPC_fz_list:
                if jinzu(i) == True or havetag("失心成疯",i) == True or i.love <= 20 or i == taoning:
                    pass
                elif i == my and taoning.meet > 0:
                    pass
                elif i.level >= taoning.level :
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
            $ taoning_1 = True
            if fz in Npcmeet:
                $ Npcmeet.remove(fz)
            if taoning in Npcmeet:
                $ Npcmeet.remove(taoning)
            call 偶遇陶凝_1 (fz) from _call_偶遇陶凝_1
    else:
        pass


    $ lucky = renpy.random.randint(0, 20)
    if place == "御花园" or place == "玉烟亭" or place == "千鲤池":
        if my.cixiu >= 80 and my.love >= 10 and lucky == 0:
            if my.taihoulike > 50:
                $ cheng = aicheng
            else:
                $ cheng = my.cheng
            if taihouxinge == "精敏":
                "正四处走走，散散心，却忽闻身后有人叫你，回首看去，竟是太后，而唤你的人，竟然是太后的宫女。"
                menu:
                    "行礼问安":
                        pass
                show 太后 at chara
                太后 "[cheng]免礼罢，哀家这奴才倒是眼尖，见着地上有这帕子，往前走几步便见着你，快看看是不是你的。"
                我 "（仔细端详了一番，的确是自己练女红时绣过的帕子。）"
                太后 "这帕子上的绣花，倒是不错，想来是心细之人，手艺也不错，可是[cheng]绣的？"
                我 "（应声）是。"
                python:
                    for i in my.friends:
                        if jinzu(i) == True or i.state == "病重" or i.level == beifei or i.taihoulike < 10:
                            pass
                        else:
                            tempfzlist.append(i)
                if len(tempfzlist) == 0:
                    太后 "（眼底显露出几分赏识）绣工不错。"
                    hide 太后
                else:
                    $ fz = renpy.random.choice(tempfzlist)
                    太后 "前些日那[fz.cheng]来看哀家时，还提过你的女红很是不错，现下看来，着实若此。"
                    hide 太后
                "（又闲聊许久……）"
                太后 "哀家乏了，[cheng]跪安罢。"
                hide 太后
            elif taihouxinge == "避世":
                "正四处走走，散散心，却忽闻身后有人叫你，回首看去，竟是太后，而唤你的人，竟然是太后的宫女。"
                menu:
                    "行礼问安":
                        pass
                show 太后 at chara
                太后 "起来便是，方才哀家呀正在后头走着呢，本打算找个亭子，再唤婢子前去唤[cheng]，谁知哀家的婢子却见着你掉了个帕子，你可瞧瞧，可是你的？"
                我 "（仔细端详了一番，的确是自己练女红时绣过的帕子。）"
                太后 "这帕子上的绣花，很是精细，间隔均匀，排线也很是精妙，色泽鲜艳，可是[cheng]自个绣的？"
                我 "（应声）是。"
                太后 "没想到[cheng]还有这等手艺，哀家可喜欢这些精巧的玩意了。改日若得空了，可得给哀家绣一个。"
                hide 太后
            elif taihouxinge == "擅权":
                "正四处走走，散散心，却忽闻身后有人叫你，回首看去，竟是太后，而唤你的人，竟然是太后的宫女。"
                menu:
                    "行礼问安":
                        pass
                show 太后 at chara
                太后 "[cheng]免礼罢，哀家这奴才倒是眼尖，见着地上有这帕子，往前走几步便见着你，快看看是不是你的。"
                我 "（仔细端详了一番，的确是自己练女红时绣过的帕子。）"
                太后 "这帕子上的绣花，可是你绣的？"
                我 "（应声）是。"
                太后 "如此绣功，比大多数哀家所见的绣品要好，除去那些极品绣品，这绣功倒很是难得。"
                太后 "如此好的绣功，可得多多用才是，可别浪费了这一门技艺。"
                hide 太后
            else:
                "正四处走走，散散心，却忽闻身后有人叫你，回首看去，竟是太后，而唤你的人，竟然是太后的宫女。"
                menu:
                    "行礼问安":
                        pass
                show 太后 at chara
                太后 "免礼罢，哀家方才在拐角处便见着[cheng]了，倒是奴才眼尖，见着你掉了这帕子，快看看是不是你的。"
                我 "（仔细端详了一番，的确是自己练女红时绣过的帕子。）"
                太后 "这帕子上的绣花，很是精细，不输宫里头的绣娘，可是[cheng]自个绣的？"
                我 "（应声）是。"
                python:
                    for i in my.friends:
                        if jinzu(i) == True or i.state == "病重" or i.level == beifei or i.taihoulike < 10:
                            pass
                        else:
                            tempfzlist.append(i)
                if len(tempfzlist) == 0:
                    太后 "（眼底显露出几分赏识）绣工不错。"
                else:
                    $ fz = renpy.random.choice(tempfzlist)
                    太后 "前些日那[fz.cheng]来看哀家时，还提过[cheng]的女红很是精巧，这回见着了，果真如此。"
                太后 "改日若是得空呀，给哀家也绣个玩意。"
                hide 太后
            $ Taihoulike_Up(my,5)
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        else:
            pass
    else:
        pass


    if place == "疏影园" and month > 10 or place == "疏影园" and month < 2:
        $ lucky = renpy.random.randint(0,40)
        if len(Npcmeet) == 0 or lucky != 0 and timenum != 1:
            pass
        else:
            $ fz = renpy.random.choice(Npcmeet)
            if fz in my.foes or my in fz.foes or fz.level > my.level:
                pass
            else:
                $ Npcmeet.remove(fz)
                $ gn = fz.Gongnv[0]
                $ gnface = gn.face
                show 我的宫女 at chara
                我的宫女 "主子，前头梅树上好像有人。"
                hide 我的宫女
                menu:
                    我 "仔细瞧了眼，倒真的瞧见有个宫女打扮的人攀在梅树枝丫上。"
                    "真是败坏风景":
                        我 "好好的疏影园，倒成了这些子宫人攀爬玩乐的地方了？就想好好赏个梅花，竟然也能被人坏了兴致！"
                        show 我的宫女 at chara
                        我的宫女 "（见你面色不虞，朝那人呵斥道）娘娘面前像什么样子，还不下来！"
                        hide 我的宫女
                        "那宫女似乎没注意到你们，被[my.Gongnv[0].name]吓了一跳，从树上跌落下来，摔得不轻。"
                        show fz at chara with dissolve
                        "另一个身影缓缓走了出来。"
                        妃子 "[my.cheng]好大的气派，不知本宫的宫女采些雪水是哪里得罪了[my.cheng]，竟要受这般大罪。"
                        menu:
                            "反将一军":
                                $ fz.like -= 5
                                我 "[fz.cheng]这是说的哪里话，嫔妾方才被娘娘的宫女吓了一跳，这会子还没缓过来，娘娘怎么能……怎么能……"
                                我 "（扯了帕子半遮着脸，另一只手捂着胸口，泫然欲泣，楚楚可怜。）"
                                if fz.xinji >= 800:
                                    妃子 "（见你如此反倒莞尔一笑）本宫并不打算小题大做，[my.cheng]也不必做出这副样子给本宫看……若[my.cheng]是有意扮跳梁小丑逗本宫开心，那这份好意，本宫可就心领。"
                                    妃子 "本宫先告辞了，[my.cheng]自便罢。"
                                    hide fz
                                elif fz.xinji >= 400:
                                    妃子 "[my.cheng]颠倒黑白的本事本宫算是见识了，只是不知皇上面前，[my.cheng]能不能也这般强词夺理。"
                                    "（[fz.cheng]忿忿不平地走了。）"
                                    hide fz
                                else:
                                    妃子 "你……你！你这般无理，我定要禀告皇上。"
                                    "（[fz.cheng]忿忿不平地走了。）"
                                    hide fz
                            "冷静反问":
                                我 "嫔妾来这赏梅，却不知怎么这梅树上还长了娘娘的人。这倒是奇了，还得请皇上来观这异象才好。"
                                妃子 "呵，是了，采梅上雪这般文雅事[my.cheng]怎会懂呢，罢了罢了，只当这奴才倒霉，遇上了[my.cheng]，可惜这条贱命呐。昨儿个皇上来，还夸这丫头伶俐，不知一会皇上去本宫那儿，本宫该让谁近前伺候才好，不如[my.cheng]说说？"
                                menu:
                                    "冷嘲":
                                        $ fz.like -= 10
                                        我 "娘娘身边竟连个可用之人都没了么？[my.Gongnv[0].name]从咱们宫里挑两个调教好的去。"
                                        妃子 "[my.cheng]如此越俎代庖，也不怕被旁人听了去？"
                                        我 "（笑问）此处哪有旁人？"
                                        妃子 "你竟如此理直气壮！"
                                        妃子 "（愤恨地拂袖而去。）"
                                    "热讽":
                                        $ fz.like -= 7
                                        我 "若皇上问起，[fz.cheng]可叫他来找嫔妾，嫔妾自会与皇上说明。"
                                        妃子 "你……！"
                                        妃子 "（愤恨地拂袖而去。）"
                                    "阐述事实":
                                        我 "娘娘恕罪，方才嫔妾来此赏梅，不知怎么惊扰了树上这位，还是先给娘娘赔个不是吧。"
                                        if fz.xingge == "娇纵" or  fz.xingge == "势利":
                                            $ Feizilike_Up(fz,1)
                                            妃子 "[my.cheng]知错就好，既如此，回去反思己过吧，未免日后落个苛待宫人的名声。"
                                        else:
                                            $ Feizilike_Up(fz,2)
                                            妃子 "罢了罢了，此事到底还是本宫的宫女不小心，[my.cheng]也莫放在心上。"
                                        我 "是。"
                                        妃子 "（带着方才那跌落的宫女便转身而去。）"
                                hide fz
                        return
                    "好奇上前":
                        "还未走到树下，就看到从另一棵梅树后走出一个女子。"
                        show fz at chara
                        我 "（[fz.cheng]也在这里？）"
                        妃子 "采够了吗？"
                        show gn at chara
                        "[fz.Gongnv[0].level] [fz.Gongnv[0].name]" "您看这些够不够？"
                        hide gn
                        show fz at chara
                        妃子 "（看了眼）够了，咱们回去罢。"
                        hide fz
                        show gn at chara
                        "[fz.Gongnv[0].level] [fz.Gongnv[0].name]" "是。"
                        hide fz
                        hide gn
                        "主仆二人的身影很快消失在不远处……"
                        我 "（采集雪水？[fz.cheng]还真是花样多呢。）"
                    "漠不关心":

                        我 "去那边走走吧。"
                        show 我的宫女 at chara
                        我的宫女 "是，主子。"
                        hide 我的宫女
                        return
    else:
        pass
    return



label 闲逛事件(place):
    if taihouxinge == "精敏" and my.taihoulike > 80 and taihou3 == False:
        $ taihou3 = True
        "还未走几步，便闻前头传来喧闹声。"
        menu:
            "走近看看":
                $ makeYTGongnv(1,"宫女")
                $ gn = YTGongnv[-1]
                show 太后 at chara
                $ gnface = gn.face
                太后 "（眉头紧锁）何人？"
                我 "臣妾给太后娘娘请安。"
                太后 "（眉头松了些）原是[aicheng]，过来同哀家坐坐。"
                hide 太后
                show gn at chara
                "建章婢子 [gn.name]" "[my.cheng]，救救奴婢吧！"
                hide gn
                show 太后 at chara
                太后 "嚷嚷什么？放肆！"
                hide 太后
                show gn at chara
                "建章婢子 [gn.name]" "（吓得赶紧闭了嘴，但一双泪汪汪的眼睛仍然看着你。）"
                hide gn
                menu:
                    "帮其说话":
                        show 太后 at chara
                        太后 "这丫头方才糊里糊涂的，将哀家撞着了，手上的这玉镯子磕着后断了，哀家能不气吗？"
                        menu:
                            "换着法子的说好话":
                                我 "太后娘娘……"
                        太后 "罢了，既然[aicheng]帮着她说话，那就将她赐你管教了，否则哀家能给她气短命不可。"
                        show gn at chara
                        "婢子 [gn.name]" "多谢太后娘娘！多谢[my.cheng]！"
                        hide gn
                        "获得宫女[gn.name]。"
                        $ gn.like = 50
                        $ YTGongnv.remove(gn)
                        $ my.Gongnv.append(gn)
                        $ timenum = timenum +1
                        $ AP = AP -1
                        jump 皇宫界面
                    "视若无睹":
                        show 太后 at chara
                        太后 "给哀家打发了这蠢奴才。"
                        hide 太后
                        show 莲稚 at chara
                        莲稚 "是，太后娘娘。"
                        hide 莲稚
                        show gn at chara
                        "建章婢子 [gn.name]" "不要啊娘娘，不要啊……"
                        hide gn
                        "建章婢子 [gn.name]" "娘娘……饶命……（逐渐被拖远。）"
                        show 太后 at chara
                        太后 "晦气。"
                        $ YTGongnv.remove(gn)
                        $ timenum = timenum +1
                        $ AP = AP -1
                        jump 皇宫界面
            "赶紧离开":


                我 "（恐怕不是什么好事，连忙领着宫人掉头离开。）"
                $ timenum = timenum +1
                $ AP = AP -1
                jump 皇宫界面

    if place == "萋霜亭" or place == "玉烟亭":
        if taihouxinge == "精敏" and my.taihoulike > 50 and taihou2 == False:
            $ taihou2 = True
            "忽闻前头亭子处，传来一阵清脆声，想来是摔碎了什么东西。"
            menu:
                "上前查看":
                    show 太后 at chara with dissolve
                    "走近看去，亭中人竟是太后，而一个宫女正跪在地上，身旁那些碎片，瞧那纹理，是杯或壶的碎片。"
                    menu:
                        "行礼":
                            pass
                    太后 "起身罢。"
                    "太后一脸不悦，手轻轻一摆，太后身旁的宫女便把地上那跪着却不敢说话、浑身都在发抖的宫女给拖了下去。"
                    太后 "给哀家打发去液庭，以后别让哀家身边再出现这种笨拙的奴才，晦气。"
                    太后 "（看向你）过来，陪哀家聊会儿。"
                    我 "是……"
                    hide 太后
                    "和太后唠嗑许久……"
                    show 太后 at chara
                    太后 "哀家乏了，来人，起驾回宫。"
                    我 "恭送太后！"
                    hide 太后
                    我 "（长舒了一口气。）"
                    $ Taihoulike_Up(my,2)
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
                "调头离开":
                    我 "（有些可疑，还是小心为上吧……）"
                    "连忙离开了此处。"
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
    else:
        pass


    if place == "千鲤池":
        if taihouxinge == "宽和" and my.taihoulike > 50 and taihou2 == False:
            $ taihou2 = True
            show 太后 at chara with dissolve
            我 "（太后今日也在此处……）"
            menu:
                "上前问安":
                    太后 "[aicheng]？快些起身便是。"
                    我 "（陪太后闲聊……）"
                    hide 太后
                    "一宫女正用绢帕装着鱼饵小跑而来，不慎在太后跟前踩到了石子，摔了一跤，鱼饵撒了一地。"
                    $ makeYTGongnv(1,"宫女")
                    $ gn = YTGongnv[-1]
                    $ gnface = gn.face
                    show gn at chara
                    "建章婢子 [gn.name]" "（吓得跪在地上）太后娘娘饶命！奴婢不是故意要冲撞太后娘娘的！"


            menu:
                "帮其说话":
                    hide gn
                    show 太后 at chara
                    "（知其是无心之过，便连忙帮着这位宫女。谁知太后见你如此倒是笑了出声。）"
                    太后 "哈哈哈，好啦好啦，你不必再帮着她说话，哀家本就不打算怪罪她，谁都有犯错的时候，不过浪费了这些鱼饵罢。"
                    hide 太后
                    show gn at chara
                    "建章婢子 [gn.name]" "多谢[my.cheng]！多谢太后娘娘！"
                    hide gn
                    show 太后 at chara
                    太后 "还不快快起身，看看有没有摔着哪了，若是伤着了就去太医院找太医包扎包扎，就说是哀家说的，下去吧。"
                    hide 太后
                    show gn at chara
                    "建章婢子 [gn.name]" "是！奴婢告退。"
                    hide gn
                    show 太后 at chara
                    太后 "鱼饵也撒了，便不折腾人再那么一来二去的了，[aicheng]，陪哀家走走罢。"
                    我 "是。"
                    太后 "来，跟哀家说说，近日可有什么趣事。"
                    "一路上，太后与你聊得很是开心。"
                    $ Taihoulike_Up(my,2)
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
                "指责宫女":
                    "建章婢子 [gn.name]" "奴婢知错了……"
                    hide gn
                    show 太后 at chara
                    太后 "（有些不悦）罢了罢了，不过是撒了些鱼饵，什么饶不饶命的，哀家有这小肚鸡肠？不过芝麻大的小事。"
                    hide 太后
                    show gn at chara
                    "建章婢子 [gn.name]" "多谢太后娘娘！谢过太后娘娘！"
                    hide gn
                    show 太后 at chara
                    太后 "快些起身罢，还这么跪着哀家可就真要怪罪了，哀家乏了。"
                    我 "（似乎扰了太后兴致。）"
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
    else:
        pass
    return

label 太医院_before3:
    $ bg("太医院")
    show screen notify("太医院")
    if tyycishu == 0:
        "太医院内充斥着淡淡的苦药味，医官们进进出出，似是忙碌。"
        "虽然此处甚少有妃嫔来往，但你的出现并未引起旁人的注意。"
    elif tyycishu == 1:
        show 莲稚 at chara with dissolve
        莲稚 "太医令大人，太后娘娘要的药备好了吗？"
        "（一个老者走了出来。）"
        show 太医令 at chara with dissolve
        太医令 "莲稚姑娘，在这儿了。还是按以前的剂量服用便是了。"
        show 莲稚 at chara with dissolve
        莲稚 "有劳大人了。"
        hide 莲稚
        show 太医令 at chara
        太医令 "唷，这位是……[my.cheng]，今日怎来太医了？"
        menu:
            "只是闲逛经过":
                太医令 "那您自便吧，微臣先去看方子了。"
                hide 太医令
            "对医术颇有兴趣":
                太医令 "（有些吃惊）哦？[my.cheng]居然医术有兴趣？"
                太医令 "这倒是少见。"
                "太医令还想说什么，却听到不远处有个太医在叫他，似是有事。"
                太医令 "那微臣告辞，[my.cheng]自便吧。"
    else:
        "刚进太医院，就看到太医令的提着药箱从门外进来。"
        show 太医令 at chara
        太医令 "微臣见过[my.cheng]。"
        太医令 "[my.cheng]今日又上太医院来啦？"
        menu:
            "想求学医术":
                $ xueyi = True
                太医令 "这……[my.cheng]您别说笑了。"
                太医令 "后宫之中妃嫔患病，向来是由太医院诊治。您金枝玉叶，何必操这些心呢？"
                我 "本宫只是从小对医术便颇感兴趣，倒也不为了别的，您不必多心。"
                太医令 "既是如此，虽无人规定女子不能学医，但也没有太医向妃嫔传授医术的道理。"
                太医令 "但，若您真有意学医……"
                太医令 "西边那间房里，放着些医书，您可自行翻阅，只是不可带离太医院。若真能入了门，以后遇到些疑难，也可来找微臣。"
                menu:
                    "如此甚好":
                        pass
            "只是逛逛":

                我 "只是闲来无事，随意走走，过会儿便离了。"
        太医令 "那微臣便先忙去了。"


    $ tyycishu = tyycishu + 1
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面


label 太医院:
    $ bg("太医院")
    show screen notify("太医院")
    if rongyulike >= 10 and rongyu1 == False:
        window show
        $ rongyu1 = True
        "走进门内，便看到一个男子的身影，在一种穿着太医院服制的人当中甚是打眼。"
        show 容予 at chara
        容予 "（看了你一眼）见过[my.cheng]。"
        容予 "（礼数周全便要转身。）"
        menu:
            "叫住他":
                $ rongyulike = rongyulike + 10
                我 "容公子请留步！"
                容予 "找在下有事么？"
                "（他的神情与方才无异，却莫名渗出几分冰冷和疏离。）"
                我 "为什么一见我就急匆匆地走了？"
                容予 "没什么。"
                容予 "在下知道您心有顾虑。"
                容予 "再者……（声音突然低了几分）我这样的人，还是离得远些才好。"
                "没等你再开口，容予便快步离开了。"
                hide 容予 with dissolve
                我 "这人还真是奇怪啊……"
                show 小宫女 at chara
                "小宫女" "这位主子……"
                "小宫女" "请恕奴婢多嘴，您还是离那人远一点。"
                我 "（那人？好歹也是太医令之子，这说得也忒不客气。）"
                "小宫女" "（压低了声音）他生来白发异瞳，但凡懂些门道的人都懂，这是十足的不详之兆。"
                "小宫女" "容予公子医术好归好，但若是同他有了来往，定是会招来横祸。"
                "小宫女" "您还不知道吧，太医令夫妇本是好心收养他，却没过几年，太医令夫人便突然得了急症，撒手人寰。"
                "小宫女" "太医令的医术您总该是知道的，那病症却连他自己也说不上来，您说吓不吓人诶？"
                "小宫女" "可怜了太医令本是好心收养了一个弃婴，到头来却连自己的亲生孩子也没有……"
                menu:
                    "容予是太医令收养的？":
                        "小宫女" "是啊，那副样子一眼便知是个怪胎了，谁家敢留着啊？"
                        "小宫女" "也就太医令大人医者仁心罢了。"
                    "无稽之谈":
                        "小宫女" "奴婢也是好心，[my.cheng]若不信，那奴婢这就退下了。"
                hide 小宫女
                我 "……"
                menu:
                    "（往后还是小心些为好）":
                        $ my.xinji = my.xinji + 10
                    "（定是小宫女暗恋容予，不想让其他人接近）":
                        $ my.xinji = my.xinji - 10
            "算了":

                我 "这人还真是奇怪啊……"
                hide 容予
    elif rongyulike >= 20 and rongyu2 == False:
        window show
        $ rongyu2 = True
        show 容予 at chara
        我 "那个……"
        容予 "听义父提起，[my.cheng]倒是时不时来太医院。"
        menu:
            "想来找你":
                容予 "找我？"
                容予 "……"
                我 "之前我不舒服的时候是你来替我诊治。"
                我 "我刚刚入宫，只不过是个无名无姓的嫔妃，你却愿意冒着犯忌讳的风险前来，所以我才想好好感谢你。"
                容予 "那便不必了。"
                "未等你反应过来，容予转身便快步离开了。"
                hide 容予
                我 "（太医院的人都躲着他，唯独我没躲着他，他怎的倒像是躲着我似的？）"
            "想学医术":
                容予 "学医？为何？"
                我 "就是想学。"
                if xueyi == True:
                    我 "你义父已经同意我在太医院查阅医术，还可向他提问。"
                    容予 "好像听义父提起过。"
                    我 "正好我遇到几处疑问，眼下太医令不在，不如便由你代劳吧？"
                    容予 "（皱着眉头）……"
                    我 "容予公子，可是在等一个“请”字？"
                    容予 "在下不敢。"
                    容予 "既是[my.cheng]所求，在下自当听命。"
                else:
                    $ xueyi = True
                    容予 "西边那间房，是太医院存放医书的地方。你要是想学，可前去查阅。"
                    我 "可我对医术一窍不通，全凭看书也能学会吗？"
                    容予 "……"
                    我 "要是有不懂的，容予公子可愿意替我解答？"
                    容予 "（皱着眉头）……"
                    我 "容予公子，可是在等一个“请”字？"
                    容予 "在下不敢。"
                    容予 "既是[my.cheng]所求，在下自当听命。"
                    我 "如此，便多谢容予公子了。"
                容予 "（似是无奈地看了你一眼）叫容予便是了。"
                容予 "……"
                容予 "你既然时常来太医院，难道没听那人说起……"
                我 "说什么？"
                容予 "说……关于我的事。"
                menu:
                    "听说了":
                        容予 "你不怕我？"
                        我 "那些话我并未放在心里。"
                        容予 "（看着你认真的眼神，一时无话。）"
                        容予 "整个太医院的人，除了义父，都无人愿意靠近我，为何你……"
                        我 "为何其他人远离你，我便要随着他们？"
                        我 "我又不是没有自己的主意。"
                        容予 "你也是，总不能别人说什么便是什么吧。"
                        容予 "（愣了愣。）"
                        hide 容予
                        show 容予_笑 at chara
                        容予 "是么……"
                        hide 容予_笑
                        show 容予 at chara
                        容予 "我现下有事，等下次过来，我一定替你解答。"
                    "没有":
                        容予 "……"
                        容予 "你想学医，我不拦你。"
                        容予 "除此以外，还是离我远些得好。"
                        容予 "因为……我不想害了你。"
                        我 "……"
                        容予 "我还有事，就先走了。若以后医书上有何不懂的，可以来寻我，我若得空便替你解答。"
                "说完，容予的身影转眼就消失了。"
                hide 容予
                我 "（又这么走了……）"
                我 "（虽然他的语气有些冷，但却莫名给人亲近的感觉。）"
    elif year>= 8 and rongyu4 == False:
        window show
        if rongyulike >= 60 and rongyu5 == 0:
            $ rongyu4 = True
            "刚走进太医院，迎面却撞上一人。"
            show 容予_忧 at chara
            容予 "[my.cheng]？"

            menu:
                容予 "……抱歉。"
                "幸好你冲撞的人是我":
                    show 容予_笑 at chara
                    容予 "（似是无奈）是。"
                    hide 容予_笑
                    我 "行色匆匆的这是要去哪儿啊？"
                    容予 "……"
                    我 "怎么了？"
                "什么事这么急？":
                    容予 "没什么。（刻意别过眼神，不与你对视。）"
                    我 "还说没什么？你以为我是傻子还是瞎子？"
                    容予 "真的没什么。"
            容予 "[my.cheng]。"
            我 "什么？"
            容予 "还记得我们刚刚认识的时候我说过的话吗？"
            容予 "我说……不要靠近我。"
            我 "我说过了，我不在乎。"
            我 "和你认识这么久了，并没有什么不幸发生在我的身上，我看，那些都是无稽之谈。"
            我 "要不然就是我体质特殊，你偏偏克不住我。"
            我 "你更应当好好待我才是。"
            show 容予_笑 at chara
            容予 "……"
            hide 容予_笑
            容予 "抱歉。"
            容予 "可我不想让你因我而受到伤害。"
            容予 "以后，我们就当做不认识，可以吗？"
            menu:
                我 "……"
                "不可以":
                    容予 "……"
                    我 "我们认识这么久了……"
                    我 "你教我医术，我陪你说话，你说不认识了就不认识了？"
                    我 "容予，你觉得这些事情都是一句不认识就能够带过的么？"
                "我都说到这个份上了你还不明白么？" if rongyulike >= 80:
                    容予 "……"
                    我 "学医也好，专程来找你也好……"
                    我 "你非得要我直说吗？"
                    我 "你明白么？"
                    容予 "我……"
                    容予 "……"
                    我 "如果你不明白，我便直说了？"
                    容予 "我明白。"
                    容予 "你不要说。"
                    容予 "我负担不起。"
            容予 "抱歉。"
            我 "为什么？"
            我 "你什么都没做错。"
            if rongyulike >= 80:
                容予 "对不起。"
                容予 "[aicheng]……我可以这样叫你一次吗？"
                menu:
                    "你以后都这样叫我吧":
                        show 容予_笑 at chara
                        容予 "我也希望。可是，我大概没有机会了。"
                        hide 容予_笑
                        我 "为什么……你到底怎么了？"
                        我 "你今天好奇怪。"
                        我 "容予，我不喜欢你这样。"
                        容予 "……那就好。"
                        容予 "（声音愈发低沉）不喜欢……就好。"
                        容予 "[aicheng]，就此别过。"
                        $ rongyulike = rongyulike + 4
                    "……":
                        容予 "……"
                        容予 "[my.cheng]，你的医术精进，已经不再需要我了。"
                        容予 "再者，也可向我义父请教。"
                        容予 "[my.cheng]，就此别过。"
            else:
                容予 "或许吧。"
                容予 "[my.cheng]，就此别过。"
            hide 容予_笑
            我 "你要去哪里？"
            容予 "我……"
            容予 "义父替我安排了婚事，我不日便要回家成亲。往后也不会再到宫中来了。"
            我 "什么？"
            容予 "（目光深沉地看着你，眼神里蕴含了很多复杂的情绪。）"
            我 "容予！"
            hide 容予_忧
            我 "容予！"
            我 "……"
            if my.xinji > 500:
                我 "（不……他定然在骗我。）"
                我 "到底发生什么了？"
            else:
                pass
            $ rongyu = False
        elif rongyu5 > 6:
            $ rongyu = False
        else:
            pass

    elif year>= 8 and rongyulike >= 60 and 0 < rongyu5 <= 7 and rongyu6 == False:
        $ rongyu6 = True
        window show
        show 太医令 at chara
        我 "太医令！"
        太医令 "（正在收拾自己的药箱，看到你的出现，显然猜到了你的来意，显得有些慌张）[my.cheng]……您、您怎么来了？"
        我 "太医令，容予呢？"
        太医令 "（满头大汗）容、容予他……（突然想到了什么）容予也老大不小了，微臣已经替他寻了亲事，他如今在家中准备成亲事宜，往后也不会再入宫了。"
        我 "（置若罔闻）我之前在奉天楼正好听见太后和奉天楼的人说话，她说……她说要用容予的命去换皇上的命，这究竟是怎么一回事？！"
        太医令 "（大惊失色，四下望了一番，确认无人听到你方才的话才松了一口气）[my.cheng]！这些话要是被别人听去了，咱们可都得掉脑袋！[my.cheng]……微臣奉劝您一句，容予同您的缘分已经尽了。"
        我 "……我做不到。"
        我 "告诉我，告诉我究竟是怎么一回事！"
        太医令 "微臣可以告诉您，可是，告诉了您又能如何？"
        太医令 "谁也救不了容予的命……谁也救不了……"
        太医令 "是天要容予的命啊！"
        我 "这究竟是怎么一回事……"
        我 "太医令大人，求求你告诉我吧。"
        太医令 "[my.cheng]莫要如此，微臣担待不起！"
        太医令 "（长叹了一口气）是了，容予他……他是皇上的亲弟弟。"
        太医令 "容予的母妃出身胡族，被视为蛮夷，然而先帝专宠于其，有人欲处之而后快。当时，微臣也是奉人之命，在其生产之时做了手脚，只是不知为何，母亡子留。"
        太医令 "微臣一生治病救人，从未做过此番夺人性命之事，后思实在是心有愧疚，无法下手，未能斩草除根，故而收为养子。"
        我 "（回想之前在奉天楼所听到的，似乎并无分别，但仍是震惊不已。）"
        我 "容予他……竟然是皇子……"
        我 "那为何如今太后又要让他偿命？"
        太医令 "微臣也不知，太后说是天意，恐怕只有奉天楼的人才知道了！"
        "说这话的时候，太医令的脸上已是老泪纵横。自己抚养了快二十年的孩子，不明不白地便没了。眼前这个老人让你心生不忍。"
        太医令 "（抹了把眼泪）若现在去奉天楼，兴许还能见容予最后一面。可惜那地方，微臣是去不得的……"
        太医令 "（似乎不愿再提）微臣还有事，[my.cheng]请自便吧。"
        hide 太医令
        我 "（眼下去奉天楼，或许还能见容予最后一面……）"
        我 "容予，我们此生，缘分真的已尽了么？"
    else:





        pass

    menu:










        "找容予" if rongyu == True and rongyu4 == False:
            window show
            show 容予 at chara
            menu:
                容予 "[my.cheng]今日前来有事吗？"
                "闲聊":
                    call 容予对话 from _call_容予对话
                "学医":
                    "容予耐心地一一替你解答疑问，医术增进。"
                    if my.medic > 80:
                        $ my.medic = my.medic + 0.8
                    elif my.medic > 50:
                        $ my.medic = my.medic + 1.5
                    else:
                        $ my.medic = my.medic + 2
                    $ rongyulike = rongyulike + 1
                    $ timenum = timenum +2
                    $ AP = AP -2
            hide 容予

        "学习医术" if xueyi == True:
            $ lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                "正好碰到太医令有空，求学医术，大有进益。"
                if my.medic > 80:
                    $ my.medic = my.medic + 1
                elif my.medic > 50:
                    $ my.medic = my.medic + 2
                else:
                    $ my.medic = my.medic + 3
            elif lucky == 1 or lucky== 2:
                "在偏房查阅医书时碰见两个小医女，研谈片刻，颇有收获。"
                if my.medic > 80:
                    $ my.medic = my.medic + 0.8
                elif my.medic > 50:
                    $ my.medic = my.medic + 1.5
                else:
                    $ my.medic = my.medic + 2
            else:
                "在偏房翻阅医书，略有收获。"
                if my.medic > 80:
                    $ my.medic = my.medic + 0.5
                elif my.medic > 50:
                    $ my.medic = my.medic + 1
                else:
                    $ my.medic = my.medic + 1.5
            $ tyycishu = tyycishu + 1
            $ timenum = timenum +2
            $ AP = AP -2
        "闲逛":


            "太医院内充斥着淡淡的苦药味，医官们进进出出，忙碌不暇。"
            "虽然此处甚少有妃嫔来往，但你的出现并未引起旁人的注意。"
            $ tyycishu = tyycishu + 1
            $ timenum = timenum +1
            $ AP = AP -1
    if rongyu2 == True and rongyu4 == False and rongyu6 == False and rongyu7 == False:
        $ rongyu = True
    else:
        pass
    window hide
    jump 皇宫界面


label 重华宫:
    if timenum >= 4:
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
        "重华宫门扉紧闭，空无一人。"
        jump 皇宫界面
    else:
        $ bg("重华宫")
        menu:
            "询问先生":
                jump 重华宫_询问先生
            "亲自教导":
                jump 重华宫_亲自教导
            "离开":


                jump 皇宫界面


label 重华宫_询问先生:
    python:
        templist = []
        for i in NPC_Kids_list:
            if i.live == 0 and i.age >= 5:
                templist.append(i)
    if len(templist) == 0:
        我 "如今重华宫尚无已入学的皇嗣。"
        jump 重华宫
    else:
        我 "要询问哪一个孩子的近况呢？"
        call screen choicekid(templist)
        if kid.sex == "皇子":
            show 先生
        else:
            show 女先生
        $ TeacherTalk(kid)
        jump 重华宫


label 重华宫_亲自教导:
    python:
        templist = []
        for i in NPC_Kids_list:
            if i.live != 0 or i.age < 5 :
                pass
            elif my.level == 0:
                templist.append(i)
            elif i.mother == my:
                templist.append(i)
    if len(templist) == 0:
        我 "如今重华宫尚无可以亲自教导的皇嗣。"
        jump 重华宫
    else:
        我 "（最多可选择5个孩子进行教导，同时教导的孩子数量越少，效果越好，消耗两个行动点和两个时间段。）"
        $ choicedlist = []
    call screen choicekid_dx(templist,choicedlist,5)
    $ num = len(choicedlist)


    python:
        if num == 1 :
            temptext = choicedlist[0].cheng
        else:
            temptext = "孩子们"
        tempnum = 0
        for i in templist:
            if i.sex == "皇子":
                tempnum = 1
                break
    menu:
        "教导学业":
            "与[temptext]引经据典，畅所欲言。"
            python:
                tempnum = 0
                for i in choicedlist:
                    
                    if my.book - i.wen <= 0:
                        pass
                    else:
                        i.like += 1/num
                        if (my.book - i.wen)*0.1*(1/num) >= 1:
                            i.wen += 1
                            tempnum += 1
                        else:
                            i.wen += (my.book - i.wen)*0.1*(1/num)
                            tempnum =  (my.book - i.wen)*0.1*(1/num)
            if tempnum >= 0.5:
                "[temptext]似乎颇有收获。"
            else:
                "但你能感觉到[temptext]并没有太大的长进……"

        "女子才艺" if tempnum == 0:
            "与[temptext]吟诗作赋，奏琴起舞。"
            python:
                tempnum = 0
                for i in choicedlist:
                    
                    if (my.muzic+my.dance)*0.5 - i.wu <= 0:
                        pass
                    else:
                        i.like += 2*(1/num)
                        if ((my.muzic+my.dance)*0.5 - i.wu)*0.1*(1/num) >= 1:
                            i.wen += 1
                            tempnum += 1
                        else:
                            i.wen += ((my.muzic+my.dance)*0.5 - i.wu)*0.1*(1/num)
                            tempnum =  ((my.muzic+my.dance)*0.5 - i.wu)*0.1*(1/num)
            if tempnum >= 0.5:
                "[temptext]似乎颇有收获。"
            else:
                "但你能感觉到[temptext]并没有太大的长进……"
        "为人处世":
            "向[temptext]谆谆教导，传授自己的处事之道以及人生追求……"
            python:
                tempnum = 0
                for i in choicedlist:
                    i.like += 2*1/num
                    if my.qingxiang >= i.qingxiang:
                        i.qingxiang += my.xinji*0.005
                    else:
                        i.qingxiang -= my.xinji*0.005

    $ AP -= 2
    $ timenum += 2
    jump 皇宫界面

init python:
    def TeacherTalk(kid):
        if kid.sex == "皇子":
            who = laoshi
        else:
            who = nvlaoshi
        temptext = ""
        if kid.duli >= 85:
            temptext = "请恕在下直言，"+kid.cheng + "有时候……已经固执到了不可理喻的地步，甚至数次和老师甚至是陛下发生争执，长此以往，恐怕并不是什么好事。"
        elif kid.duli >= 70:
            temptext= kid.cheng + "虽然性情坚毅，但……时常也过于固执，还是要懂得变通才好。"
        elif kid.duli >= 50:
            temptext= kid.cheng + "很有自己的主见，但也懂得转圜周全之道。"
        elif kid.duli >= 30:
            temptext= kid.cheng + "平日里十分乖顺，但偶尔也会发表自己的意见。"
        elif kid.duli >= 15:
            temptext = kid.cheng + "虽然性情和顺，但……做事却缺乏主见。"
        else:
            temptext = "请恕在下直言，"+kid.cheng + "的个性实在有些软弱，甚至从不提起自己的任何想法，很是令人忧心啊。"
        renpy.say(who, temptext)
        
        if kid.qinmian >= 85:
            temptext= "对于学业，"+kid.cheng + "已经到了废寝忘食的地步，但若一味按图索骥，恐怕也会事倍功半，反而伤了身子。"
        elif kid.qinmian >= 70:
            temptext= kid.cheng + "在学业上很是勤奋，但有句话叫做“纸上得来终觉浅”。"
        elif kid.qinmian >= 50:
            temptext= my.cheng+"放心，"+kid.cheng + "平日在学业上表现极好，也并未拘泥于书本之中，不仅听从臣等的督导，也很善于自己思考。"
        elif kid.qinmian >= 30:
            temptext = kid.cheng + "在学业上，似乎心有旁骛……但对于臣等的话，倒还是能听得进去几分的。"
        elif kid.qinmian >= 15:
            temptext = "“业精于勤，荒于嬉。”"+kid.cheng + "再如此下去，怕是学业都要荒废了。"
        else:
            temptext = "唉……"+kid.cheng +"心思可以说是全然未在学业上，臣等能做的，也仅仅是尽力而为罢了。"
        
        renpy.say(who, temptext)
        if kid.iq >= 80 and kid.hdlike >= 80:
            temptext = kid.cheng +"天资卓绝，陛下想来也颇为器重，臣自会好好教导，不辜负了陛下和娘娘的重望。"
            renpy.say(who, temptext)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
