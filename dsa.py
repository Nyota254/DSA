# 1. find the position of provided input in array

#############################################
# linear search
#############################################


# sol 1
# brute-force linear search

from jovian.pythondsa import evaluate_test_case

'''
Bute force
'''


# def locate_card(cards, query):
#     position = 0

#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1
#     return -1


################################
# Sol2 Binary search
# ############################

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    print('-------------------------------------', len(cards))

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ", mid:",
              mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1


###############################
# Test cases
#############################
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []

# Example
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0, 0],
        'query': 7
    },
    'output': 3
})

# edge case no element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 7
    },
    'output': -1
})

# edge case last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# function test as follows
for oneTest in tests:
    print('------Test-case-pass-status----------')
    # print(locate_card(**oneTest['input']) == oneTest['output'])
    evaluate_test_case(locate_card, oneTest)


##################################
# [7,8,1,3,4,5,6] [7,8,9,10,11,12,3,4,5]
##################################
# PSEUDO CODE
# 1. initialize highest and lowest point of the array
# 2. check if the middle number is less than the number to its right
# 3. if the number to its right is less return the array index point plus one as number of rotations
# 4. else if the element to its right is greater compare the middle element with the last element
# 5. if last element is smaller then the middle element  then let the lowest number be mid index + 1
# 6. else let  hi number be index-1
# 7. repeat step 2 to 6 else return 0
##################################
def count_rotations_binary(nums):
    '''
    count how many arrays have been rotated
    '''
    lo = 0
    hi = len(nums)-1

    while 0 < len(nums)-1:
        '''
        '''

        mid = (hi-lo)//2
        # print((hi-lo)//2, nums[mid])
        if nums[mid] < nums[mid+1]:
            return mid
        elif nums[mid] < nums[hi]:
            lo = mid + 1
        elif nums[mid] > nums[hi]:
            hi = mid-1

    return 0


#################
# Test Case if true pass
#################
test = {
    'input': {
        'nums': [28, 27, 26, 25, 3, 4, 5, 6, 7, 8],
    },
    'output': 4
}


print(count_rotations_binary(test['input']['nums']) == test['output'])
