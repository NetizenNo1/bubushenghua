init python:
    import copy
    tags = [["身怀皇嗣",0,""],["禁足一月",0,""],["禁足三月",0,""],["禁足半年",0,""],["疑罪未名","疑似罪名尚未澄清，不得侍寝"],["身受杖责",0,""],["珠胎难结","终身无法得孕",""]]
    tags_yali = [["郁结于心",""],["心衰力竭",""],["失心成疯",""]]
    tags_family= [["和亲公主","为天子血脉纯清，不得正位中宫，其子不入东宫"],["名门望族","出身高贵，难免忌外戚专权之惮"],["小家碧玉","出身低微，非长年累历难以立威立足"],["宫女上位","宫女出身，难登大雅，上位艰难"]]
    tags_limit_beauty = [["明眸皓齿","容貌上限=850"],["桃花人面","容貌+50，容貌上限=900"],["天生丽质","容貌+100，容貌上限=1000"]]
    tags_limit_qizhi = [["清姿隽逸","气质上限=850"],["冰肌玉骨","气质+50，气质上限=900"],["谪仙降世","气质+100，气质上限=1000"]]
    tags_limit_meili =[["仪态万千","魅力上限=850"],["风情万种","魅力+50，魅力上限=900"],["祸水红颜","魅力+100，魅力上限=1000"]]
    tags_limit_xinji =[["意气用事","心机-100，心机上限=600"],["心浮气躁","心机-50，心机上限=700"],["聪慧过人","心机上限=850"],["思虑入微","心机+50，心机上限=900"],["智绝无双","心机+100，心机上限=1000"]]
    tags_limit_lucky = [["灾星孽缘","福缘上限=50"],["洪福齐天","福缘+20，上限=100"]]
    tags_limit_health = [["先天弱症","体质-100，体制上限=500"],["弱柳扶风","体质-50，体质上限=600"],["生性懒惰","每回合行动点-1，体质低于800时每回合+0.5"],["夙兴夜寐","每回合行动点+1，体质高于200时每回合-0.5"]]
    tags_shuxing = [["肤若凝脂","容貌+50"],["吐气如兰","气质+50"],["拥雪成峰","魅力+50"],
    ["眸若桃花","容貌+25、魅力+25"],["青丝三千","容貌+25、气质+25"],["红袖添香","气质+25、魅力+25"]]
    tags_caiyi = [["声如莺啼","音律+"],["声音嘶哑","音律上限=80"],["身姿曼妙","舞蹈+"],["四肢崎拙","舞蹈上限=80"],["耳聪目明","诗书+"],["木讷愚钝","诗书上限=80"],["心细手巧","刺绣+"],["粗枝大叶","刺绣上限=80"],["能言善辩","争锋+"],["不善言辞","争锋-"]]
    tags_xingge = [["秋霜琨玉",""],["命犯桃花",""],["尖酸刻薄",""],["喜怒无常",""],["善解人意",""],["秋水玲珑",""]]
    tags_xihao = [["嗜甜之人","体质低于800时每回合+0.5，容貌高于200时每回合-0.5"],["喜食辛辣","体质高于200时每回合-0.5，容貌低于800时每回合+0.5"]]
    tags_jqf = [["此世安恬","被暗害成功的几率降低50%"],["亦痴亦诚","心痴之人，心善之人。倾向不会高于50，福缘不会低于80。"],["难得欢喜","得了这世上最贵重的愧疚，代价是再也感受不到爱。被暗害成功的几率降低50%，每回合增加额外威望"],["狡兔三窟","披着兔皮的狼。心计上限=1000，宫斗成功率+50%，被暗害成功率-50%，每年自己和交好者额外获得3个技能点"]]
    zyfs = ["欺凌宫人","妄议朝政","不敬先祖"]

    def start_choicetags(what):
        global sxjd
        if what in choosetags_list :
            choosetags_list.remove(what)
            sxjd += what.cost
            cantchoose_list.remove(what.leibie)
        elif sxjd < what.cost:
            pass
        else:
            choosetags_list.append(what)
            sxjd -= what.cost
            cantchoose_list.append(what.leibie)


    class newplayer_tags(object):
        def __init__(self,name,leibie,cost,jieshao,choose,tags):
            self.name = name
            self.leibie = leibie 
            self.cost = cost
            self.jieshao = jieshao
            self.choose =choose
            self.tags = tags

    tags_01 = newplayer_tags(name="明眸皓齿",leibie="容貌",cost=1,jieshao="容貌上限=850",choose = False,tags = tags_limit_beauty[0])
    tags_02 = newplayer_tags(name="桃花人面",leibie="容貌",cost=2,jieshao="容貌上限=900",choose = False,tags = tags_limit_beauty[1])
    tags_03 = newplayer_tags(name="天生丽质",leibie="容貌",cost=3,jieshao="容貌上限=1000",choose = False,tags = tags_limit_beauty[2])
    tags_04 = newplayer_tags(name="清姿隽逸",leibie="气质",cost=1,jieshao="气质上限=850",choose = False,tags = tags_limit_qizhi[0])
    tags_05 = newplayer_tags(name="冰肌玉骨",leibie="气质",cost=2,jieshao="气质上限=900",choose = False,tags = tags_limit_qizhi[1])
    tags_06 = newplayer_tags(name="谪仙降世",leibie="气质",cost=3,jieshao="气质上限=1000",choose = False,tags = tags_limit_qizhi[2])
    tags_07 = newplayer_tags(name="仪态万千",leibie="魅力",cost=1,jieshao="魅力上限=850",choose = False,tags = tags_limit_meili[0])
    tags_08 = newplayer_tags(name="风情万种",leibie="魅力",cost=2,jieshao="魅力上限=900",choose = False,tags = tags_limit_meili[1])
    tags_09 = newplayer_tags(name="祸水红颜",leibie="魅力",cost=3,jieshao="魅力上限=1000",choose = False,tags = tags_limit_meili[2])
    tags_10 = newplayer_tags(name="聪慧过人",leibie="心机",cost=1,jieshao="心机上限=850",choose = False,tags = tags_limit_xinji[2])
    tags_11 = newplayer_tags(name="思虑入微",leibie="心机",cost=2,jieshao="心机上限=900",choose = False,tags = tags_limit_xinji[3])
    tags_12 = newplayer_tags(name="智绝无双",leibie="心机",cost=3,jieshao="心机上限=1000",choose = False,tags = tags_limit_xinji[4])
    tags_13 = newplayer_tags(name="洪福齐天",leibie="福缘",cost=2,jieshao="福缘上限=100",choose = False,tags = tags_limit_lucky[1])

    choicetags_list = [tags_01,tags_02,tags_03,tags_04,tags_05,tags_06,tags_07,tags_08,tags_09,tags_10,tags_11,tags_12,tags_13]
    choosetags_list = []
    cantchoose_list = []




screen choicetags():
    frame:
        background None
        has vbox
        text "请选择人物特质" align (0.5,0.0)
        grid 3 5:
            xspacing 25
            yspacing 5
            align (0.5,0.5)
            for i in choicetags_list:
                if i.leibie in cantchoose_list and i not in choosetags_list:
                    textbutton "{color=#A1A1A1}{size=25}"+i.name+"([i.cost])":
                        action NullAction()
                        hovered Show("scrtt",tt=i.jieshao)
                        unhovered [Hide("scrtt")]
                elif i not in choosetags_list:
                    textbutton "{size=25}"+i.name+"([i.cost])":
                        action Function(start_choicetags,i)
                        hovered Show("scrtt",tt=i.jieshao)
                        unhovered [Hide("scrtt")]
                else:
                    textbutton "{color=#B22222}{size=25}"+i.name+"([i.cost])":
                        action Function(start_choicetags,i)
                        hovered Show("scrtt",tt=i.jieshao)
                        unhovered [Hide("scrtt")]
            text ""
            text ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
