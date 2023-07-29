#input
people = int(input("how many people in your class:"))
scores = []
for i in range(people):
    scores.append(float(input(f"score {i+1}:  ")))
scores.sort()
scores.reverse()
print(scores)
#process
words = ["f","d","c","b","a","a","a"]
#loop for amount of people
for i in range(people):
    #loop for grade
    for b in range(len(words)):
        if scores[i] < 50+(b*10):
            #output
            print ("student",i, "grade:", words[b])
            break
print(5,8,9)