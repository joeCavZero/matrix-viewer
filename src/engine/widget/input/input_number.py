from src.engine.widget.widget import Widget
import pygame

NUMBER_KEYS =[
    pygame.K_0, 
    pygame.K_1, 
    pygame.K_2, 
    pygame.K_3, 
    pygame.K_4, 
    pygame.K_5, 
    pygame.K_6, 
    pygame.K_7, 
    pygame.K_8, 
    pygame.K_9
]
KEYS_TO_NUMBERS = {
    pygame.K_0: "0",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9",
}

PADDING = 10

class InputNumber( Widget ):
    from src.engine.engine import Engine
    def __init__(self, position: tuple[float, float], engine):
        super().__init__(position, (200, 50), engine)
        self._value = "0"
        self._color = pygame.color.Color(255,255,255)
    
    def update(self):
        if self.is_hover() and pygame.mouse.get_just_released()[0]:
            self.engine.scene.selected_input = self
        if not self.is_hover() and pygame.mouse.get_just_released()[0]:
            if hasattr(self.engine.scene, "selected_input") and self.engine.scene.selected_input == self:
                self.engine.scene.selected_input = None
        
        # existe um momento em que a scene não é main o menu de matriz triangular, então é necessário verificar se o atributo existe para não bugar
        if hasattr(self.engine.scene, "selected_input") and self.engine.scene.selected_input == self:
            self._color = pygame.color.Color(155,255,155)
            keys_pressed = pygame.key.get_just_pressed()
            if keys_pressed[pygame.K_BACKSPACE]:
                if len(self._value) > 0:
                        self._value = self._value[:-1]
                
            
            for k in NUMBER_KEYS:
                if keys_pressed[k]:
                    self._value += KEYS_TO_NUMBERS[k]

        else:
            self._color = pygame.color.Color(255,255,255)
    def render(self, canvas: pygame.Surface):
        pygame.draw.rect(
            canvas,
            self._color,
            self.get_rect()
        )

        pygame.draw.rect(
            canvas,
            (0,0,0),
            (
                self.position.x+2,
                self.position.y + self.size.y - 4,
                self.size.x-4,
                2
            ),
            
        )
        
        font = self.engine.font_manager.get_font("arial-button")
        ren_text = pygame.font.Font.render( font, self._value, True, (0,0,0) )
        
        canvas.blit(
            ren_text,
            (self.position.x+PADDING, self.position.y+PADDING)
        )

    def get_value(self)->int:
        if self._value == "":
            return 0
        return int(self._value)