class AppSettings:
    # 1. The shared state dictionary across all instances
    _shared_state = {
        "theme": "light",
        "max_connections": 10,
        "feature_flags": {
            "beta_checkout": False,
            "dark_mode": False
        }
    }

    def __init__(self):
        # 2. Redirect this instance's attribute dictionary to the shared state
        self.__dict__ = self._shared_state

    def enable_feature(self, flag_name: str) -> None:
        """Helper method to modify shared state."""
        self.feature_flags[flag_name] = True

    def __str__(self) -> str:
        return f"Settings(theme='{self.theme}', max_connections={self.max_connections}, flags={self.feature_flags})"


# ==========================================
# Application Workflow Simulation
# ==========================================

# Module A (e.g., UI Layer) initialises its own settings helper
ui_settings = AppSettings()
print(f"UI Startup: {ui_settings.theme}")  # Output: light

# Module B (e.g., Admin Panel) initialises another helper and changes settings
admin_settings = AppSettings()
admin_settings.theme = "dark"
admin_settings.enable_feature("beta_checkout")

# Module A reads its settings again
print(f"UI Theme updated: {ui_settings.theme}")  # Output: dark
print(f"UI Flags updated: {ui_settings.feature_flags}") 
# Output: {'beta_checkout': True, 'dark_mode': False}

# Object identity proof:
print(f"Same identity? {ui_settings is admin_settings}")       # False (Different instances)
print(f"Same state dict? {ui_settings.__dict__ is admin_settings.__dict__}")  # True (Shared state)