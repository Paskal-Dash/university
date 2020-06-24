def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif (password.isalnum() and not password.isalpha() and not password.isdigit() and (password.islower() or password.isupper())) or (password.isalpha() and (not password.islower() and not password.isupper())):
       return 'Слабый пароль'
    elif password.isalnum() and (not password.islower() and not password.isupper()):
        return 'Надеждный пароль'
    else:
        return 'Ненадежный пароль'


print(password_level('qweRty'))