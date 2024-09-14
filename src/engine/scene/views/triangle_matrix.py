from src.engine.scene.scene import Scene
import pygame


class TriangleMatrixScene( Scene ):
    def __init__(self,n: int, engine):
        super().__init__(engine)
        self.n = n
        

        from src.engine.widget.buttons.redirect_button import RedirectButton
        from src.engine.widget.matrix.triangular_matrix import TriangularMatrixWidget
        from src.engine.widget.label.label import Label
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            Label((150,70),f"Matriz Triangular Superior N={self.n}", self.engine),
            Label((700,70),f"Matriz Triangular Inferior N={self.n}", self.engine),
            TriangularMatrixWidget((150,120), (500,500), self.n, "upper", self.engine),
            TriangularMatrixWidget((700,120), (500,500), self.n, "lower", self.engine)
        )
        
    