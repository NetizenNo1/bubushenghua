init python:
    def hdchenghu():
        if hdxingge == "冷漠":
            return my.cheng
        elif hdxingge == "腹黑":
            if my.love >= 80:
                if len(my.ming) == 1:
                    return my.ming+"儿"
                else:
                    return my.ming
            elif my.love >= 50:
                return "爱妃"
            else:
                return my.cheng
        elif hdxingge == "温柔":
            if my.love >= 50:
                return "爱妃"
            else:
                return my.cheng
        elif hdxingge == "风流":
            return my.cheng
        else:
            if my.love >= 80:
                return "爱妃"
            else:
                return my.cheng




screen shiqin():
    window align (0.5,1.0):
        has vbox align (0.5,0.5)
        text "{size=40}侍寝中……"

    frame align (0.8,0.5):
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        has vbox
        for i in shiqinlist:
            textbutton i action SetVariable("shiqinlabel",i),Hide("shiqin"),Return()
        text "兴致："+str(int(xingzhi))



label 吟诗作对:
    $ shiqinlist.remove("吟诗作对")
    if hdxingge == "冷漠":
        我 "皇上，臣妾近日想了几句诗，您可愿意同臣妾对上一对？"
        皇上 "（眉眼淡淡的）没兴趣，你能想出什么好诗？"
        我 "皇上……"
        皇上 "那就说来听听。"
        "……"
        if my.book >80:
            皇上 "倒是有几分意思，是朕小瞧你了。"
            我 "（得意。）"
            皇上 "看来待在朕身边，你也有点长进。"
            $ xingzhi += 10
        else:
            $ xingzhi -= 10
            if my.love > 50:
                皇上 "朕可以不夸你吗？"
                我 "（委屈）有这么差吗……"
            else:
                皇上 "这诗和人一样无趣。"


    elif hdxingge == "腹黑":
        我 "皇上，臣妾近日想了几句诗，您可愿意同臣妾对上一对？"
        皇上 "（笑意粲然）[aifei]好雅致，那便说来听听罢。"
        "……"
        if my.book >80:
            皇上 "[aifei]真是文采斐然，怕是那些文人也要甘拜下风了。"
            $ xingzhi += 10
        else:
            $ xingzhi -= 10

            if my.love > 50:
                皇上 "[aifei]的文采大有长进，真是令朕刮目相看，想来是用了许多心思。"
            else:
                皇上 "[aifei]的才思……真非常人可以领会。"

    elif hdxingge == "温柔":
        我 "皇上，臣妾近日想了几句诗，您可愿意同臣妾对上一对？"
        皇上 "（笑意粲然）[aifei]好雅致，那便说来听听罢。"
        "……"
        if my.book >80:
            皇上 "[aifei]才思果然不凡！此诗精秀巧妙，朕十分欣赏。"
            $ xingzhi += 15
        elif my.book >50:
            皇上 "[aifei]的文采虽不比那些文人，但心思别致，朕十分欣赏。"
        else:
            皇上 "[aifei]若喜吟诗作赋，改日朕叫人送几本诗书予你，通读一遍便定能大有进益。"

    elif hdxingge == "风流":
        我 "皇上，臣妾近日想了几句诗，您可愿意同臣妾对上一对？"
        皇上 "（兴致盎然）[aifei]好雅致，那便说来听听罢。"
        "……"
        if my.book >50:
            皇上 "[aifei]好文采！"
            皇上 "不如也听听朕的诗如何？"
            皇上 "娟娟白雪绛裙笼，无限风情屈曲中。小睡起来娇怯力，和身款款倚帘栊。"
            皇上 "水骨嫩，玉山隆，鸳鸯衾里挽春风。"
            我 "（羞。）"
            $ xingzhi += 20
        else:
            $ xingzhi -= 15
            皇上 "（面有难色）……[aifei]你只需貌美如花，安然承欢便是了。不必附庸风雅，落得旁人耳中只会沦为笑话。"
            我 "……"
    else:

        我 "皇上，臣妾近日想了几句诗，您可愿意同臣妾对上一对？"
        皇上 "朕不善吟诗，但若[aifei]想，那边说与朕听听吧。"
        "……"
        if my.book >80:
            皇上 "朕虽不善诗词，但也觉得[aifei]此诗精妙绝伦。"
            皇上 "我朝有[aifei]这般的才女，实在幸事。"
            $ xingzhi += 15
        elif my.book >50:
            皇上 "[aifei]的文采虽不比那些文人，但心思别致，朕有几分喜欢。"
        else:
            $ xingzhi -= 5
            皇上 "朕觉得[aifei]文采平平，此诗实在算不上好。"
    return

label 醉酒当歌:
    $ shiqinlist.remove("醉酒当歌")
    我 "今夜月色迷人，皇上，命人备上一壶好酒，同臣妾对酌几杯可好？"
    皇上 "（欣然应允。）"
    "未几，二人皆是微醺。"
    我 "皇上，此情此景，对酒当歌最合适不过。"
    皇上 "嗯……"
    if my.muzic > 80:
        皇上 "对酒当歌，人生几何！"
        皇上 "有女如斯，君当醉卧！"
        if hdxingge == "风流":
            $ xingzhi += 30
        else:
            $ xingzhi += 15
    elif my.muzic > 50:
        皇上 "今朝有酒今朝醉，明日愁来明日愁。"
        if hdxingge == "风流":
            $ xingzhi += 15
        else:
            $ xingzhi += 5
    else:
        皇上 "强乐无味。"
        if hdxingge == "风流":
            $ xingzhi -=10
        else:
            pass
    return

label 献舞一曲:
    $ shiqinlist.remove("献舞一曲")
    我 "臣妾今日准备了一支舞……"
    皇上 "（欣然应允。）"
    if my.dance > 80:
        if hdxingge == "风流":
            $ xingzhi += 25
            皇上 "（眼神始终跟随在你的身上，隐约流露出几分痴迷。）"
            "一曲舞毕。"
            皇上 "（眼中满是欣赏之色）妙哉！妙哉！此舞震慑人心，不愧是朕的[aifei]！"
        else:
            $ xingzhi += 15
            皇上 "（眼神始终跟随在你的身上，隐约流露出几分痴迷。）"
            "一曲舞毕。"
            皇上 "[aifei]的舞步真可谓是‘试舞一曲天下无’啊！"
    elif my.dance > 50:
        if hdxingge == "风流":
            $ xingzhi += 10
            皇上 "（眼神始终跟随在你的身上，时不时轻轻点头。）"
            "一曲舞毕。"
            皇上 "妙哉！"
        else:
            $ xingzhi += 5
            皇上 "（眼神始终跟随在你的身上，时不时轻轻点头。）"
            "一曲舞毕。"
            皇上 "[aifei]有心了。"
    else:
        if hdxingge == "风流":
            $ xingzhi -=10
            皇上 "（眼神始终跟随在你的身上，脸色却逐渐黯淡。）"
            "一曲舞毕。"
            皇上 "[aifei]的舞技可要再好好磨练一阵子了。"
            我 "是……"
        else:
            "一曲舞毕。"
            皇上 "（兴致缺缺。）"
    return

label 欲拒还迎:
    $ shiqinlist.remove("欲拒还迎")
    if my.qizhi > 900:
        "你欲擒故纵，似近还远，忽离忽迎。"
        "此刻[guoxing][emperor]的眼中，你俨然如同缥缈梦幻的瑶池仙女，又如同不食人间烟火的谪仙，纯美而又诱惑，令人欲罢不能。"
        $ xingzhi += 25
    elif my.qizhi > 800:
        "你欲擒故纵，忽远忽近，让人难以琢磨。"
        "[guoxing][emperor]望着你的眼神已然迷醉。"
        $ xingzhi += 20
    elif my.qizhi > 600:
        "你欲擒故纵，忽远忽近，让人难以琢磨。"
        "[guoxing][emperor]笑眼看着你，顺着你的伎俩戏玩了一阵。"
        $ xingzhi += 10
    else:
        "你欲擒故纵，意欲同他作乐。"
        "[guoxing][emperor]有些恹恹地坐在床头，不为所动。"
        $ xingzhi -=10
    return

label 倚帐调情:
    $ shiqinlist.remove("倚帐调情")
    if my.meili > 900:
        "你纱衣半褪，软玉温香，媚眼如丝，暧昧撩人的低语亲吻在[guoxing][emperor]的耳畔。"
        "此刻[guoxing][emperor]的眼中，你像是神秘妩媚的青丘灵狐，又如同暗夜中绽放的一朵红莲，妖娆而危险，令人欲罢不能。"
        $ xingzhi += 25
    elif my.meili > 800:
        "你纱衣半褪，眸送秋波。"
        "[guoxing][emperor]望着你的眼神已然迷醉。"
        $ xingzhi += 20
    elif my.meili > 600:
        "你纱衣半褪，眸送秋波。"
        "[guoxing][emperor]笑眼看着你，顺着你的伎俩戏玩了一阵。"
        $ xingzhi += 10
    else:
        "你纱衣半褪，摆出撩人姿态。"
        "[guoxing][emperor]有些恹恹地坐在床头，不为所动。"
        $ xingzhi -=10
    return

label 轻语闲聊:
    $ shiqinlist.remove("轻语闲聊")
    menu:
        "温柔抚慰":
            $ xingzhi += my.love*0.2
            if hdxingge == "腹黑":
                皇上 "[aifei]如此温柔可人，朕也不觉得政事劳累了。"
            elif hdxingge == "冷漠":
                皇上 "别以为朕不知道你那些小心思。"
                皇上 "是不是有求于朕了？"
                我 "（臣妾冤枉啊……）"
                if my.love >= 80:
                    皇上 "你不用这样朕也会答应你的。"
                else:
                    pass
            elif hdxingge == "风流":
                皇上 "有爱妃陪伴，朕的劳累似乎都一扫而光了。"
            elif hdxingge == "刚正":
                "朕最近政务繁忙，疏忽了爱妃，爱妃可是怨朕了？"
            else:
                皇上 "[aifei]如此温柔可人，朕也不觉得政事劳累了。"
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
                if my.meishu["一A"] == 0:
                    $ tempfz.love = tempfz.love - my.love*0.1
                    $ tempfz.exp =  tempfz.exp - my.love*0.2
                else:
                    $ tempfz.love -= my.love*0.1*(100+ (my.meishu["一A"]+1)*25)*0.01
                    $ tempfz.exp -= my.love*0.1*(100+ (my.meishu["一A"]+1)*25)*0.01
                $ my.love = my.love -  1
                皇上 "朕知道了……"
                $ tempfz.like -= 5
                $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "在侍寝时说了"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"的坏话。\n"
                $ allstory.insert(0,tempstory2)
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
                if my.meishu["一A"] == 0:
                    $ tempfz.love += my.love*0.1
                    $ tempfz.exp += my.love*0.1
                else:
                    $ tempfz.love += my.love*0.1*(100+ (my.meishu["一A"]+1)*25)*0.01
                    $ tempfz.exp += my.love*0.1*(100+ (my.meishu["一A"]+1)*25)*0.01
                $ my.love = my.love -  1
                $ tempfz.like += my.love*0.1
                $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "在侍寝时替"+str(tempfz.hao)+str(tempfz.weifen)+str(tempfz.name)+"美言几句。\n"
                $ allstory.insert(0,tempstory2)
                皇上 "朕知道了……"
    return

label 褪衣入梦:
    if mysqfail == True:
        皇上 "（甚是不悦）你今日为何如此不解风情？"
        我 "皇上……"
        皇上 "朕看来是太宠着你了。"
        皇上 "睡吧。"
        皇上 "即日起禁足三月。"
        $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "在侍寝时言行无状，触怒龙颜，被禁足三月。\n"
        $ allstory.insert(0,tempstory2)
        $ mustshiqin = 0
        $ my.tags.append(["禁足三月",0,""])
    else:
        if mysqnice == True:
            皇上 "今夜就留在圣宸宫吧。"
            我 "（欣喜）多谢皇上……"
            $ tempstory2 = "【闲言】"+str(year)+"年"+str(month)+"月，"+ str(my.hao)+str(my.weifen)+str(my.name) + "在侍寝时博得帝心，皇上大悦，特允其留宿。\n"
            $ allstory.insert(0,tempstory2)
        else:
            pass

        if hdxingge == "冷漠":
            皇上 "（将你抱起。）"
            hide 皇帝
            "还是往常那般冰冷。"
            if my.love >80:
                "但你却能感觉到，冰冷胸膛之下那火热跳动的心。"
            else:
                pass
            "共赴云雨。"
        elif hdxingge == "腹黑":
            hide 皇上
            "[guoxing][emperor]将你拥入怀中，二人同床共枕。"
            if my.love >80:
                "你能感觉到他迷离缥缈的眼神背后，藏着几分真情。"
            else:
                "被他拥抱的感觉，温暖，却似即若离。"
        elif hdxingge == "温柔":
            皇上 "（抱你到了榻上。）"
            hide 皇上
            "共赴云雨。"
        elif hdxingge == "风流":
            if my.love > 80:
                皇上 "（伸手抬起你的下巴，热烈地吻了上去。满足一番后，又将你紧紧揽入怀中。）"
                皇上 "（眼神炙热情深，似是急不可耐。）"
            else:
                皇上 "（面带笑容，暧昧佻然。伸手便将你抱起。）"
            hide 皇上
            "鸾颠凤倒，搓粉团朱。"
        else:

            if my.beauty*0.7 +my.meili*0.3 >900:
                $ xingzhi = 30
            else:
                $ xingzhi = 15
            hide 皇上
            "[guoxing][emperor]将你抱至榻上。"
            if my.love > 80:
                "[guoxing][emperor]威严神情的背后，藏着无限缱绻的柔情。"
            else:
                pass
            "巫云楚雨,夜月花朝。"

    if mysqnice == True and my.love >= 80 and hd_love_1 == False:
        $ hd_love_1 = True
        "夤夜，殿内安静无声，偶尔能听到窗外的风声，和身畔男子的呼吸声。"
        皇上 "……[aifei]醒了。"
        我 "嗯……皇上也醒了？"
        皇上 "（碰了碰你的脸颊）下午憩了会儿，这会儿反倒是不困了。"
        皇上 "[aifei]同朕说说话罢。"
        menu:
            "那臣妾问您一个问题罢":
                if hdxingge == "冷漠":
                    皇上 "仅限这次，问罢。"
                elif hdxingge == "风流":
                    皇上 "哦？朕也想听听[aifei]有什么想问的？"
                else:
                    皇上 "嗯，问罢。"
                menu:
                    "皇上最爱的人":
                        if hdxingge == "冷漠":
                            皇上 "朕不知道。"
                            我 怒 "皇上说好了要回答臣妾的……"
                            皇上 "可朕的确给不了你答案。"
                            皇上 "因为朕没有爱的人，又何谈最爱？"
                            皇上 "只不过朕可以回答你，朕最爱的人，绝不是会提出这种问题的蠢货。"
                            我 "（哭）"
                            我 "真的么？"
                            皇上 "骗你做甚。"
                            皇上 "（莫名心虚。）"
                        elif hdxingge == "腹黑":
                            皇上 "想听真话吗？"
                            我 "（迟疑）您这话是什么意思，莫不是还要骗臣妾？"
                            我 "（嘟哝）那也不必直说呀……"
                            皇上 "朕想哄你高兴，所以……"
                            皇上 "朕就说，最爱的是你。"
                            我 "您要真想哄臣妾，又何必让臣妾知道您是在说谎呢……"
                            我 "倒显得臣妾跟个傻瓜似的。"
                            皇上 "哈哈哈，是么……"
                            皇上 "那以后便别问这种话了。"
                            menu:
                                "是":
                                    我 "臣妾知道啦。"
                                    皇上 "（手抚上你的长发）乖乖的，听话。"
                                    皇上 "朕会喜欢你的，就像现在这样……"
                                    皇上 "（声音愈发小了下去）但帝王真心，切莫奢求。"
                                    皇上 "朕……不想害了你。"
                                "追问":
                                    我 "臣妾偏要问。皇上可知道，谎话说多了便成了真话。"
                                    我 "臣妾要您今日所说的，迟早变成真的。"
                                    皇上 "……"
                                    皇上 "[aifei]要真能做到，倒也值得朕去爱了。"
                        elif hdxingge == "温柔":
                            皇上 "（思考了一会儿）这个问题朕得好好想想。"
                            我 "（期待）"
                            皇上 "爱妃想让朕说……最爱的人是你吗？"
                            我 "臣妾……臣妾自然是想听到皇上自己的回答。"
                            皇上 "朕最爱，乃天下苍生。"
                            皇上 "这样的话……是爱妃不愿意听到的罢？"
                            我 "（迟疑）"
                            皇上 "一想到朕的爱要被分成那么多份，朕也觉得很惭愧。"
                            皇上 "朕不想辜负你，可也辜负不了这天下……"
                            我 "（您不必惭愧……）"
                            皇上 "只是朕会尽力多分你一些，好么？"

                        elif hdxingge == "风流":
                            皇上 "当然是——朕的爱妃您了。"
                            我 "咦……皇上，折煞臣妾了……"
                            皇上 "你在心上，既为“您”，朕真心如此，何来折煞？"
                            我 "皇上……"
                            皇上 "嘘……"
                            皇上 "（深吻）"
                            我 "唔……"
                            皇上 "（意犹未尽。）"
                            皇上 "起码，现在是你。"
                        else:

                            皇上 "朕最爱的人……[aifei]还真是难倒朕了。"
                            皇上 "朕最敬爱之人，自然是父皇和母后。朕最爱护之人，则是朕的子民。朕最疼爱之人，则是朕的后嗣。"
                            我 "那臣妾呢……臣妾算什么？"
                            皇上 "你……你是朕的眼前人，是应珍惜之人。"
                            皇上 "[aifei]，有你陪着朕，朕很高兴。 "
                    "喜欢什么样的女人":



                        if hdxingge == "冷漠":
                            皇上 "朕喜欢聪明的，不会缠着朕问些奇奇怪怪问题的人。"
                            menu:
                                "哦！":
                                    皇上 "不过，你例外。虽然蠢，但还是挺可爱的。"
                                "臣妾知错了":
                                    皇上 "不过，你例外。"
                        elif hdxingge == "腹黑":
                            皇上 "朕喜欢乖巧懂事的，能够体贴温柔地陪在朕身边便好。"
                        elif hdxingge == "温柔":
                            皇上 "爱妃不必在意这些，不必刻意逢迎朕的喜好，做你自己便好。"
                            皇上 "别失了尊卑、乱了纲纪，朕便能护着你。"
                        elif hdxingge == "风流":
                            皇上 "朕爱美人，爱佳人，爱[aifei]。"
                            皇上 "（亲你一口。）"
                        else:
                            皇上 "朕心中最完美的女人，其形其容，其言其行，其思其德，皆为天下妇人之典范。"
            "（装睡）":

                if hdxingge == "冷漠":
                    皇上 "……"
                    皇上 "…………"
                    皇上 "………………"
                    皇上 "（得想个办法好好收拾一顿这个女人）"
                    $ my.love += 2
                elif hdxingge == "刚正":
                    皇上 "……也是，[aifei]应当困了。"
                    皇上 "睡吧。"
                else:
                    皇上 "（轻笑了一声，替你掖了掖被角。）"
    else:

        pass


    if xingzhi >= 100:
        $ my.love += 10
        $ mustshiqin = 50
    elif 0 <= xingzhi <= 10:
        $ mustshiqin = 0
        $ my.love += 1
    else:
        $ mustshiqin = round(xingzhi*0.5)
        $ my.love += xingzhi*0.1
    $ my.exp = my.exp + 4



    $ my.shiqin = my.shiqin +1
    jump 结束本旬
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
