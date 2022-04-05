
from datetime import datetime
from pytz import timezone

########################## 
####### Shop class #######
########################## 
class BikeRental:
    def __init__(self, available_bikes):
        self.available_bikes = available_bikes
        
    def display_inventory(self):
        print(f"number of bikes available are: {self.available_bikes}")
        
    # Rent based on hour   
    def rent_hourly_basis(self, num_of_bikes):
        
        if num_of_bikes < 0:
            print("Invalid request. Request should be positive number")
            
        elif num_of_bikes > self.available_bikes:
            print(f"Available bikes are {self.available_bikes}.Request cannot be proceed.")
        else:
            #now = datetime.now()
            now = datetime.now(timezone('America/Chicago'))
            time = now.strftime("%I:%M %p")
            #now = now.hour
            # hour = datetime.strptime("hour", "%H:%M")
            print("Request completed.")
            print(f"Hourly rate is $20. Time of request is: {time}")
            
            self.available_bikes = self.available_bikes - num_of_bikes
            return now
            
    # Rent based on day        
    def rent_daily_basis(self, num_of_bikes):
            
        if num_of_bikes < 0:
            print("Invalid request. Request should be positive number")
            
        elif num_of_bikes > self.available_bikes:
            print(f"Available bikes are {self.available_bikes}.Request cannot be proceed.")
        else:
            #now = datetime.now()
            now = datetime.now(timezone('America/Chicago'))
            time = now.strftime("%I:%M %p")
            #now = now.hour
            # hour = datetime.strptime("hour", "%H:%M")
            print("Request completed.")
            print(f"Daily rate is $80. Time of request is: {time}")
            
            self.available_bikes = self.available_bikes - num_of_bikes
            return now
    
    # Rent based on week        
    def rent_weekly_basis(self, num_of_bikes):
            
            if num_of_bikes < 0:
                print("Invalid request. Request should be positive number")
                
            elif num_of_bikes > self.available_bikes:
                print(f"Available bikes are {self.available_bikes}.Request cannot be proceed.")
            else:
                #now = datetime.now()
                now = datetime.now(timezone('America/Chicago'))
                time = now.strftime("%I:%M %p")
                #now = now.hour
                # hour = datetime.strptime("hour", "%H:%M")
                print("Request completed.")
                print(f"weekly rate is $200. Time of request is: {time}")
                
                self.available_bikes = self.available_bikes - num_of_bikes
                return now
      
     # Shop handling the bike return request 
    def return_bikes(self, request):
        
        Rental_Basis,Rental_Time,num_of_bikes = request 
        
        if Rental_Basis and Rental_Time and num_of_bikes:
            self.available_bikes += num_of_bikes
            now = datetime.now(timezone('America/Chicago'))
            current_time = now.strftime("%I:%M %p")
            print(f"current time is: {current_time}")
            rental_period = now - Rental_Time
            
            # 1. hourly, 2. daily, 3. weekly
            
            if Rental_Basis == 1:
                bill = round(rental_period.seconds/3600) * num_of_bikes * 20 
            elif Rental_Basis == 2:
                bill = round(rental_period.days/ 24) * num_of_bikes * 80
            elif Rental_Basis == 3:
                bill = round(rental_period.days/7) * num_of_bikes * 120
            
            # for discount or deal
            if (num_of_bikes >= 6 and num_of_bikes <= 9):
                bill = bill * 0.7
            print(f"your bill is {bill}")
        else:
            print("Did you rent your bike here?")
            return None

#########################
#### Customer Class #####
#########################
class Customer:
    def __init__(self):
        self.bikes = 0 
        self.Rental_Basis = 0
        self.Rental_Time = 0 
        self.bill = 0 
       
    # Requesting bikes to rent (returns number of bikes) 
    def request_bikes(self):
        bikes = input("How many bikes you need? \n")
        
        try:
            bikes = int(bikes)
        except ValueError:
            print('Please enter a Number.')
            return -1
        if bikes < 1:
            print("invalid requests")
        else:
            self.bikes = bikes
        return self.bikes 
     
    # Customer returning bikes to the shop
    # Returns rental basis, rental time and bike numbers to be handled by shop
    def return_bikes(self):
        if self.Rental_Basis and self.Rental_Time and self.bikes:
            return self.Rental_Basis,self.Rental_Time,self.bikes 
        else:
            return 0,0,0

### Creating shop and customer objects ###          
shop = BikeRental(100)
customer = Customer()

### Program main body that Loops until breaks
while True:
    print(""" Menu options
    1. Display inventory 
    2. Hourly rental 
    3. Daily rental 
    4. Weekly rental 
    5. Return bikes
    6. Exit
    """)
    
    choice = input("choose from menu: ")
    
    #handle exception here for int input 
    try:
        choice = int(choice)
    except ValueError:
        print("enter valid entry:")
        continue
    
    if choice == 1:
        shop.display_inventory()
    elif choice == 2:
        customer.Rental_Time = shop.rent_hourly_basis(customer.request_bikes())
        customer.Rental_Basis = 1 
    elif choice == 3:
        customer.Rental_Time = shop.rent_daily_basis(customer.request_bikes())
        customer.Rental_Basis = 2 
    elif choice == 4:
        customer.Rental_Time = shop.rent_weekly_basis(customer.request_bikes())
        customer.Rental_Basis = 3 
    elif choice == 5:
        customer.bill = shop.return_bikes(customer.return_bikes())
        customer.Rental_Basis, customer.Rental_Time, customer.num_of_bikes = 0,0,0
        
    elif choice == 6:
        print("enter a valid choice")
        
    else:
        break
    
print("Thank you for your business. \nPlease come back again.")






