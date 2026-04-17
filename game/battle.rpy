screen battle(fz):
    $ dfsy = len(fzpais)
    frame:
        background None
        add "gui/frame.webp" zoom 1.5 align (0.5,0.5)
        viewport:
            draggable True
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            xsize 1200
            ysize 450
            align (0.5,0.5)
            has vbox
            for i in battle_list:
                if i in battle_list_fz:
                    fixed maximum (1200,100):
                        hbox xalign 0.0:
                            add im.FactorScale("Feizi/F"+str(fz.face)+".webp", 0.25)
                            text "[i]"
                elif i in  battle_list_my:
                    fixed maximum (1200,100):
                        hbox xalign 1.0:
                            text "[i]"
                            add im.FactorScale("Feizi/F"+str(my.face)+".webp", 0.25)

            if waitfz == True and len(mypais) == 0 and len(fzpais) !=0:
                timer 1.5 action Function(fzchupai,fz= fz,_update_screens=True):
                    repeat True
            elif waitfz == True and len(mypais) != 0 and len(fzpais) !=0:
                timer 1.5 action Function(fzchupai,fz= fz,_update_screens=True)
            else:
                pass




        hbox align (0.5,0.9) spacing 30:
            for i in mypais:
                if waitfz == False or len(fzpais) == 0:
                    vbox:
                        textbutton "{font=问藏书房.ttf}"+ paikunames[i] action Hide("scrtt"),Function(wochupai,what=i,fz= fz,_update_screens=True):
                            hovered Show("scrtt",tt=paikujieshi[i])
                            unhovered [Hide("scrtt")]
                        textbutton "{size=25}  放弃" action Function(woqipai,what=i,fz= fz,_update_screens=True)
                else:
                    vbox:
                        textbutton "{font=问藏书房.ttf}"+ paikunames[i] action Hide("scrtt"):
                            hovered Show("scrtt",tt=paikujieshi[i])
                            unhovered [Hide("scrtt")]
                        textbutton "{size=25}  放弃"
        hbox align (0.5,0.8):
            if waitfz == True and len(fzpais) > 0 or len(mypais) == 0 and len(fzpais)>0:
                textbutton "{font=问藏书房.ttf}等待对方回击……" action Function(fzchupai,fz= fz,_update_screens=True)
            elif len(fzpais) == 0 and len(mypais) == 0:
                textbutton "{font=问藏书房.ttf}结束争锋……" action Return()
            else:
                text "发起攻势……"
    hbox align (0.5,0.1):
        text "我方：剩余[myscore]   对方：剩余[fzscore]（剩余伎俩：[dfsy]）"
    hbox align (0.8,0.15):
        textbutton ("【玩法说明】") action Show("battletips")

screen battletips():
    frame xsize 960 ysize 540 xalign 0.5 yalign 0.5:
        background None

        key "mousedown_1" action Hide("battletips")
        add "gui/frame.webp" xalign 0.5 yalign 0.5
        text "点击任意处关闭" align (0.5,0.0)
        vbox align (0.5,0.5):
            text "{size=20}初始招数：中宫6，高位（主位）5，中位4，低位3。部分特质会增加或减少初始招数数量。\n"
            text "{size=20}暴击：会提示“会心一击”\n暴击几率：与福缘有关。\n暴击效果：和家世、位份有关，越低暴击效果越高\n"
            text "{size=20}目前已有招数有：\n恃宠生娇（比宠爱）、金枝玉叶（比家世）、破口大骂（比体质）、浓妆艳抹（比容貌）、花枝招展（比气质）、搔首弄姿（比魅力）、冷嘲热讽（比心机）——获胜方可额外获得一个新招数。\n"
            text "{size=20}蓄势待发（我方分数增加15%）、一针见血（对方分数减少15%）、沉默不语（双方分数增加30%）、鱼死网破（双方分数减少30%）——获胜后没有额外收益。\n" align (0.5,0.5)
            text "{size=20}双方招数都用完以后，分数更高的一方胜利。但如果双方剩下分数都高于100或低于0或是相等，则无法分出胜负。"
            text "{size=20}争锋结束会有三种结果（我方赢了可自由选择其中之一，如果输了则会是随机一种可能），分别是心计胜方增加/败方降低、威望胜方增加/败方降低、倾向胜方增加/败方降低。\n我方输了，对方好感不变。\n我方赢了，若选择降低对方倾向（斗志），好感不变，其他两个选项会导致下降。\n"


init python:
    paikucodes = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    paikunames = ["恃宠生娇","金枝玉叶","破口大骂","浓妆艳抹","花枝招展","搔首弄姿","冷嘲热讽","蓄势待发","一针见血","沉默不语","鱼死网破","群起攻之","居高临下"]
    paikujieshi = ["恃宠生娇：炫耀自己蒙受圣宠，以此打击对方","金枝玉叶：炫耀自己出身高贵，贬低对方","破口大骂：用粗鄙有效的话语激怒对方","浓妆艳抹：展示自己的美貌，以使对方产生自卑","花枝招展：展示自己出众的气质，让对方感到自愧不如","搔首弄姿：展示自己迷人的魅力，让对方萌生退意","冷嘲热讽：用隐晦的言辞对其进行羞辱","蓄势待发：以退为进，准备下一次进攻","一针见血：针对对方的痛处进行攻击","沉默不语：不回应对方的攻击",
    "鱼死网破：不惜自损以达到伤害对方的目的","群起攻之:利用自身的人脉（交好人数）打压对方","居高临下：后宫尊卑严谨，用等级差距打压对方"]
    def fapai(self):
        a = len(yuanweifen)
        if self.level == 0: 
            paishu = 6
        elif self.qinjunum == 1: 
            paishu = 5
        elif self.level > round(a-a/3):
            paishu = 3
        else:
            paishu = 4
        if havetag("能言善辩",self) == True :
            paishu = paishu + 1
        if havetag("不善言辞",self) == True :
            paishu = paishu - 1
        pais = []
        while len(pais) < paishu:
            suijipai = renpy.random.choice(paikucodes)
            pais.append(suijipai)
        
        return pais

    def wochupai(what,fz):
        global battle_list
        global battle_list_my
        global waitfz
        mypais.remove(what)
        temptext = "{color=FF0000}我使用了" + paikunames[what]+ "{/color}"
        battle_list.insert(0,temptext)
        battle_list_my.append(temptext)
        mychupaixiaoguo(what = what,my=my,fz=fz)
        waitfz = True
    def woqipai(what,fz):
        global battle_list
        global battle_list_my
        global waitfz
        mypais.remove(what)
        temptext = "{color=FF0000}我方失去招数——“" + paikunames[what]+ "”{/color}"
        battle_list.insert(0,temptext)
        battle_list_my.append(temptext)
        waitfz = True



    def fzchupai(fz):
        global waitfz
        global battle_list
        global battle_list_fz
        
        if len(fzpais) == 0:
            temptext = fz.hao + fz.weifen + fz.name +"已经无计可施。"
            battle_list.insert(0,temptext)
            battle_list_fz.append(temptext)
        else:
            beichupai = renpy.random.choice(fzpais)
            temptext = fz.hao + fz.weifen + fz.name +"使用了" + paikunames[beichupai]
            battle_list.insert(0,temptext)
            battle_list_fz.append(temptext)
            fzchupaixiaoguo(what = beichupai,my=my,fz=fz)
            fzpais.remove(beichupai)
        if len(mypais) == 0:
            waitfz = True
        else:
            waitfz = False



    def mychupaixiaoguo(what,my,fz):
        global fzscore
        global myscore
        global tempnum
        if what == 0:
            tempnum = (my.love - fz.love)*0.25
            if tempnum < 0:
                tempnum = -tempnum
                tempnum = DanRan(fz,tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                if my.meishu["一B"] != 0:
                    tempnum += tempnum*0.25*(my.meishu["一B"]+1)
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 1:
            tempnum = (my.familylevel - fz.familylevel)*5
            if tempnum > 0:
                tempnum = DanRan(fz,tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = int(tempnum*mybaoji)
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore + tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore + tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 2:
            my.qizhi = my.qizhi -2
            tempnum = (my.health - fz.health)*0.05
            if tempnum < 0:
                temptext = "{color=#000000}并未起效……自身气质-2{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = int(tempnum*mybaoji)
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"，自身气质-2{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"，自身气质-2{/color}"
        elif what == 3:
            tempnum = (my.beauty - fz.beauty)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 4:
            tempnum = (my.qizhi - fz.qizhi)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 5:
            tempnum = (my.meili - fz.meili)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 6:
            tempnum = (my.xinji - fz.xinji)*0.05
            if tempnum < 0:
                my.meili = my.meili -2
                temptext = "{color=#000000}并未起效……自身魅力-2{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                my.meili = my.meili -2
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = int(tempnum*mybaoji)
                    tempnum = DanRan(my,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"，自身魅力-2{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"，自身魅力-2{/color}"
        elif what == 7:
            tempnum = int(myscore*0.15)
            myscore = myscore + tempnum
            temptext = "{b}自身状态恢复"+str(tempnum)+"{/b}"
        elif what == 8:
            tempnum = int(fzscore*0.15)
            fzscore = fzscore - tempnum
            temptext = "{b}敌方状态减少"+str(tempnum)+"{/b}"
        elif what == 9:
            tempnum = int(myscore*0.3)
            myscore = myscore + tempnum
            tempnum2 = int(fzscore*0.3)
            fzscore = fzscore + tempnum2
            temptext = "{b}自身状态恢复"+str(tempnum)+",对方状态恢复"+str(tempnum2)+"{/b}"
        elif what == 10:
            tempnum = int(myscore*0.3)
            myscore = myscore - tempnum
            tempnum2 = int(fzscore*0.3)
            fzscore = fzscore - tempnum2
            temptext = "{b}自身状态减少"+str(tempnum)+"对方状态减少"+str(tempnum2)+"{/b}"
        elif what == 11:
            tempnum = len(my.friends) - len(fz.friends)
            if tempnum >= 5:
                tempnum = 25
            else:
                tempnum = tempnum * 5
            if my.huashu["二A"]  == 0 :
                pass
            else:
                tempnum *= (110+5*(my.huashu["二A"]-1))*0.01
            if tempnum < 0:
                tempnum = int(-tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        elif what == 12:
            tempnum = (fz.level - my.level)*2
            if tempnum < 0:
                tempnum = int(-tempnum)
                fzscore = fzscore + tempnum
                temptext = "{color=#000000}取得了反效果……对方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                mypais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < mybaolv:
                    tempnum = tempnum*mybaoji
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}{b}会心一击！对方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(fz,tempnum)
                    fzscore = fzscore - tempnum
                    temptext = "{color=#FF3030}对方-"+str(tempnum)+"{/color}"
        else:
            temptext = ""
        battle_list_my.append(battle_list[0]  + "\n" + temptext)
        battle_list[0] = battle_list[0]  + "\n" + temptext

    def fzchupaixiaoguo(what,my,fz):
        global myscore
        global fzscore
        global tempnum
        if what == 0:
            tempnum = (fz.love - my.love)*0.25
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                if fz.meishu["一B"] != 0:
                    tempnum += tempnum*0.25*(fz.meishu["一B"]+1)
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        elif what == 1:
            tempnum = (fz.familylevel - my.familylevel)*5
            if tempnum > 0:
                tempnum = DanRan(my,tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore + tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore + tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        elif what == 2:
            fz.qizhi = fz.qizhi -2
            tempnum = (fz.health - my.health)*0.05
            if tempnum < 0:
                temptext = "{color=#FF3030}并未起效……对方气质-2{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"，对方气质-2{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"，对方气质-2{/color}"
        elif what == 3:
            tempnum = (fz.beauty - my.beauty)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        elif what == 4:
            tempnum = (fz.qizhi - my.qizhi)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        elif what == 5:
            tempnum = (fz.meili - my.meili)*0.05
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        elif what == 6:
            tempnum = (fz.xinji - my.xinji)*0.05
            if tempnum < 0:
                fz.meili = fz.meili -2
                temptext = "{color=#FF3030}并未起效……对方魅力-2{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                fz.meili = fz.meili -2
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"，对方魅力-2{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"，对方魅力-2{/color}"
        elif what == 7:
            tempnum = int(fzscore*0.15)
            fzscore = fzscore + tempnum
            temptext = "{b}敌方状态恢复"+str(tempnum)+"{/b}"
        elif what == 8:
            tempnum = int(myscore*0.15)
            myscore = myscore - tempnum
            temptext = "{b}我方状态减少"+str(tempnum)+"{/b}"
        elif what == 9:
            tempnum = int(fzscore*0.3)
            fzscore = fzscore + tempnum
            tempnum2 = int(myscore*0.3)
            myscore = myscore + tempnum2
            temptext = "{b}敌方状态恢复"+str(tempnum)+",我方状态恢复"+str(tempnum2)+"{/b}"
        elif what == 10:
            tempnum = int(fzscore*0.3)
            fzscore = fzscore - tempnum
            tempnum2 = int(myscore*0.3)
            myscore = myscore - tempnum2
            temptext = "{b}敌方状态减少"+str(tempnum)+"我方状态减少"+str(tempnum2)+"{/b}"
        elif what == 11:
            tempnum = len(fz.friends) - len(my.friends)
            if tempnum >= 5:
                tempnum = 25
            else:
                tempnum = tempnum * 5
            if fz.huashu["二A"]  == 0 :
                pass
            else:
                tempnum *= (110+5*(fz.huashu["二A"]-1))*0.01
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        
        elif what == 12:
            tempnum = (my.level - fz.level)*3
            if tempnum < 0:
                tempnum = int(-tempnum)
                myscore = myscore + tempnum
                temptext = "{color=#FF3030}取得了反效果……我方+"+str(tempnum)+ "{/color}"
            else:
                suijipai = renpy.random.choice(paikucodes)
                fzpais.append(suijipai)
                lucky = renpy.random.randint(0,100)
                if lucky < fzbaolv:
                    tempnum = tempnum*fzbaoji
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}{b}会心一击！我方-"+str(tempnum)+"{/b}{/color}"
                else:
                    tempnum = DanRan(my,tempnum)
                    myscore = myscore - tempnum
                    temptext = "{color=#000000}我方-"+str(tempnum)+"{/color}"
        else:
            temptext = ""
        battle_list_fz.append(battle_list[0]  + "\n" + temptext)
        battle_list[0] = battle_list[0]  + "\n" + temptext





    def randombattle(zhu,bei):
        global tempstory2
        global allstory
        a = len(yuanweifen)
        if zhu.level == 0: 
            b = 6
        elif zhu.qinjunum == 1: 
            b = 5
        elif zhu.level > round(a-a/3):
            b = 3
        else:
            b = 4
        if bei.level == 0: 
            c = 6
        elif bei.qinjunum == 1: 
            c = 5
        elif bei.level > round(a-a/3):
            c = 3
        else:
            c = 4
        lucky = renpy.random.randint(0, 6)
        if bei.qingxiang <30:
            lucky -= 3
        else:
            pass
        if zhu.qingxiang > 70:
            lucky += 3
        else:
            pass
        if bei.qingxiang > 70:
            lucky += 3
        else:
            pass
        if bei == my or zhu == my:
            lucky = 1
        else:
            pass
        if lucky == 0:
            zhu.yali -= 10
            tempstory2 ="【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"意欲向"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"发起争锋，不战而胜。\n"
            allstory.insert(0,tempstory2)
            bei.qingxiang = bei.qingxiang + 1
            score = b*10-c*10
            tempnum = abs(score*(0.5-0.1*(b-c)))
            tempnum = tempnum*2
            if tempnum >= 20:
                tempnum = 20
            else:
                pass
            zhu.exp += tempnum
        else:
            bei.qingxiang += renpy.random.randint(0, 1)
            zhu.qingxiang += renpy.random.randint(0, 1)
            score = b*10-c*10
            if havetag("能言善辩",zhu) == True :
                score += 20
            if havetag("不善言辞",zhu) == True :
                score -= 20
            if havetag("能言善辩",bei) == True :
                score -= 20
            if havetag("不善言辞",bei) == True :
                score += 20
            score += (zhu.xinji-bei.xinji)*0.1
            score += (zhu.love-bei.love)*0.1
            if zhu.love-bei.love > 0 and zhu.meishu["一B"] != 0:
                score += (zhu.love-bei.love)*0.1*zhu.meishu["一B"]
            if zhu.love-bei.love < 0 and bei.meishu["一B"] != 0:
                score += (bei.love-zhu.love)*0.1*bei.meishu["一B"]
            score -= (zhu.familylevel - bei.familylevel)*2
            score += (zhu.beauty +zhu.qizhi +zhu.meili - bei.beauty -bei.qizhi -bei.meili)*0.1
            if score<= -10: 
                zhu.yali += 5
                bei.yali -= 5
                tempnum = abs(score*(0.5-0.1*(b-c)))
                if tempnum >= 20:
                    tempnum = 20
                else:
                    pass
                if bei.huashu["二A"] != 0:
                    tempnum = score*(0.5-0.1*(b-c))*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                    zhu.xinji = zhu.xinji - tempnum
                    bei.xinji = bei.xinji + tempnum
                    tempnum =score*(0.5-0.1*(b-c))*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                    battle_expchange(bei,zhu,tempnum)
                    tempnum = score*0.1*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                    zhu.qingxiang = zhu.qingxiang - tempnum
                    bei.qingxiang = bei.qingxiang + tempnum
                else:
                    battle_expchange(bei,zhu,tempnum)
                tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，狼狈落败。"
            elif score >= 10:
                zhu.yali -= 5
                bei.yali += 5
                tempnum = abs(score*(0.5-0.1*(b-c)))
                if tempnum >= 20:
                    tempnum = 20
                else:
                    pass
                if zhu.huashu["二A"] != 0:
                    tempnum = score*(0.5-0.1*(b-c))*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                    bei.xinji = bei.xinji - tempnum
                    zhu.xinji = zhu.xinji + tempnum
                    tempnum =score*(0.5-0.1*(b-c))*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                    battle_expchange(zhu,bei,tempnum)
                    tempnum = score*0.1*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                    bei.qingxiang = bei.qingxiang - tempnum
                    zhu.qingxiang = zhu.qingxiang + tempnum
                
                else:
                    battle_expchange(zhu,bei,tempnum)
                tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，大获全胜。"
            else:
                tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，但并未分出胜负。"
            lucky = 0
            if zhu.qingxiang > 70:
                lucky += renpy.random.randint(3, 5)
            elif zhu.qingxiang > 50:
                lucky += renpy.random.randint(2, 4)
            else:
                lucky += renpy.random.randint(0, 2)
            if bei.qingxiang > 70:
                lucky += renpy.random.randint(3, 5)
            elif bei.qingxiang > 50:
                lucky += renpy.random.randint(2, 4)
            else:
                lucky += renpy.random.randint(0, 2)
            if lucky > 6:
                if zhu in bei.friends or bei in zhu.friends:
                    if zhu in bei.friends:
                        bei.friends.remove(zhu)
                    if bei in zhu.friends:
                        zhu.friends.remove(bei)
                    tempstory2 += "二人心生芥蒂，分道扬镳。\n"
                    allstory.insert(0,tempstory2)
                else:
                    bei.foes.append(zhu)
                    zhu.foes.append(bei)
                    tempstory2 += "二人大动干戈，势不两立。\n"
                    allstory.insert(0,tempstory2)
            else:
                tempstory2 += "\n"
                allstory.insert(0,tempstory2)


    def zidongbattle(zhu,bei):
        global tempstory2
        global allstory
        a = len(yuanweifen)
        if zhu.level == 0:
            b = 6
        elif zhu.qinjunum == 1: 
            b = 5
        elif zhu.level > a-a*0.6:
            b = 3
        else:
            b = 4
        if bei.level == 0: 
            c = 6
        elif bei.qinjunum == 1: 
            c = 5
        elif bei.level > round(a-a/3):
            c = 3
        else:
            c = 4
        bei.qingxiang += renpy.random.randint(0, 1)
        zhu.qingxiang += renpy.random.randint(0, 1)
        
        score = b*10-c*10
        if havetag("能言善辩",zhu) == True :
            score += 20
        if havetag("不善言辞",zhu) == True :
            score -= 20
        if havetag("能言善辩",bei) == True :
            score -= 20
        if havetag("不善言辞",bei) == True :
            score += 20
        score += (zhu.xinji-bei.xinji)*0.1
        score += (zhu.love-bei.love)*0.1
        score -= (zhu.familylevel - bei.familylevel)*2
        score += (zhu.beauty +zhu.qizhi +zhu.meili - bei.beauty -bei.qizhi -bei.meili)*0.1
        if score <= -10:
            tempnum = abs(score*(0.5-0.1*(b-c)))
            if tempnum >= 20:
                tempnum = 20
            else:
                pass
            
            if bei.huashu["二A"] != 0:
                tempnum = score*(0.5-0.1*(b-c))*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                zhu.xinji = zhu.xinji - tempnum
                bei.xinji = bei.xinji + tempnum
                tempnum =score*(0.5-0.1*(b-c))*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                battle_expchange(bei,zhu,tempnum)
                tempnum = score*0.1*(100+30+(bei.huashu["二A"]-1)*20)*0.01
                zhu.qingxiang = zhu.qingxiang - tempnum
                bei.qingxiang = bei.qingxiang + tempnum
            else:
                battle_expchange(bei,zhu,tempnum)
            tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，狼狈落败。\n"
            allstory.insert(0,tempstory2)
        elif score >= 10:
            tempnum = abs(score*(0.5-0.1*(b-c)))
            if tempnum >= 20:
                tempnum = 20
            else:
                pass
            if zhu.huashu["二A"] != 0:
                tempnum = score*(0.5-0.1*(b-c))*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                bei.xinji = bei.xinji - tempnum
                zhu.xinji = zhu.xinji + tempnum
                tempnum =score*(0.5-0.1*(b-c))*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                battle_expchange(zhu,bei,tempnum)
                tempnum = score*0.1*(100+30+(zhu.huashu["二A"]-1)*20)*0.01
                bei.qingxiang = bei.qingxiang - tempnum
                zhu.qingxiang = zhu.qingxiang + tempnum
            
            else:
                battle_expchange(zhu,bei,tempnum)
            tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，大获全胜。\n"
            allstory.insert(0,tempstory2)
        else:
            tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(zhu.hao)+(zhu.weifen)+str(zhu.name) +"同"+ str(bei.hao)+str(bei.weifen)+str(bei.name)+"口舌争锋，但并未分出胜负。\n"
            allstory.insert(0,tempstory2)
        return score

    def battle_expchange(win,lose,num):
        win.exp += abs(num)
        lose.exp -= abs(num)









label battle(fz):
    $ battle_list = []
    $ battle_list_fz = []
    $ battle_list_my = []
    $ waitfz = False
    $ myscore = 100
    $ fzscore = 100
    if yxxiao in my.Gongnv and yxxiao.like > 100:
        $ fzscore -= int((yxxiao.like - 100)*0.5)
    $ mybaolv = round(my.lucky)
    $ fzbaolv= round(fz.lucky)
    $ mybaoji = 1+my.level*0.01+my.familylevel*0.01
    $ fzbaoji = 1+fz.level*0.01+fz.familylevel*0.01
    $ mypais = fapai(my)
    $ fzpais = fapai(fz)
    call screen battle(fz = fz)
    python:
        a = len(yuanweifen)
        if my.level == 0: 
            b = 6
        elif my.qinjunum == 1: 
            b = 5
        elif my.level > round(a-a/3):
            b = 3
        else:
            b = 4
        if fz.level == 0: 
            c = 6
        elif fz.qinjunum == 1: 
            c = 5
        elif fz.level > round(a-a/3):
            c = 3
        else:
            c = 4
        if myscore >= 100:
            myscore = 100
        elif myscore <= 0:
            myscore = 0
        else:
            pass
        if fzscore >= 100:
            fzscore = 100
        elif fzscore <= 0:
            fzscore = 0
        else:
            pass
    if myscore > fzscore:
        if yxxiao in my.Gongnv:
            $ tempnum = (myscore - fzscore)*0.1
            if tempnum >= 10:
                $ tempnum = 10
            $ yxxiao.like += tempnum + 5
            if yxxiao.like >= 200:
                $ yxxiao.like = 200
        $ tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(my.hao)+(my.weifen)+str(my.name) +"同"+ str(fz.hao)+str(fz.weifen)+str(fz.name)+"口舌争锋，大获全胜。\n"
        $ allstory.insert(0,tempstory2)
        "[fz.hao][fz.weifen] [fz.name]" "（黯然）是我输了……"
        $ fz.yali += 5
        $ my.yali -= 5

        menu:
            "降其心智":
                $ tempnum = (myscore - fzscore)*(0.5-0.1*(b-c))
                $ fz.xinji = fz.xinji - tempnum
                $ my.xinji = my.xinji + tempnum
                $ fz.like = fz.like - tempnum*0.1
                "[fz.hao][fz.weifen] [fz.name]" "呵呵，聪明反被聪明误啊！"
                我 "只不过是还不够聪明罢了。"
                "（双方的心计发生了变化。）"
            "辱其自尊":
                $ tempnum = (myscore - fzscore)*(0.5-0.1*(b-c))
                $ battle_expchange(my,fz,tempnum)
                $ fz.like = fz.like - tempnum*0.2
                "[fz.hao][fz.weifen] [fz.name]" "这深宫之中，有又谁比谁更不堪呢？"
                我 "自然是败者。"
                "（双方的威望发生了变化。）"
            "摧其斗志":
                $ tempnum = (myscore - fzscore)*0.1
                $ fz.qingxiang = fz.qingxiang - tempnum
                $ my.qingxiang = my.qingxiang + tempnum
                "[fz.hao][fz.weifen] [fz.name]" "这些口舌纷争究竟要到何时才能休止。"
                我 "身不由己，故无休无止。"
                "（双方对于后宫争斗的态度产生了变化）"
            "以理服人" if my.huashu["二A"] != 0:
                我 "【发动话术技能——以理服人】"
                $ tempnum = (myscore - fzscore)*(0.5-0.1*(b-c))*(100+30+(my.huashu["二A"]-1)*20)*0.01
                $ fz.xinji = fz.xinji - tempnum
                $ my.xinji = my.xinji + tempnum
                $ fz.like = fz.like - tempnum*0.1
                $ tempnum = (myscore - fzscore)*(0.5-0.1*(b-c))*(100+30+(my.huashu["二A"]-1)*20)*0.01
                $ battle_expchange(my,fz,tempnum)
                $ fz.like = fz.like - tempnum*0.2
                $ tempnum = (myscore - fzscore)*0.1*(100+30+(my.huashu["二A"]-1)*20)*0.01
                $ fz.qingxiang = fz.qingxiang - tempnum
                $ my.qingxiang = my.qingxiang + tempnum


    elif myscore < fzscore:
        $ tempstory2 =  "【争锋】"+str(year)+"年"+str(month)+"月，"+str(my.hao)+(my.weifen)+str(my.name) +"同"+ str(fz.hao)+str(fz.weifen)+str(fz.name)+"口舌争锋，狼狈落败。\n"
        $ allstory.insert(0,tempstory2)
        $ my.yali += 5
        $ fz.yali -= 5
        我 "是我输了……"
        $ lucky = renpy.random.randint(0, 2)
        if fz.huashu["二A"] != 0:
            "[fz.hao][fz.weifen] [fz.name]" "【发动话术技能——以理服人】"
            $ tempnum = (fzscore - myscore)*(0.5-0.1*(c-b))*(100+30+(fz.huashu["二A"]-1)*20)*0.01
            $ fz.xinji = fz.xinji + tempnum
            $ my.xinji = my.xinji - tempnum
            $ tempnum = (fzscore - myscore)*(0.5-0.1*(b-c))*(100+30+(fz.huashu["二A"]-1)*20)*0.01
            $ battle_expchange(fz,my,tempnum)
            $ tempnum = (fzscore - myscore)*0.1*(100+30+(fz.huashu["二A"]-1)*20)*0.01
            $ fz.qingxiang = fz.qingxiang + tempnum
            $ my.qingxiang = my.qingxiang - tempnum
        elif lucky == 0:
            $ tempnum = (fzscore - myscore)*(0.5-0.1*(c-b))
            $ fz.xinji = fz.xinji + tempnum
            $ my.xinji = my.xinji - tempnum
            if fz.qingxiang > 70:
                "[fz.hao][fz.weifen] [fz.name]" "有人大智若愚，有人则不然。"
            elif fz.qingxiang < 30:
                "[fz.hao][fz.weifen] [fz.name]" "甚是无趣。"
            else:
                "[fz.hao][fz.weifen] [fz.name]" "总有些人喜欢耍些小聪明。"
            "（双方的心计发生了变化。）"
        elif lucky == 1:
            $ tempnum = (fzscore - myscore)*(0.5-0.1*(b-c))
            $ battle_expchange(fz,my,tempnum)
            "（双方的威望发生了变化。）"
        else:
            $ tempnum = (fzscore - myscore)*0.1
            $ fz.qingxiang = fz.qingxiang + tempnum
            $ my.qingxiang = my.qingxiang - tempnum
            "（双方对于后宫争斗的态度产生了变化）"
    else:
        "（并未分出胜负……）"
    python:
        renpy.return_statement()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
