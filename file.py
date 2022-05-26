import nexmo 

client = nexmo.Client(key='ed320a43',secret='OlUMCY1dswQYQ9FD')
 
client.send_message({
     "from": "nexmo",
     "to": "989926834697",
     "text": "TEST",
})