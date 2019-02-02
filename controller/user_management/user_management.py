from controller.dbHandler.db_handler import DbHandler
from models.client_status import ClientStatus

db_handler = DbHandler()
class UserMangement():
    def get_all_clients_of_user(self,user):
        return db_handler.get_all_clients_of_user(user)

    def get_online_clients_of_user(self,user):
        all_clients = self.get_all_clients_of_user(user)
        online_clients = []
        for item in all_clients:

            if item.get_status() != ClientStatus.offline:
                online_clients.append(item)
        return online_clients

    def set_client_as_primary(self,user,client):
        #todo if user access clients
        client.set_status(ClientStatus.primary)
        return client.get_status()
    