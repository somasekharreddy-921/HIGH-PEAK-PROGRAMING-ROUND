
file1=open("input.txt","r")
file2 = open("output.txt","w+")
goodies={}
output=[]
for f in file1:
    toRead_index_price=f.index(":")
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
single_prices=list(goodies.values())


single_prices=[int(i)for i in single_prices]


single_prices.sort(reverse=True)
num_of_employees=int(input("Enter number of employees: "))
leng_considered=(len(single_prices)-num_of_employees)
for i in range(leng_considered):
    max_price=single_prices[i]
    min_price=single_prices[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=single_prices[idx_choosen:num_of_employees+idx_choosen]
diff=max(choosen_prices)-min(choosen_prices)


cnt=0
for key,value in goodies.items():
    single_prices[cnt]

    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+": "+value
        output.append(str1)
        cnt+=1
file2.write("The goodies selected for distribution: ")

file2.write("\n")

for i in output:
    file2.write(i)
    file2.write("\n")
file2.write("And the difference between  chosen goodie with highest price and the lowest price are "+str(diff))

file1.close()
file2.close()