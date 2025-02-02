from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class Google_auth(UserAuthentication):
    def login(self):
        print("Logged in using Google")

    def logout(self):
        print("Logged out from Google")

class Facebook_auth(UserAuthentication):
    def login(self):
        print("Logged in using Facebook")

    def logout(self):
        print("Logged out from Facebook")

google=Google_auth()
facebook=Facebook_auth()

google.login()
google.logout()

facebook.login()
facebook.logout()
