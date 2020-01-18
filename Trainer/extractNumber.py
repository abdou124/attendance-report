import os,glob
import re

def extract(strPath):
    os.chdir(strPath)
    sessions={}
    cpt=0
    for file in glob.glob(("*.txt")):
        f1= open(file,"r")
        cpt+=1
        line = f1.readline()
        s="session"+str(cpt)
        sessions[s]=[]
        while line :
            s1 = re.findall(r"\d{10}",line)
            if s1 != []:
              sessions.get(s).append(s1)
            line = f1.readline()
    return sessions
