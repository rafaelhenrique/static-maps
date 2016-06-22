from decouple import config

DEFAULT_LOCATION = "Rodoviária+Tietê,São+Paulo,SP"
BROWSER_KEY = config('BROWSER_KEY')
DEFAULT_LINK = (
    "https://maps.googleapis.com/maps/api/staticmap?center={}"
    "&zoom=17&size=640x640&maptype=roadmap"
    "&markers=color:blue%7Clabel:S%7C-23.5164523,-46.6241962"
    "&markers=color:green%7Clabel:G%7C40.711614,-74.012318"
    "&markers=color:red%7Clabel:C%7C40.718217,-73.998284"
    "&key={}").format(DEFAULT_LOCATION, BROWSER_KEY)
