def LengthSequence(string, length):
    '''string => a string
       length => an integer representing required length of words which are be returned'''
    result= []
    # YOUR CODE GOES HERE
    val = []
    val = string.split()
    #print(val)
    
    # Populating the values using filter lambda function
    result = list(filter(lambda x: (len(x)== length), val))

    

    return result




##Input your desired sentence input
string = input()

#input the length of the string you need to filter
length = int(input())

#calling the function
LengthSequence(string,length)
