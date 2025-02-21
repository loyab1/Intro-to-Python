#Benjamin Loya

#hypothetical classmates 3 favorite foods
hyp_classmte_fav = {'pizza','chicken parm', 'cheeseburger'}

#A set that ask for user to input their 3 favorite foods 
user_favfoods = {
    input('Enter your first favorite food: ').lower(),
    input('Enter your second favorite food: ').lower(),
    input('Enter your third favorite food: ').lower(),
}
#new set of similar items
x = user_favfoods.intersection(hyp_classmte_fav)

#if function that will output similar foods or ouput no interest if set is empty
if x:

    print('Our common foods are:', *x)
else:
    print("we have no common favorite foods.")