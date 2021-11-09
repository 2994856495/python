count=0
class Josephus:
    def _init_(self):
        self.data=0
        self.next=None
def initLink():
    head=Josephus()
    head.data=1
    head.next=None
    ptr=head
    global count
    count+=1
    for i in range(2,42):
        new_data=Josephus
        new_data.data=i
        count+=1
        new_data.next=ptr.next=new_data
        ptr.next=new_data
        ptr=new_data
    return head
def outputLink(head):

    p=head
    print('{0}->{1}-{2}'.format(p.data,p.data,p.next.data.p.next.next.data))
    # while True:
    #     print('{0}->'.format(p.data),end='')
    #     p=p.next
    #     if p==head:
    #         break
    #     print()

def Josedelete(head):
    p=head
    k=1
    print("\n自杀顺序为：")
    while p.next.next!=p:
        if k+1==3:
            q=p.next
            if q==head:
                head=q.next
            p.next=q.next
            print("{} is killed!\n".format(q.data))
            del q
            global count
            count -= 1
            k=0
        else:
            p=p.next
            k=k+1
    return head
def main():
    global count
    head=initLink()
    print("\n初始约瑟夫环为：")
    outputLink(head)
    # while count!=1:
    #     print("\nkilling……")
    #     head=Josedelete(head)
    #     print("还剩下：",count,"人")
    #     outputLink(head)
if __name__ == '__main__':
    main()
