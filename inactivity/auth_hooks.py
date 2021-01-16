from django.utils.translation import ugettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from . import urls


class InactivityMenuItem(MenuItemHook):
    """ This class ensures only authorized users will see the menu entry """

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("inactivity"),
            "fas fa-cube fa-fw",
            "inactivity:index",
            navactive=["inactivity:"],
        )

    def render(self, request):
        if request.user.has_perm("inactivity.basic_access"):
            return MenuItemHook.render(self, request)
        return ""


# @hooks.register("menu_item_hook")
# def register_menu():
#    return InactivityMenuItem()


@hooks.register("url_hook")
def register_urls():
    return UrlHook(urls, "inactivity", r"^inactivity/")
