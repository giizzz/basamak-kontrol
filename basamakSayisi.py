value=abs(int(input("Basamak sayisini öğrenmek istediğiniz sayiyi giriniz-> ")))
count=0
if(value==0):
    print("1 basamaklidir.")
else:
    while value>0 :
        value=value//10
        count+=1
    print(count,"basamaklidir.")