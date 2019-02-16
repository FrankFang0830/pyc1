amount = 0

while True:
 str = input ("Enter transaction: ")
 transaction = str.split(" ")
 type = transaction [0]
 amount = int (transaction [1])

 if type=="Deposit" or type=="deposit":
  amount += amount
 elif type=="Withdraw" or type=="withdraw":
  amount -= amount
 else:
  pass

 str = input ("want to continue (Y for yes/N for no) : ")
 if not (str[0] =="Y" or str[0] =="y") :
  # break the loop
  break

print("Total amount: ", amount)