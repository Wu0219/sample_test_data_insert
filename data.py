import pandas as pd
import random
import faker
import emoji
import re

discount_coupon_num = 3000
free_shipping_num = 3000
sum_coupon_num = discount_coupon_num + free_shipping_num -100
customer_csv = pd.read_csv("datasets/customer.csv")
name = pd.read_csv("datasets/NationalNames.csv")
address = pd.read_csv("datasets/list_of_real_usa_addresses.csv")
brand = pd.read_csv("datasets/brand.csv")
product = pd.read_csv("datasets/BigBasketProducts.csv")
comment = pd.read_csv("datasets/shopee_reviews.csv", low_memory=False)
range_coupon = ("except Africa", "recept BUPT", "only Beijing", "only USA")
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

"""
ID prefix in first digit
    1:auto-inserted data
    2:manually inserted data for testing
"""
mode = 1


def get_coupon_id(i):
    # num = random.randint(0, 1)
    if i % 2 == 0:
        return get_id(i, first_digit['discount_coupon'])
    else:
        return get_id(i, first_digit['free_shipping_coupon'])


def get_address():
    while True:
        addressout = fake.address()
        addressout = addressout.replace('\n', ' ')
        if len(addressout) <= 44:
            return addressout


def get_u_name(numIn):
    str1 = str(name.iat[numIn % 1800000, 1])

    # print(str1)
    return str1


fake = faker.Faker()


def get_s_name(numIn):
    return brand.iat[numIn % 500, 0]


def get_p_url():
    return fake.lexify(text='https://????????????/???.png')


def get_s_category():
    return product.iat[random.randint(0, 2000), 2]


def get_p_name(numIn):
    str_out = product.iat[numIn, 1]
    str_out = str_out.replace("\'", "")
    return str_out[0:44]


def get_p_category(numIn):
    return product.iat[numIn, 2]


def get_l_state():
    return random.randint(1, 3)


def get_l_time():
    return fake.date_this_decade()


def get_l_inc():
    index1 = random.randint(0, 5)
    compane = ["UPS", "Deutsche Post", "FedEx", "C. H. Robinson", "XPO Logistics", "J.B. Hunt"]
    return compane[index1]


def get_id(i, category_int):
    return mode * 100000000 + category_int * 10000000 + i


def get_o_time():
    return fake.date_time_this_decade()


def get_c_time():
    return fake.date_time_this_decade()


def get_comment():
    while True:
        commentout = comment.iat[random.randint(1, 400), 1]
        commentout = commentout.replace('\n', ' ')
        commentout = commentout.replace('\'', ' ')
        commentout = emoji.demojize(commentout)
        if len(commentout) <= 44:
            print(commentout)
            return commentout


def get_coupon_start():
    return fake.date_time_between()


def get_coupon_end():
    return str(fake.future_date("+999d")) + " 00:00:00"
