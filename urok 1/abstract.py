from abc import ABC, abstractmethod
class DataBase(ABC):
    @abstractmethod
    def add_user(self, user_id):
        pass
    @abstractmethod
    def delete_user(self, user_id):
        pass
class SQL(DataBase):
    def add_table(self):
        print('sql.execute')
