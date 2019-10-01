class CallDetail:
    def __init__(self):
        self.dialer=None
        self.receiver=None
        self.duration=None
        self.calltype=None

    def setdetails(self, y):
        self.dialer=y[0]
        self.receiver=y[1]
        self.duration=y[2]
        self.calltype=y[3]
        self.getdetails()

    def getdetails(self):
        print()
        print(self.dialer.ljust(20), end=" ")
        print(self.receiver.ljust(20), end=" ")
        print(self.duration.ljust(20), end=" ")
        print(self.calltype.rjust(20))


class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self, list_of_call_string):
        #list_of_call_objects=[CallDetail(s) for s in list_of_call_string]
        for x in range(len(list_of_call_string)):
            y=list_of_call_string[x].split(',')
            self.list_of_call_objects.append(CallDetail())
            self.list_of_call_objects[x].setdetails(y)
        


call='9990000001, 9330000001, 23, STD'
call2='9990000001, 9330000001, 54, Local'
call3='9990000001, 9330000001, 6, ISD'


list_of_call_string=[call, call2, call3]

print("Dialer".ljust(20), end=" ")
print("Receiver".ljust(20), end=" ")
print("Duration".ljust(20), end=" ")
print("Type".rjust(20), end=" ")
Util().parse_customer(list_of_call_string)
