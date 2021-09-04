#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <map>
#include <stack>
#include <cstdlib>
#include <conio.h>
using namespace std;

class Bank
{
    private:
    char name[100];
    char add[100];
    char y;
    int balance;

    public:
    void openAccount();
    void depositMoney();
    void withdrawMoney();
    void displayAccount();

};

void Bank ::openAccount()
{
    cout<<"NOTE:-"<<endl;
    cout<<"Minimum balance must be Rs.100"<<endl;
    cout<<endl;

    cout<<"Enter your full name : ";
    scanf(" %[^\n]s",name);

    cout<<"Enter your address : ";
    scanf(" %[^\n]s",add);

    cout<<"What type of account you want to open saving (s) or current (c) : ";
    cin>>y;

    if(y=='s'||y=='c')
    {
        cout<<"Enter amount to deposit : ";
        cin>>balance;

        if(balance<100)
        {
            cout<<"Please add amount more than Rs.100";
            abort();
        }

        cout<<"YOUR ACCOUNT IS CREATED !!!!"<<endl;
    }

}

void Bank ::depositMoney()
{
    int cost;
    cout<<"Enter amount you want to deposit : ";
    cin>>cost;
    balance+=cost;

    cout<<"Your new balance is : Rs"<<balance<<endl;
}

void Bank ::displayAccount()
{
    string result;
    cout<<"Name : "<<name<<endl;
    cout<<"Address : "<<add<<endl;
    
    result= (y=='s')? "Saving Account": "Current Account";
    cout<<"Type of Account : "<<result<<endl;

    cout<<"Total Balance : Rs."<<balance<<endl;
}

void Bank::withdrawMoney()
{
    cout<<"NOTE:-"<<endl;
    cout<<"Minimum balance must be Rs.100"<<endl;

    int amount;
    cout<<"Enter amount to withdraw : ";
    cin>>amount;

    if(amount+100>=balance)
    {
        cout<<"Insufficient Balance !!!!"<<endl;
        return;
    }
    else
    {
        balance=balance-amount;
    }

    cout<<"Total balance : Rs. "<<balance<<endl;
}

int menu()
{
    int ch;

    cout<<endl;
    cout<<"1) Open account \n";
    cout<<"2) Deposite money \n";
    cout<<"3) Withdraw money \n";
    cout<<"4) Display account\n";
    cout<<"5) Exit\n";
    cout<<endl;

    cout<<"Enter your choice : ";
    cin>>ch;
    cout<<endl;

    return ch;
}

int main()
{
    Bank obj;
    
    while(1)
    {
        switch(menu())
        {
            case 1:
            obj.openAccount();
            break;

            case 2:
            obj.depositMoney();
            break;

            case 3:
            obj.withdrawMoney();
            break;

            case 4:
            obj.displayAccount();
            break;

            case 5:
            exit(0);

            default:
            printf("Invalid Input!!!!");

        }
    }

    return (0);

}