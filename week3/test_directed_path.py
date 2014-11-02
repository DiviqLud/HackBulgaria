import unittest
import directed_path


class TestDirectedPath(unittest.TestCase):

    def setUp(self):
        self.directed_path = directed_path.DirectedGraph()

    def test_add_edge_with_same_names(self):
        self.directed_path.add_edge("Galin", "Emil")
        self.directed_path.add_edge("Galin", "Emil")
        self.assertEqual(self.directed_path.graph, {"Galin": ["Emil"], "Emil": []})

    def test_add_edge_with_different_names(self):
        self.directed_path.add_edge("Galin", "Emil")
        self.directed_path.add_edge("Jeni", "Mitko")
        self.directed_path.add_edge("Jeni", "Kiro")
        self.directed_path.add_edge("Kiro", "Jeni")
        #print(self.directed_path.graph)
        self.assertEqual(self.directed_path.graph, {"Galin": ["Emil"], "Emil": [], "Jeni" : ["Mitko", "Kiro"], "Mitko": [], "Kiro": ["Jeni"]})

    def test_neighbours_for(self):
        self.directed_path.add_edge("Jeni", "Mitko")
        self.directed_path.add_edge("Jeni", "Kiro")
        self.assertEqual(self.directed_path.get_neighbors_for("Jeni"), ["Mitko", "Kiro"])

    def test_path_between(self):
        self.directed_path.add_edge("Jeni", "Mitko")
        self.directed_path.add_edge("Jeni", "Kiro")
        self.directed_path.add_edge("Kiro", "Atanas")
        self.directed_path.add_edge("Atanas", "Emil")
        self.assertTrue(self.directed_path.path_between("Jeni", "Emil"))
if __name__ == '__main__':
    unittest.main()
