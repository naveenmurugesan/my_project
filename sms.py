import time
import datetime
from sinchsms import SinchSMS
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
def sendsms(name):
        number='+918940241339'
        #number = '+919524272446'
        #number = '+919159812210'
        #number = '+918667617235'
        message =name +' JUST CROSSED THE CAMERA at ' + str(now)
        #client= SinchSMS('
        client = SinchSMS('28717cde0dc7410fb3c2373b0bdec924','398988aaa43b4b1fa4340eef49097fbe')
        #client = SinchSMS('6a636257-e492-4eb3-b84a-7d45754c3683','qPbCkDBB9USs13fjo3MGuw==')
        #balaji client= SinchSMS('94619236-7c30-49e3-8eb9-bd944ff9dafb','WiLPttLCt0aO13MFrGykFA==')
        print("sending '%s' to %s" % (message,number))
        response = client.send_message(number,message)
        message_id = response['messageId']
        response = client.check_status(message_id)
        while response['status'] != 'successfull':
            print(response['status'])
            time.sleep(1)
            response = client.check_status(message_id)
           # print(response['status'])
            break
        return True

