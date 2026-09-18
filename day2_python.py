# 创建元组
t = (10,20,30,40)
# 取值
print(t[0])
# 切片
print (t[1:3])

# 集合
s = {1,2,2,3,3,3}
print(s) # 自动去重，输出 {1,2,3}
s1 = {1,2,6,8}
s2 = s.difference(s1) # 去除相同元素，即1，2
print(s2)

# 练习1：两数相加
def add(a,b):
    return a+b
c = add(3,4)
print(c)
# 练习2：列表求和
def sum_list(num_list):
    total = 0
    for i in num_list:
        total += i
    return total
print(sum_list([1,2,3,4,5]))
# 练习3：默认参数
def show_info(name,city = "西安"):
    print(name,city)
show_info("小明")
show_info("小红","北京")
# 练习4：变量作用域预判输出
num = 10
def test():
    num = 20
    print(num)
test()
print(num)
# global的使用，将内外num变成同一个变量
num = 10
def test():
    global num
    num = 20
    print(num)
test()
print(num)

#综合练习题（函数+容器综合）  题目：filter_even(num_list)接收列表，筛选偶数返回新列表
def filter_even(num_list):
    lst = []
    for i in num_list:
        if i % 2 == 0:
            lst.append(i)
    lst = set(lst)  # 用集合消除重复元素
    return lst
print(filter_even([1,2,2,4,4,3,4,5]))
