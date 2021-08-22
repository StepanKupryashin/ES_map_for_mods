
init python:
    mods['screen_map_start'] = u'Карта для начинающих'

    screen_map_condition = [False,False,False,False,False,False,False] # можно сделать и словарь
    screen_map_count = 0
    screen_map_label = 'screen_map_after_walk'
    screen_map_need_count = 1

    def screens_map_reset_condition():
        global screen_map_condition, screen_map_count, screen_map_need_count
        screen_map_condition = [False,False,False,False,False,False,False]
        screen_map_count = 0
        screen_map_need_count = 1


    def screens_map_set_condition(label,count):
        global screen_map_need_count, screen_map_label
        screen_map_label = label
        screen_map_need_count = count
    
init:
    #condition = {'label' : [(0,0,0,0), sensetive]}
    screen screen_map(condition={'screen_map_error_place' : [(414,467,200,200), screen_map_condition[0]]}):
        modal True
        imagemap:
            idle 'screens_map/map/old_map_idle.png'
            hover 'screens_map/map/old_map_hover.png'
            insensitive 'screens_map/map/old_map_insensitive.png'
            alpha True
            if condition != None:
                for label, lists in condition.items():
                    hotspot(lists[0][0], lists[0][1], lists[0][2], lists[0][3]) action [SensitiveIf(lists[1] == False), Jump(label)]

label screen_map_start:
    window show dissolve
    'Сейчас перед нами должна появиться карта'
    window hide dissolve
    $ screens_map_set_condition('screen_map_after_walk', 2)
    jump screen_map_walk

label screen_map_walk:
    if screen_map_count < screen_map_need_count:
        call screen screen_map({'screen_map_place1' : [(414,467,200,200), screen_map_condition[0]],'screen_map_place_2' : [(1000,10,200,200), screen_map_condition[1]]}) 
    else:
        'сбрасываем счетчик.'
        $ screens_map_reset_condition()
        $ renpy.jump(screen_map_label)

label screen_map_place1:
    'Place 1'
    $ screen_map_count += 1
    $ screen_map_condition[0] = True
    jump screen_map_walk

label screen_map_place_2:
    'Place 2'
    $ screen_map_count += 1
    $ screen_map_condition[1] = True
    jump screen_map_walk

label screen_map_after_walk:
    'Мы прошли все места.'
    jump screens_map_after_map

label screen_map_error_place:
    'Я забрел куда-то не туда.'

label screens_map_after_map:
    'продалжаем историю'
    return
    
