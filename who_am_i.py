#Sailik Kundu, What are you?

import random
def chance(percent):
    return random.randrange(1,101) <= percent

inventory = {"matchbox": False, "knife handle": False, "water bottle": False, "key": False, "torch": False, "litTorch": False, "knife blade": False, "knife": False, "rope": False, "crowbar": False, "paper": False}
beenTo = {"bloodyRoom": False, "garden": False, "kitchen": False, "pipeRoom": False, "cellar": False}
tiedTo = {"hole": False}

##if(not inventory["line"]):
##    inventory["line"]= True
##elif(inventory ["line"]):
##    print("hi")
##Les trucs: Assassin: holy water death(chance)

def title():
    print("   ,--.   ,--.,--.               ,--.                            ")
    print("   |  |   |  ||  ,---.  ,--,--.,-'  '-.     ,--,--.,--.--. ,---. ")
    print("   |  |.'.|  ||  .-.  |' ,-.  |'-.  .-'    ' ,-.  ||  .--'| .-. :")
    print("   |   ,'.   ||  | |  |\ '-'  |  |  |      \ '-'  ||  |   \   --.")
    print("   '--'   '--'`--' `--' `--`--'  `--'       `--`--'`--'    `----'")
    print("")
    print("                                      ,------.  ")
    print("                                     '  .--.  ' ")
    print("              ,--. ,--.,---. ,--.,--.'--' _|  | ")
    print("               \  '  /| .-. ||  ||  | .--' __'  ")
    print("                \   ' ' '-' ''  ''  ' `---'     ")
    print("              .-'  /   `---'  `----'  .---.     ")
    print("              `---'                   '---'     ")
    
    
    
def bloodyRoom():
    print("")
    if(not beenTo["bloodyRoom"]):
        print("You are in a room. You wake up on tattered sheets, feeling dehydrated. \nYour head is throbbing, and you see blood splattered everywhere. \nYou hear a dripping sound. \nYou see a bag in front of you, and something metallic in the pool of blood on the floor. \nThere is one exit towards the place from where the dripping is coming from, \nand a doorway towards the west, smelling of flora. \nYou see a large window which is barred.")
        print("")
        beenTo["bloodyRoom"] = True
        choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor look in (b)ag or (p)ick up metallic object: ")
        while (choice!="g" and choice!="d" and choice!="b" and choice!="p"):
            print("Invalid choice")
            choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming, or look in (b)ag or (p)ick up metallic object: ")
            print("")
        if choice == "g":
            garden()
        elif choice == "d":
            pipeRoom()
        elif choice == "b":
            bag()
        elif choice == "p":
            key()
    else:
        if( not inventory["crowbar"]):
            print("You are back in the starting room. \nYou see a large window which is barred.")
            if(not inventory["matchbox"] and not inventory["key"]):
                print("You see a bag in front of you")
                print("You also see something metallic in the pool of blood on the floor.")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor look in (b)ag or (p)ick up metallic object: ")
                while (choice!="g" and choice!="d" and choice!="b" and choice!="p"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \nor look in (b)ag or (p)ick up metallic object: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "b":
                    bag()
                elif choice == "p":
                    key()
    
            elif(not inventory["matchbox"] and inventory["key"]):
                print("You see a bag in front of you")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor look in (b)ag: ")
                while (choice!="g" and choice!="d" and choice!="b"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \nor look in (b)ag: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "b":
                    bag()

            elif(inventory["matchbox"] and not inventory["key"]):
                print("You see something metallic in the pool of blood on the floor.")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor (p)ick up metallic object: ")
                while (choice!="g" and choice!="d" and choice!="p"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \n (p)ick up metallic object: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "p":
                    key()
            else:
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from: ")
                while (choice!="g" and choice!="d"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
            
        else:
            print("")
            print("You now have a crowbar! The barred window might give way now")
            print("You are back in the starting room. \nYou see a large window which is barred.")
            if(not inventory["matchbox"] and not inventory["key"]):
                print("You see a bag in front of you")
                print("You also see something metallic in the pool of blood on the floor.")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor look in (b)ag or (p)ick up metallic object or (t)ry to pry open the barred window: ")
                while (choice!="g" and choice!="d" and choice!="b" and choice!="p" and choice!="t"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \nor look in (b)ag or (p)ick up metallic object \nor (t)ry to pry open the barred window: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "b":
                    bag()
                elif choice == "p":
                    key()
                elif choice== "t":
                    end8()
            elif(not inventory["matchbox"] and inventory["key"]):
                print("You see a bag in front of you")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor look in (b)ag or (t)ry to pry open the barred window: ")
                while (choice!="g" and choice!="d" and choice!="b" and choice!="t"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \nor look in (b)ag or (t)ry to pry open the barred window: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "b":
                    bag()
                elif choice == "t":
                    end8()
            elif(inventory["matchbox"] and not inventory["key"]):
                print("You see something metallic in the pool of blood on the floor.")
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from \nor (p)ick up metallic object or (t)ry to pry open the barred window: ")
                while (choice!="g" and choice!="d" and choice!="p" and choice!="t"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from \n (p)ick up metallic object or (t)ry to pry open the barred window: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                elif choice == "p":
                    key()
                else:
                    end8()
            else:
                print("")
                choice = input(" You can go to (g)arden or where the (d)ripping sound is coming from or (t)ry to pry open the barred window: ")
                while (choice!="g" and choice!="d" and choice!="t"):
                    print("Invalid choice")
                    choice = input(" You can go to (g)arden or trace where the (d)ripping sound is coming from or (t)ry to pry open the barred window: ")
                    print("")
                if choice == "g":
                    garden()
                elif choice == "d":
                    pipeRoom()
                else:
                    end8()
            
def bag():
    if (not inventory["knife handle"]):
        inventory["knife handle"] = True
    if (not inventory["matchbox"]):
        inventory["matchbox"] = True
        print("You open the bag, and inside find a matchbox and a knife handle. You take them. \nYou spot a note reading, \"You won't be forgiven for what you have done.\"")
    else:
        print("The bag is empty, except for a note reading, \"You won't be forgiven for what you have done.\"")
    bloodyRoom()
            
def key():
    if(not inventory["key"]):
        print("You unwillingly put your hand in the \n disgusting goop of haemoglobin, and find a key")
        inventory["key"]= True
    elif(inventory ["key"]):
        print("You already have the key")
    bloodyRoom()
        
def garden():
    print("")
    if(not beenTo["garden"]):
        print("You are hit with a strong sense of vegetation. \nYou feel the presence of a spirit here, and hear a voice, \nHello wanderer, \ncan you help me? A criminal has taken my life, can you make him pay?")
        beenTo["garden"] = True
        choice = input("(y)es or (n)o?: ")
        while (choice!="y" and choice!="n"):
            print("Invalid choice")
            choice = input("(y)es or (n)o?: ")
        if(choice == "y"):
            end4()
        else:
            print("*The ghost looks sad and then disappears*")
            print("You can go east or south. You see something glittering in the grass.")
            choice = input(" You can go back to (b)loody room or go to the (k)itchen or (t)ake the object: ")
            while (choice!="b" and choice!="k" and choice!="t"):
                print("Invalid choice")
                choice = input(" You can go to (b)loody room or (k)itchen: ")
            if choice == "b":
                bloodyRoom()
            elif choice == "k":
                kitchen()
            elif choice == "t":
                torch()
    else:
        print("You are hit with a strong sense of vegetation. You are back in the garden.")
        if(not inventory["torch"]):
            print("You see something glittering in the grass.")
            choice = input(" You can go back to (b)loody room or go to the (k)itchen or (t)ake the object: ")
            while (choice!="b" and choice!="k" and choice!="t"):
                print("Invalid choice")
                choice = input(" You can go to (b)loody room or (k)itchen: ")
            if choice == "b":
                bloodyRoom()
            elif choice == "k":
                kitchen()
            elif choice == "t":
                torch()
        else:
            choice = input(" You can go back to (b)loody room or go to the (k)itchen: ")
            while (choice!="b" and choice!="k"):
                print("Invalid choice")
                choice = input(" You can go to (b)loody room or (k)itchen: ")
            if choice == "b":
                bloodyRoom()
            elif choice == "k":
                kitchen()

def torch():
    print("You fish around in the grass, and find a torch with a silver handle")
    if(not inventory["torch"]):
        inventory["torch"]= True
    elif(inventory ["torch"]):
        print("You already have the torch")
    if(inventory["matchbox"]):
        lit = input("Do you wish to light the torch with a match? (y)es or (n)o?: ")
        while (lit!="y" and lit!="n"):
            print("Invalid choice")
            lit = input("(y)es or (n)o?: ")
        if lit == "y":
            inventory["litTorch"]
            print("The torch is now lit")
        elif lit == "n":
            print("The torch is not lit")
    garden()

def kitchen():
    print("")
    if(not beenTo["kitchen"]):
        print("You see a steak knife blade and a bottle of water on the counter. \nYou know the atrocities you have committed. \nYou know everyone you know is dead. \nYou see a back door to your west, and an exit to the north.")
        choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade or take bottle of (w)ater: ")
        beenTo["kitchen"] = True
        while (choice!="b" and choice!="g" and choice!="k" and choice!="w"):
            print("Invalid choice")
            choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade or take bottle of (w)ater: ")
        if choice == "b":
            if(not inventory["key"]):
                print("The door is padlocked.")
            else:
                if (chance(50)):
                    end1a()
                else:
                    end1b()
        elif choice == "g":
            garden()
        elif choice == "k":
            knifeBlade()
        elif choice == "w":
            water()
    else:
        print("You return to the kitchen.")
        if(not inventory ["knife blade"] and not inventory ["water bottle"]):
            print("You see a steak knife blade on the counter")
            print("You also see a bottle of water on the counter.")
            choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade or take bottle of (w)ater: ")
            while (choice!="b" and choice!="g" and choice!="k" and choice!="w"):
                print("Invalid choice")
                choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade or take bottle of (w)ater: ")
            if choice == "b":
                if(not inventory["key"]):
                    print("The door is padlocked.")
                else:
                    if (chance(50)):
                        end1a()
                    else:
                        end1b()
            elif choice == "g":
                garden()
            elif choice == "k":
                knifeBlade()
            elif choice == "w":
                water()
        elif(not inventory ["knife blade"] and inventory ["water bottle"]):
            print("You see a steak knife blade on the counter")
            choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade: ")
            while (choice!="b" and choice!="g" and choice!="k"):
                print("Invalid choice")
                choice = input(" You can go to (b)ack door or (g)arden or take (k)nife blade: ")
            if choice == "b":
                end1()
            elif choice == "g":
                garden()
            elif choice == "k":
                knifeBlade()
        elif(inventory ["knife blade"] and not inventory ["water bottle"]):
            print("You see a bottle of water on the counter.")
            choice = input(" You can go to (b)ack door or (g)arden or take bottle of (w)ater: ")
            while (choice!="b" and choice!="g" and choice!="w"):
                print("Invalid choice")
                choice = input(" You can go to (b)ack door or (g)arden or take bottle of (w)ater: ")
            if choice == "b":
                end1()
            elif choice == "g":
                garden()
            elif choice == "w":
                water()
        else:
            choice = input(" You can go to (b)ack door or (g)arden: ")
            while (choice!="b" and choice!="g"):
                print("Invalid choice")
                choice = input(" You can go to (b)ack door or (g)arden: ")
            if choice == "b":
                end1()
            elif choice == "g":
                garden()

def knifeBlade():
    print("You take the knife blade")
    inventory["knife blade"]
    if(inventory["knife handle"]):
        knifed = input("Do you wish to combine the knife blade and the knife handle? (y)es or (n)o?: ")
        while (knifed!="y" and knifed!="n"):
            print("Invalid choice")
            knifed = input("(y)es or (n)o?: ")
        if knifed == "y":
            inventory["knife"]
            print("You now have a knife")
            kill = input("By any chance, do you want to kill yourself with the knife? (y)es or (n)o?")
            while (kill!="y" and kill!="n"):
                print("Invalid choice")
                kill = input("(y)es or (n)o?: ")
                if (kill == "y"):
                    end5()
                else:
                    print("Too bad...")
        elif knifed == "n":
            print("You do not have a knife, but a knife blade.")
    kitchen()

def water():
    print("You take the water bottle. The liquid within sparkles...")
    inventory["water bottle"] = True
    choice = input("Would you like to drink the water?(y)es or (n)o?")
    while (choice!="y" and choice!="n"):
        print("Invalid choice")
        choice = input("(y)es or (n)o?: ")
        if (kill == "y"):
            print("You feel refreshed")
        else:
            print("Suit yourself.")
    kitchen()
    
def pipeRoom():
    print("")
    if(not beenTo["pipeRoom"]):
        beenTo["pipeRoom"] = True
        print("You are in a room with pipes coming out of all the walls. You see one pipe with conspicuous claw depressions. \nThere is one exit to the bloody room, and an odd hole in the ground which you could fit through. There is a length of rope on the floor.")
        choice = input("You can to (b)loody room or (h)ole or take (l)ength of rope: ")
        while (choice!="b" and choice!="h" and choice!="l"):
            print("Invalid choice")
            choice = input(" You can go to (b)loody room or (h)ole or take (l)ength of rope: ")
        if choice == "b":
            bloodyRoom()
        elif choice == "h":
            cellar()
        elif choice == "l":
            rope()
    else:
        print("You are back in the pipe room.")
        if(not inventory["rope"]):
            print("There is a length of rope on the floor.")
            choice = input("You can to (b)loody room or (h)ole or take (l)ength of rope: ")
            while (choice!="b" and choice!="h" and choice!="l"):
                print("Invalid choice")
                choice = input(" You can go to (b)loody room or (h)ole or take (l)ength of rope: ")
            if choice == "b":
                bloodyRoom()
            elif choice == "h":
                cellar()
            elif choice == "l":
                rope()
        else:
            choice = input("You can to (b)loody room or (h)ole: ")
            if(tiedTo["hole"]):print("A length of rope is tied to a nearby pipe, leading down into the hole")
            while (choice!="b" and choice!="h"):
                print("Invalid choice")
                choice = input(" You can go to (b)loody room or (h)ole: ")
            if choice == "b":
                bloodyRoom()
            elif choice == "h":
                cellar()

def rope():
    if (not inventory["rope"]):
        print("You take the length of rope")
        inventory["rope"] = True
        choice = input("Do you want to tie the length of rope to one of the pipes? (y)es or (n)o?: ")
        while(choice!="y" and choice!="n"):
            print("Invalid choice")
            choice = input("Do you want to tie the length of rope to one of the pipes? (y)es or (n)o?: ")
        if choice == "y":
            print("The rope is now tied to a nearby pipe. You could probably enter the hole without injury now")
            tiedTo["hole"] = True
        elif choice == "n":
            print("Well... now you just have a length of rope in your...pockets")
    else:
        print("You already have the length of rope")
    pipeRoom()

def cellar():
    print("")
    if(not tiedTo["hole"]):
        end6()
    else:
        if(not inventory["litTorch"]):
            print("You are in a dark cellar which reeks of something rotten. It is too dark to see.")
            end3()
        else:
            if(not beenTo["cellar"]):
                beenTo["cellar"]= True
                print("You are in a cellar, a basement of a sort perhaps? \nYou see a burning coal furnace, and a piece of paper sticking out of the bundle of coal on the ground. \nYou see a length of rope leading back up.")
                choice = input("You can return to the (p)ipe room or (e)xamine the piece of paper: ")
                while(choice!="p" and choice!="e"):
                    print("Invalid choice")
                    choice = input("You can return to the (p)ipe room or (e)xamine the piece of paper: ")
                if choice == "p":
                    pipeRoom()
                    tiedTo["hole"]
                elif choice == "e":
                    print("As you start to pull the piece of paper, you feel it attached to a much heavier mass. It's a book! \nYou examine it further and see depictions of several rituals and experiments...\n You feel like this should be top secret information...\n when out of nowhere, a figure cloaked in black appears!")
                    inventory["paper"] = True
                    choice = input("Do you wish to wait and see what he has to (s)ay, or (a)ttack him?")
                    while(choice!="s" and choice!="a"):
                        print("Invalid choice")
                        choice = input("Do you wish to wait and see what he has to (s)ay, or (a)ttack him?")
                    if choice == "s":
                        if(chance(50)):
                            print("Hey master, come on! I've been looking for you! He goes down through an opening in the floor,and beckons for you to come with.")  
                            end2()
                        else:
                            end7()
                    elif choice == "a":
                        if(inventory["knife"]):
                            print("Lucky for you, you have a knife! After you stab him, he disappears into thin air! A crowbar remains in his place. You take it.")
                            inventory["crowbar"]= True
                            choice = input("You can return to the (p)ipe room: ")
                            while(choice!="p"):
                                print("Invalid choice")
                                choice = input("You can return to the (p)ipe room: ")
                            if choice == "p":
                                pipeRoom()
                        else:
                            print("With no useful weapon at hand, you are defenseless.")
                            end7()
            else:
                print("You are back in the cellar. \nYou see the burning coal furnace, as bright as ever. ")
                if(not inventory["paper"]):
                    print("You also see a piece of paper sticking out of the bundle of coal on the ground")
                    choice = input("You can return to the (p)ipe room or (e)xamine the piece of paper: ")
                    while(choice!="p" and choice!="e"):
                        print("Invalid choice")
                        choice = input("You can return to the (p)ipe room or (e)xamine the piece of paper: ")
                    if choice == "p":
                        pipeRoom()
                        tiedTo["hole"]
                    elif choice == "e":
                        print("As you start to pull the piece of paper, you feel it attached to a much heavier mass. It's a book! \nYou examine it further and see depictions of several rituals and experiments...\n You feel like this should be top secret information...\n when out of nowhere, a figure cloaked in black appears!")
                        inventory["paper"] = True
                        choice = input("Do you wish to wait and see what he has to (s)ay, or (a)ttack him?")
                        while(choice!="s" and choice!="a"):
                            print("Invalid choice")
                            choice = input("Do you wish to wait and see what he has to (s)ay, or (a)ttack him?")
                        if choice == "s":
                            if(chance(50)):
                                print("Hey master, come on! I've been looking for you! He goes down through an opening in the floor,and beckons for you to come with.")  
                                end2()
                            else:
                                end7()
                        elif choice == "a":
                            if(inventory["knife"]):
                                print("Lucky for you, you have a knife! After you stab him, he disappears into thin air! A crowbar remains in his place. You take it.")
                                inventory["crowbar"]= True
                                choice = input("You can return to the (p)ipe room: ")
                                while(choice!="p"):
                                    print("Invalid choice")
                                    choice = input("You can return to the (p)ipe room: ")
                                if choice == "p":
                                    pipeRoom()
                            else:
                                print("With no useful weapon at hand, you are defenseless.")
                                end7()
                else:
                    print("You are back in the cellar. \nYou see a burning coal furnace.")
                    choice = input("You can return to the (p)ipe room : ")
                    while(choice!="p"):
                        print("Invalid choice")
                        choice = input("You can return to the (p)ipe room: ")
                    if (choice == "p"):
                        pipeRoom()
                    
                
                
def end1a():
    print("You use the bloody key to open the door. You see the starry night shine before you. \nThe authorities are here to take you back. \nYou will spend the rest of your life in confinement.")

def end1b():
    print("You use the bloody key to open the door. Your family is here to take you back to the asylum. \nYou have a mental disease, and you must be brought back to sanity.")
    
def end2():
    print("You see a trap door appear all of a sudden. \nYou use it and access your massive underground empire of which you are the lord.")

def end3():
    print("Darkness consumes you and you die of hunger, forever trapped in the abyss of the dungeon. \nYou think you are dead. \nThe next instant, you open your eyes and wake up scrambling in bed.")

def end4():
    print("You see your life flashing before your eyes. \nYou have sinned, and you have been punished accordingly... \n YOU WERE THE MURDERER ALL THIS TIME. YOU REAP WHAT YOU SOW. \nMUAHAHAHAHAHA!")
    
def end5():
    print("You have managed to make your own quietus. I applaud you. Death is a wonderful thing, is it not? \nAh well, good luck, and good bye, you shall be trapped in this game forever, never knowing your true self.")

def end6():
    print("Without anything to climb down with, you fall to your death...")

def end7():
    print("The assassin stabs you repeatedly, you eventually succumb to your wounds and enter the reaper's realm")

def end8():
    print("You escape from the window, and run as fast as you can until you get to the road. \nYour family is waiting for you. You have escaped the mansion of death successfully. \n\tCongratulations!")
          
def main():
    title()
    bloodyRoom()
    
    
if __name__ == "__main__":
    main()
