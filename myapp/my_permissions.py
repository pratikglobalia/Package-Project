from rest_framework import permissions

class MyCustomPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.type == 'teacher':
            return True
    