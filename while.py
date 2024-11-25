# this loop will continue untill the time that n equal as zero if it being zero the loop will be finishes.
n = 5
while n > 0:
    print (n)
    # we use this structure becuase after every time that print the value it will mines on eto continue.
    n = n - 1
# this loop will continue until name being equal as end.
name = input('what is your name?')
while name != 'end':
    print('salam', name)
    # we put name out of the quatation mark becuase it is varibale that we use to read the name so it is not a string.
    name = input('what is your name?')

# one of the most important thing about this is that we should pay attention about identation and space that it means 
# if we remove the spaces in the loop the are not the statments of it and they are dependent rules. 

n = 3
while n > 0:
    print (n)
    n = n - 1

n = 3
while n >= 0:
    # the equal sign of it will show the that until the n being -1 it will continue and print 3 to 0.
    print(n)
    n = n -1

# infinit loop : the loop that does not finish and it continue forever.
n = 3
while n >= 0:
    print (n)
    #this is a infinit loop becuase it will increse and never being -1 to stop.
    n = n + 1
    # if we wanna stop this we use control with c or use squear red sign. 

# Break Rule
n = 3
while n >= 0: 
    print (n)
    n = n + 1
    # if we wanna examine one thing we use the sign of == for this one means until n equal as 100 contine when being 100 stop.
    if n == 100:
        # break rule that it means it will break the loop so we the loop will not continue.
        break 

n = 3
while n >= 0:
    print (n)
    n = n + 1
    if n == 100:
        print (' oh you reached 100')
        break 
print ('out of the loop')
