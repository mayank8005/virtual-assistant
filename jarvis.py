import datetime

class Mind:

    __name = ''
    __age = 0
    __username = ''

    def __init__(self,uname):
        if uname=="":
            uname ='user'
        self.__name = 'jarvis'
        self.__age = 0
        self.__username = uname
        self.greet(1)

    def __userInfo(self,mode):
        if mode ==1 and self.__username != 'user':
            print('your name is ' + self.__username)
        elif mode ==1 and self.__username == 'user':
            print("sorry i don't know your name....")

    def greet(self,mode):
       if mode == 1:
            print("HELLO "+ self.__username +" , i am " + self.__name + " how can i help you ?")
       elif mode ==2:
           print('i am great ,thank you !')
       elif mode == 3:
           print('my name is ' +self.__name)
       elif mode == 4:
           print('')


    def __temperature(self):
        print('currently this service is not active')

    def __exit(self):
        print('bye '+self.__username)
        exit(0)

    def __displayTime(self):
        print('current time is '+ str(datetime.datetime.now().time()))
    def __unableToUnderstand(self):
        print('unable to understand , i need an upgrade')

    def commandThinker(self,request):

           if 'hello' in request or 'hey' in request :
               if 'how' in request :
                   self.greet(2)
               else:
                   self.greet(1)


           elif 'how' in request or "how's" in request :
               if 'you' in request:
                   self.greet(2)
               elif 'temperature' in request or 'weather' in request:
                   self.__temperature()
               else:
                   self.__unableToUnderstand()





           elif 'temperature' in request or 'weather' in request:
               self.__temperature()


           elif 'what' in request or 'whats' in request or "what's" in request:
               if 'my' in request and 'name' in request:
                   self.__userInfo(1)
               elif 'your' in request and 'name' in request:
                    self.greet(3)
               elif 'time' in request:
                   self.__displayTime()
               else:
                   self.__unableToUnderstand()

           elif 'time' in request:
               self.__displayTime()



           elif 'exit' in request or 'bye' in request:
               self.__exit()



           else:
               self.__unableToUnderstand()



print('whats your name buddy ?')
brain = Mind(input())
while(1):
    command = input()
    command = command.lower()
    brain.commandThinker(command)


