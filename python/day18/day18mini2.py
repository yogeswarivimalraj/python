def role_required(allowed_role):
    """
    Decorator that allows only specific roles to access a function.
    """
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != allowed_role:
                raise PermissionError(
                    f"Access Denied! '{user_role}' role is not allowed to run '{func.__name__}'."
                )
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_role, user_id):
    return f"User {user_id} deleted successfully!"

@role_required("guest")
def view_content(user_role):
    return "Guest content visible."

print(delete_user("admin", 101))   
print(view_content("guest"))      

# print(delete_user("guest", 101))   
