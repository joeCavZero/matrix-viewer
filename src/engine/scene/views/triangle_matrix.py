from engine.scene.scene import Scene
import pygame


class TriangleMatrixScene( Scene ):
    def __init__(self,n: int, engine):
        super().__init__(engine)
        self.n = n
        

        from engine.widget.buttons.redirect_button import RedirectButton
        from engine.widget.matrix.triangular_matrix import TriangularMatrixWidget
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine), 
            TriangularMatrixWidget((150,50), (500,500), self.n, "upper", self.engine),
            TriangularMatrixWidget((700,50), (500,500), self.n, "lower", self.engine)
        )
        
    