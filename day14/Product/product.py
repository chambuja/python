#product 폴드만들고
# Product 추상 클래스를 만들고
# 속성:name , price
# 메소드 : 추상함수 display_info(), get_name(), get_price(), set_price()
from  abc import  ABC,abstractmethod
class Product(ABC):
    def get_name(self):
        return self.get_name()
    @abstractmethod
     pass
# =============================================
# Beverage
# display_info()