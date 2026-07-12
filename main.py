"""Nucleo del Juego de la Vida de Conway.

Este modulo contiene la estructura de datos de la grilla y operaciones basicas
sin depender de la interfaz grafica.
"""

from __future__ import annotations


class Grid:
	def __init__(self, rows: int, cols: int) -> None:
		if rows <= 0 or cols <= 0:
			raise ValueError("rows y cols deben ser mayores que cero")

		self.rows = rows
		self.cols = cols
		self._cells = [[False for _ in range(cols)] for _ in range(rows)]

	def _validate_position(self, x: int, y: int) -> None:
		if not (0 <= x < self.cols and 0 <= y < self.rows):
			raise IndexError("La posicion esta fuera de la grilla")

	def get_cell(self, x: int, y: int) -> bool:
		self._validate_position(x, y)
		return self._cells[y][x]

	def set_cell(self, x: int, y: int, value: bool) -> None:
		self._validate_position(x, y)
		self._cells[y][x] = bool(value)

	def clear(self) -> None:
		for y in range(self.rows):
			for x in range(self.cols):
				self._cells[y][x] = False


if __name__ == "__main__":
	grid = Grid(5, 5)
	grid.set_cell(2, 2, True)
	print(grid.get_cell(2, 2))
