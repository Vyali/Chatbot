from django.shortcuts import render
import aiml
import os
# Create your views here.


kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

'''if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
    print('brain file present')
else:
    kernel.bootstrap(learnFiles = "std-startup.xml",commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
'''
response_msglist =[]
old_response=[]
def index(request):
    return render(request,'index.html')

def takeinput(request):
    print("in take input")
    user_input = []
    bot_response = []

    old_response = response_msglist
    while True:
        if request.method == 'POST':
            inp_msg = request.POST.get('inpmsg',None)
            user_input.append(inp_msg)
            response_msglist.append(user_input)
            response_msg = kernel.respond(inp_msg)
            if(response_msg):
                bot_response.append(response_msg)
                print(response_msg)
                print(response_msglist)
            else:
                bot_response.append("sorry")
                print("ssorrrry")
            response_msglist.append(bot_response)
        return render(request,'index.html',{'response_msg_list':response_msglist})






        #print(kernel.respond(inp_msg))
        #return render(request, 'index.html', {'outmsg' : kernel.respond(inp_msg)})
        # Create the kernel and learn AIML files


        # Press CTRL-C to break this loop
