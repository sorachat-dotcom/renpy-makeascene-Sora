
# The entry point for this game.
label start:

    # Calls the beginning scene
    call beginning

    # Call all the other scenes in between
    call scene001

    call scene_sjkillen

    # Calls the end scene
    call end

    # This ends the game.
    return
