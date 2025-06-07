from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS --> επιτρέπονται για όλους
        if request.method in permissions.SAFE_METHODS:
            return True
        # Μόνο αν ο χρήστης είναι ο δημιουργός του αντικειμένου
        return obj.user == request.user 