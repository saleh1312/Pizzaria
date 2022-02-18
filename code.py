
# to handle the clients
class client:
    def __init__(self,pref,dis_pref):
        self.prefs=pref
        self.dis_pref=dis_pref
        
# to get every client with what they likes and hates
def get_clients(request):
    chunks=request.split("\n")
    num_clients=chunks[0]
    clns=[]
    for i in range(1,int(num_clients)*2,2):
        pref=chunks[i].split(" ")
        pref=pref[1:] if len(pref)>0 else pref
        dis_pref=chunks[i+1].split(" ")
        dis_pref=dis_pref[1:] if len(dis_pref)>0 else dis_pref
        cln=client(pref,dis_pref)
        clns.append(cln)
    return clns
       
# score 
def score(clns,conf):
    sco=0
    for cln in clns:
        s1=0
        if len([item for item in cln.prefs if item in conf])==len([item for item in cln.prefs]):
            s1=1
        s2=0
        if len([item for item in cln.dis_pref if item in conf])==0:
            s2=1
            
        sco+=(s1*s2)
        
    return sco
            
#to get best action in the confusing ingredients 
def recursion(clients,conf,bad):
    
    if len(bad)==0:
        return score(clients,conf),conf
    

    yes_score,c=recursion(clients ,conf+[bad[0]],bad[1:])
    no_score,c=recursion(clients ,conf,bad[1:])
    
    if yes_score > no_score:
        return yes_score,c
    else:
        return no_score,c
    
def get_best(clns):
    good=[]
    bad=[]
    for cln in clns:
        good.extend(cln.prefs)
        bad.extend(cln.dis_pref)
    good=list(set(good))
    bad=list(set(bad))

    confirmed=[item for item in good if item not in bad]
    
    return recursion(clns,confirmed,bad)



def main(reqest):
    clients=get_clients(request)
    ingredients=get_best(clients)[1]

    return(str(len(ingredients))+' '+' '.join(ingredients))

if __name__ =="__main__":
    with open('in\\d_difficult.in.txt') as f:
        request = f.read()
        output=main(request)
        
        with open('out\\d_difficult.out.txt',"w") as w:
            w.write(output)
    
    
    


























