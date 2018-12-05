#-*-coding:utf-8-*-
'''九宫格的横竖对角三个数字之和都为15，且9个数字不能重复。。。思路，用到itertools里面的permutations，
可以组合3个数字，这样我们可以先选出来所有的和为15的组合，然后迭代出这样就可以计算竖排为15的组合，再去重
'''
import itertools

num3=[]
num=[i for i in range(1,10)]
num_3=[j for j in itertools.permutations(num,3)]
for num_315 in num_3:
    if sum(num_315)==15:
        num3.append(num_315)
for nums1 in num3:
    for nums2 in num3:
        for nums3 in num3:
            if nums1[0]+nums2[0]+nums3[0]==15&nums1[1]+nums2[1]+nums3[1]==15&nums1[2]+nums2[2]+nums3[2]==15&nums1[0]+nums2[1]+nums3[2]==15&nums1[2]+nums2[1]+nums3[0]==15:
                if len(set(nums1) & set(nums2)) == 0 & len(set(nums1) & set(nums3)) == 0 & len(
                            set(nums3) & set(nums2)) == 0:#set（）可以把tuple变成集合，然后可以进行交集等运算
                    print(nums1, nums2, nums3)
