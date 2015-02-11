class Carddeck:
    #instance vars 
    import random
    values={2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"T",11:"J",12:"Q",13:"K",14:"A"}
    suits={1:"C",2:"S",3:"D",4:"H"}
    
    index=0
    card=""#2 char string of values and suit
    
    def __init__(self,value="",suit=""):        
        self.value=value
        self.suit=suit

    def __repr__():#return string with deck displayed as list
        i=0
        j=0
        for i in suits:
            for j in values:
                card[i*j]=card[i*j] + suits[i],",", values[j]
                return suits[i],",", values[j]

    def shuffle():
        i=0
        for i in len(self.card):
            self.card[i]=random.shuffle() 
            self.card[i+1].index=0

    def dealcard():
        for i in len(self.card):
            return self.card[i+1]


    

    def dealhand():
        return Pokerhand(list(self.card[0], self.card[1], self.card[2], self.card[3], self.card[4]))


class Pokerhand(Carddeck):
    a=Carddeck()
    ranking={0:'High card',
                 1:'One pair',
                 2:'Two pair',
                 3:'Three of a kind',
                 4:'Straight',
                 5:'Flush',
                 6:'Full house',
                 7:'Four of a kind',
                 8:'Straight flush'}
     
    def __init__(self,clist):
        self.clist=clist
        

    def __repr__(self):#returns all elements of 5 hand
        for i in self.clist:
            return i

    def rank():
        maxval = max(dealhand())
        minval = min(dealhand())
        if len(self.clist) < 5:
            print ("length isn't five")
        rank = 0
        for i in clist:
            if i.a.value in values:
                if len(i.a.dealhand()) == 5:
                    return ranking[1]
                elif len(i.a.dealhand()) == 3:
                    if not 3 in i.a.dealhand():
                        return ranking[2]
                    else:
                         return ranking[3]
                elif len(i.a.dealhand()) == 2:
                    if 2 in len(i.a.dealhand()):
                        return ranking[6]
                    else:
                        return ranking[7]
                elif len(i.a.dealcard().suit) ==1 and maxval - minval == 4 :
                    return ranking[4]
                elif len(set(i.a.dealcard().suit)) == 1:
                    return ranking[5]
                else:
                    return ranking[8]



def main():
    obj = Carddeck()
    ranking={0:'High card',
                 1:'One pair',
                 2:'Two pair',
                 3:'Three of a kind',
                 4:'Straight',
                 5:'Flush',
                 6:'Full house',
                 7:'Four of a kind',
                 8:'Straight flush'}          
    for i in range(100,000):
        for i in range(9):
            print (ranking[i],":",max(obj.dealhand().rank()))
