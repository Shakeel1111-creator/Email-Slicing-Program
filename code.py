#Email Slicing Program

email=input('enter your email:')
i=email.index('@')
user_name=email[:i]
domain=email[i+1:]
print(f'User name is {user_name}')
print(f'User Domain is {domain}')
