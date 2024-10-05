
from src.engine.widget.matrix.matrix_viewer import MatrixViewer

class MatrixInputViewer(MatrixViewer):
    def __init__(self, position: tuple[float,float], matrix: list[list[int]], engine: Engine):
        super().__init__(position, matrix, engine)
       