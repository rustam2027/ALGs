def swap(array: list, left: int, right: int) -> None:
    array[left], array[right] = array[right], array[left]


class Beep():
    def __init__(self, values: list, priorities: list) -> None:
        self.value = values
        self.priority = priorities
        i = len(self.priority) // 2 + 1
        while i >= 0:
            self.__fix_down(i)
            i -= 1

    def __swap(self, left: int, right: int):
        swap(self.value, left, right)
        swap(self.priority, left, right)

    def insert(self, priority: int, value: any) -> None:
        if not self.value:
            self.value.append(value)
            self.priority.append(priority)
        else:
            self.value.append(value)
            self.priority.append(priority)
            self.__fix_up(len(self.value) - 1)

    def __fix_down(self, i: int) -> None:
        while (i != 0 and i * 2 < len(self.value)) or (i == 0 and 1 < len(self.value)):
            if i:
                left_index = i * 2
            else:
                left_index = 1

            if (i != 0 and i * 2 + 1 < len(self.value)) or (i == 0 and 2 < len(self.value)):
                if i:
                    right_index = i * 2 + 1
                else:
                    right_index = 2
            else:
                right_index = i

            if self.priority[i] >= self.priority[right_index] or self.priority[i] >= self.priority[left_index]:
                if self.priority[left_index] < self.priority[right_index]:
                    self.__swap(i, left_index)
                    i = left_index
                else:
                    self.__swap(i, right_index)
                    if i == right_index:
                        break
                    i = right_index
            else:
                break

    def __fix_up(self, index: int):
        while index != 0:
            pre = index // 2
            if self.priority[pre] > self.priority[index]:
                self.__swap(pre, index)
                index = pre
            else:
                break

    def peek_min(self) -> any:
        return self.value[0]

    def extract_min(self) -> any:
        self.__swap(0, len(self.value) - 1)
        ret = self.value.pop()
        self.priority.pop()
        self.__fix_down(0)
        return ret

    def decrease_priority(self, val: any, new_priority: int) -> None:
        index = self.value.index(val)
        self.priority[index] = new_priority
        self.__fix_up(index)

    def __getitem__(self, value: any) -> int:
        if value in self.value:
            return self.priority[self.value.index(value)]
        else:
            return False

    def __bool__(self) -> bool:
        if self.priority:
            return True
        else:
            return False

    def __str__(self) -> str:
        return str(self.value) + "\n" + str(self.priority)
