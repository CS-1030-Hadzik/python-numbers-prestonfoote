#TODO create a variable called my_int and store a two digit whole number in it
my_int = 24
#TODO print out the following using my_int as the variable
#			binary value of my_int
#			octal value of my_int
#			hex value of my_int
bin(my_int)
oct(my_int)
hex(my_int)
#TODO create a variable with the current number of credits that you have earned in college.
# 			just count this class (4 credits) if you have not earned any credits
my_credits = 4

# create a second variable called AAS_credits required and assign it a value of 60
AAS_credits = 60
# create a third variable called BS_credits required and assign it a value of 120
BS_credits = 120
# print out the following using the variables that you have just created.
# 			 'I have taken .... number of credits
print ('I have taken', my_credits, 'credits so far')
# 			 'I have taken .... number of credits left until AAS degree (perform calculation)
credits_remaining = AAS_credits - my_credits
print ('I have', credits_remaining, 'credits left until AAS degree')
# 			 'I have taken .... number of credits left until BS degree (perform calculation)
credits_left = BS_credits - my_credits
print ('I have', credits_left, 'credits left until BS degree')
# 			 'I have .... percentage of AAS degree completed(perform calculation)
AAS_credit_percentage = (my_credits / AAS_credits) *100
print ('I have', AAS_credit_percentage, 'percentage of AAS degree completed')
# 			 'I have .... percentage of BS degree completed(perform calculation)
BS_credit_percentage = (my_credits / BS_credits) *100
print ('I have', BS_credit_percentage, 'percentage of BS degree completed')
# 			 'I have about .... number of classes left until AAS degree (perform calculation use 3 credit average class)
# find the # of classes in AAS
AAS_classes = AAS_credits / 3
my_classes = my_credits / 3
classes_remaining = AAS_classes - my_classes
print ( 'I have', classes_remaining, 'left in my AAS degree')

# 			 'I have about .... number of classes left until BS degree (perform calculation use 3 credit average class)
BS_classes = BS_credits / 3
me_classes = my_credits / 3
class_remaining = BS_classes - me_classes
print ('I have', class_remaining, 'lef in my BS degree')
#TODO change the value of your my int variable to 64206
#			print converted my_int to binary
#			print converted my_int to octal
#			print converted my_int to hex