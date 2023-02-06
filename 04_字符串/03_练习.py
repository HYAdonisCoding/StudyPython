# 提示输入
name = input('请输入姓名：')
chinese = int(input('请输入语文成绩：'))
math = int(input('请输入数学成绩：'))
english = int(input('请输入姓名英语：'))

# 计算总成绩
total = chinese + math + english

# 打印
print('姓名：' + name +', 总成绩：' + str(total))
print(f'姓名：{name}, 总成绩：{total}')
print(F'姓名：{name}, 总成绩：{total}')
print('姓名： %s, 总成绩：%f, 平均分：%f' % (name, total, total/3))

# 格式转换说明符
# %d、%i转成整数（int）
# %s转成字符串（str）
# %f转成浮点数（float）
# 字符串 % 数据