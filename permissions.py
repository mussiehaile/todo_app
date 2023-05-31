from rest_framework.permissions import BasePermission



class ISSTAFF(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
class ISACTIVE(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active
class ISDIRECTOR(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_director
