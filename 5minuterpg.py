#5 Minute RPG Version 1.0 by Michael Hyatt 8/7/2017
import random
import art

#Creates the player with starting stats.
class player:
	hp = 50
	lvl = 1
	strg = 4
	exp = 0
	maxhp = 50
	gold = 0
	potion = 5
	
#Function to process experience gain after battle. Also determines level gains.
def level(xp):	
	player.exp = player.exp + xp
	if player.exp >= 10 and player.exp < 20:
		if player.lvl != 2: #Checks to make sure the player has not already leveled up. If they haven't then it congratulates the player.
			print art.lvlup
			player.hp = 100
			print 'Congratulations! You have become stronger! You are now level 2! \n'
		player.lvl = 2
		player.maxhp = 100
		player.strg = 6
	elif player.exp >= 20 and player.exp < 40:
		if player.lvl != 3:
			print art.lvlup
			player.hp = 150
			print 'Congratulations! You have become stronger! You are now level 3! \n'
		player.lvl = 3
		player.maxhp = 150
		player.strg = 9
	elif player.exp >= 40 and player.exp < 80:
		if player.lvl != 4:
			print art.lvlup
			player.hp = 225
			print 'Congratulations! You have become stronger! You are now level 4! \n'
		player.lvl = 4
		player.maxhp = 225
		player.strg = 13
	elif player.exp >= 80 and player.exp < 160:
		if player.lvl != 5:
			print art.lvlup
			player.hp = 320
			print 'Congratulations! You have become stronger! You are now level 5! \n'
		player.lvl = 5
		player.maxhp = 320
		player.strg = 18
	elif player.exp >= 160 and player.exp < 320:
		if player.lvl != 6:
			print art.lvlup
			player.hp = 450
			print 'Congratulations! You have become stronger! You are now level 6! \n'
		player.lvl = 6
		player.maxhp = 450
		player.strg = 24
	elif player.exp >= 320 and player.exp < 640:
		if player.lvl != 7:
			print art.lvlup
			player.hp = 650
			print 'Congratulations! You have become stronger! You are now level 7! \n'
		player.lvl = 7
		player.maxhp = 650
		player.strg = 31
	elif player.exp >= 640 and player.exp < 1280:
		if player.lvl != 8:
			print art.lvlup
			player.hp = 900
			print 'Congratulations! You have become stronger! You are now level 8! \n'
		player.lvl = 8
		player.maxhp = 900
		player.strg = 39
	elif player.exp >= 1280 and player.exp < 2600:
		if player.lvl != 9:
			print art.lvlup
			player.hp = 1200
			print 'Congratulations! You have become stronger! You are now level 9! \n'
		player.lvl = 9
		player.maxhp = 1200
		player.strg = 48
	elif player.exp >= 2600:
		if player.lvl != 10:
			print art.lvlup
			player.hp = 2000
			print 'Congratulations! You have become stronger! You are now level 10! YOU HAVE REACHED MAX LEVEL! \n'
		player.lvl = 10
		player.maxhp = 2000
		player.strg = 60

#This function determines life gain or loss depending if its called from the mob attack or the potion use.		
def life(life):
	player.hp = player.hp + life
	if player.hp > player.maxhp: #makes sure the player does not gain more than the maxiumum life.
		player.hp = player.maxhp
		
	elif player.hp <= 0: #If the player has no life left then they lose.
		print art.lose
		print '\n \n'
		playagain = input('Play Again? \n 1. Yes \n 2. No \n')
		if playagain == 1:
			player.lvl = 1
			player.hp = 50
			player.exp = 0
			menu(0)
		elif playagain == 2:
			menu(0)

#Function contains the main menu
def menu(x):
	while x == 0:
		print art.player + '\n Health: [' + str(player.hp) + ' / ' + str(player.maxhp) + '] \n Level: ' + str(player.lvl) + '\n Experience: ' + str(player.exp) + '\n Gold: ' + str(player.gold) + '\n Potions: ' + str(player.potion)
		x = input('\nWhat would you like to do? \n 1. Fight mob \n 2. Rest \n 3. Buy potion (10 Gold) \n')
		if x == 1:
			print '\nSo you want to fight a mob?\n'
			y = input(' What type of mob would you like to fight? \n##################\n# 1. Easy Mob    #\n# 2. Hard Mob    #\n# 3. Harder Mob  #\n# 4. Hardest Mob #\n# 5. MOB BOSS    #\n# 6. Go back     #\n##################\n')
			if y == 6:
				menu(0)
			elif (y < 6) and (y > 0):
				mob(y)
			else:
				print 'invalid option.'
			
		elif x == 2:
			player.hp = player.maxhp
			print art.bed
			print 'You enjoyed a full nights rest and regained all of your hit points! \n'
			x = 0
		elif x == 3:
			if player.gold <= 5:
				print 'Sorry. You are too broke to buy a potion.'
			else:
				print 'You bought a potion.'
				player.potion = player.potion + 1
				player.gold = player.gold - 10
			x = 0
		else:
			print 'That is not a valid option. \n'
			x = 0
		
#The different monster types here.		
def mob(type):
	if type == 1:
		print art.fight
		print ' You have engaged a Easy Mob. '
		battle('Easy Mob', 50, 5, 5)
		
	elif type == 2:
		print art.fight
		print ' You have engaged a Hard Mob. '
		battle('Hard Mob', 100, 10, 15)
	
	elif type == 3:
		print art.fight
		print ' You have engaged a Harder Mob. '
		battle('Harder Mob', 200, 30, 30)
	
	elif type == 4:
		print art.fight
		print ' You have engaged the Harest Mob. '
		battle('Hardest Mob', 400, 75, 60)
	
	elif type == 5:
		print art.bossfight
		print ' You have engaged the MOB BOSS. '
		battle('MOB BOSS', 1600, 125, 0)
			
#The actual battle engine.
def battle(mobname, mob_hp, xpgain, goldgain):
	while mob_hp >= 1:
		print '####################################################'
		print '# Health: [' + str(player.hp) + ' / ' + str(player.maxhp) + '] Potions: ' + str(player.potion) + ' | ' + mobname + ' Health: ' + str(mob_hp) + ' #'
		print '####################################################'
		option = input('#Choose an option: #\n# 1. Attack        #\n# 2. Drink Potion  #\n####################\n')
		
		if option == 1:
			print art.attack
			#The following two variables determine the damage amounts for the player and mob.
			atk = player.strg + random.randint(1,player.strg) + player.lvl * 2 #determines the player attack amount
			mobatk = xpgain * random.randint(1,3) - player.lvl * random.randint(1,player.lvl) #determines the mob attack amount
			if mobatk <= 0:
				mobatk = 1
			print 'You attack the ' + mobname + ' for ' + str(atk) + ' points of damage. \n'
			print 'The ' + mobname + ' attacks you for ' + str(mobatk) + ' points of damage. \n'
			mob_hp = mob_hp - atk
			life(-mobatk) #sends the mob damage amount to the life function to subtract life.
			if mob_hp <= 0:
				#checks to see if the mob killed was the Mob Boss. If it was then they win.
				if xpgain == 125:
					print art.win
					print '\n \n'
					playagain = input('Play Again? \n 1. Yes \n 2. No \n')
					if playagain == 1:
						player.lvl = 1
						player.hp = 50
						player.exp = 0
						menu(0)
					elif playagain == 2:
						menu(0)
				else:
					print art.victory
					print 'You killed the ' + mobname + '. \n'
					print 'You have gained ' + str(xpgain) + ' experience points.'
					print 'You have received ' + str(goldgain) +' gold.'
					player.gold = player.gold + goldgain
					level(xpgain)
					menu(0)
		elif option == 2: #drink a potion!
			if player.potion > 0:
				pot = random.randint(5,15) * player.lvl
				player.potion = player.potion - 1
				life(pot) #sends potion amount to life function.
				print art.potion
				print 'You drank a potion and regained ' + str(pot) + ' hit points! \n'
			else:
				print 'You don\'t have any potions.'
		else:
			print 'Invalid option.'
			
print art.banner
print '\n Welcome to the 5 Minute RPG! You have 5 minutes to defeat the Mob Boss. Ready? Go!\n' 		
menu(0)