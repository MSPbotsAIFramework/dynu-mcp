from .._json import error_envelope

NO_TOKEN = error_envelope(
    "not_configured", "No Dynu API key. Send the X-Dynu-Api-Key header.", False
)
