init python:
    def Skills_Bool(who,which,skill):
        if skill == "初始" :
            if  which["初始"] == 3:
                return "{color=#696969}已达上限"
            elif  which["初始"] == 0 and who.skillcosts < 3:
                return "{color=#696969}点数不足"
            elif  which["初始"] == 1 and who.skillcosts < 3:
                return "{color=#696969}点数不足"
            elif  which["初始"] == 2 and who.skillcosts < 5:
                return "{color=#696969}点数不足"
            else:
                return "升级"
        elif skill == "一A" :
            if  which["一A"] == 3:
                return "{color=#696969}已达上限"
            elif which["初始"] <=  which["一A"] :
                return "{color=#696969}不可升级"
            
            else:
                if  which["一A"] == 0 and who.skillcosts < 1:
                    return "{color=#696969}点数不足"
                elif  which["一A"] == 1 and who.skillcosts < 3:
                    return "{color=#696969}点数不足"
                elif  which["一A"] == 2 and who.skillcosts < 5:
                    return "{color=#696969}点数不足"
                else:
                    return "升级"
        elif skill == "一B" :
            if  which["一B"] == 3:
                return "{color=#696969}已达上限"
            elif which["初始"] <=  which["一B"] :
                return  "{color=#696969}不可升级"
            else:
                if  which["一B"] == 0 and who.skillcosts < 1:
                    return "{color=#696969}点数不足"
                elif  which["一B"] == 1 and who.skillcosts < 3:
                    return "{color=#696969}点数不足"
                elif  which["一B"] == 2 and who.skillcosts < 5:
                    return "{color=#696969}点数不足"
                else:
                    return "升级"
        elif skill == "二A" :
            if  which["二A"] == 3:
                return "{color=#696969}已达上限"
            else:
                if which["一A"]>= which["一B"]:
                    tempnum = which["一A"]
                else:
                    tempnum = which["一B"]
                if tempnum <=  which["二A"] :
                    return  "{color=#696969}不可升级"
                
                else:
                    if  which["二A"] == 0 and who.skillcosts < 3:
                        return "{color=#696969}点数不足"
                    elif  which["二A"] == 1 and who.skillcosts < 3:
                        return "{color=#696969}点数不足"
                    elif  which["二A"] == 2 and who.skillcosts < 5:
                        return "{color=#696969}点数不足"
                    else:
                        return "升级"
        
        elif skill == "二B" :
            if  which["二B"] == 3:
                return "{color=#696969}已达上限"
            else:
                if which["一A"]>= which["一B"]:
                    tempnum = which["一A"]
                else:
                    tempnum = which["一B"]
                if tempnum <=  which["二B"] :
                    return  "{color=#696969}不可升级"
                
                else:
                    if  which["二B"] == 0 and who.skillcosts < 3:
                        return "{color=#696969}点数不足"
                    elif  which["二B"] == 1 and who.skillcosts < 3:
                        return "{color=#696969}点数不足"
                    elif  which["二B"] == 2 and who.skillcosts < 5:
                        return "{color=#696969}点数不足"
                    else:
                        return "升级"
        elif skill == "三级":
            if which["三级"] == 3:
                return "{color=#696969}已达上限"
            else:
                if which["二A"]>= which["二B"]:
                    tempnum = which["二A"]
                else:
                    tempnum = which["二B"]
                if tempnum <=  which["三级"] :
                    return  "{color=#696969}不可升级"
                
                else:
                    if  which["三级"] == 0 and who.skillcosts < 5:
                        return "{color=#696969}点数不足"
                    elif  which["三级"] == 1 and who.skillcosts < 3:
                        return "{color=#696969}点数不足"
                    elif  which["三级"] == 2 and who.skillcosts < 5:
                        return "{color=#696969}点数不足"
                    else:
                        return "升级"
        
        else:
            return "{color=#696969}暂未实装"







    def Skills_Up(who,which,skill):
        if skill == "初始" :
            if  which["初始"] == 0 :
                who.skillcosts -= 3
            elif  which["初始"] == 1 :
                who.skillcosts -= 3
            elif  which["初始"] == 2 :
                who.skillcosts -= 3
            else:
                pass
            which["初始"] += 1
        elif skill == "一A" :
            if  which["一A"] == 0 :
                who.skillcosts -= 1
            elif  which["一A"] == 1:
                who.skillcosts -= 3
            elif  which["一A"] == 2 :
                who.skillcosts -= 5
            else:
                pass
            which["一A"] += 1
        elif skill == "一B" :
            if  which["一B"] == 0 :
                who.skillcosts -= 1
            elif  which["一B"] == 1 :
                who.skillcosts -= 3
            elif  which["一B"] == 2 :
                who.skillcosts -= 5
            else:
                pass
            which["一B"] += 1
        elif skill == "二A" :
            if  which["二A"] == 0:
                who.skillcosts -= 3
            elif  which["二A"] == 1:
                who.skillcosts -= 3
            elif  which["二A"] == 2:
                who.skillcosts -= 5
            else:
                pass
            which["二A"] += 1
        
        elif skill == "二B" :
            if  which["二B"] == 0:
                who.skillcosts -= 3
            elif  which["二B"] == 1:
                who.skillcosts -= 3
            elif  which["二B"] == 2:
                who.skillcosts -= 5
            else:
                pass
            which["二B"] += 1
        elif skill == "三级":
            if  which["三级"] == 0 :
                who.skillcosts -= 5
            elif  which["三级"] == 1:
                who.skillcosts -= 3
            elif  which["三级"] == 2:
                who.skillcosts -= 5
            else:
                pass
            which["三级"] += 1
        
        
        else:
            who.skillcosts -= 10
            which["大招"] += 1



    def Skill_Level(what):
        if what == 0:
            return "{size=25}{color=#2F4F4F}未习得"
        elif what == 1:
            return "{size=25}{color=#008000}初级"
        elif what == 2:
            return "{size=25}{color=#0040FF}中级"
        else:
            return "{size=25}{color=#EE00EE}已掌握"


style myskills_text:
    size 40
    font "问藏书房.ttf"

style myskills_button_text:
    size 30
    font "问藏书房.ttf"

screen myskills_1:
    tag myskills
    modal True
    zorder 1
    style_prefix "myskills"
    fixed align (0.5,0.5):

        add "gui/frame.webp" zoom 1.5 xalign 0.5 yalign 0.5
        side "tr bl":
            spacing 1280
            add "flower.webp"
            add "flower.webp"
    frame:
        background None
        xysize (1280,720)
        align (0.5,0.5)
        hbox align (0.5,0.0) spacing 25:
            text "{font=问藏书房.ttf}可用点数："+ str(my.skillcosts)
            textbutton "{font=问藏书房.ttf}查看说明" action Show("skills_tips")
        hbox align (0.5,1.0) spacing 25:
            textbutton "{font=问藏书房.ttf}{size=40}上一页"
            textbutton "{font=问藏书房.ttf}{size=40}关闭" action Hide("myskills_1")
            textbutton "{font=问藏书房.ttf}{size=40}下一页" action Hide("myskills_1"),Show("myskills_2")



        vbox align (0.1,0.5):
            hbox:
                text "          "
                text "{size=50}话术"
            hbox:
                text "          "
                vbox:
                    text "中宫之主"+ str(Skill_Level(my.huashu["大招"]))
                    if Skills_Bool(my,my.huashu,"大招") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"大招"):
                            action NullAction()
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"大招"):
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]

            hbox:
                text "          "
                vbox:
                    text "戮力同心"+ str(Skill_Level(my.huashu["三级"]))
                    if Skills_Bool(my,my.huashu,"三级") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"三级"):
                            action NullAction()
                            hovered Show("scrtt",tt="在宫斗事件中每一位不在冷宫中的交好嫔妃无条件额外为你提供5/10%/15%的成功率")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"三级"):
                            hovered Show("scrtt",tt="在宫斗事件中每一位不在冷宫中的交好嫔妃无条件额外为你提供5/10%/15%的成功率")
                            unhovered [Hide("scrtt")]

            hbox:
                vbox:
                    text "以理服人"+ str(Skill_Level(my.huashu["二A"]))
                    if Skills_Bool(my,my.huashu,"二A") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"二A"):
                            action NullAction()
                            hovered Show("scrtt",tt="增加争锋中【群起攻之】的伤害10%/15%/25%，并且争锋胜利后可同时获得三种效果，但数值是原本的30%/50%/70%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"二A"):
                            hovered Show("scrtt",tt="增加争锋中【群起攻之】的伤害10%/15%/25%，并且争锋胜利后可同时获得三种效果，但数值是原本的30%/50%/70%")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "有难同当"+ str(Skill_Level(my.huashu["二B"]))
                    if Skills_Bool(my,my.huashu,"二B") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"二B"):
                            action NullAction()
                            hovered Show("scrtt",tt="当你的盟友或金兰被宫斗成功时，可以使用该技能营救该妃子。成功率为心计*10%，若成功，惩罚降低10%/30%/50%，好感增加5/10/15")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"二B"):
                            hovered Show("scrtt",tt="当你的盟友或金兰被宫斗成功时，可以使用该技能营救该妃子。成功率为心计*10%，若成功，惩罚降低10%/30%/50%，好感增加5/10/15")
                            unhovered [Hide("scrtt")]
            hbox:
                vbox:
                    text "以和为贵"+ str(Skill_Level(my.huashu["一A"]))
                    if Skills_Bool(my,my.huashu,"一A") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"一A"):
                            action NullAction()
                            hovered Show("scrtt",tt="可斡旋其他妃子与交恶者的关系，并少量降低她的倾向，但会损失少量好感")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"一A"):
                            hovered Show("scrtt",tt="可斡旋其他妃子与交恶者的关系，并少量降低她的倾向，但会损失少量好感")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "趋炎附势"+ str(Skill_Level(my.huashu["一B"]))
                    if Skills_Bool(my,my.huashu,"一B") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"一B"):
                            action NullAction()
                            hovered Show("scrtt",tt="减少被提升和提升他人位份的技能冷却时间1月/2月/3月")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"一B"):
                            hovered Show("scrtt",tt="减少被提升和提升他人位份的技能冷却时间1月/2月/3月")
                            unhovered [Hide("scrtt")]
            hbox:
                text "          "
                vbox:
                    text "左右逢源"+ str(Skill_Level(my.huashu["初始"]))
                    if Skills_Bool(my,my.huashu,"初始") != "升级":
                        textbutton Skills_Bool(my,my.huashu,"初始"):
                            action NullAction()
                            hovered Show("scrtt",tt="提升太后和其他妃子的好感速度+10%/15%/25%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.huashu,"初始"):
                            hovered Show("scrtt",tt="提升太后和其他妃子的好感速度+10%/15%/25%")
                            unhovered [Hide("scrtt")]

        vbox align (0.9,0.5):
            hbox:
                text "          "
                text "{size=50}媚术"
            hbox:
                text "          "
                vbox:
                    text "专宠艳后"+ str(Skill_Level(my.meishu["大招"]))
                    if Skills_Bool(my,my.meishu,"大招") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"大招"):
                            action NullAction()
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"大招"):
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]

            hbox:
                text "          "
                vbox:
                    if my.jiayun == False:
                        text "假孕"+ str(Skill_Level(my.meishu["三级"]))
                        if Skills_Bool(my,my.meishu,"三级") != "升级":
                            textbutton Skills_Bool(my,my.meishu,"三级"):
                                action NullAction()
                                hovered Show("scrtt",tt="在侍寝后使用，可被太医诊出有孕，需在有孕1月后、8月前使用第二段【假流产】技能。")
                                unhovered [Hide("scrtt")]
                        else:
                            textbutton "升级" action Function(Skills_Up,my,my.meishu,"三级"):
                                hovered Show("scrtt",tt="在侍寝后使用，可被太医诊出有孕，需在有孕1月后、8月前使用第二段【假流产】技能。")
                                unhovered [Hide("scrtt")]
                    else:
                        text "假流产"+ str(Skill_Level(my.meishu["三级"]))
                        if yunqi(my) <= 3:
                            textbutton "不可使用":
                                action NullAction()
                                hovered Show("scrtt",tt="需在“孕期”1月以后、8月之前使用。")
                                unhovered [Hide("scrtt")]
                        else:
                            textbutton "使用":
                                hovered Show("scrtt",tt="指定陷害至多3名妃子，被陷害者初始自带15/30/50的嫌疑度。")
                                unhovered [Hide("scrtt")]
                                action Hide("myskills"),Hide("myshuxing"),Hide("scrtt"),Call("不幸小产_假孕",fz = my)


            hbox:
                vbox:
                    text "落阱下石"+ str(Skill_Level(my.meishu["二A"]))
                    if Skills_Bool(my,my.meishu,"二A") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"二A"):
                            action NullAction()
                            hovered Show("scrtt",tt="皇帝处罚妃子时，可以发动技能增加其处罚25%/50%/75%。成功率为宠爱度*100%。成功后会消耗宠爱度，魅力越高，消耗越少，该妃子好感度下降5/10/15。")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"二A"):
                            hovered Show("scrtt",tt="皇帝处罚妃子时，可以发动技能增加其处罚25%/50%/75%。成功率为宠爱度*100%。成功后会消耗宠爱度，魅力越高，消耗越少，该妃子好感度下降5/10/15。")
                            unhovered [Hide("scrtt")]

                text "    "
                vbox:
                    text "梨花带雨"+ str(Skill_Level(my.meishu["二B"]))
                    if Skills_Bool(my,my.meishu,"二B") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"二B"):
                            action NullAction()
                            hovered Show("scrtt",tt="当你/交好/金兰将被皇帝触发的时候，可以发动技能降低受到的惩罚25%/50%/75%。成功率为宠爱度*100%，成功后会消耗宠爱度，魅力越高，消耗越少，该妃子（自己除外）好感度上升5/10/15")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"二B"):
                            hovered Show("scrtt",tt="当你/交好/金兰将被皇帝触发的时候，可以发动技能降低受到的惩罚25%/50%/75%。成功率为宠爱度*100%，成功后会消耗宠爱度，魅力越高，消耗越少，该妃子（自己除外）好感度上升5/10/15")
                            unhovered [Hide("scrtt")]
            hbox:
                vbox:
                    text "床笫之欢"+ str(Skill_Level(my.meishu["一A"]))
                    if Skills_Bool(my,my.meishu,"一A") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"一A"):
                            action NullAction()
                            hovered Show("scrtt",tt="增加10%/20%/30%大猪蹄子侍寝时的初始兴致。增加在侍寝时50%/75%/100%美言和诉苦其他妃子的效果。每次侍寝都会额外增加0.15/0.25/0.5的魅力，但会降低5体质")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"一A"):
                            hovered Show("scrtt",tt="增加10%/20%/30%大猪蹄子侍寝时的初始兴致。增加在侍寝时50%/75%/100%美言和诉苦其他妃子的效果。每次侍寝都会额外增加0.15/0.25/0.5的魅力，但会降低5体质")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "恃宠生娇"+ str(Skill_Level(my.meishu["一B"]))
                    if Skills_Bool(my,my.meishu,"一B") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"一B"):
                            action NullAction()
                            hovered Show("scrtt",tt="争锋中使用【侍宠生娇】造成的伤害增加50%/75%/100%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"一B"):
                            hovered Show("scrtt",tt="争锋中使用【侍宠生娇】造成的伤害增加50%/75%/100%")
                            unhovered [Hide("scrtt")]
            hbox:
                text "          "
                vbox:
                    text "歌舞精进"+ str(Skill_Level(my.meishu["初始"]))
                    if Skills_Bool(my,my.meishu,"初始") != "升级":
                        textbutton Skills_Bool(my,my.meishu,"初始"):
                            action NullAction()
                            hovered Show("scrtt",tt="曲谱/舞谱的修习速度增加15%/30%/50%，并且每次都会额外增加0.15/0.3/0.5的魅力，但会额外消耗一个行动点")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.meishu,"初始"):
                            hovered Show("scrtt",tt="曲谱/舞谱的修习速度增加15%/30%/50%，并且每次都会额外增加0.15/0.3/0.5的魅力，但会额外消耗一个行动点")
                            unhovered [Hide("scrtt")]

screen myskills_2:
    tag myskills
    modal True
    zorder 1
    style_prefix "myskills"
    fixed align (0.5,0.5):

        add "gui/frame.webp" zoom 1.5 xalign 0.5 yalign 0.5
        side "tr bl":
            spacing 1280
            add "flower.webp"
            add "flower.webp"
    frame:
        background None
        xysize (1280,720)
        align (0.5,0.5)
        hbox align (0.5,0.0) spacing 25:
            text "{font=问藏书房.ttf}可用点数："+ str(my.skillcosts)
            textbutton "{font=问藏书房.ttf}查看说明" action Show("skills_tips")
        hbox align (0.5,1.0) spacing 25:
            textbutton "{font=问藏书房.ttf}{size=40}上一页" action Hide("myskills_2"),Show("myskills_1")
            textbutton "{font=问藏书房.ttf}{size=40}关闭" action Hide("myskills_2")
            textbutton "{font=问藏书房.ttf}{size=40}下一页"




        vbox align (0.1,0.5):
            hbox:
                text "          "
                text "{size=50}自保"
            hbox:
                text "          "
                vbox:
                    text "绝世贤后"+ str(Skill_Level(my.fangyu["大招"]))
                    if Skills_Bool(my,my.fangyu,"大招") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"大招"):
                            action NullAction()
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"大招"):
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]

            hbox:
                text "          "
                vbox:
                    text "不言而信"+ str(Skill_Level(my.fangyu["三级"]))
                    if Skills_Bool(my,my.fangyu,"三级") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"三级"):
                            action NullAction()
                            hovered Show("scrtt",tt="当自己或其他妃子在宫斗事件中将受到惩罚的时候，所有惩罚降低50%/75%/100%，使用后技能等级归0")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"三级"):
                            hovered Show("scrtt",tt="当自己或其他妃子在宫斗事件中将受到惩罚的时候，所有惩罚降低50%/75%/100%，使用后技能等级归0")
                            unhovered [Hide("scrtt")]

            hbox:
                vbox:
                    text "明哲保身"+ str(Skill_Level(my.fangyu["二A"]))
                    if Skills_Bool(my,my.fangyu,"二A") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"二A"):
                            action NullAction()
                            hovered Show("scrtt",tt="被下毒时成功的概率降低15%/30%/50%，且凶手必定会有嫌疑，初始嫌疑度为15/30/50")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"二A"):
                            hovered Show("scrtt",tt="被下毒时成功的概率降低15%/30%/50%，且凶手必定会有嫌疑，初始嫌疑度为15/30/50")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "清者自清"+ str(Skill_Level(my.fangyu["二B"]))
                    if Skills_Bool(my,my.fangyu,"二B") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"二B"):
                            action NullAction()
                            hovered Show("scrtt",tt="被造谣的成功率降低50%/75%/100%，不为真凶时调查进度会减慢15%/30%/50%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"二B"):
                            hovered Show("scrtt",tt="被造谣的成功率降低50%/75%/100%，不为真凶时调查进度会减慢15%/30%/50%")
                            unhovered [Hide("scrtt")]
            hbox:
                vbox:
                    text "淡然处之"+ str(Skill_Level(my.fangyu["一A"]))
                    if Skills_Bool(my,my.fangyu,"一A") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"一A"):
                            action NullAction()
                            hovered Show("scrtt",tt="减少争锋中受到的伤害和增益都会减少至原本的90%/75%/50%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"一A"):
                            hovered Show("scrtt",tt="减少争锋中受到的伤害和增益都会减少至原本的90%/75%/50%")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "以德服人"+ str(Skill_Level(my.fangyu["一B"]))
                    if Skills_Bool(my,my.fangyu,"一B") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"一B"):
                            action NullAction()
                            hovered Show("scrtt",tt="所有宫女每旬野心下降0.3/0.5/1，且更不容易被收买")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"一B"):
                            hovered Show("scrtt",tt="所有宫女每旬野心下降0.3/0.5/1，且更不容易被收买")
                            unhovered [Hide("scrtt")]
            hbox:
                text "          "
                vbox:
                    text "才学精进"+ str(Skill_Level(my.fangyu["初始"]))
                    if Skills_Bool(my,my.fangyu,"初始") != "升级":
                        textbutton Skills_Bool(my,my.fangyu,"初始"):
                            action NullAction()
                            hovered Show("scrtt",tt="增加修习才学（10%/20%/30%），并且每次都会额外增加0.1/0.2/0.3的心计")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.fangyu,"初始"):
                            hovered Show("scrtt",tt="增加修习才学（10%/20%/30%），并且每次都会额外增加0.1/0.2/0.3的心计")
                            unhovered [Hide("scrtt")]

        vbox align (0.9,0.5):
            hbox:
                text "          "
                text "{size=50}毒害"
            hbox:
                text "          "
                vbox:
                    text "蛇蝎毒后"+ str(Skill_Level(my.anhai["大招"]))
                    if Skills_Bool(my,my.anhai,"大招") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"大招"):
                            action NullAction()
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"大招"):
                            hovered Show("scrtt",tt="暂未实装")
                            unhovered [Hide("scrtt")]

            hbox:
                text "          "
                vbox:
                    text "深藏身名"+ str(Skill_Level(my.anhai["三级"]))
                    hbox:
                        if Skills_Bool(my,my.anhai,"三级") != "升级":
                            textbutton Skills_Bool(my,my.anhai,"三级"):
                                action NullAction()
                                hovered Show("scrtt",tt="对其他角色使用慢性毒药，接下来该目标会每个月自动掉损失额外寿命，无人可查，无人可救。（目前可对妃嫔和皇嗣使用，可以叠加）")
                                unhovered [Hide("scrtt")]
                        else:
                            textbutton "升级" action Function(Skills_Up,my,my.anhai,"三级"):
                                hovered Show("scrtt",tt="对其他角色使用慢性毒药，接下来该目标会每个月自动掉损失额外寿命，无人可查，无人可救。（目前可对妃嫔和皇嗣使用，可以叠加）")
                                unhovered [Hide("scrtt")]
                        if my.anhai["三级"] == 0:
                            pass
                        else:
                            textbutton "使用" action Hide("myskills_2"),Hide("myshuxing"),Call("深藏身名")




            hbox:
                vbox:
                    text "亲力亲为"+ str(Skill_Level(my.anhai["二A"]))
                    if Skills_Bool(my,my.anhai,"二A") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"二A"):
                            action NullAction()
                            hovered Show("scrtt",tt="下毒前无需收买宫女，并自带相当于收买了1/2/3名500野心的贴身侍女的成功率，但需要三个行动点")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"二A"):
                            hovered Show("scrtt",tt="下毒前无需收买宫女，并自带相当于收买了1/2/3名500野心的贴身侍女的成功率，但需要三个行动点")
                            unhovered [Hide("scrtt")]

                text "    "
                vbox:
                    text "借刀杀人"+ str(Skill_Level(my.anhai["二B"]))
                    if Skills_Bool(my,my.anhai,"二B") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"二B"):
                            action NullAction()
                            hovered Show("scrtt",tt="每次下毒可指定嫁祸一人，其初始嫌疑为15%/30%/50%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"二B"):
                            hovered Show("scrtt",tt="每次下毒可指定嫁祸一人，其初始嫌疑为15%/30%/50%")
                            unhovered [Hide("scrtt")]
            hbox:
                vbox:
                    text "心狠手辣"+ str(Skill_Level(my.anhai["一A"]))
                    if Skills_Bool(my,my.anhai,"一A") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"一A"):
                            action NullAction()
                            hovered Show("scrtt",tt="下毒和造谣成功率增加8%/16%/30%")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"一A"):
                            hovered Show("scrtt",tt="下毒和造谣成功率增加8%/16%/30%")
                            unhovered [Hide("scrtt")]
                text "    "
                vbox:
                    text "笑里藏刀"+ str(Skill_Level(my.anhai["一B"]))
                    if Skills_Bool(my,my.anhai,"一B") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"一B"):
                            action NullAction()
                            hovered Show("scrtt",tt="邀请/召见其他妃子来寝宫时，可使用“品茶”功能，使对方降低5/7/10点健康，每旬可使用一次")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"一B"):
                            hovered Show("scrtt",tt="邀请/召见其他妃子来寝宫时，可使用“品茶”功能，使对方降低5/7/10点健康，每旬可使用一次")
                            unhovered [Hide("scrtt")]
            hbox:
                text "          "
                vbox:
                    text "寻医问药"+ str(Skill_Level(my.anhai["初始"]))
                    if Skills_Bool(my,my.anhai,"初始") != "升级":
                        textbutton Skills_Bool(my,my.anhai,"初始"):
                            action NullAction()
                            hovered Show("scrtt",tt="月姑姑处可购买妒芳容/红麝粉/鹤顶红，宫女“寻医问药”概率增加")
                            unhovered [Hide("scrtt")]
                    else:
                        textbutton "升级" action Function(Skills_Up,my,my.anhai,"初始"):
                            hovered Show("scrtt",tt="月姑姑处可购买妒芳容/红麝粉/鹤顶红，宫女“寻医问药”概率增加")
                            unhovered [Hide("scrtt")]


screen skills_tips:
    style_prefix "myskills"
    zorder 5
    modal True
    frame:
        xysize (1280,720)
        align (0.5,0.5)
        has vbox align (0.0,0.5)
        text "{font=问藏书房.ttf}{size=30}每个技能树下有1个初始技能，2个一级技能，2个二级技能，1个三级技能，1个最终技能，除终极技能以外所有技能均有三个等级。终极技能目前版本还没有实装，也就是无法升级和使用。{p}习得一个初始技能需要3个技能点，一级技能1点，二级技能3点，三级技能5点，终极技能待定。每个技能增进分别需要3、5个技能点。{p}{p}目前的技能点获得方式：{p}游戏开始时，玩家拥有一定的技能点，14岁为10点，每大一岁多5个技能点。{p}每到1年的1月，每个妃子获得3个技能点{p}每次宴会被太后夸奖/向皇上敬酒获得3个技能点。{p}剧情妃和特殊剧情可提供一定的技能点。{p}以后会增加更多获取方式。{p}"
        textbutton "我知道了" action Hide("skills_tips") align (0.5,0.5)

style fzskills_text:
    size 35
    align (0.5,0.5)
    min_width 150



screen fzskills(fz):

    modal True
    zorder 1
    style_prefix "fzskills"
    fixed align (0.5,0.5):

        add "gui/frame.webp" zoom 1.34 xalign 0.5 yalign 0.5

    frame:
        background None
        xysize (1280,720)
        align (0.5,0.5)
        text "{font=问藏书房.ttf}剩余点数：:"+ str(fz.skillcosts) align (0.5,0.0)
        hbox align (0.5,1.0) spacing 25:

            textbutton "{font=问藏书房.ttf}{size=40}关闭" action Hide("fzskills")


        hbox align (0.5,0.5) spacing 40:
            vbox spacing 20:
                text "话术："
                text "左右逢源:"+ str(Skill_Level(fz.huashu["初始"]))
                text "以和为贵:"+ str(Skill_Level(fz.huashu["一A"]))
                text "趋炎附势:"+ str(Skill_Level(fz.huashu["一B"]))
                text "以理服人:"+ str(Skill_Level(fz.huashu["二A"]))
                text "有难同当:"+ str(Skill_Level(fz.huashu["二B"]))
                text "戮力同心:"+ str(Skill_Level(fz.huashu["三级"]))
                text "中宫之主:"+ str(Skill_Level(fz.huashu["大招"]))
            vbox spacing 20:
                text "媚术："
                text "歌舞精进:"+ str(Skill_Level(fz.meishu["初始"]))
                text "床笫之欢:"+ str(Skill_Level(fz.meishu["一A"]))
                text "恃宠生娇:"+ str(Skill_Level(fz.meishu["一B"]))
                text "落井下石:"+ str(Skill_Level(fz.meishu["二A"]))
                text "梨花带雨:"+ str(Skill_Level(fz.meishu["二B"]))
                text "假孕小产:"+ str(Skill_Level(fz.meishu["三级"]))
                text "专宠艳后:"+ str(Skill_Level(fz.meishu["大招"]))
            vbox spacing 20:
                text "自保："
                text "才学精进:"+ str(Skill_Level(fz.fangyu["初始"]))
                text "淡然处之:"+ str(Skill_Level(fz.fangyu["一A"]))
                text "以德服人:"+ str(Skill_Level(fz.fangyu["一B"]))
                text "明哲保身:"+ str(Skill_Level(fz.fangyu["二A"]))
                text "清者自清:"+ str(Skill_Level(fz.fangyu["二B"]))
                text "不言而信:"+ str(Skill_Level(fz.fangyu["三级"]))
                text "绝世贤后:"+ str(Skill_Level(fz.fangyu["大招"]))
            vbox spacing 20:
                text "暗害："
                text "寻医问药:"+ str(Skill_Level(fz.anhai["初始"]))
                text "心狠手辣:"+ str(Skill_Level(fz.anhai["一A"]))
                text "笑里藏刀:"+ str(Skill_Level(fz.anhai["一B"]))
                text "亲力亲为:"+ str(Skill_Level(fz.anhai["二A"]))
                text "借刀杀人:"+ str(Skill_Level(fz.anhai["二B"]))
                text "深藏身名:"+ str(Skill_Level(fz.anhai["三级"]))
                text "蛇蝎毒后:"+ str(Skill_Level(fz.anhai["大招"]))

init python:

    def NPC_Skill_Fenpei(self):
        if self.skillcosts == 0:
            pass
        else:
            huashu = self.huashu["初始"]+self.huashu["一A"]+self.huashu["一B"]+self.huashu["二A"]+self.huashu["二B"]+self.huashu["三级"]
            meishu = self.meishu["初始"]+self.meishu["一A"]+self.meishu["一B"]+self.meishu["二A"]+self.meishu["二B"]+self.meishu["三级"]
            fangyu = self.fangyu["初始"]+self.fangyu["一A"]+self.fangyu["一B"]+self.fangyu["二A"]+self.fangyu["二B"]+self.fangyu["三级"]
            anhai = self.anhai["初始"]+self.anhai["一A"]+self.anhai["一B"]+self.anhai["二A"]+self.anhai["二B"]+self.anhai["三级"]
            templist = [huashu,meishu,fangyu,anhai]
            templist = sorted(templist, reverse = True)
            skilllist = []
            for i in templist:
                if i == huashu:
                    skilllist.append(self.huashu)
                if i == meishu:
                    skilllist.append(self.meishu)
                if i == anhai:
                    skilllist.append(self.anhai)
                if i == fangyu:
                    skilllist.append(self.fangyu)
            
            for i in skilllist:
                if Skills_Bool(self,i,"三级") == "升级":
                    Skills_Up(self,i,"三级")
                if Skills_Bool(self,i,"二A") == "升级":
                    lucky = renpy.random.randint(0,3)
                    if lucky == 0:
                        Skills_Up(self,i,"二A")
                if Skills_Bool(self,i,"二B") == "升级":
                    lucky = renpy.random.randint(0,2)
                    if lucky == 0:
                        Skills_Up(self,i,"二B")
                if Skills_Bool(self,i,"一A") == "升级":
                    lucky = renpy.random.randint(0,5)
                    if lucky == 0:
                        Skills_Up(self,i,"一A")
                if Skills_Bool(self,i,"一B") == "升级":
                    lucky = renpy.random.randint(0,5)
                    if lucky == 0:
                        Skills_Up(self,i,"一B")
                if Skills_Bool(self,i,"初始") == "升级":
                    lucky = renpy.random.randint(0,10)
                    if lucky == 0:
                        Skills_Up(self,i,"初始")





    def Taihoulike_Up(who,num):
        if who.huashu["初始"]== 0:
            who.taihoulike += num
        elif who.huashu["初始"]== 1:
            who.taihoulike += num*1.1
        elif who.huashu["初始"]== 2:
            who.taihoulike += num*1.15
        else:
            who.taihoulike += num*1.25
        if who.taihoulike >= 100:
            who.taihoulike = 100
    def Feizilike_Up(who,num):
        if who.like < -20:
            num = num*0.1
        elif who.like < 0:
            num = num*0.5
        else:
            pass
        if my.huashu["初始"]== 0:
            who.like += num
        elif my.huashu["初始"]== 1:
            who.like += num*1.1
        elif my.huashu["初始"]== 2:
            who.like += num*1.15
        else:
            who.like += num*1.25
        if who.like >= 100:
            who.like = 100

    def YouNan(who):
        YNTD = 0
        for i in who.friends:
            if i.huashu["二B"] == 0 or i == my or jinzu(i) == True or i.level == beifei:
                pass
            else:
                lucky =  renpy.random.randint(0,100)
                tempnum = i.xinji*0.1
                if lucky <= tempnum:
                    YNTD += 10 + (i.huashu["二B"]-1)*20
                    temptext = i.cheng + "发动【话术技能——有难同当】为"+who.cheng+"求情成功。"
                    renpy.say(None, temptext)
                else:
                    pass
        return YNTD



    def LuoJing(who):
        LJXS = 0
        for i in who.foes:
            if i.meishu["二A"] == 0 or i == my or jinzu(i) == True or i.level == beifei:
                pass
            else:
                lucky =  renpy.random.randint(0,100)
                tempnum = i.love
                if lucky <= tempnum:
                    LJXS += i.meishu["二A"]*25
                    temptext = i.cheng + "发动【媚术技能——落井下石】成功。"
                    i.love -= (1000-i.meili)*0.05
                    renpy.say(None, temptext)
                else:
                    pass
        return YNTD


    def LiHua(who):
        LHDY = 0
        if who.meishu["二B"] == 0 or who == my or jinzu(who) == True or who.level == beifei:
            pass
        else:
            lucky =  renpy.random.randint(0,100)
            tempnum = who.love
            if lucky <= tempnum:
                LHDY += who.meishu["二B"]*25
                who.love -= (1000-who.meili)*0.05
                temptext = who.cheng + "发动【媚术技能——梨花带雨】为自己求情成功。"
                renpy.say(None, temptext)
            else:
                pass
        for i in who.friends:
            if i.meishu["二B"] == 0 or i == my or jinzu(i) == True or i.level == beifei:
                pass
            else:
                lucky =  renpy.random.randint(0,100)
                tempnum = i.love
                if lucky <= tempnum:
                    LHDY += 10 + (i.meishu["二B"]-1)*20
                    i.love -= (1000-i.meili)*0.05
                    temptext = i.cheng + "发动【媚术技能——梨花带雨】为"+who.cheng+"求情成功。"
                    renpy.say(None, temptext)
                else:
                    pass
        return LHDY


    def DanRan(who,num):
        if who.fangyu["一A"] == 1:
            num = 0.9*num
        elif who.fangyu["一A"] == 2:
            num = 0.75*num
        elif who.fangyu["一A"] == 3:
            num = 0.5*num
        else:
            num = num
        return int(num)


    def JieDao(self):
        if len(self.zhu.foes) == 0 or self.zhu.anhai["二B"] == 0 or self.zhu == my :
            pass
        else:
            templist = []
            for i in self.zhu.foes:
                if i not in NPC_fz_list:
                    pass
                elif i == self.bei:
                    pass
                elif jinzu(i)== True or havetag("失心成疯",i) == True:
                    pass
                else:
                    templist.append(i)
            if len(templist) == 0:
                pass
            else:
                fz = renpy.random.choice(templist)
                if self.zhu.anhai["二B"] == 1:
                    tempnum = 15
                elif self.zhu.anhai["二B"] == 2:
                    tempnum = 30
                else:
                    tempnum = 50
                self.xianyi.append([fz,tempnum])



label 深藏身名:

    $ tempnum = my.anhai["三级"]
    menu:
        "要对谁使用技能？"
        "后妃":




            $ templist = NPC_fz_list + NPC_fz_feilist
            if len(templist) == 0:
                "暂无可使用对象。"
                jump 寝居界面
            else:
                call screen choicefz(templist)
                $ manxingdu.append([fz,tempnum])
                "[fz.cheng]每回合将会扣除额外的寿命……"
        "皇嗣":


            $ templist = []
            python:
                for i in NPC_Kids_list:
                    if i.live != -1:
                        templist.append(i)
            if len(templist) == 0:
                "暂无可使用对象。"
                jump 寝居界面
            else:
                call screen choicekid(templist)
                $ manxingdu.append([kid,tempnum])
                "[kid.cheng]每回合将会扣除额外的寿命……"
        "算了":

            jump 寝居界面
    $ my.anhai["三级"] = 0
    jump 寝居界面
 
