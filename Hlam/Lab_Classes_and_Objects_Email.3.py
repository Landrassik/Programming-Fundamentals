class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.s = sender
        self.r = receiver
        self.c = content
        self.i = is_sent


    def send(self):
        self.i = True


    def get_info(self):
        return f"{self.s} says to {self.r}: {self.c}. Sent: {self.i}"


emails = []
line = input()

while line != 'Stop':
    line = line.split()
    s = line[0]
    r = line[1]
    c = line[2]
    email = Email(s, r, c)
    emails.append(email)
    line = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())