import offshoot


class SerpentCanabaltGamePlugin(offshoot.Plugin):
    name = "SerpentCanabaltGamePlugin"
    version = "0.1.0"

    libraries = []

    files = [
        {"path": "serpent_Canabalt_game.py", "pluggable": "Game"}
    ]

    config = {
        "fps": 2
    }

    @classmethod
    def on_install(cls):
        print("\n\n%s was installed successfully!" % cls.__name__)

    @classmethod
    def on_uninstall(cls):
        print("\n\n%s was uninstalled successfully!" % cls.__name__)


if __name__ == "__main__":
    offshoot.executable_hook(SerpentCanabaltGamePlugin)
