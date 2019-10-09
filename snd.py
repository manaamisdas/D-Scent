# pseudocode datei slice and dice. muss noch übersetzt werden
# zerhackt dateien und stellt diesen stuecken ggf. etwas müll voran
# speichert schnippsel (als zahl?) in datenbank (am besten ohne muell, den muell kann man ja auch noch spaeter hinzufuegen)
# erstellt db-eintrag mit allen bekannten eigenschaften der datei
# soll trainingsdaten 


# anregungen: 	- netz bekommt blick einmal durch umgebungsblick auf zahl repraesentiert von n-bytes. wobei n so gewahlt wird, dass min. 4*n lueckenlos in float repraesentiert werden kann 
#					(   so das jede information mehrmals eingelesen wird. z.b.: n=11 => erstes neuron bekommt als input float(concathex(5*random,1.byte,2.byte,3.byte,4.byte,5.byte,6.byte))  )
#				- zweiter blick durch clustersehen, der (z.b. summe)

import db
import json,os,stat



listOfFiles = $1
length = [1024,0] #standart length of each slice/chunk and double defiation
junklength = [0,40]
junk_generate_from_files = False #or listOfFiles, File
junkdist = even #or distribution curve function or pseudorandom
junkpatterns = [a4,b,f,affe] #hex, which repeatfills

def slice(listOfFiles):
	file = listOfFiles.pop 
	l = file.length()

	dd if=


# uploads chunk 
def put(file={"original_file_hash":,"groesze_k":10,"type":"picture","subtype":"svg","comment":"testdata","encrypted":False,"chunklenght_b":1024},db="http://ae.hopto.org/sod/",chunk=bytes([0x13, 0x00, 0x00, 0x00, 0x08, 0x00]):



def read(file):


import hashlib

# returns sha256 hash of file and file itself in array of mermoryview(bytearray)
# maybe later for performance remove memoryview wrapping
def sumNcut(filename):
	file_stats = os.stat(filename)
    h  = hashlib.sha256()
    file = []
    b  = bytearray(length[0]+random.randint(length[1]*-1,length[1])) #128*1024=causal speed efficient
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
            file.append(mv)
            mv = memoryview(bytearray(length[0]+random.randint(length[1]*-1,length[1])))
            #print (mv.nbytes)
    file_info = {"original_file_hash":h.hexdigest(),
    				"original_file_name":filename,
    				"groesze":file_stats[stat.ST_SIZE],
    				"type":"picture",
    				"subtype":"svg",
    				"comment":"testdata",
    				"encrypted":False}
    return (file,file_info,file_stats)
