from src.engine.scene.scene import Scene
from src.engine.widget.input.input_number import InputNumber
from src.engine.widget.buttons.construct_triangular_matrix_button import ConstructTriangularMatrixButton

class TriangleMatrixMenuScene( Scene ):
    def __init__(self, engine):
        super().__init__(engine)
        self.selected_input: InputNumber = None

        from src.engine.widget.buttons.redirect_button import RedirectButton
        from src.engine.widget.input.input_number import InputNumber
        from src.engine.widget.label.label import Label
        self.n_input: InputNumber = InputNumber((0,100), self.engine).center()

        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            self.n_input,
            Label((500,100),"N:", self.engine),
            ConstructTriangularMatrixButton((0,200), "MONTAR MATRIZ TRIANGULAR", self.engine).center()
        )