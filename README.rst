Usage
=====


Settings
--------

::

    INSTALLED_APPS = (
        # ...
        'sitewidgets',
    )


Loading sitewidgets tags
------------------------

::

    {% load sitewidgets_tags %}


Widgets
=======


Facebook
--------

Loading the SDK::

    {% with lang="fr_CA" %}
    {% fb_sdk %} 
    {% endwith %}

Loading the SDK in a different language::

    {% with lang="fr_CA" %}
    {% fb_sdk %} 
    {% endwith %}


Like button
^^^^^^^^^^^

::

    {% fb_like_button %}


Like box
^^^^^^^^

::

    {% with width=290 height=380 %}
    {% fb_like_box "https://www.facebook.com/pages/My-Page/0123456789" %}
    {% endwith %}