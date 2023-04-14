def hasSingleCycle(array):
    # Write your code here.
    for i in range(len(array)):
        dictionary = dict()
        index = i
        isCircle = True
        while isCircle:
            if index in dictionary:
                return False
            else:
                dictionary[index] = True
            if len(dictionary) == len(array):
                isCircle = False
            index = index + array[index]
            if index >= 0 and index < len(array):
                continue
            elif index < 0:
                index = (len(array) + index) % len(array)
            elif index >= len(array):
                index = (index - len(array)) % len(array)
            else:
                continue
            print(dictionary)
    return True
            
            
        

