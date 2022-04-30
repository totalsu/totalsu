#컴퓨팅 과제 16

#교안 40페이지, 배송료 계산(다방향 선택)

price = int(input("상품의 가격을 입력하세요.: "))

if price > 100000:
    shipping_cost = 0
else:
    if price > 2000:
        shipping_cost = 3000
    else:
        shipping_cost = 5000

print("배송료는", shipping_cost, "입니다.")

#######################################################################################
########## test ####################### test ####################### test #############
#######################################################################################
price = int(input("상품의 가격을 입력하세요.: "))

if price > 100000:
    shipping_cost = 0
else:
    if price > 50000:
        shipping_cost = 1000
    else:
        if price > 40000:
            shipping_cost = 2000
        else:
            if price > 30000:
                shipping_cost = 3000
            else:
                if price > 20000:
                    shipping_cost = 4000
                else:
                    shipping_cost = 5000

print(shipping_cost)
