'''#[expression for target in interable]
foo = [1, 2, 3, 4, 5]
#将列表foo的每一项都乘以2，再返回由其结果组成的新列表
#用for循环来做
for i in range(len(foo)):
    foo[i] *= 2
print(foo)

#用列表推导式来做
foo = [i * 2 for i in foo]
print(foo)
[expression for target in interable if condition]
'''

foo = [i + 1 for i in range(10) if i % 2 == 0]
print(foo)

""" [expression for target1 in iterable1 if condition1
            for target2 in iteralbe2 if condition2
                    ...
            for targetN in iteralbeN if conditionN] """