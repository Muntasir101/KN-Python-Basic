import random
import string

coupon_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
coupon_code = ''.join(random.choice(coupon_chars) for i in range(5))
print(coupon_code)