#vac = "sinovac"
#pham = "sinopham"
#phi = "phizer"
#mod = "moderna"
#az = "astrazeneca"
pm = "third shot as Pfizer or Moderna is suggested"
apm = "third shot as Astrazenega, Pfizer or Moderna is suggested"

vac1 = ["moderna","sinovac","sinopharm","pfizer","astrazeneca"]
for i in range(len(vac1)):
    print("press",i + 1,"for", vac1[i])
vaccine1 = int(input("input number vaccine 1 here :"))
vaccine2 = int(input("input number vaccine 2 here :"))
#moderna
if vaccine1 == 1 :
    print ("first vac is", vac1[vaccine1-1])
    if vaccine2 == 1:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
#sinovac
elif vaccine1 == 2 :
    print ("first vac is", vac1[vaccine1-1])
    if vaccine2 == 2:
        print("second vac is", vac1[vaccine2-1])
        print(apm)
    if vaccine2 == 5:
         print("second vac is", vac1[vaccine2-1])
         print(apm)
    if vaccine2 == 4:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
#sinopharm
elif vaccine1 == 3 :
    print ("first vac is", vac1[vaccine1-1])
    if vaccine2 == 3:
        print("second vac is", vac1[vaccine2-1])
        print(apm)
    if vaccine2 == 5:
         print("second vac is", vac1[vaccine2-1])
         print(apm)
    if vaccine2 == 4:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
#pfizer
elif vaccine1 == 4 :
    print ("first vac is", vac1[vaccine1-1])
    if vaccine2 == 4:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
#aztrazeneca
elif vaccine1 == 5 :
    print ("first vac is", vac1[vaccine1-1])
    if vaccine2 == 5:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
    if vaccine2 == 4:
        print("second vac is", vac1[vaccine2-1])
        print(pm)
#elif vaccine1 == 2 or 3 :
    #print ("first vac is", vac1[vaccine1-1])
    #if vaccine2 == 5:
      #  print("second vac is", vac1[vaccine2-1])
       # print("3rd shot as pfizer or moderna is suggested")

#elif vaccine1 == 2 or 3 :
 #   print ("first vac is", vac1[vaccine1-1])
     
#elif vaccine1 == 5:
 #   print ("first vac is", vac1[vaccine1-1])
  #  if vaccine2 == 4:
   #      print("second vac is", vac1[vaccine2-1])
    #-     print("3rd shot as pfizer or moderna is suggested")
else:
    print("error fuck of")

    

#x = int(input)
#vac 2