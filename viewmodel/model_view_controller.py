#model_view_controller.py
import backend

class model(object):

   def __init__(self, myitems):
    self.create_items(myitems)

   def create_items(self, myitems):
       backend.create_items(myitems)

class view(object):
    
    @staticmethod
    def printItem_view():
        print(backend.items)

class controller(object):
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
 
    def printItem_view(self):
        self.view.printItem_view()

myitems = { 'itemTask': 'Walk the Dogs', 'itemDescription': 'Take them over the field', 'itemStatus': 'Ready' }

c = controller(model(myitems), view())

c.printItem_view()