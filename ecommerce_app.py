from utils import get_user_input, is_valid_input
from product import Product
from user import User


MENU = '''
    ---- Main Menu ----
    
    1. Login
    2. Register
    3. Add Product
    4. Remove Product
    5. Search Product
    6. List Products
    7. Exit 
'''


class ECommerce:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.products = []
        self.MINIMUM_OPTION = 1
        self.MAXIMUM_OPTION = 7
       
    def add_product(self):
        if self.current_user is None:
            print('Please log in to add a product.')
            return
        
        name = get_user_input(
            display_text = 'Enter product name: ',
            invalid_message = 'Invalid product name! Please try again!'
        )
        quantity = get_user_input(
            display_text = 'Enter product quantity: ',
            invalid_message = 'Invalid input, please enter integer value!',
            dtype = int
        )
        price = get_user_input(
            display_text = 'Enter product price: ',
            invalid_message = 'Invalid input, please enter correct value!',
            dtype = float
        )
        new_product = Product(name, quantity, price)
        self.products.append(new_product)   
        print('Product added successfully.')

    def remove_product(self):
        if self.current_user is None:
            print('Please log in to remove a product.')
            return
        
        name = get_user_input(
            display_text = 'Enter product name to remove: ',
            invalid_message = 'Invalid product name! Please try again!'
        )
        found_product = None
        for product in self.products:
            if product.name == name:
                found_product = product
                break

        if found_product:
            self.products.remove(found_product)
            print('Product removed successfully.')
        else:
            print('Product not found.')
            
    def search_products(self):
        name = get_user_input(
            display_text = 'Enter product name to search: ',
            invalid_message = 'Invalid product name! Please try again!'
        )
        found_products = []
        for product in self.products:
            if name.lower() in product.name.lower():
                found_products.append(product)

        if found_products:
            print('Found products:')
            for product in found_products:
                print(f'Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}')
                
        else:
            print('No products found.')

    def list_products(self):
        if self.products:
            print('Available products:')
            for product in self.products:
                print(f'Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}')
                
        else:
            print('No products available.')

    def login(self):
        email = get_user_input(
            display_text = 'Enter your email: ',
            invalid_message = 'Invalid email! Please try again!'
        )
        password = get_user_input(
            display_text = 'Enter your password: ',
            invalid_message = 'Invalid password! Please try again!'
        )
        
        # Check if the user exists in the users list
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print('Login successful!')
                return
            
        print('Invalid username or password.')

    def register(self):
        name = get_user_input(
            display_text = 'Enter your name: ',
            invalid_message = 'Invalid username! Please try again!'
        )
        email = get_user_input(
            display_text = 'Enter your email: ',
            invalid_message = 'Invalid email! Please try again!'
        )
        password = get_user_input(
            display_text = 'Enter your password: ',
            invalid_message = 'Invalid password! Please try again!'
        )
        
        for user in self.users:
            if user.email == email:
                print('User with this email already exists. Please try again.')
                return

        new_user = User(name, password, email)
        self.users.append(new_user)
        print('Registration successful!')
        
    def run_main_menu(self):
        choice = None
        while is_valid_input(choice, min_inp = self.MINIMUM_OPTION, max_inp = self.MAXIMUM_OPTION):
            print(MENU)
            choice = get_user_input(
                display_text = 'Enter your choice (1-7): ',
                invalid_message = 'Invalid choice, please try again! ',
                dtype = int
            )            
            if choice == 1:
                self.login()
            elif choice == 2:
                self.register()
            elif choice == 3:
                self.add_product()
            elif choice == 4:
                self.remove_product()
            elif choice == 5:
                self.search_products()
            elif choice == 6:
                self.list_products()
            elif choice == 7:
                print('Exiting the application.')
                break
            else:
                print('Invalid choice. Please try again.')
    
            
app = ECommerce()
app.run_main_menu()
