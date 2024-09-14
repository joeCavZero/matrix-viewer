from src.engine.scene.scene import Scene
import pygame

class MenuScene( Scene ):
    def __init__(self, engine):
        super().__init__(engine)

        from src.engine.widget.buttons.redirect_button import RedirectButton
        self.add_widgets( 
            RedirectButton((0,200), "MATRIZ TRIANGULAR", "to_triangle_matrix_menu", self.engine).center(),
            RedirectButton((0,270), "CREDITOS", "to_credits", self.engine).center() 
        
        )
        
    def render(self, canvas: pygame.Surface):
        self.render_widgets(canvas)

        # TITLE
        font = self.engine.font_manager.get_font("arial-title")
        ren_title = pygame.font.Font.render( font, "MATRIX VIEWER", True, (255,255,255) )

        canvas.blit(
            ren_title,
            (self.engine.window.get_width()//2-ren_title.get_width()//2, 50)
        )
    