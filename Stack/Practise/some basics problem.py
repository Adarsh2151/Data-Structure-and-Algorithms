

"""
There is simple approach 
for cpp - first empty the stack then after add them by needed operation

for python - Take a list store the open and check for close then some logic


So . I am not writing all approach


"""


def DeleteMiddleFromStack():    

    problem_link = "https://www.codingninjas.com/codestudio/problems/   delete-middle-element-from-stack_985246"   

    solution = """ 
    void deleteMiddle(stack<int>&inputStack, int N,int c = 0){
        if (inputStack.empty()){
            return ;
        };  
	if (N/2 == c){
            inputStack.pop();
            return ;
        }
        int n = inputStack.top();
        inputStack.pop();
        deleteMiddle(inputStack,N,c+1);

        inputStack.push(n);
    
    }

"""



def ValidParentheses():
    problemLink = "https://www.codingninjas.com/codestudio/problems/valid-parenthesis_795104"
    solution = """
    def isValidParenthesis(expression):

        # Write your code here.
        l = list()
        open = {"(":")","{":"}","[":"]"}

        for i in expression:
            if i in open.keys():
                l.append(i)
            else:
                if l == []:
                    return False
                if i == open[l[-1]]:
                    l.pop()
                else:
                    
                    return False
        return True if l == [] else False

    
    
    
    
    """
    


def Insert_An_Element_At_Its_Bottom_In_A_Given_Stack():
    
    problem_link = "https://www.codingninjas.com/codestudio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166"

    solution = """
    stack<int> pushAtBottom(stack<int>& st, int x) 
    {
        if (st.empty()){
            st.push(x);
            return st;
        };
        int n = st.top();
        st.pop();
        pushAtBottom(st,x);
        st.push(n);
        return st;
    }

    
    
    
    """
    
def Reverse_Stack_Using_Recursion():
    problem_link = "https://www.codingninjas.com/codestudio/problems/reverse-stack-using-recursion_631875"
    
    solution = """
    void pushAtBottom(stack<int>& st, int x) 
    {
        if (st.empty()){
            st.push(x);
            return ;
        };
        
        
        int n = st.top();
        st.pop();
        pushAtBottom(st,x);
        st.push(n);
    }
    void reverseStack(stack<int> &st) {
        if (st.empty()){
            return ;
        };
        
        int n = st.top();
        st.pop();
        reverseStack(st);
        pushAtBottom(st,n);
    }
    
    """
    
def Sort_a_Stack():

    problem_link = "https://www.codingninjas.com/codestudio/problems/sort-a-stack_985275"
    
    solution = """
    void insertSort(stack<int> &stack , int x){
        if (stack.empty() ||  stack.top() <= x){
            stack.push(x);
            return ;      
        }
        int n = stack.top();
        stack.pop();
        insertSort(stack,x);
        stack.push(n);
    }

    void sortStack(stack<int> &stack)
    {
        // Write your code here
        if (stack.empty()){
            return ;
        }
        int  n = stack.top();
        stack.pop();
        sortStack(stack);
        
        insertSort(stack,n);
    }
    
    """
    
    
    
link = "https://www.codingninjas.com/codestudio/problems/redundant-brackets_975473"

def findRedundantBrackets(s:str):
    # Write your code here.
    # Return boolean True or False.
    
    
    l = []

    ch = "(+-*/"
    for i in s:
        if i in ch:
            l.append(i)
        else:
            if i == ")":
                count = 0
                while l == [] or l[-1] != "(":
                    count += 1
                    l.pop()
                if count == 0:
                    return True
                l.pop()
    return False
        
        
link = "https://www.codingninjas.com/codestudio/problems/minimum-cost-to-make-string-valid_1115770"    
    
def findMinimumCost(str):
	# Write your code here.
    if len(str)%2 == 1:
        return -1
    l = []
    for i in str:
        if i == "{":
            l.append(i)
        else:
            if l != [] and l[-1] == "{":
                l.pop()
            else:
                l.append(i)
    if len(l)%2 == 1:
        return -1
    a = 0
    b = 0
    for k in l:
        if k == "{":
            a+= 1
        else:
            b+= 1
    return (a+1)//2 + (b+1)//2