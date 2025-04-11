restricted_users = set()

def is_user_restricted(user_id):
    return str(user_id) in restricted_users

def restrict_user(user_id):
    restricted_users.add(str(user_id))

def unrestrict_user(user_id):
    restricted_users.discard(str(user_id))