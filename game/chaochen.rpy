init python:
    guanwei = ["","一品","二品","三品","四品","五品","六品","七品","八品","九品"]
    Guanyuan_page=0
    class MalesFactory(object):
        def instantiation_Males(self):
            return NPC_Males()




    class Males(object):
        def __init__(self):
            self.xing = xing
            self.ming = ming
            self.name = name
            self.age = age
            self.level = level
            self.duty = duty
            self.zhong = zhong
            self.neng = neng
            self.exp = exp
            self.shili = shili
            self.feizi = feizi
            self.zhichi = zhichi
            self.friends = friends
            self.foes = foes
            self.marry = marry
            self.lovers = lovers
        
        def Males_creat(self):
            self.xing = ""
            self.ming = ""
            self.name = ""
            self.age = 0
            self.face = 0
            self.beauty = 0
            self.shou = 80
            self.level = 0
            self.duty = ""
            self.zhong = 0
            self.neng = 0
            self.exp = 0
            self.shili = 0
            self.feizi = []
            self.zhichi = None
            self.friends = []
            self.foes = []
            self.marry = False
            self.lovers = []

    def Males_random(self,whose,how):
        self.xing = whose.xing
        self.ming = renpy.random.choice(malename_list)+renpy.random.choice(malename2_list)
        self.name = self.xing+self.ming
        if how == 0: 
            self.age =  whose.age + renpy.random.randint(18,40)
            self.marry = True
        elif how == 1:
            self.age =  whose.age + renpy.random.randint(-10,10)
            if self.age <= 16:
                self.age = 16
            lucky = renpy.random.randint(0,self.age)
            if lucky <= 12:
                pass
            else:
                self.marry = True
        elif how == 2:
            self.age =  whose.age + renpy.random.randint(36,60)
            if self.age >= 70:
                self.age = 70
            self.marry = True
        else:
            self.age = whose.age + renpy.random.randint(-20,20)
            if self.age <= 16:
                self.age = 16
            self.marry = True
        
        self.face = 0
        self.beauty = renpy.random.randint(0,100)
        self.shou = renpy.random.randint(self.age+5,100)
        
        self.level = whose.familylevel
        self.duty = whose.fatherduty
        self.zhong = renpy.random.randint(0,100)
        self.neng = renpy.random.randint(0,100)
        self.shili = (11 - self.level)*renpy.random.randint(1,10) *0.1 + renpy.random.randint(-20,20) + self.neng
        self.exp = renpy.random.randint(-20,20)
        self.feizi = [whose]
        self.zhichi = None
        self.friends = []
        self.foes = []


    class NPC_Males(Males):
        def __init__(self):
            Males.Males_creat(self)

    factory = MalesFactory()

    def Creat_Males(whose,how):
        a = factory.instantiation_Males()
        Males_random(a,whose,how)
        if how == 0:
            whose.father = a
        else:
            pass
        whose.jiazu.append(a)
        if 1 <= a.level <= 9:
            guanyuan_list.append(a)

    def gyb_change(how):
        global guanyuan_list
        guanyuan_list = sorted(guanyuan_list, key=attrgetter(how),reverse = False)

style guanyuanbiao_button_text:
    font "问藏书房.ttf"
    min_width 100
    size 30
    text_align 0.5


style guanyuanbiao_text:
    min_width 100
    size 30
    text_align 0.5


screen guanyuanbiao:
    style_prefix "guanyuanbiao"
    $ next_Guanyuan_page = Guanyuan_page + 1
    $ prev_Guanyuan_page = Guanyuan_page - 1
    $ max_Guanyuan_page = round(len(guanyuan_list)/10)+1
    $ b = Guanyuan_page*10+10

    if b >= len(guanyuan_list):
        $ b = len(guanyuan_list)
    else:
        pass
    frame:
        background Frame([ "gui/frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=True)
        xsize 1400
        ysize 680
        align (0.5,0.5)
        hbox:
            align (0.5, 1.0)
            spacing 0
            if Guanyuan_page > 0:
                textbutton "《《" action SetVariable('Guanyuan_page', prev_Guanyuan_page), Show("guanyuanbiao")
            else:
                textbutton "《《"
            text "第[next_Guanyuan_page]页"
            if Guanyuan_page < max_Guanyuan_page:
                textbutton "》》" action SetVariable('Guanyuan_page', next_Guanyuan_page), Show("guanyuanbiao")
            else:
                textbutton "》》"

        grid 1 11:
            pos (0.05,0.05)
            xsize 1400
            ysize 600
            xspacing 20
            $ a = 0
            $ next_Guanyuan_page = Guanyuan_page + 1
            fixed:
                xsize 1400
                ysize 40
                hbox spacing 25:
                    textbutton "职位":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"level")
                        align (0.5,0.5)
                    textbutton "名字":
                        text_style "guanyuanbiao_button_text"
                        action NullAction()
                        align (0.5,0.5)
                    textbutton "年龄":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"age")
                        align (0.5,0.5)
                    textbutton "外貌":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"beauty")
                        align (0.5,0.5)
                    textbutton "能力":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"neng")
                        align (0.5,0.5)
                    textbutton "忠诚":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"zhong")
                        align (0.5,0.5)
                    textbutton "势力":
                        text_style "guanyuanbiao_button_text"
                        action Function(gyb_change,"shili")
                        align (0.5,0.5)
                    textbutton "婚配":
                        text_style "guanyuanbiao_button_text"
                        action NullAction()
                        align (0.5,0.5)
                    text "关系" align (0.5,0.0)


            for i in guanyuan_list[Guanyuan_page*10:b]:
                if a <= b:
                    fixed:
                        xsize 1400
                        ysize 40
                        hbox spacing 25:
                            text guanwei[i.level] + i.duty align (0.5,0.5)
                            text "[i.name]" align (0.5,0.5)
                            text "[i.age]" align (0.5,0.5)
                            text "[i.beauty]" align (0.5,0.5)
                            text "[i.neng]" align (0.5,0.5)
                            text "[i.zhong]" align (0.5,0.5)
                            text "[i.shili]" align (0.5,0.5)
                            if i.marry == True:
                                text "已婚" align (0.5,0.5)
                            else:
                                text "未婚" align (0.5,0.5)
                            python:
                                temptext = ""

                                for j in i.feizi:
                                    temptext += j.hao+j.weifen+j.name + " "
                            text "[temptext]" align (0.5,0.5)


                    $ a = a + 1
                else:
                    null
            if a < 10:
                for j in range(a, 10):
                    null
    frame:
        background None
        align (1.0,1.0)
        imagebutton idle "gui/button/返1.webp" hover "gui/button/返2.webp":
            action Hide("guanyuanbiao"),Jump("皇宫界面")
 
