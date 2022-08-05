from collections import deque


class TrStack:
    """Transactional stack implementation"""

    def __init__(self, stack_type=deque) -> None:
        self.stack = stack_type()
        self.in_transaction = False
        self.pointer = 0
        self.committed = 0
        self.stack.append(stack_type())

    def push(self, value):
        self.stack[self.pointer].append(value)

    def top(self):
        try:
            return self.stack[self.pointer][-1]
        except IndexError:
            return 0

    def pop(self):
        try:
            return self.stack[self.pointer].pop()
        except IndexError:
            pass

    def begin(self):
        """
        Creates a new transaction by making a new temp stack.
        Copy last stack into it.
        Only when commit or rollback called the temp slacks will removed.
        """
        self.in_transaction = True
        self.stack.append(self.stack[self.pointer].copy())
        self.pointer += 1
        self.committed += 1

    def rollback(self):
        """
        Cancels current transaction and returns to previous stack.
        """
        if not self.in_transaction:
            return False
        else:
            self.stack.pop()
            self.pointer -= 1
            self.committed -= 1
            if self.committed == 0:
                self.in_transaction = False
            return True

    def commit(self):
        """
        Commits current transaction deletes temp stack.
        """
        if not self.in_transaction:
            return False
        else:
            cur_stack = self.stack.pop()
            self.pointer -= 1
            self.committed -= 1
            self.stack[self.pointer] = cur_stack
            if self.committed == 0:
                self.in_transaction = False
            return True
