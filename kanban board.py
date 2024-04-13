import pickle

class Task:
  def __init__(self, title, priority):
    self.title = title
    self.priority = priority

class Board:
  def __init__(self, board_name):
    self.tasks = []
    self.board_name = board_name

  def board_menu(self):
    choice = int(input("Enter 1 to add Task\nEnter 2 to view tasks\nEnter 3 to remove task\nEnter 4 to print tasks according to priority\nEnter any other no to go to Klankan Board menu"))
    if choice == 1:
      task_name = input("Enter Task Name: ")
      priority = input("Enter priority of Task")
      self.tasks.append(Task(task_name, priority))
      self.board_menu()
    elif choice == 2:
      j = 0
      print('Task no.\t'+'Task Name\t'+'Priority')
      for i in self.tasks:
        j += 1
        print(str(j)+'\t\t'+i.title+'\t\t'+i.priority)
      self.board_menu()
    elif choice == 3:
      remove_choice = int(input("Enter the task no. to be removed"))
      self.tasks.pop(remove_choice-1)
      self.board_menu()
    elif choice == 4:
      print('Task Name\t'+'Priority')
      for i in range(3):
        for j in self.tasks:
          if i == 0 and j.priority == 'High':
            print(j.title+'\t'+j.priority)
          elif i == 1 and j.priority == 'Medium':
            print(j.title+'\t'+j.priority)
          elif i == 2 and j.priority == 'Low':
            print(j.title+'\t'+j.priority)
      self.board_menu()
    else:
      menu()

def save_boards():
  with open('kanban.pkl', 'wb') as f:
    pickle.dump(k_b, f)

def load_boards():
  global k_b
  with open('kanban.pkl', 'rb') as f:
    k_b = pickle.load(f)

def menu():
  option = int(input("Enter 1 to add Kanban Board\nEnter 2 to view all boards\nEnter 3 to select a board\nEnter 4 to save and exit"))
  if option == 1:
    add_board()
  elif option == 2:
    view_all_boards()
  elif option == 3:
    choice = int(input('Enter the board no.'))-1
    k_b[choice].board_menu()
  elif option == 4:
    save_boards()
    exit()

def add_board():
  print('Enter board name : ')
  board_name = input()
  k_b.append(Board(board_name))
  menu()

def view_all_boards():
  j = 0
  print('Board No.\tBoard Name')
  for i in k_b:
    print(str(j+1)+"\t\t"+i.board_name)
    j += 1
  menu()

try:
  load_boards()
except (FileNotFoundError, EOFError):
  k_b = []

menu()
