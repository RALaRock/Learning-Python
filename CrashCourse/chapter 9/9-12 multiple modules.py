# 9-12. Multiple Modules:
# Store the User class in one module, and store the
# Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call
# show_privileges() to show that everything is still
# working correctly.

import user_properties as User

a_user = User.Admin("Samuel", "Blathering")
print(a_user.describe_user())

# describe user is contained in the User class
# in the Iser2.py module
a_user.describe_user()
# priviledges is contained in the Priviledges class
# in the user_properties.py module
a_user.priviledges.show_priviledges()

print()

b_user = User.User("Bill", "NotAdmin")
print(b_user.describe_user())
