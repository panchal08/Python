class ValidationException(Exception):
    def __init__(self, arg):
        self.msg = arg


class PasswordNotMatchException(Exception):
    def __init__(self, arg):
        self.msg = arg


class Login:
    @staticmethod
    def validation(user, pwd):
        if user == 'admin' and pwd == '12345':
            print('Login Successfully')
        elif not user.isalpha():
            raise ValidationException('Please enter valid USER ID')
        else:
            raise PasswordNotMatchException('USER ID and Password not match')


if __name__ == '__main__':
    user = input('Entre USER ID : ')
    pwd = input('Enter Password : ')
    Login.validation(user, pwd)
