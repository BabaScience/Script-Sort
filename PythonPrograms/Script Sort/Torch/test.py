import Test
from typing import Union



def greeting(name: Union[int, str]) -> str:
    print('hello', name)


greeting(False)
