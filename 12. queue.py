class QueueError(IndexError): #creating a class and inheriting IndexError exception
    pass


class Queue: #creating another class
    def __init__(self): #initilizing with a constructor
        self.queue = [] # a list called queue init with empty list

    def put(self, elem): #put takes eliment and insert it in our queue list
        self.queue.insert(0, elem) #insertion done from the front (our queue item is entering from the front aand remove from back)

    def get(self):      
        if len(self.queue) > 0: #if something is in list aka len >0
            elem = self.queue[-1] #get me that last one
            del self.queue[-1]     #remove it 
            return elem
        else:
            raise QueueError #if error rais index error 


que = Queue() #create queue obj
que.put(1)  #we call our put fn to insert 1 dog and False into our queue
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get()) #iterate the item and invoke get which returns and remove a list item
except:
    print("Queue error") #this will be called bc we iteratored more thean items in list
    