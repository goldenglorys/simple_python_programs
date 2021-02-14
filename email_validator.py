# import re
#
# user_email = input("Enter the email you wanted to validate:\n")
#
# while True:
#     if validate_email(user_email):
#         print('Validation successful')
#         break
#     else:
#         print('Invalid! Try again')
#         user_email = input("Enter the email you wanted to validate:\n")
# 
#
# def validate_email(email):
#     if len(email) > 5:
#         return bool(re.match("^.+@(/[?)[a-zA-Z0-9-.]+.([a-zA-Z{2,3}|[0-9]{1,3})(]?)$", email))
