price = float(input('Enter the price : '))
qty = int(input('Enter the quantity : '))
total_bill = price * qty

if total_bill > 5000 :
    discount = 0.15 * total_bill
    discounted_price = total_bill - discount
else:
    discount = 0
    discounted_price = total_bill

gst = 0.18 * discounted_price

final_amt = discounted_price + gst

print('Item price : ', price)
print('Quantity : ', qty)
print('Total Price : ', total_bill)
print('Discount : ', discount)
print('Price after discount : ', discounted_price)
print('GST : ', gst)
print('Final amount : ', final_amt)