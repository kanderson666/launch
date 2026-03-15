"""
Problem 1: Tracking how many instances have been created (class variable + class method)

Create a DownloadTask class that tracks how many tasks have been created in total.

Requirements:

Use a class variable to keep count.
Increment the count in __init__.
Provide a class method total_tasks that returns how many tasks have been created.
Each instance should store a filename attribute.
"""

class DownloadTask:
    tasks = 0

    def __init__(self, file_name):
        self.__class__.tasks += 1
        self.filename = file_name

    @classmethod
    def total_tasks(cls):
        return cls.tasks

class Test(DownloadTask):
    pass


# Test cases
if __name__ == '__main__':
    assert DownloadTask.total_tasks() == 0

    t1 = DownloadTask('file1.zip')
    t2 = DownloadTask('file2.zip')
    assert DownloadTask.total_tasks() == 2

    t3 = DownloadTask('file3.zip')
    assert DownloadTask.total_tasks() == 3

    # Should also work via the instance, but you should *call it on the class*
    assert t1.filename == 'file1.zip'
    assert DownloadTask.total_tasks() == 3

    print("Problem 1 tests passed.")

    test = Test('hi')
    print(DownloadTask.total_tasks())
    print(test.total_tasks())
