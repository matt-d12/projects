"""
File Name: adventuregame.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Branching story tree to practice nested statements - Spooky themed for Halloween
"""
#DISCLAIMER: I am no writer, hopefully the story makes sense. Ignore the cheesiness 
#Import textwrap for long print lines
import textwrap

#Define function for restarting game - call after every ending
def game_end():
    restart = input("Would like you like to restart? (Yes/No) ")
    if restart.lower() == "yes":
        game_start()
    else:
        quit

#Establish a little backstory - slight horror theme as its spooky month
#Total of 9 endings: 4 survive, 5 do not 
def game_start():
    print(textwrap.dedent("""
        You are not the hero of this story. You merely are trying to escape alive.
        You don't remember how you got in this house, but you recognize that scream.
        It's her. You hear that lifeless scream growing closer and closer.
        Your heart rate shoots through the roof. Do I run? Do I hide? She's getting closer...
    """))

    #Using same variable throughout as only using strings I felt using a bunch would over-complicate
    #Begin with first choice - CAPS used to help choices stand out for player
    choice = input("Choice: Do you RUN or HIDE? ")

    #Follow if first choice was RUN
    if choice.lower() == "run":
        print(textwrap.dedent("""
            You have chosen to run.
            You dart out of the bedroom and make your way down the stairs to the front door.
            It's locked. You can hear her coming down the stairs now. Slow, steady, stalking footsteps.
            The kitchen is to your left. There might be a back door there.
            The family room is on your right. There might be a window to climb out of.
        """))
        choice = input("Choice: Do you go to the KITCHEN or FAMILY room? ")
        #----------------------------------------------------------------------------------------------
        #Follow if second choice was KITCHEN
        if choice.lower() == "kitchen":
            print(textwrap.dedent("""
                You have chosen the kitchen. 
                Dust covered countertops and wooden cabinents litter the room.
                The smell. Putrid rotten food hits your nostrils like a wall blocking all other scents. 
                There's another door! A small white wooden door with a half window that peers into the backyard.
                You grab the circlular handle but no luck, it just turns over and over.
                She's at the bottom of the stairs now.
                Maybe you can smash the window with something from the kitchen.
                Or you can try to find a weapon to defend yourself.
            """))
            choice = input("Choice: Do you look for a WEAPON or try to BREAK the window? ")
            #------------------------------------------------------------------------------------------
            #Follow if third choice was WEAPON - Ending #1 of 9 total
            if choice.lower() == "weapon":
                print(textwrap.dedent("""
                    You have chosen to look for a weapon.
                    You frantically search through drawer after drawer in the kitchen, but
                    to no avail. You hear the scream. She's right behind you now. 
                    You close your eyes and take a deep breath, accepting your fate. 
                    You feel nothing, just hearing the scream, then nothing but warmth, silence and darkness.
                                                    
                    GAME OVER - You didn't survive - Ending 1/9
                """))
                #Call function to restart or end game
                game_end()

            #------------------------------------------------------------------------------------------
            #Follow if third choice was BREAK - Ending #2 of 9 total
            elif choice.lower() == "break":
                print(textwrap.dedent("""
                    You have chosen to break the window.
                    There's a broken piece of tile that is seperated from the rest of the floor.
                    You throw that piece through the window and it shatters. She definitely heard you.
                    You reach through the window, grab the handle and hear a click! 
                    The door swings open and you sprint out of there as fast as your legs can carry you.
                    Her scream fills the yard but slowly fades to nothing, you're already over the fence and aren't turning back.
                                                    
                    GAME OVER - You survived - Ending 2/9
                """))
                game_end()
            #Else statement to handle invalid inputs
            else:
                print("Invalid choice, please try again.")
                game_end()
                
        #----------------------------------------------------------------------------------------------
        #Follow if second choice was FAMILY
        elif choice.lower() == "family":
            print(textwrap.dedent("""
                You have chosen the family room.
                Old couches and ripping chairs fill the room. A box TV playing nothing sits against the far wall.
                A scream fills the room. She's is at the bottom of the stairs now. 
                You notice a large window peering out to the street. You might be able to break it and squeeze through. 
                Or do you hide under the couch and wait for her to pass?
            """))
            choice = input("Choice: Do you hide under the COUCH or try to break and SQUEEZE through the window? ")
            #------------------------------------------------------------------------------------------
            #Follow if third choice was COUCH - Ending #3 of 9 total
            if choice.lower() == "couch":
                print(textwrap.dedent("""
                    You have chosen to hide under the couch.
                    You drop to the floor and scoot under the couch facing the doorway where the stairs are.
                    You see her walking. Slow heavy footsteps towards the room. 
                    Her scream stops. It looks like she's walking to the next room over as she goes out of sight.
                    You take the chance to come out from under the couch. As you start moving you feel something grab your leg. 
                    Her scream shakes the couch and walls. Then nothing but cold, silence and darkness.
                                    
                    GAME OVER - You didn't survive - Ending 3/9
                """))
                game_end()
            #------------------------------------------------------------------------------------------
            #Follow if third choice was SQUEEZE - Ending #4 of 9 total
            elif choice.lower() == "squeeze":
                print(textwrap.dedent("""
                    You have chosen to break and squeeze through the window.
                    There's a tall lamp you quickly grab and stab at the window shattering it completely. 
                    As you're getting ready to jump through, you feel a hand grasp at your coat.
                    Instincs kick and you slip your arms out of the sleeves in one fell swoop.
                    You bust through the window, the glass cutting you all over. You don't feel a thing, adrenaline has taken over now.
                    Her scream fills the street but slowly fades to nothing, you're in the clear and need to put as much 
                    distance between you, that house and her as possible.
                                    
                    GAME OVER - You survived - Ending 4/9
                """))
                game_end()
        #Else statement to handle invalid inputs
        else:
            print("Invalid choice, please try again.")
            game_end()

    #--------------------------------------------------------------------------------------------------

    #Follow if first choice was HIDE
    elif choice.lower() == "hide":
        print(textwrap.dedent("""
            You have chosen to hide.
            You quickly crawl under the bed and cover your mouth so she doesn't hear your breathing.
            Stalking, steady, aching footsteps approach the master bedroom you are in. 
            Stop... She stopped right infront of the door. You can't see her above her legs but you see she's barefoot 
            with a blood stained dress on. After holding your breath for what felt like ages, she screams.
            She screams and begins heading down the hallway again, her scream getting more and more distant.
            You crawl out from from under the bed. Need to move, need to act.
        """))
        choice = input("Choice: Do you look for a WINDOW or PEEK down the hallway to see where she's going? ")
        #----------------------------------------------------------------------------------------------
        #Follow if second choice was WINDOW
        if choice.lower() == "window":
            print(textwrap.dedent("""
                You have chosen the window.
                You tug and tug but it won't budge. You can see it's still a bit light outside but the window is covered in cobwebs from the outside.
                Her scream is still coming from the hallway but who knows how long until she comes back.
                You try to peer through the window again but it's hard to tell what's on the other side, might be a ledge or a straight drop.
                If you build up enough speed and jump through you might be able to break through the thin glass.
                Or you could turn around and go look for another way. The screaming seems to have stopped or maybe she's out of earshot now.
            """))
            choice = input("Choice: Do you try to JUMP through the window or TURN around to look for another way? ")
            #------------------------------------------------------------------------------------------
            #Follow if third choice was JUMP - Ending #5 of 9 total
            if choice.lower() == "jump":
                print(textwrap.dedent("""
                    You have chosen to try and jump through the window.
                    The window is pretty big but you think skinny thoughts anyways.
                    You take a few steps back trying to psych yourself up for what you are about to do.
                    You dash at the window, jumping and flatening yourself like a torpedo covering your head with your hands and then, black.
                    You don't remember what happend but you couldn't have been out that long as it's still light outside.
                    You slowly get your feet back under you and stand. As you begin to walk pain circulates all over.
                    You dare not look back as you hear her scream fill the street as you hobble on your way home now.
                                    
                    GAME OVER - You survived - Ending 5/9
                """))
                game_end()
            #------------------------------------------------------------------------------------------
            #Follow if third choice was TURN - Ending #6 of 9 total
            elif choice.lower() == "turn":
                print(textwrap.dedent("""
                    You have chosen to turn around and look for another way.
                    You turn back from the window and head for the doorway to leave the room. There's has to be another way out. 
                    Fear. The only emotion you feel as you walk through the doorway almost bumping into her. 
                    You are eye to eye and before you can comprehend what she looks like, you close your eyes and cover your ears as her scream shakes the hallway walls. 
                    Then darkness...not as if there's an absence of light, there's just... nothing.
                                                    
                    GAME OVER - You didn't survive - Ending 6/9
                """))
                game_end()
            #Else statement to handle invalid inputs
            else:
                print("Invalid choice, please try again.")
                game_end()

        #----------------------------------------------------------------------------------------------
        #Follow if second choice was PEEK
        elif choice.lower() == "peek":
            print(textwrap.dedent("""
                You have chosen to peek down the hallway.
                She's out of sight, but not out of earshot. she must have just rounded that corner up ahead.
                You can hear her scream growing distant at a steady pace as she continues down that hallway.
                There's a balcony straight ahead. You bet you can run right past her and get out of here before she notices.
                What if it's locked like everything else? Maybe you should follow her down the other hallway to see what that offers?
                You could use this chance to attack! You'd have the element of suprise and come up on her blindspot.
                There's a heavy wooden dresser in the room. You could take a drawer from that and swing at her to cause some serious damage.
            """))
            choice = input("Choice: Do you run for the BALCONY, quietly FOLLOW her to other hallway or ATTACK with the dresser drawer? ")
            #------------------------------------------------------------------------------------------
            #Follow if third choice was BALCONY - Ending #7 of 9 total
            if choice.lower() == "balcony":
                print(textwrap.dedent("""
                    You have chosen to go for the balcony.
                    As you exit the bedroom you quietly but swiftly make your way to the balcony. She is still heading down the other hallway unaware of you.
                    You grasp the handle and the door falls right over crashing onto the ground. The hinges were rotted out! 
                    Her scream causes you to bolt upright and as you turn to look she has come back around the corner heading straight for you.
                    You don't have time to think or accept your fate and you jump. A loud snap and pain shoots through your legs.
                    Something is broken but you don't have time to stop. Need to distance yourself as quick as possible. 
                    Her scream fills the street but slowly fades to nothing, hopefully your legs can carry you to a hospital.
                                
                    GAME OVER - You survived - Ending 7/9
                """))
                game_end()
            #------------------------------------------------------------------------------------------
            #Follow if third choice was FOLLOW - Ending #8 of 9 total
            if choice.lower() == "follow":
                print(textwrap.dedent("""
                    You have chosen to quietly follow her down the other hallway.
                    You do your best to impersonate a spy as you come up to the corner where the other hallway begins.
                    There's a small coffee table you use to help hold your body weight as you stick your head around.
                    She's not screaming anymore... or moving... just stationary.
                    CRACK! The coffee table breaks under the pressure and you fall onto the ground right at the intersection of the two hallways.
                    Before you can even lift your head completely, you see her feet right infront of you and then, that scream. 
                    You feel nothing but warmth, silence and darkness. It's almost... peaceful. 
                    
                    GAME OVER - You didn't survive - Ending 8/9
                """))
                game_end()
            #------------------------------------------------------------------------------------------
            #Follow if third choice was ATTACK - Ending #9 of 9 total
            if choice.lower() == "attack":
                print(textwrap.dedent("""
                    You have chosen to grab the dresser drawer and attack her.
                    This is the boldest thing you've ever done but your mother taught you to fight your fears, not run from them.
                    You grab the middle drawer and begin to pull but it's stuck in there good. You give it a little elbow grease but the whole dresser comes crashing down.
                    Rotted wood litters the drawers and support legs causing it to almost fold in on itself.
                    Quiet. Why is it quiet? Why has her scream stopped? But you feel it.
                    The hairs on the back of your neck tell you it's over. Cold air penetrates the room, then her scream and then nothing.
                                                    
                    GAME OVER - You didn't survive - Ending 9/9
                """))
                game_end()
            #Else statement to handle invalid inputs
            else:
                print("Invalid choice, please try again.")
                game_end()
        #Else statement to handle invalid inputs
        else:
            print("Invalid choice, please try again.")
            game_end()
    #--------------------------------------------------------------------------------------------------
    #Else statement to handle invalid inputs
    else:
        print("Invalid choice, please try again.")
        game_end()

#Call function to actually start the game after defining it
game_start()