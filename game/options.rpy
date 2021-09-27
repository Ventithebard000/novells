













define config.name = _("100 Degrees")





define gui.show_name = True




define config.version = "0.7"





define gui.about = _p("""This is an in-progress visual novel developed by Locket (Writing and Programming) and Magicfluffnugget (Writing and Art) created for the Yaoi Game Jam 2020.

Step out of your comfort zone and make new friends at the cooking club! Yuuma Fujiwara has always kept to himself, staying out of large social activities--especially clubs. But when his childhood friend Kyo Sasaki pushes him into joining the cooking club, Yuuma will have to come out of his shell and lend a helping hand to Katsumi Hoshino, resident cooking club disaster. Follow Yuuma on his adventures through patience, compassion, new friendships, and a budding romance.
""")






define build.name = "100Degrees"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "100Degrees-1595373585"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
