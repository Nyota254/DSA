#################################################################################################
# SECTION 1 BINARY SEARCH,LINKED LISTS AND COMPLEXITY
################################################################################################


# 1. find the position of provided input in array

# sol 1
# brute-force linear search

# from jovian.pythondsa import evaluate_test_case

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

        # visualization
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
    print(locate_card(**oneTest['input']) == oneTest['output'])
    # evaluate_test_case(locate_card, oneTest)


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

# newArray = test['input']['nums']
# newArray1 = newArray[1:4]
# print(newArray1)
print(count_rotations_binary(test['input']['nums']) == test['output'])


########################################################################################################
# SECTION 2 BINARY SEARCH TREES,TRAVERSALS AND BALANCING
#########################################################################################################
'''
Problem
QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.
'''


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(name='{}', username='{}' ,email='{}')".format(self.name, self.username, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

database = UserDatabase()

database.insert(aakash)
database.insert(vishal)
database.insert(biraj)

user = database.find('biraj')
print(user)
print(database.list_all())

#################################
# THE ABOVE CODE TIMECOMPLEXITY ANALYSIS
# worst case scenario it will take n iterations as it is a bruteforce method thus O(n) in complexity
# for insert find and update need optimization with logarithmic time sublinear O(log n) algo.
# the list has a complexity of constant time O(1).
