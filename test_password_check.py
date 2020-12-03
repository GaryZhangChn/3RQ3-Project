from pwdck import Pwdck
from user import User


def test_check_letter():
    user1 = User('abc','user1')
    user1pwdcheck = Pwdck(user1.pwd)
    user1pwdcheck.check_letter()
    assert user1pwdcheck.hasletter, "this password doesn't contain letters!!!"

def test_check_number():
    user2 = User('123', 'user2')
    user2pwdcheck = Pwdck(user2.pwd)
    user2pwdcheck.check_number()
    assert user2pwdcheck.hasnumber, "this password doesn't contain numbers!!!"

def test_check_priv():
    user1 = User('adc1','user1')
    user1.priv = False
    user2 = User('a123','user2')
#    assert user1.priv, "this user has selected using private album!!!"
    assert user2.priv, "the default pricacy preference should be public!!!"