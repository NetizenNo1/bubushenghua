












define config.name = _("步步生花")




define gui.show_name = False




define config.version = "26.0.0"




define gui.about = _p("""
""")





define build.name = "bubushenghua"






define config.has_sound = True
define config.has_music = True
define config.has_voice = True







define config.fade_music = 1.0




define config.main_menu_music = "Audio/main-menu-theme.ogg"
define config.enter_sound = "Audio/se_maoudamashii_se_sound06.ogg"
define config.exit_sound = "Audio/se_maoudamashii_se_sound06.ogg"

define audio.FTL = "<from 1.5>Audio/黎明序幕.mp3"
define audio.SLY = "<from 2>Audio/经年.mp3"
define audio.YHY = "<from 1>Audio/月色流樱.mp3"
define audio.TYC = "<from 1.5>Audio/夜凉如水.mp3"
define audio.Bad = "<from 0.5>Audio/雾霭.mp3"
define audio.Bigmap = "<from 0.5>Audio/归途.mp3"















define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "hide"




define config.window_show_transition = None
define config.window_hide_transition = None






define config.default_transform = lihui




default preferences.text_cps = 30




default preferences.afm_time = 15














define config.save_directory = None






define config.window_icon = "gui/window_icon.webp"






init python:

















    build.classify('**~', None)
    build.classify('**.psd', None)
    build.classify('**.bak', None)
    build.classify('**.rar', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.txt', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/images/bg/备用/*', None)
    build.classify('game/images/bg/天元山/*', None)
    build.classify('game/images/Male2/*', None)
    build.classify('game/位份/*', None)
    build.classify('game/备用字体/*', None)

    build.archive("scripts", "all")
    build.archive("Male", "all")
    build.archive("Kid", "all")
    build.archive("Other", "all")
    build.archive("bg", "all")
    build.archive("Audio", "all")


    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/images/Male/**', 'Male')
    build.classify('game/images/Maps/WhiteLight/**', 'Other')
    build.classify('game/images/Kid/**', 'Kid')
    build.classify('game/images/Special/**', 'Other')
    build.classify('game/images/Juqingfei/**', 'Other')
    build.classify('game/images/bg/**', 'bg')
    build.classify('game/images/Nvzhu/**', 'Other')
    build.classify('game/images/Royal/**', 'Other')
    build.classify('game/images/Maps/**', 'bg')
    build.classify('game/images/flower.webp', 'Other')
    build.classify('game/Audio/**', 'Audio')
    build.classify('game/images/Feizi/Fatan.webp', 'Other')
    build.classify('game/images/Feizi/F426.webp', 'Other')
    build.classify('game/images/Feizi/Fchuhuan.webp', 'Other')
    build.classify('game/images/Feizi/FFY0.webp', 'Other')
    build.classify('game/images/Feizi/FFY1.webp', 'Other')
    build.classify('game/images/Feizi/FFY2.webp', 'Other')
    build.classify('game/images/Feizi/Fjinshu.webp', 'Other')
    build.classify('game/images/Feizi/Ftaoning.webp', 'Other')
    build.classify('game/images/Feizi/FRE0.webp', 'Other')
    build.classify('game/images/Feizi/FYF0.webp', 'Other')
    build.classify('game/images/Feizi/FYF1.webp', 'Other')
    build.classify('game/images/Feizi/FYF2.webp', 'Other')
    build.classify('game/images/Gongnv/GN老鸡.webp', 'Other')
    build.classify('game/images/Gongnv/GN潇潇.webp', 'Other')








    build.documentation('*.html')
    build.documentation('*.txt')


















    config.developer = True
    config.console = True
define config.implicit_with_none = None

init:
    python:
        if 'K_LCTRL' in config.keymap['skip']:
            config.keymap['skip'].remove('K_LCTRL')
        config.keymap['skip'].append('z')

    $ _dismiss_pause = False
 
