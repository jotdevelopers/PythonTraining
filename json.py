person = {}
while True:
    print("1. Add Person/n", "2. Delete Person/n", "3. Exit")
    inp = int(input())
    if inp == 1:
        p = input('Enter Person Name')
        person[p] = {}
        person[p]['occupation'] = []
        person[p]['education'] = []
        
        while True:
            print("1. Enter Occupation # To Break/n", "2. Enter Education # To Break/n", "3. Exit")
            inp = int(input())
            if inp == 1:
                occupation = {}
                while True:
                    key = input("Enter Key")
                    if key == '#': break
                    value = input("Enter Value")               
                    occupation[key] = value
                person[p]['occupation'].append(occupation)
            elif inp == 2:
                education = {}
                while True:
                    key = input("Enter Key")
                    if key == '#': break
                    value = input("Enter Value")               
                    education[key] = value
                person[p]['education'].append(education)
            elif inp == 3: break
    elif inp == 3: break

print(person)
