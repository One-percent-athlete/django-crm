from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganizerLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is organizer."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect('leads:lead_list')
        return super().dispatch(request, *args, **kwargs)