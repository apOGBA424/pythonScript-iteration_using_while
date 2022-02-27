
profit = 500
accounts = ['savings','investments','expenses']
target = 0

while target != len(accounts):
	print(accounts[target].capitalize(), 'account gets', profit//len(accounts), 'share from\nbusiness profit.')
	target+=1
