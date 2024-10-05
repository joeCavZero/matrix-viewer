from src.engine.scene.scene import Scene
from src.engine.widget.input.input_number import InputNumber
from src.engine.widget.buttons.construct_scaled_matrix_button import ConstructScaledMatrixButton

class ScaledMatrixMenuScene( Scene ):
    def __init__(self, engine ):
        super().__init__(engine)
        self.selected_input: InputNumber = None

        from src.engine.widget.buttons.redirect_button import RedirectButton
        from src.engine.widget.input.input_float import InputFloat
        from src.engine.widget.label.label import Label
        
        self.v1x1 = InputFloat((300,100), self.engine)
        self.v1x2 = InputFloat((500,100), self.engine)
        self.v1x3 = InputFloat((700,100), self.engine)
        self.v1x4 = InputFloat((900,100), self.engine)
        
        self.v2x1 = InputFloat((300,200), self.engine)
        self.v2x2 = InputFloat((500,200), self.engine)
        self.v2x3 = InputFloat((700,200), self.engine)
        self.v2x4 = InputFloat((900,200), self.engine)
        
        self.v3x1 = InputFloat((300,300), self.engine)
        self.v3x2 = InputFloat((500,300), self.engine)
        self.v3x3 = InputFloat((700,300), self.engine)
        self.v3x4 = InputFloat((900,300), self.engine)
        
        
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            self.v1x1, self.v1x2, self.v1x3, self.v1x4,
            self.v2x1, self.v2x2, self.v2x3, self.v2x4,
            self.v3x1, self.v3x2, self.v3x3, self.v3x4,
            
            ConstructScaledMatrixButton((0,500), "MONTAR MATRIZ ESCALONADA", self.engine).center()
        )