class Publisher(object):
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)
    def send_notif(self, message):
        for user in self.users:
            user.notify(message)

class Subscriber(object):

    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username + ' received Message:' + message)

publisher = Publisher()

# membuat notif observer telah menerima pesan
sabiq = Subscriber('sabiqxs')
iif = Subscriber('miftah')
publisher.register(sabiq)
publisher.register(iif)


# notifikasi di kirimkan ke setiap observer
publisher.send_notif('kita telah update website ini')
publisher.send_notif('make sure to add a profile picture')