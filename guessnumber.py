'''
功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
'''


def guess_number(answer):
	inputnumber = int(input("what's your guess?"))

	while inputnumber!='q':
		if inputnumber < answer:
			print("the number is smaller than the answer.\n")
			inputnumber = int(input("what's your guess?"))

		if inputnumber > answer:
			print("the number is bigger than the answer")
			inputnumber = int(input("what's your guess?"))
		if inputnumber == answer:
			print ("good job, you are right.")
			break


