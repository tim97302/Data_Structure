class ListNode(object):
    def __init__(self, value, next=None,head=None):
        self.val = value
        self.next = next
        self.head = head
    def show(self): # 遍歷連結串列
        print('連結串列元素如下：')
        p = self.head
        if p == None:
            print('Empty!')
        while  p:
            print(p.val,end=',')
            p = p.next
        print('over!')
    def insert(self,pos):
        p=self.head
        if pos==1:
            self.head=ListNode(self.val)
            self.head.next=p
        n=2
        while pos>n and p.next!=None:
            p=p.next
            n+=1
        if n==pos:
            tmp=p.next
            p.next=ListNode(self.val)
            print(p.next.val)
            p=p.next
            print(p.val)
            p.next=tmp


if __name__ == "__main__" :
    Node_5 = ListNode(5,None)
    Node_4 = ListNode(4,Node_5)
    Node_3 = ListNode(3, Node_4)
    Node_2 = ListNode(2, Node_3)
    Node_1 = ListNode(1, Node_2)
    Head=ListNode(None,None,Node_1)
    Node_insert=ListNode(15,Node_4,Node_1)
    Node_insert.insert(3)
    Head.show()