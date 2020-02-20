print("Robinson Crusoe Day \nby DE '23")

def gameover():
    print("Game over, would you like to try again?")
for i in range (0,100):
    for i in range(0,1):
        print("Hello! You are stranded on a deserted island after a horde of squirrels chased you there. There is nobody else on the island, but it looks like people may have been here before, You get up to see a boar chasing you, and you have a knife, do you stab him?")
        x=(input("Yes or No?"))
        if x==("yes"):
            print("You are very uncoordinated and accidentally stab yourself and die")
            gameover()
            break
        else:
            print("The boar is thankful you didn't stab him, and leaves you alone")
        print("Now you need to find food. After a long time searching you find a banana tree and a coconut tree? Which one do you choose?")
        y=(input("Coconut or Banana?"))
        if y!="coconut" and y!="banana" and y!="Coconut" and y!="Banana":
            print ("That wasn't an option.")
            gameover()
            i=2
        else:
            print ("Interesting choice.You now need water,you spot a clear lake and a really dirty lake, which do you drink from?")
            z=(input("Clear or Dirty"))
        if z!="clear" and z!="Clear":
            print("As you go to get some water, an Alligator jumps out of the water and quickly eats you.")
            gameover()
            i=2
        else:
                print("The water looks clear, but do you want to make a fire to boil it just in case?")
                a=(input("Do you boil it?"))
        if a!="yes" and "Yes" and "boil" and "Boil":
            print("Although the water looked clear, it was infected, and you die of E. coli")
            gameover()
        else:
            print("After getting firewood earlier that night, you need to light the fire, do you use a piece if glass and try to foucus the sunlight, or rub two sticks together to ignite the fire?")
            b=(input("Glass or Friction?"))
        if b!= "friction" and "Friction" and "sticks" and "Sticks":
            print("The glass doesn't work because it is dark outside, you quickly freeze to death") 
            gameover()
            i=2
        else:
            print("Now that you have clean water and a fire, it's time to go to sleep, do you keep the fire going overnight?")  
            c=(input("Yes or No?"))  
        if c!= "yes" and "Yes":
            print("You underestimated how much temperatures drop at night, and quicly freeze without a fire,")
            gameover()
            i=2
        else:
            print("You wake up to the sound of helicopter blades coming towards you, this is your chance to get out of here. Do you shout and wave your arms at the helicopter, or do you make a big fire?")
            d=(input("Shout or Fire?"))
        if d!="Bonfire" and "bonfire":
            print("You aren't nearly loud enough to get his attention from the helicopter and he passes you over, you are then attacked by a pack of zebras.")
            gameover()
            i=2
        else:
            print("The fire catches the eye of the pilot and he quickly picks you up,and he takes you home to your family")
            print("Good job! You have survived this wild adventure, see you next time!")
