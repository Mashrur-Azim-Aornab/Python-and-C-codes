//all the numbers whose digits' product is equal to n99. for example, n99=96, so one of the those numbers is 843 as 8*4*3=96. here is my code:
// This entire code was developed in June, 2023
#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
void show_vector(vector<int>& a,int i=0,int l=-3){
    if(l==-3){
        l=a.size();
    }
    if(i!=l-1){
        cout<<a[i]<<" ";
    }                                //this code gives all the numbers whose digits' product is equal to n99. suppose, n99=96 and 843 is one of the numbers(as, 8*4*3=96).
    else{
        cout<<a[i]<<endl;
    }
    if(i+1<=l-1){
        show_vector(a,i+1,l);
    }
}
void exhibit_vector(vector< vector<int> >&a){
    int l=a.size();
    for(int q=0;q<l;q++){
        for(int k=0;k<10;k++){
            if(k!=9){
                cout<<a[q][k]<<" ";
            }
            else{
                cout<<a[q][k]<<endl;
            }
        }
    }
}
 //returns true if there is no exact same vector like "b" in vector "a"
bool barking_pork(vector< vector<int> >& a,vector< int >& b){
    int l=a.size();  
    for(int q=0;q<l;q++){
        int c=0;
        for(int k=0;k<10;k++){
            if(a[q][k]==b[k]){
                c++;
            }
        }
        //cout<<"c: "<<c<<endl;
        if(c==10){
            return false;
        }
    }
    return true;
}
//returns factorial of n
int pork(int n){
	if(n==0 || n==1){
		return 1;
	}
	return n*pork(n-1);
}
void display_array(int* a,int l,int i=0){
	if(i!=l-1){
		cout<<*a<<" ";
	}
	else{
		cout<<*a<<endl;
	}
	if(i+1<=l-1){
		display_array(a+1,l,i+1);
	}
}
int process(int* a,int l){
	int s=0;
	int p=1;
	for(int i=2;i<l;i++){
		s=s+*(a+i);
		p=p*pork(*(a+i));
	}
	return (pork(s))/p;
}
int process_stange(vector<int>& a){
    int l=a.size();
	int s=0;
	int p=1;
	for(int i=2;i<l;i++){
		s=s+a[i];
		p=p*pork(a[i]);
	}
	return (pork(s))/p;
}
bool prime_check(int n,int i=2){
	if(n==1){
		return false;
	}
	if(n%2==0 && n>2){
		return false;
	}
	if(n%i==0){
		return false;
	}
	if(i+1<=n/2){
		return prime_check(n,i+1);
	}
	return true;
}
bool prime_detector(int n){
	if(n==1){
		return false;
	}
	if(n==2){
		return true;
	}
	if(n%2==0 && n>2){
		return false;
	}
	int i=3;
	int g=sqrt(n);
	while(i<=g){
		if(n%i==0){
			return false;
		}
		i=i+2;
	}
	return true;
}
vector<int> only_primes233(int n){
    vector<int> r(10,0);
    int q=2;
    while(q<10){
        if(n%q!=0 && q==9 && n>9){
            vector<int> v(10,0);
            return v;
        }
        //cout<<n<<" "<<q<<endl;
        bool x=prime_detector(n);
        if(x==true){
            if(n<10){
                //*(r+n)=*(r+n)+1;
                r[n]=r[n]+1;
                break;
            }
            else{
                vector<int> v(10,0);
                return v;
            }
        }
        if(n%q==0){
            //*(r+q)=*(r+q)+1;
            r[q]=r[q]+1;
            n=n/q;
            q=2;
        }
        else{
            q++;
        }
    }
    //show_vector(r);
    return r;
}
void vector_processing(vector<int>& g,vector< vector<int> >&f){
    vector<int> a;
    int l2=g.size();
    for(int q=0;q<l2;q++){
        a.push_back(g[q]);
    }
    if(a[2]>=1 && a[3]>=1){
            a[2]=a[2]-1;
            a[3]=a[3]-1;
            a[6]=a[6]+1;
            bool x=barking_pork(f,a);
            if(x==true){
                f.push_back(a);
            }
            //sdf
            a[2]=a[2]+1;
            a[3]=a[3]+1;
            a[6]=a[6]-1;
        }
    if(a[2]>=2){
        a[2]=a[2]-2;
        a[4]=a[4]+1;
        bool x=barking_pork(f,a);
        if(x==true){
            f.push_back(a);
        }
        //sdf
        a[2]=a[2]+2;
        a[4]=a[4]-1;
    }
    
    if(a[2]>=3){
            a[8]=a[8]+1;
            a[2]=a[2]-3;
            bool x = barking_pork(f,a);
            if(x==true){
                f.push_back(a);
            }
            a[8]=a[8]-1;
            a[2]=a[2]+3;
        }
    if(a[2]>=4){
            a[4]=a[4]+2;
            a[2]=a[2]-4;
            bool x = barking_pork(f,a);
            if(x==true){
                f.push_back(a);
            }
            a[4]=a[4]-2;
            a[2]=a[2]+4;
    }
    if(a[3]>=2){
        a[3]=a[3]-2;
        a[9]=a[9]+1;
        bool x= barking_pork(f,a);
        if(x==true){
            f.push_back(a);
        }
        a[3]=a[3]+2;
        a[9]=a[9]+1;
    }
    //exhibit_vector(f);
}
int final_processing(int n99){
    bool x59=prime_detector(n99);
    if(n99%2!=0 && x59== true && n99>10){
        return 0;
    }
    
    vector<int> p= only_primes233(n99);
    //show_vector(p);
    int seoul=p.size();
    int hiroshima=0;
    for(int q=0;q<seoul;q++){
        if(p[q]!=0){
            hiroshima++;
        }
    }
    if(hiroshima==0){
        return 0;
    }
    if(hiroshima==1){
    	cout<<"Do you want to see all the possible combinations? Enter 'YES' to see. Otherwise, enter 'NO'"<<endl;
    string v91;
    cin>>v91;
    if(v91=="YES"){
        cout<<0<<" "<<1<<" "<<2<<" "<<3<<" "<<4<<" "<<5<<" "<<6<<" "<<7<<" "<<8<<" "<<9<<endl<<endl<<endl;
        show_vector(p);
    }
    	return 1;
	}
    vector< vector<int> > fire;
    fire.push_back(p);
    int q=0;
    int l9=fire.size();
    while(q<l9){
        vector_processing(fire[q],fire);
        q++;
        if(l9<fire.size()){
            l9=fire.size();
        }
    }
    cout<<"Do you want to see all the possible combinations? Enter 'YES' to see. Otherwise, enter 'NO'"<<endl;
    string v91;
    cin>>v91;
    if(v91=="YES"){
        cout<<0<<" "<<1<<" "<<2<<" "<<3<<" "<<4<<" "<<5<<" "<<6<<" "<<7<<" "<<8<<" "<<9<<endl<<endl<<endl;
        exhibit_vector(fire);
    }
    //exhibit_vector(fire); this function shows all the possible combinations
    int py=fire.size();
    int numbers=0;
    for(int q=0;q<py;q++){
        numbers=numbers+process_stange(fire[q]);
    }
    return numbers;
}
int main(){
    int n99;
    cin>>n99;
    cout<<final_processing(n99)<<endl;
    
}