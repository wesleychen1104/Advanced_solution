############# Q9. Print the sum of the first and third element in the list "numbers" and print the result ############
# Topic: tuples

numbers = (4, 9, 16, 36)

# Code here

print(numbers[0]+numbers[2])
 



############# Q10. Fill out the next 3 nubmers in the pattern using the append() function and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 25]

# Code here

numbers.append(6**2)
numbers.append(7**2)
numbers.append(8**2)
print(numbers)







############# Q11. Append the sum of the 2nd and 4th element in the list "numbers" to itself and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 25]

# Code here

numbers.append(numbers[1]+numbers[3])
print(numbers)




############# Q12. Fill in the missing number between 16 and 36 and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 36]

# Code here

numbers.insert(3,5**2)
print(numbers)



############# Q13. Remove the element that breaks the pattern and print the result ############
# Topic: lists, list functions

numbers = [3, 9, 16, 25, 36]

numbers.remove(3)







############# 
# Q14. Create a dictionary with the following data and print the dictionary:
# Alex has $100
# Kevin has $50
# Henry has $500
############

# Topic: dictionaries

# Code here

data = {
    "Alex": {100
    },
    "Kevin": {50
    },
    "Henry": {500
    }
}

print(data)








############# 
# Q15 A. Create a dictionary with the following transactions and print the dictionary:
# Alex purchased a sweater for $100
# Kevin purchased a bookbag for $50
# Henry purchased a scarf for $500
############

# Topic: nested dictionaries

# Code here

transactions = {
    "Alex": {
        "sweater": 100
    },
    "Kevin": {
        "bookbag": 50
    },
    "Henry": {
        "Henry": 500
    }
}

print(transactions)


