# 21.Python-遍历列表时删除元素的正确做法
a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i>5:
        pass
    else:
        a.remove(i)
    print(a)
print('-----------')
print(id(a))
# filter

b = filter(lambda x:x>5,a)
print(list(b))

# 22.字符串的操作题目
# 全字母短句 PANGRAM 是包含所有英文字母的句子，比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG. 定义并实现一个方法
# get_missing_letter,传入一个字符串采纳数，返回参数字符串变成一个 PANGRAM 中所缺失的字符。
# 应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母顺序排序（请忽略所有非 ACSII 字符）
def get_missing_letter(a):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set(a)
    ret = "".join(sorted(s1-s2))
    return ret

print(get_missing_letter("python"))

# 23.可变类型和不可变类型
# 1,可变类型有list,dict.不可变类型有string，number,tuple.
#
# 2,当进行修改操作时，可变类型传递的是内存中的地址，也就是说，直接修改内存中的值，并没有开辟新的内存。
#
# 3,不可变类型被改变时，并没有改变原内存地址中的值，而是开辟一块新的内存，将原地址中的值复制过去，对这块新开辟的内存中的值进行操作。

# 24.is和==有什么区别？
# is：比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象。是否指向同一个内存地址
#
# == ： 比较的两个对象的内容/值是否相等，默认会调用对象的eq()方法

# 25.求出列表所有奇数并构造新列表
a = [1,2,3,4,5,6,7,8,9,10]
print([i for i in a if i%2==1])

# 26.用一行python代码写出1+2+3+10248
num = sum([1,2,3,10248])
print(num)

# 27.Python中变量的作用域？（变量查找顺序)
# 函数作用域的LEGB顺序
#
# 1.什么是LEGB?
#
# L： local 函数内部作用域
#
# E: enclosing 函数内部与内嵌函数之间
#
# G: global 全局作用域
#
# B： build-in 内置作用
#
# python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的

# 28.字符串 "123" 转换成 123，不使用内置api，例如 int()

def atoi(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num




