from flask import Flask, request
from twilio.rest import Client
import datetime

account_sid = 'AC5c0df5a188c9e3d4d0e222fbe9541f32'
auth_token = 'd1f8d9f67e61ab158cda87ce21516958'
client = Client(account_sid, auth_token)

app = Flask(__name__)

#App Route to get body of a text messages, appends to a text file
@app.route("/sms", methods=['GET', 'POST'])
def sms_record_response():
    #Body of the Text Message
    textbody = request.values.get('Body', None)
    #Creating a timestamp for the message 
    now = datetime.datetime.now()
    nowlist = list(str(now))
    nowlist = nowlist[0:nowlist.index('.')]
    #Opens the file that needs to be appended
    openfile = open('C:/Users/Elvin/Flask_Final/messages.txt','a')
    #String of time + body + newline
    if textbody != None:
        openfile.write(str(''.join(nowlist))+' '+str(textbody)+'\n')
        count =+ 1
    #Close the file to save the message
    openfile.close()
    #Statement to return
    statement = "Last Refresh was at "+str(''.join(nowlist))
    #Return a nice message
    return statement

#App Route to print out all text messages when prompted
@app.route("/file", methods=['GET', 'POST'])
def updated_file():
    #Opens the appended file of messages
    openfile = open('C:/Users/Elvin/Flask_Final/messages.txt','r')
    #Sets message count to 0
    allmessages = ''
    #For each line in the file
    for line in openfile:
        #It forms it into one giant string
        allmessages = allmessages + line
    #Close file
    openfile.close()
    #Return the string
    return allmessages
    

if __name__ == "__main__":
    app.run(debug=True)
