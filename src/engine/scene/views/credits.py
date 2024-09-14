from src.engine.scene.scene import Scene
from src.engine.widget.input.input_number import InputNumber
from src.engine.widget.buttons.construct_triangular_matrix_button import ConstructTriangularMatrixButton

class CreditsScene( Scene ):
    def __init__(self, engine):
        super().__init__(engine)
        self.selected_input: InputNumber = None

        from src.engine.widget.buttons.redirect_button import RedirectButton
        from src.engine.widget.input.input_number import InputNumber
        from src.engine.widget.label.label import Label
        
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            Label((0,100),"Feito por João Gabriel Freitas Cavalcante\nAluno de Ciências da Computação na UFPI - Petrônio Portella\nGithub: JoeCavZero", self.engine).center(),
        )