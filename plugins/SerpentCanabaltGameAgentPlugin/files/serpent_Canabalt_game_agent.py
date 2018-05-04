import random
from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
from serpent.sprite_locator import SpriteLocator

class SerpentCanabaltGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        for i, game_frame in enumerate(self.game_frame_buffer.frames):
            self.visual_debugger.store_image_data(
                game_frame.frame,
                game_frame.frame.shape,
                str(i)
            )
        sprite_locator = SpriteLocator()
        location2 = sprite_locator.locate(sprite=self.game.api.getKartonSprite(), game_frame=game_frame)
        print(location2)
        if random.uniform(0.0,1.0) < 0.3:
            self.input_controller.tap_key(KeyboardKey.KEY_SPACE)

