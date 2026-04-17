init python:
    import copy
    def bgm(self):
        temp = eval("audio." + self)
        if renpy.music.get_playing(channel='music') != temp:
            renpy.music.play(temp)
        else:
            pass


    sanfei = ["淑妃","德妃","贤妃"]
    jiupin = ["昭仪","昭容","昭媛","修仪","修媛","修容","充仪","充媛","充容"]

    hejing = ["千鲤池","莲韵池","太液池","涵虚泽","蓬莱岛"]
    yuanlin = ["御花园","上林苑","紫竹林","疏影园"]
    yuhuayuan = ["御花园","玉烟亭","千鲤池","花间阁"]




    xing_list = ["王","陈","李","王","陈","李","黎","成","刘","刘","柳","黄","花","沈","沈","苏","苏","凤","兰","冷","廖","金","洪","荣","戚","秦","戚","秦","关","谷","董","殷","殷","辛","郑","梅","左","武","郁","邓","万","甄","沈","宋","宋","风","向","钟","谢","钟","谢","曾","戴","公孙","长孙","独孤","夏侯","季","蔺","吴","鄢","景","季","蔺","吴","鄢","景","云","岳","尚","商","姚","姚","迟","饶","展","荆","海","魏","卫","魏","卫","朱","祝","祝","兰","苏","舒","萧","萧","肖","林","林","林","凌","连","安","庄","华","年","曾","罗","洛","孙","简","贺","纳兰","尹","伊","倪","习","叶","叶","岳","慕容","慕容","童","周","张","周","张","章","杨","赵","陆","路","赵","陆","路","袁","代","易","何","付","何","付","钟","田","孟","孟","温","文","闻","江","姜","姜","蒋","冯","郭","虞","郁","余","俞","容成","傅","欧阳","上官","晏","韩","梁","常","容","司马","司徒","闵","卓","言","颜",
    "胡","楚","顾","墨","潘","拓跋","邱","郭","薛","唐","薛","唐","汤","晋","庄","徐","许","徐","许","吕","卢","荀","施","齐","司","祁","施","齐","司","祁","姬","姒","木","穆","慕","木","穆","慕","白","夏","谭","方","方","云","曲","水","阮","宁","任","史","乔","周","上官","慕容","楚","禇","温","车","朱","秦","尤","何","贺","戚","言","华","陶","余","喻","水","窦","云","苏","潘","葛","任","袁","柳","唐","连","练","廉","费","裴","岑","薛","越","汤","滕","罗","洛","骆","安","常","毕","时","傅","齐","顾","孟","平","穆","萧","姚","邵","湛","明","臧","伏","谈","祝","杜","阮","纪","尹","袭","席","路","娄","魏","危","梅","童","林","夏","胡","凌","霍","蔡","徐","柯","昝","卢","莫","房","解","应","丁","宣","崔","嵇","荀","杨","甄","封","靳","段","景","段","景","郗","班","宁","詹","薄","薄","蒲","蔺","翟","晏","晏","鱼","易","慎","耿","简","关","竺"]




    ming2_list = ["樱","莹","樱","莹","樱","莹","映","颖","宸","澄","华","灵","翎","妩","芜","画","宁","杏","桃","诺","络","珞","析","吟","真","珍","贞","臻","弗","沁","思","玫","香","竹","兮","兮","汐","惜","曦","溪","兮","卓","扶","池","漾","蝶","笙","修","凌","伶","龄","聆","菱","玲","陵","苓","泠","晴","轻","卿","沁","琴","黎","梨","离","姜","嘉","佳","央","姗","妤","洁","婷","澜","澜","兰","兰","兰","素","音","银","秀","朱","珠","紫","南","舒","菁","夏","璃","雅","曼","媚","眉","明","昭","君","诗","敏","茗","彤","瞳","韶","淑","苏","纯","淳","秋","巧","乔","穗","安","恬","璇","容","容","蓉","舜","娴","清","衣","衣","稚","芹","衾","庆","寻","薰","韵","芸","韵","芸","蕴","筠","娆","瑶","娆","瑶","娆","瑶","雪","萍","萱","媛","雪","蓼","柔","柔","岑","笙","欢","雨","语","嫣","语","嫣","燕","艳","妍","滟","颜","妍","颜","言","心","欣","心","欣","馨","伊","仪","伊","仪","忆","漪","宜","碧","白","楚","芙","钰","玉","羽","郁","珩","璐","婉","宛","晚","莞","婉","宛","晚","莞","婉","宛","绾","瑜","愉","瑜","愉","虞","莲","莲","潋","怜","若","月","闲","若","月","悦","染","苒","芊","纤","芊","纤","柳","烟","凝","霜","涵","寒","含","梦","如","如","茹","乐","之","之","芳","芬","蕊","吹","兰","悠","菲","墨","陌","茉","默","薇","端","祈","戚","萧","潇","惠","静","荷","年","念","汐","熙","曦","茵","芷","锦","瑾","堇","锦","瑾","堇","潇","湘","蕙","慧","瑟","佩","巧","然","絮","煦","谧","宓","瑶","琼","儿","儿","儿","儿","儿","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    ming1_list = ["樱","莹","莹","映","颖","宸","澄","华","灵","翎","妩","梧","芜","画","画","宁","星","杏","桃","浣","洛","诺","络","珞","析","吟","吟","真","珍","贞","臻","弗","沁","沁","沁","思","玫","阮","香","竹","兮","汐","惜","曦","溪","兮","卓","扶","池","漾","蝶","修","凌","伶","龄","聆","菱","玲","陵","苓","泠","晴","泠","晴","泠","晴","轻","卿","卿","卿","沁","琴","丽","黎","梨","离","笑","嘉","佳","央","姗","妤","语","玉","予","瑜","瑜","洁","婷","澜","澜","兰","兰","兰","素","音","银","秀","流","朱","珠","橙","紫","绿","南","舒","晶","夏","璃","雅","曼","媚","眉","倩","明","昭","君","诗","敏","茗","彤","瞳","韶","淑","苏","纯","淳","淳","秋","冬","巧","乔","穗","安","宝","恬","璇","容","容","蓉","绒","顺","娴","清","衣","稚","芹","衾","寻","薰","韵","芸","蕴","筠","韵","芸","蕴","筠","娆","瑶","瑶","瑶","雪","萍","萱","宣","媛","雪","寄","柔","柔","柔","岑","笙","润","欢","雨","语","嫣","嫣","燕","艳","妍","妍","滟","颜","言","心","欣","欣","馨","伊","仪","忆","漪","宜","宜","碧","楚","黛","芙","钰","玉","羽","郁","珩","璐","露","婉","宛","晚","莞","婉","宛","晚","莞","瑜","愉","虞","莲","潋","怜","若","若","若","若","月","悦","染","苒","芊","芊","芊","纤","柳","烟","凝","烟","凝","霜","涵","寒","含","梦","如","如","如","茹","乐","之","芳","芬","蕊","吹","兰","悠","悠","菲","苑","墨","陌","茉","默","薇","慎","端","祈","萋","期","潇","惠","静","素","素","荷","年","念","西","汐","熙","曦","茵","芷","锦","瑾","堇","锦","瑾","堇","潇","湘","蕙","慧","瑟","佩","然","翠","絮","煦","绛","谧","宓","瑶","琼","之","子","子","子"]

    malename_list = ["泊","凌","景","靖","凌","定","伏","闲","德","端","浩","珩","冠","辉","寒","徽","晖","寄","既","寂","寞","籍","霁","迹","立","蒲","如","长","畅","荼","雾","悟","与","宇","喻","予","豫","慎","宸","晨","悠","昇","峪","彦","穆","江","麟","尘","川","霄","常","鹤","志","道","念","卫","栾","宣","之","拓","翰","效","宇","弘","如","庄","颢","少","宁","胥","丞","舒","行","凡","竞","冉","泽","睦","迟","澄","熙","以","峥","明","凯","锡","锦","展","昭","昭","玄","玄","安"]

    malename2_list = ["泊","凌","景","靖","凌","彬","伏","闲","德","端","浩","珩","冠","辉","寒","徽","晖","寄","及","既","寂","寞","理","籍","霁","迹","立","蒲","如","长","畅","荼","雾","悟","与","宇","喻","予","豫","慎","宸","晨","悠","昇","峪","彦","穆","江","麟","尘","欢","川","霄","常","鹤","志","念","栾","宣","之","拓","翰","效","宇","弘","如","庄","颢","少","宁","胥","丞","舒","行","凡","竞","冉","泽","睦","迟","澄","熙","峥","明","凯","锡","昭","昭","玄","玄","安","锦","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

    hime_hao = ["镇国","万年","太平","敬武","长乐","长宁"]
    hime_hao1 = ["永","万","高","弘","陶","常","富","固","新","获","平","嘉","隆","裕","德","敬","温","宁","颛","庆","永","密","禧","熙","熹","荣","安","康","成","明","诚","宣","懿","乐","阳","文","舞","惠","宜","仪","贤","昭","毓","英","盈","齐","临","灵","昌","昶","旭","绪","兴","广","建","宪","穆","遥","渝","懋","玉","原","元","信","华","丰","兰"]
    hime_hao2 = ["城","阴","河","山","寿","陵","平","嘉","隆","裕","德","敬","温","宁","颛","庆","永","密","禧","熙","熹","荣","安","康","成","明","诚","宣","懿","乐","阳","文","舞","惠","宜","仪","贤","昭","毓","英","盈","齐","临","灵","昌","昶","旭","绪","兴","广","建","宪","穆","遥","渝","懋","玉","原","元","信","华","丰","兰"]
    teshuming = ["安然","锦瑟","月仪","瑾年","宓枕","解语","沅栎","婠婠","执宜","梦纾","蓁蓁","归晚","楚楚","云瑶","姒月","妍霏","絮锦","溪暮","玉倾","筠娘","双鲤","芷君","则淇","妤仪","灼华","韶光","腻云","沭华","重月","知意","奉吟","云栖","云翳","羡鱼","嬛嬛","墨染","寄雨","蔚纾","子莹","柒羽","慕情","招摇","芙鸳","无乐","月笙","兰泽","弄影","熹微","月来","安韶","灼华","安岁","清鸢","卿辞","寻寻","又双","叒叕","九歌","九韶","清湫","清浅","霓裳","辞柔","剪梅","玉棠","明麒","白芷","尧茜","弋弋","训英","青窈","解忧","玉致","攒玉","云昭","熙媛","沅儿","云裳","云倾","启楚","月牙","子卿","子衿","漱漱","疏疏","宴歌","琬琰","当归","琳琅","觅玉","云书","与荷","寻漪","清鸾","清知","月见","沅芷","追月","余欢","珲音","知颐","之贻","从仪","霜华","芸笙","聆歌","明笑","禾猗","惊瑜","相映","青照","兰因","絮果","犹知","云簪","时缨","如枝","凭澜","当当","罗敷","柳娇","蒙欢","梦沅","梦芙","云中","风莲","迟迟","晚晚","娇娇","芊芊","溶溶","莺莺","翩翩","翡翠","蝉语","归鹭","绯婴","弗楹","飞燕","合德","飞滟","宜主","遗光","思琅","阿姬","琊姬","广湄","眉钗","诱霜","若拙"]



    def cygd(how=True): 
        global tempfzlist
        tempfzlist = []
        for i in NPC_fz_list:
            if i.level == beifei:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重":
                pass
            elif   tags[4] in i.tags:
                pass
            elif tags_yali[2] in i.tags:
                pass
            else:
                tempfzlist.append(i)
        if how == True:
            if my in tempfzlist:
                tempfzlist.remove(my)
        else:
            pass
        return tempfzlist

    def weifenzu_del(self):
        a = self.level
        if isinstance(weifen_list[a][1],list):
            if self.weifen != []:
                tempweifen = renpy.random.choice(weifen_list[a][1])
                
                weifen_list[a][1].remove(tempweifen)
                self.weifen = str(tempweifen)
            else:
                
                tempweifen = renpy.random.choice(yuanweifen[a][1])
                self.weifen = str(tempweifen)
        else:
            self.weifen = str(weifen_list[a][1])
        return self.weifen

    def weifenzu_add(self):
        for i in yuanweifen:
            if isinstance(i[1],tuple):
                if self.weifen in i[1]:
                    a = i[0]
                    if isinstance(weifen_list[a][1],list) and self.weifen not in weifen_list[a][1]:
                        weifen_list[a][1].append(self.weifen)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return self.weifen

    import pygame.scrap
    def scrubs(what):
        pygame.scrap.put(pygame.SCRAP_TEXT, what.encode("utf-8"))
        renpy.notify("已复制文本至剪贴板。")





    def randompalace(self):
        tempnum = len(shengyuzhengdian_list)
        
        
        
        if self.level ==0:
            self.palace = "凤仪宫"
            self.palacenum = 999
            self.qinjunum = 999
            self.qinju = ""
        elif self.level == beifei:
            self.palace = "冷宫"
            self.palacenum = 666
            self.qinjunum = 666
            self.qinju = ""
        elif self.level < 4 and len(shengyuzhengdian_list) >0:
            a = renpy.random.choice(shengyuzhengdian_list)
            shengyuzhengdian_list.remove(a)
            palaces[a][0][1] = palaces[a][0][1] +1
            palaces[a][1][1] = self
            self.palacenum = a
            self.qinjunum = 1
            self.palace =  palaces[a][0][0]
            self.qinju =  palaces[a][1][0]
        
        
        else:
            if len(shengyucedian_list) != 0:
                a = renpy.random.choice(shengyucedian_list)
                templist = []
                tempnum = 2
                for j in palaces[a][2:]:
                    if str(j[1]) == "":
                        templist.append(tempnum)
                    else:
                        pass
                    tempnum += 1
                b = renpy.random.choice(templist)
                palaces[a][0][1] = palaces[a][0][1] +1
                self.qinju =palaces[a][b][0]
                palaces[a][b][1] = self
                self.palacenum = a
                self.qinjunum = b
                self.palace =  palaces[a][0][0]
                tempnum = 0
                for j in palaces[a][2:]:
                    
                    if str(j[1]) == "":
                        tempnum += 1
                    else:
                        pass
                if tempnum <= 0 :
                    shengyucedian_list.remove(a)
            
            
            
            else:
                self.palace = "未分配"
                self.palacenum = -1
                self.qinjunum = -1
                self.qinju = ""











    def randomname(self):
        self.xing = renpy.random.choice(xing_list)
        self.ming = renpy.random.choice(ming_list) + renpy.random.choice(ming2_list)
        if len(self.ming) >= 3:
            self.ming = self.ming[0] + self.ming[1]
        if self.ming in teshuming and self.ming in ming_list:
            ming_list.remove(self.ming)
        self.name = self.xing + self.ming
        
        return self.name



    def randomshuxing(self):
        lucky = renpy.random.randint(0, 2)
        if lucky ==0:
            self.beauty = self.makelucky/3 + renpy.random.randint(-100,200)
            if self.beauty > 950:
                self.beauty = 950
            else:
                pass
            self.meili = (self.makelucky-self.beauty)/2 + renpy.random.randint(-100,200)
            if self.meili >950:
                self.meili = 950
            else:
                pass
            self.qizhi = self.makelucky - self.meili - self.beauty + renpy.random.randint(0,200)
            if self.qizhi >950:
                self.qizhi = 950
            else:
                pass
        elif lucky == 1:
            self.meili = self.makelucky/3 + renpy.random.randint(-100,200)
            if self.meili >950:
                self.meili = 950
            else:
                pass
            self.qizhi = (self.makelucky-self.meili)/2 + renpy.random.randint(-100,200)
            if self.qizhi >950:
                self.qizhi = 950
            else:
                pass
            self.beauty = self.makelucky - self.meili - self.qizhi + renpy.random.randint(0,200)
            if self.beauty > 950:
                self.beauty = 950
            else:
                pass
        else :
            self.qizhi =self.makelucky/3 + renpy.random.randint(-100,200)
            if self.qizhi >950:
                self.qizhi = 950
            else:
                pass
            self.beauty = (self.makelucky-self.qizhi)/2 + renpy.random.randint(-100,200)
            if self.beauty > 950:
                self.beauty = 950
            else:
                pass
            self.meili = self.makelucky - self.qizhi - self.beauty + renpy.random.randint(0,200)
            if self.meili >950:
                self.meili = 950
            else:
                pass


    def Feizifamily(self):
        self.father = None
        self.jiazu = []
        lucky = renpy.random.randint(1, 60)
        if lucky < 10:
            self.familylocation = "义女"
        elif lucky < 30:
            self.familylocation = "庶女"
        else:
            self.familylocation = "嫡女"
        
        lucky = renpy.random.randint(1, 10)
        if lucky < 100:
            self.fatherduty = renpy.random.choice(['文官', '武将'])
        else:
            self.fatherduty = "内侍"
        
        if year == 1 and self != my:
            lucky = renpy.random.randint(0,20)
            if lucky == 0:
                self.familylevel = 12
                self.fatherduty = ""
                self.familylocation = renpy.random.choice(['嫡女', '庶女'])
                self.family = "原东宫侍女"
                return
            else:
                lucky = renpy.random.randint(0, 30)
        else :
            lucky = renpy.random.randint(1, 65)
        
        if lucky == 0:
            lucky = renpy.random.randint(0, 1)
            if lucky == 0:
                pass
            else:
                self.xing = renpy.random.choice(['阿史那', '赫连',"耶律","郁久闾"])
            self.name = self.xing + self.ming
            self.familylevel = 0
            self.fatherduty = "国王"
            self.familylocation = renpy.random.choice(['嫡女', '庶女'])
            self.family = "和亲公主"
            self.tags.append(tags_family[0])
        elif lucky > 0 and lucky <= 2:
            self.familylevel = 1
            self.family = "一品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 2 and lucky <= 5:
            self.familylevel = 2
            self.family = "二品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 5 and lucky <= 10:
            self.familylevel = 3
            self.family = "三品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 10 and lucky <= 18:
            self.familylevel = 4
            self.family = "四品" + self.fatherduty + self.familylocation
        elif lucky > 18 and lucky <= 30:
            self.familylevel = 5
            self.family = "五品" + self.fatherduty + self.familylocation
        elif lucky > 30 and lucky <= 40:
            self.familylevel = 6
            self.family = "六品" + self.fatherduty + self.familylocation
        elif lucky > 40 and lucky <= 48:
            self.familylevel = 7
            self.family = "七品" + self.fatherduty + self.familylocation
        elif lucky > 48 and lucky <= 55:
            self.familylevel = 8
            self.family = "八品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[2])
        elif lucky > 55 and lucky <= 60:
            self.familylevel = 9
            self.family = "九品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[2])
        elif lucky > 60 and lucky <= 64:
            self.familylevel = 10
            self.fatherduty = "富商"
            self.familylocation = '嫡女'
            self.family = "富商之女"
            self.tags.append(tags_family[2])
        elif lucky == 65:
            self.familylevel = 11
            self.fatherduty = "平民"
            self.familylocation = '嫡女'
            self.family = "平民之女"
            self.tags.append(tags_family[2])
        else:
            self.familylevel = 12
            self.fatherduty = ""
            self.familylocation = '嫡女'
            self.family = ""
        tempbool = False
        if 0 <= self.familylevel <= 7:
            templist =  NPC_fz_list
            if self in templist:
                templist.remove(self)
            
            for i in templist:
                if i.familylevel == self.familylevel and self.fatherduty == i.fatherduty :
                    if i.familylevel == 0:
                        lucky = renpy.random.randint(0, 4)
                    else:
                        lucky = renpy.random.randint(0, i.familylevel+4)
                    if lucky == 0 and i.father != "" and isinstance(i.father,NoneType) == False:
                        tempbool = True
                        self.father = i.father
                        temp = i.father
                        if self not in temp.feizi:
                            temp.feizi.append(self)
                        if i not in temp.feizi:
                            temp.feizi.append(i)
                        
                        
                        
                        
                        
                        for j in temp.feizi:
                            
                            for x in temp.feizi:
                                if x != j and x not in j.sisters:
                                    j.sisters.append(x)
                                if x != j and j not in x.sisters:
                                    x.sisters.append(j)
                        
                        self.xing = i.xing
                        self.father = i.father
                    i.name = i.xing + i.ming
                    self.name = self.xing +self.ming
                    break
                else:
                    pass
        
        if tempbool == False and self != my:
            Creat_Males(whose = self,how = 0)
    def Xiunvfamily(self):
        self.father = None
        self.jiazu = []
        lucky = renpy.random.randint(1, 60)
        if lucky < 10:
            self.familylocation = "义女"
        elif lucky < 30:
            self.familylocation = "庶女"
        else:
            self.familylocation = "嫡女"
        
        
        self.fatherduty = renpy.random.choice(['文官', '武将'])
        
        
        
        lucky = renpy.random.randint(1, 65)
        
        
        if lucky > 0 and lucky <= 2:
            self.familylevel = 1
            self.family = "一品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 2 and lucky <= 5:
            self.familylevel = 2
            self.family = "二品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 5 and lucky <= 10:
            self.familylevel = 3
            self.family = "三品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[1])
        elif lucky > 10 and lucky <= 18:
            self.familylevel = 4
            self.family = "四品" + self.fatherduty + self.familylocation
        elif lucky > 18 and lucky <= 30:
            self.familylevel = 5
            self.family = "五品" + self.fatherduty + self.familylocation
        elif lucky > 30 and lucky <= 40:
            self.familylevel = 6
            self.family = "六品" + self.fatherduty + self.familylocation
        elif lucky > 40 and lucky <= 48:
            self.familylevel = 7
            self.family = "七品" + self.fatherduty + self.familylocation
        elif lucky > 48 and lucky <= 55:
            self.familylevel = 8
            self.family = "八品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[2])
        elif lucky > 55 and lucky <= 60:
            self.familylevel = 9
            self.family = "九品" + self.fatherduty + self.familylocation
            self.tags.append(tags_family[2])
        elif lucky > 60 and lucky <= 64:
            self.familylevel = 10
            self.fatherduty = "富商"
            self.familylocation = '嫡女'
            self.family = "富商之女"
            self.tags.append(tags_family[2])
        elif lucky == 65:
            self.familylevel = 11
            self.fatherduty = "平民"
            self.familylocation = '嫡女'
            self.family = "平民之女"
            self.tags.append(tags_family[2])
        else:
            self.familylevel = 12
            self.fatherduty = ""
            self.familylocation = ''
            self.family = ""
        tempbool = False
        if 0 <= self.familylevel <= 7:
            templist =  NPC_fz_list
            if self in templist:
                templist.remove(self)
            for i in templist:
                if i.familylevel == self.familylevel and self.fatherduty == i.fatherduty:
                    if i.familylevel == 0:
                        lucky = renpy.random.randint(0, 5)
                    else:
                        lucky = renpy.random.randint(0, i.familylevel+3)
                    if lucky == 0 and i.father != "" and isinstance(i.father,NoneType) == False:
                        tempbool = True
                        self.father = i.father
                        temp = i.father
                        if self not in temp.feizi:
                            temp.feizi.append(self)
                        if self not in i.sisters:
                            i.sisters.append(self)
                        if i not in self.sisters:
                            self.sisters.append(i)
                        
                        for j in i.sisters:
                            if j not in self.sisters and j != i and j != self:
                                self.sisters.append(j)
                        
                        self.xing = i.xing
                        self.father = i.father
                    i.name = i.xing + i.ming
                    self.name = self.xing +self.ming
                    break
                else:
                    pass




    def randomtags(self):
        tagslist = [tags_limit_beauty,tags_limit_qizhi,tags_limit_meili,tags_limit_health,tags_limit_lucky,tags_limit_xinji,tags_shuxing,tags_caiyi,tags_xingge,tags_xihao]
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            pass
        else:
            temptaglist = renpy.random.choice(tagslist)
            temptag = renpy.random.choice(temptaglist)
            self.tags.append(temptag)
            tagslist.remove(temptaglist)
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            pass
        else:
            temptaglist = renpy.random.choice(tagslist)
            temptag = renpy.random.choice(temptaglist)
            self.tags.append(temptag)
            tagslist.remove(temptaglist)
        lucky = renpy.random.randint(0, 1)
        if lucky == 0:
            pass
        else:
            temptaglist = renpy.random.choice(tagslist)
            temptag = renpy.random.choice(temptaglist)
            self.tags.append(temptag)
            tagslist.remove(temptaglist)



    def Feizilevel0(self):
        a = 0
        if weifen_list[0][5] == 0 :
            self.exp = yuanweifen[0][3]*renpy.random.randint(105, 140)*0.01
            self.level = weifen_list[0][0]
            self.weifen = weifen_list[0][1]
            weifen_list[0][5] = 1
        
        else:
            while self.exp < weifen_list[a][3]:
                a = a + 1
            
            
            while weifen_list[a][5]+1 > weifen_list[a][2] :
                a = a + 1
            
            weifen_list[a][5] = weifen_list[a][5] + 1
            self.level = weifen_list[a][0]
            self.weifen = weifen_list[a][1]
        
        weifenzu_del(self)
        self.paixu = beifei - self.level
        
        return self.weifen
        return weifen_list[0][5]
        return weifen_list[a][5]

    def Feizilevel_xuanxiu(self):
        global weifen_list
        NPC_fz_list.append(self)
        a = 0
        
        while self.exp < weifen_list[a][3]:
            a = a + 1
        
        
        while weifen_list[a][5]+1 > weifen_list[a][2] :
            a = a + 1
        
        weifen_list[a][5] = weifen_list[a][5] + 1
        self.level = weifen_list[a][0]
        self.weifen = weifen_list[a][1]
        weifenzu_del(self)
        self.paixu = beifei - self.level
        self.story = []
        lucky = renpy.random.randint(0, 12)
        randompalace(self)
        ChangeGongnv(self)
        
        if self.hao == "":
            tempstory = str(nianhao)+str(year)+"年，经由选秀入宫，册为"+str(self.weifen)+"。\n"
            self.story.append(tempstory)
        else:
            tempstory = str(nianhao)+str(year)+"年，经由选秀入宫，册为"+str(self.hao)+str(self.weifen)+"。\n"
            self.story.append(tempstory)
        if self.hao =="":
            self.cheng = self.xing +self.weifen
        else:
            self.cheng = self.hao +self.weifen
        if diwei(self) <= 1:
            self.tequan1 = 6
        
        return self.weifen
        return weifen_list[0][5]
        return weifen_list[a][5]




    def Feizilevel_first(self):
        global weifen_list
        a = 0
        
        while self.exp < weifen_list[a][3]:
            a = a + 1
        
        
        while weifen_list[a][5]+1 > weifen_list[a][2] :
            a = a + 1
        
        weifen_list[a][5] = weifen_list[a][5] + 1
        self.level = weifen_list[a][0]
        self.weifen = weifen_list[a][1]
        weifenzu_del(self)
        self.paixu = beifei - self.level
        self.story = []
        lucky = renpy.random.randint(0, 12)
        if self.level == 0:
            tempstory = "原东宫太子妃。\n"+str(nianhao)+"元年立为正宫皇后。\n"
            self.story.append(tempstory)
        elif self.familylevel == 0:
            tempstory = str(nianhao)+"元年和亲入宫。\n"+str(nianhao)+str(year)+"年，为"+str(self.hao)+str(self.weifen)+"。\n"
            self.story.append(tempstory)
        elif self.level < 3:
            tempstory = "原东宫太子侧妃。\n"+str(nianhao)+str(year)+"年，为"+str(self.hao)+str(self.weifen)+"。\n"
            self.story.append(tempstory)
        elif lucky == 0 and self.familylevel < 5:
            tempstory = str(nianhao)+"元年由太后举荐入宫。\n"+str(nianhao)+str(year)+"年，为"+str(self.hao)+str(self.weifen)+"。\n"
            self.taihoulike = 60 + renpy.random.randint(0, 30)
            self.story.append(tempstory)
        else :
            tempstory ="原东宫太子侍妾。\n"+str(nianhao)+str(year)+"年，为"+str(self.hao)+str(self.weifen)+"。\n"
            self.story.append(tempstory)
        if self.hao =="":
            self.cheng = self.xing +self.weifen
        else:
            self.cheng = self.hao +self.weifen
        randompalace(self)
        ChangeGongnv(self)
        if diwei(self) <= 1:
            self.tequan1 = 6
        
        return self.weifen
        return weifen_list[0][5]
        return weifen_list[a][5]

    def Feizilevel(self):
        global weifen_list
        a = 0
        
        while self.exp < weifen_list[a][3]:
            a = a + 1
        
        
        while weifen_list[a][5]+1 > weifen_list[a][2] :
            a = a + 1
        
        weifen_list[a][5] = weifen_list[a][5] + 1
        self.level = weifen_list[a][0]
        self.weifen = weifen_list[a][1]
        weifenzu_del(self)
        self.paixu = beifei - self.level
        
        return self.weifen
        return weifen_list[0][5]
        return weifen_list[a][5]


    def shuxingmiaoshu(self):
        
        if self.health >900:
            self.healthlv = "{color=#FF3030}强韧{/color}"
        elif self.health >700:
            self.healthlv = "{color=#EE00EE}强健{/color}"
        elif self.health >400:
            self.healthlv = "{color=#0040FF}康健{/color}"
        elif self.health >200:
            self.healthlv = "{color=#008000}无恙{/color}"
        elif self.health >100:
            self.healthlv = "{color=#2F4F4F}娇弱{/color}"
        else:
            self.healthlv = "{color=#A1A1A1}孱弱{/color}"
        
        if self.beauty >900:
            self.beautylv = "{color=#FF3030}绝世{/color}"
        elif self.beauty >700:
            self.beautylv = "{color=#EE00EE}国色{/color}"
        elif self.beauty >400:
            self.beautylv = "{color=#0040FF}花颜{/color}"
        elif self.beauty >200:
            self.beautylv = "{color=#008000}端美{/color}"
        elif self.beauty >100:
            self.beautylv = "{color=#2F4F4F}清秀{/color}"
        else:
            self.beautylv = "{color=#A1A1A1}寻常{/color}"
        
        if self.qizhi >900:
            self.qizhilv = "{color=#FF3030}仙姿{/color}"
        elif self.qizhi >700:
            self.qizhilv = "{color=#EE00EE}出尘{/color}"
        elif self.qizhi >400:
            self.qizhilv = "{color=#0040FF}脱俗{/color}"
        elif self.qizhi >200:
            self.qizhilv = "{color=#008000}优雅{/color}"
        elif self.qizhi >100:
            self.qizhilv = "{color=#2F4F4F}端庄{/color}"
        else:
            self.qizhilv = "{color=#A1A1A1}庸俗{/color}"
        
        if self.meili >900:
            self.meililv = "{color=#FF3030}媚绝{/color}"
        elif self.meili >700:
            self.meililv = "{color=#EE00EE}尤物{/color}"
        elif self.meili >400:
            self.meililv = "{color=#0040FF}窈窕{/color}"
        elif self.meili >200:
            self.meililv = "{color=#008000}娉婷{/color}"
        elif self.meili >100:
            self.meililv = "{color=#2F4F4F}可人{/color}"
        else:
            self.meililv = "{color=#A1A1A1}平淡{/color}"
        
        if self.dance > 80:
            self.dancelv = "{color=#FF3030}炉火纯青{/color}"
        elif self.dance > 50:
            self.dancelv = "{color=#EE00EE}精通{/color}"
        elif self.dance > 30:
            self.dancelv = "{color=#0040FF}擅长{/color}"
        elif self.dance > 15:
            self.dancelv = "{color=#008000}上手{/color}"
        elif self.dance > 5:
            self.dancelv = "{color=#2F4F4F}入门{/color}"
        else:
            self.dancelv = "{color=#A1A1A1}不入门{/color}"
        
        if self.book > 80:
            self.booklv = "{color=#FF3030}炉火纯青{/color}"
        elif self.book > 50:
            self.booklv = "{color=#EE00EE}精通{/color}"
        elif self.book > 30:
            self.booklv = "{color=#0040FF}擅长{/color}"
        elif self.book > 15:
            self.booklv = "{color=#008000}上手{/color}"
        elif self.book > 5:
            self.booklv = "{color=#2F4F4F}入门{/color}"
        else:
            self.booklv = "{color=#A1A1A1}不入门{/color}"
        
        if self.cixiu > 80:
            self.cixiulv = "{color=#FF3030}炉火纯青{/color}"
        elif self.cixiu > 50:
            self.cixiulv = "{color=#EE00EE}精通{/color}"
        elif self.cixiu > 30:
            self.cixiulv = "{color=#0040FF}擅长{/color}"
        elif self.cixiu > 15:
            self.cixiulv = "{color=#008000}上手{/color}"
        elif self.cixiu > 5:
            self.cixiulv = "{color=#2F4F4F}入门{/color}"
        else:
            self.cixiulv = "{color=#A1A1A1}不入门{/color}"
        
        if self.muzic > 80:
            self.muziclv = "{color=#FF3030}炉火纯青{/color}"
        elif self.muzic > 50:
            self.muziclv = "{color=#EE00EE}精通{/color}"
        elif self.muzic > 30:
            self.muziclv = "{color=#0040FF}擅长{/color}"
        elif self.muzic > 15:
            self.muziclv = "{color=#008000}上手{/color}"
        elif self.muzic > 5:
            self.muziclv = "{color=#2F4F4F}入门{/color}"
        else:
            self.muziclv = "{color=#A1A1A1}不入门{/color}"
        
        if self.medic > 80:
            self.mediclv = "{color=#FF3030}炉火纯青{/color}"
        elif self.medic > 50:
            self.mediclv = "{color=#EE00EE}精通{/color}"
        elif self.medic > 30:
            self.mediclv = "{color=#0040FF}擅长{/color}"
        elif self.medic > 15:
            self.mediclv = "{color=#008000}上手{/color}"
        elif self.medic > 5:
            self.mediclv = "{color=#2F4F4F}入门{/color}"
        else:
            self.mediclv = "{color=#A1A1A1}不入门{/color}"
        
        
        
        
        
        if self.like == 999:
            self.likelv = "——"
        elif self.like > 80:
            self.likelv = "{color=#FF3030}倾情{/color}"
        elif self.like > 50:
            self.likelv = "{color=#EE00EE}知心{/color}"
        elif self.like > 25:
            self.likelv = "{color=#0040FF}喜爱{/color}"
        elif self.like > 10:
            self.likelv = "{color=#008000}和睦{/color}"
        elif self.like >= 0:
            self.likelv = "{color=#2F4F4F}陌路{/color}"
        elif self.like >-20:
            self.likelv = "{color=#A1A1A1}厌恶{/color}"
        else:
            self.likelv = "{color=#000000}憎恶{/color}"
        
        if self.love > 80:
            self.lovelv = "{color=#FF3030}专宠{/color}"
        elif self.love > 50:
            self.lovelv = "{color=#EE00EE}盛宠{/color}"
        elif self.love > 25:
            self.lovelv = "{color=#0040FF}受宠{/color}"
        elif self.love > 10:
            self.lovelv = "{color=#008000}小宠{/color}"
        elif self.love >= -1:
            self.lovelv = "{color=#2F4F4F}无宠{/color}"
        elif self.love >= -20:
            self.lovelv = "{color=#A1A1A1}厌烦{/color}"
        else:
            self.lovelv = "{color=#000000}憎恶{/color}"
        
        if self.xinji1 == False:
            self.xinjilv = "未知"
        elif self.xinji >900:
            self.xinjilv = "{color=#FF3030}莫测{/color}"
        elif self.xinji >700:
            self.xinjilv = "{color=#EE00EE}高深{/color}"
        elif self.xinji >400:
            self.xinjilv = "{color=#0040FF}善谋{/color}"
        elif self.xinji >200:
            self.xinjilv = "{color=#008000}世故{/color}"
        elif self.xinji >100:
            self.xinjilv = "{color=#2F4F4F}直率{/color}"
        else:
            self.xinjilv = "{color=#A1A1A1}单纯{/color}"



    def Feizishengjiang(self):
        pretext = str(self.hao)+str(self.weifen)+str(self.name)
        b = int(self.level)
        global pretext
        global yetinghao
        global temptext
        global NPC_fz_feilist
        if b < 0 :
            pass
        
        else:
            a = beifei
            while self.exp > weifen_list[a][4] and a > 0 :
                a = a - 1
            
            
            if a == self.level:
                pass
            
            elif a < self.level and self.shiqin > 0 or b == beifei:
                while weifen_list[a][5] == weifen_list[a][2] :
                    a = a + 1
                if a >= self.level:
                    pass
                else:
                    self.yali -= 15
                    if self.level > 0 and a == 0 and self.love > -20:
                        weifenzu_add(self)
                        temptext = str("被立为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                        Changeqinju(self)
                        self.tequan1 = 0
                        renpy.call("立后事件",self = self,from_current=False)
                    
                    elif b == beifei or self in NPC_fz_feilist:
                        weifenzu_add(self)
                        temptext = str("被接出冷宫，册为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        self.jinzu = 0
                        weifenzu_del(self)
                        randompalace(self)
                        if self not in NPC_fz_list:
                            NPC_fz_list.append(self)
                        else:
                            pass
                        if self in NPC_fz_feilist:
                            NPC_fz_feilist.remove(self)
                        else:
                            pass
                        ChangeGongnv(self)
                        if self.level < 4:
                            self.tequan1 = 0
                        else:
                            pass
                    
                    elif self.level > 3 and a < 4 :
                        self.tequan1 = 0
                        weifenzu_add(self)
                        
                        temptext = str("晋为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                        
                        Changeqinju(self)
                        randompalace(self)
                    
                    else:
                        weifenzu_add(self)
                        temptext = str("晋为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                    
                    ChangeGongnv(self)
                    if self.hao =="":
                        self.cheng = self.xing + self.weifen
                    else:
                        self.cheng = self.hao +self.weifen
                    
                    if self.hao == "":
                        if self.level == 0 or self.love > 80:
                            lucky = renpy.random.randint(0, 1)
                        elif self.level < 3 or self.love > 50:
                            lucky = renpy.random.randint(0, 1)
                        elif self.level < 8 or self.love > 30:
                            lucky = renpy.random.randint(0, 2)
                        else:
                            lucky = renpy.random.randint(0, 3)
                        if self == my and yetinghao != "":
                            lucky = 0
                        else:
                            pass
                        if lucky == 0:
                            if yetinghao != ""  and self == my:
                                self.hao = yetinghao
                                yetinghao = ""
                            else:
                                self.hao = renpy.random.choice(hao_list)
                                hao_list.remove(self.hao)
                                lucky = renpy.random.randint(0, 10)
                                if lucky == 0 and self.love >= 10:
                                    temphao = renpy.random.choice(hao_list)
                                    hao_list.remove(temphao)
                                    self.hao += temphao
                                else:
                                    pass
                            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"，赐号"+str(self.hao)+"。\n"
                            tempstory2 ="【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext  +temptext+str(self.weifen)+"，赐号"+str(self.hao)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            gongxi.append([self,"晋位"])
                            if self == my:
                                renpy.call("主角晋位赐号",from_current=False)
                            else :
                                pass
                        else :
                            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"。\n"
                            tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.weifen)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            gongxi.append([self,"晋位"])
                            if self == my:
                                renpy.call("主角晋位",from_current=False)
                            else :
                                pass
                    else :
                        lucky = renpy.random.randint(0, 20)
                        if self == my and yetinghao != "":
                            lucky = 0
                        else:
                            pass
                        if lucky == 0:
                            temphao = self.hao
                            if yetinghao != "" and self == my:
                                if len(self.hao) >= 2:
                                    for i in self.hao:
                                        hao_list.append(i)
                                else:
                                    hao_list.append(self.hao)
                                self.hao = yetinghao
                                yetinghao = ""
                            else:
                                self.hao = renpy.random.choice(hao_list)
                                hao_list.remove(self.hao)
                                if len(temphao) >= 2:
                                    for i in temphao:
                                        hao_list.append(i)
                                else:
                                    hao_list.append(temphao)
                                lucky = renpy.random.randint(0, 10)
                                if lucky == 0 and self.love >= 20:
                                    temphao = renpy.random.choice(hao_list)
                                    hao_list.remove(temphao)
                                    self.hao += temphao
                                else:
                                    pass
                            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"，改号"+str(self.hao)+"。\n"
                            tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.weifen)+"，改号"+str(self.hao)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            gongxi.append([self,"晋位"])
                            if self == my:
                                renpy.call("主角晋位改号",from_current=False)
                            else :
                                pass
                        
                        else :
                            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.hao)+str(self.weifen)+"。\n"
                            tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.hao)+str(self.weifen)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            gongxi.append([self,"晋位"])
                            if self == my:
                                renpy.call("主角晋位",from_current=False)
                            else :
                                pass
                    if b == beifei :
                        renpy.call("有人出冷宫了",fz = self,from_current=False)
                    else:
                        pass
            
            
            else:
                pass
            a = 0
            while self.exp < weifen_list[a][3] and a < beifei:
                a = a + 1
            
            if a == self.level:
                pass
            elif self.level == beifei:
                pass
            elif huaiyun(self) == True:
                pass
            
            elif a > self.level :
                
                
                while weifen_list[a][5] == weifen_list[a][2] :
                    a = a + 1
                
                
                if a <= self.level:
                    pass
                else:
                    self.yali += 15
                    
                    
                    
                    
                    if self.level == 0 and a > 0 and a != beifei:
                        weifenzu_add(self)
                        temptext = str("被废去皇后之位，居")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                        randompalace(self)
                        renpy.call("废后事件",self = self,from_current=False)
                    else:
                        pass
                    if a == beifei and huaiyun(self) == False :
                        temptext = str("被打入冷宫，废为")
                        weifenzu_add(self)
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                        if self.hao == "":
                            pass
                        else:
                            if len(self.hao) >= 2:
                                for i in self.hao:
                                    hao_list.append(i)
                            else:
                                hao_list.append(self.hao)
                            self.hao = ""
                        
                        if self == my:
                            my.Gongnv = sorted(my.Gongnv, key=attrgetter("like"),reverse = True)
                            tempfz = my.Gongnv[0]
                            for i in self.Gongnv:
                                if i != tempfz:
                                    self.Gongnv.remove(i)
                                    YTGongnv.append(i)
                                else:
                                    pass
                        
                        else:
                            for i in self.Gongnv:
                                self.Gongnv.remove(i)
                                YTGongnv.append(i)
                        
                        Changeqinju(self)
                        randompalace(self)
                        NPC_fz_list.remove(self)
                        NPC_fz_feilist.append(self)
                    elif self.level < 4 and a > 3 :
                        weifenzu_add(self)
                        temptext = str("贬为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                        Changeqinju(self)
                        randompalace(self)
                    else:
                        weifenzu_add(self)
                        temptext = str("降为")
                        weifen_list[b][5] = weifen_list[b][5]-1
                        weifen_list[a][5] = weifen_list[a][5]+1
                        self.level = weifen_list[a][0]
                        self.weifen = weifen_list[a][1]
                        weifenzu_del(self)
                    
                    
                    ChangeGongnv(self)
                    
                    if self.hao == "":
                        tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.weifen)+"。\n"
                        tempstory2 ="【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext + temptext +str(self.weifen)+"。\n"
                        self.story.append(tempstory)
                        allstory.insert(0,tempstory2)
                        xiluo.append([self,"降位"])
                        if self == my and my.level == beifei :
                            renpy.call("有人被打入冷宫",fz = self,from_current=False)
                        elif  self == my:
                            renpy.call("主角降位",from_current=False)
                        else :
                            pass
                    else :
                        lucky = renpy.random.randint(0, 5)
                        if a == beifei:
                            lucky == 0
                        else:
                            pass
                        if lucky == 0:
                            if len(self.hao) >= 2:
                                for i in self.hao:
                                    hao_list.append(i)
                            else:
                                hao_list.append(self.hao)
                            self.hao = ""
                            tempstory = str(year)+"年"+str(month)+"月，褫夺封号，"+temptext+str(self.weifen)+"。\n"
                            tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext + "被褫夺封号，"+temptext+str(self.weifen)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            xiluo.append([self,"降位"])
                            if self == my and my.level == beifei :
                                renpy.call("有人被打入冷宫",fz = self,from_current=False)
                            elif self == my:
                                renpy.call("主角降位去号",from_current=False)
                            else :
                                pass
                        
                        else :
                            tempstory = str(year)+"年"+str(month)+"月，"+temptext+str(self.hao) + str(self.weifen)+"。\n"
                            tempstory2 = "【圣旨】"+str(year)+"年"+str(month)+"月，"+ pretext +temptext+str(self.hao) + str(self.weifen)+"。\n"
                            self.story.append(tempstory)
                            allstory.insert(0,tempstory2)
                            xiluo.append([self,"降位"])
                            if self == my and my.level == beifei :
                                renpy.call("有人被打入冷宫",fz = self,from_current=False)
                            elif self == my:
                                renpy.call("主角降位",from_current=False)
                            else :
                                pass
                    if self.hao =="":
                        self.cheng = self.xing +self.weifen
                    else:
                        self.cheng = self.hao +self.weifen
                    if a == beifei and huaiyun(self) == False:
                        renpy.call("有人被打入冷宫",fz = self,from_current=False)
                    else:
                        pass
            
            
            
            self.paixu = beifei - self.level
            
            return self

    def deletexiunv(self):
        a = self.level
        weifen_list[a][5] = weifen_list[a][5] -1
        weifenzu_add(self)
        if self in NPC_fz_list:
            NPC_fz_list.remove(self)
        elif self in NPC_fz_feilist:
            NPC_fz_feilist.remove(self)
        else:
            pass
        if self.level == 0 or self.level == beifei:
            pass
        else:
            if self.palacenum == -1:
                pass
            else:
                palaces[self.palacenum][0][1] = palaces[self.palacenum][0][1] - 1
                palaces[self.palacenum][self.qinjunum][1] = ""
                if self.qinjunum == 1:
                    shengyuzhengdian_list.append(self.palacenum)
                else:
                    tempnum = 0
                    for j in palaces[self.palacenum][2:]:
                        if str(j[1]) == "":
                            tempnum += 1
                        else:
                            pass
                    if tempnum > 0 and self.palacenum not in shengyucedian_list:
                        shengyucedian_list.append(self.palacenum)
                    else:
                        pass
        
        if self.hao != "":
            if len(self.hao) >= 2:
                for i in self.hao:
                    hao_list.append(i)
            else:
                hao_list.append(self.hao)
        else:
            pass
        for i in self.Gongnv:
            self.Gongnv.remove(i)
        for i in NPC_fz_list:
            if self in i.foes:
                i.foes.remove(self)
            elif self in i.friends:
                i.friends.remove(self)
            else:
                pass
        for i in NPC_fz_feilist:
            if self in i.foes:
                i.foes.remove(self)
            elif self in i.friends:
                i.friends.remove(self)
            else:
                pass

    def Killfz(self):
        global NPC_fz_list
        global NPC_fz_fellist
        global NPC_fz_dielist
        a = self.level
        weifen_list[a][5] = weifen_list[a][5] -1
        self.story.append(tempstory)
        allstory.insert(0,tempstory2)
        weifenzu_add(self)
        if self in NPC_fz_list:
            NPC_fz_list.remove(self)
        elif self in NPC_fz_feilist:
            NPC_fz_feilist.remove(self)
        else:
            pass
        NPC_fz_dielist.append(self)
        if self.level == 0 or self.level == beifei:
            pass
        else:
            palaces[self.palacenum][0][1] = palaces[self.palacenum][0][1] - 1
            palaces[self.palacenum][self.qinjunum][1] = ""
            if self.qinjunum == 1:
                shengyuzhengdian_list.append(self.palacenum)
            else:
                tempnum = 0
                for j in palaces[self.palacenum][2:]:
                    if str(j[1]) == "":
                        tempnum += 1
                    else:
                        pass
                if tempnum > 0 and self.palacenum not in shengyucedian_list:
                    shengyucedian_list.append(self.palacenum)
                else:
                    pass
        for i in self.Gongnv:
            self.Gongnv.remove(i)
            YTGongnv.append(i)
        for i in NPC_fz_list:
            if self in i.foes:
                i.foes.remove(self)
            elif self in i.friends:
                i.friends.remove(self)
            else:
                pass
        for i in NPC_fz_feilist:
            if self in i.foes:
                i.foes.remove(self)
            elif self in i.friends:
                i.friends.remove(self)
            else:
                pass
        
        return NPC_fz_list
        return NPC_fz_feilist
        return NPC_fz_dielist

    def Changeqinju(self):
        if self.palacenum == -1 or self.palacenum  == 999:
            pass
        else:
            palaces[self.palacenum][0][1] = palaces[self.palacenum][0][1] - 1
            palaces[self.palacenum][self.qinjunum][1] = ""
            if self.qinjunum == 1:
                shengyuzhengdian_list.append(self.palacenum)
            else :
                tempnum = 0
                for j in palaces[self.palacenum][2:]:
                    if str(j[1]) == "":
                        tempnum += 1
                    else:
                        pass
                if tempnum <= 0 and self.palacenum in shengyucedian_list:
                    shengyucedian_list.remove(self.palacenum)
                else:
                    pass
        if self.level == 0:
            
            self.palace = "凤仪宫"
            self.palacenum = 999
            self.qinjunum = 999
            self.qinju = ""

    def ChangeGongnv(self):
        self.Gongnv = sorted(self.Gongnv, key=attrgetter("lv"),reverse = False)
        
        a = len(yuanweifen)
        if self.level == 0: 
            yingyougn = [1,1,2,2,4]
            if len(self.Gongnv) > 0:
                self.Gongnv[0].level = "长御"
                self.Gongnv[0].lv = 0
                if len(self.Gongnv) < 10:
                    a = 10 - len(self.Gongnv)
                    makeGongnv(self,a,"宫女","女官")
                for i in self.Gongnv[1:]:
                    i.lv = 1
                    i.level = "女官"
            else:
                if len(self.Gongnv) < 10:
                    a = 10 - len(self.Gongnv)
                    makeGongnv(self,a,"宫女","长御")
                for i in self.Gongnv:
                    i.lv = 0
                    i.level = "长御"
            
            
            self.Gongnv = sorted(self.Gongnv, key=attrgetter("lv"),reverse = False)
        elif self.qinjunum == 1: 
            yingyougn = [0,1,1,2,3]
            if len(self.Gongnv) < 7:
                a = 7 - len(self.Gongnv)
                makeGongnv(self,a,"宫女","女官")
            for i in self.Gongnv:
                i.lv = 1
                i.level = "女官"
        elif self.level > round(a-a/3):
            yingyougn = [0,0,0,1,1]
            if len(self.Gongnv) < 2:
                a = 2 - len(self.Gongnv)
                makeGongnv(self,a,"宫女","贴身侍女")
            for i in self.Gongnv:
                i.lv = 0
                i.level = "贴身侍女"
        else:
            yingyougn = [0,0,1,1,2]
            if len(self.Gongnv) < 4:
                a = 4 - len(self.Gongnv)
                makeGongnv(self,a,"宫女","大宫女")
            for i in self.Gongnv:
                i.lv = 2
                i.level = "大宫女"
        
        templist = []
        for i in self.Gongnv:
            if i.lv == 0:
                templist.append(i)
            else:
                pass
        if len(templist)< yingyougn[0]:
            a = yingyougn[0] - len(templist)
            makeGongnv(self,a,"宫女","长御")
        elif len(templist)> yingyougn[0]:
            for i in templist[yingyougn[0]:]:
                i.level = "女官"
                i.lv = 1
        else:
            pass
        
        templist = []
        for i in self.Gongnv:
            if i.lv == 1:
                templist.append(i)
            else:
                pass
        if len(templist)< yingyougn[1]:
            a = yingyougn[1] - len(templist)
            makeGongnv(self,a,"宫女","女官")
        elif len(templist)> yingyougn[1]:
            for i in templist[yingyougn[1]:]:
                i.level = "大宫女"
                i.lv = 2
        else:
            pass
        
        templist = []
        for i in self.Gongnv:
            if i.lv == 2:
                templist.append(i)
            else:
                pass
        if len(templist)< yingyougn[2]:
            a = yingyougn[2] - len(templist)
            makeGongnv(self,a,"宫女","大宫女")
        elif len(templist)> yingyougn[2]:
            for i in templist[yingyougn[2]:]:
                i.level = "贴身侍女"
                i.lv = 3
        else:
            pass
        
        templist = []
        for i in self.Gongnv:
            if i.lv == 3:
                templist.append(i)
            else:
                pass
        if len(templist)< yingyougn[3]:
            a = yingyougn[3] - len(templist)
            makeGongnv(self,a,"宫女","贴身侍女")
        elif len(templist)> yingyougn[3]:
            for i in templist[yingyougn[3]:]:
                i.level = "婢子"
                i.lv = 4
        else:
            pass
        
        templist = []
        for i in self.Gongnv:
            if i.lv == 4:
                templist.append(i)
            else:
                pass
        if len(templist)< yingyougn[4]:
            a = yingyougn[4] - len(templist)
            makeGongnv(self,a,"宫女","婢子")
        elif len(templist)> yingyougn[4]:
            for i in templist[yingyougn[4]:]:
                i.level = "散役"
                i.lv = 5
        else:
            pass






    def huaiyun(self):
        temptag = ""
        for i in self.tags:
            if "身怀皇嗣" in i:
                temptag = "有孕"
            
            else:
                pass
        if temptag == "有孕":
            return True
        else:
            return False

    def jinzu(self):
        temptag = ""
        for i in self.tags:
            if "禁足一月" in i:
                temptag = "禁足"
            elif "禁足三月" in i:
                temptag = "禁足"
            elif "禁足半年" in i:
                temptag = "禁足"
            else:
                pass
        if temptag == "禁足":
            return True
        else:
            return False

    def fengfei(self):
        temptag = 0
        for i in self.tags:
            if "失心成疯" in i:
                temptag = 1
            else:
                pass
        if temptag == 1:
            return True
        else:
            return False

    def yuli(self): 
        temptext = "有"
        for i in zysj_ready:
            if i.zhu == self:
                temptext = "无"
            else:
                pass
        
        if temptext == "有":
            return True
        else:
            return False

    def havetag(what,self):
        temptag = ""
        for i in self.tags:
            if what in i:
                temptag = "有"
            else:
                pass
        if temptag == "有":
            return True
        else:
            return False

    def tags_buff(self):
        
        if havetag("天生丽质",self) == True :
            self.beauty += 100
        elif havetag("桃花人面",self) == True :
            self.beauty += 50
        
        else:
            pass
        
        if havetag("谪仙降世",self) == True :
            self.qizhi+= 100
        elif havetag("冰肌玉骨",self) == True :
            self.qizhi+= 50
        else:
            pass
        
        if havetag("祸水红颜",self) == True :
            self.meili += 100
        elif havetag("风情万种",self) == True :
            self.meili += 50
        else:
            pass
        
        if havetag("智绝无双",self) == True :
            self.xinji += 100
        elif havetag("思虑入微",self) == True :
            self.xinji += 50
        elif havetag("心浮气躁",self) == True :
            self.xinji -= 50
        elif havetag("意气用事",self) == True :
            self.xinji -= 100
        else:
            pass
        
        if havetag("洪福齐天",self) == True :
            self.lucky += 20
        else:
            pass
        
        
        if havetag("先天弱症",self) == True :
            self.health -= 100
        elif havetag("弱柳扶风",self) == True :
            self.health -= 50
        else:
            pass
        
        if havetag("肤若凝脂",self) == True:
            self.beauty += 50
        if havetag("吐气如兰",self) == True:
            self.qizhi += 50
        if havetag("拥雪成峰",self) == True:
            self.meili += 50
        if havetag("眸若桃花",self) == True:
            self.meili += 25
            self.beauty += 25
        if havetag("青丝三千",self) == True:
            self.qizhi += 25
            self.beauty += 25
        if havetag("红袖添香",self) == True:
            self.meili += 25
            self.qizhi += 25

    def tags_NPCyangcheng(self):
        NPC_Skill_Fenpei(self)
        if self.meishu["初始"] == 1:
            self.meili += 0.15
            lucky = renpy.random.randint(0,1)
            if lucky == 0:
                self.muzic += 0.15
            else:
                self.dance += 0.15
        if self.meishu["初始"] == 2:
            self.meili += 0.3
            lucky = renpy.random.randint(0,1)
            if lucky == 0:
                self.muzic += 0.3
            else:
                self.dance += 0.3
        if self.meishu["初始"] == 3:
            self.meili += 0.5
            lucky = renpy.random.randint(0,1)
            if lucky == 0:
                self.muzic += 0.5
            else:
                self.dance += 0.5
        
        if self.fangyu["初始"] == 1:
            self.book += 0.1
            self.xinji += 0.1
        if self.fangyu["初始"] == 2:
            self.book += 0.2
            self.xinji += 0.2
        if self.fangyu["初始"] == 3:
            self.book += 0.3
            self.xinji += 0.3
        
        
        if havetag("天生丽质",self) == True :
            self.beauty += renpy.random.randint(0,3)*0.02
        elif havetag("桃花人面",self) == True :
            self.beauty += renpy.random.randint(0,2)*0.02
        elif havetag("明眸皓齿",self) == True :
            self.beauty += renpy.random.randint(0,1)*0.02
        else:
            pass
        
        if havetag("谪仙降世",self) == True :
            self.qizhi+= renpy.random.randint(0,3)*0.02
        elif havetag("冰肌玉骨",self) == True :
            self.qizhi+= renpy.random.randint(0,2)*0.02
        elif havetag("清姿隽逸",self) == True :
            self.qizhi+= renpy.random.randint(0,1)*0.02
        else:
            pass
        
        if havetag("祸水红颜",self) == True :
            self.meili += renpy.random.randint(0,3)*0.02
        elif havetag("风情万种",self) == True :
            self.meili += renpy.random.randint(0,2)*0.02
        elif havetag("仪态万千",self) == True :
            self.meili += renpy.random.randint(0,1)*0.02
        else:
            pass
        
        if havetag("身姿曼妙",self) == True :
            self.dance += renpy.random.randint(0,20)*0.1
            self.meili+= renpy.random.randint(0,15)*0.02
        if havetag("声如莺啼",self) == True :
            self.muzic += renpy.random.randint(0,20)*0.1
            self.qizhi+= renpy.random.randint(0,15)*0.02
        if havetag("耳聪目明",self) == True :
            self.book += renpy.random.randint(0,20)*0.2
        if havetag("心细手巧",self) == True :
            self.cixiu += renpy.random.randint(0,20)*0.1
        
        if havetag("生性懒惰",self) == True :
            if self.health <= 800:
                self.health += 0.5
        if havetag("夙兴夜寐",self) == True :
            if self.health > 200:
                self.health -= 0.5
        
        if havetag("嗜甜之人",self) == True :
            if self.health <= 800:
                self.health += 0.5
            if self.beauty > 200:
                self.beauty -= 0.5
        if havetag("喜食辛辣",self) == True :
            if self.health > 200:
                self.health -= 0.5
            if self.beauty <= 800:
                self.beauty += 0.5


    def tags_limitcheck(self):
        if havetag("失心成疯",self) == True :
            if self.exp >= yuanweifen[1][4]:
                self.exp = yuanweifen[1][4]
            else:
                pass
            if self.qizhi >=100:
                self.qizhi = 100
            if self.meili >= 100:
                self.meili = 100
            if self.xinji != 0:
                self.xinji = 0
            if self.yali != 0:
                self.yali == 0
        
        if havetag("和亲公主",self) == True and self.exp >= yuanweifen[1][4]:
            self.exp = yuanweifen[1][4]
        elif havetag("小家碧玉",self) == True and self.exp >= yuanweifen[0][3]*(0.5 + self.year*0.1):
            self.exp = yuanweifen[0][3]*(0.5 + self.year*0.1)
        elif havetag("宫女上位",self) == True and self.exp >= yuanweifen[0][3]*(0.2 + self.year*0.1):
            self.exp = yuanweifen[0][3]*(0.2 + self.year*0.1)
        
        elif havetag("名门望族",self) == True and self.love >= 80+(self.year-10):
            self.love = 80+(self.year-10)
        else:
            pass
        
        if havetag("天生丽质",self) == True :
            if self.beauty >=1000:
                self.beauty = 1000
            else:
                pass
        elif havetag("桃花人面",self) == True :
            if self.beauty >=900:
                self.beauty = 900
            else:
                pass
        
        elif havetag("明眸皓齿",self) == True :
            if self.beauty >=850:
                self.beauty = 850
            else:
                pass
        else:
            if self.beauty >= 800:
                self.beauty = 800
            else:
                pass
        
        
        if havetag("谪仙降世",self) == True :
            if self.qizhi >=1000:
                self.qizhi = 1000
            else:
                pass
        elif havetag("冰肌玉骨",self) == True :
            if self.qizhi >=900:
                self.qizhi = 900
            else:
                pass
        elif havetag("清姿隽逸",self) == True :
            if self.qizhi >=850:
                self.qizhi = 850
            else:
                pass
        else:
            if self.qizhi >= 800:
                self.qizhi = 800
            else:
                pass
        
        if havetag("祸水红颜",self) == True :
            if self.meili >=1000:
                self.meili = 1000
            else:
                pass
        elif havetag("风情万种",self) == True :
            if self.meili >=900:
                self.meili = 900
            else:
                pass
        elif havetag("仪态万千",self) == True :
            if self.meili >=850:
                self.meili = 850
            else:
                pass
        else:
            if self.meili >= 800:
                self.meili = 800
            else:
                pass
        
        if havetag("智绝无双",self) == True or havetag("狡兔三窟",self) == True:
            if self.xinji >=1000:
                self.xinji = 1000
            else:
                pass
        elif havetag("思虑入微",self) == True :
            if self.xinji >=900:
                self.xinji = 900
            else:
                pass
        elif havetag("聪慧过人",self) == True :
            if self.xinji >=850:
                self.xinji = 850
            else:
                pass
        elif havetag("心浮气躁",self) == True :
            if self.xinji >=700:
                self.xinji = 700
            else:
                pass
        elif havetag("意气用事",self) == True :
            if self.xinji >=600:
                self.xinji = 600
            else:
                pass
        else:
            if self.xinji >= 800:
                self.xinji = 800
            else:
                pass
        if havetag("洪福齐天",self) == True or havetag("亦痴亦诚",self) == True:
            if  self.lucky >=100:
                self.lucky = 100
            else:
                pass
        elif havetag("灾星孽缘",self) == True :
            if self.lucky >=50:
                self.lucky = 50
            else:
                pass
        
        else:
            if self.lucky >= 80:
                self.lucky = 80
            else:
                pass
        
        
        if havetag("先天弱症",self) == True :
            if self.health >=500:
                self.health = 500
            else:
                pass
        elif havetag("弱柳扶风",self) == True :
            if self.health >=600:
                self.health = 600
            else:
                pass
        else:
            if self.health >= 1000:
                self.health = 1000
            else:
                pass
        
        
        
        if havetag("声音嘶哑",self) == True and self.muzic >= 80:
            self.muzic = 80
        if havetag("四肢崎拙",self) == True and self.dance >= 80:
            self.dance = 80
        if havetag("木讷愚钝",self) == True and self.book >= 80:
            self.book = 80
        if havetag("粗枝大叶",self) == True and self.cixiu >= 80:
            self.cixiu = 80
        
        if havetag("亦痴亦诚",self) == True :
            if self.qingxiang >= 50:
                self.qingxiang = 50
            if self.lucky <= 80:
                self.lucky = 80
        
        if havetag("难得欢喜",self) == True :
            if self.love <= 0:
                self.love = 0
            if persistent.expspeed == 0 and self.level != 0:
                self.exp += 0.1 + self.love*0.01
            elif persistent.expspeed == 1 and self.level != 0:
                self.exp += 0.2 + self.love*0.02
            elif persistent.expspeed == 2 and self.level != 0:
                self.exp += 0.4 + self.love*0.04
            else:
                pass



    def randomfz():
        templist = []
        for i in NPC_fz_list:
            if i == my:
                pass
            elif jinzu(i) == True:
                pass
            elif i.state == "病重" or i.state == "禁足" or i.state == "抱恙":
                pass
            elif   tags[4] in i.tags:
                pass
            elif  tags_yali[2] in i.tags:
                pass
            
            else:
                templist.append(i)
        if len(templist) == 0:
            return my
        else:
            fz = renpy.random.choice(templist)
            return fz


    def xiaduchengfa(fz,bei,du,jieguo):
        global tongmou
        global jiahuo
        global tempnum
        tempnum = yuanweifen[1][4]/(beifei-2)*0.6
        if persistent.expspeed == 1:
            tempnum = tempnum
        elif persistent.expspeed == 0:
            tempnum = tempnum*0.5
        else:
            tempnum = tempnum*2
        a = len(yuanweifen)
        if fz.level == 0: 
            b = 6
        elif fz.qinjunum == 1:
            b = 5
        elif fz.level > a-a*0.6:
            b = 3
        else:
            b = 4
        if fz.love > 80:
            b += 3
        elif fz.love >60:
            b+= 2
        elif fz.love > 30:
            b+= 1
        else:
            pass
        if bei.level == 0:
            c = 6
        elif bei.qinjunum == 1:
            c = 5
        elif bei.level > a-a*0.6:
            c = 3
        else:
            c = 4
        if bei.love > 80:
            c += 3
        elif bei.love >60:
            c+= 2
        elif bei.love > 30:
            c+= 1
        else:
            pass
        tempnum = tempnum + tempnum*(c-b)*0.1
        if du == 0:
            pass
        elif du == 1:
            tempnum = tempnum*2
        elif du == 2:
            tempnum = tempnum*1.5
        else: 
            tempnum = tempnum*2.5
        if jieguo == "成功":
            tempnum = tempnum*1
        else:
            tempnum = tempnum*0.75
        if fz == my and tongmou == True:
            tempnum = tempnum*0.5
            fz.exp -= int(tempnum)
        elif fz == my and jiahuo == True:
            tempnum = int(tempnum)
        else:
            fz.exp -= int(tempnum)

    def changecheng(self):
        if self.hao =="":
            self.cheng = self.xing + self.weifen
        else:
            self.cheng = self.hao +self.weifen

    def diwei(self):
        a = len(yuanweifen)
        if self.level == 0: 
            return 0
        elif self.qinjunum == 1: 
            return 1
        elif self.level > round(a-a/3):
            return 3
        else:
            return 2

    def huanggong():
        global map1
        global map2
        if month > 1 and month < 5:
            map1 = "春"
        elif month > 4 and month < 8:
            map1 = "夏"
        elif month > 7 and month < 11:
            map1 = "秋"
        else:
            map1 = "冬"
        
        if timenum == 4:
            map2 = "黄昏"
        elif timenum== 5:
            map2 = "晚上"
        else:
            map2 = "白天"

    def bg(self):
        global timenum
        renpy.scene()
        ClearScreens()
        global map1
        global map2
        if self == "妃嫔寝居外":
            if timenum == 4 :
                renpy.show("妃嫔寝居外 傍晚")
            elif timenum == 5 :
                renpy.show("妃嫔寝居外 夜晚")
            else:
                renpy.show("妃嫔寝居外")
        elif self == "凤仪宫外":
            if timenum == 4 :
                renpy.show("凤仪宫外 傍晚")
            elif timenum == 5 :
                renpy.show("凤仪宫外 夜晚")
            else:
                renpy.show("凤仪宫外")
        elif self == "妃嫔寝居内":
            if timenum == 5 :
                renpy.show("妃嫔寝居内 夜")
            else:
                renpy.show("妃嫔寝居内")
        elif self == "观仙台":
            if timenum == 5 :
                renpy.show("观仙台 夜")
            else:
                renpy.show("观仙台")
        elif self == "上林苑":
            if timenum == 5 :
                renpy.show("上林苑 夜")
            else:
                renpy.show("上林苑")
        elif self == "紫竹林":
            if timenum == 5 :
                renpy.show("紫竹林 夜")
            else:
                renpy.show("紫竹林")
        elif self == "御花园":
            if month > 4 and month < 8:
                if timenum == 5 :
                    renpy.show("御花园 夏 夜晚")
                else:
                    renpy.show("御花园 夏")
            else:
                if timenum == 5 :
                    renpy.show("御花园 夜")
                else:
                    renpy.show("御花园")
        elif self == "寝居":
            if diwei(my) == 0:
                renpy.show("凤仪宫内")
            elif my.qinjunum == 1:
                if timenum == 5 :
                    renpy.show("寝居2深夜")
                elif timenum == 4 :
                    renpy.show("寝居2傍晚")
                else:
                    renpy.show("寝居2白天")
            else:
                if timenum == 5 :
                    renpy.show("寝居1深夜")
                elif timenum == 4 :
                    renpy.show("寝居1傍晚")
                else:
                    renpy.show("寝居1白天")
        elif self == "锦寒宫":
            if timenum == 5 :
                renpy.show("锦寒宫 夜")
            else:
                renpy.show("锦寒宫")
        elif self == "花间阁":
            if timenum == 5 :
                renpy.show("花间阁 夜")
            else:
                renpy.show("花间阁")
        elif self == "莲韵池":
            if month > 4 and month < 8 and timenum == 5:
                renpy.show("莲韵池 夏 夜晚")
            elif month > 4 and month < 8 and timenum == 4:
                renpy.show("莲韵池 夏 黄昏")
            elif month > 4 and month < 8 :
                renpy.show("莲韵池 夏 白天")
            elif timenum == 5:
                renpy.show("莲韵池 夜晚")
            elif timenum == 4:
                renpy.show("莲韵池 黄昏")
            else:
                renpy.show("莲韵池 白天")
        elif self == "千鲤池":
            if month < 2 or month > 10 :
                if timenum == 5:
                    renpy.show("千鲤池 冬 夜晚")
                else:
                    renpy.show("千鲤池 冬 白天")
            else:
                if timenum == 5:
                    renpy.show("千鲤池 夜晚")
                else:
                    renpy.show("千鲤池 白天")
        elif self == "掖廷":
            if month < 2 or month > 10 and timenum >= 4:
                renpy.show("掖廷 冬 夜晚")
            elif  month < 2 or month > 10 :
                renpy.show("掖廷 冬 白天")
            elif month > 7 and month < 11  and timenum >= 4:
                renpy.show("掖廷 秋 夜晚")
            elif month > 7 and month < 11  :
                renpy.show("掖廷 秋 白天")
            elif timenum >= 4:
                renpy.show("掖廷 夜晚")
            else:
                renpy.show("掖廷 白天")
        elif self == "重华宫":
            if timenum == 5:
                renpy.show("重华宫 夜晚")
            elif timenum == 4:
                renpy.show("重华宫 傍晚")
            else:
                renpy.show("重华宫 白天")
        elif self == "皇宫":
            if month > 1 and month < 5:
                map1 = "春"
            elif month > 4 and month < 8:
                map1 = "夏"
            elif month > 7 and month < 11:
                map1 = "秋"
            else:
                map1 = "冬"
            
            if timenum == 4:
                map2 = "黄昏"
            elif timenum== 5:
                map2 = "晚上"
            else:
                map2 = "白天"
            
            
            renpy.show("皇宫")
        else:
            renpy.show(self)

    def HZ(who,what):
        global my_face
        global my_face_Normal
        global my_face_Smile
        global my_face_Think
        global my_face_Cry
        global my_face_Amaze
        global my_face_Angry
        if who == "妖妃":
            my_face = "Nvzhu/妖妃 " +what + ".webp"
            my_face_Normal = "Nvzhu/妖妃 " +what + ".webp"
            my_face_Smile = "Nvzhu/妖妃 " +what + " 笑.webp"
            my_face_Think = "Nvzhu/妖妃 " +what + " 思.webp"
            my_face_Cry = "Nvzhu/妖妃 " +what + " 泪.webp"
            my_face_Amaze = "Nvzhu/妖妃 " +what + ".webp"
            my_face_Angry = "Nvzhu/妖妃 " +what + ".webp"
        elif who == "福遥":
            my_face = "Nvzhu/福遥 " +what + ".webp"
            my_face_Normal = "Nvzhu/福遥 " +what + ".webp"
            my_face_Smile = "Nvzhu/福遥 " +what + " 笑.webp"
            my_face_Think = "Nvzhu/福遥 " +what + " 思.webp"
            my_face_Cry = "Nvzhu/福遥 " +what + " 泪.webp"
            my_face_Amaze = "Nvzhu/福遥 " +what + " 惊.webp"
            my_face_Angry = "Nvzhu/福遥 " +what + " 怒.webp"
        else:
            my_face = "Nvzhu/"+who+" " +what + ".webp"
            my_face_Normal = "Nvzhu/"+who+" " +what + ".webp"
            my_face_Smile = "Nvzhu/"+who+" "  +what + " 笑.webp"
            my_face_Think = "Nvzhu/"+who+" "  +what +" 思.webp"
            my_face_Cry = "Nvzhu/"+who+" "  +what +" 泪.webp"
            my_face_Amaze = "Nvzhu/"+who+" "  +what +" 惊.webp"
            my_face_Angry = "Nvzhu/"+who+" "  +what +" 怒.webp"
        return

    def yunqi(self):
        for i in self.tags:
            if "身怀皇嗣" in i:
                return i[1]



label 定义妃子(fz):
    image fz = "Feizi/F[fz.face].webp"

    python:
        fz = Character("[fz.hao][fz.weifen]-[fz.name]", color="#F08080",image=fz,what_suffix="{image=end_pic}")
        renpy.return_statement()
 
