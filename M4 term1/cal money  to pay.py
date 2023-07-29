round = int(input('round to use : '))
round_rn = 1

while round_rn<=round:
    total = int(input('total money : '))
    ppl = int(input('amount of people : '))
    print ('pay',total/ppl,'per person')