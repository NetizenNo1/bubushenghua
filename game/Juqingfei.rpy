


label 阿檀:
    python:
        atan.level = beifei
        atan.xing = "郑"
        atan.ming= "思檀"
        atan.name= "郑思檀"
        atan.hao = ""
        atan.state = "寻常"


        atan.age = 17
        atan.family = "前奉天楼司祝"
        atan.familylevel = 9
        atan.fatherduty = ""
        atan.familylocation = ""
        atan.health = 300
        atan.beauty = 650
        atan.yuanmao = atan.beauty
        atan.qizhi = 700
        atan.meili = 400
        atan.dance = 0
        atan.book = 50
        atan.cixiu = 20
        atan.muzic =20
        atan.battle = 0
        atan.medic = 0
        atan.like = 50
        atan.love = 0
        if 0 in atan_help:
            atan.love += 10
        if 1 in atan_help:
            atan.love += my.love*0.1
        if 2 in atan_help:
            atan.love += 10
        if atan.love <= 5:
            atan.love = 5

        tempnum = len(atan_help)+1
        a = int(beifei*0.5)+1
        atan.exp = weifen_list[a][3]*(1+tempnum*0.1)
        atan.year = 0
        atan.xinji = 350
        atan.xinji1 = True
        atan.xingge = "安静"
        atan.xingge1 = True
        atan.meet = 0
        atan.kids = []
        atan.taihoulike = 0
        if 2 in atan_help:
            atan.taihoulike += 20
        atan.lucky = 100
        atan.makelucky = 0
        atan.Gongnv =[]
        atan.qingxiang = 0
        atan.shiqin = 0
        atan.jinzu = 0
        atan.friends = []
        atan.foes = []
        atan.face = "atan"
        atan.shou = 60
        atan.tags = []
        atan.tags.append(tags_jqf[1])
        atan.tags.append(tags_limit_qizhi[1])
        atan.yali = 0
        Feizilevel_xuanxiu(atan)
        atan.cheng = atan.hao + atan.weifen
        atan.tequan1 = -1
        atan.tequan2 = -1
        atan.story = []
        atan.meishu = {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
        atan.huashu =  {"初始":2,"一A":2,"一B":2,"二A":0,"二B":2,"三级":0,"大招":0}
        atan.anhai =  {"初始":0,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
        atan.fangyu = {"初始":3,"一A":3,"一B":3,"二A":3,"二B":3,"三级":3,"大招":0}
        tempstory = "原为奉天楼司祝，虔心侍神，因对皇帝生情，入宫为妃。\n"+str(nianhao)+str(year)+"年"+str(month)+"月，册为"+str(atan.weifen)+"。\n"
        atan.story.append(tempstory)
        tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，奉天楼司祝"+str(atan.name)+"被册为"+str(atan.weifen)+"。\n"
        allstory.insert(0,tempstory2)
        if atan not in NPC_fz_list:
            NPC_fz_list.append(atan)
        juqingfei.append(atan)
    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子，皇上的旨意已经下来了，掖廷那边方才已经派人去奉天楼接了阿檀姑娘。"
    我 笑 "太好了，但愿阿檀往后余生，再也不要受相思之苦……"
    hide 我的宫女
    return

label 阿檀_出宫:
    "一晃，到了阿檀出宫的日子……"
    "往后，再也没有奉天楼的司祝阿檀。"
    "但，或许有一位善良无私的“神女阿檀”的故事将长久地流传下去……"
    $ my.lucky += 50
    return

label 阿檀_去世:
    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子，奴婢方才听外头的宫女说，奉天楼死了一个司祝……"
    我的宫女 "似乎就是阿檀……"
    我 "知道了……"
    hide 我的宫女
    if atan_end_1 < 6 or atan_end_2 == 1:
        我 思 "阿檀，我还是没能帮得了你。"
    return




label 楚欢:
    python:
        chuhuan.level = beifei
        chuhuan.xing = "楚"
        chuhuan.ming= "欢"
        chuhuan.name= "楚欢"
        chuhuan.hao = ""
        chuhuan.state = "寻常"
        chuhuan.age = 16
        chuhuan.family = "安平侯之女"
        chuhuan.familylevel = 1
        chuhuan.fatherduty = "文官"
        chuhuan.familylocation = "嫡女"
        chuhuan.health = 480
        chuhuan.beauty = 760
        chuhuan.yuanmao = chuhuan.beauty
        chuhuan.qizhi = 620
        chuhuan.meili = 500
        chuhuan.dance = 85
        chuhuan.book = 50
        chuhuan.cixiu = 50
        chuhuan.muzic =50
        chuhuan.battle = 0
        chuhuan.medic = 0
        chuhuan.like = 5
        chuhuan.love = 25

        chuhuan.exp = 0
        chuhuan.year = 0

        chuhuan.xinji = 700
        chuhuan.xinji1 = False

        chuhuan.xingge = "温婉"

        chuhuan.xingge1 = False
        chuhuan.meet = 0
        chuhuan.kids = []
        chuhuan.taihoulike = 30
        chuhuan.lucky = 20
        chuhuan.makelucky = 0
        chuhuan.Gongnv =[]
        chuhuan.qingxiang = 100
        chuhuan.shiqin = 0
        chuhuan.jinzu = 0
        chuhuan.friends = []
        chuhuan.foes = []
        chuhuan.face = "chuhuan"

        chuhuan.shou = 50
        chuhuan.tags = []
        chuhuan.tags.append(tags_jqf[2])
        chuhuan.tags.append(tags_xingge[4])
        chuhuan.tags.append(tags_limit_lucky[0])
        chuhuan.tags.append(tags_shuxing[3])
        chuhuan.meishu = {"初始":3,"一A":1,"一B":1,"二A":1,"二B":1,"三级":1,"大招":0}
        chuhuan.huashu =  {"初始":2,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
        chuhuan.anhai =  {"初始":3,"一A":2,"一B":0,"二A":2,"二B":2,"三级":1,"大招":0}
        chuhuan.fangyu = {"初始":2,"一A":0,"一B":1,"二A":1,"二B":1,"三级":1,"大招":0}

        chuhuan.yali = 0
        b = int(len(weifen_list)*0.4)
        chuhuan.exp = weifen_list[b][3] + (weifen_list[b][4]-weifen_list[b][3])*0.5
        Feizilevel_xuanxiu(chuhuan)
        chuhuan.cheng = chuhuan.hao + chuhuan.weifen
        chuhuan.tequan1 = -1
        chuhuan.tequan2 = -1
        chuhuan.story = []
        tempstory = "安平侯流落在外的女儿。\n"+str(nianhao)+str(year)+"年"+str(month)+"月，被皇帝接入宫中，册为"+str(chuhuan.weifen)+"。\n"
        chuhuan.story.append(tempstory)
        tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，安平侯之女"+str(chuhuan.name)+"被册为"+str(chuhuan.weifen)+"。\n"
        allstory.insert(0,tempstory2)
        if chuhuan not in NPC_fz_list:
            NPC_fz_list.append(chuhuan)
        juqingfei.append(chuhuan)
    return

label 楚欢_皇上烦心(place):
    $ chuhuan_1 = True
    皇上 "（默默叹了口气。）"
    皇上 "朕在想小时候的一件事，朕小时候做错了一件事情。"
    if place == "圣宸宫内":
        "在自己信任的人面前，他将自己心中的话语倾诉而出……"
    else:
        "略带犹豫，他仍然将心中的话向你倾诉而出……"
    scene black
    hide 皇帝
    皇上 "那个时候，朕还是一个小孩子。也是一个酷热的夏日，安平侯在家中设宴，父皇带朕一同前往。"
    皇上 "父皇同那些贵戚朝臣把酒言欢之时，朕也同安平侯家的几个小孩痛快地玩了一晚上。"
    皇上 "朕千不该万不该，不该许下那无法实现的约定。"
    我 思 "皇上……同谁人做了什么约定？"
    皇上 "（叹）"
    皇上 "是安平侯家的女儿。"
    皇上 "朕当时夸下海口，说攀上京城最高的峰顶，就能到月亮上去。旁的小孩都因朕的皇子身份而不敢有异……可偏偏她……"
    皇上 "她竟当场和朕吵了起来，朕心虚却又不服，约她一月后在西郊再聚，带她到山顶去，再上那月亮去。"
    menu:
        "真想不到皇上也曾有童趣无邪的时候":
            pass
        "谁都曾是孩童，这算不得什么":
            pass
    皇上 "可……就是这一句话，朕害了那女孩儿一辈子。"
    我 惊 "啊……"
    皇上 "一月后，朕未能赴约。而她……竟真的绕过安平侯府上下的耳目，偷偷跑了出去，在郊外苦守一夜未等到朕，却失了音讯……"
    我 "（！）"
    我 "她……"
    $ bg(place)
    show 皇帝
    皇上 "此事朕瞒了十年，每当想起那个女孩儿同朕争执时那坚持的目光，都会觉得心头悸动不安。"
    皇上 "朕对不起她，却又很怕再见到她……朕一直希望她仍好好活在这世上，一点也不比在安平侯府上差。"

    menu:
        "那是不可能的":
            皇上 "朕知道……那么小的女孩儿，独自一人去了山郊，便再也没了下落，怎么可能平安无事？"
            皇上 "朕不知道她到底经历了什么，可她活了下来，还回了安平侯府。"
            皇上 "就在上个月。"
        "那女孩儿定然无事":
            我 "皇上治国有方，天下太平，鲜少有歹徒作乱之事，那女孩儿应当无事罢。"
            皇上 "不知道算不上上是“无事”，但她的确活着，还回了安平侯府。"
            皇上 "就在上个月。"
    皇上 "安平侯想让她入宫为妃……说，是她自己的意思，她一直慕着朕……可朕觉着，她应是恨着朕才是。"
    皇上 "现下，实在不知道该如何是好。"
    menu:
        "接进宫来好好补偿她":
            $ chuhuan_2 = True
            我 "那姑娘也是安平侯上养尊处优长大的，在外流落了这么多年，想来也吃了不少苦。"
            我 "您将她接进宫来，往后好好补偿她罢。"
            皇上 "嗯……"
        "此事不妥":
            $ chuhuan_2 = False
            我 "这……安平侯家这姑娘流落在外这么多年，好不容易回来了，怎就急着送进宫来？"
            皇上 "朕也是觉得奇怪。"
            皇上 "安平侯同朕说起此事时还万般舍不得。"
            我 "他们好不容易团聚，若入了宫，以后便再难见上一面。"
            我 "这姑娘也是个可怜人儿，臣妾觉着，皇上还是等过些日子再给她另外指个门当户对的好人家罢。"
            皇上 "（颔首）是了，入了宫朕未必便能顾得上她。"
    if place != "圣宸宫内":
        皇上 "罢了，天色已晚，朕便回宫了。"
        皇上 "你也早些回去休息罢。"
        我 笑 "是。臣妾恭送皇上。"
        $ my.love += 2
    else:
        pass
    hide 皇帝
    return

label 楚欢_进宫:
    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子，奴婢听闻皇上已将那安平侯家的千金接进宫来了。"
    menu:
        我的宫女 "册的是……[chuhuan.weifen]的位份。"
        "知道了":
            pass
    hide 我的宫女
    return

label 楚欢_自动进宫:
    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子，奴婢听闻皇上命人将安平侯家的千金接进宫来了。"
    我的宫女 "册的是……[chuhuan.weifen]的位份。"
    我 "安平侯之女？"
    我 "（这么突然……）"

    hide 我的宫女
    return

label 楚欢_初次见面:
    if my.level <= chuhuan.level:
        $ zicheng = "本宫"
    else:
        $ zicheng = "嫔妾"

    menu:
        "我知道你的事情" if chuhuan_1 == True:
            楚欢 忧 "[my.cheng]知道我的事……"
            楚欢 "难道……"
            "你将之前皇帝的忧虑迟疑告诉了她。"
            楚欢 思 "皇上……"
            楚欢 常 "皇上如此信任[my.cheng]，真是让人羡慕。"
            楚欢 常 "我刚入宫不久，虽说昔日和皇上有些情分，可到底过了这么多年了，如今也生分了。"
            楚欢 常 "不过我看到后宫有这么多温柔解语的女子陪伴在他身边，也真为皇上感到高兴。"
        "既然入了宫，就得安分守己" if my.level < chuhuan.level:
            楚欢 忧 "啊……嫔妾惶恐。"
            楚欢 "嫔妾自小离开了侯府，不比寻常闺秀端庄得体，若嫔妾有什么错处，还请您多多担待。"
            楚欢 "嫔妾会安安分分地待在宫里，不给皇上添麻烦的……"
        "你这些年过得还好吧" if chuhuan_1 == True:
            楚欢 忧 "啊……[my.cheng]这话……"
            楚欢 "难道……"
            "你将之前皇帝的忧虑迟疑告诉了她。"
            楚欢 笑 "看来皇上很是信任[my.cheng]呢。"
            楚欢 常 "真好……"
            楚欢 "我这些年来过得很好，虽然幼时流落在外，但好歹衣食无忧，也算是平安长大。如今能入宫陪伴皇上，可以说是三生有幸了。"
            楚欢 笑 "而且后宫里有有这么多温柔解语的女子陪伴在皇上身边，实在是让人为皇上感到高兴。"
        "……":
            楚欢 忧 "[my.cheng]为什么不说话……是不喜欢我吗？"
            楚欢 "对不起……我知道这宫里很多人都讨厌我……"
            楚欢 "[my.cheng]，你喜欢陛下吗……"
            楚欢 思 "对不起，我不知道，早知道这样我就不会求父母送我入宫了……我只是想离陛下近一点……这些年，我好想他……"
    hide 楚欢
    return

label 楚欢_中秋宴会:
    $ bg("御花园")
    with fade
    $ chuhuan.meet += 1
    "宴会上——"
    show 楚欢
    楚欢 笑 "各位娘娘、妹妹，今日是欢儿向皇上求请举办这次中秋赏月会……因而，先在这里多谢各位赏脸。"
    "宴席上，阖宫嫔妃结伴而坐，除了位份较低的嫔妃不敢有所不敬之外，便无人再听她说话。"
    "楚欢尴尬地坐在席间，脸上的笑意逐渐凝结。"
    楚欢 忧 "欢儿初来乍到，若是有什么不周到的地方……"
    楚欢 思 "……"
    楚欢 思 "今日中秋宴会，各位不必拘束，欢儿也不多话，免得搅了大家的兴致。"
    hide 楚欢
    show 我的宫女
    我的宫女 "主子，这宫里头的人都不待见[chuhuan.cheng]呢……"
    我 "是啊……"
    hide 我的宫女
    menu:
        "同楚欢说话":
            if my.level <= chuhuan.level:
                $ zicheng = "本宫"
            else:
                $ zicheng = "嫔妾"
            show 楚欢
            楚欢 "[my.cheng]，你这是……"
            我 "方才[chuhuan.cheng]不是说不必拘束么？[zicheng]陪[chuhuan.cheng]说会儿话罢。"
            楚欢 笑 "那自然好。"
            hide 楚欢
            show 赵公公
            赵公公 "皇上驾到——"
            "众嫔妃" "恭迎皇上！"
            hide 赵公公
            show 楚欢 at you
            show 皇帝 at zuo
            楚欢 笑 "皇上不是说今日政务繁忙，无暇前来么？"
            皇上 "放心不下你独自操持家宴，所以过来看看。"
            皇上 "（看到你坐在她身边，便一颔首）倒是没叫朕失望。"
            皇上 "（在你身边坐下。）"
            楚欢 忧 "欢儿的确不擅长这些……不过为了皇上，欢儿会努力去学，再怎么也不能为皇上添麻烦呐。"
            皇上 "你把自己照顾好便是了。"
            楚欢 笑 "这些年来，虽然衣食无忧，但大多数时候都是欢儿自己照顾自己的，这您便不必担心了。"
            皇上 "（垂眸）嗯……"
            $ my.love += 2
        "和其他妃子一起孤立她":
            我 "（举杯小酌。）"
            show 赵公公
            赵公公 "皇上驾到——"
            "众嫔妃" "恭迎皇上！"
            hide 赵公公
            show 楚欢 at you
            show 皇帝 at zuo
            楚欢 笑 "皇上不是说今日政务繁忙，无暇前来么？"
            皇上 "放心不下你独自操持家宴，所以过来看看。"
            皇上 "（见她独自坐在席间，双眉间便显露出几分不悦）也罢。"
            皇上 "（同她坐下。）"
            楚欢 忧 "欢儿的确不擅长这些……不过为了皇上，欢儿会努力去学，再怎么也不能为皇上添麻烦呐。"
            皇上 "你把自己照顾好便是了。"
            楚欢 笑 "这些年来，虽然衣食无忧，但大多数时候都是欢儿自己照顾自己的，这您便不必担心了。"
            皇上 "（垂眸）嗯……"
            楚欢 常 "您看今夜的月色，好美。"
            楚欢 "欢儿因了您那一句话，还念着攀上那京城郊外的山顶，到月亮上去呢……"
            皇上 "欢儿，别说这些了。"
            楚欢 笑 "欢儿知道，您如今是九五之尊，要以天下为先。"
            楚欢 "是没机会陪欢儿去月亮上了……"
            楚欢 "您不陪欢儿，欢儿不想一个人去。您在哪里，欢儿就在哪里，好不好？"
            皇上 "……好。"
            $ chuhuan.love += 5
    "阖宫的妃子见皇上同[chuhuan.cheng]热络亲昵，心里多少有些不是滋味儿。"
    "在其中一些人的眼里，楚欢的到来无疑是一根恨不得除之而后快的刺。"
    hide 楚欢
    hide 皇帝

    return


label 楚欢_落水(fz, place):
    $ bgm("Bad")
    $ chuhuan_4 = True
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
    "？？？" "呜……"
    我 "（是谁在哭？）"
    $ gn = fz.Gongnv[0]
    show fz at zuo
    show gn at you
    妃子 "[gn.name]……眼下我信得过只有你了……"
    宫女 "[fz.cheng]……"
    妃子 "没人会相信我，没人能帮得了我。"
    妃子 "我该怎么办？难道就这么坐以待毙么？"
    宫女 "啊……"
    宫女 "（看到了你）啊，[my.cheng[0]]、[my.cheng]……"
    妃子 "（慌忙擦着眼泪，瞧着你的神色。）"
    menu:
        "上前询问":
            if my.level < fz.level:
                妃子 "啊，见过[my.cheng]。"
                我 "妹妹免礼。"
                $ wo = "姐姐"
                $ ni = "妹妹"
            else:
                我 "见过姐姐。"
                妃子 "（轻舒一口气）妹妹免礼吧。"
                $ wo = "妹妹"
                $ ni = "姐姐"
            我 惊 "[wo]方才听到[ni]在说……"
            妃子 "（慌张）[ni]什么也没说，多半是[wo]听错了。"
            我 常 "原是[wo]听岔了。"
            我 笑 "也罢，想来以我们的交情，也没必要藏着掖着不是？[ni]说无事，但便无事了。"
            妃子 "嗯……"
            妃子 "（却未能忍住，突然之间泣不成声）其实……其实[ni]眼下实在是不知道该怎么办了……"
            妃子 "[ni]很想告诉[wo]，可又怕[wo]牵连其中……怎么办……[ni]真的已经走投无路了……"
            我 惊 "（好端端地怎么突然……）"
            我 惊 "[ni]莫急，咱们慢慢说。"
            妃子 "好……[ni]信得过你，你若听了不信，便当[ni]没说过。"
            我 常 "（点头。）"
            妃子 "那[ni]便直说了……"
            "……"
            我 惊 "什么……你的意思是，[chuhuan.cheng]早已买通了你身边的几个宫女，只等伺机而动，要取你性命？"
            妃子 "如此已是千真万确，可[ni]却只是毫无办法……"
            妃子 "若非[gn.name]向[ni]禀报了那几人有异心，[ni]恐怕全然被蒙在股里。"
            妃子 "眼下若将她们调离，亦是打草惊蛇。若禀告皇上，却无凭无据，怕是难以令人信服……"
            宫女 "是奴婢亲眼瞧见了的，可奴婢人微言轻，放在皇上面前算不了什么证据，只能先告诉了主子，也好有所防范。但奴婢并未欺骗主子，奴婢也没必要借此污蔑[chuhuan.cheng]……"
            妃子 "（点头）是，[gn.name]是能信得过的。"
            妃子 "可……[ni]又能如何防范呢？"
            妃子 "若此事不是[gn.name]所说，[ni]尚且难以相信，毕竟[chuhuan.cheng]平日里那柔柔弱弱的样子，谁知道她会有这般的心思？"
            妃子 "[ni]又不曾得罪她，虽然偶尔能得皇上欢欣，但论恩宠，却也不是宫里头一份的啊！"
            menu:
                "[wo]也不太相信":
                    $ xingzi += 5
                "这背后或许有什么误会":
                    $ xingzi -= 5
                "想办法搜集证据吧":
                    pass
            妃子 "（抽泣。）"
            妃子 "罢了罢了，说出来到底还是舒服些了……至于该怎么对付她，[ni]如今也没有头绪，先走一步算一步吧……"
            宫女 "（对不住了，主子。）"
            我 惊 "？！"
            $ bg(place)
            with hpunch
            妃子 "啊！"
            scene black
            妃子 "救命！"
            宫女 "主子，奴婢这就来救你！"
            "一切发生得太过突然，以至于你一时都未能有所反应。"
            "你只能看到[fz.cheng]整个人突然向后倒去，在落入水中的最后一刻，伸出的手{w}终于没能碰触到你。"
            $ bg(place)
            with hpunch
            我 惊 "这……"
            "宫人" "快来人！来人啊！[fz.cheng]落水了！"
            scene black
            with fade
            "……"
            $ bg("圣宸宫内")
            show 皇帝
            with fade
            menu:
                我 "皇上……"
                "[fz.cheng]怎么样了？":
                    $ taidu += 2
                "皇上脸色好差":
                    $ xingzi -= 5
            皇上 "太医还在救治[fz.cheng]，但，希望很渺茫了。"
            皇上 "那个宫女已经没了。"
            menu:
                "（悲痛万分）":
                    $ taidu += 3
                    我 泪 "[fz.cheng]一定要没事……"
                    皇上 "（叹了口气）朕知道，你和她交情不错，是吗？"
                    我 "是……"
                    皇上 "当时到底发生了什么？"
                "皇上在怀疑臣妾吗？":
                    $ xingzi += 5
                    皇上 "朕不是怀疑。"
                    皇上 "朕也不想怀疑。"
                    皇上 "朕知道你不想被怀疑，但也希望[fz.cheng]能求得公道，对吗？"
                "……":
                    $ taidu -= 5
                    皇上 "根据将[fz.cheng]救起的宫人的说法，当时只有你和你的宫女在场，对吗？"
            我 思 "事出突然，臣妾也不知为何她突然便……"

            menu:
                我 "（她说[chuhuan.cheng]同她的宫人暗通款曲，莫非……）"
                "说出[fz.cheng]发现的事":
                    $ chuhuan_5 = 1
                    皇上 "（蹙眉）好端端地怎么提起[chuhuan.cheng]来了？"
                    皇上 "况且，她的为人……"
                    menu:
                        "那臣妾的为人不可信么？":
                            $ xingzi += 5
                            皇上 "朕不是这个意思。"
                            我 "皇上要是相信臣妾，不如试着顺着[chuhuan.cheng]那边查下去，兴许真的会有所牵扯。"
                            我 "当然，臣妾知道自己也有很大的嫌疑，皇上要查便查，相信最后会还臣妾一个清白。"
                            皇上 "好。"
                        "但这实在蹊跷":
                            $ xingzi -= 5
                            皇上 "既然如此，[chuhuan.cheng]和你，朕都会去查的。"
                            皇上 "但愿此事与你无关……"
                            皇上 "也与她无关……唉。"
                        "无话可说":
                            $ taidu -= 5
                            皇上 "罢了……朕按照你说的查一查便是了。"
                            皇上 "但对于你，朕也是要查的。"
                            皇上 "朕愿意相信你，但也要让其他人信服，否则往后难免有人在背后说三道四。"
                            我 "臣妾但凭皇上做主。"
                    hide 皇帝
                    show 皇帝 at zuo
                    皇上 "（沉思片刻）去传[chuhuan.cheng]。"
                    show 赵公公 at you
                    赵公公 "是！"
                    hide 赵公公
                    皇上 "去屏风后面。"
                    我 "是。"
                    "片刻后……"
                    show 楚欢 at you
                    楚欢 "欢儿参见皇上。"
                    皇上 "嗯，坐吧。"
                    楚欢 "皇上怎的突然召欢儿过来？"
                    皇上 "倒也没什么，就是这后宫里头事情啊……扰得朕心烦。"
                    皇上 "也只有你，能让朕觉得舒心了。"
                    楚欢 笑 "皇上……"
                    楚欢 忧 "[fz.cheng]的事情欢儿听说了，如今情况可明朗了？"
                    皇上 "太医说应当没什么大碍，晚些时候便能醒来了，只是身子受损，得花些时日才能休养过来，往后得小心些了。"
                    楚欢 盯 "（？！）"
                    楚欢 常 "[fz.cheng]真是吉人自有天相，也是陛下您的福泽庇佑，才让她化险为夷。"
                    皇上 "只是她这次落水实在蹊跷，不过等她醒来，多半便也知晓事情的前因了。"
                    楚欢 "欢儿听说当时只有[my.cheng]在场，该不会是……"
                    楚欢 "不，[my.cheng]决计不是那种人，况且她同[fz.cheng]交情甚好，虽然[fz.cheng]得您欢欣，但却也是比不上她的，她不必下手如此狠毒……"
                    皇上 "是啊，朕也觉得应当不是她。总之，等[fz.cheng]和当时立即下去救她的宫女醒了，便一切都了然了。"
                    楚欢 盯 "（那个宫女也还活着？！）"
                    皇上 "怎么了，你怎么表情有些怪怪的？"
                    楚欢 "没、没什么……"
                    皇上 "……"
                    皇上 "你应当有话对朕说，不是吗？"
                    楚欢 忧 "欢儿不明白您的意思呀……"
                    楚欢 忧 "（不敢看他）难道这事还和欢儿有关系么？"
                    楚欢 盯 "欢儿今日一直都在[chuhuan.qinju]，[chuhuan.palace]的宫人都能为欢儿作证，怎么可能跑到[place]去了呢？"
                    楚欢 怒 "难、难道是有人信口胡说了些什么……"
                    皇上 "朕倒是不明白你的意思了。"
                    皇上 "是朕误会了什么？还是你误会了什么？"
                    楚欢 忧 "啊……"
                    楚欢 思 "欢儿……"
                    皇上 "罢了，朕现下没心思再同你细说，反正等[fz.cheng]和她的宫女醒了，便知道真相了。"
                    hide 楚欢
                    show 赵公公 at you
                    赵公公 "皇上请恕罪，[fz.cheng]醒了。"
                    皇上 "（眼神一亮）醒了？状况可还好？"
                    赵公公 "嗯……倒是挺精神的，吵着要皇上替她做主呢……"
                    皇上 "咳……此事竟真是有人意欲加害她么？朕绝不姑息！"
                    赵公公 "皇上是要现下去看娘娘还是等娘娘先自个儿安静下来？"
                    皇上 "朕自然是现在就要去。"
                    赵公公 "是，不过娘娘受了惊吓，这会儿哭闹着呢，还说着什么要您严惩[chuhuan.cheng]……"
                    皇上 "什么？！"
                    hide 赵公公
                    show 楚欢 at you
                    楚欢 怒 "赵公公，此事与本宫何干，你可不要在皇上跟前胡说！"
                    hide 楚欢
                    show 赵公公 at you
                    赵公公 "哎哟，您可折煞了，奴才哪儿敢呢……这不是劝皇上先别去嘛。"
                    赵公公 "皇上，您看……"
                    皇上 "哼！"
                    hide 赵公公
                    show 楚欢 at you
                    楚欢 忧 "皇上……"
                    楚欢 "此事、此事真不知道如何会与欢儿有关，欢儿真的好委屈……"
                    皇上 "若和你无关，便无需解释。"
                    皇上 "等朕同[fz.cheng]说过了话再来问罪，你先退下吧。"
                    楚欢 怒 "皇上！"
                    皇上 "还有何事？"
                    楚欢 怒 "欢儿只想问您一句，您从一开始就在怀疑欢儿了，是吗？"
                    楚欢 "这到底是为什么？"
                    皇上 "朕怀疑你？"
                    皇上 "不，是你自己马脚露得太早了。"
                    楚欢 "……"
                    楚欢 笑 "呵……"
                    皇上 "所以，你现在还有什么话想对朕说的吗？"
                    楚欢 笑 "皇上果然是皇上，除了您，谁还会想到我身上呢？"
                    楚欢 "是[my.name]，对么？"
                    楚欢 "是她开了口，说了我和[fz.cheng]的事，对么？"
                    皇上 "朕现在不想回答这些。"
                    皇上 "朕也不急着问罪，眼下朕要去看看[fz.cheng]。"
                    楚欢 "呵……您真的很爱她，很信任她呢。"
                    楚欢 思 "可是，凭什么……"
                    楚欢 "她嫌疑那般明显，只需要三言两语，便能让你信了。"
                    楚欢 "而我什么也没做，你便疑了。"
                    皇上 "你什么都没做吗？"
                    楚欢 常 "我……"
                    楚欢 "是，我做了，可我没让你知道。"
                    楚欢 "你不该知道的。"
                    楚欢 "[guoxing][emperor]。"
                    皇上 "你这是大不敬！"
                    楚欢 "那换了[my.cheng]呢？"
                    皇上 "她不会这样对朕说话。"
                    楚欢 "是啊，她不会。"
                    楚欢 "因为她不配！她不敢！"
                    楚欢 怒 "只有我……只有我……"
                    楚欢 怒 "你本该喜欢我，你本该疼爱我的！"
                    楚欢 "因为你，我受了那么多苦，我什么都没了！"
                    楚欢 "你坐在这九五之尊的位置上，却什么也不肯偿还我！"
                    皇上 "从前的事，是朕欠你，你想要朕怎样偿还？"
                    皇上 "要让朕看着你祸乱后宫，枉顾人命？"
                    皇上 "那朕岂不是欠的更多！"
                    楚欢 "那都是你该的！"
                    楚欢 "你本应该爱我，给我我想要的一切！"
                    楚欢 "我进宫来，不是看你和其他女人卿卿我我的，而你，却连一个正眼都不肯给我？"
                    楚欢 "我以为你可以补偿我，把所有的宠爱都给我，你会捧着我，护着我，可以把我过去十几年来遗失的幸福都弥补回来……"
                    楚欢 "可惜我错了，原来你根本没打算弥补我。"
                    楚欢 "我入宫时，她们如临大敌，我遭人冷眼，你未置一词。这么多年，什么荣华、什么恩宠……我竟与那些人并无分别！"
                    楚欢 "[guoxing][emperor]，我恨透了了你，恨透了你喜欢的那些女人。"
                    楚欢 "明明她们都不配……她们在我面前算什么？"
                    楚欢 "她们从你身上得到的一切都应该属于我，她们根本不配得到这些！"
                    皇上 "疯子！"
                    楚欢 "是啊，我疯了……"
                    楚欢 "一个千金大小姐，经历了那些事情，却还苟活着，怎么会不疯呢……"
                    皇上 "你说，你过得很好。"
                    楚欢 笑 "所以，你就不愧疚啦？"
                    楚欢 "哈哈哈……哈哈哈……"
                    楚欢 "我可惨啦。"
                    楚欢 "惨得就像是谁都可以踩死的一只蚂蚁。"
                    楚欢 "就这样，我还是什么都得不到呢……"
                    楚欢 思 "你真的可有够无情的……我很想这么说，可是看你和[my.cheng]在一起的时候，你真的一点也不无情呢。"
                    皇上 "楚欢……"
                    楚欢 "你不必去见[fz.cheng]了。"
                    楚欢 常 "是我做的，全都是我。"
                    楚欢 "我买通了[gn.name]，让她找机会在[fz.cheng]和[my.cheng]单独在一起的时候下手，嫁祸给[my.cheng]。"
                    楚欢 "我只是想除掉你喜欢的女人，因为她抢走了原本应该属于我的东西。"
                    皇上 "属于你的东西。"
                    皇上 "你是觉得朕喜欢你吗？"
                    楚欢 "你不喜欢也必须喜欢。"
                    楚欢 "就算对我仅仅是愧疚，也只能愧疚，你的心里除了对我的愧疚以外已经容不下其他任何感情了。"
                    皇上 "你已经疯了。"
                    皇上 "朕不想和你多说什么。"
                    皇上 "来人，送[chuhuan.cheng]回宫，听候发落。"
                    "宫人" "是。"
                    楚欢 笑 "皇上，你难道不想承认，你欠了我很多么？"
                    皇上 "是有亏欠。朕的补偿，就是顺应你或是你家族的心意接你进宫。"
                    皇上 "你若安分守己，朕能一辈子护你无忧。"
                    楚欢 "无忧？"
                    楚欢 怒 "你看我无忧了么？"
                    皇上 "是你欲求不满，自寻烦恼。"
                    皇上 "你的亏欠，不是无可填补。朕的补偿，自然也不是任你索求。"
                    楚欢 "好。"
                    楚欢 常 "原来……"
                    楚欢 "是欢儿痴心妄想了。"
                    楚欢 "欢儿……告退。"
                    hide 楚欢
                    hide 皇帝
                    show 皇帝
                    皇上 "……"
                    我 "皇上……"
                    皇上 "竟然真的是她……"
                    menu:
                        "皇上打算如何处置？":
                            $ xingzi += 5
                            皇上 "嗯……"
                        "先去看看[fz.cheng]吧":
                            $ xingzi -= 5
                            皇上 "唉……"
                    皇上 "楚欢的事情，朕还需要将前因后果调查清楚。"
                    皇上 "至于[fz.cheng]……"
                    if my.lucky + fz.lucky < 100:
                        皇上 "朕不过是试探她罢了。"
                        我 惊 "？！"
                        $ Killfz(fz)
                        $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"溺水而亡。\n"
                        $ allstory.insert(0,tempstory2)
                        $ tempstory =str(year)+"年"+str(month)+"月，溺水而亡。\n"
                        $ fz.story.append(tempstory)
                        皇上 "[fz.cheng]已经去了。"
                        我 "怎么会这样……"
                    else:
                        皇上 "方才那些话，不过是试探。"
                        我 惊 "？！"
                        皇上 "太医说她身子受损，一时半会儿不会醒来。"
                        皇上 "等醒过来了，也需要静养。现下，还是让太医为她再做诊治吧。"
                        我 "[fz.cheng]没事便好……"
                        $ fz.health = fz.health*0.5 - 100
                        $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"不慎落水。\n"
                        $ allstory.insert(0,tempstory2)
                        $ tempstory =str(year)+"年"+str(month)+"月，不慎落水，身子受损。\n"
                        $ fz.story.append(tempstory)
                    $ AP -= 1
                    $ timenum += 1
                    jump 寝居界面
                "沉默不语":
                    $ chuhuan_5 = 2
                    皇上 "这样的说法，即便朕相信你，却也不能让其他人信服。"
                    皇上 "看来朕得好好调查了。"
                    menu:
                        "皇上不信我":
                            $ xingzi += 5
                            皇上 "这也是为了证明你的清白，明白吗？"
                        "臣妾相信皇上能给臣妾一个清白":
                            $ xingzi -= 5
                        "无话可说":
                            $ taidu -= 5
                    皇上 "来人，送[my.cheng]回宫，在事情查明之前，任何人未经特许不得出入[my.qinju]。"
                    $ my.tags.append(tags[4])
                    $ my.tags.append(["禁足一月",0,""])
                    $ Killfz(fz)
                    $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"溺水而亡。\n"
                    $ allstory.insert(0,tempstory2)
                    $ tempstory =str(year)+"年"+str(month)+"月，溺水而亡。\n"
                    $ fz.story.append(tempstory)
                    $ chuhuan_die = fz
                    皇上 "别让朕失望。"
                    $ AP -= 1
                    $ timenum += 1
                    jump 寝居界面
        "假装没看见":

            $ taidu -= 5
            我 思 "（虽然[fz.cheng]同我交情不浅，不知道她所说的是所为何事，但眼下还是别蹚这浑水了。）"
            我 常 "（看向远处）[my.Gongnv[0].name]，陪本宫去那边走走。"
            妃子 "……（松了一口气。）"
            宫女 "（主子，对不住了。）"
            妃子 "啊！？"
            我 惊 "（什么声音？）"
            宫女 "来人啊！来人啊！[fz.cheng]落水了！！"
            scene black with fade
            "宫人们七手八脚地将[fz.cheng]救了起来。"
            "然而等到太医来的时候，已经回天乏术了。"

            $ AP -= 1
            $ timenum += 1
            $ bg("寝居")
            我 思 "……"
            show 我的宫女
            我的宫女 "主子，您还好吧？"
            我 "[fz.cheng]她……"
            我 "唉。"
            if my.xinji >= 500:
                我 "（实在蹊跷……）"
            "因目睹这一场意外，压力大量上升。"
            $ my.yali += 50
            $ Killfz(self = fz)
            $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，"+str(fz.hao)+(fz.weifen)+str(fz.name) +"溺水而亡。\n"
            $ allstory.insert(0,tempstory2)
            $ tempstory =str(year)+"年"+str(month)+"月，溺水而亡。\n"
            $ fz.story.append(tempstory)
            jump 寝居界面


label 楚欢_女主被罚(fz):
    $ bg("寝居")
    show 我的宫女
    我的宫女 "主子……方才掖廷的人来了，说咱们[my.qinju]的禁足已经解了。"
    我的宫女 "不过掖廷调查无果，[fz.cheng]落水的罪名还是落在咱们头上了……"
    我 思 "本宫知道了。"
    我的宫女 "主子……我们好冤啊。"
    $ tempstory2 ="【大事】"+str(year)+"年"+str(month)+"月，经查："+str(fz.hao)+(fz.weifen)+str(fz.name) +"落水身亡一案，为"+str(my.hao)+(my.weifen)+str(my.name) +"所为。\n"
    $ allstory.insert(0,tempstory2)
    $ tempstory =str(year)+"年"+str(month)+"月，不慎致使"+str(fz.hao)+(fz.weifen)+str(fz.name) +"落水身亡。\n"
    $ fz.story.append(tempstory)
    hide 我的宫女
    if my.level <= 0:
        $ my.level = 0
    elif my.level  >= beifei:
        $ my.level = beifei - 1
    $ tempnum = yuanweifen[my.level][3]-yuanweifen[my.level+1][3]
    $ my.exp -= int(2*tempnum)
    $ my.love -= fz.love
    if tags[4] in my.tags:
        $ my.tags.remove(tags[4])
    return

label 楚欢_最后一面:
    $ bg("妃嫔寝居内")
    $ chuhuan_5 = 0
    show 楚欢
    楚欢 "[my.cheng]愿意前来，实在是欢儿三生有幸呢。"
    menu:
        "有话快说":
            $ xingzi += 5
            $ tempnum = 1
            楚欢 笑 "呵……"
            楚欢 "原来[guoxing][emperor]喜欢你这样的，亏得我处处柔弱示人，到头来……却连你的一根手指头都比不上。"
            我 "你心里的虚伪，皇上他未必看不出来。"
            楚欢 "你说是，那自然是了，这后宫里还有谁比你更懂他呢？"
            楚欢 "我是全然不懂的……"
            楚欢 "不过，如今也没必要懂了。"
        "你何苦至此":
            $ xingzi -= 5
            $ tempnum = 2
            楚欢 盯 "你当然不会懂得。"
            楚欢 "如果你是我，你兴许比我现在更加狠毒，更加不堪……不，你或许根本活不下来。"
            我 "我很同情你，但这不是你无视纲纪、肆意妄为的理由。"
            我 "你是很可怜，可她又做了什么……"
            我 "就因为身在后宫，是皇上的妃嫔？就因为你的不幸，就让其他人也因你不幸吗？"
            楚欢 笑 "哈……"
    楚欢 思 "……"
    楚欢 常 "[my.cheng]……"
    我 常 "罢了，如今皇上尚未将你定罪，我也不便多言。"
    我 "你为何要见我？"
    楚欢 笑 "难道不是[my.cheng]有话问我么？"
    楚欢 "比如，她到底是怎么落水的？"
    if my.xinji >= 500:
        我 "你买通了她的宫女，不是么？就连她唯一觉得信得过的其实也已经在为你卖命了……"
        楚欢 笑 "不愧是[my.cheng]呐。"
        楚欢 "这也是为什么我不直接向你下手……不过，这一招竟然仍然未能除掉你。"
        楚欢 思 "罢了，并非我考虑不周，也并非你料事如神。"
    else:
        楚欢 "我以为，以[my.cheng]的本事，应当猜不出我都做了些什么。"
        我 "……"
        楚欢 笑 "她跟你说了什么？"
        我 怒 "你买通了她身边的宫人，想要伺机动手。"
        楚欢 "可惜，发现这一切的那个宫女，也已经被我收买了。"
        我 "什么？！"
        楚欢 "你果然没有想到呢。"
        楚欢 思 "原本如今待罪的人，应当是你……"
    楚欢 "只是我没有想到，[guoxing][emperor]会这样信任你……"
    楚欢 怒 "这份信任……应该属于我！"
    楚欢 "他怎么可以把属于我的东西都给了你！"
    楚欢 "你们对他来说，怎么可能比我重要？我可是让他愧疚一生的人！"
    我 "（她简直就是个不可理喻的疯子……）"


    with hpunch
    menu:
        "{color=#FF0000}楚欢向你发起了争锋！！":
            hide 楚欢
            $ battle_list = []
            $ battle_list_fz = []
            $ battle_list_my = []
            $ waitfz = False
            if tempnum == 1:
                nvl clear
                旁白 "特殊争锋说明：\n楚欢处于绝境之中，初始技能增加3。\n根据我方情绪，初始技能减少3。\n争锋结束时分数高于楚欢方可取胜！\n"
                nvl clear
                $ myscore = 100
                $ mybaolv = round(my.lucky)
                $ fzbaolv= round(chuhuan.lucky)
                $ fzscore = 100
                if yxxiao in my.Gongnv and yxxiao.like > 100:
                    $ fzscore -= int((yxxiao.like - 100)*0.5)
                $ mybaoji = 1+my.level*0.01+my.familylevel*0.01
                $ fzbaoji = 1+chuhuan.level*0.01+chuhuan.familylevel*0.01
                python:
                    if my.level == 0: 
                        paishu = 6
                    elif diwei(my)==1: 
                        paishu = 5
                    elif diwei(my)==3:
                        paishu = 3
                    else:
                        paishu = 4
                    if havetag("能言善辩",my) == True :
                        paishu = paishu + 1
                    if havetag("不善言辞",my) == True :
                        paishu = paishu - 1
                    paishu -= 3
                    if paishu <= 0:
                        paishu = 0
                    mypais = []
                    while len(mypais) < paishu:
                        suijipai = renpy.random.choice(paikucodes)
                        mypais.append(suijipai)
            else:

                nvl clear
                旁白 "特殊争锋说明：\n楚欢处于绝境之中，初始状态增加一倍。\n根据我方情绪，初始技能增加3，但初始状态减半。\n争锋结束时分数高于楚欢方可取胜！\n"
                nvl clear
                $ myscore = 50
                $ fzscore = 200
                if yxxiao in my.Gongnv and yxxiao.like > 100:
                    $ fzscore -= int((yxxiao.like - 100)*0.5)
                $ mybaolv = round(my.lucky)
                $ fzbaolv= round(fz.lucky)
                $ mybaoji = 1+my.level*0.01+my.familylevel*0.01
                $ fzbaoji = 1+fz.level*0.01+fz.familylevel*0.01
                python:
                    if my.level == 0: 
                        paishu = 6
                    elif diwei(my)==1: 
                        paishu = 5
                    elif diwei(my)==3:
                        paishu = 3
                    else:
                        paishu = 4
                    if havetag("能言善辩",my) == True :
                        paishu = paishu + 1
                    if havetag("不善言辞",my) == True :
                        paishu = paishu - 1
                    paishu += 3
                    mypais = []
                    while len(mypais) < paishu:
                        suijipai = renpy.random.choice(paikucodes)
                        mypais.append(suijipai)
            python:
                if chuhuan.level == 0: 
                    paishu = 6
                elif chuhuan.qinjunum == 1: 
                    paishu = 5
                elif diwei(chuhuan) == 3:
                    paishu = 3
                else:
                    paishu = 4
                if tempnum == 1:
                    paishu += 3
                    templist = [7,8,10,10,10,10]
                else:
                    templist = [7,8,9,9,9,9,10]
                fzpais = []

                while len(fzpais) < paishu:
                    suijipai = renpy.random.choice(templist)
                    fzpais.append(suijipai)


            "进入争锋！"
            call screen battle(fz = chuhuan)
            show 楚欢
            if myscore > fzscore:
                if yxxiao in my.Gongnv:
                    $ tempnum = (myscore - fzscore)*0.1
                    if tempnum >= 10:
                        $ tempnum = 10
                    $ yxxiao.like += tempnum + 5
                    if yxxiao.like >= 200:
                        $ yxxiao.like = 200
                楚欢 怒 "……"
                楚欢 思 "哼……"
                我 "所以，[chuhuan.cheng]你还有什么话说？"
                楚欢 "没有。"
                楚欢 "我无话可说。"
                楚欢 "从一开始就错了。"
                楚欢 "凡我所求，皆不可得。"
                楚欢 "凡我所避，纷至而来。"
                楚欢 "哪怕是片刻的欢喜，上天也不肯施舍给我……"
                menu:
                    "了结她" if poison03 in kufang and my.qingxiang > 70:
                        $ xingzi+= 10
                        $ taidu -= 10
                        $ liangxin -= 10
                        我 "[my.Gongnv[0].name]，替[chuhuan.cheng]备一杯好酒，本宫亲自送她上路。"
                        楚欢 笑 "[my.cheng]也不怕脏了自己的手？"
                        我 "与此脏了本宫的手，本宫更不想在心里留一根刺。"
                        我 "[chuhuan.cheng]，你说，是么？"
                        楚欢 "是啊……"
                        scene black
                        with fade
                        "片刻后……"
                        "亲眼看到楚欢喝下鸩酒，你才离开了[chuhuan.qinju]。"
                        $ bg("妃嫔寝居内")
                        show 楚欢 血
                        with fade
                        楚欢 血 "可笑……可笑啊……"
                        $ my.lucky -= 10
                        $ kufang.remove(poison03)
                        $ bg("寝居")
                        with fade
                        show 我的宫女
                        我的宫女 "主子，[chuhuan.palace]那边已经传了消息，说[chuhuan.cheng]没了……"
                        我 "皇上可知道了？"
                        我的宫女 "皇上叫掖廷的人瞒下实情，叫人记下是隐疾发作去了的。"
                        我 "嗯，妃嫔自戕是大罪，皇上也是顾念着安平侯那边。"
                    "离开":
                        我 怒 "上天不肯给与你的，你也不该从旁人身上索取。"
                        楚欢 常 "你这高高在上的嘴脸可真让我恶心得想吐。"
                        楚欢 笑 "不过，反正也不会再见到你了。"
                        hide 楚欢
                        $ bg("寝居")
                        with fade
                        show 我的宫女
                        我的宫女 "主子，[chuhuan.palace]那边已经传了消息，说[chuhuan.cheng]服毒自尽了……"
                        我 "（倒吸了一口凉气，但却并不感到意外。）"
                        我 "皇上可知道了？"
                        我的宫女 "皇上叫掖廷的人瞒下实情，叫人记下是隐疾发作去了的。"
                        我 "嗯，妃嫔自戕是大罪，皇上也是顾念着安平侯那边。"
                "获得了5个技能点。"
                $ my.skillcosts += 5

                $ tempstory = str(year)+"年"+str(month)+"月，因身患隐疾发作，病故。\n"
                $ tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(chuhuan.hao)+str(chuhuan.weifen)+str(chuhuan.name)+ "因身患隐疾发作，病故。\n"


                $ Killfz(chuhuan)
                $ AP -= 1
                $ timenum += 1
                jump 寝居界面
            else:
                楚欢 "你也不过如此……"
                楚欢 "咳咳……"
                with hpunch
                楚欢 血 "呵呵……"
                我 惊 "（她这是……）"
                "宫人" "皇上到——"
                show 楚欢 血 at zuo
                show 皇帝 at you
                皇上 "楚欢，你这是？！"
                楚欢 "皇上……欢儿罪大恶极……"
                楚欢 "罪该万死……"
                楚欢 "是[my.cheng]替欢儿解脱，不怪她……"
                楚欢 "毕竟……这后宫里，谁都不待见欢儿……如今……终于可以离……"
                皇上 "欢儿！"
                皇上 "你做了什么……"
                楚欢 "[my.cheng]给欢儿准备了一杯鸩酒，欢儿本有话想对您说，想等您来了再喝……"
                楚欢 "[my.cheng]不给欢儿机会，不过也没关系……还是赶上……能见您一面……"
                皇上 "太医……传太医！"
                楚欢 "不用了……皇上……欢儿能死在你的面前，已经心满意足……"
                楚欢 "欢儿做错了太多……但如果成了死人，或许能得到您的原谅……吗……"
                皇上 "……"
                皇上 "朕也辜负了你太多。"
                皇上 "若不是朕，这一切本不该发生……"
                楚欢 "您能说一句……爱我么……"
                皇上 "……"
                皇上 "朕爱你。"
                楚欢 "啊……"
                楚欢 "真好……"
                hide 楚欢
                皇上 "[chuhuan.cheng]！"
                我 "皇上……"
                皇上 "你！{w}你何必多此一举……"
                皇上 "她有错，朕自会惩处。你为何偏要这般？"
                我 "臣妾……"
                皇上 "够了，你这样让朕如何向安平侯交待？"
                show 太医令 at zuo
                太医令 "微臣参见皇——"
                皇上 "快，太医令，快看看[chuhuan.cheng]怎么样了？"
                太医令 "（触其鼻息）这……"
                太医令 "（摇头）皇上节哀。"
                皇上 "唉……"
                hide 太医令
                我 "真的不是臣妾……"
                皇上 "来人，传朕旨意，[my.cheng]禁足三月，无诏不得出。"
                皇上 "回去好好思过。"
                皇上 "此事朕会瞒下，但朕不能不发落你。"
                皇上 "你太让朕失望了……"
                $ my.exp -= chuhuan.exp
                $ my.love -= chuhuan.love
                $ tempstory = str(year)+"年"+str(month)+"月，因身患隐疾发作，病故。\n"
                $ tempstory2 = "【讣告】"+str(year)+"年"+str(month)+"月，"+ str(chuhuan.hao)+str(chuhuan.weifen)+str(chuhuan.name)+ "因身患隐疾发作，病故。\n"


                $ Killfz(chuhuan)
                $ my.tags.append(["禁足三月",0,""])
                $ AP -= 1
                $ timenum += 1
                jump 寝居界面



init python:
    def maketaoning(taoning):
        global taoning_xuanxiu
        taoning.level = beifei
        taoning.xing = "陶"
        taoning.ming= "凝"
        taoning.name= "陶凝"
        taoning.hao = ""
        taoning.state = "寻常"
        taoning.age = 16
        taoning.family = "六品文官庶女"
        taoning.familylevel = 6
        taoning.fatherduty = "文官"
        taoning.familylocation = "庶女"
        taoning.health = 730
        taoning.beauty = 350
        taoning.yuanmao = taoning.beauty
        taoning.qizhi = 520
        taoning.meili = 445
        taoning.dance = 30
        taoning.book = 40
        taoning.cixiu = 60
        taoning.muzic =30
        taoning.battle = 0
        taoning.medic = 0
        taoning.like = 15
        taoning.love = (taoning.beauty +taoning.meili+taoning.qizhi)/250 + taoning.familylevel/4
        taoning.taihoulike = (taoning.beauty +taoning.meili+taoning.qizhi)/250 - taoning.familylevel/4
        
        taoning.exp = 0
        taoning.year = 0
        taoning.xinji = 920
        taoning.xinji1 = False
        taoning.xingge = "安静"
        taoning.xingge1 = False
        taoning.meet = 0
        taoning.kids = []
        taoning.lucky = 20
        taoning.makelucky = 0
        taoning.Gongnv =[]
        taoning.qingxiang = 40
        taoning.shiqin = 0
        taoning.jinzu = 0
        taoning.friends = []
        taoning.foes = []
        taoning.face = "taoning"
        
        taoning.shou = 60
        taoning.tags = []
        taoning.tags.append(tags_jqf[3])
        taoning.meishu = {"初始":1,"一A":0,"一B":0,"二A":0,"二B":0,"三级":0,"大招":0}
        taoning.huashu =  {"初始":3,"一A":2,"一B":3,"二A":0,"二B":2,"三级":2,"大招":0}
        taoning.anhai =  {"初始":3,"一A":3,"一B":3,"二A":3,"二B":1,"三级":0,"大招":0}
        taoning.fangyu = {"初始":1,"一A":1,"一B":1,"二A":1,"二B":1,"三级":0,"大招":0}
        Creat_Males(taoning,how = 0)
        taoning.father.duty = "文官"
        taoning.father.zhong = 90
        taoning.father.neng = 30
        taoning.father.exp = 0
        
        
        taoning.yali = 0
        a = int(len(weifen_list)*0.5)
        taoning.exp = weifen_list[a][3] - weifen_list[a+1][3]*7*0.2 + taoning.beauty/10 + taoning.qizhi/30 + taoning.meili/30 + taoning.love*2 + renpy.random.randint(-20, 30)
        if taoning.exp < 0:
            taoning.exp = 0
        else:
            pass
        taoning.cheng = taoning.hao + taoning.weifen
        taoning.tequan1 = -1
        taoning.tequan2 = -1
        
        juqingfei.append(taoning)
        taoning_xuanxiu = False

label 陶凝_初次见面:
    我 "本宫还记得你入宫前……"
    陶凝 "嫔妾入宫前可曾和娘娘有什么渊源？"
    我 笑 "当时你在宫中跟丢了教引的嬷嬷，还是本宫的宫女替你指了去路了。"
    陶凝 "啊……当时那位竟是娘娘的宫女。"
    "只见陶凝退后一步，竟朝你行了跪拜的大礼。"
    陶凝 "陶凝愚钝，若非娘娘的宫女相助，恐怕当时便以秀女失仪之名被逐出宫去，颜面尽失。娘娘对陶凝来说，是有大恩之人。"
    我 "好了，起来罢。"
    我 "本宫也想问你，那日你回了储秀宫，可有被嬷嬷责罚？"
    陶凝 "只是思过一日，并无重责。"
    我 "那便好……"
    陶凝 笑 "对嫔妾来说自然是极好。既保住了颜面，还有幸入选进宫，能与娘娘结缘，得您的照拂。"
    $ Feizilike_Up(taoning,10)
    return


label 偶遇陶凝_1(fz):
    if fz != my:
        show fz at zuo with dissolve
        show 陶凝 笑 at you with dissolve
        妃子 "噢……你是那新进入宫的陶氏。"
        陶凝 常 "是……嫔妾见过[fz.cheng]。今日良辰好景，您若有兴致，嫔妾陪您走走罢？"
        if fz.xingge == "娇纵" or fz.xingge == "势利":
            妃子 "本是兴致好的，可瞧见了些寒酸子气。就像是在满汉全席上瞧见了一只苍蝇，叫人倒胃口。"
            陶凝 思 "嫔妾眼拙，可没见着什么苍蝇。您若不喜，叫宫人吆了去便是。"
            妃子 "[taoning.cheng]，你是真不懂，还是装不懂啊？"
            妃子 "苍蝇就是苍蝇，烦人，就算停在本宫的箸子上，那也变不成蝴蝶呀。"
            陶凝 思 "您要真和苍蝇说话，它也是听不懂的。"
            妃子 "哼！别以为本宫不知道你们这些新秀是什么心思，可是别动到本宫头上来了！"
            妃子 "本宫可不想做给别人乘凉的大树！"
            陶凝 "您自然不是。"
            hide fz
            hide 陶凝
            if fz not in Npcmeet:
                $ Npcmeet.append(fz)
            $ fz.foes.append(taoning)
            $ fz.foes.append(taoning)
            $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+fz.hao+fz.weifen+fz.name +"与"+taoning.hao+taoning.weifen+taoning.name +"在宫中偶遇，二人话不投机，不欢而散。\n"
            $ allstory.insert(0,tempstory2)
        elif fz.xingge == "清冷" or fz.xingge == "安静":
            妃子 "良辰好景？"
            妃子 "本宫怎得没瞧见……此处人多口杂，本宫倒觉得还是太液和上林的景致好些。"
            陶凝 思 "嫔妾刚入宫未久，也不知道这宫中何处景美，便也只得循着人多的地方来了。"
            妃子 "哦……这宫里大抵是喜欢此处的人多些，你倒也没说错。只是本宫喜清静罢了。"
            妃子 "改日得空再同你说话，本宫先走了，[taoning.cheng]自便罢。"
            hide fz with dissolve
            hide 陶凝 with dissolve
            if taoning not in Npcmeet:
                $ Npcmeet.append(taoning)
        else:
            妃子 "好呀，过来吧，[taoning.cheng]。"
            陶凝 常 "是。"
            妃子 "本宫记得你刚进宫不久，倒也知道这御花园的景好？"
            陶凝 思 "嫔妾不知，是跟着您来的。"
            妃子 "哦？"
            陶凝 "嫔妾以为，您去的地儿必定是最好的。"
            陶凝 思 "只是……怕您不许。"
            妃子 "瞧你说的本宫像是有多可怕似的。"
            妃子 "嗯……你资历尚浅，懂得跟着前人走，倒不失为聪明之举。"
            陶凝 常 "是。"
            妃子 "陶凝——本宫记下了。"
            hide fz with dissolve
            hide 陶凝 with dissolve
            $ fz.friends.append(taoning)
            $ fz.friends.append(taoning)
            $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+fz.hao+fz.weifen+fz.name +"与"+taoning.hao+taoning.weifen+taoning.name +"在宫中偶遇，二人相谈甚欢，意犹未尽。\n"
            $ allstory.insert(0,tempstory2)
    else:
        show 陶凝 笑 with dissolve
        陶凝 "嫔妾给[my.cheng]请安。"
        $ taoning.meet += 1
        我 "噢……你是那新进入宫的陶氏。"
        陶凝 常 "是……嫔妾见过[fz.cheng]。今日良辰好景，您若有兴致，嫔妾陪您走走罢？"
        menu:
            "欣然同意":
                $ taidu += 4
                我 笑 "好呀，过来吧，[taoning.cheng]。"
                陶凝 常 "是。"
                我 常 "本宫记得你刚进宫不久，倒也知道这御花园的景好？"
                陶凝 思 "嫔妾不知，是跟着您来的。"
                我 "哦？"
                陶凝 "嫔妾以为，您去的地儿必定是最好的。"
                陶凝 思 "只是……怕您不许。"
                我 "瞧你说的本宫像是有多可怕似的。"
                我 "嗯……你资历尚浅，懂得跟着前人走，倒不失为聪明之举。"
                陶凝 常 "是。"
                我 "本宫还记得你入宫前……"
                陶凝 思 "嫔妾入宫前可曾和娘娘有什么渊源？"
                我 笑 "当时你在宫中跟丢了教引的嬷嬷，还是本宫的宫女替你指了去路了。"
                陶凝 常 "啊……当时那位竟是娘娘的宫女。"
                "只见陶凝退后一步，竟朝你行了跪拜的大礼。"
                陶凝 "陶凝愚钝，若非娘娘的宫女相助，恐怕当时便以秀女失仪之名被逐出宫去，颜面尽失。娘娘对陶凝来说，是有大恩之人。"
                我 "好了，起来罢。"
                我 "本宫也想问你，那日你回了储秀宫，可有被嬷嬷责罚？"
                陶凝 "只是思过一日，并无重责。"
                我 "那便好……"
                陶凝 "对嫔妾来说自然是极好。既保住了颜面，还有幸入选进宫，能与娘娘结缘，得您的照拂。"
                我 "先陪本宫走走罢。"
                $ Feizilike_Up(taoning,10)
                $ Npcmeet.append(taoning)
                hide 陶凝
                $ fz.friends.append(taoning)
                $ fz.friends.append(taoning)
                $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+fz.hao+fz.weifen+fz.name +"与"+taoning.hao+taoning.weifen+taoning.name +"在宫中偶遇，二人相谈甚欢，意犹未尽。\n"
                $ allstory.insert(0,tempstory2)
            "不屑一顾":
                $ xingzi += 3
                $ taidu -= 3
                我 "本是兴致好的，可瞧见了些寒酸子气。就像是在满汉全席上瞧见了一只苍蝇，叫人倒胃口。"
                陶凝 思 "嫔妾眼拙，可没见着什么苍蝇。您若不喜，叫宫人吆了去便是。"
                我 怒 "哼！"
                我 "（这些新秀一个个得倒都是不肯安分，竟敢把心思动到我头上来了，也不看看自己配不配！）"
                我 "本宫可不想做给别人乘凉的大树！"
                陶凝 "您自然不是。"
                $ taoning.like -= 5
                hide 陶凝 with dissolve
                $ fz.foes.append(taoning)
                $ fz.foes.append(taoning)
                $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+fz.hao+fz.weifen+fz.name +"与"+taoning.hao+taoning.weifen+taoning.name +"在宫中偶遇，二人话不投机，不欢而散。\n"
                $ allstory.insert(0,tempstory2)
            "推辞离去":

                我 思 "良辰好景？"
                我 "本宫怎得没瞧见……此处人多口杂，本宫倒觉得还是太液和上林的景致好些。"
                陶凝 思 "嫔妾刚入宫未久，也不知道这宫中何处景美，便也只得循着人多的地方来了。"
                我 常 "哦……这宫里大抵是喜欢此处的人多些，你倒也没说错。只是本宫喜清静罢了。"
                我 "改日得空再同你说话，本宫先走了，[taoning.cheng]自便罢。"
                陶凝 "是嫔妾扰了您了，嫔妾告退。"
                hide 陶凝 with dissolve
                $ taidu -= 3
    return

label 偶遇陶凝_2(fz):
    $ bg("皇宫")
    show 我的宫女
    我的宫女 "主子，今个日头真烈啊。"
    我的宫女 "咦，前头那是……"
    hide 我的宫女
    show fz at zuo with dissolve
    妃子 "今年当真是酷暑……[fz.Gongnv[0].name]，记得叫人多备些冰碗，否则本宫可真要吃不消了。"
    show 陶凝 at you with dissolve
    陶凝 "嫔妾给[fz.cheng]请安。"
    妃子 "噢，是[taoning.cheng]啊。免礼吧，这么热的天，你怎的也在外面？"
    陶凝 "回娘娘的话，嫔妾正打算去莲韵池走走。"
    妃子 "咦，今日如此酷热，旁的人都巴不得窝在寝居偷个凉快，你倒好，巴巴往外头跑。御花园现下可热得没人去了。"
    陶凝 "是，只是嫔妾屋子里也闷得很，倒不如莲韵池，有林荫和轻风，反而清爽些。"
    妃子 "你知道？"
    陶凝 "嫔妾这几日午后都会去那儿寻个凉快。"
    妃子 "噢……本宫倒好一阵子没去莲韵池了。今年的莲花该开了吧？"
    陶凝 "是应了时节，开得正盛呢。"
    妃子 "[taoning.cheng]，倒是很知时节呢。这宫里就该多些像你这般玲珑的人。"
    妃子 "天气一热，大伙儿都像本宫一样，热得心浮气躁了。"
    陶凝 "嫔妾愚钝，不知道为何会被娘娘称赞。嫔妾只想寻个凉快。"
    妃子 "真的只是想寻个凉快吗？"
    妃子 "本宫殿里备好了冰碗，[taoning.cheng]要不要去坐坐？"
    陶凝 思 "这……嫔妾却之不恭，可……"
    妃子 "你若不想去，本宫也不会为难你。"
    陶凝 常 "那嫔妾便改日再去拜访了。"
    妃子 "嗯，你去罢。"
    hide 陶凝 with dissolve
    $ gn = fz.Gongnv[0]
    show gn at you
    宫女 "主子，这[taoning.cheng]……"
    妃子 "本宫之前竟没发现，宫里还有这么一号人物。"
    宫女 "主子，您的意思是……"
    妃子 "替本宫盯着她。"
    宫女 "是。可是奴婢愚钝，您方才是有意示好，而她却傻愣愣地不领情……"
    妃子 "你的确是愚钝。"
    宫女 "啊……"
    妃子 "你想想今日咱们路上遇到的嫔妃宫女，哪个不是满身大汗，脚步匆匆？你看她那平心静气的样子，同本宫行礼时也是妥妥帖帖挑不出错来。"
    妃子 "脸上更是一滴汗都没有。"
    宫女 "您这么一说……"
    妃子 "还有，本宫方才示好，就连你也看出来了，你觉得她真的看不出来吗？"
    宫女 "那她……主子，奴婢快绕晕了。"
    妃子 "她想让本宫觉得她不聪明……"
    妃子 "哎哟，实在是太热啦。先回宫再说罢。"
    宫女 "是！奴婢替您打扇。"
    hide fz with dissolve
    hide gn with dissolve
    return

label 陶凝_黑化(fz):
    $ bg("皇宫")
    $ taoning_3 = True
    $ gn = fz.Gongnv[0]
    show 陶凝 思 at you with dissolve
    陶凝 思 "……"
    show fz at zuo with dissolve
    妃子 "[gn.name]，你看本宫这簪子好看吗……咦，这不是……这位是谁来着……"
    hide 陶凝
    show gn at you
    宫女 "主子，是[taoning.cheng]。"
    if fz.level <= taoning.level:
        妃子 "噢，是[taoning.cheng]啊，难得见你出来走动，本宫都忘了还有这个人了。"
        hide gn
        show 陶凝 思 at you
        陶凝 思 "……"
        妃子 "[taoning.cheng]？"
        陶凝 常 "（回神）！"
        陶凝 怒 "嫔妾见过[fz.cheng]。"
        妃子 "还知道见过本宫？真不知道你是眼睛不好还是耳朵不好。"
        陶凝 笑 "嫔妾出门前看了本书，只是嫔妾愚钝，参悟不透其中的含义，故而一直冥思苦想，未想因此出神，失了礼数，还望[fz.cheng]见谅。"
        妃子 "本宫看你不仅眼瞎耳聋，脑子也不好。那你倒是说说，你看的是什么书，又为何参悟不透？若是说不出来，那就是意图狡辩，罪加一等！"
        陶凝 思 "嫔妾看《左传》中有一句“莫敖必败，举趾高，心不固矣。”因此迷惑，为何莫敖走路时要将脚抬高，又为何会因此“必败”呢？"
        妃子 "……"
        妃子 "你、你！你竟敢讽刺本宫？"
        if fz.familylevel < taoning.familylevel:
            妃子 "小门小户的出身，就是没有涵养，读了几本书就以为自己有什么雄才大略了？"
            妃子 "可惜了，哪怕你是诸葛神通又如何？身在后宫，空有一副伶牙俐齿，不讨皇上喜欢又有什么用？"
        else:
            妃子 "哼……想不到宫里还有这么一位深藏不露的才女，怎得也没听旁人提起，也没得皇上垂青呢？"
        陶凝 "嫔妾自知愚钝，只是娘娘有问，嫔妾才有答，自是不敢称才。"
        妃子 "你这会儿倒是不敢了？"
        if my.level < fz.level and taoning not in my.foes:
            menu:
                "替陶凝解围":
                    $ Feizilike_Up(taoning,10)
                    陶凝 "嫔妾见过[my.cheng]。"
                    妃子 "嫔妾给[my.cheng]请安。"
                    menu:
                        "温言调解":
                            $ xingzi -= 5
                            我 "都免礼吧。"
                            我 "方才的事情本宫都听到了。"
                            妃子 "呃……"
                            我 "一件小事罢了，[taoning.cheng]确实失了礼数，但[fz.cheng]也不必如此得理不饶人，伤了和气，得不偿失啊。"
                            妃子 "这……罢了，毕竟没冒犯到自己头上，在[my.cheng]看来，的确是件不值一提的小事。"
                            我 "本宫是瞧见[taoning.cheng]的确并非有意，反倒是你有些咄咄逼人了。"
                            我 "听本宫一言，此事就此揭过。"
                            妃子 "是……[my.cheng]的面子嫔妾是不得不给的，否则不就像[taoning.cheng]那样失了礼数了？"
                            hide fz
                            $ fz.like -= 5
                        "愤然斥责":

                            $ xingzi += 5
                            我 "安？"
                            我 "本宫如何能安呢，[fz.cheng]如此得皇上怜惜，却屈尊向本宫请安，实在是折煞。"
                            妃子 "这……嫔妾……"
                            我 "[fz.cheng]为何如此惶恐？莫不是本宫不小心做错了什么，还是今个妆容打扮不妥帖，吓到你了？若真如此，还请[fz.cheng]不要怪罪，更不要告诉了皇上，惹得皇上大怒，责罚于本宫呢。"
                            妃子 "嫔、嫔妾怎敢……"
                            我 "怎么，这会儿你又不敢了？"
                            妃子 "嫔妾知错，嫔妾知错……"
                            我 "方才吱呀乱叫，这会儿倒是装起可怜样子来了，本宫都快被你给逗笑了。既然知错了，就赶紧给本宫滚。"
                            妃子 "是……"
                            hide fz
                            $ fz.like -= 10
                    hide 陶凝
                    show 陶凝
                    陶凝 思 "[my.cheng]……"
                    我 "[fz.cheng]行事娇纵，多得是人会治理她，你不必同她一般见识。"
                    陶凝 "嫔妾人微言轻，即便是被挑了刺，也只能受着了。"
                    我 "不过本宫倒瞧着你也不是任人欺负的，方才那几句话可是实打实地把她给气坏了。"
                    陶凝 笑 "今日多谢娘娘解围了。"
                    我 "嗯。"
                    陶凝 "嫔妾告退。"
                    hide 陶凝
                "转身离开":


                    我 "（还是不要掺和得好。）"
                    妃子 "既然你这么爱研读史书，那就把春秋三传都抄一遍如何？"
                    妃子 "而且你不是说参悟不透吗？都说“读书百遍其义自见”，你就把那一章抄上一百遍，本宫不信你还读不懂！"
                    陶凝 "嫔妾遵命。"
                    妃子 "哼，鼠雀之辈，真把自己当一回事儿了！"
                    hide fz
                    陶凝 "……"
                    hide 陶凝
        else:
            妃子 "既然你这么爱研读史书，那就把春秋三传都抄一遍如何？"
            妃子 "而且你不是说参悟不透吗？都说“读书百遍其义自见”，你就把那一章抄上一百遍，本宫不信你还读不懂！"
            陶凝 "嫔妾遵命。"
            妃子 "哼，鼠雀之辈，真把自己当一回事儿了！"
            hide fz
            陶凝 "……"
            hide 陶凝
    else:

        妃子 "哎，是嫔妾失礼了，难得见您出来走动，嫔妾都忘了还有这个人了。"
        妃子 "嫔妾见过[taoning.cheng]了。"
        hide gn
        show 陶凝 思 at you
        陶凝 "……"
        妃子 "[taoning.cheng]？"
        陶凝 常 "（回神）！"
        陶凝 "是[fz.cheng]啊。"
        陶凝 "没什么事，[fz.cheng]请自便罢。"
        妃子 "呵……[taoning.cheng]这做派也太大了点儿，嫔妾位份虽在您之下，但好歹也算是在皇上面前说得上话的人，在您这儿怎得连个正眼都难得了？"
        妃子 "这传出去，且不说别人如何议论，皇上怕也是会有所不快呢。"
        陶凝 思 "那你便不要传出去便好了。"
        妃子 "咳！"
        妃子 "那[taoning.cheng]还请恕嫔妾不能从命了，这样的事情想让嫔妾闷在心里怕是做不到呢！"
        陶凝 "我说了，方才是无心之举，并非有意无视[fz.cheng]。[fz.cheng]如此不依不饶，还想要如何呢？是非得向你请罪才可以就此揭过么？"
        妃子 "嫔妾人微言轻，当然担不起[taoning.cheng]的请罪。"
        妃子 "可[taoning.cheng]目中无人之事，也得让旁的人知晓才是。"
        if my.level < taoning.level and taoning not in my.foes:
            menu:
                "替陶凝解围":
                    $ Feizilike_Up(taoning,10)
                    陶凝 "嫔妾见过[my.cheng]。"
                    妃子 "嫔妾[my.cheng]安。"
                    menu:
                        "温言调解":
                            $ xingzi -= 5
                            我 "都免礼吧。"
                            我 "方才的事情本宫都听到了。"
                            妃子 "呃……"
                            我 "[fz.cheng]觉得[taoning.cheng]轻视自己，可你自己不也是无礼犯上？"
                            妃子 "这……是[taoning.cheng]她先……"
                            我 "好了，本宫瞧见[taoning.cheng]的确并非有意，反倒是你有些咄咄逼人了。"
                            我 "听本宫一言，此事就此揭过。"
                            妃子 "是……[my.cheng]的面子嫔妾是不得不给的，否则不就同[taoning.cheng]一般目中无人了？"
                            hide fz
                            $ fz.like -= 5
                        "愤然斥责":

                            $ xingzi += 5
                            我 "安？"
                            我 "本宫可不敢不安呢，若是举止有什么疏漏，可要被[fz.cheng]昭告后宫了。"
                            妃子 "这……嫔妾……"
                            我 "[fz.cheng]为何如此惶恐？莫不是本宫真的做错了什么？那你可要跟本宫明说，本宫必然悔改，还望你不要外传才是。"
                            妃子 "嫔、嫔妾怎敢……"
                            我 "怎么，这会儿你又不敢了？"
                            妃子 "嫔妾知错，嫔妾知错……"
                            我 "方才吱呀乱叫，这会儿倒是装起可怜样子来了，本宫都快被你给逗笑了。既然知错了，就赶紧给本宫滚。"
                            妃子 "是……"
                            hide fz
                            $ fz.like -= 10
                    hide 陶凝
                    show 陶凝
                    陶凝 思 "[my.cheng]……"
                    我 "你位份在她之上，不必这么忍气吞声的。"
                    陶凝 "嫔妾……是在忍气吞声吗……"
                    陶凝 笑 "原来如此，嫔妾知道了。还有，多谢娘娘解围。"
                    我 "嗯。"
                    陶凝 "嫔妾告退。"
                    hide 陶凝
                "转身离开":


                    我 "（还是不要掺和得好。）"
                    陶凝 "好，随[fz.cheng]去说便是了。"
                    妃子 "也是，反正，[taoning.cheng]也没什么可在乎的了。"
                    妃子 "倒是嫔妾在这里白费功夫，显得跟个小丑似的，让[taoning.cheng]见笑了。"
                    陶凝 "[fz.cheng]说的是。"
                    妃子 "你！"
                    妃子 "哼，浪费时间！"
                    hide fz
                    陶凝 "……"
                    hide 陶凝
        else:
            陶凝 "好，随[fz.cheng]去说便是了。"
            妃子 "也是，反正，[taoning.cheng]也没什么可在乎的了。"
            妃子 "倒是嫔妾在这里白费功夫，显得跟个小丑似的，让[taoning.cheng]见笑了。"
            陶凝 "[fz.cheng]说的是。"
            妃子 "你！"
            妃子 "哼，浪费时间！"
            hide fz
            陶凝 "……"
            hide 陶凝
    $ taoning.qingxiang += 30
    $ taoning.foes.append(fz)
    $ fz.foes.append(taoning)
    $ tempstory2 ="【闲言】"+str(year)+"年"+str(month)+"月，"+taoning.hao+taoning.weifen+taoning.name +"与"+fz.hao+fz.weifen+fz.name +"在宫中偶遇，二人话不投机，不欢而散。\n"
    $ allstory.insert(0,tempstory2)
    return

label 陶凝_家中事:
    $ taoning_4 = True
    if taoning.level < my.level:
        $ zicheng = "嫔妾"
        $ cheng = "本宫"
    else:
        $ zicheng = "本宫"
        $ cheng = "嫔妾"
    陶凝 "[my.cheng]来了。[cheng]未能及时迎接，还望你不要见怪。"
    我 "[taoning.cheng]这是在写什么……"
    陶凝 "……是家书。"
    我 "（一入宫门，便再难与族人见上一面，宫中妃嫔同家族书信来往的也不少。）"
    我 "是想家了吗？"
    陶凝 "[cheng]家中并没有什么可值得思念的。"
    我 "那这些家书……"
    陶凝 "骗自己还有些念想罢了。"
    陶凝 "[taoning.Gongnv[0].name]，把这些都收起来留着点灯用罢。"
    我 "你这又是何必呢？"
    陶凝 "写了挺久，平白丢了也是可惜。"
    menu:
        "那写它干什么":
            $ xingzi += 3
            陶凝 "是呀，[cheng]从来不是个聪明人，做的蠢事也不少了。"
            陶凝 "又何妨多这一件。"
        "家中人对你不好？":
            $ taidu += 3
            陶凝 "既然能送进宫来，又能差到哪里去？"
    我 "听[taoning.cheng]的话，倒像是和家中有什么怨气似的。"
    陶凝 思 "……"
    我 "（像是说中了。）"
    我 "怨气也罢，思念也罢，既然都写了，还不如差了宫人送出去。"
    陶凝 "从前在家里，[cheng]又再大的怨气也无人在乎。如今[cheng]在宫中亦是人微言轻，且不说叫不叫得动宫人，即便送到，恐怕也与以前一般无二。"
    陶凝 "再者，家中待[cheng]不差，爹娘瞧见了，除了心中徒生不快又能如何？"
    我 "这话倒叫[zicheng]有些糊涂了。以前也甚少听你提起家中，像是有什么不快，但也有感情在。"
    陶凝 "毕竟[cheng]是娘一手抚养大的，怎么会没有感情呢？[cheng]在府中是庶出，虽然遭人轻视，但也不至于被苛待。"
    陶凝 "家父待娘亲虽然已无初时情分，但[cheng]到底也是他的正经女儿。"
    陶凝 "罢了罢了……多说无益，[cheng]对他们有怨气，可自己又好得了哪里去？"
    我 "[taoning.cheng]现下如何不好？"
    陶凝 "嗯……入宫前娘亲说，只要在宫里平平安安得便是好了。那[cheng]的确现下的确没什么不好。"
    陶凝 "他们一开始也没指望着靠[cheng]光耀门楣。"
    if my.xinji >= 800:
        我 "[zicheng]却是知晓，若[taoning.cheng]想青云直上，怕是没人能挡得了你。"
        陶凝 "[my.cheng]说笑了，[cheng]还想着学一学爹娘的安分守己呢，能入宫已是福分，哪敢还有青云直上的妄想？"
    else:
        我 "[taoning.cheng]这便是妄自菲薄了。"
        陶凝 "可惜了[cheng]学到了他们的不争气，却没学到他们的安分守己呢。"
    我 思 "……"
    陶凝 "[cheng]的家父自入仕以来，一直本本分分，从无苞苴竿牍之事。而娘亲她……"
    陶凝 "家父结发早逝，当时她同家父情意尚深，本可争一争嫡妻之位。"
    陶凝 "可她却念及自己本是通房上位，当不得那嫡妻之位。说来[cheng]家父也不过是个小官，苦苦守着那所谓的繁复缛节又能有多好听？将嫡妻之位拱手让人，旁人便会多看她几眼么？不会，只会觉着她一辈子都翻不了身罢了。"
    陶凝 "她的日子本可以比如今好上许多的。"
    陶凝 "家父他也是如此，无人赞许他高风亮节，只会觉得他呆板蠢钝，愚不可及。但凡有些功劳苦劳，全落了他人头上，而若有什么罪责，便全由他来担着。"
    menu:
        "人各有志，不必强求":
            $ xingzi -= 3
        "莫要重蹈覆辙":
            $ xingzi += 3
    陶凝 "兴许如此罢。"
    陶凝 "果然……往后还是别写那些劳什子的玩意儿了，乱了自己的心神。"
    return

label 陶凝_好事:
    $ taoning_5 = True
    if taoning.level < my.level:
        $ zicheng = "嫔妾"
        $ cheng = "我"
    else:
        $ zicheng = "我"
        $ cheng = "嫔妾"
    陶凝 笑 "[aicheng]来了。"
    我 笑 "今日心情似乎不错。是因为令尊升迁之事？"
    陶凝 笑 "是，但也不全是。"
    我 笑 "记得你之前说起令尊在仕途上似乎并不是那么一帆风顺……"
    陶凝 常 "岂止是不顺？怕是他自己这辈子都没想过自己还会有升官的机会罢，更没有想过，自己升官靠的不是自己的本事，而是自己的女儿——他从来没指望过的女儿。"
    陶凝 "也不知道他如今到底是高兴还是不高兴呢？"
    if my.xinji < 500:
        我 常 "既然升官了，自然是喜出望外的。"
        陶凝 "哈……听[aicheng]这么说，兴许我家父他当真是这么想的呢。"
        我 "（怎么感觉有点怪怪的……）"
        陶凝 "毕竟你们心思都不深。"
        陶凝 "只不过你单纯率真，他死板愚钝罢了。"
        陶凝 "嗯，定然如此，他应是喜出望外才是。"
        陶凝 "我娘她……定然也是高兴的罢。"
        我 思 "令堂她也？"
        陶凝 "她被抬为了平妻，是寻常妾室做梦也得不到的待遇。"
        陶凝 "而这也是我给的。"
    else:
        我 思 "你曾说过他从不行鸿都买第之事，如今凭着女儿在宫中的地位得了官位，岂非他所愿？"
        我 "说直白些……"
        陶凝 "是讽刺。"
        我 "正是。"
        我 "不过……这正是你所愿的？"
        陶凝 "是，而且不仅如此，更让我高兴的是，我让我娘亲做了平妻。"
        陶凝 "要么违背上意，要么违纲乱礼，无论哪一种，都是他们所不愿的。"
    if xingzi >= 50:
        我 笑 "这样很好。"
        我 "他们都是安分守己之人。如今你是天家的人，而他们的本分之中，自然包括了遵从你的意愿。"
        陶凝 笑 "是啊，我的意愿，他们无可违背。"
        陶凝 "而且……不仅仅是他们。"
        $ Feizilike_Up(taoning,3)
    陶凝 "我也要谢谢他们。"
    陶凝 "他们教会了我默默无闻，教会了我收敛锋芒……"
    陶凝 "还有[aicheng]你。"
    陶凝 "才有了今天坐在正殿主位之上的陶凝。"
    "获得了5个技能点。"
    $ my.skillcosts += 5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
