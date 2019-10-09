import hashlib,random,os,stat

length = [1024,5]

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

f,i,s=sumNcut("C:\python-3.7.3-webinstall.exe")
