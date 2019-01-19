from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
import random
import numpy
import keras

class SerpentDashbotGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        input_dim = game_frame.shape #input dimension of neural network
        layers = random.randint(1,3) #number of hidden layers
    
    def handle_play(self, game_frame):
        #visual debugger
        for i, game_frame in enumerate(self.game_frame_buffer.frames):
            self.visual_debugger.store_image_data(
                game_frame.frame,
                game_frame.frame.shape,
                str(i)
            )

        #pressing the space bar
        self.input_controller.tap_key(KeyboardKey.KEY_SPACE, duration=0.05)        
        print("Jumped!")