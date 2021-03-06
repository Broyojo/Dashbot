from serpent.game import Game

from .api.api import GeometrydashAPI

from serpent.utilities import Singleton




class SerpentGeometrydashGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Geometry Dash"

        kwargs["app_id"] = "322170"
        kwargs["app_args"] = None
        
        
        

        super().__init__(**kwargs)

        self.api_class = GeometrydashAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:200x200|FLOAT"

    @property
    def screen_regions(self):
        regions = {
            "SAMPLE_REGION": (0, 0, 0, 0)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
