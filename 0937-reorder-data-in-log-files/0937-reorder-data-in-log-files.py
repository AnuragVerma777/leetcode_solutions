class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                digits.append(log)           # keep original order
            else:
                letters.append((content, identifier))

        letters.sort()                       # by content, then identifier

        return [identifier + " " + content for content, identifier in letters] + digits
        