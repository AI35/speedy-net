def activate_production(settings):
    settings.update({
        'DEFAULT_FROM_EMAIL': 'webmaster@speedy.net',
        'DEBUG': False,
    })