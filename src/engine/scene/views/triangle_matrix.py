from engine.scene.scene import Scene

class TriangleMatrixScene( Scene ):
    def __init__(self, engine):
        super().__init__(engine)

        from engine.widget.buttons.redirect_button import RedirectButton
        self.add_widgets( 
            RedirectButton((10,10), "voltar", "back", self.engine),
            RedirectButton((0,100), "atumalaca", "to_triangle_matrix", self.engine) 
        )
        
    