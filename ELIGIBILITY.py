age = int(input("Enter age : "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
    
# Works fine but you can do other checking such that if the person anything else asides from number, it should not just break the code
# Handle that edge case