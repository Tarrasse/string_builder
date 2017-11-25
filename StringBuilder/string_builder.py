class StringBuilder:
    """
    python class for efficient string concatenation and building
    """

    def __init__(self, max_length=None):
        self.capacity = max_length
        self.subs = []
        self.length = 0

    def append(self, sub):
        """
        appends sub string to the existing string

        :param sub: sub-string to be appended
        :return:
            :boolean:
            True if the sub string appended correctly
            False if the string length after the appending will exceed the maximum length
        """

        length = len(sub)
        if self.capacity is not None \
                and self.length + length > self.capacity:
            return False
        self.subs.append(str(sub))
        self.length += length
        return True

    def delete(self, start=None, end=None):
        """
        deleted sub-string starting from start and end at end - 1

        if end is None :
            delete all starting from the start index
        if start is None :
            delete all and stop a index-1

        if neither is none:
            delete the subset between start and end

        if both are none :
            empty the string builder

        :param start: starting index
        :param end: ending indes
        """
        if (end != None) and (start != None) and (end < start):
            raise RuntimeError("end must be bigger than or equal start")

        if start is not None:
            if end is not None:
                # start = #, end = #
                # delete items within the range
                self.delete_subset(start, end)
            else:
                # start = #, end = None
                # delete items after the start index
                self.delete_all_after(start)
        else:
            if end is not None:
                # start = None, end = #
                # delete items before the end index
                self.delete_all_before(end)
            else:
                # delete all
                self.subs = []
                self.length = 0

    def delete_all_before(self, index):
        """
        delete all the characters before the index

        :type index: int
        """

        if index > self.length - 1 or index < 0:
            raise RuntimeError("index must be (0 <= index <= length-1)")
        idx = 0
        for i in range(len(self.subs)):
            sub = self.subs[i]
            if idx < index:
                if index < (i + len(sub) - 1):
                    self.subs[i] = sub[(index - i):]
                else:
                    self.subs[i] = ""
            idx += len(sub)
        self.length -= index

    def delete_all_after(self, index):
        """
       delete all the characters after the index

       :type index: int
       """
        if index > self.length - 1 or index < 0:
            raise RuntimeError("index must be (0 <= index <= length-1)")

        idx = 0
        for i in range(len(self.subs)):
            sub = self.subs[i]
            sub_length = len(sub)
            if idx <= index < (idx + sub_length):
                self.subs[i] = sub[:(index - idx + 1)]
            elif idx > index:
                self.subs[i] = ""
            idx += len(sub)
        self.length -= (self.length - index - 1)

    def delete_subset(self, start, end):
        """
        delete substring starting from start and ends before end
        :param start: starting index
        :param end: stopping index
        """
        if end < start:
            raise RuntimeError("end must be bigger than or equal start")
        if start > self.length - 1 or start < 0:
            raise RuntimeError("start must be (0 <= index <= length-1)")
        if end > self.length - 1 or end < 0:
            raise RuntimeError("end must be (0 <= index <= length-1)")

        idx = 0
        started = False
        for i in range(len(self.subs)):
            sub = self.subs[i]
            sub_length = len(sub)
            if started:
                if idx <= end < (idx + sub_length):
                    self.subs[i] = sub[(end - idx):]
                elif end < idx:
                    break
                else:
                    self.subs[i] = ""
            if idx <= start < (idx + sub_length):
                if i <= end < (i + sub_length):
                    self.subs[i] = sub[:(start - idx)] + sub[(end - idx):]
                else:
                    started = True
                    self.subs[i] = sub[:(start - idx)]

            idx += sub_length

    def delete_char_at(self, index):
        """
        delete character at index
        :param index: index of character to be deleted
        """
        if index > self.length - 1 or index < 0:
            raise RuntimeError("index must be (0 <= index <= length-1)")

        idx = 0
        for i in range(len(self.subs)):
            sub = self.subs[i]
            sub = str(sub)
            if idx < (index + len(sub) - 1):
                if idx >= index:
                    char_index = index - idx
                    self.subs[i] = sub[:char_index] + sub[char_index:]
            idx += len(sub)
        self.length -= 1

    def build(self):
        """
        builds the string

        :return:
         string of appended sub-strings
        """
        return ''.join(self.subs)

    def to_string(self):
        """
        builds the string
        :return:
         string of appended sub-string
        """
        return self.build()

    def replace(self, old, new, start=None, end=None):
        """
        replace all the characters between the range(start, end)

        :param old: to be replaced character
        :param new: new character
        :param start: starting index
        :param end: stopping index
        """
        if (end != None)  and (start != None):
            if end < start:
                raise RuntimeError("end must be bigger than or equal start")
            if start > self.length - 1 or start < 0:
                raise RuntimeError("start must be (0 <= index <= length-1)")
            if end > self.length - 1 or end < 0:
                raise RuntimeError("end must be (0 <= index <= length-1)")

        index = 0
        for i_subs in range(len(self.subs)):
            sub = self.subs[i_subs]
            for i_sub in range(len(sub)):
                if (start is None or start <= index) \
                        and (end is None or end > index) \
                        and sub[i_sub] == old:
                    self.subs[i_subs] = sub[:i_sub] + new + sub[i_sub + 1:]
