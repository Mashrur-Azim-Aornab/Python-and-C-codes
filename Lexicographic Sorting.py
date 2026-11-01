#python code sort a list of strings in lexicographical order(dictionary style) and this code is completely done me
#this entire code was developed in June, 2023


def sort(a):
    l=len(a)
    u=0
    while u<l:
        min=u
        f=u+1
        while f<l:
            if a[min]>a[f]:
                min=f
            f=f+1
        if min!=u:
            v=a[u]
            a[u]=a[min]
            a[min]=v
        u=u+1
def largest_string(a,i=0,l=-3,m=-15):
    if l==-3:
        l=len(a)
    k=len(a[i])
    if m<k:
        m=k
    if i+1<=l-1:
        return largest_string(a,i+1,l,m)
    return m
def equalizing_length(a,i=0,b=-3,l=-55):
    if l==-55:
        l=len(a)
        b=largest_string(a)
    a[i]=a[i]+"0"*(b-len(a[i]))
    if i+1<=l-1:
        equalizing_length(a,i+1,b,l)
def searching_index(a,b,i=0,l=-52):
    if l==-52:
        l=len(a)
    if a[i]==b:
        return i
    if i+1<=l-1:
        return searching_index(a,b,i+1,l)
    return -1
def removing_redundancy(a,i=0,l=-55):
    if l==-55:
        l=len(a)
    a[i]=a[i]+"0"
    k=searching_index(a[i],"0")
    a[i]=a[i][:k]
    if i+1<=l-1:
        return removing_redundancy(a,i+1,l)
    return a
def copy_list(a,b=[],i=0,l=-33):
    if l==-33:
        l=len(a)
    b.append(a[i])
    if i+1<=l-1:
        return copy_list(a,b,i+1,l)
    return b
def lowest_ascII(a,i,i1=0,l=-3,m=9999):
    if l==-3:
        l=len(a)
    if ord(a[i1][i])<m:
        m=ord(a[i1][i])
    if i1+1<=l-1:
        return lowest_ascII(a,i,i1+1,l,m)
    return m
def lowest_ascIIz(a,i,b,i1=0,l=-3,m=9999):
    if l==-3:
        l=len(a)
    if a[i1][:i]==b and ord(a[i1][i])<m:
        m=ord(a[i1][i])
    if i1+1<=l-1:
        return lowest_ascIIz(a,i,b,i1+1,l,m)
    return m
def search(a,b,i=0,l=-3):
    if l==-3:
        l=len(a)
    if a[i]==b:
        return i
    if i+1<=l-1:
        return search(a,b,i+1,l)
    return -1
def fire(a,x):
    l=len(a[0])
    k = lowest_ascII(a, 0)
    k=chr(k)
    for i in range(1,l):
        #print(k)
        k1=lowest_ascIIz(a,i,k)
        k=k+chr(k1)
        #if i==l-1:
            #print(k,len(k))
    s=search(a,k)
    a=a[:s]+a[s+1:]
    x.append(k)
    return a
def lexico(b):
    equalizing_length(b)
    t=[]
    l=len(b)
    for f in range(0,l):
        b=fire(b,t)
    return removing_redundancy(t)
b = ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Jeju", "Gimpo", "Pohang","Gangneung", "Chuncheon", "Mokpo", "Andong", "Gunsan", "Jinju", "Uijeongbu", "Gyeongju", "Suncheon", "Gumi","Cheongju", "Ansan", "Yeosu", "Miryang", "Gwangmyeong", "Hwaseong", "Icheon", "Pyeongtaek", "Naju", "Sacheon"]
p=lexico(b)
print(p)
places = ["Istanbul", "Riyadh", "Ankara", "Jeddah", "Izmir", "Mecca", "Antalya", "Medina", "Bursa", "Dammam", "Adana", "Tabuk", "Gaziantep", "Al-Khobar", "Konya", "Taif", "Mersin", "Hail", "Kayseri", "Riyadh", "Trabzon", "Jizan", "Eskisehir", "Najran", "Samsun", "Buraydah", "Denizli", "Al-Ahsa", "Malatya", "Qatif", "Gebze", "Abha", "Erzurum", "Jeddah", "Kahramanmaras", "Hafar Al-Batin", "Aydin", "Al-Mubarraz", "Manisa", "Medina", "Hatay", "Al-Kharj", "Eskişehir", "Yanbu", "Sakarya", "Al-Jubail", "Sivas", "Istanbul", "Dhahran", "Kütahya", "Qassim", "Mardin", "Riyadh", "Van", "Jubail", "Sakaka", "Sivas", "Antakya", "Dammam", "Adiyaman", "Qatif", "Karaman", "Al-Hofuf", "Kütahya", "Al Qunfudhah", "Balikesir", "Al-Jubail", "Afyonkarahisar", "Yanbu", "Giresun", "Al-Qatif", "Zonguldak", "Taif", "Arar", "Siirt", "Medina", "Bolu", "Al-Ahsa", "Diyarbakir", "Tabuk", "Tokat", "Dhahran", "Bilecik", "Riyadh", "Aksaray", "Sakakah", "Isparta", "Jeddah", "Amasya", "Buraydah", "Bingöl", "Makkah", "Kahramanmaras", "Hail", "Gaziantep"]
z=lexico(places)
print(z)
zq=['ABC', 'ABCD', 'ABCE', 'DhumketuExpress', 'PadmaExpress', 'ShonarBangla', 'SubornoExpress']
sq=['ABC', 'ABCD', 'ABCE', 'lsdfwekeivndqpn', 'PadmaExpress']
print(lexico(sq))
print(lexico(zq))