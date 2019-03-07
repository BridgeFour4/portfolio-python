#nathan broadbent
#9/18
#change sorter

def change_sorter():
    #1 input from user for change
    total_change=int(input("How much change do you have in your pocket"))
    
    
    
    #2 calculate change
    q= total_change // 25
    whats_left=total_change%25
    
    d= whats_left // 10
    whats_left=whats_left%10
    
    n= whats_left // 5
    whats_left=whats_left%5
    
    p=whats_left
    
    #3 display back
    print("you have\n",q,"quarters\n",d,"dimes\n",n,"nickels\n","and",p,"pennies")

change_sorter()





def change2(total_change):
    #1 input from user for change
    total_change=total_change
    #2 calculate change
    dol= total_change//100
    whats_left=total_change%100
    
    q= whats_left // 25
    whats_left=whats_left%25
    
    d= whats_left // 10
    whats_left=whats_left%10
    
    n= whats_left // 5
    whats_left=whats_left%5
    
    p=whats_left
    
    #3 display back
    return dol,q,d,n,p

total_change=int(input("How much change do you have in your pocket"))
dol,q,d,n,p=change2(total_change)

print("you have\n",dol,"dollars\n",q,"quarters\n",d,"dimes\n",n,"nickels\n","and",p,"pennies")



    
