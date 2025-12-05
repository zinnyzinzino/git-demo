class Stack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.capacity = cap
        self.top = -1

    def push(self, x):
        if self.top == self.capacity - 1:
            raise OverflowError("overflow")
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            raise IndexError("underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.top == -1:
            raise IndexError("empty")
        return self.arr[self.top]

    def isempty(self):
        return self.top == -1

    def size(self):
        return self.top + 1


if __name__ == "__main__":
    st = Stack(10)
    st.push(1)
    st.push(3)
    st.push(4)
    st.push(2)

    print("popped:", st.pop())
    print("top:", st.peek())
    print("size:", st.size())