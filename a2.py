s1 = {2 , 3 ,1}
s2 = {'b','a','c'}
s3 = list(zip(s1, s2))
print(s3,'\n')

#part2
stock = ['reliance', 'infoys', 'tcs']
prices = [2175 , 1127 , 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stock, prices)}
print('\n{}'.format(new_dict))