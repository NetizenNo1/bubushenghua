init python:
    def feipin0_func(newstring):
        store.feipin0 = newstring
    def feipin1_func(newstring):
        store.feipin1 = newstring
    def feipin2_func(newstring):
        store.feipin2 = newstring
    def feipin3_func(newstring):
        store.feipin3 = newstring
    def feipin4_func(newstring):
        store.feipin4 = newstring
    def feipin5_func(newstring):
        store.feipin5 = newstring
    def feipin6_func(newstring):
        store.feipin6 = newstring
    def feipin7_func(newstring):
        store.feipin7 = newstring
    def feipin8_func(newstring):
        store.feipin8 = newstring
    def feipin9_func(newstring):
        store.feipin9 = newstring
    def feipin10_func(newstring):
        store.feipin10 = newstring
    def feipin11_func(newstring):
        store.feipin11 = newstring
    def feipin12_func(newstring):
        store.feipin12 = newstring
    def feipin13_func(newstring):
        store.feipin13 = newstring
    def feipin14_func(newstring):
        store.feipin14 = newstring
    def feipin15_func(newstring):
        store.feipin15 = newstring
    def feipin16_func(newstring):
        store.feipin16 = newstring

    def feipinshu0_func(newnumber):
        store.feipinshu0 = newnumber
    def feipinshu1_func(newnumber):
        store.feipinshu1 = newnumber
    def feipinshu2_func(newnumber):
        store.feipinshu2 = newnumber
    def feipinshu3_func(newnumber):
        store.feipinshu3 = newnumber
    def feipinshu4_func(newnumber):
        store.feipinshu4 = newnumber
    def feipinshu5_func(newnumber):
        store.feipinshu5 = newnumber
    def feipinshu6_func(newnumber):
        store.feipinshu6 = newnumber
    def feipinshu7_func(newnumber):
        store.feipinshu7 = newnumber
    def feipinshu8_func(newnumber):
        store.feipinshu8 = newnumber
    def feipinshu9_func(newnumber):
        store.feipinshu9 = newnumber
    def feipinshu10_func(newnumber):
        store.feipinshu10 = newnumber
    def feipinshu11_func(newnumber):
        store.feipinshu11 = newnumber
    def feipinshu12_func(newnumber):
        store.feipinshu12 = newnumber
    def feipinshu13_func(newnumber):
        store.feipinshu13 = newnumber
    def feipinshu14_func(newnumber):
        store.feipinshu14 = newnumber
    def feipinshu15_func(newnumber):
        store.feipinshu15 = newnumber


init:
    default feipin0 = "皇后"
    default feipin1 = "贵妃"
    default feipin2 = "三妃"
    default feipin3 = "妃"
    default feipin4 = "九嫔"
    default feipin5 = "贵嫔"
    default feipin6 = "婕妤"
    default feipin7 = "容华"
    default feipin8 = "嫔"
    default feipin9 = "贵人"
    default feipin10 = "美人"
    default feipin11 = "才人"
    default feipin12 = "常在"
    default feipin13 = "御女"
    default feipin14 = "选侍"
    default feipin15 = "答应"
    default feipin16 = "更衣"

    default feipinshu0 = 1
    default feipinshu1 = 1
    default feipinshu2 = 3
    default feipinshu3 = 2
    default feipinshu4 = 9
    default feipinshu5 = 12
    default feipinshu6 = 9999
    default feipinshu7 = 9999
    default feipinshu8 = 9999
    default feipinshu9 = 9999
    default feipinshu10 = 9999
    default feipinshu11 = 9999
    default feipinshu12 = 9999
    default feipinshu13 = 9999
    default feipinshu14 = 9999
    default feipinshu15 = 9999
    default feipinshu16 = 9999


label 默认妃阶:
    $ feipin0 = "皇后"
    $ feipin1 = "贵妃"
    $ feipin2 = "三妃"
    $ feipin3 = "妃"
    $ feipin4 = "九嫔"
    $ feipin5 = "贵嫔"
    $ feipin6 = "婕妤"
    $ feipin7 = "容华"
    $ feipin8 = "嫔"
    $ feipin9 = "贵人"
    $ feipin10 = "美人"
    $ feipin11 = "才人"
    $ feipin12 = "常在"
    $ feipin13 = "御女"
    $ feipin14 = "选侍"
    $ feipin15 = "答应"
    $ feipin16 = "更衣"
    $ feipinshu0 = 1
    $ feipinshu1 = 1
    $ feipinshu2 = 3
    $ feipinshu3 = 2
    $ feipinshu4 = 9
    $ feipinshu5 = 12
    $ feipinshu6 = 9999
    $ feipinshu7 = 9999
    $ feipinshu8 = 9999
    $ feipinshu9 = 9999
    $ feipinshu10 = 9999
    $ feipinshu11 = 9999
    $ feipinshu12 = 9999
    $ feipinshu13 = 9999
    $ feipinshu14 = 9999
    $ feipinshu15 = 9999
    $ feipinshu16 = 9999

    call screen Changeweifen


screen Changeweifen:
    frame:
        xysize (800,800)
        align (0.5,0.5)
        vbox xalign 0.5:
            text ""
            text "妃阶设定" align (0.5,0.5)
        grid 3 18 align (0.5,0.5) xspacing 100:
            text "品级"
            text "位份"
            text "人数"
            text "中宫"
            button:
                id "weifen_0"
                action NullAction()
                add Input(size=28, color="#000", default=feipin0,changed=feipin0_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_0")) yalign 2.0
            button:
                id "renshu_0"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu0,changed=feipinshu0_func,length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_0")) yalign 2.0

            text "正一品{size=15}"
            button:
                id "weifen_1"
                action NullAction()
                add Input(size=28, color="#000", default=feipin1,changed=feipin1_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_1")) yalign 2.0
            button:
                id "renshu_1"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu1,changed=feipinshu1_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_1")) yalign 2.0

            text "从一品{size=15}"
            button:
                id "weifen_2"
                action NullAction()
                add Input(size=28, color="#000", default=feipin2,changed=feipin2_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_2")) yalign 2.0
            button:
                id "renshu_2"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu2,changed=feipinshu2_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_2")) yalign 2.0

            text "正二品{size=15}"
            button:
                id "weifen_3"
                action NullAction()
                add Input(size=28, color="#000", default=feipin3,changed=feipin3_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_3")) yalign 2.0
            button:
                id "renshu_3"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu3,changed=feipinshu3_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_3")) yalign 2.0

            text "从二品"
            button:
                id "weifen_4"
                action NullAction()
                add Input(size=28, color="#000", default=feipin4,changed=feipin4_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_4")) yalign 2.0
            button:
                id "renshu_4"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu4,changed=feipinshu4_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_4")) yalign 2.0


            text "正三品"
            button:
                id "weifen_5"
                action NullAction()
                add Input(size=28, color="#000", default=feipin5,changed=feipin5_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_5")) yalign 2.0
            button:
                id "renshu_5"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu5,changed=feipinshu5_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_5")) yalign 2.0

            text "从三品"
            button:
                id "weifen_6"
                action NullAction()
                add Input(size=28, color="#000", default=feipin6,changed=feipin6_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_6")) yalign 2.0
            button:
                id "renshu_6"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu6,changed=feipinshu6_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_6")) yalign 2.0

            text "正四品"
            button:
                id "weifen_7"
                action NullAction()
                add Input(size=28, color="#000", default=feipin7,changed=feipin7_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_7")) yalign 2.0
            button:
                id "renshu_7"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu7,changed=feipinshu7_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_7")) yalign 2.0

            text "从四品"
            button:
                id "weifen_8"
                action NullAction()
                add Input(size=28, color="#000", default=feipin8,changed=feipin8_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_8")) yalign 2.0
            button:
                id "renshu_8"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu8,changed=feipinshu8_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_8")) yalign 2.0

            text "正五品"
            button:
                id "weifen_9"
                action NullAction()
                add Input(size=28, color="#000", default=feipin9,changed=feipin9_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_9")) yalign 2.0
            button:
                id "renshu_9"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu9,changed=feipinshu9_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_9")) yalign 2.0

            text "从五品"
            button:
                id "weifen_10"
                action NullAction()
                add Input(size=28, color="#000", default=feipin10,changed=feipin10_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_10")) yalign 2.0
            button:
                id "renshu_10"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu10,changed=feipinshu10_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_10")) yalign 2.0

            text "正六品"
            button:
                id "weifen_11"
                action NullAction()
                add Input(size=28, color="#000", default=feipin11,changed=feipin11_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_11")) yalign 2.0
            button:
                id "renshu_11"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu11,changed=feipinshu11_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_11")) yalign 2.0

            text "从六品"
            button:
                id "weifen_12"
                action NullAction()
                add Input(size=28, color="#000", default=feipin12,changed=feipin12_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_12")) yalign 2.0
            button:
                id "renshu_12"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu12,changed=feipinshu12_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_12")) yalign 2.0

            text "正七品"
            button:
                id "weifen_13"
                action NullAction()
                add Input(size=28, color="#000", default=feipin13,changed=feipin13_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_13")) yalign 2.0
            button:
                id "renshu_13"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu13,changed=feipinshu13_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_13")) yalign 2.0

            text "从七品"
            button:
                id "weifen_14"
                action NullAction()
                add Input(size=28, color="#000", default=feipin14,changed=feipin14_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_14")) yalign 2.0
            button:
                id "renshu_14"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu14,changed=feipinshu14_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_14")) yalign 2.0

            text "正八品"
            button:
                id "weifen_15"
                action NullAction()
                add Input(size=28, color="#000", default=feipin15,changed=feipin15_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_15")) yalign 2.0
            button:
                id "renshu_15"
                action NullAction()
                add Input(size=28,color="#000",default=feipinshu15,changed=feipinshu15_func, length=4,allow={"1","2","3","4","5","6","7","8","9","0"},button=renpy.get_widget("Changeweifen","renshu_15")) yalign 2.0

            text "从八品"
            button:
                id "weifen_16"
                action NullAction()
                add Input(size=28, color="#000", default=feipin16,changed=feipin16_func, length=3,copypaste=True,button=renpy.get_widget("Changeweifen","weifen_16")) yalign 2.0
            text "9999"

        hbox:
            align (0.5,1.0)
            spacing 25
            textbutton "恢复默认" action Hide("Changeweifen"),Jump("默认妃阶")
            textbutton "完成" action Hide("Changeweifen"),Jump("设定完成")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
