"""Tests of inheritance, behavior, limits, and failure detection."""

import unittest
from dataclasses import replace

from lineage_lab import Cell, digest, inspect_record, make_child, response


class LineageLabTest(unittest.TestCase):
    def setUp(self):
        self.parent = Cell("P", None, 0, 2, ("observed:A",))

    def test_faithful_child_preserves_declared_state_and_observable_behavior(self):
        child, record = make_child(self.parent, label="a")
        self.assertEqual(child.parent, self.parent.identity)
        self.assertNotEqual(child.identity, self.parent.identity)
        self.assertEqual(child.memory, self.parent.memory)
        self.assertTrue(inspect_record(self.parent, child, record))
        self.assertEqual([response(child, x) for x in (0, 2, 5)],
                         [response(self.parent, x) for x in (0, 2, 5)])

    def test_bounded_variation_changes_held_out_behavior(self):
        child, record = make_child(self.parent, label="b", weight_change=1)
        self.assertTrue(inspect_record(self.parent, child, record))
        self.assertEqual(response(child, 0), response(self.parent, 0))
        self.assertNotEqual(response(child, 5), response(self.parent, 5))

    def test_limit_is_enforced(self):
        with self.assertRaises(ValueError):
            make_child(self.parent, label="b", weight_change=2)
        with self.assertRaises(ValueError):
            make_child(self.parent, label="c")

    def test_tampering_breaks_the_snapshot_check(self):
        child, record = make_child(self.parent, label="b", weight_change=1)
        altered = replace(child, memory=())
        self.assertNotEqual(digest(altered), record.child_digest)
        self.assertFalse(inspect_record(self.parent, altered, record))

    def test_same_output_at_one_signal_does_not_prove_same_identity(self):
        child, record = make_child(self.parent, label="b", weight_change=1)
        self.assertEqual(response(child, 0), response(self.parent, 0))
        self.assertNotEqual(child.identity, self.parent.identity)
        self.assertTrue(inspect_record(self.parent, child, record))


if __name__ == "__main__":
    unittest.main()
