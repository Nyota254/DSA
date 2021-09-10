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
