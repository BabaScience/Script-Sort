from pathlib import Path
from myQueue import Queue
from myStack import Stack
import os 

r'''
Path from the begining:
/anaconda3/lib/python3.8/site-packages/torch/
'''
p = r'../../../../anaconda3/lib/python3.8/site-packages/torch/'
pt = r'Test/'
fp = 'torch.txt'

class Topsort:
    r"""
        
    """
    def __init__(self, path=pt, f_name=fp):
        self.base_path = r'../../../../'
        self.f_name = f_name
        self.script_names = 'Python Scipt.txt'
        self.path = path
        self.directories = Queue()
        self.python_files = []   # -> tuple (filename, directory)
        self.current_dirs = Stack()
        self.visited_dir = {}
        self.topsorted_list = []
        self.python_files_name = []
        self.graph = {}
        self._more = []

    def __solve(self):
        r"""
            
        """
        print('CHECKING ENCAPSULATIONS...\n')
        i = 0
        for every_dir in self.python_files:
            self.__loading(len(self.python_files), i)
            n, d = every_dir 
            path = d+n
            # print('\n\n\t\t', path)
            self.dfs(path)
            i += 1
    def dfs(self, directory):
        if not self.visited_dir[directory]:
            self.visited_dir[directory] = True
            self.current_dirs.push(directory)
            while not self.current_dirs.is_empty():
                curr_dir = self.current_dirs.last_on_stack()
                if self.__find_neighbours(curr_dir):
                    #print(curr_dir, '-------->', self.__find_neighbours(curr_dir))
                    for neighbour in self.__find_neighbours(curr_dir):
                        self.dfs(neighbour)
                else:
                    self.topsorted_list.append(self.current_dirs.pop())


    def get_all_python_files(self, path):
        print('CHEIKING ALL SCRIPT FILES...')
        self.directories.enqueue(path) 
        for p_file in self.find_all_python_files(path):
            self.python_files.append(p_file)
            self.python_files_name.append(p_file[0][:-3])
        while not self.directories.is_empty():
            cur_path = self.directories.dequeue()
            for folder_path in self.__find_all_folders(cur_path):
                self.directories.enqueue(folder_path)
                self.get_all_python_files(folder_path)
        r'''Saving all python programs names in File '''
        """
        with open(self.script_names, 'w') as f:
            for t in self.python_files:
                f.write(str(t[0]) + '\n') # filename
                f.write(str(t[1]) + '\n') # folder(parent) """
        self.__fill_visited_dir()
        return self.python_files

    def __fill_visited_dir(self):
        print('CALCULATING ..')
        for n, d in self.python_files:
            self.visited_dir[d+n] = False

    def find_all_python_files(self, path): 
        r"""
            Finding all python files in <path>
            and returns a list of tuple of (file_name, directory)
        """
        # go trough all folders and get all the python files 
        python_files = []
        with os.scandir(path) as main_dir:
            for element in main_dir:
                if element.name[-3:] == '.py': 
                    r''' if element is a python file '''
                    # print(element.name)
                    python_files.append((element.name, path))
        return python_files

    
    def __find_all_folders(self, path):
        r"""
            Finding all Folders in <path>
            and returns a list of all
        """
        folders = []
        with os.scandir(path) as  main_dir:
            for element in main_dir:
                if os.path.isdir(element):
                    r''' if element is a folder  '''
                    # print(element.name)
                    folders.append(path + element.name + '/')
        return folders
    def find_subdirectories(self, path):
        r"""
            Find all SubDirectories inside <path>
            and returns a list of all sub directories
            and their parent as a tuple (x, y)
        """
        folders = self.__find_all_folders(path)
        dirs = []
        for folder in folders:
            sub_dir = path + folder + '/'
            dirs.append((sub_dir, path))
        return dirs

    def sort(self):
        r"""
            
        """
        print('THIS OPERATION MAY TAKE FEW TIME DIPENDING ON THE SIDE OF THE FOLDER PLEASE BE PATIENT')
        self.get_all_python_files(self.path)
        self.__make_graph()
        # print(self.graph)
        # TopSort algorithm
        self.__solve()
        # Save it in self.f_name
        print(f'SAVING WORK IN {self.f_name}')
        with open(self.f_name, 'w') as f:
            for d in self.topsorted_list:
                f.write(d + '\n')
        return self.topsorted_list

    def __make_graph(self):
        print('MAKING GRAPH....')
        for p in self.python_files:
            self.__loading(len(self.python_files), self.python_files.index(p))
            current_file = p[1]+p[0]
            self.__check_encapsulation(current_file) # automatically append to the graph
            # print('Python File ->', current_file) 

    def __check_encapsulation(self, file_directory):
        r"""
            Check if the python file from <file_directory>
            has imported a module (python) file
        """
        imports = []
        comments = [
                "'''", '"""'
                ]
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            enable = True
            for line in lines:
                i = 0
                if ' torch.py' in line:
                    self._more.append((line, file_directory))
                if any(_ in line for _ in comments):
                    enable = not enable
                for file_name in self.python_files_name:
                    if 'import ' in line and file_name in line and enable:
                        # print(file_directory, '-->' , line, '---->', file_name)
                        imports.append(self.python_files[i][1]+self.python_files[i][0])
                    i += 1
                    
        if imports:
            self.graph[file_directory] = imports
        else:
            self.graph[file_directory] = []
        # print(file_directory, 'HAS IMPOTED: ', imports)

    def find_servers(self, directory):
        return self.graph[directory]

    def __find_neighbours(self, directory):
        n = []
        for _ in self.graph[directory]:
            if not self.visited_dir[_]:
                n.append(_)
        return n
    def __loading(self, scale, indx):
        r"""
            Needs to be implemented inside an iteration where <indx> changes
            to have a loading bar.
        """
        tot = 80
        res = scale - indx
        k = tot / scale
        hash_factor = int(k * indx)
        space_factor = int(k * res) 
        hashs = '#' * hash_factor
        spaces = ' ' * space_factor
        print('[' + hashs, spaces + ']')
