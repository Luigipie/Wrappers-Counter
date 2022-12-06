#Legenda
# qs = quarters ,  nk = nickel, dm = dimes
print('do you want calculate how much wrappers do you need for your money?')
answer = input()
if answer == 'yes':
    conversion = True
while conversion == True:
    print('Do you wanna use pounds or grams?')
    answer_1 = input()
    if answer_1 == 'pounds':
        pounds_value = 1
    if answer_1 == 'pounds':
        print ('insert the weight in pounds \n')

        x = 0.275578             #weight of full wrapper     
        z = 0.440925            #weight of full wrapper
        y = 0.25000421           #weight of full wrapper
        j = 0.50000841            #weight of full wrapper

        print ('how much penny do you have?')
        a = input()
        penny =0.00551156     #pounds
        print ('how much nickel do you have?')
        b = input()
        nickel = 0.0110231     #pounds
        print ('how much dime do you have?')
        c = input()
        dime = 0.005000084106    #pounds
        print ('how much quarters do you have? \n')
        d = input()
        quarters = 0.0125663 #pounds

        def fraction_penny (a,x):               #all the operations about penny
            return (float(a)/float(x))          #to calculate how many wrappers you can fill

        money_penny = (float(a) / float(penny))                 #this permit to calculate how many penny we've
        result = fraction_penny (a,x)                           #this to calculate how many wrapper you can fill
        penny_dollar = float(money_penny) / float (100)         #this to trasform penny in dollars

        def fraction_nickel (b,z):              #all the operations about nickel
            return (float(b)/float(z))          #to calculate how many wrappers you can fill

        money_nickel = (float(b)/float(nickel))                 #this permit to calculate how many nickel we've
        result_nk = fraction_nickel(b,z)                        #this to calculate how many wrapper you can fill
        nk_dollar = float (money_nickel) / float (20)           #this to trasform nickel in dollars

        def fraction_dime (c,y):                #all the operations about dimes
            return (float(c)/float(y))          #to calculate how many wrappers you can fill

        money_dime = (float(c)/float(quarters))                 #this permit to calculate how many dime we've
        result_dm = fraction_dime (c,y)                         #this to calculate how many wrapper you can fill
        dm_dollar = float (money_dime) / float (10)             #this to trasform dimes in dollars

        def fraction_quarters (d,j):            #all the operations about quarters
            return (float(c)/float(j))          #to calculate how many wrappers you can fill

        money_quarters = (float(d) / float(quarters))           #this permit to calculate how many quarters we've
        result_qs = fraction_quarters (d,j)                     #this to calculate how many wrapper you can fill
        qs_dollar = float (money_quarters) / float (4)          #this to trasform quarters in dollars

        def total_money (penny_dollar,nk_dollar,dm_dollar,qs_dollar):
            return (float (penny_dollar) + float (nk_dollar) + float (dm_dollar) + float (qs_dollar))   #to calculate how much dollars we've

        total_dollars = total_money(penny_dollar,nk_dollar,dm_dollar,qs_dollar) 

        print ("in total, you've circa", round (total_dollars), 'dollars \n')
        print ('you have' , round(money_penny),'penny and you can fill' , round(result), 'red wrappers \n')
        print ('you have', round (money_nickel),'nickel and you can fill', round(result_nk), 'blue wrappers \n')
        print ('you have', round (money_dime),'dime and you can fill', round(result_dm), 'green wrappers \n')
        print ('you have', round (money_quarters),'quarter and you can fill', round(result_qs), 'orange wrappers \n')
        print ('do you wanna continue to calculate?')
        answer = input()
        if answer == 'no':
            exit()
    else:
        print ('insert the weight in grams')

        x = 125
        z = 200
        y = 113.4
        j = 226.8
        
        print ('how much penny do you have?')
        a = input()
        penny = 2.5     #grams
        print ('how much nickel do you have?')
        b = input()
        nickel = 5      #grams
        print ('how much dime do you have?')
        c = input()
        dime = 2.268    #grams
        print ('how much quarters do you have? \n')
        d = input()
        quarters = 5.67 #grams

        def fraction_penny (a,x):               #all the operations about penny
            return (float(a)/float(x))          #to calculate how many wrappers you can fill

        money_penny = (float(a) / float(penny))                 #this permit to calculate how many penny we've
        result = fraction_penny (a,x)                           #this to calculate how many wrapper you can fill
        penny_dollar = float(money_penny) / float (100)         #this to trasform penny in dollars

        def fraction_nickel (b,z):              #all the operations about nickel
            return (float(b)/float(z))          #to calculate how many wrappers you can fill

        money_nickel = (float(b)/float(nickel))                 #this permit to calculate how many nickel we've
        result_nk = fraction_nickel(b,z)                        #this to calculate how many wrapper you can fill
        nk_dollar = float (money_nickel) / float (20)           #this to trasform nickel in dollars

        def fraction_dime (c,y):                #all the operations about dimes
            return (float(c)/float(y))          #to calculate how many wrappers you can fill

        money_dime = (float(c)/float(quarters))                 #this permit to calculate how many dime we've
        result_dm = fraction_dime (c,y)                         #this to calculate how many wrapper you can fill
        dm_dollar = float (money_dime) / float (10)             #this to trasform dimes in dollars

        def fraction_quarters (d,j):            #all the operations about quarters
            return (float(c)/float(j))          #to calculate how many wrappers you can fill

        money_quarters = (float(d) / float(quarters))           #this permit to calculate how many quarters we've
        result_qs = fraction_quarters (d,j)                     #this to calculate how many wrapper you can fill
        qs_dollar = float (money_quarters) / float (4)          #this to trasform quarters in dollars

        def total_money (penny_dollar,nk_dollar,dm_dollar,qs_dollar):
            return (float (penny_dollar) + float (nk_dollar) + float (dm_dollar) + float (qs_dollar))   #to calculate how much dollars we've

        total_dollars = total_money(penny_dollar,nk_dollar,dm_dollar,qs_dollar) 

        print ("in total, you've circa", round (total_dollars), 'dollars \n')
        print ('you have' , round(money_penny),'penny and you can fill' , round(result), 'red wrappers \n')
        print ('you have', round (money_nickel),'nickel and you can fill', round(result_nk), 'blue wrappers \n')
        print ('you have', round (money_dime),'dime and you can fill', round(result_dm), 'green wrappers \n')
        print ('you have', round (money_quarters),'quarter and you can fill', round(result_qs), 'orange wrappers \n')
        print ('do you wanna continue to calculate?')
        answer = input()
        if answer == 'no':
            exit()
