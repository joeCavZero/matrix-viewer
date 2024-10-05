from src.engine.scene.scene import Scene
import pygame


class ScaledMatrixScene( Scene ):
    def __init__(self, matrix ,engine):
        super().__init__(engine)
        
        

        from src.engine.widget.buttons.redirect_button import RedirectButton
        from src.engine.widget.matrix.matrix_viewer import MatrixViewer
        from src.engine.widget.label.label import Label
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            Label((150,70),f"Matriz escalonada", self.engine).center(),
            MatrixViewer((150,120), (500,500),matrix, 3,4, self.engine).center()
            
        )
        
    