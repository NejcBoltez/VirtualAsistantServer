import random
import time
import os
import webbrowser
#import wolframalpha
import wikipedia
import urllib.parse as urllib

new = 2
ukaz = [""]
izgovorjeno=[""]

class AI():
    
    def saveResponse(self,response):
        self.response = response;
        BASE_DIR= os.path.dirname(os.path.abspath(__file__))
        file_to_open=os.path.join(BASE_DIR, "allCommands.txt")
        allCommands = ""
        with open(file_to_open,"r") as f_w:
            allCommands = f_w.read()
        with open(file_to_open,"w") as f_w:
            print(str(allCommands) + str(self.question) + ";")
            f_w.write(str(allCommands) + str(self.question) + ";")
    def datoteka(self):
        a = "How shuld I named the document"
        '''self.saveResponse(a)
        ime = #self.posluh()
        d = "What shuld I write in the document"
        self.saveResponse(d)
        vno = #self.posluh
        novdoc = gTTS(text=vno, lang='en')
        imedat = ime + ".txt"
        novdoc.save(imedat)'''
    def searchWiki(self,vpras):
        odgovor = wikipedia.summary(vpras, sentences = 2)
        self.saveResponse(odgovor)
        print (odgovor)
    def quest(self):
        vprasanja= [' ']
        que = 0
        while True:
            vpras = ""
            h = 0
            if que == 0:
                vr = "What is your question?"
            else:
                vr = "Do you have any more questions?"
            self.saveResponse(vr)
            que+=1
            vn = input("What is your question: ")
            if vn == "":
                vn = input("What is your question: ")
                self.saveResponse(vn)
            data = "Accesing the data. Please wait."
            self.saveResponse(data)
            vra = vn.split(" ")
            for y in vra:
                if y == "he" or y == "she" or y == "it":
                    if h == 0:
                        vpras += y + " "
                    else:
                        vp = self.wiki(vprasanja[len(vprasanja) - 1])
                        vpras += vp
                elif  y == "thank" or y == "thanks":
                    tha="You are welcome."
                    self.saveResponse(tha)
                elif y == "question":
                    h = 0
                else :
                    if y == vra[len(vra)-1]:
                        vpras += y + "."
                    else:
                        vpras += y + " "

            vprasanja.append(vpras)
            #try:
            #    app_id = "L82GJK-J6W72HEX54"
            #    client = wolframalpha.Client(app_id)
            #    res = client.query(vpras)
            #    answer = next(res.results).text
                #self.saveResponse(answer)
            #    print answer
            #except:
            #wikipedia.set_lang("")
            odgovor = wikipedia.summary(vpras, sentences = 2)
            self.saveResponse(odgovor)
            print (odgovor)
    def james(self,resp2):
            lis = ("Hello", "hello", "Wikipedia", "Google", "day", "hate", "of", "do not", "don't", "thanks", "map","maps", "search", "facebook", "new", "document", "folder", "alarm", "good", "how", "identify", "identified", "thank", "shutdown", "on", "lights", "living", "room", "my", "reminders", "reminder", "for", "music", "flip", "coin", "off", "shut", "up", "don't", "jokes", "email", "note", "problem", "bye", "time","calendar","morning","web","Alexa", "date", "YouTube", "question", "are", "smart", "stupid", "getting", "smarter", "name", "doing","who", "what", "where","who's", "what's", "where's")
            self.question = resp2
            self.response = ""
            print (resp2)
            izgovorjeno.append(resp2)
            male = resp2.lower()
            vnos = resp2.split(" ")
            vneseno = [" "]
            besedilo = ""

            for word in vnos:
                for x in lis:
                    if word == x:
                        vneseno.append(x)
                        besedilo += x + " "
            ukaz.append(besedilo)

            for z in range(0,len(vneseno)):
                esa = vneseno[z]
                if esa == "email":
                    b = random.choice(("email ok then", "ok. Whats your email adress", "what should I write in email"))
                    print (b)
                    self.saveResponse(b)
                elif esa == "hello" or esa == "Hello":
                    he = "Hello to you too"
                    self.saveResponse(he)
                elif esa == "do not":
                    #z+=1
                    continue
                elif esa == "don't":
                    #z+=1
                    continue
                elif esa == "James":
                    h = random.choice(("Hello I am James. I am waiting for your command", "Hy sir. What should I do for you"))
                    self.saveResponse(h)
                elif esa == "date" or esa == "day":
                    date = time.strftime("%A, %B %d %Y ")
                    izpis = "Today it is "+date
                    print (izpis)
                    self.saveResponse(izpis)
                elif esa == "time":
                    h = str(int(time.strftime("%H")))
                    m = str(int(time.strftime("%M")))
                    s = str(int(time.strftime("%S")))
                    g= "Current time is " + m + " past " + h + " and " + s + " seconds"
                    self.saveResponse(g)
                elif esa == "question":
                    self.quest()
                elif esa == "morning":
                    g = "Good morning, Nejc. Have a wonderful day."
                    self.saveResponse(g)
                    print (g)
                elif esa == "YouTube":
                    speak = "Opening youtube"
                    #self.saveResponse(speak)
                    url = "https://www.youtube.com/"
                    webbrowser.open(url, new=new)
                elif esa == "facebook":
                    speak = "Opening facebook"
                    #self.saveResponse(speak)
                    url = "https://www.facebook.com/"
                    webbrowser.open(url, new=new)
                elif esa == "jokes":
                    c = random.choice(("I do not know any joke", "Knock Knock"))
                    print (c)
                    self.saveResponse(c)
                elif esa == "problem":
                    t= random.choice(("I do not know how to help you", "What should I do about it."))
                    print (t)
                    self.saveResponse(t)
                elif esa == "web":
                    print ("opening chrome!!")
                    webspeak = "Opening webbrowser"
                    self.saveResponse(webspeak)
                    url = "https://www.google.com"
                    webbrowser.open(url, new=new)
                elif esa == "bye":
                    m = random.choice(("Goodbye", "See you later sir"))
                    self.saveResponse(m)
                elif esa == "alarm":
                    ala = "On what time should I set an alarm."
                    self.saveResponse(ala)
                elif esa == "good":
                    dobr = "That is very nice to hear. Should I do anything else for you?"
                    self.saveResponse(dobr)
                    break
                elif esa == "shutdown":
                    shut = "Shutting down ..."
                    self.saveResponse(shut)
                elif esa in ("who", "what", "where"):
                    q= ""
                    findQuestion=False
                    for m in vnos:
                        if (findQuestion):
                            q += m
                        if (m == "is"):
                            findQuestion = True
                        if (m in ("who's", "what's", "where's")):
                            findQuestion = True
                    self.searchWiki(q)
            if besedilo == "are smart ":
                smartass = "Thank you sir."
                self.saveResponse(smartass)
            elif besedilo == "flip coin ":
                coin = random.choice(("I got heads.", "I got tails."))
                self.saveResponse(coin)
            elif besedilo == "are stupid ":
                stupido = "Well in that case you programmed me to be stupid."
                self.saveResponse(stupido)
            elif besedilo == "are getting smarter ":
                sma = "I learn of my mistakes, sir."
                self.saveResponse(sma)
            elif besedilo == "name ":
                name = "My name is James"
                self.saveResponse(name)
            elif besedilo == "search Google for ":
                t=0
                iskanje=""
                for k in vnos:
                    if k == "for":
                        t+=1
                        continue
                    if t == 1:
                        if k == vnos[len(vnos)-1]:
                            iskanje+= k
                        else:
                            iskanje+= k+" "
                print (iskanje)
                encoded = urllib.quote(iskanje)
                webbrowser.open("https://www.google.si/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="+encoded)
            elif besedilo == "search Wikipedia for ":
                ig=0
                wiki=""
                for m in vnos:
                    if m == "for":
                        ig+=1
                        print (m)
                        continue
                    if ig == 1:
                        if m == vnos[len(vnos)-1]:
                            wiki+= m
                        else:
                            wiki+= m+" "
                print (wiki)
                encoded = urllib.quote(wiki)
                webbrowser.open("https://sl.wikipedia.org/wiki/"+encoded)
            elif besedilo == "hate ":
                sov= "I hate you to."
                self.saveResponse(sov)
            elif besedilo == "how are ":
                pocutje = "I am very good. What about you?"
                self.saveResponse(pocutje)
            elif besedilo == "identify ":
                description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
                self.saveResponse(description)
            elif besedilo == "identified ":
                description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
                self.saveResponse(description)
            elif besedilo == "are doing ":
                delo = "I am waiting for your command, sir."
                self.saveResponse(delo)
            elif besedilo == "do something":
                de = "What should I do for you?"
                self.saveResponse(de)
            elif besedilo == "music ":
                a = "playing music"
                self.saveResponse(a)
                #os.system("start C:/Users/nejcb/Desktop/seznam.xspf")
            elif besedilo == "new file ":
                self.datoteka()
            elif besedilo == "new document ":
                self.datoteka()
            elif besedilo == "off lights living room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.saveResponse(predvajaj)
            elif besedilo == "on lights living room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.saveResponse(predvajaj)
            elif besedilo == "off lights my room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.saveResponse(predvajaj)
            elif besedilo == "on lights my room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.saveResponse(predvajaj)
            elif besedilo == "":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.saveResponse(predvajaj)
            elif besedilo == "map of " or besedilo == "maps of ":
                mesto = ""
                z=0
                zemla = "Openning google maps."
                self.saveResponse(zemla)
                for i in vnos:
                    if i == "of":
                     z+=1
                     continue
                    if z == 1:
                        if i == vnos[len(vnos)-1]:
                            mesto+= i
                        else:
                            mesto+= i+" "
                city = urllib.quote(mesto)
                zemljevid= "https://www.google.de/maps/"
                webbrowser.open("https://www.google.de/maps/place/"+city)
            elif besedilo == "thank " or besedilo == "thanks ":
                izgovor="You are welcome"
                self.saveResponse(izgovor)
#AI()
