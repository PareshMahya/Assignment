# 3. Create a class to find three elements that sum to zero from a set of n real numbers
#      Input array: [-25,-10,-7,-3,2,4,8,10]
#      Expected output: [[-10,2,8],[-7,-3,10]


def find_3_number(nums):
    num = sorted(nums)
    l = len(num)
    ans = []
    three_num_set = False
    for i in range(0, l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if (num[i] + num[j] + num[k] == 0):
                    ans.append([num[1],num[j],num[k]])
                    three_num_set = True
    print(ans)
    if (three_num_set == False):
        print("There is no set of three-element, whose sum equal to zero.")
 

num = [-25, -10, -7, -3, 2, 4, 8, 10]
find_3_number(num)
