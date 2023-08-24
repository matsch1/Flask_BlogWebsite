import os


class LineCounter():
    def __init__(self, base_directory, coding_language,spacer):
        self. illegal_folders = ['__pycache__']
        self.base_directory = base_directory
        self.coding_language = coding_language
        self.spacer = spacer
        self.number_of_lines = self.__count_lines(
            base_directory, coding_language)

    def __count_lines(self, base_directory, coding_language):
        number_of_lines = 0
        for root, dirs, files in os.walk(base_directory):
            dir_parts = root.split(self.spacer)
            if not (dir_parts[-1] in self.illegal_folders):
                for file in files:
                    if '.'+coding_language in file:
                        with open(root + self.spacer + file, 'r') as read_file:
                            lines = read_file.readlines()
                            number_of_lines += len(lines)

        return number_of_lines
