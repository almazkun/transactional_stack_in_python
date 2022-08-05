from unittest import TestCase
from tr_stack import TrStack
from collections import deque


class TestMain(TestCase):
    def test_main(self):
        stack_type_list = [deque, list]
        for stack_type in stack_type_list:

            tr_st = TrStack(stack_type=stack_type)

            self.assertEqual(tr_st.top(), 0)
            self.assertEqual(tr_st.pop(), None)

            tr_st.push(1)

            self.assertEqual(tr_st.top(), 1)
            self.assertEqual(tr_st.pop(), 1)
            self.assertEqual(tr_st.top(), 0)
            self.assertEqual(tr_st.pop(), None)

            tr_st.push(1)
            tr_st.push(2)

            self.assertEqual(tr_st.top(), 2)
            self.assertEqual(tr_st.pop(), 2)
            self.assertEqual(tr_st.top(), 1)
            self.assertEqual(tr_st.pop(), 1)
            self.assertEqual(tr_st.top(), 0)
            self.assertEqual(tr_st.pop(), None)

            tr_st.begin()
            tr_st.push(1)
            tr_st.push(2)
            tr_st.begin()
            tr_st.push(3)
            tr_st.push(4)

            self.assertEqual(tr_st.top(), 4)
            self.assertEqual(tr_st.pop(), 4)
            self.assertEqual(tr_st.top(), 3)
            self.assertTrue(tr_st.rollback())
            self.assertEqual(tr_st.top(), 2)

            tr_st.push(5)

            self.assertEqual(tr_st.top(), 5)
            self.assertTrue(tr_st.commit())
            self.assertEqual(tr_st.top(), 5)
            self.assertFalse(tr_st.rollback())
            self.assertFalse(tr_st.commit())
            self.assertEqual(tr_st.stack, stack_type([stack_type([1, 2, 5])]))
