from database import DBase
from .entities.admin_user import AdminUser


class AdminUserModel():

    @classmethod
    def get_for_login(self, user):
        try:

            connection = DBase.get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username , last_name , user, password, created_at FROM  superuser WHERE user = %s",(user,))
                
                row = cursor.fetchone()

                admin_user = None

                if row != None:
                    admin_user = AdminUser(row[0],row[1],row[2],row[3],row[4],row[5])

                    admin_user = admin_user.to_json()

            connection.close()

            return admin_user

        except Exception as ex:
            raise Exception(ex)
