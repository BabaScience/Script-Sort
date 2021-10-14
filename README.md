# Script-Sort

Python program that given a folder, checks all python file in the folder and write in "torch.txt" file all the files after ordering them in the following manner

a -> b   (means file "a" imports file "b" as a module)

a -> b -> c (a imports b which import c)

example:

  a -> b -> d
  d -> c 
  f -> b
  e
  
torch.txt:
  e
  c
  d
  b
  f
  a
  
 To use it open "main.py" and put your folder name in path variable, then run "main.py".
