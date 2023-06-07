"""
ID prefix in second digit for each category:
     user:1
     shop:2
     product:3
     orderitem:4
     order:5
     logistics info:6
     comment:7
     discount_coupon: 8,
    free_shipping_coupon: 9,

ID prefix in first digit
    1:auto-inserted data
    2:real data

ID has totally 9 digit : abxxxxxxx
a use for identify if it is manually inserted  SEE mode in data.py col:11
b for each category
"""

import pymysql
import data
import tel
import random

first_digit = {
    'user': 1,
    'shop': 2,
    'product': 3,
    'orderitem': 4,
    'order': 5,
    'logisticsinfo': 6,
    'comment': 7,
    'discount_coupon': 8,
    'free_shipping_coupon': 9,
}

user_num = 10000
shop_num = 400
product_num = 10000
order_num = 20000
order_item_num = 400000
logistics_num = order_num
comment_num = 3000
following_num = 4000
discount_coupon_num = data.discount_coupon_num
free_shipping_num = data.free_shipping_num
sum_coupon_num = data.sum_coupon_num
# 打开数据库连接
try:
    db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, database="mydb")
    print('连接成功！')
except:
    print('something wrong!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# 使用预处理语句创建表
'''--USER-- '''
for i in range(user_num):
    sql = """INSERT INTO user(u_id,u_name,u_tel,u_address)
             VALUES ({},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_address(), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['user']),
                              "\'", data.get_u_name(i), "\'",
                              "\'", tel.get_tel(i), "\'",
                              "\'", data.get_address(), "\'",
                              ))
    # if i % (number_of_row/1000) == 0:
    #     print(i/number_of_row)



print("666")

'''---SHOP---'''

for i in range(shop_num):
    sql = """INSERT INTO shop(s_id,s_name,s_tel,s_category)
             VALUES ({},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_s_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_s_category(), "\'",
    #                  ))
    cursor.execute(sql.format(data.get_id(i, first_digit['shop']),
                              "\'", data.get_s_name(i), "\'",
                              "\'", tel.get_tel(i), "\'",
                              "\'", data.get_s_category(), "\'",
                              ))

print("666")



'''---PRODUCT---'''
# 使用预处理语句创建表
for i in range(product_num):
    sql = """INSERT INTO product(p_id,p_name,p_category,price,imageURL,shop_s_id)
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(i,
    #                  "\'", data.get_s_name(i), "\'",
    #                  "\'", tel.get_tel(i), "\'",
    #                  "\'", data.get_s_category(), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['product']),
                              "\'", data.get_p_name(i), "\'",
                              "\'", data.get_p_category(i), "\'",
                              "\'", random.randint(0, 10000), "\'",
                              "\'", data.get_p_url(), "\'",
                              "\'", data.get_id(random.randint(0, shop_num - 1), first_digit['shop']), "\'",
                              ))

print("666")



'''---logistic--'''
for i in range(logistics_num):
    sql = """INSERT INTO logisticsinfo(l_id,inc,l_state,expect_date,l_from,l_to,l_fee)
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{},{});"""
    # cursor.executemany(sql,input_name)
    # print(sql.format(data.get_id(i, first_digit['logisticsinfo']),
    #                  "\'", data.get_l_inc(), "\'",
    #                  "\'", data.get_l_state(), "\'",
    #                  "\'", data.get_l_time(), "\'",
    #                  "\'", data.get_address(), "\'",
    #                  "\'", data.get_address(), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['logisticsinfo']),
                              "\'", data.get_l_inc(), "\'",
                              "\'", data.get_l_state(), "\'",
                              "\'", data.get_l_time(), "\'",
                              "\'", data.get_address(), "\'",
                              "\'", data.get_address(), "\'",
                              random.randint(1, 20) * 10,
                              ))

print("666")




# ------discount_coupon-----------
for i in range(discount_coupon_num):
    sql = """INSERT INTO discount_coupon(discount_coupon_id,discount)
                 VALUES ({},{});"""
    # print(sql.format(data.get_id(i, first_digit['discount_coupon']),
    #                  random.randint(1, 100),
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['discount_coupon']),
                              random.randint(1, 100),
                              ))

print("666")



# ------free shipping-----------
for i in range(free_shipping_num):
    sql = """INSERT INTO free_shipping_coupon(free_shipping_coupon_id,`range`)
                 VALUES ({},{}{}{});"""
    # print(sql.format(data.get_id(i, first_digit['user']),
    #                  data.get_id(random.randint(0, shop_num - 1), first_digit['shop']),
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['free_shipping_coupon']),
                              "\'", data.range_coupon[random.randint(0, 3)], "\'",
                              ))

print("666")



'''---coupon--'''
for i in range(sum_coupon_num):
    sql = """INSERT INTO coupon(coupon_id,c_state,u_id,begin_time,end_time) 
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # print(sql.format(data.get_id(i, first_digit['order']),
    #                  "\'", data.get_o_time(), "\'",
    #                  "\'", data.get_p_category(i), "\'",
    #                  "\'", data.get_p_url(), "\'",
    #                  "\'", data.get_id(random.randint(0, shop_num - 1), first_digit['shop']), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_coupon_id(i),
                              "\'", random.randint(1,2), "\'",
                              "\'", data.get_id(random.randint(0, user_num - 1), first_digit['user']), "\'",
                              "\'", data.get_coupon_start(), "\'",
                              "\'", data.get_coupon_end(),
                              "\'",

                              ))

print("777")

'''---order--'''
for i in range(order_num):
    sql = """INSERT INTO `order`(o_id,o_time,u_id,s_id,l_id,coupon_id) 
                 VALUES ({},{}{}{},{}{}{},{}{}{},{}{}{},{}{}{});"""
    # print(sql.format(data.get_id(i, first_digit['order']),
    #                  "\'", data.get_o_time(), "\'",
    #                  "\'", data.get_p_category(i), "\'",
    #                  "\'", data.get_p_url(), "\'",
    #                  "\'", data.get_id(random.randint(0, shop_num - 1), first_digit['shop']), "\'",
    #                  ))
    print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['order']),
                              "\'", data.get_o_time(), "\'",
                              "\'", data.get_id(random.randint(0, user_num - 1), first_digit['user']), "\'",
                              "\'", data.get_id(random.randint(0, shop_num - 1), first_digit['shop']), "\'",
                              "\'", data.get_id(random.randint(0, logistics_num - 1), first_digit['logisticsinfo']),
                              "\'",
                              "\'", data.get_coupon_id(i%sum_coupon_num),
                              "\'",

                              ))

print("666")



'''--order item---'''
for i in range(order_item_num):
    sql = """INSERT INTO orderitem(oi_id,Product_p_id,o_id,amount)
                 VALUES ({},{},{},{});"""
    # print(sql.format(data.get_id(i, first_digit['order']),
    #                  "\'", data.get_o_time(), "\'",
    #                  "\'", data.get_p_category(i), "\'",
    #                  "\'", data.get_p_url(), "\'",
    #                  "\'", data.get_id(random.randint(0, shop_num - 1), first_digit['shop']), "\'",
    #                  ))
    # print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['orderitem']),
                              data.get_id(random.randint(0, product_num - 1), first_digit['product']),
                              data.get_id(random.randint(0, order_num - 1), first_digit['order']),
                              random.randint(1, 13),

                              ))

print("666")



# ---------comment-------
for i in range(comment_num):
    sql = """INSERT INTO comment(c_id,c_time,star,text,u_id,p_id)
                 VALUES ({},{}{}{},{},{}{}{},{},{});"""
    print(sql.format(data.get_id(i, first_digit['comment']),
                     "\'", data.get_c_time(), "\'",
                     random.randint(0, 5),
                     "\'", data.get_comment(), "\'",
                     data.get_id(random.randint(0, user_num - 1), first_digit['user']),
                     data.get_id(random.randint(0, product_num - 1), first_digit['product']),

                     ))
    print(i)
    cursor.execute(sql.format(data.get_id(i, first_digit['comment']),
                              "\'", data.get_c_time(), "\'",
                              random.randint(0, 5),
                              "\'", data.get_comment(), "\'",
                              data.get_id(random.randint(0, user_num - 1), first_digit['user']),
                              data.get_id(random.randint(0, product_num - 1), first_digit['product']),

                              ))

print("666")



# ------following-----------
for i in range(following_num):
    sql = """INSERT INTO following(u_id,s_id)
                 VALUES ({},{});"""
    for j in range(0, random.randint(1, 100)):
        try:
            print(sql.format(data.get_id(i, first_digit['user']),
                             data.get_id(i, first_digit['user']),
                             ))
            print(i)
            cursor.execute(sql.format(data.get_id(i, first_digit['user']),
                                      data.get_id(random.randint(0, shop_num - 1), first_digit['shop']),
                                      ))
        except:
            print("nima")

print("666")



# # ------discount_coupon-----------
# for i in range(discount_coupon_num):
#     sql = """INSERT INTO discount_coupon(Coupon_id,coupon_state,begin_time,end_time,user_u_id,o_id,min_amount,discount)
#                  VALUES ({},{},{}{}{},{}{}{},{},{},{},{});"""
#     print(sql.format(data.get_id(i, first_digit['discount_coupon']),
#                      random.randint(0, 1),
#                      "\'", data.get_discount_coupon_start(), "\'",
#                      "\'", data.get_discount_coupon_end(), "\'",
#                      data.get_id(random.randint(0, user_num - 1), first_digit['user']),
#                      data.get_id(random.randint(0, order_num - 1), first_digit['order']),
#                      random.randint(5, 20) * 100,
#                      random.randint(1, 4) * 100,
#                      ))
#     print(i)
#     cursor.execute(sql.format(data.get_id(i, first_digit['discount_coupon']),
#                               random.randint(1, 2),
#                               "\'", data.get_discount_coupon_start(), "\'",
#                               "\'", data.get_discount_coupon_end(), "\'",
#                               data.get_id(random.randint(0, user_num - 1), first_digit['user']),
#                               data.get_id(random.randint(0, order_num - 1), first_digit['order']),
#                               random.randint(5, 20) * 100,
#                               random.randint(1, 4) * 100,
#                               ))
#
# # ------free shipping-----------
# for i in range(free_shipping_num):
#     sql = """INSERT INTO free_shipping_coupon(Coupon_id,coupon_state,begin_time,end_time,u_id,order_o_id,range_)
#                  VALUES ({},{},{}{}{},{}{}{},{},{},{});"""
#     # print(sql.format(data.get_id(i, first_digit['user']),
#     #                  data.get_id(random.randint(0, shop_num - 1), first_digit['shop']),
#     #                  ))
#     print(i)
#     cursor.execute(sql.format(data.get_id(i, first_digit['discount_coupon']),
#                               random.randint(1, 2),
#                               "\'", data.get_discount_coupon_start(), "\'",
#                               "\'", data.get_discount_coupon_end(), "\'",
#                               data.get_id(random.randint(0, user_num - 1), first_digit['user']),
#                               data.get_id(random.randint(0, order_num - 1), first_digit['order']),
#                               random.randint(5, 20) * 100,
#                               ))


db.commit()
print(cursor.fetchall())
print('成功！')

# 关闭数据库连接
db.close()
