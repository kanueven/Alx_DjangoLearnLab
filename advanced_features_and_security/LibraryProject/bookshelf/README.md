Overview
Step 5:Document the steps
This project demonstrates how to use Django models, meta permissions, groups, and views to enforce fine-grained access control.
It uses a Vlogs model as an example to illustrate creating, editing, viewing, and deleting permissions.

Step 1: Define Custom Permissions in the Model
Permissions are defined in the model’s Meta class.
can_view, can_create, can_edit, can_delete are the codename variables used to check permissions in views.


These permissions are automatically registered in the Django admin after migrations.

Step 2: Create Groups and Assign Permissions
Use Django’s Admin site or code to create groups and assign permissions.
Editors: can view, create, and edit vlogs.


Viewers: can only view vlogs.


Admins: have all permissions.


⚠️ Always use the exact codename strings from the model’s Meta.permissions.

Step 3: Enforce Permissions in Views
Use @permission_required to protect views:
raise_exception=True ensures unauthorized users get a 403 error instead of being silently redirected.


