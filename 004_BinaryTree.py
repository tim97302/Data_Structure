class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def setLeft(self,left):
        self.left=left
    def setRight(self,right):
        self.right=right
    @classmethod
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            if p.val==q.val:
                return True and Node.isSameTree(p.left,q.left) and Node.isSameTree(p.right,q.right)
            else:
                return False
    @staticmethod
    def show(p):
        p_right=p
        if p == None:
            print('Empty!')
        while  p:
            print(p.val,end=',')
            p = p.left
        print('over!')
        while p_right:
            print(p_right.val,end=',')
            p_right=p_right.right
        print('over!')
if __name__=="__main__":
    #build tree
    p1=Node('A')
    root_p=p1
    p2=Node('B')
    p3=Node('C')
    p4=Node('D')
    p5=Node('E')
    p7=Node('F')
    p1.setLeft(p2)
    p1.setRight(p3)
    p2.setLeft(p4)
    p2.setRight(p5)
    p3.setRight(p7)
    q1=Node('A')
    root_q=q1
    q2=Node('B')
    q3=Node('C')
    q4=Node('D')
    q5=Node('P')
    q7=Node('F')
    q1.setLeft(q2)
    q1.setRight(q3)
    q2.setLeft(q4)
    q2.setRight(q5)
    q3.setRight(q7)
    Node.show(q1)
    Node.show(q1)
    ans=p1.isSameTree(p1,q1)
    print(ans)