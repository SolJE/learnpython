x="There are %d types of people." % 10 # %d为格式变量，此句是将10按%d的格式变化后插入原文本中，再将整个字符串赋值给变量x；
binary='binary' # 变量赋值
do_not="don't" # 变量赋值
y='Those who know %s and those who %s.' % (binary,do_not) # 将binary和do_not两个变量按顺序以%s的格式插入到文本中，再将整个字符串赋值给变量y；

print(x) # 输出变量x；
print(y) # 输出变量y；
print("I said: %r." % x) # 输入文本，将x按%r的格式变化后插入原本文中输出；
print("I also said: '%s'" % y) # 输出文本，将y按%s的格式变化后插入原本文中输出；

hilarious = False # 这个变量赋值不用加引号，我也不懂为什么；
joke_evaluation = "Isn't that joke so funny?! %r" # 这个%r被忽略了？不懂

print (joke_evaluation % hilarious) # 此处%起了连接字符串的功能，字符串中间显示空格。不知是不是。

w = "This is the left side of..." # 赋值
e = "a string with a right side." # 赋值

print (w + e) # 此处+号起了连接字符串的功能，字符串中间无空格。不知是不是。
