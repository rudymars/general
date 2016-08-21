def lijst_unieke_woorden_nieuw():
    #uniekwoord
    import glob, os
    import xml.etree.ElementTree as ET
    #from pydub import AudioSegment
    num_notfound = 0
    import os
    tempval = os.getcwd()
    




    zoekpad = tempval# + "\Python Bloemendal\\asr-out"
    
    zoekpad = zoekpad
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
            #name = name.decode("utf-8", "replace")#Decodeer en fix die shit met trema's
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
    print len(lijst_gevonden_woorden)
test = lijst_unieke_woorden_nieuw()