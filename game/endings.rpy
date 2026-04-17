define persistent.end_die = False
define persistent.end_killmyself = False
$ persistent.end_naturaldeath = False




label 寿终正寝:
    "这日入睡后，你忽然感觉自己的身体变得轻盈缥缈。"
    "睁开眼睛，竟看到自己躺在榻上。"
    我 "我这是……"
    "一阵眩晕袭来。"
    "仿佛灵魂已经剥离了身体。你意识到，自己已经到了弥留之际。"
    show screen notify("忘川")
    show 冥妃 at chara with dissolve
    "神秘女子" "按照我们的约定，你的灵魂如今归我所有。"
    "神秘女子" "去吧，总有一天，我们还会再见面。"
    hide 冥妃
    "女子微笑不语，你只能看到自己坠入忘川河中，人世的一切在脑海中逐渐浮现，然后，渐行渐远。"
    scene black
    with dissolve
    nvl clear
    pause 2
    $ persistent.end_naturaldeath = True
    $ textlist = ""
    python:
        for i in allstory:
            textlist = textlist + i
    $ scrubs(textlist)
    旁白 "达成结局——寿终正寝。"
    python:
        renpy.set_return_stack("")
    return

label 非正常死亡:
    "一阵剧痛袭来……"
    "仿佛灵魂已经剥离了身体。你意识到，自己已经到了弥留之际。"
    scene 冥府
    with fade

    show screen notify("忘川")
    show 冥妃 at chara with dissolve
    "神秘女子" "当真叫人没有想到，居然会以这样的方式和你再次相见……"
    "神秘女子" "是的，再次……"
    "神秘女子" "让我失望了？（轻笑）不，没有。见惯了你们俗世自扰，倒也还算有趣。"
    "神秘女子" "不过，可惜了这魂魄，却还不能令我餍足。"
    menu:
        "重返阳界":
            "神秘女子" "俗世之人，生死有命。"
            "神秘女子" "倒也是，我本就叫你做了逆天而行之事……人死复生，对我来说并非难事，不过，你总该要付出些代价，让我值得为你做这些？"
            "神秘女子" "去吧，且让我看看你还能蹉跎到几时……"
            $ my.health = my.health*0.5
            $ my.beauty = my.beauty*0.5
            $ my.meili = my.meili*0.5
            $ my.qizhi = my.qizhi*0.5
            $ my.lucky = -10
            $ my.book = 0
            $ my.dance = 0
            $ my.muzic = 0
            $ my.cixiu = 0
            $ my.shou = my.shou - 10
            python:
                renpy.return_statement()
        "遁入轮回":

            "女子微笑不语，你只能看到自己坠入忘川河中，人世的一切在脑海中逐渐浮现，然后，渐行渐远。"
            scene black
            with dissolve
            nvl clear
            pause 2
            旁白 "达成结局——魂断深宫"
            $ textlist = ""
            python:
                for i in allstory:
                    textlist = textlist + i
            $ scrubs(textlist)
            nvl clear
            $ persistent.end_die = True
            pause 2
            python:
                renpy.set_return_stack("")
            return


label 自尽:
    "这日，你支开了宫女……"
    我 "这样的日子，真是毫无指望，受够了……真是受够了……"
    "一阵剧痛袭来……"
    "仿佛灵魂已经剥离了身体。你意识到，自己已经到了弥留之际。"
    scene 冥府
    with fade
    show screen notify("忘川")
    show 冥妃 at chara with dissolve
    "神秘女子" "当真叫人没有想到，居然会以这样的方式和你再次相见……"
    "神秘女子" "是的，再次……"
    "神秘女子" "让我失望了？（轻笑）不，没有。见惯了你们俗世自扰，倒也还算有趣。"
    "神秘女子" "不过，可惜了这魂魄，却还不能令我餍足。"
    "女子微笑不语，你只能看到自己坠入忘川河中，人世的一切在脑海中逐渐浮现，然后，渐行渐远。"
    hide 冥妃
    scene black
    with dissolve
    nvl clear
    pause 2
    $ textlist = ""
    python:
        for i in allstory:
            textlist = textlist + i
    $ scrubs(textlist)
    旁白 "达成结局——暴殒轻生"
    nvl clear
    $ persistent.end_killmyself = True
    pause 2
    python:
        renpy.set_return_stack("")
    return

label 容予HAPPYEND:
    $ fz = my
    scene black with fade
    "身体突然开始向下坠落，然而又似如羽毛般轻盈……"
    "今生所经历的一切开始在脑海中浮现。"
    "一幕一幕——有笑，有泪，有喜，有怨。"
    "最后，停格在和容予相拥的画面。"
    nvl clear
    旁白 "[nianhao][year]年，[my.hao][my.weifen][my.xing][my.ming]于宫中暴毙。"
    nvl clear
    旁白 "从此，世间再无[my.cheng]。"
    旁白 "亦无容予。"
    scene 田园 with fade
    show fz at chara
    "[my.name]" "相公！相公！等等我！"
    hide fz
    show 容予_黑发_笑 at chara with dissolve
    容予 "（笑着停下脚步，揉了揉你的头发）好啦，等你就是了。"
    hide 容予_黑发_笑
    show fz at chara
    "[my.name]" "（挽住他的臂弯后却兀自加快了脚步，拉着他不停朝前走去）你走的太慢了！"
    hide fz
    show 容予_黑发 at chara
    容予 "是，娘子说的是。不过娘子不必如此着急，小心又像上次那样崴了脚要我背。"
    hide 容予_黑发
    show fz at chara
    "[my.name]" "可是我想快些回家嘛……"
    hide fz
    show 容予_黑发_笑 at chara
    容予 "好。"
    容予 "我们回家。"
    hide 容予_黑发_笑
    scene black
    with dissolve
    nvl clear
    pause 2
    $ textlist = ""
    python:
        for i in allstory:
            textlist = textlist + i
    $ scrubs(textlist)
    旁白 "达成结局——容予线·与子偕老"
    nvl clear
    $ persistent.end_rongyuhe = True
    pause 2
    python:
        renpy.set_return_stack("")
    return

label 应福遥结局_失败:
    scene black
    "一晃又是三年过去……"
    "你未能成功完成【绝处逢生】的所有任务……"
    "在奸人设计之下，你再次被打入深渊，但你仍可以继续体验未来的人生。"
    menu:
        "继续游戏":
            $ player = 0
            $ my.exp = weifen_list[beifei][4] - 300
            $ my.love = -20
            return
        "放弃":

            python:
                renpy.set_return_stack("")
            return



label 应福遥结局_成功:
    scene black
    "恭喜你通关了【绝处逢生】！"
    "你现在可以继续体验未来的人生！"
    menu:
        "继续游戏":
            $ player = 0
            return
        "离开":

            python:
                renpy.set_return_stack("")
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
