a,number,n_be_choosed,i=[" "]*9,"1 2 3 4 5 6 7 8 9","",0
#印出最初的兩個九宮格
print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n\n"+" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
while i<=9:
	input_o=input("(O) Select[1-9]: ")
	#判斷輸入的位置是否合法或重複
	while True:
		if number.count(input_o)==0 or input_o=="":
			print("Invali d input. Try again.")
			input_o=input("(O) Select[1-9]: ")
		elif n_be_choosed.count(input_o)==1:
			print("Cell "+input_o+" has been filled. Try again.")
			input_o=input("(O) Select[1-9]: ")
		else:
			break
	n_be_choosed,a[int(input_o)-1],i=n_be_choosed+input_o+" ","O",i+1
	#判斷玩家是否獲勝
	if a[0:3]==["O"]*3 or a[3:6]==["O"]*3 or a[6:9]==["O"]*3 or a[0:7:3]==["O"]*3 or a[1:8:3]==["O"]*3 or a[2:9:3]==["O"]*3 or a[0:9:4]==["O"]*3 or a[2:7:2]==["O"]*3:
		print("\nPlayer O win!\n\n"+" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
		break
	#判斷是否和局
	elif i==9:
		print("\nTie. Bye~\n\n"+" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
		break
	print(" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
	input_x=input("(X) Select[1-9]: ")
	#判斷輸入的位置是否合法或重複	
	while True:
		if number.count(input_x)==0 or input_x=="":
			print("Invalid input. Try again.")
			input_x=input("(X) Select[1-9]: ")
		elif n_be_choosed.count(input_x)==1:
			print("Cell "+str(input_x)+" has been filled. Try again.")
			input_x=input("(X) Select[1-9]: ")
		else:
			break
	n_be_choosed,a[int(input_x)-1],i=n_be_choosed+input_x+" ","X",i+1
	#判斷玩家是否獲勝
	if a[0:3]==["X"]*3 or a[3:6]==["X"]*3 or a[6:9]==["X"]*3 or a[0:7:3]==["X"]*3 or a[1:8:3]==["X"]*3 or a[2:9:3]==["X"]*3 or a[0:9:4]==["X"]*3 or a[2:7:2]==["X"]*3:
		print("\nPlayer X win!\n\n"+" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
		break
	print(" "+a[0]+" | "+a[1]+" | "+a[2]+" "+"\n---|---|---\n"+" "+a[3]+" | "+a[4]+" | "+a[5]+" "+"\n---|---|---\n"+" "+a[6]+" | "+a[7]+" | "+a[8]+" \n\n")
	