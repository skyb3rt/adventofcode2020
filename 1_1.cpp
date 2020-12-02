#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <list>

using namespace std;

list<int> les_fil(){
	string line;
  	list<int> mylist;
  	list<int>::iterator it;
  	it = mylist.begin();
  	ifstream myfile ("1.txt");
  	if (myfile.is_open())
  	{
    	while ( getline (myfile,line) )
    	{
	  		++it;
      		mylist.insert(it,stoi(line)) ;
    	}
    myfile.close();
	  }
	return mylist;
}

int finn_to(int verdi,list<int> my_list){
	int tall;
	int resultat;
	list<int>::iterator it;
	list < int > :: iterator pos;
  	for (int x : my_list){
    	tall = (verdi - x);
		pos = find(my_list.begin(),my_list.end(),tall);
		if (pos !=my_list.end())
			resultat = tall*x;
	  }
	return resultat;
}

int main () {
	cout << finn_to(2020,les_fil());
	cout << '\n';
  	return 0;
}