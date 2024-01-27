from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
     
        if request.method == 'GET':
            return True

        return bool(obj.user == request.user or request.user.is_staff)


class IsStaffOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return bool(obj.user == request.user)