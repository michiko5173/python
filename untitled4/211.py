from twilio.rest import Client
accountSID = 'AC2f277c1548bdabafd72dbd105cca5211'
authToken = '1d6503e2cbc71175bfb86e207602aac6'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+7067487396'
myCellPhone = '+8615858865173'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I wantto see you.', from_=myTwilioNumber, to=myCellPhone)