/* Single Linked List

#include<iostream>

using namespace std;

class Node {
    public:
    int data;
    Node *next;

    Node(int data){
        this->data = data;
        this->next = NULL;
    };
    ~Node (){
        if (this->next != NULL){
            delete next;
            this->next = NULL;
        };


    };


};


class LinkedList{


    public:
    Node *head;
    Node *tail;

    LinkedList(int val){
        Node *n = new Node(val);
        this->head = n;
        this->tail = head;
    };

    void deleteNode(int pos){
        if (pos == 1){
            Node* o = head;
            head = head->next;
            o->next = NULL;
            delete o;


        }
        else{
            cout<<"G";

        int i = 2;
        Node* k = head;
        while (i<pos)
        {
            cout << " vadr"<<endl;
            i++;
            k = k->next;
        };
        Node *cur = k->next;
        k->next = k->next->next;

        delete cur;
        }
    };

    void insert(int pos,int val){


        int i = 1;
        Node* h = head;
        Node* n = new Node(val);
        if (pos == 0){
            n->next = h;
            this->head = n;
        };

        while(h != 0 ){
            if( i == pos){
                n->next = h->next;
                h->next = n;
            };
            h = h->next;
            i += 1;

        };

    };
    void append(int val){
        Node *n = new Node(val);
        tail->next = n;
        tail = tail->next;

    };
    void print(){

        while (head != 0){
            cout << head->data;
            cout<<endl;
            head = head->next;
        };

    };

};


int main(){
    LinkedList l(45);
    l.append(77);
    l.append(4);
    l.append(64);
    l.insert(4,7);
    l.deleteNode(2);
    l.print();
    // cout << n->data<<endl;
    // cout << n->next->data;
    // cout << n->next->next;
    // cout << n->next->next;

    return 0;
}



*/


#include<iostream>

using namespace std;


class Node
{
private:
    /* data */
public:
    int val;
    Node *next;
    Node *prev;
    Node(int val,Node* next = NULL,Node* prev=NULL){
        this->val = val;
        this->next = next;
        this->prev = prev;
    };

    ~Node();
};
class LinkedList{
public:
    Node *head;
    Node *tail;

    LinkedList(int val){
        Node *n = new Node(val);
        this->head = n;
        this->tail = n;

    }
    void insertAtHead(int val){
        Node *n = new Node(val);
        this->head->prev = n;
        n->next = this->head;
        this->head = n;

    }

    void insertAtTail(int val){
        Node *n = new Node(val);
        n->prev = this->tail;
        this->tail->next = n;
        this->tail = n;

    }

    void insertAtPos(int pos,int val){
        if (pos == 0){
            insertAtHead(val);
            return;
        };
        Node *h = this->head;
        while (pos>1){
            if (h == NULL){
                cout<<"Not Assignable"<<endl;
                return;
            };
            h = h->next;
            pos -= 1;
        };
        if (pos == 1){
            this->insertAtTail(val);
            return;
        };
        Node *n = new Node(val);
        h->next->prev = n;
        n->next = h->next;
        n->prev = h;;
        h->next = n;

    };

    void print(){
        Node *h = this->head;
        while (h!=NULL){
            cout << " "<< h->val;
            h = h->next;
        };
    }
};


int main()
{
    LinkedList l1 = LinkedList(45);
    l1.insertAtHead(9);
    l1.insertAtTail(78);
    l1.insertAtPos(4,4);
    l1.print();
    return 0;
}

