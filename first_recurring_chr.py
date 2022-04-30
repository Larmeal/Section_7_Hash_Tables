# #Google Question
# #Given an array = [2,5,1,2,3,5,1,2,4]:
# #It should return 2

# #Given an array = [2,1,1,2,3,5,1,2,4]:
# #It should return 1

# #Given an array = [2,3,4,5]:
# #It should return undefined



array_1 = [2,5,1,2,3,5,1,2,4]
array_2 = [2,1,1,2,3,5,1,2,4]
array_3 = [2,3,4,5] 


def find_duplicates(array):
    duplicated = {}
    for i in range(len(array)):
        if array[i] in duplicated:
            return array[i]
        else:
            duplicated[array[i]] = True
    
    return None

def naive_frc(array):
    l = len(array)
    i= 0
    frc = None
    while(i<l):
        j = i+1
        while(j<l):
            if array[i] == array[j]:
                l = j
                frc = array[j]
                continue
            else:
                j+=1
        i += 1
    return frc

print(find_duplicates(array_2))
print(naive_frc(array_2))