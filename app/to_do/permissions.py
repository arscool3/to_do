from rest_framework import permissions

class IsOwnerOrReadyOnly(permissions.BasePermission) :
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.groups.filter(name = 'admin') :
            return True
        return obj.user == request.user


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='employee'):
            return True
        return False
