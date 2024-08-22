## Permissions and Groups Setup

### Custom Permissions:
- **can_view**: Allows viewing of books.
- **can_create**: Allows creation of new books.
- **can_edit**: Allows editing of existing books.
- **can_delete**: Allows deletion of books.

### User Groups:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Have full access to create, edit, view, and delete books.

### Implementation:
Permissions are enforced in views using the `@permission_required` decorator. Ensure users are assigned to the correct groups to manage access appropriately.
