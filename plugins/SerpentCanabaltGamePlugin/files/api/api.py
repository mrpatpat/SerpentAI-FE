from serpent.game_api import GameAPI


class CanabaltAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def getSchrankSprite(self):
        return self.game.sprites.get("SPRITE_SCHRANK")

    def getKartonSprite(self):
        return self.game.sprites.get("SPRITE_KARTON")

    class MyAPINamespace:

        @classmethod
        def my_namespaced_api_function(cls):
            api = CanabaltAPI.instance