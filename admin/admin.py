class AdminManager:
    def __init__(self):
        self.admins = {"12345678"}  # Example: Add admin user IDs here
        self.restricted_users = set()

    def is_admin(self, user_id):
        return str(user_id) in self.admins

    def restrict_user(self, user_id):
        self.restricted_users.add(str(user_id))

    def unrestrict_user(self, user_id):
        self.restricted_users.discard(str(user_id))

    def list_restricted_users(self):
        return list(self.restricted_users)