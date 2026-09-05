# nested loops = A loop within another loop (outer, inner)
#                 outer loop:
#                   inner loop:


# for i in range(1,11):
#     print(i,end="\t")


# for x in range(3):
#     print("\n")
#     for i in range(1,10):
#         print(i,end="\t")
  
rows = int(input("Enter the number of rows: "))
collums = int(input("Enter the number of collumns: "))

# for r in range(0,rows):
#     for c in range(0,collums):
#         print("*",end="  ")
#     print()

#rows = 5
#collumns = 6 
for r in range(1,rows+1):
    for c in range(1,collums+1):
        if r==1 or r == rows or c == 1 or c == collums:
         print("*",end="  ")
        else:
           print(" ",end="  ")
    print()