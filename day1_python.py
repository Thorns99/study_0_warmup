# 字符串格式化练习
class_num = 2
salary = 5000
message = "我是%s班的，工资为%s" % (class_num, salary)
print(message)

# if语句训练
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print("您已成年，需要补票10元，祝您游玩愉快")

# if...elif...else语句训练
height = input("请输入您的身高(cm):")
height = int(height)
if height <= 120 and height > 0:
    print("您的身高不高于120cm，可以免费游玩")
elif height > 120:
    print("您的身高高于120cm，请补票10元")
else:
    print("输入有误，请重新输入")

# 练习1：循环输出1～100所有偶数(for)
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# 练习1：循环输出1～100所有偶数(while)
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1

#练习2：给定列表  num_list = [12,45,7,23,9,56] ，遍历找出大于20的数字，放到新列表
num_list = [12,45,7,23,9,56]
new_list = []
i = 0
while i < len(num_list):
    if num_list[i]>20:
        new_list.append(num_list[i])
    i = i + 1
print(new_list)

# 练习3：字典 user = {"name":"张三","age":20,"gender":"男"} ，遍历打印所有key和value
user = {"name":"张三","age":20,"gender":"男"}
for key,value in user.items():
    print(key,value)

#练习4：输入分数，判断等级规则：>=90优秀，80~89良好，60~79及格，小于60不及格
score = int(input("请输入分数："))
if score >= 90:
    print("成绩优秀")
elif score >= 80:
    print("成绩良好")
elif score >= 60:
    print("成绩及格")
elif score >= 0:
    print("成绩不及格")
else:
    print("成绩输入错误，请重新输入")