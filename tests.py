import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )
    
    def test_maze_break_walls(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        for cells in m1._cells:
            for cell in cells:
                self.assertTrue(
                    not cell.has_bottom_wall or
                    not cell.has_left_wall or
                    not cell.has_right_wall or
                    not cell.has_top_wall
                )

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        m1._reset_cells_visited()
        for cells in m1._cells:
            for cell in cells:
                self.assertFalse(cell.visited)
    

    def test_dfs_solve(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertTrue(m1.dfs_solve())
    

    def test_dead_end_solve(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertTrue(m1.dead_end_solve())


if __name__ == "__main__":
    unittest.main()
