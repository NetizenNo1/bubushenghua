
label 建章宫_精敏:

    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    if my.taihoulike>30 and taihou1 == False:

        $ taihou1 = True
        $ taihoumeet = taihoumeet +1
        show 太后 at chara
        "还未到殿外，便见着太后已在外头 。"
        menu:
            "上前请安":
                pass
        太后 "[cheng]怎这巧？可是来找哀家何事？"
        menu:
            "说明来意":
                pass
        太后 "嗯，哀家现正要去奉天楼祈福， 随哀家一同去罢。"
        menu:
            "欣然跟上":
                scene black
                with fade
                "太后一路话不多，时而还会呵斥做事不足的宫女，一路气氛严肃。祈福后也并未多说什么。"
                $ AP = AP - 2
                $ timenum = timenum + 2
                $ bg("建章宫内")
                with fade
                show 太后 at chara

                太后 "哀家今乏了，今儿便不见客了，跪安罢。"
                jump 皇宫界面
            "委婉推辞":
                太后 "可是瞧不起哀家？"
                太后 "吓唬你罢，哀家也不勉强，跪安罢。"
                "待其走了几步，便听到冷哼一声。"
                hide 太后
                jump 皇宫界面
    else:
        pass
    show 莲稚 at chara
    $ lucky = renpy.random.randint(0,4)
    if lucky ==0:
        莲稚 "[my.cheng]，太后今天不见客，请您改日再来吧。"
        jump 皇宫界面
    elif lucky ==1:
        莲稚 "真不巧，太后今日前往奉天楼祈福了。[my.cheng]，您请回吧。"
        jump 皇宫界面
    else:
        $ taihoumeet = taihoumeet +1
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        "过了一会儿……"
        show 莲稚 at chara
        莲稚 "奴婢这就带您过去。"
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        if my.taihoulike >50:
            $ cheng = aicheng
        else:
            $ cheng = my.cheng
        $ lucky = renpy.random.randint(0,4)
        if month > 1 and month < 5:
            if lucky == 0:
                太后 "哟哟哟，来……过来，对。"
                "（太后正训练着她养的文鸟，那文鸟生性十分乖巧，太后唤它往哪就往哪。）"
                menu:
                    "问安":
                        pass
                太后 "[cheng]？起来吧，瞧哀家这家伙，可比人听话多了。"
                hide 太后
            elif lucky == 1:
                太后 "[cheng]来得正好，哀家刚吩咐御膳房做了些吃食，看看想吃什么，随便尝尝罢。"
                menu:
                    "枣泥酥":
                        太后 "这枣泥酥做的还不错，回头哀家唤人去打赏下那厨子。"
                    "云片糕":
                        太后 "这云片糕做的还不错，回头哀家唤人去打赏下那厨子。"

                hide 太后
            elif lucky == 2:
                太后 "哀家近日有那么几个宫女，很是不省心。"
                太后 "哀家最不喜那些做事情手脚不利索的，磕磕碰碰做事还慢。"
                太后 "[cheng]的那几个奴才如何？若是不省心的，还不如打发了。"
                hide 太后
            elif lucky == 3:
                "一进去，御医正在里头给太后请平安脉，正行礼，那御医便退下了，嘴里还嘱咐了太后几句，只是冬天染的风寒未褪去，再喝些药调理调理驱驱寒便是。"
                太后 "（叹了口气），[cheng]起来吧，坐哀家这陪哀家说说话，旁人都退下罢。"
                我 "是。"
            else:

                "进去便见着太后正亲自修剪着那盆景，盆景翠绿，看上去养得极好。"
                太后 "怎[cheng]今儿有空来哀家这？起来罢。"
                我 "（闲聊片刻）"
                hide 太后
        elif month > 4 and month < 8:
            if lucky == 0:
                太后 "[cheng]来啦？正巧这会儿还偷得几分凉爽，陪哀家去院子里走走吧。"
                我 "是。"
                $ bg("建章宫外")
                太后 "（命宫人备了鱼饵，去池子边上给鱼儿们喂食。）"
                太后 "[cheng]起来吧，你说那里头的几条大鱼是吃小鱼，还是吃哀家手里的鱼饵？"
                hide 太后
            elif lucky == 1:
                "一小宫女端着一小碗在那里紧张得很，碗里头尽是一些小虫子，而太后正喂着她肩上那文鸟。"
                太后 "这小东西怎都吃不饱。"
                menu:
                    "行礼请安":
                        pass
                太后 "[cheng]起身便是，你可要来喂喂这文鸟？不知[cheng]可怕虫子不。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来得正好，哀家让御膳房送来了些点心，不如尝尝合不合胃口？那芸豆可是哀家家乡的特产喏。"
                menu:
                    "蜜汁蜂巢糕":
                        太后 "这芸豆尝起来，可真是曾经的味道呀……"
                    "芸豆卷":
                        太后 "这芸豆尝起来，可真是曾经的味道呀……"

                hide 太后
            elif lucky == 3:
                python:
                    for i in NPC_fz_list:
                        if i.state == "禁足" or i.state == "病重" or i.level == 17 or i.xinji > 800:
                            pass
                        else:
                            tempfzlist.append(i)
                if len(tempfzlist) == 0:
                    太后 "[cheng]，这大热天的，你一路上过来热不热？坐吧，喝盏凉茶。"
                    hide 太后
                else:
                    $ fz = renpy.random.choice(tempfzlist)
                    太后 "[cheng]瞧瞧，这可真是有趣了，这大热天的，那[fz.cheng]竟唤人给哀家送了件厚衣裳，可是嫌哀家不够热？"
                    hide 太后
            else:
                "一进去，御医正在里头给太后请平安脉。正行礼，那御医便退下了，嘴里还嘱咐了太后几句，说是身子并无大碍，但现天热不宜多出门，若出也最好快日落时。"
                太后 "[cheng]起来吧，坐哀家这陪哀家说说话，去，上茶给[my.cheng]。"
                hide 太后
        elif month > 7 and month < 11:
            if lucky == 0:
                "一来便见着太后手一甩，一碟吃食便落于地上，哐啷的一声，而其中一个宫女连忙跪下，大气不敢出。"
                太后 "瞧瞧这人，抖得可是厉害了，罢了，哀家今儿心情不错，打发去掖庭罢了。噢？[cheng]来了，哀家现才见着，来，陪哀家品品茶。"
                hide 太后
            elif lucky == 1:
                "太后正与那文鸟玩闹得很是兴奋。"
                menu:
                    "行礼问安":
                        pass
                太后 "[cheng]快些起身罢，来随哀家一同逗逗这小东西，也就它最得哀家心。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来哀家这，今儿那新来的宫女机灵着，找来了些百合什么的，便吩咐去做了些吃食，尝尝罢。"
                menu:
                    "松子百合酥":
                        太后 "倒是这松子味哀家更为喜欢，[cheng]觉着呢？"
                    "珍珠翡翠圆":
                        太后 "倒是这松子味哀家更为喜欢，[cheng]觉着呢？"

                hide 太后
            elif lucky == 3:
                太后 "[cheng]可有怎么趣事？赶紧说来给哀家听听，哀家院里头还有个秋千，方才可有见着？不如坐着玩玩？"
                hide 太后
            else:
                "一进去，御医正在里头给太后请平安脉，正行礼，那御医便退下了，嘴里还嘱咐了太后几句，只是秋风微起，夏又刚去，衣裳添得晚了有些许着凉，但并无大碍。"
                太后 "（叹了口气），[cheng]起来吧，坐哀家这陪哀家说说话，可要吃些杏仁什的？"
                hide 太后
        else:
            if lucky == 0:
                hide 太后
                "进殿里，并未曾见太后身影。"
                我 "（奇怪，方才宫女传进来，太后应在才是。）"
                太后 "[cheng]。"
                我 "（循声望去。）"
                $ bg("建章宫外")
                show 太后 at chara with dissolve
                太后 "哀家不过穿得一身白站于外头树下，[cheng]怎这就瞧不着哀家了？"
                hide 太后
            elif lucky == 1:
                "太后手里拿着一布匹不知在绣些什么，只肉眼可见那布匹挺厚，想必十分暖和。"
                menu:
                    "行礼问安":
                        pass
                太后 "[cheng]起来罢，你瞧瞧哀家手里这绣的如何？近日天儿冷了，炭火若是不够记得跟掖廷要，文鸟不适烤炭火，哀家只好弄小毛毯了。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来了，于火炉边烤烤暖和会罢，哀家刚吩咐人去御膳房拿来了些暖身子的汤羹，既然来了便喝些吧。"
                menu:
                    "七翠羹":
                        太后 "这乌鸡汤味足，想来那掌勺的厨子，应是下了不少功夫。"
                    "人参乌鸡汤":
                        太后 "这乌鸡汤味足，想来那掌勺的厨子，应是下了不少功夫。"

                hide 太后
            elif lucky == 3:
                太后 "哀家年轻时其实也不太信那神明，还觉得那些老人家都愚钝得很。但真当自己老了，心烦意乱时，也只能念念经文烧烧香，才可静下心来。兴许……（叹气）"
                hide 太后
            else:
                "一进去，御医正在里头给太后请平安脉，正行礼，那御医便退下了，嘴里还嘱咐了太后几句，说是冬冷近来雪又大，夜里得关好窗子才是，免得受冻，得按时服药才行。"
                太后 "咳咳……[cheng]进来吧，咳咳咳……坐，烤烤炉火，别冻着了。"
                hide 太后

    $ Taihoulike_Up(my,2)

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面






label 建章宫_擅权:
    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    show 莲稚 at chara
    if my.taihoulike>30 and taihou1 == False:
        $ taihou1 = True
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        show 莲稚 at chara with dissolve
        莲稚 "[my.cheng]请进，太后娘娘在里头候着您呢。"
        hide 莲稚
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        太后 "怎么今儿得空来看哀家了？"
        menu:
            "行礼问安，说明来意":
                pass
        太后 "赐坐罢，哀家这还有些小点心，若是不嫌便尝尝。"
        太后 "哀家听闻[cheng]家中，有一兄长近儿得了个榜眼。"
        menu:
            "回娘娘，着实有此事。":
                pass
            "是考了好些年才得的榜眼。":
                pass
            "兄长不才，不过榜眼罢了。":
                pass

        太后 "倒是挺好，虽不及状元但也着实有一番实力，哀家这儿正好有一翡翠扣，由此做赏罢。"
        menu:
            "嫔妾替兄长谢过太后娘娘。":
                pass
        "吃了些许点心，于太后一同话家常。虽一直有说有聊，可这氛围却隐隐不妥，看不出太后所想。"
        太后 "哀家乏了，[cheng]跪安罢。"
        我 "是，臣妾告退。"
        hide 太后
        $ bg("建章宫外")
        "刚离开殿门，便闻身后传来一宫女被呵斥声。"
        $ taihoumeet = taihoumeet +1
        $ Taihoulike_Up(my,1)
        $ timenum = timenum +1
        $ AP = AP -1
        jump 皇宫界面

    elif my.taihoulike > 80 and taihou3 == False:
        $ taihou3 = True
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "您来的不巧，皇上正与太后娘娘对弈呢，您还是请回罢。"
        我 "那我改日再来拜访。"
        hide 莲稚
        我 "（转身刚走出建章宫门外，便听到一阵脚步声……）"
        show 莲稚 at chara with dissolve
        莲稚 "[my.cheng]，娘娘传您进去坐坐呢。"
        hide 莲稚
        $ bg("建章宫内")
        "殿内皇上和太后坐在桌前对弈，看神情，现下是太后棋高一着。"
        menu:
            "行礼问安":
                pass
        show 太后 at chara
        太后 "免礼，赐座吧。"
        if hdxingge == "腹黑":
            太后 "皇上，这局可是哀家赢了。"
            hide 太后
            show 皇帝 at chara
            皇上 "儿臣又输了。"
            hide 皇帝
            show 太后 at chara
            太后 "皇上可真没让着哀家？"
            hide 太后
            show 皇帝 at chara
            皇上 "儿臣真没有，定是今儿手气不好。"
            hide 皇帝
            show 太后 at chara
            太后 "哀家方才说过的话，皇上也答应过的，可要愿赌服输。"
            hide 太后
            show 皇帝 at chara
            皇上 "那是自然，母后讲便是。"
            hide 皇帝
            show 太后 at chara
            太后 "（看了你一眼）[cheng]家中有一兄长，可是得了榜眼，现下皇上可有给其安排职务？"
            hide 太后
            show 皇帝 at chara
            皇上 "（看上去早就知太后会说这些似的，只不紧不慢的抿了口茶，所有所思）儿臣还真未安排，母后定是觉得这人不错。"
            hide 皇帝
            show 太后 at chara
            太后 "的确，哀家派人去瞧过……"
            hide 太后
            show 皇帝 at chara
            皇上 "（未等太后说完，便回头看你）兄长擅何？"
            menu:
                "擅文":
                    pass
                "擅武":
                    pass
                "文武双全":
                    pass
            皇上 "如此，儿臣其实也派人去看过。"
            hide 皇帝
            show 太后 at chara
            太后 "不愧是皇上，可想好安排什么职务了？"
            hide 太后
            show 皇帝 at chara
            皇上 "儿臣昨儿就下旨给[my.cheng]兄长了，估摸着今儿就能送到。"
            hide 皇帝
            show 太后 at chara
            太后 "哈哈哈，[cheng]还不快快谢皇上。"
            hide 太后
            show 皇帝 at chara
            我 "多谢皇上！"
            皇上 "既然有[my.cheng]在这儿陪母后，那朕便回去批阅奏折。"
            皇上 "儿臣告退。"
            hide 皇帝
            show 太后 at chara
            太后 "行，你去吧。"
            我 "臣妾恭送皇上。"
            太后 "（看了你一眼，笑着）你呀，也该多为自己还有背后的家族多做打算啊。"
            我 "臣妾谨遵太后娘娘教诲。"
            hide 太后
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        elif hdxingge == "温柔":
            太后 "皇上可是又让着哀家？"
            hide 太后
            show 皇帝 at chara
            皇上 "母后有所求，说便是，不必下棋分胜负。"
            hide 皇帝
            show 太后 at chara
            太后 "你呀你，就不怕哀家判断有误？"
            hide 太后
            show 皇帝 at chara
            皇上 "怎会，母后的眼光向来不错，儿臣不就是母后眼光所养？"
            hide 皇帝
            show 太后 at chara
            太后 "罢了罢了，哀家说不过你，哀家呀早就观察了[my.cheng]家那兄长许久，皇上可知此人？"
            hide 太后
            show 皇帝 at chara
            皇上 "自然知晓，乃是新的榜眼。"
            hide 皇帝
            show 太后 at chara
            太后 "那可有什么想法？"
            hide 太后
            show 皇帝 at chara
            皇上 "（看你一眼，微笑）来朕这。"
            我 "（走上前去。）"
            皇上 "兄长擅什可知晓？"
            menu:
                "擅文":
                    pass
                "擅武":
                    pass
                "文武双全":
                    pass
            皇上 "嗯嗯，于朕想的一致，看样子爱妃与兄长关系甚好。"
            皇上 "（沉吟片刻）朕已有打算，回去便命人拟旨，好让你兄长尽快入职。"
            hide 皇帝
            show 太后 at chara
            太后 "还不快谢皇上？"
            hide 太后
            show 皇帝 at chara
            我 "多谢皇上！"
            皇上 "爱妃就在这儿陪母后罢，朕得空了再去看你，母后也得注意身子。儿臣告退。"
            我 "臣妾恭送皇上。"
            hide 皇帝
            show 太后 at chara
            太后 "（待皇上的身影消失后，转头看着你，笑着点了点头。）"
            hide 太后
            $ mustshiqin = mustshiqin + 50
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        elif hdxingge == "风流":
            hide 太后
            show 皇帝 at chara
            皇上 "（含情望你）爱妃，过来，来朕这。"
            我 "（向前几步，一下就被皇上揽入怀中）"
            hide 皇帝
            show 太后 at chara
            太后 "（似是习以为常。）"
            太后 "皇上不好好下，哀家可就要赢了。"
            hide 太后
            show 皇帝 at chara
            皇上 "母后唤[my.cheng]进来，不已然赢了儿臣？"
            hide 皇帝
            show 太后 at chara
            太后 "那哀家可就说了？"
            hide 太后
            show 皇帝 at chara
            皇上 "母后说便是。"
            hide 皇帝
            show 太后 at chara
            太后 "方才哀家不是提了[cheng]家那兄长，得了那榜眼，皇上可有什么……"
            hide 太后
            show 皇帝 at chara
            皇上 "这事儿臣已经交给朝中大臣去办了，儿臣先与[my.cheng]回去了，走吧，爱妃想去哪逛？朕陪你。"
            hide 皇帝
            我 "（看了太后一眼，却见她嘴角竟挂着一抹异样的微笑。）"
            scene black
            $ mustshiqin = 100
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        elif hdxingge == "刚正":
            太后 "皇上又赢了。"
            hide 太后
            show 皇帝 at chara
            皇上 "感觉母后技艺有些生疏了。"
            hide 皇帝
            show 太后 at chara
            太后 "明明是皇上，总是不让着哀家。"
            hide 太后
            show 皇帝 at chara
            皇上 "不过，母后方才说的，若是母后赢了，儿臣要答应的条件是什么？"
            hide 皇帝
            show 太后 at chara
            太后 "你可知[my.cheng]兄长中了榜眼。"
            hide 太后
            show 皇帝 at chara
            皇上 "儿臣自然知晓，昨日便封去九品官员里了。"
            hide 皇帝
            show 太后 at chara
            太后 "噢？皇上怎如此迅速。"
            hide 太后
            show 皇帝 at chara
            皇上 "朝中事物儿臣向来重视，岂会放着人才不顾。"
            hide 皇帝
            show 太后 at chara
            太后 "不过，好歹也是榜眼，还是[my.cheng]的兄长，却只能从九品官员做起，是否有些不妥？"
            hide 太后
            show 皇帝 at chara
            皇上 "虽说得了榜眼，但毕竟从未出仕，理应从低做起，有能方可居上。"
            hide 皇帝
            show 太后 at chara
            太后 "皇上说的有理。如此，倒是省了哀家这番心思了。那[my.cheng]便随皇上一同回去罢，哀家输了好几局了，不玩了不玩了。"
            hide 太后
            show 皇帝 at chara
            皇上 "（无奈）是，儿臣告退。"
            hide 皇帝
            scene black
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        else:
            太后 "皇上，这局可是哀家赢了。"
            hide 太后
            show 皇帝 at chara
            皇上 "母后着实厉害，儿臣的确输了。"
            hide 皇帝
            show 太后 at chara
            太后 "哀家方才说过的话，皇上也答应过的，可要愿赌服输。"
            hide 太后
            show 皇帝 at chara
            皇上 "母后请讲。"
            hide 皇帝
            show 太后 at chara
            太后 "[cheng]家中有一兄长，可是得了榜眼，现下皇上可有给其安排职务？"
            hide 太后
            show 皇帝 at chara
            皇上 "（似是早知太后会说这些，面不改色，冷声）未曾。"
            hide 皇帝
            show 太后 at chara
            太后 "[cheng]，过来。哀家问你，你那兄长可擅文擅武？"
            menu:
                "擅文":
                    pass
                "擅武":
                    pass
                "文武双全":
                    pass
            太后 "（甚喜）皇上方才来时不是让哀家推荐个人选吗？这倒是赶巧了。皇上意下如何。"
            hide 太后
            show 皇帝 at chara
            皇上 "（点头。）"
            hide 皇帝
            show 太后 at chara
            太后 "嗯，由此甚好，[cheng]，还不快谢过皇上。"
            太后 "（使了个眼色，想来皇上是给了个品级职权不低的官。）"
            hide 太后
            show 皇帝 at chara
            我 "多谢皇上！"
            皇上 "那儿臣便先回去批阅奏折，让[my.cheng]留在这儿陪您罢，儿臣告退了。"
            我 "臣妾恭送皇上。"
            hide 皇帝
            show 太后 at chara
            太后 "（满脸欣喜）来来来，陪哀家再下一局。"
            我 "是。"
            hide 太后
            $ mustshiqin = mustshiqin + 50
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
    else:



        pass

    $ lucky = renpy.random.randint(0,4)
    if lucky ==0:
        莲稚 "[my.cheng]，太后今天不见客，请您改日再来吧。"
        jump 皇宫界面
    elif lucky ==1:
        莲稚 "真不巧，太后今日前往奉天楼祈福了。[my.cheng]，您请回吧。"
        jump 皇宫界面
    else:
        $ taihoumeet = taihoumeet +1
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        "过了一会儿……"
        show 莲稚 at chara
        莲稚 "奴婢这就带您过去。"
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        $ lucky = renpy.random.randint(0,4)
        if month > 1 and month < 5:
            if lucky == 0:
                "太后正坐于主位，而面前却有棋盘，她一人独自下棋，抬首看了眼你。"
                太后 "[cheng]起来罢，可会对弈？"
                menu:
                    "会，陪太后下棋":
                        hide 太后
                        "坐太后身旁，时不时于太后说些话。身旁那香炉散发的香味总是让你多注意几番。那里头的香，很是好闻，与这微微带着些许花香的微风混在一起，美妙也。"
                        "过了许久，一局过去。"
                        if my.xinji > 800:
                            太后 "哀家输了，皇上偶尔都会输给哀家，[cheng]很是厉害，竟这般会。"
                        else:
                            太后 "[cheng]这可是输了，不过无碍，许久无人陪哀家下棋了，哀家下得很是快活。"
                    "不会，在一旁陪太后说话":
                        太后 "那便罢了，技多不压身，[cheng]还是学学的好。"
                        我 "臣妾谨遵太后娘娘教诲。"
                        hide 太后
                        "坐太后身旁，时不时于太后说些话。身旁那香炉散发的香味总是让你多注意几番。那里头的香，很是好闻，与这微微带着些许花香的微风混在一起，美妙也。"
                        "不久，太后有些乏了，便跪安了。"


            elif lucky == 1:
                太后 "[cheng]来得正好，尝尝哀家的手艺，这是皇上给的两种茶，看看喜欢喝哪个，尝尝便是。"
                menu:
                    "碧螺春":
                        pass
                    "信阳毛尖":
                        pass

                太后 "这茶映着外头百花齐放的佳境，很是契合。"
            elif lucky == 2:
                太后 "[cheng]来了？正好哀家想去院子头走走，你同哀家一起吧。"
                我 "是。"
                $ bg("建章宫外")
                太后 "[cheng]可喜这杜鹃？哀家倒很是喜欢。"
                "的确放眼望去，丛中牡丹居多，颜色各不相同，但不会有其中一朵最为娇艳突出。"
                太后 "随哀家在外头喝茶赏景罢。"
            elif lucky == 3:
                太后 "方才有一琴女给哀家奏了曲，倒是不怎样，哀家给打发去宫外了。"
                太后 "这人得识趣，装作清高还想要名利，真是惹得哀家发笑。"
            else:
                太后 "哀家前些日子又盘了盘宫中的账务，隐隐感觉有些地方似乎有些出入，[cheng]花销可够？"
        elif month > 4 and month < 8:
            if lucky == 0:
                "太后正坐于主位，而面前却有棋盘，她一人独自下棋，抬首看了眼你。"
                太后 "[cheng]起来罢，可会对弈？"
                menu:
                    "会，陪太后下棋":
                        hide 太后
                        "坐太后身旁，陪太后一同下棋，不远处的一鱼缸子总是让你不由自主的看去，里头的鱼儿娇小可爱，在这盛夏里，宛若一抹清凉萦绕心头。"
                        "过了许久，一局过去。"
                        if my.xinji > 800:
                            太后 "哀家输了，皇上偶尔都会输给哀家，[cheng]很是厉害，竟这般会。"
                        else:
                            太后 "[cheng]这可是输了，不过无碍，许久无人陪哀家下棋了，哀家下得很是快活。"
                    "不会，在一旁陪太后说话":
                        太后 "那便罢了，技多不压身，[cheng]还是学学的好。"
                        我 "臣妾谨遵太后娘娘教诲。"
                        hide 太后
                        "坐太后身旁，陪太后一同下棋，不远处的一鱼缸子总是让你不由自主的看去，里头的鱼儿娇小可爱，在这盛夏里，宛若一抹清凉萦绕心头。"
                        "不久，太后有些乏了，便跪安了。"

            elif lucky == 1:
                太后 "来得正好，尝尝哀家的手艺，虽现下酷暑难耐，但这茶可是凉水所泡，快些试试。"
                menu:
                    "安吉白茶":
                        pass
                    "白牡丹":
                        pass

                太后 "尝起来可真是清热解渴。"
            elif lucky == 2:
                太后 "[cheng]可要跟哀家一同去奉天楼，哀家正要去一番。"
                我 "臣妾遵命"
                scene 奉天楼 with dissolve
                "一路虽热，但太后体恤，唤人拿上油纸伞，晒不着又有丝丝风吹，便不觉太热。"
                scene 望仙殿 with dissolve
                show 太后 at chara
                太后 "偶尔来来，总是可得那么一丝平静。"
            elif lucky == 3:
                太后 "哀家就喜欢听戏曲，你瞧瞧那些角儿，每个都有各自特色，又颇为真实。"
                太后 "院子里的人在那唱着那《梨花颂》，声音婉转。跪安后，那曲儿好有些余音绕梁。"
            else:
                太后 "哀家刚从御花园回来，[cheng]可有觉着有些花似没养好？方才一路上也没觉着有宫人浇花，想来是又不知上哪偷懒去了，得好好整顿这方奖罚才是。"

        elif month > 7 and month < 11:
            if lucky == 0:

                "太后正坐于主位，而面前却有棋盘，她一人独自下棋，抬首看了眼你。"
                太后 "[cheng]起来罢，可会对弈？"
                menu:
                    "会，陪太后下棋":
                        hide 太后
                        "坐太后身旁，陪太后一同下棋。窗外忽一阵秋风入屋，那风还伴着一片落叶飘落脚边，而这秋风并不让人觉着冷，反倒再朝窗外看去，秋色浓得很是喜欢。"
                        "过了许久，一局过去。"
                        if my.xinji > 800:
                            太后 "哀家输了，皇上偶尔都会输给哀家，[cheng]很是厉害，竟这般会。"
                        else:
                            太后 "[cheng]这可是输了，不过无碍，许久无人陪哀家下棋了，哀家下得很是快活。"
                    "不会，在一旁陪太后说话":
                        太后 "那便罢了，技多不压身，[cheng]还是学学的好。"
                        我 "臣妾谨遵太后娘娘教诲。"
                        hide 太后
                        "坐太后身旁，陪太后一同下棋。窗外忽一阵秋风入屋，那风还伴着一片落叶飘落脚边，而这秋风并不让人觉着冷，反倒再朝窗外看去，秋色浓得很是喜欢。"
                        "不久，太后有些乏了，便跪安了。"

            elif lucky == 1:
                太后 "[cheng]来得正好，秋时的茶叶颇多，哀家沏了两壶，都是皇上让人送来的上好的茶叶，快些尝尝。"
                menu:
                    "大红袍":
                        pass
                    "铁观音":
                        pass

                太后 "哀家最喜这秋季，无需百花齐放，只是落叶几许便可感其美无比。"
            elif lucky == 2:
                太后 "[cheng]来啦？同哀家去院子里转转吧。"
                我 "臣妾遵命。"
                hide 太后
                $ bg("建章宫外")
                with dissolve
                show 太后 at chara
                太后 "[cheng]瞧瞧这院子景色，细看总是有那么一丝不同。"
                "院中石阶尽是落叶零散，有的花却正在盛开，有的因叶落，只剩枝丫，而有的还正茂盛，树绿浓荫。"
                太后 "太后：哀家倒是有些想听个曲儿。"
            elif lucky == 3:
                太后 "进来便见着一穿得有些媚俗的女子被带了下去，看那头上饰物，应地位不高。"
                太后 "[cheng]来了，可是见着方才那被拖下去的？呵，摆弄骚姿的货色，竟只因脸蛋有几分好看便自学些舞姿，跑来哀家这摆弄，哀家老了可不傻。"
            else:
                太后 "最近入宫的那批舞女竟有混水摸鱼的，技不如人还搞动作上位，又有何用呢？哀家今儿去巡视一番，便把这几个没用的货色给轰走了。"
                太后 "[cheng]可得擦亮眼睛，这宫里头，林子大什么都有，总有那么几个是混吃混喝的白眼狼。"
        else:

            if lucky == 0:
                "太后正坐于主位，而面前却有棋盘，她一人独自下棋，抬首看了眼你。"
                太后 "[cheng]起来罢，可会对弈？"
                menu:
                    "会，陪太后下棋":
                        hide 太后
                        "坐太后身旁，陪太后一同下棋。透过窗子看去，外头那院子设计很妙，花草树木高低有序却又相互交错，哪怕现都裹上雪，都可感觉这景就是为了这窗做的。"
                        "过了许久，一局过去。"
                        if my.xinji > 800:
                            太后 "哀家输了，皇上偶尔都会输给哀家，[cheng]很是厉害，竟这般会。"
                        else:
                            太后 "[cheng]这可是输了，不过无碍，许久无人陪哀家下棋了，哀家下得很是快活。"
                    "不会，在一旁陪太后说话":
                        太后 "那便罢了，技多不压身，[cheng]还是学学的好。"
                        我 "臣妾谨遵太后娘娘教诲。"
                        hide 太后
                        "坐太后身旁，陪太后一同下棋。透过窗子看去，外头那院子设计很妙，花草树木高低有序却又相互交错，哪怕现都裹上雪，都可感觉这景就是为了这窗做的。"
                        "不久，太后有些乏了，便跪安了。"

            elif lucky == 1:
                太后 "[cheng]来了，起来罢，外头冷得很，快些把外衣褪去来哀家这吧，离火近些暖和。喝些热茶罢，现茶都容易凉了，快趁热。"
                menu:
                    "熟普洱":
                        pass
                    "茉莉花":
                        pass

                太后 "这入冬了，哀家便不愿四处走动了，哀家不喜这一尘不染的日子，总感觉这令哀家不适。"
            elif lucky == 2:
                太后 "[cheng]来了便坐吧，这有玉米羹，还热乎着，快些喝喝暖和暖和。"
                我 "臣妾多谢太后娘娘。"
                "窗外白茫茫，还有寒风夹杂着些许雪花吹来，太后示意宫女将窗关上，但仍有丝丝寒风透过缝隙而入。"
                太后 "这般冷的天儿，哀家都不愿怎么动弹了。"
            elif lucky == 3:
                太后 "[cheng]来了便坐罢。前些日子哀家，可是贬了个掖庭管事的去，竟敢议论哀家，还议论宫中妃嫔，一个麻雀还想变凤凰，就这点手段都没有还敢议论。"
            else:
                太后 "哀家瞧[cheng]，可是没怎么吃好都瘦了？"
                太后 "说来哀家近日碰着个想趁哀家不在时爬皇上床的，还真是不自量力，自个什么货色还不清楚？竟还敢偷哀家的衣裳。"
    hide 太后
    $ Taihoulike_Up(my,2)

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面



label 擅权太后剧情2(place):
    $ taihou2 = True
    $ fz = renpy.random.choice(Npcmeet)
    show 太后 at chara
    "你正准备给太后行礼，却又有一人前来，你定睛一看，是[fz.cheng]。"
    hide 太后
    show fz at chara
    if fz.level < my.level:
        "[fz.hao][fz.weifen] [fz.name]" "臣妾见过太后娘娘。"
        我 "请[fz.cheng]安。"
    else:
        "[fz.hao][fz.weifen] [fz.name]" "臣妾见过太后娘娘，见过[my.cheng]。"
    hide fz
    show 太后 at chara
    太后 "都平身罢。哀家今儿出门可是碰着什么头彩了，竟一出门便见着两位美人儿呢。"
    menu:
        "嫔妾怎美得过太后娘娘":
            if fz.taihoulike > my.taihoulike:
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "就是，明明娘娘更美才是。"
                "[fz.hao][fz.weifen] [fz.name]" "娘娘如今芳华依旧，谁能比得上？"
                hide fz
                show 太后 at chara
                太后 "怎就成了哀家了，真是斗不过你们这一张张嘴。"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "娘娘可是要四处逛逛？"
                hide fz
                show 太后 at chara
                太后 "哀家正有此意。"
                太后 "[fz.cheng]，你陪着哀家吧。"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "（欣喜）臣妾遵命。"
                hide fz
                "二人离去。"
                $ Taihoulike_Up(fz,2)
                call 后宫游玩 (place=place) from _call_后宫游玩_6
            else:
                太后 "这嘴儿可真甜，哀家老了，怎比得上你们。"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "怎有，娘娘还是芳华依旧呢。"
                hide fz
                show 太后 at chara
                太后 "（不悦的看向[fz.cheng]）哦？这么说来是说哀家真老了？"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "（一慌）不，不是，嫔妾不是这个意思。"
                hide fz
                show 太后 at chara
                太后 "真是扫兴，罢了罢了 ，你退下吧。"
                太后 "[aicheng]，随哀家四处走走。"
                我 "是。"
                hide 太后
                "同太后信步闲谈。"
                $ Taihoulike_Up(my,2)
        "娘娘哪里的话，明是[fz.cheng]更美":

            if fz.taihoulike > my.taihoulike:
                太后 "哦？[my.cheng]言下倒也不是不对。"
                hide 太后
                show fz at chara
                if fz.level < my.level:
                    "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]自谦也就罢了，太后娘娘就知道拿臣妾打趣。"
                else:
                    "[fz.hao][fz.weifen] [fz.name]" "[my.cheng]谬赞。太后娘娘，您可别拿臣妾打趣了。"
                hide fz
                show 太后 at chara
                太后 "哈哈哈，你这丫头，哀家正儿八经夸你，怎就成打趣了？"
                我 "（想说什么，却插不上嘴。只能见着她们二人相谈甚欢。）"
                我 "（太后似在故意绕开我的话茬……）"
                太后 "[fz.cheng]，随哀家走走。[my.cheng]先跪安罢。"
                我 "是。"
                hide 太后
                "二人离去。"
                $ Taihoulike_Up(fz,2)
                call 后宫游玩 (place=place) from _call_后宫游玩_7
            else:
                太后 "[aicheng]可真是谦虚了，哀家倒是觉着你看着更是舒服。（看了[fz.cheng]一眼，脸上似带着几分傲气。）"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "……（垂首，一时无话。）"
                hide fz
                show 太后 at chara
                太后 "[aicheng]，随哀家走走。[fz.cheng]就先跪安罢。"
                hide 太后
                show fz at chara
                "[fz.hao][fz.weifen] [fz.name]" "是，臣妾告退。"
                hide fz
                "同太后信步闲谈。"
                $ Taihoulike_Up(my,2)
        "（谦逊垂首，默然不语）":
            hide 太后
            show fz at chara
            "[fz.hao][fz.weifen] [fz.name]" "太后娘娘谬赞了。"
            hide fz
            show 太后 at chara
            太后 "罢了，你们陪哀家走走吧。"
            "你与[fz.cheng]齐声称是。"
            hide 太后
            "三人同游，其乐融融。"
            $ Taihoulike_Up(my,1)
            $ Taihoulike_Up(fz,1)
            $ fz.like + 1
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面





label 建章宫_宽和:
    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng

    show 莲稚 at chara
    if my.taihoulike>30 and taihou1 == False:
        $ taihou1 = True
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        show 莲稚 at chara with dissolve
        莲稚 "[my.cheng]来得可真是时候，娘娘唤你快些进去呢。"
        hide 莲稚
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        "殿内，太后娘娘于那儿不知忙活些什么，案上乱通通的，尽是长得一致的桂花糕。"
        menu:
            "行礼问安":
                pass
        太后 "无需多礼，起来便是。"
        太后 "来哀家身旁，帮哀家尝尝这些桂花糕到底有何不同。"
        我 "（无法拒绝）是。"
        太后 "（将筷子递到你的面前。）"
        menu:
            "嫔妾觉着这盘桂花味较重的好吃。":
                pass
            "嫔妾觉着这甜味更浓的更是好吃些。":
                pass
            "嫔妾觉着这桂花味淡如点睛的更好入口。":
                pass
            "嫔妾觉着这甜味较轻的好些。":
                pass
            "嫔妾觉着这桂花与甜味中规中矩的正好。":
                pass
        太后 "如此也，这是哀家唤一御膳房厨子做的，哀家倒是忽有些好奇各种不同桂花糕有何等区别，这不，倒腾来了一堆。"
        太后 "这不正巧，你来得正是时候，快些陪哀家一同吃了才是，吃不完的拿点回去打赏给奴才们也是不错。"
        menu:
            "谢过太后":
                pass
        "果真吃不下，最后剩了不少，便依着太后意思带回寝宫赏给奴才们了。"
        $ taihoumeet = taihoumeet +1
        $ Taihoulike_Up(my,2)
        $ timenum = timenum +1
        $ AP = AP -1
        jump 皇宫界面
    else:


        pass

    $ lucky = renpy.random.randint(0,4)
    if lucky ==0:
        莲稚 "[my.cheng]，太后今天不见客，请您改日再来吧。"
        jump 皇宫界面
    elif lucky ==1:
        莲稚 "真不巧，太后今日前往奉天楼祈福了。[my.cheng]，您请回吧。"
        jump 皇宫界面
    else:
        $ taihoumeet = taihoumeet +1
        莲稚 "奴婢见过[my.cheng]。"
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        "过了一会儿……"
        show 莲稚 at chara
        莲稚 "奴婢这就带您过去。"
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        if my.taihoulike >50:
            $ cheng = aicheng
        else:
            $ cheng = my.cheng
        $ lucky = renpy.random.randint(0,4)
        if month > 1 and month < 5:
            if lucky == 0:
                太后 "快些起身罢，哀家近日在宫里闷得慌，方才闻御花园那金盛菊开了一片。快，随哀家去外头逛逛。"
                hide 太后
            elif lucky == 1:
                "进去便见着太后眉头微皱，托着下巴不知在想些什么。"
                menu:
                    "请安，问其忧虑":
                        pass
                太后 "[cheng]起来罢。唉无碍，不过兴许年纪大了，睡时总多梦，睡得很不是安稳。哀家已吩咐人点安神香了。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来哀家这，快看这些花，你说哪个好。"
                menu:
                    "丁香":
                        pass
                    "芍药":
                        pass
                    "君子兰":
                        pass
                太后 "那哀家就吩咐人种这盆罢，来，进来喝口茶。"
                hide 太后
            elif lucky == 3:
                太后 "原是[cheng]，快些起身罢，来坐哀家边上。"
                太后 "近日皇上给哀家送来了几本传记，你看看有没有喜欢的，拿去看便是。"
                hide 太后
            else:
                "进去便见着太后正在瞧这屋檐下的什么，走近看去，原那屋檐下是一燕子窝。"
                太后 "哎呦瞧这燕子，哀家都不舍得弄掉它，你看叽叽喳喳的，多热闹。"
                hide 太后
        elif month > 4 and month < 8:
            if lucky == 0:
                太后 "快些起身罢，哀家近日在宫里闷得慌，方才闻御花园一亭子爬满了牵牛。快，随哀家去外头逛逛。"
                hide 太后
            elif lucky == 1:
                "进去便见着太后眉头微皱，托着下巴不知在想些什么。"
                menu:
                    "请安，问其忧虑":
                        pass
                太后 "[cheng]起来罢。只是这天儿太热，把哀家那盆刚种下不久的花儿晒焉了，罢了罢了，还不如陪哀家唠唠，喝几口茶。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来哀家这，快看这些花，你说哪个好。"
                menu:
                    "金露花":
                        pass
                    "夏瑾":
                        pass
                    "三角梅":
                        pass
                太后 "那哀家就吩咐人种这盆罢，来，快些进来，哀家已唤人泡好热茶了。可要喝个莲子羹？"
                hide 太后
            elif lucky == 3:
                太后 "原是[cheng]，快些起身罢，来坐哀家边上。"
                太后 "近日皇上给哀家送来了几个玉石块，说是哀家喜欢什么样式便吩咐人下去雕出来，你瞧哪个更适合做簪子？"
                hide 太后
            else:
                "进去便见太后正让宫女拿着一水盆，走近细看，里头竟然是好几条金鱼。"
                太后 "[cheng]来了，哀家正吩咐人打理池子呢，夏里那青苔长得可快了，不打理都要望不到池底了。"
                hide 太后
        elif month > 7 and month < 11:
            if lucky == 0:
                太后 "快些起身罢，现都起凉风了，衣裳可得多穿些，别凉着了。你瞧你头上，都有落叶挂着了。"
                hide 太后
            elif lucky == 1:
                "进去便见着太后眉头微皱，托着下巴不知在想些什么。"
                menu:
                    "请安，问其忧虑":
                        pass
                太后 "无碍，起身罢。不过看着这秋叶落，想起了些许往事罢。"
                太后 "过来陪哀家唠唠吧。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来哀家这，秋色正浓，哀家想多添几盆花，你瞧哪个好？"
                menu:
                    "紫茉莉":
                        pass
                    "美女樱":
                        pass
                    "蝴蝶兰":
                        pass
                太后 "那哀家就吩咐人种这盆罢，来，进来，哀家近日习得用落叶做书签，这便教你。"
                hide 太后
            elif lucky == 3:
                太后 "原是[cheng]，快些起身罢，来坐哀家边上。"
                太后 "近日皇上给哀家送来了只松鼠崽子，你瞧，多有趣，还在这扒拉着坚果呢。"
                hide 太后
            else:
                "进去便见太后正看着书，正准备行礼，被太后身旁的宫女示意先不要做声。"
                我 "（安静在旁边候着。）"
                太后 "（抬首见你，连忙道）[cheng]来了，怎没人告诉哀家，来，这天儿凉快，看书正是适合呢，就不看什么四书五经了，这传说什么的多有趣。"
                hide 太后
        else:

            if lucky == 0:
                太后 "快些起身罢，这天儿冷得很，快些起来吧，瞧你身上都是雪，快去火便烤烤，暖和暖和身子。"
                hide 太后
            elif lucky == 1:
                "进去便见着太后立于窗边，望着这白茫茫的雪景，不知思绪什么。"
                menu:
                    "请安，问其忧虑":
                        pass
                太后 "[cheng]起来罢，地凉，来哀家这坐着烤火暖和几分罢。也无碍，不过是又犯老毛病了，一入冬这腿就生疼，老了……"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来哀家这，瞧这院子入冬便没什么色，皆白茫茫的毫无生气，便唤人拿来了这几盆花，你瞧哪个好？"
                menu:
                    "洋琼花":
                        pass
                    "蟹爪兰":
                        pass
                    "一品红":
                        pass
                太后 "那哀家就吩咐人种这盆罢，来，快些进来，哀家已唤人泡好热茶了。可要喝个莲子羹？"
                hide 太后
            elif lucky == 3:
                太后 "原是[cheng]，快些起身罢，来坐哀家边上。"
                太后 "近日皇上给哀家送来了几匹新布料，怪厚实的，改日唤人给你也做件衣裳。"
                hide 太后
            else:
                "进去便见太后正将梅枝插于瓶中，那梅枝上的梅开得正红。"
                太后 "[cheng]来了，哀家正摆弄着插花，[cheng]可要来试试？"
                hide 太后
    $ Taihoulike_Up(my,2)

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面




label 建章宫_避世:
    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    show 莲稚 at chara
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    $ taihoumeet = taihoumeet +1
    莲稚 "奴婢见过[my.cheng]。"
    if my.taihoulike>30 and taihou1 == False:
        $ taihou1 = True
        莲稚 "太后今儿不见客，正要去为国祈福，还请改日再……"
        莲稚 "太后娘娘。"
        hide 莲稚
        show 太后 at chara with dissolve
        太后 "（从身后的宫门内缓缓行来。）"
        menu:
            "问安":
                pass
        太后 "是[cheng]呀，免礼罢 。怎今儿来得这般早。"
        太后 "既然[cheng]今儿来得 这般巧，若是无事，可要陪哀家走一遭？"
        menu:
            "推辞":
                太后 "如此哀家也不强求，哀家就先走了，再说可得耽误时辰了。"
                hide 太后 with dissolve
                jump 皇宫界面
            "一同随行":
                太后 "（只点头，并未回话，走在前头。）"
                hide 太后 with dissolve
                scene 奉天楼 with dissolve
                "路上与太后并没多少交谈， 有一搭没一搭，但太后似乎挺高兴 。"
                scene 望仙殿 with dissolve
                "到望仙殿后，跟着太后做着一致的祈福步骤，直到礼成。"
                show 太后 at chara
                太后 "嗯，[cheng]还挺有心 ，此举可是善举，可得多行才是。"
                太后 "自行回去罢，哀家也乏了"
                hide 太后
                $ taihoumeet = taihoumeet +1
                $ Taihoulike_Up(my,2)
                $ timenum = timenum +2
                $ AP = AP -2
                jump 皇宫界面
    elif my.taihoulike>80 and taihou3 == False and len(my.kids) > 0:
        $ taihou3 = True
        莲稚 "娘娘方才才念叨着宫里闷得慌，快些进去罢。"
        hide 莲稚
        $ bg("建章宫内")
        show 太后 at chara
        太后 "（见着你一脸欣喜还未等你行礼便拉着你到她身旁的侧位去，丝毫不在意身段。）"

        太后 "[cheng]，快来哀家旁坐着。来人，快快备好茶。 "
        我 "（笑容满面）娘娘今日为何如此客气？"
        "（一同聊起各种趣事，欢笑不断。）"
        if my.huaiyun > 0:
            太后 "[cheng]现有孕在身，可得好生照料身子才是，近日皇上给了哀家一根人参，可是上等的品质，等会回去时，可不用跟哀家客气，拿回去让御膳房的人好生伺候着，可别委屈了。"
            menu:
                "替腹中孩子先谢过太后娘娘。":
                    pass
                "有劳太后娘娘挂心了，定会好生照料的。":
                    pass
                "（行礼言谢，并未多言）":
                    pass
                "得这番福分，孩子还未出生呢，怕是就要被太后娘娘宠坏了":
                    pass
            "唠嗑许久，还吃了些许点心。"
            太后 "哎呀，哀家改日定要在皇上面前夸夸你这孩子，不像别的，都不知来看看哀家，今儿时辰也晚了哀家唤人送你回去。"
            "说罢，还专门嘱咐宫人送你回寝宫方才放心。"
            hide 太后
            $ taihoumeet = taihoumeet +1
            $ Taihoulike_Up(my,2)
            $ timenum = timenum +1
            $ AP = AP -1
            jump 皇宫界面
        else:
            $ tempkid = renpy.random.choice(my.kids)
            太后 "说来也许久未见着[tempkid.name]了，若是得空了 ，可得带[tempkid.name]来看看哀家，哀家这儿清静得很，近日还得了只鹦鹉，想来孩子定会喜欢。"
            menu:
                "改日定带[tempkid.name]来":
                    pass
                "娘娘说得极是，今儿倒是[aicheng]想得不周":
                    pass
                "[tempkid.name]调皮得很，改日带其过来，娘娘便知道咯":
                    pass
                "娘娘有所不知，[tempkid.name]最喜的便是鸟儿喏":
                    pass
            太后 "如此甚好，晚些皇上会来于哀家一同用膳，[cheng]不如留下一同？"
            我 "多谢娘娘！"
            "不久，皇上果真前来陪太后用膳，并未多言什么，只就像一寻常家宴一般，只是少了歌舞。"
            $ taihoumeet = taihoumeet +1
            $ Taihoulike_Up(my,2)
            $ timenum = timenum +2
            $ AP = AP -1
            jump 皇宫界面
    else:


        pass
    $ lucky = renpy.random.randint(0,4)

    if lucky ==0:
        莲稚 "[my.cheng]，太后今天不见客，请您改日再来吧。"
        jump 皇宫界面
    elif lucky ==1:
        莲稚 "真不巧，太后今日前往奉天楼祈福了。[my.cheng]，您请回吧。"
        jump 皇宫界面
    else:
        莲稚 "还请让奴婢为您通禀一声。"
        hide 莲稚
        "过了一会儿……"
        show 莲稚 at chara
        莲稚 "奴婢这就带您过去。"
        $ bg("建章宫内")
        with dissolve
        show 太后 at chara
        $ lucky = renpy.random.randint(0,4)
        if month > 1 and month < 5:
            if lucky == 0:
                太后 "咳……[cheng]坐罢。"
                menu:
                    "问安":
                        pass
                太后 "哎，前些日子受了些许风寒，倒是大意了，不过无碍。喝些暖茶罢。"
                hide 太后
            elif lucky == 1:
                太后 "[cheng]，来了便坐吧。方才御膳房送来了桃花酥，可要尝尝？"
                menu:
                    "尝尝味道":
                        pass
                我 "（品着花茶，尝着桃花酥。）"
                我 "（果然太后这儿的，味道都更好喏。）"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来了！哎呦来得正是时候，你看这鹦鹉可讨人喜了。"
                "只见一鹦鹉在那一直念叨着吉祥祝福的话，想来是皇上训好送给太后的。"
                hide 太后
            elif lucky == 3:
                太后 "[cheng]来看哀家了？听宫人们说，今日外头天气不错。"
                我 "回太后的话，今日天气晴好，确实不错，适宜外出走动。"
                太后 "那你陪哀家在院子里走走吧。"
                我 "是。"
                $ bg("建章宫外")
                "你同太后走到院中，太后坐到院中石椅上，双眼望那正盛开的山茶。"
                太后 "迟日江山丽，春风花草香。"
                hide 太后
            else:
                太后 "哀家近日，唤人来种多了株玉兰，若是[cheng]喜欢，哀家也唤人给你拿去一盆。"
                我 "（颔首）臣妾多谢太后娘娘美意。"
                hide 太后
        elif month > 4 and month < 8:
            if lucky == 0:
                太后 "这日可真是热……瞧[cheng]这晒得脸儿红红的，来人给[cheng]扇扇。"
                menu:
                    "谢过好意，问安":
                        pass
                太后 "无碍无碍，哀家不过是觉这酷暑难消，已唤人拿些冰来了。"
                hide 太后
            elif lucky == 1:
                太后 "[cheng]来了便坐吧。方才御膳房送来了西瓜，都切好了，消消暑罢。"
                menu:
                    "尝尝西瓜":
                        pass
                我 "（这夏日里的西瓜格外的甜。）"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来了！哎呦来得正是时候，你看这鹦鹉可讨人喜了。"
                "只见一鹦鹉在那一直念叨着，让太后正午时分别出门什么的话，想来是皇上训好送给太后的。"
                hide 太后
            elif lucky == 3:
                太后 "[cheng]来看哀家了？听宫人们说，今日外头天气不错。"
                我 "回太后的话，今日日头没前几日那么烈了，还时有清风吹风，反倒有几分凉爽。"
                太后 "那你陪哀家在院子里走走吧。"
                我 "是。"
                $ bg("建章宫外")
                "你同太后走到院中，同太后到院中一树下乘凉，她双眼望那正盛开的翠菊。"
                太后 "绿树浓荫夏日长，楼台倒影入池塘。"
                hide 太后
            else:
                太后 "哀家近日，唤人来种那木槿，若是[cheng]喜欢，哀家改日日唤人去替你也栽一株，不过得秋时，才可见其花。"
                hide 太后
        elif month > 7 and month < 11:
            if lucky == 0:
                太后 "秋意渐浓，近儿[cheng]可得注意添几件衣裳，别着凉了。"
                menu:
                    "谢过好意，问安":
                        pass
                太后 "哀家也命人添了几件，皇上也挂记着哀家，身儿好着呢。"
                hide 太后
            elif lucky == 1:
                太后 "[cheng]来了便坐吧。方才御膳房送来了桂花糕，可是哀家院里那棵桂花所做，尝尝如何。"
                menu:
                    "尝尝糕点":
                        pass
                "太后今日看起来十分欢喜，一直聊着趣事，品着新茶，很是满足。"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来了！哎呦来得正是时候，你看这鹦鹉可讨人喜了。"
                "只见一鹦鹉在那，念叨着让娘娘注意穿衣，别凉着了的话，想来是皇上训好送给太后的。"
                hide 太后
            elif lucky == 3:
                太后 "[cheng]来看哀家了？听宫人们说，今日外头天气不错。"
                我 "回太后的话，今日秋高气爽，适宜外出走动。"
                太后 "那你陪哀家在院子里走走吧。"
                我 "是。"
                $ bg("建章宫外")
                "秋风萧萧却满是桂花香，一地落叶混着落花。"
                "你同太后走到院中，太后坐于桂花树下听戏。那戏子在落叶中比划嚷嚷，尽是意境。"
                太后 "秋风生渭水，落叶满长安。"
                hide 太后
            else:
                太后 "瞧瞧，哀家夏时种下的木槿，现开得很是红艳，与这落叶一同，很是美哉。"
                hide 太后
        else:
            if lucky == 0:
                太后 "天儿冷得很，快喝些茶暖暖身吧，咳咳……."
                menu:
                    "问安":
                        pass
                hide 太后
                show 莲稚 at chara
                莲稚 "娘娘，药煎好了，快趁热喝吧。"
                hide 莲稚
                show 太后 at chara
                太后 "老了，没什么大碍，咳咳……冷着罢。"
                hide 太后
            elif lucky == 1:
                太后 "[cheng]来了便坐吧。方才御膳房送来了生姜汤，快喝一些暖暖身子。"
                menu:
                    "尝尝姜汤":
                        pass
                我 "（姜汤入口暖意生，瞬间寒意皆散，暖和得很。）"
                hide 太后
            elif lucky == 2:
                太后 "[cheng]来了！哎呦来得正是时候，你看这鹦鹉可讨人喜了。"
                "只见一鹦鹉在那，念叨着让娘娘多坐暖炉边，烤烤火的话，想来是皇上训好送给太后的。"
                hide 太后
            elif lucky == 3:
                太后 "[cheng]来看哀家了？听宫人们说，今日外头雪景很美。"
                我 "回太后的话，路上都是银装素裹，美不胜收呢。"
                太后 "那你陪哀家在院子里走走吧。"
                我 "是。"
                $ bg("建章宫外")
                "四周一片皆白，太后身披斗篷立于院中赏那独梅，雪不会便在其肩上堆了几许。"
                太后 "墙角数枝梅，凌寒独自开。"
                hide 太后
            else:
                太后 "这梅开得呀，总是让哀家想起一姑娘，那身上的傲气，就跟这梅花似的，可惜呀……"
                hide 太后


    $ Taihoulike_Up(my,2)

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面

label 避世太后剧情2(place):
    $ taihou2 = True
    show 太后 at chara
    "她本在池边唉声叹气 ，闻你行礼，连忙回首，喜出望外。"
    太后 "是[aicheng]呀，免礼免礼，正愁没人陪哀家，来得倒是时候。"
    menu:
        "哄太后开心":
            太后 "行了行了，就你这点小伎俩 ，哀家还看不出来吗？[aicheng]这份心，哀家领了，罢了罢了。 "
            我 "臣妾只是不想看到娘娘不高兴。"
            "陪着太后闲聊许久，太后心情似乎好了些许，慢慢的也开始有了笑容。"
            太后 "哀家这腰没你好，在外头许久倒是有些乏了，你便先退下罢。"
            我 "是。"
            hide 太后
            $ Taihoulike_Up(my,1)
            call 后宫游玩 (place=place) from _call_后宫游玩_8
        "问为何叹气":


            太后 "你瞧，方才哀家于此依池看这经文，谁知一个不甚，竟掉入了池中。这经文可是奉天楼那边给的，虽说是手抄本，但也是神圣之物，只恐怕神明要怪罪下来。"
            menu:
                "向太后要来经文，为太后再抄一份":
                    太后 "由此甚好，如此便交给[aicheng]你了，但经文可容不得半分差错，抄写时心中需无杂念，若是办的不妥，可是对神明不敬。"
                    我 "臣妾明白。"
                    太后 "（同身旁宫女交待了几句。）"
                    太后 "哀家已安排了，晚些便会有人将经文给你送去，可得好生保管，交于你，哀家兴许可放心不少。"
                    我 "请娘娘放心，此事绝无半点差池。"
                    太后 "时候不早了，哀家也该回去了。改日[aicheng]再来找哀家时，把经文带上便是。"
                    hide 太后
                    $ Taihoulike_Up(my,3)
                    $ timenum = timenum +1
                    $ AP = AP -1
                    jump 皇宫界面
                "神仙慈悲，愿陪太后同去请罪":
                    太后 "[aicheng]此言也并非无理，而又有此心的话，便随哀家走一遭罢。"
                    hide 太后
                    scene 望仙殿 with dissolve
                    "同太后在殿内跪了许久，在被望仙殿当值者告知神明并未动怒以后方才放心离开。"
                    show 太后 at chara
                    太后 "辛苦[aicheng]陪哀家来这一遭了。"
                    我 "臣妾无碍，太后娘娘心诚，定能打动上天，庇佑国祚昌盛、娘娘与皇上康健如意呢。"
                    太后 "哈哈哈，[aicheng]的嘴向来这样甜。"
                    太后 "莲稚，晚些回了建章宫，你将那支[acc07.name]给[my.cheng]送去。"
                    hide 太后
                    show 莲稚 at chara
                    莲稚 "奴婢遵命！"
                    hide 莲稚
                    show 太后 at chara
                    我 "臣妾谢娘娘赏赐。"
                    hide 太后
                    "得到[acc07.name]×1。"
                    $ kufang.append(acc07)
                    $ Taihoulike_Up(my,3)
                    $ timenum = timenum +2
                    $ AP = AP -2
                    jump 皇宫界面
                "无心之失，神明不会怪罪":
                    太后 "唉，罢了罢了，哀家回头再让旁人再抄录一份便是。 "
                    hide 太后
                    show 莲稚 at chara
                    莲稚 "娘娘可莫要再唉声叹气。娘娘不是说过，叹气多了福分都会被叹出去了？"
                    hide 莲稚
                    show 太后 at chara
                    太后 "对对对，是这么一回事，还是你懂哀家。"
                    太后 "时候不早了，莲稚，咱们回去吧。"
                    hide 太后
                    show 莲稚 at chara
                    莲稚 "是。"
                    hide 莲稚
                    "太后同莲稚聊着天离开了。"
                    $ Taihoulike_Up(my,1)
                    call 后宫游玩 (place=place) from _call_后宫游玩_9


label 建章宫_late:
    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    show 莲稚 at chara
    莲稚 "[my.cheng]，太后已经歇息了。请您改日赶早来吧。"
    jump 皇宫界面

label 建章宫_first:
    $ taihoumeet = 1
    $ bg("建章宫外")
    with dissolve
    show screen notify("建章宫")
    show 莲稚 at chara
    莲稚 "见过[my.cheng]，您今日是来向太后请安的吗？"
    莲稚 "还请让奴婢为您通禀一声。"
    hide 莲稚
    "过了一会儿……"
    show 莲稚 at chara
    莲稚 "奴婢这就带您过去。"
    $ bg("建章宫内")
    with dissolve
    我 "臣妾[my.xing]氏，向太后娘娘请安。"
    show 太后 at chara
    太后 "起来罢。"
    if player == 0:

        if my.familylevel <=4:
            太后 "虎父无犬女，嗯，没给你父亲丢脸。"
        else:
            太后 "你这份心意哀家心领了。"
        if taihouxinge == "宽和":
            太后 "后宫这么些嫔妃啊，像你这样孝顺的可不多哟。"
        elif taihouxinge == "擅权":
            太后 "晓得要来看看哀家，倒是有些心思的。"
        elif taihouxinge == "精敏":
            太后 "懂得孝敬哀家，倒也还算不错。"
        else:
            太后 "哀家自个儿得着清静，你个小女孩儿家的倒也不必常来，免得还沾了些刻板死沉之气。"



        if my.qizhi >800 and my.book + my.cixiu >150:
            太后 "嗯，看得出来是个好孩子。"
            太后 "有像你这样聪明贤惠的姑娘陪伴在皇上身边，哀家也就放心了。"
            menu:
                "太后谬赞了":
                    $ Taihoulike_Up(my,3)
                "其实……臣妾还没有侍寝过呢" if my.shiqin == 0:
                    我 "（羞）"
                    太后 "哦？皇上这些日子都在忙什么呢？"
                    太后 "你放宽心。既然如此，哀家会到皇上那边去招呼一声的。"
                    我 "多谢太后娘娘！"
                    $ mustshiqin = 100
                    $ Taihoulike_Up(my,2)
        else:

            if my.qizhi >800:
                "和太后闲聊了一会儿。"
                hide 太后
                我 "（看起来太后对我有些好感。）"
                $ Taihoulike_Up(my,2)
            elif my.qizhi < 500 and taihouxinge != "避世":
                "和太后闲聊了一会儿。"
                hide 太后
                我 "（看起来太后不太喜欢我。）"
            else:
                "和太后闲聊了一会儿。"
                hide 太后
                我 "（看不出太后的喜恶。）"
                $ Taihoulike_Up(my,1)

    elif player == 1:
        pass
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面


label 建章宫_阿檀:
    $ atan_help_th = True
    $ bg("建章宫外")
    with fade
    show 太后
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    太后 "[cheng]？今日有事找哀家么？"
    menu:
        "奉天楼的阿檀……":
            pass
    if taihouxinge == "宽和" or taihouxinge == "避世":
        if my.taihoulike >= 20:
            $ atan_help.append(2)
            太后 "（叹气）这姑娘竟如此可怜么……"
            太后 "罢了，[cheng]你身在后宫，竟也愿意为她求一个陪伴君侧的机会，可见那姑娘一片痴心，的确感人。"
            太后 "此事安排掖廷去办吧，若有人有异，便说是哀家同意了的。"
        else:
            太后 "（叹气）虽说这阿檀痴心感人，但身为奉天楼司祝，若接入后宫，怕是引得神仙不快……"
            太后 "哀家却是不敢冒这个险。"
            太后 "唉，看她造化罢，旁人帮不上什么忙。"
    else:
        if my.taihoulike >= 50:
            $ atan_help.append(2)
            太后 "（叹气）这姑娘竟如此可怜么……就连哀家也有些想帮她一把了。"
            太后 "况且[cheng]你身在后宫，竟也愿意为她求一个陪伴君侧的机会，可见那姑娘一片痴心，的确感人。"
            太后 "此事安排掖廷去办吧，若有人有异，便说是哀家同意了的。"
        else:
            太后 "（叹气）先不说她是否另有所求，身为奉天楼司祝，若将她接入后宫，怕是引得神仙不快，殃及社稷，岂非因小失大？"
            太后 "此事不要再提。"
    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面

label 建章宫_楚欢:
    $ chuhuan_th = True
    $ bg("建章宫外")
    with fade
    if my.taihoulike >50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    show 莲稚
    莲稚 "奴婢见过[my.cheng]。"
    莲稚 "太后现下不在建章宫……不过估摸着也快回来了。"
    莲稚 "不过估摸着也快回来了。"
    莲稚 "您是改日再来，还是在偏殿等等？"
    我 "嗯……"
    hide 莲稚
    "太后的声音" "你祖父为先皇出生入死，建功立业，如今你入了宫，哀家和皇上自然也会厚待于你。"
    "太后的声音" "若有什么缺的少的，亦或是旁人忘生诽意，你便来同哀家说。"
    show 太后 at zuo
    show 楚欢 at you
    楚欢 笑 "太后娘娘放心，宫里的姐妹对欢儿很好，皇上……也对欢儿很好。"
    太后 "那便好，今个儿倒是辛苦你陪哀家去奉天楼祈福了。"
    楚欢 "这是欢儿的福气，何来辛苦？"
    楚欢 "倒是往后欢儿常来叨扰，您可莫嫌欢儿烦了。"
    太后 "好孩子。"
    楚欢 常 "啊，是[my.cheng]……"
    if my.level <= chuhuan.level:
        楚欢 "见过[my.cheng]。"
    else:
        我 "见过太后娘娘、[chuhuan.cheng]。"
    太后 "[cheng]是来看哀家的？"
    if my.taihoulike < chuhuan.taihoulike:
        太后 "哀家今个儿想和[chuhuan.cheng]聊聊，[cheng]改日再来吧。"
        $ Taihoulike_Up(chuhuan,2)
    else:
        太后 "好了，欢儿就送哀家到这里吧，你回宫休息。"
        楚欢 常 "是……"
        太后 "[cheng]随哀家来吧。"
        我 "是。"
        $ bg("建章宫内")
        with fade
        show 太后
        "同太后闲话家常。"
        $ Taihoulike_Up(my,2)

    $ timenum = timenum +1
    $ AP = AP -1
    jump 皇宫界面


label 太后_专宠指责:
    if my.familylevel == 11 and taihouxinge == "擅权":
        $ bg("寝居")
        show 我的宫女
        我的宫女 "主子，方才太后唤人来传话，说是请主子。"
        menu:
            "抱恙推辞":
                我的宫女 "是，那奴婢这就去转告。"
                "（片刻后……）"
                我的宫女 "主子，太后说必须去……不得抗令。"
                $ my.taihoulike -= 5
            "立刻前去":
                我的宫女 "是，奴婢这就转告那宫女。"
        $ bg("建章宫外")
        show 莲稚
        莲稚 "随奴婢来罢。"
        $ bg("建章宫内")
        show 太后
        "太后正坐于主位之上，双目微合，似在闭目养神。"
        menu:
            "行礼请安":
                pass

        太后 "[aicheng]起来罢。"
        "太后并未正眼瞧你，也并未让你起身，就这么让你一直行礼。不知过了多久，你双脚隐约有些酸痛。"
        太后 "（缓缓端起茶杯，喝了口茶）哀家才见着这有人，原是[my.cheng]来了，哀家等得都乏了，坐吧。"
        太后 "听闻近日皇上经常前去看[my.cheng]，得如此荣宠，想来皇上定是十分喜欢喏。"
        "太后一直说着你独宠后宫，皇上哪都不去，有所影响。"
        太后 "哀家并没什么意思，只是宫中各妃嫔皆有头有脸的，出身皆乃大家闺秀，哪怕八品官员之女，家中也是为朝廷做事，皇上都不多走动走动，这子嗣怎可好？不是哀家说你甚，只是[my.cheng]家中境况，何人不知？得了荣宠便已是八辈子的福分了，可莫要贪咯……"
        menu:
            "臣妾知道":
                $ taidu += 3
            "（默不作声）":
                $ taidu -= 3
        $ my.tags.append(["禁足三月",0,""])
        $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "见罪于太后，被禁足三月。\n"
        $ allstory.insert(0,tempstory2)
        太后 "罢了，也该叫皇上将你放一放了。"
        太后 "传哀家旨意，[my.cheng]禁足三月，无诏不得出。"
        太后 "[my.cheng]跪安罢，哀家乏了。"


    elif my.taihoulike >= 50:
        if taihouxinge == "宽和":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后娘娘唤人来了，说是唤主子去陪陪太后。"
            menu:
                "连忙动身":
                    pass
            我的宫女 "奴婢给主子把发簪摆弄规整些。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "见过[my.cheng]，太后娘娘已在里头候着了，请随奴婢来罢。"
            $ bg("建章宫内")
            show 太后
            太后 "（手里拿着一册诗经，见你进来，方才放下）[aicheng]来啦。"
            menu:
                "行礼请安":
                    pass
            太后 "（摆手示意起身，笑言）起来吧，来，坐哀家这。"
            我 "太后娘娘可是在建章宫里觉着乏了，唤[aicheng]来陪您呐？"
            太后 "哈哈哈，[aicheng]果真懂哀家，唤你来果真不错。来人，去将刚弄好的点心呈上。"
            "与太后闲聊各种，本聊的很是愉快，可太后忽想起什么似的。"
            太后 "（忽严肃的看向你）不过，哀家现想起个事，得与[aicheng]说说才是。"
            太后 "哀家昨儿，有妃子来请安时，竟跟哀家言，说是[aicheng]独占后宫，霸占皇上，有失体统……可有此事？"
            menu:
                "大胆应声":
                    $ xingzi += 5
                    我 "回娘娘，臣妾可没如此！此人定是胡说八道！只是皇上近日多番去臣妾那儿关心臣妾罢。"
                    太后 "你倒是不避讳。"
                    我 "事实如此，臣妾自然不避讳。"
                "默不作声":

                    $ xingzi -= 5
                    太后 "（见你不吭声）怎么？可是哀家所言有假？"
                    我 "不曾有假，只是……"
            太后 "哀家自然知道[aicheng]不过现下盛宠，这些妃嫔见不得这般恩宠不在自个身罢。而事实如何，哀家贵为太后，自然知晓这后宫事。"
            我 "娘娘……"
            太后 "[aicheng]需记着，哀家终是太后，不可保你甚，哀家也需为皇上开枝散叶着想……唉。"
            太后 "为了这子嗣，也为了自个，莫要被妃嫔们的妒忌所扰，[aicheng]还是近日多多举荐皇上去去别宫也不是不可，你可知哀家在说什么？"
            太后 "好了，哀家也有些乏了，[aicheng]跪安罢。"

        elif taihouxinge == "擅权":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后唤人来传话，说是让主子去陪陪太后。"
            menu:
                "抱恙推辞":
                    我的宫女 "是，那奴婢这就去转告。"
                    "（片刻后……）"
                    我的宫女 "主子，太后说必须去……"
                    $ my.taihoulike -= 5
                "立刻前去":
                    我的宫女 "是，奴婢这就转告那宫女。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "见过[my.cheng]，太后正里头等着呢，请随奴婢来罢。"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，双目微合，似在闭目养神。"
            menu:
                "行礼请安":
                    pass

            太后 "[aicheng]起来罢，坐哀家旁。"
            太后 "（只见太后喝了口茶，似想着什么）皇上近日可是常去[aicheng]那？"
            我 "是。"
            太后 "近日有妃嫔跟哀家言，说是[aicheng]独宠后宫，已许久没去别妃嫔宫中……说是[aicheng]蛊惑了皇上心智。"
            太后 "哀家知道蛊惑之言[aicheng]自是没有，但哀家唤人问了，着实皇上近日最常去的便是[aicheng]那儿。"
            太后 "这宫里的妃嫔，皆是为了给皇上开枝散叶的，而不是独享这份荣宠的，哀家信你，但旁人不信，[aicheng]可知晓？"
            menu:
                "臣妾知道":
                    $ taidu += 3
                "（默不作声）":
                    $ taidu -= 3
            太后 "罢了，陪哀家下个棋吧。"
            "对弈几局，输赢皆有。"
            太后 "哀家有些乏了，[aicheng]便回去罢。"


        elif taihouxinge == "避世":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后娘娘唤人来了，说是唤主子去陪陪娘娘，娘娘现已在建章宫里候着了。"
            menu:
                "连忙动身":
                    pass
            我的宫女 "对了主子，这是方才御膳房送来了的糕点，还热着呢。"
            我 "（之前去陪太后时，太后似是说过很是喜吃这点心。）"
            我 "一并带上吧。"
            我的宫女 "是，主子。"

            $ bg("建章宫外")
            show 莲稚
            莲稚 "见过[my.cheng]，太后娘娘已在里头候着了，请随奴婢来罢。"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，手中拿着经文，口中还念着。"
            menu:
                "行礼问安":
                    pass
            太后 "（见你来了，便将手中经文放下，和善笑着）[aicheng]快些起来吧，来，坐哀家这儿。"
            我 "不知娘娘找臣妾何事？"
            太后 "无事，不过是有些无趣，便找你来陪陪哀家罢了，怎么？可是不便？"
            我 "怎有，臣妾高兴着呢。"
            太后 "（太后忽想起什么似的）说来，哀家近日听闻，[aicheng]独占后宫，可有此事？"
            menu:
                "大胆应是":
                    $ xingzi += 5
                    太后 "[aicheng]倒挺实诚的，哀家都不知说甚好。"
                    我 "事实如此，臣妾自然不避讳。"
                    太后 "哀家也不瞒[aicheng]，哀家是看了那侍寝的册子，又听传言，才有此一问罢了。"
                    太后 "哀家知道，这宫里没有哪位妃嫔，不想皇上常去她那，就算有人有此言，也定是忽悠你罢了。"
                    太后 "多数无益，但哀家知晓，这后宫里的人呀，无人不想给皇上开枝散叶，这现下皇上常去[aicheng]那，自然议论纷纷。"
                    "你后面没有做声，而太后也逐渐不再说什么，只是不瞧其脸色都可知，其心情不怎么样。"
                    太后 "好了，哀家也不是想训斥你什么，只是这宫里，专宠一事的确难容，[aicheng]知晓便是，哀家不过是提醒提醒[aicheng]，免得惹上什么事。哀家也有些乏了，跪安罢。"
                "默不作声":

                    $ xingzi -= 5
                    太后 "罢了，其实哀家什么都知道。"
                    我 "太后娘娘此言怎讲？"
                    太后 "哀家也不瞒[aicheng]，哀家是看了那侍寝的册子，又听传言，才问罢。"
                    太后 "哀家知道，这宫里没有哪位妃嫔，不想皇上常去她那，就算有人有此言，也定是忽悠你罢了。"
                    太后 "多数无益，但哀家知晓，这后宫里的人呀，无人不想给皇上开枝散叶，这现下皇上常去[aicheng]那，自然议论纷纷。"
                    "你后面没有做声，而太后也逐渐不再说什么，只是不瞧其脸色都可知，其心情不怎么样。"
                    太后 "好了，哀家也不是想训斥你什么，只是这宫里，专宠一事的确难容，[aicheng]知晓便是。哀家也有些乏了，跪安罢。"
        else:


            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后唤人来传话，说是请主子去太后宫里。"
            我 "可有言是何事？"
            我的宫女 "奴婢问了，可其也说不知……似乎还挺急，言是太后已然候着了。"
            menu:
                "抱恙推辞":
                    我的宫女 "是，那奴婢这就去转告。"
                    "（片刻后……）"
                    我的宫女 "主子，那宫女闻言直怕得哆嗦，唤主子必须前去，否则太后会迁怒她们……"
                    $ my.taihoulike -= 5
                "立刻前去":
                    我的宫女 "是，奴婢这就转告那宫女。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "（小声）[my.cheng]请恕奴婢多嘴了，还望您等会小心说话才是……太后现下正发着脾气呢，若是[my.cheng]再来晚些，刚才给[my.cheng]传话那宫女的小命，怕是都要不保了……"
            我 "（惊）"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，手中正拿着剪子，修剪着一盆栽，不……那盆栽已剪得只剩几许叶，枝条在却也凌乱不堪。"
            menu:
                "行礼请安":
                    pass
            "太后并未正眼瞧你，也并未让你起身，只是仍然在那儿一下下的将那些叶片悉数剪下，终一叶不留。良久，只闻一声叹气……"
            太后 "罢了，[aicheng]起来罢。"
            我 "谢太后。"
            太后 "[aicheng]可知哀家方才为何罚你？"
            我 "（忍着腿酸）臣妾不知……"
            太后 "不知？"
            "只闻太后冷笑一声，又将那些枝条用力剪下，那盆栽便更为丑陋不堪。"
            太后 "昨儿可是有人来告诉哀家，言[aicheng]蛊惑君心，扰乱后宫，持宠而娇，何人接近皇上便用尽手段……可有此事？"
            menu:
                "绝无此事":
                    $ xingzi += 5
                "默不作声":
                    $ xingzi -= 5

            太后 "哼！哀家自然知道并无此事，但哀家也知道，[aicheng]现下正得皇上盛宠，近日的确多去[aicheng]那儿。这后宫妃嫔皆羡慕得很，自然会跑来哀家这捏造事实就为了给你一击。[aicheng]可知这个理？"
            menu:
                "臣妾知道":
                    pass
            太后 "你知道又有何用，这宫里的妃嫔，注定不过是给皇上开枝散叶的，若是不想还有下次有人给哀家告状，[aicheng]还是多想想法子吧。"
            太后 "罢了，烦的很……最厌这些事做了还有人跑来告诉哀家的了，麻烦。跪安罢。"
    else:
        if taihouxinge == "宽和":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后娘娘唤人来了，说是唤主子去陪陪太后。"
            menu:
                "连忙动身":
                    pass
            我的宫女 "奴婢给主子把发簪摆弄规整些。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "见过[my.cheng]，太后娘娘已在里头候着了，请随奴婢来罢。"
            $ bg("建章宫内")
            show 太后
            太后 "（忽抬头看眼你，过了一会）起来罢，哀家看得入神，没注意到[my.cheng]来了。"
            我 "不知娘娘找臣妾何事？"
            太后 "无事，不过是有些无趣，便找你来陪陪哀家罢了。"
            "同太后寒暄几句……"
            太后 "（忽想起什么似的）噢说来，哀家今日听闻，皇上可是常去[my.cheng]宫中？"

            menu:
                "大胆应是":
                    $ xingzi += 5
                    太后 "你倒是不避讳。"
                    我 "事实如此，臣妾自然不避讳。"
                    太后 "那你可知，有人来哀家这告状了？"
                "默不作声":


                    $ xingzi -= 5
                    太后 "（见你不吭声）怎么？可是哀家所言有假？"
                    我 "不曾有假，只是……"
                    太后 "哀家都知道了，哀家可是太后，自然有人会将侍寝名录告诉哀家。"
                    太后 "恐怕[my.cheng]不知，近日可有人来给哀家告状了。"
            我 "告状？"
            太后 "你自然不知，哀家知道，这宫里没有哪位妃嫔，不想皇上常去她那，就算有人有此言，也定是忽悠你罢了。"
            太后 "哀家并未去查，但这些日常可是听了不少耳旁风……说[my.cheng]蛊惑君心，手段高明，令旁人都接近不得皇上。"
            太后 "哀家没有什么意思，知道哀家不想再听闻这些耳旁风，且哀家不愿看到谁争风吃醋，把这后宫扰乱，而最好的方法，自然是各妃平等不妒忌，但现下看来，[my.cheng]很是让旁人妒忌呢。"
            "你后面没有做声，而太后也逐渐不再说什么，只是不瞧其脸色都可知，其心情不怎么样。也并非无事寻你，而是假借话家常寻你罢。"
            $ my.tags.append(["禁足一月",0,""])
            $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "见罪于太后，被禁足一月。\n"
            $ allstory.insert(0,tempstory2)
            太后 "罢了，也该叫皇上将你放一放了。"
            太后 "传哀家旨意，[my.cheng]禁足一月，无诏不得出。"
            太后 "哀家乏了 [my.cheng]跪安罢。"

        elif taihouxinge == "擅权":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后唤人来传话，说是让主子去陪陪太后。"
            menu:
                "抱恙推辞":
                    我的宫女 "是，那奴婢这就去转告。"
                    "（片刻后……）"
                    我的宫女 "主子，太后说必须去……"
                    $ my.taihoulike -= 5
                "立刻前去":
                    我的宫女 "是，奴婢这就转告那宫女。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "（小声）莫嫌奴婢多嘴，还望[my.cheng]等会小心说话才是……"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，双目微合，似在闭目养神。"
            menu:
                "行礼请安":
                    pass

            太后 "[aicheng]起来罢。"
            "太后并未正眼瞧你，也并未赐坐。只见她缓缓端起茶杯，喝了口茶。"
            "又过了会儿……"
            太后 "赐坐吧。"
            太后 "听闻近日皇上经常前去看[my.cheng]，得如此荣宠，想来皇上定是十分喜欢喏。"
            "太后一直说着你独宠后宫，皇上哪都不去，有所影响。"
            太后 "不是哀家说[my.cheng]什么不是，只是这宫里的女人，都是服侍着皇上，为皇上开枝散叶，好让子嗣繁盛的，可莫要吃什么独食，可是会撑死的，[my.cheng]可知这份理？"
            menu:
                "臣妾知道":
                    $ taidu += 3
                "（默不作声）":
                    $ taidu -= 3
            $ my.tags.append(["禁足一月",0,""])
            $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "见罪于太后，被禁足一月。\n"
            $ allstory.insert(0,tempstory2)
            太后 "罢了，也该叫皇上将你放一放了。"
            太后 "传哀家旨意，[my.cheng]禁足一月，无诏不得出。"
            太后 "[my.cheng]跪安罢，哀家乏了。"



        elif taihouxinge == "避世":
            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后娘娘唤人来了，说是唤主子去陪陪娘娘，娘娘现已在建章宫里候着了。"
            menu:
                "连忙动身":
                    pass
            我的宫女 "方才御膳房送来了的糕点，还热着呢，奴婢给主子带上，可给太后娘娘尝尝。"
            我 "（之前去陪太后时，太后似是说过很是喜吃这点心。）"
            我 "一并带上吧。"
            我的宫女 "是，主子。"

            $ bg("建章宫外")
            show 莲稚
            莲稚 "见过[my.cheng]，太后娘娘已在里头候着了，请随奴婢来罢。"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，手中拿着经文，口中还念着。"
            menu:
                "行礼问安":
                    pass
            太后 "（因被打断，似乎有些不悦，但还是抬头看了眼你）起来吧，来，坐。"
            我 "不知娘娘找臣妾何事？"
            太后 "无事，不过是有些无趣，便找你来陪陪哀家罢了，怎么？可是不便？"
            我 "怎有，臣妾高兴着呢。"
            "与太后闲聊各种，聊的很是愉快，还吃着你带来的糕点，很是惬意。"
            太后 "说来，哀家近日听闻，[my.cheng]独占后宫，可有此事？"
            menu:
                "大胆应是":
                    $ xingzi += 5
                    太后 "你倒挺实诚的。"
                    我 "事实如此，臣妾自然不避讳。"
                    太后 "哀家也不瞒[my.cheng]，哀家是看了那侍寝的册子，又听传言，才有此一问罢了。"
                    太后 "哀家知道，这宫里没有哪位妃嫔，不想皇上常去她那，就算有人有此言，也定是忽悠你罢了。"
                    太后 "多数无益，但哀家知晓，这后宫里的人呀，无人不想给皇上开枝散叶，这现下皇上常去[my.cheng]那，自然议论纷纷。"
                    "你后面没有做声，而太后也逐渐不再说什么，只是不瞧其脸色都可知，其心情不怎么样。"
                    太后 "好了，哀家也不是想训斥你什么，只是这宫里，专宠一事的确难容，[my.cheng]知晓便是。哀家也有些乏了，跪安罢。"
                "默不作声":


                    $ xingzi -= 5
                    太后 "罢了，其实哀家什么都知道。"
                    我 "太后娘娘此言怎讲？"
                    太后 "哀家也不瞒[my.cheng]，哀家是看了那侍寝的册子，又听传言，才问罢。"
                    太后 "哀家知道，这宫里没有哪位妃嫔，不想皇上常去她那，就算有人有此言，也定是忽悠你罢了。"
                    太后 "多数无益，但哀家知晓，这后宫里的人呀，无人不想给皇上开枝散叶，这现下皇上常去[aicheng]那，自然议论纷纷。"
                    "你后面没有做声，而太后也逐渐不再说什么，只是不瞧其脸色都可知，其心情不怎么样。"
                    太后 "好了，哀家也不是想训斥你什么，只是这宫里，专宠一事的确难容，[aicheng]知晓便是。哀家也有些乏了，跪安罢。"
        else:


            $ bg("寝居")
            show 我的宫女
            我的宫女 "主子，方才太后唤人来传话，说是请主子去太后宫里。"
            我 "可有言是何事？"
            我的宫女 "奴婢问了，可其也说不知……似乎还挺急，言是太后已然候着了。"
            menu:
                "抱恙推辞":
                    我的宫女 "是，那奴婢这就去转告。"
                    "（片刻后……）"
                    我的宫女 "主子，那宫女闻言直怕得哆嗦，唤主子必须前去，否则太后会迁怒她们……"
                    $ my.taihoulike -= 5
                "立刻前去":
                    我的宫女 "是，奴婢这就转告那宫女。"
            $ bg("建章宫外")
            show 莲稚
            莲稚 "（小声）[my.cheng]请恕奴婢多嘴了，还望您等会小心说话才是……太后现下正发着脾气呢，若是[my.cheng]再来晚些，刚才给[my.cheng]传话那宫女的小命，怕是都要不保了……"
            我 "（惊）"
            $ bg("建章宫内")
            show 太后
            "太后正坐于主位之上，手中正拿着剪子，修剪着一盆栽，不……那盆栽已剪得只剩几许叶，枝条在却也凌乱不堪。"
            menu:
                "行礼请安":
                    pass
            "太后并未正眼瞧你，也并未让你起身，只是仍然在那儿一下下的将那些叶片悉数剪下，终一叶不留。"
            太后 "[my.cheng]可真有本事，可知哀家为何唤你？"
            我 "（忍着腿酸）臣妾不知……"
            太后 "不知？"
            太后 "将剪子甩向你，所幸没有打中，但也滑落在你身旁不远处打转……"
            我 "（不敢出声。）"
            太后 "昨儿可是有人来告诉哀家，言[my.cheng]蛊惑君心，扰乱后宫，持宠而娇，何人接近皇上便用尽手段！可有此事？"
            menu:
                "绝无此事":
                    $ xingzi += 5
                "默不作声":
                    $ xingzi -= 5

            太后 "哼！[my.cheng]有没有哀家不知吗？这后宫里，哀家什么事都知道！但你用什么手段那些，哀家不管，哀家只管这后宫妃嫔，乃都是为了给皇上开枝散叶的，绝不可独享，[my.cheng]可明白？"
            menu:
                "臣妾知道":
                    pass

            太后 "罢了！给哀家回去，禁足一月！烦的很……最厌这些事做了还有人跑来告诉哀家的了，麻烦。"
            $ my.tags.append(["禁足一月",0,""])
            $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "见罪于太后，被禁足一月。\n"
            $ allstory.insert(0,tempstory2)
    $ AP -= 1
    $ timenum += 1
    jump 寝居界面


label 太后考才艺:
    if my.taihoulike > 50:
        $ cheng = aicheng
    else:
        $ cheng = my.cheng
    "打开书不久，才看进去几行，便有宫女来报。"
    if taihouxinge == "宽和":
        show 我的宫女
        我的宫女 "主子，太后娘娘来了。"
        hide 我的宫女
        "一个回首，太后便已然站在身后。"
        show 太后
        menu:
            "行礼":
                pass
        太后 "快些起来吧，这些礼仪便是免了，现在身有龙嗣，可不能这么乱来，现下无旁人，这些规矩便罢了。"
        太后 "噢？是诗集，哀家也有一本一样的。说来前些日子之前哀家听人说，[cheng]很擅诗词，哀家可得领略一番才是。"

    elif taihouxinge == "避世":
        show 我的宫女
        我的宫女 "主子，太后娘娘来了。"
        hide 我的宫女
        show 太后
        太后 "[cheng]在做什么呢？"
        menu:
            "行礼":
                pass
        太后 "快些起来快些起来，怀着龙嗣呢，这些礼节不要也罢。"
        太后 "（连忙将你虚扶起身）"
        太后 "这是在看诗集？哀家听闻[cheng]博览群书，对诗很是行家，哀家倒是有些好奇，便出题考考罢。"

    elif taihouxinge == "精敏":
        show 我的宫女
        我的宫女 "（微微发抖）主子……太后娘娘来了。"
        hide 我的宫女
        show 太后
        太后 "（朝着你的一个宫女冷哼到）你这小婢子礼数不足，可得多加练练才是。"

        menu:
            "行礼":
                pass

        太后 "罢了罢了，快些起身罢，[cheng]现怀着龙嗣，行个礼若是出了什么岔子，哀家可担当不起。"
        太后 "说来[cheng]的那个婢子可得好生管教才是......噢？[cheng]这可是在看诗集？哀家倒是听闻[cheng]诗词歌赋很是不错，倒是得考考才是。"
    else:
        show 我的宫女
        我的宫女 "主子，太后娘娘来了。"
        hide 我的宫女
        show 太后
        "回首，便见着太后一身华服，很是庄重，微低眼眸看向你。"
        menu:
            "行礼":
                pass
        太后 "快些起来罢，[cheng]现下怀着龙嗣，不同寻常，这些礼节不做也罢。"
        太后 "诗集？哀家只不过听闻[cheng]诗词十分了得，倒没见过实的，倒是得瞧瞧[cheng]的本事才是。"


    python:
        tempnum = 0
        num = 0
        tiku = list(range(0,15))
        questions = renpy.random.sample(tiku,3)
    $ renpy.call("太后考才艺_题库",what =questions[0],from_current=False)

    $ renpy.call("太后考才艺_题库",what =questions[1],from_current=False)

    $ renpy.call("太后考才艺_题库",what =questions[2],from_current=False)


    if taihouxinge == "宽和":
        if tempnum == 3:
            太后 "（抚掌而笑）哈哈哈，不愧是[cheng]，回答得当真不错，可谓一字不漏。"
            太后 "说来，哀家这回可是带了东西来，便是作为怀有龙嗣的贺礼了。"
            $ yuci = renpy.random.choice(presents_hign)
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
            "又闲聊许久。"
            太后 "哀家便先回去了，[cheng]好生歇息罢，改日若是得闲了，便来看看哀家罢。"
        else:




            太后 "虽未全中，倒也不错，也是有那么一番才华在其中。"
            "又闲聊了许久。"
            太后 "哀家这便先回去了，[cheng]可得好生歇息着，可别操劳着了。"



    elif taihouxinge == "避世":
        if tempnum == 3:
            太后 "不错不错，果然名不虚传，但如今怀有身孕，还是多加休息才是，可不要过多操劳。"
            太后 "对了，哀家带了东西给你，便是作为怀有龙嗣的贺礼了。"
            $ yuci = renpy.random.choice(presents_hign)
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
            "又闲聊许久。"
            太后 "哀家便先回去了，[cheng]好生歇息罢。"
        else:



            太后 "嗯......[cheng]还需多加努力，巩固一番才是。"
            "又闲聊了许久。"
            太后 "哀家这便先回去了，[cheng]可得好生歇息着，不必送了。"


    elif taihouxinge == "避世":
        if tempnum == 3:
            太后 "的确不错，哀家果真没有看错人，[cheng]小嘴若是再甜些，把诗词用作喻人，想必更好。"
            太后 "对了，哀家东西多，便随便翻了个东西，作为怀上龙嗣的贺礼了。"
            $ yuci = renpy.random.choice(presents_hign)
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
            "又闲聊许久。"
            太后 "哀家乏了，便回去了，那些琐碎的事情交给奴才们做就是，要学会使唤他们，可别养坏了。"
        else:


            太后 "（冷哼）不过如此，看来[cheng]还得多加看书，练练才是，可别坏了这名声让旁人笑话了才是。"
            "又闲聊了许久。"
            太后 "罢了，哀家乏了便先回去了，不必送了。"
    else:


        if tempnum == 3:
            太后 "不错不错，哀家很是欣赏，[cheng]果真如传闻所言这般。"
            太后 "说来，哀家带了些东西来，做这怀有龙嗣的贺礼，待会可得记得叫人收好才是。"
            $ yuci = renpy.random.choice(presents_hign)
            "获得了[yuci.name]×1。"
            $ kufang.append(yuci)
            "又闲聊许久。"
            太后 "好了，哀家还有事，便先回去罢，[cheng]好生照看自个，若有什么需要的，唤人来找哀家便是。"
        else:



            太后 "既有名声在外，可得好生护着，换作旁人，可是难有此名，[cheng]可得再上些心思才是。"
            "又闲聊了许久。"
            太后 "罢了，哀家乏了便先回去了，改日得空了，便来看看哀家罢。"
    $ Taihoulike_Up(my,tempnum)

    hide 太后
    if timenum == 5:
        jump 结束本旬
    else:
        $ timenum = timenum + 1
        $ AP = AP - 1
        jump 寝居界面


label 太后考才艺_题库(what):

    python:
        if what == 0:
            wen = "予独爱莲之出淤泥而不染，濯清涟而不妖。"
            dui = "中通外直，不蔓不枝，香远益清，亭亭净植，可远观而不可亵玩焉。"
            cuo = "中通外直，亭亭净植，不蔓不枝，香远益清，可远观而不可亵玩焉。"
        elif what == 1:
            wen = "春未老，风细柳斜斜。"
            dui = "试上超然台上望，半壕春水一城花。"
            cuo = "试上留然台上望，半豪春水一城花。"
        elif what == 2:
            wen = "花自飘零水自流。一种相思，两处闲愁。"
            dui = "此情无计可消除，才下眉头，却上心头。"
            cuo = "此情无计可消愁，才下眉头，却上心头。"
        elif what == 3:
            wen = "夜来携手梦同游，晨起盈巾泪莫收。"
            dui = "漳浦老身三度病，咸阳宿草八回秋。"
            cuo = "漳浦老身几度病，咸阳宿草几回秋。"
        elif what == 4:
            wen = "画角声中，牧马频来去。"
            dui = "满目荒凉谁可语？西风吹老丹枫树。"
            cuo = "满目荒凉谁可言？东风吹老丹红树。"
        elif what == 5:
            wen = "身无彩凤双飞翼，心有灵犀一点通。"
            dui = "隔座送钩春酒暖，分曹射覆蜡灯红。"
            cuo = "分曹射覆蜡灯红，隔座送钩春酒暖。"
        elif what == 6:
            wen = "疏影横斜水清浅，暗香浮动月黄昏。"
            dui = "霜禽欲下先偷眼，粉蝶如知合断魂。"
            cuo = "霜衾欲下先偷泪，粉蝶如知应断魂。"
        elif what == 7:
            wen = "林花谢了春红，太匆匆。无奈朝来寒雨晚来风。"
            dui = "胭脂泪，相留醉，几时重。自是人生长恨水长东。"
            cuo = "自是人生长恨水长东。胭脂泪，相留醉，几时重。"
        elif what == 8:
            wen = "问世间，情为何物，直教生死相许？"
            dui = "天南地北双飞客，老翅几回寒暑。"
            cuo = "欢乐趣，离别苦，就中更有痴儿女。"
        elif what == 9:
            wen = "众芳摇落独暄妍，占尽风情向小园。"
            dui = "疏影横斜水清浅，暗香浮动月黄昏"
            cuo = "霜禽欲下先偷眼，粉蝶如知合断魂。"
        elif what == 10:
            wen = "滚滚长江东逝水，浪花淘尽英雄。"
            dui = "是非成败转头空。"
            cuo = "是成非败转头空。"
        elif what == 11:
            wen = "合欢桃核终堪恨，里许元来别有人。"
            dui = "井底点灯深烛伊，共郎长行莫围棋。"
            cuo = "玲珑骰子安红豆，入骨相思知不知。"
        elif what == 12:
            wen = "去年今日此门中，人面桃花相映红。"
            dui = "人面不知何处去，桃花依旧笑春风。"
            cuo = "桃花依旧笑春风，人面不知何处去。"
        elif what == 13:
            wen = "一声梧叶一声秋，一点芭蕉一点愁，三更归梦三更后。"
            dui = "落灯花，棋未收，叹新丰孤馆人留。"
            cuo = "棋未收，落灯花，叹新丰孤馆人留。"
        else:
            wen = "浮云一别后，流水十年间。"
            dui = "欢笑情如旧，萧疏鬓已斑。"
            cuo = "江汉曾为客，相逢每醉还。"


    太后 "[wen]"
    $ lucky = renpy.random.randint(0,1)
    if lucky == 1:
        menu:
            "[dui]":
                $ tempnum += 1
            "[cuo]":

                pass
    else:
        menu:
            "[cuo]":
                pass
            "[dui]":
                $ tempnum += 1


    python:
        renpy.return_statement()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
