#Fuck you таймкоды! Just FUCK YOU!!!
timecodes = """
00:44:56:09 Девочка и инструкторство 
00:48:32:04 Прибыльный дайвинг
00:49:54:24 Дайверская кругосветка
00:53:41:05 Будушее профессии 
00:54:43:07 Для кого профессия дайвинг инструктор
00:58:19:22 Холодильник желаний
"""
row=list(timecodes)
newtimecodes = """"""
p=0
h=0
for n in row:
    if n==':':
        p += 1
        if p==3:
            h =+ 1
            p = 0    
        else:
            newtimecodes += n
    elif h==1:
        h+=1
    elif h==2:
        h=0
        
    else: 
        newtimecodes += n
        
print(newtimecodes)