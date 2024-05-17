# input process output
weight = int(input('请输入你的体重(kg)：'))
heigh = float(input('请输入你的身高(m)：'))

# BMI = weight/1.8*high

print (weight/(1.8*heigh))


# input 输入的不管是什么内容，都会被当作字符串去处理
# 入如果input输入的内容是整数，可以通过内置函数int等等
