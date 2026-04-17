
style gdjm_text:
    font "问藏书房.ttf"
    size 25
    text_align 0.5

style gdjm_button_text:
    font "问藏书房.ttf"
    size 25
    text_align 0.5
    min_width 100
screen gdjm_ready():
    style_prefix "gdjm"
    default gdjm_page = 1
    add "gui/frame.webp" zoom 1.2 xalign 0.45 yalign 0.25
    frame:
        background None
        xsize 1200
        ysize 480
        align (0.4,0.3)
        has vpgrid
        cols 1
        rows len(xdsj_ready)+len(zysj_ready)+2
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        pos (0.1,0.0)
        xsize 1200
        ysize 480
        yspacing 30
        fixed:
            xsize 1200
            ysize 35
            hbox:
                text "状态" align (0.5,0.5) min_width 100
                text "涉事人" align (0.5,0.5) min_width 200
                text "事件" align (0.5,0.5) min_width 100
                text "时限" align (0.5,0.5) min_width 100
                text "进度" align (0.5,0.5) min_width 100
                text "主使" align (0.5,0.5) min_width 200
                text "合谋" align (0.5,0.5) min_width 200


        for i in gdsj:
            if i in zysj_ready:
                if i.zhu == my:
                    fixed:
                        xsize 1200
                        ysize 35
                        hbox:
                            if my.state == "病重" or jinzu(my) == True:
                                textbutton "无法筹备"
                            else:
                                textbutton "筹备" action Function(myzaoyao_gc,sj = i )
                            text i.bei.hao + i.bei.weifen + i.bei.name min_width 200
                            text zyfs[i.way] min_width 100
                            text str(i.time1) min_width 100
                            text str(int(i.jilv)) min_width 100
                            text i.zhu.hao + i.zhu.weifen + i.zhu.name min_width 200
                            text "妃嫔"+str(len(i.hemou)) + "人 宫女" + str(len(i.gn)) + "人 " min_width 200
                elif i in xdsj_ready:
                    if i.zhu == my:
                        fixed:
                            xsize 1200
                            ysize 35
                            hbox:

                                text "准备中"


                                text i.bei.hao + i.bei.weifen + i.bei.name min_width 200
                                text xdwp[i.way] min_width 100
                                text "-" min_width 100
                                text "-" min_width 100
                                text i.zhu.hao + i.zhu.weifen + i.zhu.name min_width 200
                                text "宫女" + str(len(i.gn)) + "人 " min_width 200
                else:
                    pass


            else:
                pass
        hbox spacing 15:
            textbutton "管理宫务" action Hide("gdjm_ready"),Call("管理宫务")
            textbutton "管理皇嗣" action Hide("gdjm_ready"),Call("管理皇嗣")
            textbutton "家族事宜" action Hide("gdjm_ready"),Call("家族事宜")
            textbutton "制造谣言" action Hide("gdjm_ready"),Call("主角造谣")
            textbutton "使用毒药" action Hide("gdjm_ready"),Call("主角下毒")

    frame:
        background None
        align (0.2,0.1)
        has hbox

        textbutton "{size=30}{font=问藏书房.ttf}我 的"
        textbutton "{size=30}{font=问藏书房.ttf}调查中" action Hide("gdjm_ready"),Show("gdjm")
        textbutton "{size=30}{font=问藏书房.ttf}已结束" action Hide("gdjm_ready"),Show("gdjm_end")

    frame:
        background None
        align (0.8,0.8)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("gdjm_ready"),Show("myroom")


screen gdjm():
    style_prefix "gdjm"
    default gdjm_page = 1
    add "gui/frame.webp" zoom 1.2 xalign 0.45 yalign 0.25
    frame:
        background None
        xsize 1200
        ysize 500
        align (0.4,0.3)
        has viewport
        draggable True
        mousewheel True
        scrollbars "horizontal"
        align (0.5,0.5)
        xsize 1080
        ysize 450
        hbox:
            for i in gdsj:

                if i in zysj:
                    $ tempnum = 100 - i.jilv
                    if tempnum <= 0:
                        $ tempnum = 0
                    vbox spacing 20:
                        text i.bei.hao + i.bei.weifen + i.bei.name:
                            size 35
                            min_width 300
                        text zyfs[i.way] + "事件":
                            size 35
                            min_width 300
                        text "剩余时间:" +str(i.time2):
                            size 30
                            min_width 300
                        text "调查进度:" +str(tempnum):
                            size 30
                            min_width 300
                        text "{size=30}助力施压":
                            size 30
                            min_width 300
                        hbox align (0.5,0.5):

                            textbutton "{size=25}银两贿赂" action Call("造谣_助_贿赂",what = i)
                            textbutton "{size=25}委派宫女" action Call("造谣_委派",what= i,how = 0)
                        text "{size=30}阻挠调查":
                            size 30
                            min_width 300
                        hbox align (0.5,0.5):
                            textbutton "{size=25}银两贿赂" action Call("造谣_阻_贿赂",what = i)
                            textbutton "{size=25}委派宫女" action Call("造谣_委派",what= i,how = 1)
                elif i in xdsj:
                    vbox spacing 20:
                        text i.bei.hao + i.bei.weifen + i.bei.name:
                            size 35
                            min_width 300
                        if i.jieguo == -1:
                            text "被投毒未遂事件":
                                size 35
                                min_width 300
                        else:
                            text "中毒事件":
                                size 35
                                min_width 300
                        text "涉及毒药:"+xdwp[i.way]:
                            size 25
                            min_width 300
                        text "调查期限:"+str(i.time2):
                            size 25
                            min_width 300
                        text "涉嫌人物:":
                            size 30
                            min_width 300
                        for j in i.xianyi:
                            text j[0].hao + j[0].weifen + j[0].name +"：" +str(int(j[1])):
                                size 25
                                min_width 300
                            hbox align (0.5,0.5):
                                text "{size=40}↑"
                                textbutton "{size=20}银两贿赂" action Call("下毒_助_贿赂",what = j)
                                textbutton "{size=20}委派宫女" action Call("下毒_委派",what= j,how = 0)
                            hbox align (0.5,0.5):
                                text "{size=40}↓"
                                textbutton "{size=20}银两贿赂" action Call("下毒_阻_贿赂",what = j)
                                textbutton "{size=20}委派宫女" action Call("下毒_委派",what= j,how = 1)


    frame:
        background None
        align (0.2,0.1)
        has hbox

        textbutton "{size=30}{font=问藏书房.ttf}我 的" action Hide("gdjm"),Show("gdjm_ready")
        textbutton "{size=30}{font=问藏书房.ttf}调查中"
        textbutton "{size=30}{font=问藏书房.ttf}已结束" action Hide("gdjm"),Show("gdjm_end")

    frame:
        background None
        align (0.8,0.8)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("gdjm"),Show("myroom")

screen gdjm_end():
    style_prefix "gdjm"
    default gdjm_page = 1
    add "gui/frame.webp" zoom 1.2 xalign 0.45 yalign 0.25
    frame:
        background None
        xsize 1200
        ysize 480
        align (0.4,0.3)

        has vpgrid
        cols 1
        rows len(xdsj_end)+len(zysj_end)+1
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        pos (0.1,0.0)
        xsize 1200
        ysize 480
        yspacing 30
        fixed:
            xsize 1200
            ysize 35
            hbox:
                text "状态" align (0.5,0.5) min_width 100
                text "涉事人" align (0.5,0.5) min_width 200
                text "事件" align (0.5,0.5) min_width 100
                text "时限" align (0.5,0.5) min_width 100
                text "进度" align (0.5,0.5) min_width 100
                text "主使" align (0.5,0.5) min_width 200
                text "合谋" align (0.5,0.5) min_width 200

        for i in gdsj:

            if i in zysj_end:
                $ temptext = ""
                for j in i.hemou:
                    $ temptext += str(j.hao) + str(j.weifen) + str(j.name) + " "
                fixed:
                    xsize 1200
                    ysize 35
                    hbox:
                        hbox:
                            text "已结束" min_width 100
                            text i.bei.hao + i.bei.weifen + i.bei.name min_width 200
                            text zyfs[i.way] min_width 100
                            text "-" min_width 100
                            if i.state == 1:
                                text "冤案" min_width 100
                                text i.zhu.hao + i.zhu.weifen + i.zhu.name min_width 200
                                text temptext min_width 200
                            elif i.state == 0:
                                textbutton "定罪":
                                    action NullAction()
                                    hovered Show("scrtt",tt=i.zhu.name)
                                    unhovered [Hide("scrtt")]
                                text " "
                                text " "


            elif i in xdsj_end:
                fixed:
                    xsize 1200
                    ysize 35
                    hbox:
                        hbox:
                            if i.jieguo == -1:
                                text "未遂" min_width 100

                            else:
                                text "中毒" min_width 100

                            text i.bei.hao + i.bei.weifen + i.bei.name min_width 200
                            text xdwp[i.way] min_width 100
                            text "-" min_width 100
                            if i.state == 0:
                                textbutton "疑案":
                                    action NullAction()
                                    hovered Show("scrtt",tt=i.zhu.name)
                                    unhovered [Hide("scrtt")]

                                text ""
                                text ""
                            elif i.state == 1:
                                textbutton "查明":
                                    action NullAction()
                                    hovered Show("scrtt",tt=i.zhu.name)
                                    unhovered [Hide("scrtt")]

                                text i.zuiren.hao + i.zuiren.weifen + i.zuiren.name min_width 200
                                text ""



    frame:
        background None
        align (0.2,0.1)
        has hbox
        textbutton "{size=30}{font=问藏书房.ttf}我 的" action Hide("gdjm_end"),Show("gdjm_ready")
        textbutton "{size=30}{font=问藏书房.ttf}调查中" action Hide("gdjm_end"),Show("gdjm")
        textbutton "{size=30}{font=问藏书房.ttf}已结束"

    frame:
        background None
        align (0.8,0.8)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("gdjm_end"),Show("myroom")
 
