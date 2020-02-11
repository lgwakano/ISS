
#check file exists
import os.path

class FileManager:

    @staticmethod #no need to instanciate
    def file_exists():
        if os.path.isfile('currentbuffer.txt'):
            #print ("File exist")
            return True
        else:
            #print ("File not exist")
            return False

    @staticmethod
    def write_on_file(text, mode="w"):
        try:
            with open('currentbuffer.txt', mode) as f:
                f.write(text)
        except IOError:
            print("File does not exist or is unaccessible")

    @staticmethod
    def read_file():
        text = ''
        try:
            with open('currentbuffer.txt', 'r') as f:
                text = f.readline()
        except IOError:
            print("Cannot read file")
        return text

    @staticmethod
    def delete_file():
        os.remove('currentbuffer.txt')