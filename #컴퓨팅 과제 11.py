#컴퓨팅 과제 11

#교안 31페이지, 배송료 계산 알고리즘

print("############################")
print(   "# 배송료 계산 프로그램#   ")
print("############################")

price = int(input("상품의 가격을 입력하시오."))

if price > 2000:
    shipping_cost = 0
else:
    shipping_cost =3000

print("shipping", shipping_cost)
