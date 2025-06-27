## if sth is interface we but I front the name 


from abc import ABCMeta, abstractmethod

class IPerson(meta=ABCMeta):
    @abstractmethod 
    def person_method():
        """ Interface method : bir arayüzün temelde ne olduğu sadece bir imza tanımıdır. Bu yüzden fonksiyonlara ve yöntemlere sahip 
            sahip olup ne yaptıklarını söyleyemeyeceğiz
         
          
        """