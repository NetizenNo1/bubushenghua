init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)






















image end_pic:
    "扇子.webp"
    size (35,35)
    block:
        rotate 0
        linear 3.0 rotate 360
        repeat


screen say(who, what):
    style_prefix "say"
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    outlines [ (absolute(1), "#FFFFFF", absolute(1), absolute(0.5)) ]
                    min_width 218
                    text_align 0.5


        text what id "what"



    if not renpy.variant("small"):
        add SideImage() xalign 0.04 yalign 1.0
    else:
        add SideImage() xalign 0.04 yalign 1.0




init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos











screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width








init python:
    import math
    choice_page = 0
    kids_page = 0

screen choice(items):
    style_prefix "choice"
    $ next_choice_page = choice_page + 1
    $ prev_choice_page = choice_page - 1
    $ max_choice_page = int(math.modf(len(items)/6)[1])
    $ b = choice_page*6+6
    $ c = items[next_choice_page*6:next_choice_page*6+6]


    if b >= len(items):
        $ b = len(items)
    else:
        pass

    vbox:
        for i in items[choice_page*6:b]:
            textbutton i.caption action SetVariable('choice_page', 0),i.action
        if choice_page > 0:
            textbutton "上一页" action SetVariable('choice_page', prev_choice_page)
        if choice_page < max_choice_page and max_choice_page > 1 and len(c)>0:
            textbutton "下一页" action SetVariable('choice_page', next_choice_page)

screen choice_zy_gn(list):
    modal True
    style_prefix "choice"
    $ next_choice_page = choice_page + 1
    $ prev_choice_page = choice_page - 1
    $ max_choice_page = int(math.modf(len(list)/5)[1])
    $ b = choice_page*5+5
    $ c = list[next_choice_page*5:next_choice_page*5+5]


    if b >= len(list):
        $ b = len(list)
    else:
        pass

    vbox:
        for i in list[choice_page*5:b]:
            textbutton i[0] action SetVariable('choice_page', 0),SetVariable('gn', i[1]),Hide("choice_zy_gn"),Return()
        textbutton "算了" action SetVariable('choice_page', 0),Hide("choice_zy_gn"),Jump("寝居界面")
        if choice_page > 0:
            textbutton "上一页" action SetVariable('choice_page', prev_choice_page)
        if choice_page < max_choice_page and max_choice_page > 1 and len(c)>0:
            textbutton "下一页" action SetVariable('choice_page', next_choice_page)





define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text:
    min_width 490

style choice_vbox:
    xalign 0.5
    ypos 338
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    background Frame("gui/button/choice_idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/choice_hover_background.webp", gui.button_borders, tile=gui.button_tile)
    xalign 0.5
    xsize 900
    ysize 45

    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")













screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            spacing 20

            textbutton _("返回") action Rollback()
            textbutton _("回顾") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("存档") action ShowMenu('save')
            textbutton _("快速存档") action QuickSave()
            textbutton _("快速读档") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')
        frame:
            background None
            style_prefix "quick"

            xalign 0.0
            yalign 1.0




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text


style quick_button:
    background Frame("gui/button/quick_idle_background.webp", gui.quick_button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/quick_hover_background.webp", gui.quick_button_borders, tile=gui.button_tile)

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 40
    font "问藏书房.ttf"
    color "#B22222"
    hover_color "#990000"
    outlines [ (absolute(1), "#E6E6FA", absolute(0), absolute(1)) ]











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("存档") action ShowMenu("save")


        textbutton _("读档") action ShowMenu("load")

        textbutton _("系统") action ShowMenu("preferences")
        if main_menu:

            textbutton _("鸣谢") action Show("thanks")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题画面") action MainMenu()



        if renpy.variant("pc"):





            textbutton _("退出游戏") action Quit(confirm=not main_menu)








style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



screen GiveMeMoney():
    frame xsize 960 ysize 540 xalign 0.5 yalign 0.5:
        background None
        text "点击任意处关闭" align (0.5,0.0)
        key "mousedown_1" action Hide("GiveMeMoney")
        add "gui/frame.webp" xalign 0.5 yalign 0.5
        add "恰饭.webp" xalign 0.5 yalign 0.5
        vbox align (0.95,0.05):
            text "{size=20}欢迎打赏作者喝奶茶~"
            text "{size=20}（打赏纯属自愿，学生党请量力而行）"
            text "{size=20}第0期打赏榜（2019.11.22-2019.11.30）榜首福利：" align (0.5,0.5)
            text "{size=20}指定某性格的皇帝制作一段1000字左右专属剧情" align (0.5,0.5)






screen main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background
    add "WhiteLight" align (0.5,0.5)



    frame




    use navigation
    if persistent.mingxie == False:
        use thanks


    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 350
    yfill True

    background "gui/overlay/main_menu.webp"

style main_menu_vbox:
    xalign 1.0
    xoffset -25
    xmaximum 1000
    yalign 1.0
    yoffset -25

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")



style thanks_text:
    font "问藏书房.ttf"
    size 25
    text_align 0.0

screen thanks:
    style_prefix "thanks"
    modal True
    frame xsize 1280 ysize 720 xalign 0.5 yalign 0.5:
        viewport:
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            xsize 1200
            ysize 600
            align (0.5,0.5)
            has vbox spacing 10
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【作者声明】" align (0.5,0.5)
            text "{color=#000000}该版本为游戏制作中的测试版本，仅通过官方群和作者本人网盘发布，任何在其他地方下载的游戏文件，均属侵权盗版。"
            text "{color=#000000}游戏内所使用的部分素材来自于网络，仅为测试期间使用，不涉及任何商业行为，在正式版公开发布时均会撤换。"
            text "{color=#000000}PC版支持玩家自行替换人物立绘，安卓版玩家可通过特殊手段替换立绘，由于涉及游戏拆包，在仅限自用的前提下，作者本人立场为：不提倡，不禁止。"
            text "{color=#000000}但严禁将游戏内素材破解外传、或破解其他游戏素材替换至本游戏内使用，此类侵权行为造成的后果均由破解者自行承担。"
            text "{color=#000000}《深宫曲》游戏除授权类/公共素材版权属于原作者以外，所有版权归游戏作者【弦歌容锦】所有。"
            text "{color=#000000}游戏内的玩法可参考、借鉴，范围包括但不限于游戏、小说、文字演绎，不必再向作者询问授权，但还望标明来源。"
            text "{color=#000000}但任何抄袭文字、剧情、设定的行为均属侵权。（以《深宫曲》为原作的同人创作除外。）"
            text "" align (0.5,0.5)
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【特别鸣谢】" align (0.5,0.5)
            text "{color=#000000}剧本/建议：酒腻 桃灼青 阿涛peach 仙女虾 孤高的养鸡人 "
            text "{color=#000000}立绘捐赠：游潇洒 念卿 夔斛 魏姐 遇见 小九九"
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【人物立绘】" align (0.5,0.5)
            text "{color=#000000}木寒阁：未以西、花舞卿、贰花  水墨蛋清：伏贼、饼子会飞  金风细雨：初九、七七、千皇 丹青客：咔咔、问问、魈尧  无言书生：烟雨  墨韵：迟秋 七弦祀：青落 杯莫亭：戊戌"
            text "{color=#000000}海底捞：遇瞳、斋虚沽御、沙拉肉肉酱、花千树  一页书：阿光、时年、月竹  光明顶：夜君  画重锦：惜语、兔小柒、张小娘子  欣里画：花盐 玉琼楼：开岁 千歌：翩跹 画夜：进击的喵 "
            text "{color=#000000}夯昊、八阿鸽、PAPA、米可、栖白、昇崎、糖又欣、臣子木、梧丘、勇、清鲤鲤、云芍、甜澄、秋寒、大碗猫耳面、白阿也、玖山、白月梦、红果儿、缪缪、小智、孤高的养鸡人"
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【游戏场景】" align (0.5,0.5)
            text "{color=#000000}风格洲 幽蓝朵朵 半盏灯 烟雨 舟行绿水 西行寺妖 夙汐飞飞 子说 3N"
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【其他素材】" align (0.5,0.5)
            text "{color=#000000}觅图网、柒夜迷走、疏楼曲-青萝蔓草、君氏清然、-遇瞳-、旧时明月、轻舟十寒、钮祜禄君念、小草清清呦、光明顶、相见欢、幼姝特效、苒苒烟几渡、米卷、阿苒Aran、白鹿、秦云北、軟糖PLUTO、缙云小朋友、寒叶临渡、月半狼叫、魔王魂、PerituneMaterial、枫刹若舞"
            text "{color=#000000}其余素材来源于网络"
        textbutton "{size=35}关闭" align (0.5,1.0) action SetVariable("persistent.mingxie",True),Hide("thanks")


screen tips:
    style_prefix "thanks"
    modal True
    frame xsize 1280 ysize 720 xalign 0.5 yalign 0.5:
        viewport:
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            xsize 1200
            ysize 600
            align (0.5,0.5)
            has vbox spacing 10
            text "{size=35}{color=#000000}{font=问藏书房.ttf}【针对0.5版本的一些常见问题】" align (0.5,0.5)
            text "{color=#000000}1.为什么我不能通过反复进出寝宫等方式刷随机剧情了？"
            text "{color=#000000}{size=22}答：改了代码，不能刷了。"
            text "{color=#000000}2.为什么一些对我厌恶或憎恨的妃子的好感一直提升不上来？"
            text "{color=#000000}{size=22}答：新增设定，一旦妃子对你的好感为负，想要再提升好感就非常困难了。结仇需谨慎。当然如果有足够的时间、精力和财力，也许能够将对方“感化”。"
            text "{color=#000000}3.怎样让父亲升官？"
            text "{color=#000000}{size=22}答：目前只有接济银两一种方法，可以增加父亲的功勋，除一品外，功勋到达100即可升职。"
            text "{color=#000000}4.平民和富商之女的家世不能提升了吗？"
            text "{color=#000000}{size=22}答：可以接济银两，或者等家里主动来要钱，同样是功勋值到达100即可发家/入仕。虽然不会出现在官员表里，但玩家可以通过特殊人物属性面板查看父亲的情况。"
            text "{color=#000000}5.官员的属性分别有什么用？可以提升吗？"
            text "{color=#000000}{size=22}答：能力：顾名思义，能力越高越容易得到功勋。{p}忠诚：忠诚越低越容易被皇帝所不喜，降低功勋和势力。{p}势力：越高越容易送族女入宫，对皇储的支持效果越大，但也越容易被皇帝所忌惮。{p}功勋：除一品外，功勋到达100即可升职。品级越低越容易得到功勋。{p}年龄：目前还没做死亡和告老还乡剧情，后期朝堂老龄化情况会比较严重。。{p}颜值：顾名思义，没有实际作用。{p}婚配状况：待完善。{p}目前能力、忠诚还没有办法改变。{p}势力和功勋的变化和皇帝的性格/属性有关，比如专制的皇帝会尽可能地压低大臣的势力，即便忠臣也难以幸免。"
            text "{color=#000000}6.为什么我是名门望族，家里人却不送毒药了？"
            text "{color=#000000}{size=22}答：只有父亲忠诚<50且能力>50的情况下才会送毒药。"
            text "{color=#000000}7.技能点如何获得？"
            text "{color=#000000}{size=22}答：女主技能点初始固定15岁10点，每大一岁多5点。目前获得技能点的方式包括：每年1月自动获得3点，每次宴会敬酒或者被太后夸赞获得3点，剧情妃提供。"
            text "{color=#000000}8.NPC也有技能吗？"
            text "{color=#000000}{size=22}答：是的，但是她们的初始技能点不是像玩家那样固定的，根据不同的出身、家庭地位、性格、倾向等因素，会有不同的情形。但是后续的获得是和女主一样的，使用效果也和女主一样。"
            text "{color=#000000}9.为什么月姑姑不卖毒药或者其他某某东西了？"
            text "{color=#000000}{size=22}答：一品红再次绝版了，其他毒药需要持有毒害类的初始技能月姑姑才会出售，其他物品则为每次随机进货。为了补偿这一点，月姑姑出现在掖廷的概率提高了。"
            text "{color=#000000}10.皇嗣有的属性不见了，还有能力、势力是什么？势力为什么不长？"
            text "{color=#000000}{size=22}答：好感目前没什么用，所以隐藏了，但仍然存在。勤勉、独立为隐藏属性，能力和势力以后也会隐藏起来，目前版本为了方便调试平衡性所以展示出来了。勤勉和独立比较容易就可以在重华宫老师那里知道。{p}由于是隐藏属性，它们的实际作用和名字并不一定完全吻合，比如“能力”其实是相对于学习成绩、更偏向于务实能力的属性。而势力只是皇子自己的威信，支持者并未被计算在内，只有在开府以后才会增长。"
            text "{color=#000000}11.为什么我不能修改自己孩子的培养方式？"
            text "{color=#000000}{size=22}答：是为了配合“休息玩乐”的变动，在孩子已入学、未婚配之前，只有清晨可以修改。“休息玩乐”下的孩子可以不去上课，随时召见。"
            text "{color=#000000}12.重华宫有什么用？"
            text "{color=#000000}{size=22}答：通过老师的话语可以大概了解到皇嗣的情况。可以亲自教导皇嗣，提升他们属性，还可以将自己的处事之道传授给孩子们，让孩子的倾向和自己靠拢，增进和孩子们的感情。"

            text "{color=#000000}13.为什么我的皇子不去拉拢大臣？为什么有的皇子拉拢了很多大臣，但是被立为太子的是其他皇子？"
            text "{color=#000000}{size=22}答：皇子也有自己的志向，有的皇子无心夺嫡。还有可能能力不足，不能得到支持。例如高忠诚的臣子很少会支持非嫡非长的皇子。{p}大臣也不一定都在朝中有话语权，在夺嫡中占比重最大的是皇上的器重，其次是皇子本身的势力，最后才是大臣和其他皇嗣支持。一般来说太子之位都是属于嫡子/长子的，其他皇子想要成为太子会非常困难。{p}妃嫔目前对于夺嫡的参与度还比较低，以后会继续完善。"
            text "{color=#000000}14.已经立了太子还有可能被废吗？"
            text "{color=#000000}{size=22}答：理论上有可能的，但基本上需要更方面都比原太子要优秀一倍才可以达到。在数值没有经过平衡性测试的情况下，可能实际上并不能做到。{p}以后还会进行更多的调整，可能会结合皇帝的各项属性，出现各种现实中很难实现但并非不可能的事情，比如把皇帝变成昏君然后推自己的废物皇子上位（笑"
            text "{color=#000000}15.为什么皇帝一直不立太子？"
            text "{color=#000000}{size=22}答：因为还没有符合条件的皇子出现。如果当皇帝已经无法生育以后或许会放宽要求，但仍可能直到游戏结束也没有立太子。目前子嗣部分仍不完善，太子其实也没什么大用，以后可能会设置一个硬性时间限制，比如皇帝无法生育以后会强制立太子等。"
            text "{color=#000000}16.孩子为什么生病，会死掉吗？"
            text "{color=#000000}{size=22}答：目前皇嗣只会有体质<0或寿命到头而死亡。生病正常，太医会治，除非你让他带病读书直到体力掉到0，否则不会有事，但是体质越低越容易生病，长期生病会影响学习效率。"
            text "{color=#000000}17.有的妃子死亡以后还被查出来下毒或谣言是BUG吗？会修复吗？"
            text "{color=#000000}{size=22}答：准确来说是文案表现错误，是在其死亡之前被造谣或者被列入下毒嫌疑人的，在死亡后才被调查出来。以后会再完善一下。"
            text "{color=#000000}"
        textbutton "{size=35}关闭" align (0.5,1.0) action Hide("thanks"),Jump("寝居界面")












screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 38
    top_padding 150

    background "gui/overlay/game_menu.webp"

style game_menu_navigation_frame:
    xsize 350
    yfill True

style game_menu_content_frame:
    left_margin 50
    right_margin 25
    top_margin 13

style game_menu_viewport:
    xsize 1150

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 13

style game_menu_label:
    xpos 63
    ysize 150

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -37









screen about():
    tag menu





    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("存档"))


screen load():
    tag menu


    use file_slots(_("读档"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("暂无存档")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}自动") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}快速") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 63
    ypadding 4

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("系统设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("显示模式")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏幕") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("快进模式")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("选项后") action Preference("after choices", "toggle")
                    textbutton _("转场特效") action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    style_prefix "radio"
                    label _("隐藏数值")
                    textbutton _("不显示[[推荐]") action SetVariable("persistent.ycsz", True)
                    textbutton _("显示") action SetVariable("persistent.ycsz", False)
                vbox:
                    style_prefix "radio"
                    label _("晋升速度")
                    textbutton _("较慢") action SetVariable("persistent.expspeed", 0)
                    textbutton _("正常[[默认]") action SetVariable("persistent.expspeed", 1)
                    textbutton _("较快") action SetVariable("persistent.expspeed", 2)
                vbox:
                    style_prefix "radio"
                    label _("自动选择")
                    textbutton _("开启") action SetVariable("persistent.auto_choice_delay", 0.01),SetVariable("config.auto_choice_delay", 0.01)
                    textbutton _("关闭[[默认]") action SetVariable("persistent.auto_choice_delay", None),SetVariable("config.auto_choice_delay", None)





            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字显示速度")

                    bar value Preference("text speed")

                    label _("自动模式等待时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 282

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)
    foreground "gui/button/radio_[prefix_]foreground.webp"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)
    foreground "gui/button/check_[prefix_]foreground.webp"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 438

style slider_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)
    yalign 0.5
    left_margin 13

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 563










screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("暂无历史记录。")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    font "问藏书房.ttf"
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    font "问藏书房.ttf"
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("帮助文档"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 19

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)
    xmargin 10

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 313
    right_padding 25

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 38

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 125

            textbutton _("是") action yes_action
            textbutton _("否") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    outlines [ (absolute(2), "#FFFFFF", absolute(1), absolute(1)) ]
    text_align 0.5
    layout "subtitle"
    font "问藏书房.ttf"
    size 40
    color "#490202"

style confirm_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 8

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "问藏书房.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 5 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yalign 0.3
    xalign 0.5
    padding gui.nvl_borders.padding
    ysize gui.textbox_height
    background Image("gui/nvl.webp", xalign=0.5, yalign=1.0)

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    background Frame("gui/button/idle_background.webp", gui.button_borders, tile=gui.button_tile)
    hover_background Frame("gui/button/hover_background.webp", gui.button_borders, tile=gui.button_tile)
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 563



screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("返回") action Rollback()
        textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("自动") action Preference("auto-forward", "toggle")
        textbutton _("存档") action ShowMenu()
        textbutton _("设置") action ShowMenu('preferences')
    frame:
        background None
        style_prefix "quick"

        xalign 0.0
        yalign 1.0



style window:
    variant "small"
    background "gui/phone/textbox.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

style game_menu_navigation_frame:
    variant "small"
    xsize 425

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 500

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 750






image Snow:


    zoom 1.66

    "images/Maps/Snow/01_00000.webp"
    pause 0.1
    "images/Maps/Snow/01_00001.webp"
    pause 0.1
    "images/Maps/Snow/01_00002.webp"
    pause 0.1
    "images/Maps/Snow/01_00003.webp"
    pause 0.1
    "images/Maps/Snow/01_00004.webp"
    pause 0.1
    "images/Maps/Snow/01_00005.webp"
    pause 0.1
    "images/Maps/Snow/01_00006.webp"
    pause 0.1
    "images/Maps/Snow/01_00007.webp"
    pause 0.1
    "images/Maps/Snow/01_00008.webp"
    pause 0.1
    "images/Maps/Snow/01_00009.webp"
    pause 0.1
    "images/Maps/Snow/01_00010.webp"
    pause 0.1
    "images/Maps/Snow/01_00011.webp"
    pause 0.1
    "images/Maps/Snow/01_00012.webp"
    pause 0.1
    "images/Maps/Snow/01_00013.webp"
    pause 0.1
    "images/Maps/Snow/01_00014.webp"
    pause 0.1
    "images/Maps/Snow/01_00015.webp"
    pause 0.1
    "images/Maps/Snow/01_00016.webp"
    pause 0.1
    "images/Maps/Snow/01_00017.webp"
    pause 0.1
    "images/Maps/Snow/01_00018.webp"
    pause 0.1
    "images/Maps/Snow/01_00019.webp"
    pause 0.1
    "images/Maps/Snow/01_00020.webp"
    pause 0.1
    "images/Maps/Snow/01_00021.webp"
    pause 0.1
    "images/Maps/Snow/01_00022.webp"
    pause 0.1
    "images/Maps/Snow/01_00023.webp"
    pause 0.1
    "images/Maps/Snow/01_00024.webp"
    pause 0.1
    "images/Maps/Snow/01_00025.webp"
    pause 0.1
    "images/Maps/Snow/01_00026.webp"
    pause 0.1
    "images/Maps/Snow/01_00027.webp"
    pause 0.1
    "images/Maps/Snow/01_00028.webp"
    pause 0.1
    "images/Maps/Snow/01_00029.webp"
    pause 0.1
    "images/Maps/Snow/01_00030.webp"
    pause 0.1
    "images/Maps/Snow/01_00031.webp"
    pause 0.1
    "images/Maps/Snow/01_00032.webp"
    pause 0.1
    "images/Maps/Snow/01_00033.webp"
    pause 0.1
    "images/Maps/Snow/01_00034.webp"
    pause 0.1
    "images/Maps/Snow/01_00035.webp"
    pause 0.1
    "images/Maps/Snow/01_00036.webp"
    pause 0.1
    "images/Maps/Snow/01_00037.webp"
    pause 0.1
    "images/Maps/Snow/01_00038.webp"
    pause 0.1
    "images/Maps/Snow/01_00039.webp"
    pause 0.1
    "images/Maps/Snow/01_00040.webp"
    pause 0.1
    "images/Maps/Snow/01_00041.webp"
    pause 0.1
    "images/Maps/Snow/01_00042.webp"
    pause 0.1
    "images/Maps/Snow/01_00043.webp"
    pause 0.1
    "images/Maps/Snow/01_00044.webp"
    pause 0.1

    repeat

image WhiteLight:

    "images/Maps/WhiteLight/(1).webp"
    pause 0.1
    "images/Maps/WhiteLight/(2).webp"
    pause 0.1
    "images/Maps/WhiteLight/(3).webp"
    pause 0.1
    "images/Maps/WhiteLight/(4).webp"
    pause 0.1
    "images/Maps/WhiteLight/(5).webp"
    pause 0.1
    "images/Maps/WhiteLight/(6).webp"
    pause 0.1
    "images/Maps/WhiteLight/(7).webp"
    pause 0.1
    "images/Maps/WhiteLight/(8).webp"
    pause 0.1
    "images/Maps/WhiteLight/(9).webp"
    pause 0.1
    "images/Maps/WhiteLight/(10).webp"
    pause 0.1
    "images/Maps/WhiteLight/(11).webp"
    pause 0.1
    "images/Maps/WhiteLight/(12).webp"
    pause 0.1
    "images/Maps/WhiteLight/(13).webp"
    pause 0.1
    "images/Maps/WhiteLight/(14).webp"
    pause 0.1
    "images/Maps/WhiteLight/(15).webp"
    pause 0.1
    "images/Maps/WhiteLight/(16).webp"
    pause 0.1
    "images/Maps/WhiteLight/(17).webp"
    pause 0.1
    "images/Maps/WhiteLight/(18).webp"
    pause 0.1
    "images/Maps/WhiteLight/(19).webp"
    pause 0.1
    "images/Maps/WhiteLight/(20).webp"
    pause 0.1
    "images/Maps/WhiteLight/(21).webp"
    pause 0.1
    "images/Maps/WhiteLight/(22).webp"
    pause 0.1
    "images/Maps/WhiteLight/(23).webp"
    pause 0.1
    "images/Maps/WhiteLight/(24).webp"
    pause 0.1
    "images/Maps/WhiteLight/(25).webp"
    pause 0.1
    "images/Maps/WhiteLight/(26).webp"
    pause 0.1
    "images/Maps/WhiteLight/(27).webp"
    pause 0.1
    "images/Maps/WhiteLight/(28).webp"
    pause 0.1
    "images/Maps/WhiteLight/(29).webp"
    pause 0.1
    "images/Maps/WhiteLight/(30).webp"
    pause 0.1
    repeat

image Flower:

    zoom 1.66

    "images/Maps/Flower/00000.webp"
    pause 0.1
    "images/Maps/Flower/00001.webp"
    pause 0.1
    "images/Maps/Flower/00002.webp"
    pause 0.1
    "images/Maps/Flower/00003.webp"
    pause 0.1
    "images/Maps/Flower/00004.webp"
    pause 0.1
    "images/Maps/Flower/00005.webp"
    pause 0.1
    "images/Maps/Flower/00006.webp"
    pause 0.1
    "images/Maps/Flower/00007.webp"
    pause 0.1
    "images/Maps/Flower/00008.webp"
    pause 0.1
    "images/Maps/Flower/00009.webp"
    pause 0.1
    "images/Maps/Flower/00010.webp"
    pause 0.1
    "images/Maps/Flower/00011.webp"
    pause 0.1
    "images/Maps/Flower/00012.webp"
    pause 0.1
    "images/Maps/Flower/00013.webp"
    pause 0.1
    "images/Maps/Flower/00014.webp"
    pause 0.1

    repeat





screen calendar:
    style_prefix "calendar"
    $ yunqi = 999

    zorder 99







    frame:
        xalign 1.0
        yalign 0.0
        python:
            if datenum == 1:
                datetext = "上旬"
            elif datenum == 2:
                datetext =  "中旬"
            else :
                datetext = "下旬"
            if timenum == 1:
                timetext = "清晨"
            elif timenum == 2:
                timetext =  "晌午"
            elif timenum == 3:
                timetext = "午后"
            elif timenum == 4:
                timetext = "傍晚"
            else:
                timetext = "深夜"
            for i in my.tags:
                if "身怀皇嗣" in i:
                    yunqi = i[1]
                else:
                    pass


        vbox:
            text "{size=30}[nianhao][year]年[month]月"
            text "{size=30}[datetext] [timetext]"
            text "{size=30}行动点:[AP]"
            if my.shiqin == 0:
                text "{size=20}任务提示：侍寝（0/1）"
            else:
                pass

            if huaiyun(my) == True:
                text "{size=20}任务提示：孕期（[yunqi]/30旬）"
            else:
                if my not in biaoyan and my.state == "寻常" and month == 3:
                    text "{size=20}任务提示：可报名宴会表演。"
                elif month ==9 and my.state == "寻常" and my not in biaoyan:
                    text "{size=20}任务提示：可报名宴会表演。"
                else:
                    pass






style calendar_frame:
    background Frame("gui/日历.webp", borders=(5,5,5,5), tile=None)

    padding gui.notify_frame_borders.padding


init python:


    def chara(d):

        return chara0(d)
transform lihui:
    xalign 0.5
    yalign 0.35

transform chara0:
    xalign 0.5
    yalign 0.35

transform zuo:
    xalign 0.25
    yalign 0.35

transform you:
    xalign 0.75
    yalign 0.35

transform cg:
    xalign 0.5
    yalign 0.45


transform selectmyface:
    xalign 0.2
    yalign 0.5


screen choicefz(list):
    style_prefix "choicemianban"

    $ a = (len(list)-1)/3 + 1
    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        align (0.5,0.2)
        xsize 960
        ysize 540
        text "  " align (0.5,0.02)
        vpgrid:
            align (0.5,0.5)
            xsize 940
            ysize 400

            rows a
            cols 3

            draggable True
            mousewheel True
            xspacing 20
            yspacing 35


            for i in list:
                $ shuxingmiaoshu(i)
                textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action SetVariable("fz",i),Hide("choicefz"),Return()
            if len(list)-1 - 3*a == 1:
                textbutton ""
            elif len(list)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass

screen choicefz_dx(list, choicedlist, num):
    style_prefix "choicemianban"

    $ a = (len(list)-1)/3 + 1
    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        align (0.5,0.2)
        xsize 960
        ysize 540
        text "  " align (0.5,0.02)
        vpgrid:
            align (0.5,0.5)
            xsize 940
            ysize 400

            rows a
            cols 3

            draggable True
            mousewheel True
            xspacing 20
            yspacing 35


            for i in list:
                $ shuxingmiaoshu(i)
                if len(choicedlist) >= num and i not in choicedlist:
                    textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])"
                elif i in choicedlist:
                    textbutton "{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action RemoveFromSet(choicedlist,i)
                else:
                    textbutton "{color=#B22222}{size=25}"+i.hao+i.weifen+" "+i.name+"([i.likelv])" action AddToSet(choicedlist,i)
            if len(list)-1 - 3*a == 1:
                textbutton ""
            elif len(list)-1 - 3*a == 2:
                textbutton ""
                textbutton ""
            else:
                pass
        if len(choicedlist) == 0:
            pass
        else:
            textbutton "确定":
                align (0.5,1.0)
                action Hide("choicefz_dx"),Return()



style choicemianban_button_text:
    font "问藏书房.ttf"
    text_align 0.2
    align (0.0,0.0)
    min_width 280

style choicemianban_button:

    xalign 0.5

    hover_sound "Audio/se_maoudamashii_se_switch02.ogg"
    activate_sound "Audio/se_maoudamashii_se_sound15.ogg"

