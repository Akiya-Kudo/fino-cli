from rich.console import Console
from rich.theme import Theme

# ===============================
# Themes
# ===============================
STANDARD_THEME = Theme(
    {
        # --- semantic ---
        "error": "red",
        "warning": "yellow",
        "info": "cyan",
        "success": "green",
        # --- brand (fallback-safe) ---
        "brand.primary": "yellow",
        "brand.secondary": "yellow",
        "brand.tertiary": "bright_yellow",
        "brand.quaternary": "bright_yellow",
        # --- ui ---
        "panel.border": "white",
        "panel.title": "white",
    }
)

T256_THEME = Theme(
    {
        # --- semantic ---
        "error": "red3",
        "warning": "gold3",
        "info": "sky_blue3",
        "success": "sea_green3",
        # --- brand (fallback-safe) ---
        "brand.primary": "orange_red1",
        "brand.secondary": "orange1",
        "brand.tertiary": "gold1",
        "brand.quaternary": "light_goldenrod1",
        # --- ui ---
        "panel.border": "sandy_brown",
        "panel.title": "orange_red1",
    }
)

TRUECOLOR_THEME = Theme(
    {
        # --- semantic ---
        "error": "red3",
        "warning": "gold3",
        "info": "sky_blue3",
        "success": "sea_green3",
        # --- brand (fallback-safe) ---
        "brand.primary": "orange_red1",
        "brand.secondary": "orange1",
        "brand.tertiary": "gold1",
        "brand.quaternary": "light_goldenrod1",
        # --- ui ---
        "panel.border": "sandy_brown",
        "panel.title": "orange_red1",
    }
)


# ===============================
# Console factory
# ===============================
def create_console() -> Console:
    console = Console()
    theme: Theme
    if console.color_system == "truecolor":
        theme = TRUECOLOR_THEME
    elif console.color_system == "256":
        theme = T256_THEME
    else:
        theme = STANDARD_THEME
    return Console(theme=theme)
