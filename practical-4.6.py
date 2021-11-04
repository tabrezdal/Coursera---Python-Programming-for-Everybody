def computepay(h,r):
 if h <= 40:
  pay = h * r
  print(pay)
 
 else:
  pay = 40 * r
  x = h - 40
  r = r * 1.5
  pay = pay + (x * r)
  return pay

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate :")
r = float(rate)

  
p = computepay(h,r)
print("Pay",p)




