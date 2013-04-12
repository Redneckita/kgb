KGB
===

KGB (Klaus Game Bot) is a remake of https://code.google.com/p/k-g-b/ and he is an Urban Terror 4.1 and 4.2 bot written in python 2.7 that aims to be flexible, stable and performant game bot for Urban Terror. Skills, ratios and other 'statistical' features are voluntarily excluded from the developing in order to focus on performance and flexibility.

KGB is currently being maintained and developed.

KGB is ideal for a server that hosts multiple game instances because updates are managed by the server so that gameservers' admins don't need to worry about them. Their bot is always up-to-date and always get the latest bug fixes...


How to run KGB
====================

A basic example looks like::

    # myapp/api.py
    # ============
    from tastypie.resources import ModelResource
    from myapp.models import Entry


    class EntryResource(ModelResource):
        class Meta:
            queryset = Entry.objects.all()


    # urls.py
    # =======
    from django.conf.urls.defaults import *
    from tastypie.api import Api
    from myapp.api import EntryResource

    v1_api = Api(api_name='v1')
    v1_api.register(EntryResource())

    urlpatterns = patterns('',
        # The normal jazz here then...
        (r'^api/', include(v1_api.urls)),
    )
