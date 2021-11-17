balls=51
while balls>1:
    user=int(input("pick less than 5 balls"))
    if user<=5 :
        balls=balls-user
        computer=5-user
        balls=balls-computer
        print('balls left after computer chance',balls)
    if balls==1:
        print('you lost')


        
    
