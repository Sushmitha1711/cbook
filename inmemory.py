
from contact import Contact
from beautifultable import BeautifulTable

class InMemoryImpl:
    contact_list=[]

    @classmethod
    def addcontact(cls):
        name=input("enter the name:")
        email=input("entyer the email:")
        mobile=input("entet the mobile:")
        address=input("enter the address:")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"contact is added successfully with name: {name}")

    @classmethod
    def deletecontact(cls):
        name=input("enter the name to delete:")
        contact=cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"{name} is deleted successfully:")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"contact with name {name} is not found:")


    @classmethod
    def viewcontacts(cls):
        InMemoryImpl._paint(cls.contact_list)


    @classmethod
    def search(cls):
        if len(cls.contact_list)>0:
            name=input("enter the name to search:")
            s_list=list(filter(lambda x:x.get__name().lower(),cls.contact_list))
            if len(s_list)>0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"there is no data found with given search data:{name}")
        else:
            print("contact book is empty!....you cant sesrch")

    @classmethod
    def updatecontact(cls):
        name=input("enter the name to update:")
        contact=cls.get_contact_by_name(name)
        if contact:
            print("1.name 2.email 3.mobile 4.address")
            ch=int(input("enter your choice:"))
            if ch==1:
                print(f"old name:{contact.get__name()}")
                name=input("enter the new name:")
                if name:
                    contact.set__name(name)
            elif ch==2:
                print(f"old email:{contact.get__email()}")
                email=input("enter the new email:")
                if email:
                    contact.set__email(email)
            elif ch==3:
                print(f"old mobile:{contact.get__mobile()}")
                mobile=input("enter the new mobile:")
                if mobile:
                    contact.set__mobile(mobile)
            elif ch==4:
                print(f"old address:{contact.get__address()}")
                address=input("enter the new address:")
                if address:
                    contact.set__address(address)
        else:
            print(f"contact with name {name} not available:")

    @staticmethod
    def _paint(lst):
        table=BeautifulTable()
        if len(lst)!=0:
            table=BeautifulTable()
            table.column_headers=["name","email","mobile","address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print("contact book is empty!....")

    @classmethod
    def get_contact_by_name(cls,name):

        if len(cls.contact_list)>0:
            contact=list(filter(lambda x:x.get__name().lower()==name.lower(),cls.contact_list))
            return contact[0]  if contact else None
