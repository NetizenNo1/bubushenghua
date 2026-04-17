init python:
    def fl(pic, b = 0.2):
        return im.MatrixColor(pic, im.matrix.brightness(b))

screen scrtt(x=100, y=100, tt="ToolTips", ttime=0.5, htime=0, mpos=renpy.get_mouse_pos(), m=True):
    zorder 999
    if m:
        $ x = mpos[0]
        $ y = mpos[1]
    if ttime == 0:
        $ ttime = 0.1
    timer ttime action Show("scrtt_text", x = x, y = y, tt = tt)
    on "hide" action Hide("scrtt_text")
    if htime > 0:
        timer htime action Hide("scrtt")

screen scrtt_text(x, y, tt):
    zorder 999
    if x < 720:
        $ xa = 0.0
        if (1280 - x) < 640:
            $ xm = 1280 - x
        else:
            $ xm = 640
    else:
        $ xa = 1.0
        $ xm = 640

    if y < 360:
        $ ya = 0.0
        if (720 - y) < 360:
            $ ym = 720 - x
        else:
            $ ym = 360
    else:
        $ ym = 360
        $ ya = 1.0
    frame xanchor xa yanchor ya xpos x+10 ypos y+10 xmaximum xm ymaximum ym padding (20,10,20,10) background Frame("gui/notify.webp",10,10,tile = False):

        if isinstance(tt,int):
            text str(tt) color "#990000" size 25 font "问藏书房.ttf"
        else:
            text tt color "#990000" size 25 font "问藏书房.ttf"





screen ccc:

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" pos (100,0)
    textbutton (_("名称1")):
        action NullAction()
        tooltip "{color=fff}{b}名称1:{/b}\n介绍介绍介绍介绍介绍介绍介绍介绍{/color}"



    textbutton (_("名称2")):
        xpos 1200
        action NullAction()
        hovered Show("scrtt",tt="{b}名称2:{/b}\n介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍")
        unhovered [Hide("scrtt")]
    textbutton (_("名称2")):
        yalign .5
        xalign .5
        action NullAction()
        hovered Show("scrtt",tt="{b}名称2:{/b}\n介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍")
        unhovered [Hide("scrtt")]
    imagebutton:
        idle "gui/button/slot_idle_background.webp"
        hover fl("gui/button/slot_idle_background.webp")
        yalign 1.0
        xalign 1.0
        action NullAction()
        hovered Show("scrtt",tt="{b}名称2:{/b}\n介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍")
        unhovered [Hide("scrtt")]
 
