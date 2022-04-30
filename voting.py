from audioop import reverse


age=int(input("Enter age here"))
if (age<18):
    print("You cannot vote ")
elif(age>=18):
    print("You can vote")
x=["a","b",1,42,True,False]
# print(x.reverse())
x.reverse()
print(x)
y=(10,20,30,40,50)
for number in y:print(number%3)
a=[150,250,350,450,550]
b=[]
b=[num//9 for num in a]
print(b)
country_codes={"Kenya":254,"Uganda":256,"Rwanda":250}
country_codes["Burundi"]=257
print(country_codes)
country_codes["Morocco"]=312
print(country_codes)
country_codes.pop("Uganda")
print(country_codes)
p