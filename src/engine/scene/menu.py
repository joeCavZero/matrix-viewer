from engine.scene.scene import Scene


class MenuScene( Scene ):
    def __init__(self, engine):
        super().__init__(engine)

        from engine.widget.redirect_button import RedirectButton
        self.widgets.append( RedirectButton(100,100, "tome", self.engine) )
        
    