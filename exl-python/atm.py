balance = 50000
flag = True

while(flag):
    withdrawl_amt = int(input('ENter amount to withdraw : '))
    if withdrawl_amt % 100 != 0:
        print('Invalid deno')

    elif withdrawl_amt < balance:
        balance = balance - withdrawl_amt
        print('balance left : ', balance)
        flag = False

    elif withdrawl_amt > balance:
        print('Insufficient balance')
