
define persistent.ycsz = True
define persistent.expspeed = 1
define persistent.mingxie = False
define persistent.auto_choice_delay = None
define config.auto_choice_delay = persistent.auto_choice_delay

define 我 = Character("[my.hao][my.weifen] [my.name]", color="#F08080",image="my")
define 皇上 = Character("皇帝  [guoxing][emperor]",color="#F7AB00")
define 太后 = Character("太后  [taihou]",color="#FF8C00")
define 皇后 = Character("皇后  [NPC_fz_list[0].name]",color="#990000")
define 旁白 = Character(None, kind=nvl, color="#c8c8ff")
define 李公公 = Character("大太监  李公公",color="#2F4F4F")
define 我的宫女 = Character("[my.Gongnv[0].level]  [my.Gongnv[0].name]",color="#3CB371",image="GN[my.Gongnv[0].face]")
image 赵公公 = "images/Special/御前太监.webp"
define 赵公公 = Character("御前太监  赵公公",color="#2F4F4F",image="赵公公")
define 莲稚 = Character("建章女官  莲稚",color="#3CB371",image="莲稚")
define 璇音 = Character("璇音阁主 素女")
define 霓裳 = Character("霓裳阁主 漆雕婵")
define 司乐 = Character("大司乐 泠伦")
define 太医令 = Character("太医令 容廷淮",color="#3CB371")
define 掌祀 = Character("掌祀 匀褚")
define 蒹葭 = Character("蒹葭")
define 容予 = Character("容予",color="#6495ED",image="容予")
define nvlaoshi = Character("先生 冯礼曦",color="#4169E1",image="冯礼曦")
define laoshi = Character("先生 章子楚",color="#4169E1",image="章子楚")


define 小太监 = Character("小太监",color="#2F4F4F")
define 来福 = Character("小太监 来福",color="#2F4F4F")
define 月姑姑 = Character("月姑姑",image="月姑姑")
define 孩子 = Character("[kid.cheng] [kid.name]")

image 孩子 = "images/Kid/[kid.face].webp"
image 掌祀 = "images/Special/掌祀.webp"
image 璇音 = "images/Special/璇音阁主.webp"
image 霓裳 = "images/Special/霓裳阁主.webp"
image 司乐 = "images/Special/大司乐.webp"
image 寝居 = "bg/主角房间/[qinjutu].webp"
image 皇宫 = "Maps/地图-[map1]-[map2].webp"
image 先生 = "images/Special/章子楚.webp"
image 女先生 = "images/Special/冯礼曦.webp"

define 妃子 = Character("[fz.hao][fz.weifen] [fz.name]")
define 宫女 = Character("[gn.level] [gn.name]",image="GN[gn.face]")
define fz2 = Character("[fz2.hao][fz2.weifen] [fz2.name]")
image fz2 = "images/Feizi/F[fz2.face].webp"
image tempgn = "images/Gongnv/GN[tempgn.face].webp"



define 阿檀 = Character("司祝 阿檀",image="阿檀")
define 楚欢 = Character("[chuhuan.hao][chuhuan.weifen] [chuhuan.name]",image="楚欢")
define 陶凝 = Character("[taoning.hao][taoning.weifen] [taoning.name]",image="陶凝")








label start:

    $ _game_menu_screen = None
    $ _ignore_action = True

    python:
        juqingfei = []


        sanfei_list = ["淑妃","德妃","贤妃"]
        jiupin_list = ["昭仪","昭容","昭媛","修仪","修媛","修容","充仪","充媛","充容"]
        weifen_Normal = [[0,"皇后",1,2101,9999,0,240],[1,"贵妃",1,1750,2200,0,200],[2,["淑妃","德妃","贤妃"],3,1450,1800,0,180],[3,"妃",2,1150,1500,0,150],[4,["昭仪","昭容","昭媛","修仪","修媛","修容","充仪","充媛","充容"],9,970,1200,0,120],[5,"贵嫔",9,770,1000,0,100],[6,"婕妤",9999,625,800,0,80],[7,"容华",9999,475,650,0,60],[8,"嫔",9999,380,500,0,50],[9,"贵人",9999,280,400,0,40],[10,"美人",9999,230,300,0,40],[11,"才人",9999,180,250,0,30],[12,"常在",9999,130,200,0,30],[13,"御女",9999,80,150,0,20],[14,"选侍",9999,50,100,0,20],[15,"答应",9999,10,60,0,10],[16,"更衣",9999,-50,20,0,10],[17,"庶人",9999,-9999,0,0,0]]

        weifen_list = []
        xing_list = ["王","陈","李","王","陈","李","黎","成","刘","刘","柳","黄","花","沈","沈","苏","苏","凤","兰","冷","廖","金","洪","荣","戚","秦","戚","秦","关","谷","董","殷","殷","辛","郑","梅","左","武","郁","邓","万","甄","沈","宋","宋","风","向","钟","谢","钟","谢","曾","戴","公孙","长孙","独孤","夏侯","季","蔺","吴","鄢","景","季","蔺","吴","鄢","景","云","岳","尚","商","姚","姚","迟","饶","展","荆","海","魏","卫","魏","卫","朱","祝","祝","兰","苏","舒","萧","萧","肖","林","林","林","凌","连","安","庄","华","年","曾","罗","洛","孙","简","贺","纳兰","尹","伊","倪","习","叶","叶","岳","慕容","慕容","童","周","张","周","张","章","杨","赵","陆","路","赵","陆","路","袁","代","易","何","付","何","付","钟","田","孟","孟","温","文","闻","江","姜","姜","蒋","冯","郭","虞","郁","余","俞","容成","傅","欧阳","上官","晏","韩","梁","常","容","司马","司徒","闵","卓","言","颜",
        "胡","楚","顾","墨","潘","拓跋","邱","郭","薛","唐","薛","唐","汤","晋","庄","徐","许","徐","许","吕","卢","荀","施","齐","司","祁","施","齐","司","祁","姬","姒","木","穆","慕","木","穆","慕","白","夏","谭","方","方","云","曲","水","阮","宁","任","史","乔","周","上官","慕容","楚","禇","温","车","朱","秦","尤","何","贺","戚","言","华","陶","余","喻","水","窦","云","苏","潘","葛","任","袁","柳","唐","连","练","廉","费","裴","岑","薛","越","汤","滕","罗","洛","骆","安","常","毕","时","傅","齐","顾","孟","平","穆","萧","姚","邵","湛","明","臧","伏","谈","祝","杜","阮","纪","尹","袭","席","路","娄","魏","危","梅","童","林","夏","胡","凌","霍","蔡","徐","柯","昝","卢","莫","房","解","应","丁","宣","崔","嵇","荀","杨","甄","封","靳","段","景","段","景","郗","班","宁","詹","薄","薄","蒲","蔺","翟","晏","晏","鱼","易","慎","耿","简","关","竺"]


        ming_list = ming1_list + teshuming


        list_femaleface = list(range(1,426))
        pre_femaleface = list(range(1,426))
        hao_list = ["昭","明","靖","元","妍","贞","嘉","安","定","令","荣","宸","庄","敬","慈","懿","琪","祁","贤","穆","茂","良","淑","佳","恪","瑞","和","慎","端","顺","纯","裕","谦","全","昌","平","肃","哲","敏","芊","华","梅","媚","姣","姝","柔","怡","玫","姗","惠","娴","德","婉","仪","雅","容","穗","蕊","慧","蕙","徽","肃","慎","睦","恭","敬","秀","丽","清","欢","芬","芳","玉","瑶","琼","琳","静","婧","瑾","瑜","璎","珞","灵","澈","恩","淳","颖","悠","绮","纤","婳","晔","滟","逸","舒","畅","锦","倩","念","茵","衍","鸢","文","希","玺","康","思","欣","馨","晴","沁","澄","凝","泠","丹","兰","黛","娆","念","薇","茹","依","涟","鸾","景","谧","润","韶","潇","妧","蔚","汐","湘","绣","璇","诩","煦","吟","嫣","英","滢","窈","颐","莹","芷","旖","黎","洁","沐","苒","澜","楚","妤","沛","曼","韵","倾","瑛"]
        prehao_list = ["昭","明","靖","元","妍","贞","嘉","安","定","令","荣","宸","庄","敬","慈","懿","琪","祁","贤","穆","茂","良","淑","佳","恪","瑞","和","慎","端","顺","纯","裕","谦","全","昌","平","肃","哲","敏","芊","华","梅","媚","姣","姝","柔","怡","恬","玫","姗","惠","娴","德","婉","仪","雅","容","穗","蕊","慧","蕙","徽","肃","慎","睦","恭","敬","秀","丽","清","欢","芬","芳","玉","瑶","琼","琳","静","婧","瑾","瑜","璎","珞","灵","澈","恩","淳","颖","悠","绮","纤","婳","晔","滟","逸","舒","畅","锦","倩","念","茵","衍","鸢","文","希","玺","康","思","欣","馨","晴","沁","澄","凝","泠","丹","兰","黛","娆","念","薇","茹","依","涟","鸾","景","谧","润","韶","潇","妧","蔚","汐","湘","绣","璇","诩","煦","吟","嫣","英","滢","窈","颐","莹","芷","旖","黎","洁","沐","苒","澜","楚","妤","沛","曼","韵","倾","瑛"]


        palace0 = [["关雎宫",0],["昭鸾殿",""],["云意阁",""],["云通阁",""],["瑞雀楼",""],["朱鸟苑",""],["怡然馆",""],["晴水居",""],["景平轩",""],["伊然小筑",""]]
        palace1 = [["未央宫",0],["大澈殿",""],["垂茵阁",""],["品幽阁",""],["红绡楼",""],["飞霜苑",""],["霁月馆",""],["萃薇居",""],["碧萦轩",""],["烟雨小筑",""]]
        palace2 = [["忘忧宫",0],["漪兰殿",""],["凝霜阁",""],["垂露阁",""],["荔茵楼",""],["莹心苑",""],["清韵馆",""],["景凝居",""],["清芷轩",""],["浣缨小筑",""]]
        palace3 = [["伏莘宫",0],["长生殿",""],["邀月阁",""],["连星阁",""],["曦照楼",""],["云芙苑",""],["皓雪居",""],["幽梦馆",""],["浅黛轩",""],["竹雅小筑",""]]
        palace4 = [["宓秀宫",0],["披香殿",""],["梅香阁",""],["撷芳阁",""],["棠梨苑",""],["芳菲馆",""],["凝香居",""],["桂芜楼",""],["海棠轩",""],["玉兰小筑",""]]
        palace5 = [["瑶倾宫",0],["瑶光殿",""],["宝璎阁",""],["瑶华阁",""],["丽瑾楼",""],["蕊珠苑",""],["弄玉馆",""],["明玉居",""],["馥玉轩",""],["画玉小筑",""]]

        palaces = [palace0,palace1,palace2,palace3,palace4,palace5]
        guanyuan_list = []
        NPC_fz_list = []
        NPC_newfz_list =[]


        shengyuzhengdian_list = list(range(0,6))
        shengyucedian_list = list(range(0,6))

        huangzi = ["大皇子","二皇子","三皇子","四皇子","五皇子","六皇子","七皇子","八皇子","九皇子","十皇子","十一皇子","十二皇子","十三皇子","十四皇子","十五皇子","十六皇子","十七皇子","十八皇子","十九皇子","二十皇子","二十一皇子","二十二皇子","二十三皇子","二十四皇子","二十五皇子","二十六皇子","二十七皇子","二十八皇子","二十九皇子","三十皇子"]
        gongzhu = ["大公主","二公主","三公主","四公主","五公主","六公主","七公主","八公主","九公主","十公主","十一公主","十二公主","十三公主","十四公主","十五公主","十六公主","十七公主","十八公主","十九公主","二十公主","二十一公主","二十二公主","二十三公主","二十四公主","二十五公主","二十六公主","二十七公主","二十八公主","二十九公主","三十公主"]
        tempnum = 0








    call screen choiceplayer
    jump newplayer

label after_load2:
    return


label overture:
    scene 冥府
    with fade

    show screen notify("忘川")

    旁白 "一望无际的黑暗与阴寒。"
    nvl clear
    旁白 "与人间截然不同的景色……"
    nvl clear
    旁白 "脑海中涌入无数碎片，支离斑驳，无法拼凑。"
    nvl clear

    menu:
        "我是谁？这里是哪里？":

            pass

    旁白 "你努力睁开沉重的眼睛，只能感觉到绝望与痛苦席卷而来。"
    nvl clear
    旁白 "你朝着前方唯一一道微弱迷离的光追寻而去，一个身影逐渐清晰明亮。"
    nvl clear
    旁白 "一个女子站在那片鲜艳如血的曼珠沙华之中，容颜绝世而诡丽。"
    nvl clear


    show 冥妃 at chara with dissolve


    "神秘女子" "呵呵……"
    "神秘女子" "已经多久没有见到像你这样幽怨的魂灵了呢？"
    "神秘女子" "可怜的孩子，让我看看是什么束缚着你，让你不得安宁？"






    "……"

    "神秘女子" "原来是个被弃的嫔妃。"
    "神秘女子" "世间女子多凄苦……"
    "神秘女子" "虽然无法体会你的感受，不过我倒是很愿意帮你呢。"
    "神秘女子" "代价就是你这飘零破碎的灵魂。"
    "神秘女子" "如何，愿意同我做这个交易么？"






    menu:
        "为何要帮我？":
            pass

    "神秘女子" "哦，原是不相信我。"
    "神秘女子" "你来看看这个……"

    "她的手中聚集起华丽的光芒，展现出一副奇妙的画卷。"
    hide 冥妃
    show 星云卷 at chara with dissolve
    pause 1.0
    menu:
        "这是……":
            pass

    "一个年幼的女孩儿躺在榻上，双目紧闭。"
    "你甚至隐约能够听到哭声。"
    hide 星云卷
    show 冥妃 at chara
    "神秘女子" "她本是阳寿未尽，却不知何故突然魂飞魄散，我倒是棘手的很呐……"
    "神秘女子" "这孩子未来的命数，原本也是深陷宫闱。正好将你的魂渡给她，替她走过余生，再献祭于我。"
    "神秘女子" "不过这孩子阳寿也堪堪剩下二十载罢了，于你，可足够了？"
    menu:
        "足矣。":
            pass

    "神秘女子" "那便……"
    "神秘女子" "二十年后，再在此处相见罢。"
    "神秘女子" "可怜的……{w}绊心人。"

    hide 冥妃

    旁白 "宫闱的门就在你的眼前——"
    nvl clear
    旁白 "一个女子最美丽的二十年就要在此度过。"
    nvl clear
    旁白 "接下来的故事，由你来撰写。"
    nvl clear
    jump startgo

label startgo:
    if my.xing == "易" and my.ming == "珊绫":
        $ my.skillcosts = 130
    else:
        $ my.skillcosts = 10 + (my.age-14)*5
    show 容锦
    "弦歌容锦" "各位娘娘，0.5版本新增了{color=#FF3030}“技能”{/color}系统！！初始默认是没有任何技能的，需要自己{color=#FF3030}分配点数{/color}。所以请记得入宫后在{color=#FF3030}主角属性面板左下角的“技能”界面{/color}升级自己的技能！"
    "弦歌容锦" "技能界面上有具体说明，不知道每个技能有什么用的话，把鼠标或手放在技能名字下方的“升级”或者“不可升级”等字样就能看到{color=#FF3030}技能说明{/color}了！"
    "弦歌容锦" "还有关于新版的一些{color=#FF3030}{/color}常见问题，都放在“召见婢女”的选项内了，有什么疑问可以先去看一下，也许就能解决你的问题了！"
    "弦歌容锦" "{color=#FF3030}一定要去点技能啊！{/color}"


    menu:
        "知道了！":
            pass
        "会记得！":
            pass
        "我偏不！":
            $ my.skillcosts = 0
    hide 容锦
    if player == 0:
        jump start_0
    elif player == 1:
        jump start_1
    elif player == 2:
        jump start_2
    else:
        pass


label start_0:
    python:
        import copy
        weifen_list = []
        weifen_list = copy.deepcopy(weifen_Normal)
        yuanweifen = copy.deepcopy(weifen_Normal)
        yuanweifen = tuple(yuanweifen)
        beifei = len(yuanweifen)-1
        global yuanweifen

        for i in yuanweifen:
            if isinstance(i[1],str):
                pass
            else:
                i[1] = tuple(i[1])

        for i in weifen_list:
            if isinstance(i[1],tuple):
                i[1] = list(i[1])

    scene 京城远景
    with fade
    $ nianhao = "建昭"
    $ year = 1
    $ month = renpy.random.randint(3,6)
    if my.xing == "易" and my.ming == "珊绫":
        $ money = 1000
    elif my.familylevel == 10:
        $ money = 100
    elif my.familylevel == 11:
        $ money = 20
    else:
        $ money = 50+ 5*(12-my.familylevel)

    call hajime from _call_hajime
    $ lucky = renpy.random.randint(4,8)
    $ Creat_Feizi(lucky,0)



    python:
        lucky = renpy.random.randint(0,10)
        if lucky > 8:
            lucky = 3
        elif lucky > 6:
            lucky = 2
        elif lucky > 4:
            lucky = 1
        else:
            lucky = 0
        num = 0
        while num < lucky :
            num += 1
            fz = renpy.random.choice(NPC_fz_list)
            Creat_Kids(fz)
            fz.exp += 100
        if lucky == 3:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)
            NPC_Kids_list[2].age = 0

        elif lucky == 2:
            NPC_Kids_list[0].age = renpy.random.randint(2,3)
            NPC_Kids_list[1].age = renpy.random.randint(0,1)

        elif lucky == 1:
            NPC_Kids_list[0].age = renpy.random.randint(0,3)
        else :
            pass
        year = 4
        NPC_Kids_list = sorted(NPC_Kids_list, key=attrgetter("age"),reverse = True)
        for i in NPC_Kids_list:
            temptext = str(year-i.age)+"年"+str(month)+"月，为"+str(i.shengmu.name)+"所生。\n"
            i.story.append(temptext)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("exp"),reverse = True)

        for i in NPC_fz_list:
            tags_limitcheck(i)
            Feizilevel_first(i)




    $ year = 4
    $ xiunvnum = renpy.random.randint(3,7)
    $ Creat_Feizi(xiunvnum,1)
    $ xiunvnum = xiunvnum +1


    python:

        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
        Kidsnum = len(NPC_Kids_list)
        for i in NPC_fz_list:
            renpy.call("定义妃子",fz = i,from_current=False)

    image 皇后 = "Feizi/F[NPC_fz_list[0].face].webp"
    nvl clear

    旁白 "{cps=*0.5}初元二十八年，先帝驾崩。太子[emperor]继承大统，改元[nianhao]。{/cps}"
    nvl clear
    旁白 "{cps=*0.5}[nianhao]四年[month]月，因圣上膝下贫瘠，为稳固国之根基，故诏天下诸道州县，广选秀女，以实六宫。{/cps}"
    nvl clear
    with fade
    旁白 "{cps=*0.5}经宫中教习一月后，众秀女经由圣上殿选，最终入选者共[xiunvnum]人。{/cps}"


    nvl clear
    旁白 "{cps=*0.5}其中，你——{w}[my.family][my.name]亦在其列。{/cps}"
    nvl clear
    scene 府外
    with fade
    "之前你在储秀宫中，曾听教习嬷嬷说，殿选三日后，册封的旨意就会下达。"
    "你回想起三日前的场景……"
    $ my.hao = ""
    $ my.weifen = "秀女"

    scene 储秀宫
    with dissolve
    show screen notify("储秀宫")
    $ fz = NPC_fz_list[0]
    "正殿之上——当今圣上[emperor]、[fz.hao][fz.weifen][fz.name]、太后[taihou]端居高座。"
    "漫长的等待之后……"
    "宫人" "宣——{p}[my.family][myname1]氏[myname2]觐见。"
    menu:
        "走上前去":
            pass

    show 太后 at chara
    太后 "抬起头来。"
    menu:
        "抬头":
            pass

    if my.familylevel < 4:
        太后 "嗯，倒是不错，没有辱没了你父亲的名声。{p}皇帝可喜欢？"
    elif my.beauty > 900:
        show fz at chara
        妃子 "这……皇上，这可是不得多的的美人啊。"
        hide fz
        "你缓缓抬头，却看到[emperor]略有些失神错愕的眼神。"
    elif my.beauty > 700:
        太后 "模样倒是俊俏。皇上应当喜欢。"
    elif my.lucky > 100:
        太后 "这丫头看起来倒是个有福气的。"
    elif my.qizhi > 700:
        show fz at chara
        妃子 "气质很是出挑。不知陛下意下如何？"
    elif my.meili >700:
        show fz at chara
        妃子 "倒是媚骨天成，丽而不妖。"
    else:
        太后 "看起来不大出挑，可有才艺？"
        hide 太后
        hide fz
        hide 皇帝
        if my.dance > my.muzic and my.dance >my.book and my.dance > my.cixiu:
            menu:
                "善歌舞":
                    pass
            我 "（于大殿之中，轻展衣袖，回旋而舞。）"
            if my.dance > 80:
                我 "（体态婀娜，如流风回雪。美目盼兮，如秋水连漪。）"
                show 太后 at chara
                "太后" "这丫头的舞技倒是可堪一绝。"
            else:
                show 太后 at chara
                "太后" "这丫头的舞技倒是尚可。"

        elif my.muzic > my.dance and my.muzic >my.book and my.muzic > my.cixiu:
            menu:
                "善音律":
                    pass
            我 "（取来一琴，指尖轻动，琴声渐起。）"
            if my.muzic > 80:
                我 "（时而如高山流水，时而如小溪潺潺，悲欢缓急，尽付琴中。）"
                show 太后 at chara
                "太后" "这丫头的舞技倒是可堪一绝。"
            else:
                show 太后 at chara
                "太后" "这丫头的琴技倒是尚可。"

        elif my.book > my.dance and my.book >my.muzic and my.book > my.cixiu:
            menu:
                "喜诗书":
                    pass
            我 "（取来笔墨，横展纸卷，执笔横书。）"
            if my.book > 80:
                我 "（翰墨挥洒，下笔生花。）"
                show 太后 at chara
                "太后" "这手字的确写得极好。"
            else:
                show 太后 at chara
                "太后" "这副字也算是尚可。"
        else:
            menu:
                "擅女红":
                    pass
            我 "回太后娘娘，小女无甚才艺，只闲时在闺中玩弄些刺绣织缝的玩意。"
            我 "(呈上自家中带来的绣图。)"
            if my.cixiu > 80:
                show 太后 at chara
                "太后" "好精致的绣图，竟连宫里负责织造的宫人也被你给比下去了。"
            else:
                show 太后 at chara
                "太后" "针脚齐平，心思秀巧，算是尚可。"
        show fz at chara
        妃子 "母后似乎对她还算喜欢，不知皇上意下如何？"

    hide 太后
    hide fz
    show 皇帝 at chara
    if hdxingge =="冷漠":
        皇上 "（沉默不语，似是兴致缺缺。）"
        hide 皇帝
        show 太后 at chara
        太后 "罢了，留牌子。"
    elif hdxingge == "腹黑":
        皇上 "（笑而不语，未置一词。）"
        hide 皇帝
        show 太后 at chara
        太后 "罢了，留牌子。"
    elif hdxingge =="风流" and my.beauty>700:
        皇上 "朕很喜欢，留下吧。"
    elif hdxingge == "温柔" and my.qizhi>700:
        皇上 "这姑娘合朕眼缘，留牌子。"
    elif hdxingge == "温柔" or hdxingge == "刚正":
        皇上 "儿臣听母后的。"
        hide 皇帝
        hide fz
        show 太后 at chara
        太后 "那便留下吧。"
    else:
        皇上 "（沉默片刻。）"

        皇上 "留牌子。"
    hide 皇帝
    show fz at chara
    妃子 "还不谢恩？"
    menu:
        "谢恩。":
            pass
    hide fz
    show 太后 at chara
    太后 "下去吧。"
    hide 太后
    "你缓缓退出殿外。"
    "其余一众秀女，被留用者自然欣喜，而未能中选者各自忧愁。"
    "而你只知道——"
    menu:
        "自己终究成了这宫墙之内的囚鸟":
            $ my.qingxiang = 10
        "往后，一切随缘便是":
            $ my.qingxiang = 25
        "人不犯我，我不犯人，但求问心无愧":
            $ my.qingxiang = 40
        "愿得圣恩庇佑，不受深宫寂寞之苦":
            $ my.qingxiang = 60
        "后宫之中，终将会有属于自己的一片天地":
            $ my.qiangxiang = 75
        "若不攀得荣华富贵，又为何来此一遭？":
            $ my.qingxiang = 90
    $ allstory =[]
    $ tempstory = "【大事】"+"4年"+str(month)+"月，新秀入宫。\n"
    $ allstory.insert(0,tempstory)

    scene 府外
    with fade
    "正当你失神之际，却听到远处传来马车的声响。"
    "家中上下齐聚门外。"
    "官员" "秀女[my.name]接旨！"
    menu:
        "跪下":
            pass
    我 "臣女在。"
    "官员" "“秀女[myname1]氏[myname2]，仪容肃恭，德行出众，柔嘉成性，淑慎持躬。"
    python:
        my.shou = renpy.random.randint(45,65)
        if my.health < 300:
            my.shou = my.shou - renpy.random.randint(5,10)
        elif my.health > 700:
            my.shou = my.shou + renpy.random.randint(5,10)
        else:
            pass
        if my.beauty > 900:
            my.shou = my.shou - renpy.random.randint(5,10)
        elif my.beauty < 400:
            my.shou = my.shou + renpy.random.randint(5,10)
        else:
            pass

        tempnum = my.dance + my.book + my.cixiu + my.muzic
        tempnum2 = my.familylevel
        if my.familylocation == "义女":
            tempnum2 = my.familylevel + 2
        elif my.familylocation == "庶女":
            tempnum2 = my.familylevel + 1
        else:
            pass

        a = int(len(weifen_list)*0.5)
        my.exp = weifen_list[a][3] - weifen_list[a][3]*(tempnum2*0.12)  + my.beauty/40 + my.qizhi/80 + my.meili/80 + my.love + renpy.random.randint(-30, 50)
        for i in my.father.feizi:
            for x in my.father.feizi:
                if x != i and x not in i.sisters:
                    i.sisters.append(x)
                if x != i and i not in x.sisters:
                    x.sisters.append(i)

        for i in my.sisters:
            my.exp += i.love*0.1
            if i.exp >= weifen_list[0][3]:
                my.exp += weifen_list[0][3]*0.05
            elif i.exp <= 0:
                pass
            else:
                my.exp += i.exp*0.05
            if i.name == "魏锦书":
                pass
            else:
                i.like += renpy.random.randint(-50,80)

        if my.exp < 0:
            my.exp = 0
        else:
            pass
        tags_limitcheck(my)

        Feizilevel(my)

        if my.level < 11:
            lucky = renpy.random.randint(0, 4)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""

        elif my.love > 10 :
            lucky = renpy.random.randint(0, 5)
            if lucky == 0:
                my.hao = renpy.random.choice(hao_list)
                hao_list.remove(my.hao)
            else :
                my.hao = ""
        else:
            my.hao = ""
        my.story = []

        if my.hao == "":
            tempstory = str(nianhao)+"四年，经由选秀入宫，册为"+str(my.weifen)+"。\n"
            my.story.append(tempstory)
        else:
            tempstory = str(nianhao)+"四年，经由选秀入宫，册为"+str(my.weifen)+"，赐封号"+str(my.hao)+",是为"+str(my.hao)+str(my.weifen)+"。\n"
            my.story.append(tempstory)


        if my.hao =="":
            my.cheng = myname1 +my.weifen
        else:
            my.cheng = my.hao +my.weifen
        randompalace(my)
        NPC_fz_list.append(my)
        NPC_newfz_list.append(my)
        NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("level"),reverse = False)
    "官员" "故今册尔为{color=#FF3030}[my.hao][my.weifen]{/color}，充侍内廷。”"

    "官员" "“……即刻入宫，不得有误。钦此！”"

    我 "臣……{w}妾……"
    我 "接旨。"
    menu:
        "进入宫廷":
            pass

    scene black
    with dissolve

    $ _game_menu_screen = "save"
    李公公 "[my.cheng]请进。"


    $ qinjutu = "寝居1白天"
    $ bg("寝居")
    with dissolve
    show screen notify(my.palace+my.qinju)
    show 李公公 at chara
    李公公 "往后这里便是您的住处了。"
    menu:
        "多谢公公":
            pass
    李公公 "[my.cheng]客气了。"
    李公公 "您刚刚入宫，身边需要几个得利的宫人伺候。"
    李公公 "（朝外招了招手。）"

    image GN小春 = "Gongnv/GN小春.webp"
    image GN阿夏 = "Gongnv/GN阿夏.webp"
    image GN秋子 = "Gongnv/GN秋子.webp"
    image GN冬儿 = "Gongnv/GN冬儿.webp"

    show GN小春 at chara
    "{color=#3CB371}小春{/color}" "奴婢给[my.cheng]请安了！"
    show GN阿夏 at chara
    "{color=#3CB371}阿夏{/color}" "奴婢阿夏给[my.cheng]请安。"
    show GN秋子 at chara
    "{color=#3CB371}秋子{/color}" "奴婢秋子给[my.cheng]请安。"
    show GN冬儿 at chara
    "{color=#3CB371}冬儿{/color}" "奴婢冬儿给[my.cheng]请安。"
    $ bg("寝居")
    show 李公公 at chara
    李公公 "就是这四位了，不知道您更中意哪一个？"
    "宫女小春，年方十四，单纯可爱，勤劳善良。{p}宫女阿夏，双八年华，年轻漂亮，活泼开朗。"
    "宫女秋子，芳龄十八，温柔知礼，行事规矩。{p}宫女冬儿，双十之龄，行事沉稳，勤俭低调。"

    menu:
        "小春":
            show GN小春 at chara
            "{color=#3CB371}小春{/color}" "奴婢一定好好伺候您的！保证听您的吩咐！"
            image 我的宫女 = "Gongnv/GN小春.webp"
            python:
                my.Gongnv.append(chun)
                NPC_Gongnv_list.append(chun)
            jump 宫女赐名
        "阿夏":
            show GN阿夏 at chara
            "{color=#3CB371}阿夏{/color}" "奴婢多谢[my.cheng]娘娘的赏识，奴婢一定会好好服侍您的！"
            image 我的宫女 = "Gongnv/GN阿夏.webp"
            python:
                my.Gongnv.append(xia)
                NPC_Gongnv_list.append(xia)
            jump 宫女赐名
        "秋子":
            show GN秋子 at chara
            "{color=#3CB371}秋子{/color}" "是，奴婢一定对[my.cheng]尽心尽力。"
            image 我的宫女 = "Gongnv/GN秋子.webp"
            python:
                my.Gongnv.append(qiu)
                NPC_Gongnv_list.append(qiu)
            jump 宫女赐名
        "冬儿":
            show GN冬儿 at chara
            "{color=#3CB371}冬儿{/color}" "是，奴婢遵命。"
            image 我的宫女 = "Gongnv/GN冬儿.webp"
            python:
                my.Gongnv.append(dong)
                NPC_Gongnv_list.append(dong)
            jump 宫女赐名
        "都不中意":
            $ bg("寝居")
            show 李公公 at chara
            李公公 "那稍后奴才再让掖廷那边按照您的位份给您分配宫人过来。"
            jump 初入宫闱

label 宫女赐名:
    $ bg("寝居")
    show 李公公 at chara
    李公公 "您可要为[my.Gongnv[0].name]赐名？"
    menu:
        "是":
            python:
                tempname = renpy.input("为宫女赐名",length=3)
                tempname = tempname.strip()

                if not tempname:
                    tempname = my.Gongnv[0].name
                my.Gongnv[0].name = tempname
        "否":

            pass
    show 李公公 at chara
    李公公 "那就由[my.Gongnv[0].name]伺候您了。"
    李公公 "稍后奴才再让掖廷那边按照您的位份给您分配别的宫人过来。"
    jump 初入宫闱

label 初入宫闱:

    python:

        if len(my.Gongnv) == 1:
            a = len(yuanweifen)
            if my.level == 0: 
                my.Gongnv[0].level = "长御"
                my.Gongnv[0].lv = 0
            elif my == 1: 
                my.Gongnv[0].level = "女官"
                my.Gongnv[0].lv = 1
            elif my.level > round(a-a/3):
                my.Gongnv[0].level = "贴身侍女"
                my.Gongnv[0].lv = 3
            else:
                my.Gongnv[0].level = "大宫女"
                my.Gongnv[0].lv = 2
        else:
            pass
        ChangeGongnv(my)

    if len(my.Gongnv) == 1:
        pass
    else:
        image 我的宫女 = "Gongnv/GN[my.Gongnv[0].face].webp"
        show 我的宫女 at chara
        我的宫女 "奴婢[my.Gongnv[0].name],参见[my.cheng]。以后就由奴婢伺候您的寝居了。"


    $ bg("寝居")
    with fade
    show 我的宫女 at chara
    我的宫女 "先让奴婢为您介绍一下今后在宫中的日常活动吧。"
    我的宫女 "一年四季，共十二个月，每个月分为上、中、下旬，每一旬又有清晨、中午、下午、傍晚、深夜。"
    我的宫女 "每一个时间段可以分别做出行动。不过，如果您的体质不够健康的话，体力耗尽的话，只能在寝宫中休息度过这段时间了。"
    我的宫女 "请您务必注意自己的玉体康健，如果抱恙的话，就只能待在寝居之中等待太医诊治，根据病情，可能会白白浪费大量的时间。"
    python:
        if my.health > 700:
            AP = 5
        elif my.health > 400:
            AP = 4
        elif my.health > 200:
            AP = 3
        elif my.health > 100:
            AP = 2
        elif my.health > 0:
            AP = 1
        else:
            AP = 0
    show screen calendar
    pause 1
    我的宫女 "您应该已经看到了，您现在每旬拥有[AP]个行动点。"
    我的宫女 "当然，请您放心，奴婢们也会为了主子的健康所努力的。"
    $ AP = 0
    show screen calendar
    我的宫女 "您一路车马劳顿一定已经很累了吧。为了您的身体着想，今天还是不要进行其他行动了。"

    menu:
        "明白了":
            pass













    我的宫女 "对了，奴婢对您的行事风格还不大清楚。不知[my.cheng]您打算以后如何规划宫里的开销呢？"
    menu:
        "节俭开销":
            $ kaixiao = 1
            我的宫女 "奴婢明白。"
        "正常开销":

            $ kaixiao = 2
            我的宫女 "奴婢明白。"
        "奢侈开销":

            $ kaixiao = 3
            我的宫女 "奴婢明白。"
        "详细解释":

            我的宫女 "节俭开销大概是您月俸的四分之一。{p}是最省钱的方式。{w}不过也会影响您的体质和在外的威信。"
            我的宫女 "普通开销大概是您月俸的一半。{p}对日常起居没有太大的影响。"
            我的宫女 "奢侈开销大概是您月俸的四分之三。{p}开销增大，自然也能让奴婢们多花心思增加为您强健体魄，也能树立起在外的威信。"
            我的宫女 "您打算如何安排呢？"
            menu:
                "节俭开销":
                    $ kaixiao = 1
                    我的宫女 "奴婢明白。"
                "正常开销":

                    $ kaixiao = 2
                    我的宫女 "奴婢明白。"
                "奢侈开销":

                    $ kaixiao = 3
                    我的宫女 "奴婢明白。"

    if my.Gongnv[0].xingge =="单纯":
        python:
            templist = []
            for i in NPC_fz_list:
                if i.year == 0 and i != my:
                    templist.append(i)
        我的宫女 "说起来，娘娘在储秀宫的时候，可有结交朋友？"
        $ firstfriend = templist[1]
        menu:
            "没有。":
                我的宫女 "啊？"
                我的宫女 "奴、奴婢失言了……"
                $ firstfriend = None
            "[firstfriend.name]":
                $ firstfriend.like = firstfriend.like + 50
                我的宫女 "原来是{color=#FF3030}[firstfriend.cheng]{/color}呀！"
                我的宫女 "奴婢记得她住在[firstfriend.palace][firstfriend.qinju]。娘娘既然与[firstfriend.cheng]在储秀宫已经结下了友谊，那往后也可以多加来往。"
    elif my.Gongnv[0].xingge =="机灵":
        python:
            templist = []
            for i in NPC_fz_list:
                if i.year == 0 :
                    templist.append(i)
        $ firstfriend = None
        $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
        $ tempfz = templist[0]
        if tempfz == my:
            我的宫女 "说起来，奴婢之前打听到，在秀女之中，皇上对您最是上心呢！"
            我的宫女 "奴婢觉得，皇上以后一定会您宠爱有加的！"
            menu:
                "（心花怒放）嘴真甜，赏":
                    我的宫女 "多谢主子！"
                    $ my.Gongnv[0].yexin = my.Gongnv[0].yexin - 5
                    $ money = money - 2
                "知道了":
                    pass
        else:
            我的宫女 "说起来，奴婢之前打听到，在秀女之中，皇上对{color=#FF3030}[tempfz.cheng]{/color}最是上心呢！"
            我的宫女 "这后宫这么多嫔妃，有谁不想得到圣上的垂青呢？"
            我的宫女 "您可要多多注意此人。"
    elif my.Gongnv[0].xingge =="聪颖":
        python:
            templist = []
            for i in NPC_fz_list:
                if i.year == 0 :
                    templist.append(i)
        $ firstfriend = None
        $ templist = sorted(templist, key=attrgetter("love"),reverse = True)
        $ tempfz = templist[0]
        if tempfz == my:
            我的宫女 "奴婢之前打听到，在秀女之中，皇上似乎对您最是垂青。"
            $ templist = sorted(NPC_newfz_list, key=attrgetter("taihoulike"),reverse = True)
            $ tempfz = templist[0]
            if tempfz == my:
                我的宫女 "太后也最欣赏您。"
            else:
                我的宫女 "而太后最欣赏{color=#FF3030}[tempfz.cheng]。"
        else:
            我的宫女 "奴婢之前打听到，在秀女之中，皇上似乎对{color=#FF3030}[tempfz.cheng]{/color}最是垂青。"
            $ templist = sorted(templist, key=attrgetter("taihoulike"),reverse = True)
            $ tempfz = templist[0]
            if tempfz == my:
                我的宫女 "而太后则最欣赏您。"
            else:
                我的宫女 "而太后最欣赏{color=#FF3030}[tempfz.cheng]{/color}。"
    else:
        python:
            templist = []
            for i in NPC_fz_list:
                if i.year == 0 :
                    templist.append(i)
        $ firstfriend = None
        $ templist = sorted(templist, key=attrgetter("level"),reverse = False)
        $ tempfz = templist[0]
        if tempfz == my:
            我的宫女 "奴婢打听到，这届新秀之中，您的位分最高。"
            我的宫女 "这会儿宫里大抵有不少眼睛在盯着您吧，还请您小心谨慎。"
            menu:
                "不足为惧":
                    $ my.xinji = my.xinji -10
                "明白了":
                    $ my.xinji = my.xinji +10
        else:
            我的宫女 "奴婢打听到，这届新秀之中，{color=#FF3030}[tempfz.cheng]{/color}的位分最高。"
            我的宫女 "若您有心，可以多加注意。"

    if NPC_fz_list[0].level == 0:
        我的宫女 "按规矩，明日一早，新秀们应去皇后娘娘宫里拜谒请安，可万万疏忽不得。"
    else:
        我的宫女 "按规矩，秀女入宫后应去凤仪宫拜谒请安。只是如今宫中后位空悬，皇上亦是体谅各位主子，便免了此礼。"
    我的宫女 "奴婢服侍您歇息吧。"


    hide screen calender
    scene black
    with fade
    旁白 "一夜过去……"
    python:
        for i in NPC_fz_list:
            i.paixu = beifei - i.level
    $ NPC_fz_list = sorted(NPC_fz_list, key=attrgetter("paixu","exp"),reverse = True)
    python:
        if my.health > 700:
            AP = 5
        elif my.health > 400:
            AP = 4
        elif my.health > 200:
            AP = 3
        elif my.health > 100:
            AP = 2
        elif my.health > 0:
            AP = 1
        else:
            AP = 0
    if NPC_fz_list[0].level == 0:
        jump 初次请安_准备
    else:
        $ month = month +1
        $ datenum = 1
        $ timenum = 1
        jump 寝居界面

label 养成开始:
    $ mapname = "寝居"
    show screen myroom
    call screen Myroombuttons
    show screen notify(my.palace+my.qinju)



label 寝居界面:
    $ renpy.scene(layer='screens')
    $ renpy.scene("black")

    with dissolve


    $ bgm("Bigmap")
    $ mapname = "寝居"
    if my.level == beifei:
        $ qinjutu = "冷宫内"

        scene 冷宫内
        $ mapname = "冷宫"
        show screen Myroombuttons
        show screen calendar

        menu:
            "抄写经书":
                $ my.exp = my.exp + 2
                $ my.lucky = my.lucky +0.2
                "在冷宫内抄写经书，感觉心神宁静。"
            "浑噩度日":
                $ my.health = my.health + 2
                "浑噩度日……"
            "一死了之":
                jump 自尽
        python:
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)

        jump 结束本旬
    else:

        if my.level == 0:
            $ qinjutu = "凤仪宫内"
        elif my.level < 4:
            if timenum < 4:
                $ qinjutu = "寝居2白天"
            else:
                $ qinjutu = "寝居2傍晚"
        else:
            if timenum < 4:
                $ qinjutu = "寝居1白天"
            else:
                $ qinjutu = "寝居1傍晚"
        $ bg("寝居")
        with dissolve
        show screen calendar


        python:
            if timenum == 1 and time_1 == False:
                time_1 = True
                renpy.call("临时事件检测",from_current=False)
                renpy.call("侍寝事件检测",from_current=False)
            if timenum == 2 and time_2 == False:
                time_2 = True
                renpy.call("临时事件检测",from_current=False)
                renpy.call("侍寝事件检测",from_current=False)
            if timenum == 3 and time_3 == False:
                time_3 = True
                renpy.call("临时事件检测",from_current=False)
                renpy.call("侍寝事件检测",from_current=False)
            if timenum == 4 and time_4 == False:
                time_4 = True
                renpy.call("临时事件检测",from_current=False)
                renpy.call("侍寝事件检测",from_current=False)
            if timenum == 5 and time_5 == False:
                time_5 = True
                renpy.call("临时事件检测",from_current=False)
                renpy.call("侍寝事件检测",from_current=False)
        $ mapname = "寝居"
        if AP > 0 and timenum <= 5:
            pass
        else:

            jump 结束本旬
    show screen calendar


    show screen notify(my.palace+my.qinju)
    show screen myroom
    call screen Myroombuttons

label 皇宫界面:
    $ renpy.scene(layer='screens')
    $ renpy.scene("black")
    with dissolve
    $ mapname = "皇宫"
    $ bgm("Bigmap")
    $ bg("皇宫")
    show screen calendar


    python:
        if timenum == 1 and time_1 == False:
            time_1 = True
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)
        if timenum == 2 and time_2 == False:
            time_2 = True
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)
        if timenum == 3 and time_3 == False:
            time_3 = True
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)
        if timenum == 4 and time_4 == False:
            time_4 = True
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)
        if timenum == 5 and time_5 == False:
            time_5 = True
            renpy.call("临时事件检测",from_current=False)
            renpy.call("侍寝事件检测",from_current=False)
    if AP > 0 and timenum <= 5:
        pass
    else:

        jump 结束本旬
    show screen notify("皇宫")
    show screen Bigmap
    call screen Normalbuttons
















label 备用:
    show screen jm()
    我 "现在皇宫里共有[Kidsnum]位皇子。"


    return
 
