#Deze werkt!

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
        

zoekpad = "C:/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/asr"
#zin = "Er werd al sinds aan het viaduct gebouwd ".lower() #lowercase gemaakt. 
#zin = "achttien"

zin = "nederland gaat de oorlog winnen"


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
            

print "done!"
print len(lijst_soundbites)

for woorden in lijst_niet_gevonden:
    print 'het volgende woord is niet gevonden: ' + woorden


    
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
    print str(objecten.bestandsnaam)
    sound = AudioSegment.from_mp3("C:/Dropbox/Studie/Master/Master Thesis/Python Bloemendal/audiofragmenten/" + str(objecten.bestandsnaam) + '.mp3')
    exportsound = sound[objecten.begintijd:objecten.eindtijd]
    exportsound.export("C:/export/" + objecten.woord + ".mp3", format="mp3")
    sound_concatenate = sound_concatenate + sound[objecten.begintijd:objecten.eindtijd] + empty
    
sound_concatenate.export("C:/export/final3.mp3", format="mp3")
print "done!"
