############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
print "Welcome to the Celcius to Farenheit Calculator." 
print "What temperature do you want to convert?"
uI = int(raw_input())
swag = uI * 9 / 5 + 32
print swag
print "Who Has a Fever?"

tempList = [110, 170, 98, 78, 96, 106, 102, 101, 100 , 99]
swagList = []
for x in tempList:
    if x >= 100:
        swagList.append(x)
print swagList
list1 = [] 
postion = 0  
print "Patient Diagnosis"

keepGoing = True
while(keepGoing):
    print "Hello, How are you?"
    print "What is your temperature?"
    hi = int(raw_input())
    if hi < 100:
        print "You're ok. I recommend rest for now."
    if hi >= 105:
        print "You need to see a doctor!"
    if hi < 105: 
        print "Have you been sick in the past 24 hours? 3 for yes 4 for no"
        uSick = int(raw_input())
        if uSick == 3 and hi >= 102:
            print "You need to see a doctor!"    
    if hi >= 100:
        print "Have you been to West Africa lately?: 1 for yes, 2 for no"
        use = int(raw_input())
        if use == 1:
            print "You have Ebola, you're going to die most likely, I recommend going the CDC."
        if use == 2:
            print "I recommend rest for now, if it happens again come back for more testing!"
    print "Are there any more patients waiting? 5 for yes 6 for no"
    balls = int(raw_input())
    if balls == 6:
        keepGoing = False