K=[]

def push(K):
     BOOKID=float(input("ENTER BOOKID:"))      #int or float
     BOOKNAME=input("ENTER BOOK NAME:")        #float can be used for price
     AUTHOR=input("ENTER AUTHOR NAME:")        #for set 4 itemno,itemname,price
     P=[BOOKID,BOOKNAME,AUTHOR]
     K.append(P)
     print(K)
     print("ELEMENT ADDED SUCCESSFULLY")
def pop(K):
     if K==[]:                             #len(K)
        print("UNDERFLOW!!!")
     else:
        print("ELEMENT DELETED IS:", K.pop())
while True:
    print("1.PUSH")
    print("2.POP")
    print("3.EXIT")
    C=int(input("ENTER YOUR CHOICE:"))
    if C==1:
        push(K)
    elif C==2:
        pop(K)
    elif C==3:
        break
    else:
        print("       INVALID CHOICE")
        print("****RUN THE PROGRAM AGAIN****")
        print("*****WITH CORRECT CHOICE****")
        
        
    
