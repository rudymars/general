#Herschrijf zin

import re
import sys
from OpenDutchWordnet import Wn_grid_parser
instance = Wn_grid_parser(Wn_grid_parser.odwn)

uitspreekzin = "De minister president is ontevreden"
words_notfound_article = []

class woord_vervang:
    def __init__(self, realpart, imagpart):
             self.origineel = realpart
             self.vervang = imagpart

def lijst_unieke_woorden_nieuw():
    #uniekwoord
    import glob, os
    import xml.etree.ElementTree as ET
    #from pydub import AudioSegment
    num_notfound = 0
    import os
    tempval = os.getcwd()
    




    zoekpad = tempval + "\Python Bloemendal\\asr-out"
    
    zoekpad = "C:/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/asr-out"
    print zoekpad
    lijst_gevonden_woorden = []
    
    os.chdir(zoekpad)
    
    print zoekpad
    for file in glob.glob("*.xml"): #itereer door de map, check alleen xml files
        #print file

        tree = ET.parse(zoekpad + "/" + file)
        root = tree.getroot()


        for woorden in root.iter('word'):
            for child in woorden:
                score = child.get('COMBINED')
            name = woorden.get('wordID')
            
            begintijd = woorden.get('beginTime') 
            eindtijd = woorden.get('endTime')
            lijst_gevonden_woorden.append(name)
            #break

    def remove_duplicates(values):
        output = []
        seen = set()
        for value in values:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output
    #print lijst_gevonden_woorden
    #print len(lijst_gevonden_woorden)
    lijst_gevonden_woorden = remove_duplicates(lijst_gevonden_woorden)
    
    for woord in lijst_gevonden_woorden:
        try:
            woord = woord.decode("utf-8", "replace")

        except ValueError:
            #print "Oops!  That was no valid number.  Try again..."
            pass
            
    
    
    return lijst_gevonden_woorden
    #print len(lijst_gevonden_woorden)

woordenlijst = lijst_unieke_woorden_nieuw()
templist = uitspreekzin.split(" ")
uitspreekwoorden = []
for woord in templist:
    uitspreekwoorden.append(woord)

words_notfound_article = []
lijst_gevonden_woorden = []
lijst_vervangwoorden = []

templist = uitspreekwoorden[:]
for woorden in templist:
    if woorden in woordenlijst:
        lijst_gevonden_woorden.append(woorden)
        uitspreekwoorden.remove(woorden)
    else:
        words_notfound_article.append(woorden)
        
        
print len(lijst_gevonden_woorden),"gevonden woorden"
print len(words_notfound_article),"niet gevonden"
print "---------"
print "Nu verder met synoniemen"
#print len(uitspreekwoorden)
#print lijst_gevonden_woorden

templist = words_notfound_article[:]
#print len(templist)

exitloop = False
for woord in templist[:]:
    synoniemen = instance.lemma_synonyms(woord)
    #print woord
    for synoniem in synoniemen:

        if synoniem in woordenlijst:
            #print synoniem,woord
            vervangwoord = woord_vervang(woord,synoniem)
            print woord,'vervangen met',synoniem
            lijst_vervangwoorden.append(vervangwoord)

            lijst_gevonden_woorden.append(synoniem)
            if woord in words_notfound_article:
                words_notfound_article.remove(woord)
            templist.append(woord)

                # break
            
print len(lijst_gevonden_woorden),"gevonden woorden"
print len(words_notfound_article),"niet gevonden"
print words_notfound_article
print "---------"
print "nu verder met decompounding"

for zoekwoord in words_notfound_article:
    woorden_corpus = woordenlijst[:]


    
    for woord in woorden_corpus:
        if len(woord) > len(zoekwoord):
            woorden_corpus.remove(woord)
            break
            
 


    for woord in woorden_corpus:
            if woord not in zoekwoord:
                woorden_corpus.remove(woord)
                
    for woord in woorden_corpus:
        for letter in list(woord):
            if letter not in zoekwoord:
                woorden_corpus.remove(woord)
                break
                
    input_list = woorden_corpus
    #print len(input_list),"kandidaten voor",zoekwoord


    woord1_loop_exit = False
    for woord1 in input_list:
        if woord1_loop_exit == True:
            break
    
        if woord1 not in zoekwoord:
            continue
        for woord2 in input_list:
            if woord2 not in zoekwoord:
                continue
            if woord1+woord2 == zoekwoord:
                #bigram gevonden
                if zoekwoord in words_notfound_article:
                    words_notfound_article.remove(zoekwoord)
                    lijst_gevonden_woorden.append(woord)
                    woord1_loop_exit = True
                    #print zoekwoord ,"kan worden gemaakt uit:"
                    #print woord1,woord2
                    tempvalue = woord1 + " " + woord2
                    vervangwoord = woord_vervang(zoekwoord,tempvalue)
                    lijst_vervangwoorden.append(vervangwoord)
                    break

            for woord3 in input_list:
                if woord3 not in zoekwoord:
                    continue
                if woord3 in zoekwoord:
                    if woord1+woord2+woord3 == zoekwoord:
                        if zoekwoord in words_notfound_article:
                            words_notfound_article.remove(zoekwoord)
                            lijst_gevonden_woorden.append(woord)
                            woord1_loop_exit = True
                            #print zoekwoord ,"kan worden gemaakt uit:"
                            #print woord1,woord2,woord3
                            tempvalue = woord1 + " " + woord2 + " " + woord3
                            vervangwoord = woord_vervang(zoekwoord,tempvalue)
                            lijst_vervangwoorden.append(vervangwoord)
                            break
                            
print len(lijst_gevonden_woorden),"gevonden woorden"
print len(words_notfound_article),"niet gevonden"
print "---------"

#for vervangwoord in lijst_vervangwoorden:
#    print vervangwoord.origineel,'vervangen met',vervangwoord.vervang

print "originele zin:",uitspreekzin
    
templist = uitspreekzin.split(" ")
tempsentance = "" 

for vervangwoord in lijst_vervangwoorden:
    uitspreekzin = uitspreekzin.replace(vervangwoord.origineel,vervangwoord.vervang)
    
print "uitspreekbare zin:",uitspreekzin
    
import glob, os
import xml.etree.ElementTree as ET
from pydub import AudioSegment

class soundbite:
    def __init__(self, woord, begintijd, eindtijd,bestandsnaam,score):
        self.woord = woord #het woord zelf
        self.begintijd = begintijd #milliseconden
        self.eindtijd = eindtijd #milliseconden
        self.bestandsnaam = bestandsnaam #bestandsnaam waar het fragment in zit.
        self.score = score
        

zoekpad = "C:/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/asr-out"
#zin = "Er werd al sinds aan het viaduct gebouwd ".lower() #lowercase gemaakt. 
#zin = "achttien"

zin = uitspreekzin


lijst_soundbites = []
lijst_zoekwoorden = zin.split(' ')
lijst_niet_gevonden = zin.split(' ')

os.chdir(zoekpad)

for file in glob.glob("*.xml"): #itereer door de map, check alleen xml files
           
    tree = ET.parse(zoekpad + "/" + file)
    root = tree.getroot()

    
    for woorden in root.iter('word'):
        for child in woorden:
            score = child.get('COMBINED')
        name = woorden.get('wordID')
        begintijd = float(woorden.get('beginTime'))
        eindtijd = float(woorden.get('endTime'))
        
        for zoekwoorden in lijst_zoekwoorden:
                #buffer eindtijd is aantal milliseconden plus en minus
                buffer = 20
                buffer_voor = 10
                if name == zoekwoorden:
                    #print "score van gevonden woord: " + score
                    begintijd = ((float(begintijd)) * 1000) - buffer_voor
                    eindtijd = ((float(eindtijd)) * 1000) + buffer
                    #^zorgt ervoor dat begintijd een float is. 
                    #print name + " is gevonden in " + file.split('.')[1]    
                        
                          
                    x = soundbite(name,begintijd,eindtijd,file.split('.')[1],score)
                    lijst_soundbites.append(x)        
                    #print x.woord,'is toegevoegd aan de lijst'
                    for soundbites in lijst_soundbites:
                        if soundbites.woord == x.woord:
                            if soundbites.score < x.score: #Als een woord meerdere keren gevonden wordt, pak dan degene met het hoogste acoustische score
                                lijst_soundbites.remove(soundbites)
                                
                            if soundbites.score > x.score:
                                if x in lijst_soundbites:
                                    lijst_soundbites.remove(x)
                                
                                
                                
                    #
                    #print 'nieuw woord toegevoegd: ' + x.woord + ' met score ' + x.score
                            #print gevonden.score + " en " + score
                    
                    if zoekwoorden in lijst_niet_gevonden: lijst_niet_gevonden.remove(zoekwoorden)
            

#print "done!"
#print len(lijst_soundbites)

#for woorden in lijst_niet_gevonden:
#    print 'het volgende woord is niet gevonden: ' + woorden


    
#het sorteren van de lijst:
lijst_fragmenten = []
for woorden in zin.split(' '):
    for objecten in lijst_soundbites:
        if woorden == objecten.woord:
            lijst_fragmenten.append(objecten)
            
AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe" #ik weet niet of dit optioneel is.
AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
sound = AudioSegment.silent(duration=10)
sound_concatenate = sound[0:1] #een begin maken voor het contateneerbestand
#empty = AudioSegment.silent(duration=100) #leeg geluidsfragment tussen woorden
empty = AudioSegment.silent(duration=100) #leeg geluidsfragment tussen woorden

for objecten in lijst_fragmenten:
    #print objecten.woord
    #print objecten.bestandsnaam
    #print objecten.begintijd
    #print objecten.eindtijd
    #sound = AudioSegment.from_mp3("C:/Users/Rudy/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/audiofragmenten/" + str(objecten.bestandsnaam) + '.mp3')
    #print str(objecten.bestandsnaam)
    sound = AudioSegment.from_mp3("C:/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/audiofragmenten/" + str(objecten.bestandsnaam) + '.mp3')
    exportsound = sound[objecten.begintijd:objecten.eindtijd]
    exportsound.export("C:/export/" + objecten.woord + ".mp3", format="mp3")
    sound_concatenate = sound_concatenate + sound[objecten.begintijd:objecten.eindtijd] + empty
    
sound_concatenate.export("C:/export/testzin_minpres2.mp3", format="mp3")
print "done! het audiobestand staat in je C schijf"    
    
    