@namespace
class SpriteKind:
    fruit2 = SpriteKind.create()
    fruit1 = SpriteKind.create()
    fruit5 = SpriteKind.create()
    co2 = SpriteKind.create()
def set_up_for_players(num: number):
    global index
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    while index <= num - 1:
        mp.set_player_sprite(mp.get_player_by_index(index),
            sprites.create(list2[index], SpriteKind.player))
        mp.move_with_buttons(mp.get_player_by_index(index))
        mp.set_player_state(mp.get_player_by_index(index), MultiplayerState.score, 20)
        mp.get_player_sprite(mp.get_player_by_index(index)).set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
        mp.get_player_sprite(mp.get_player_by_index(index)).set_stay_in_screen(True)
        index += 1

def on_countdown_end():
    if mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score):
        mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.ONE))
    elif mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score):
        mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.TWO))
    elif mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score):
        mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.THREE))
    elif mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.score) and mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.score) > mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.score):
        mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.FOUR))
    else:
        game.set_game_over_message(True, "It's a Tie!!!")
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite2, otherSprite2):
    if day != 0:
        if sprite2 == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.ONE),
                MultiplayerState.score,
                penalty)
            energy_1.value += penalty
        elif sprite2 == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.TWO),
                MultiplayerState.score,
                penalty)
            energy_2.value += penalty
        elif sprite2 == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.THREE),
                MultiplayerState.score,
                penalty)
            energy_3.value += penalty
        else:
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.FOUR),
                MultiplayerState.score,
                penalty)
            energy_4.value += penalty
        otherSprite2.destroy(effects.fire, 100)
        scene.camera_shake(4, 100)
        music.zapped.play()
        spawnEnemy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def player_bars(num2: number):
    if statusbars.all_of_kind(StatusBarKind.energy)[num2].value >= statusbars.all_of_kind(StatusBarKind.energy)[num2].max:
        statusbars.all_of_kind(StatusBarKind.magic)[num2].set_color(5, 13)
        animation.run_image_animation(mp.get_player_sprite(mp.all_players()[num2]),
            animations[num2],
            500,
            True)
    if statusbars.all_of_kind(StatusBarKind.magic)[num2].value >= statusbars.all_of_kind(StatusBarKind.magic)[num2].max:
        scaling.scale_by_percent(mp.get_player_sprite(mp.all_players()[num2]),
            50,
            ScaleDirection.UNIFORMLY,
            ScaleAnchor.MIDDLE)
        statusbars.all_of_kind(StatusBarKind.magic)[num2].set_color(5, 0)
        statusbars.all_of_kind(StatusBarKind.magic)[num2].value = 0
        statusbars.all_of_kind(StatusBarKind.energy)[num2].value = 0
        animation.stop_animation(animation.AnimationTypes.ALL,
            mp.get_player_sprite(mp.all_players()[num2]))

def on_on_score(player22):
    for value in indexes:
        if mp.all_players()[value] == player22:
            sprites.destroy(mp.get_player_sprite(mp.all_players()[value]),
                effects.disintegrate,
                500)
            indexes.remove_at(indexes.index(value))
            if len(indexes) == 1:
                mp.game_over_player_win(mp.all_players()[indexes[0]])
                game.set_game_over_message(True, "Ha vinto!!")
mp.on_score(0, on_on_score)

def on_status_reached_comparison_gte_type_percentage(status2):
    value3 = 0
    while value3 <= len(indexes) - 1:
        if statusbars.all_of_kind(StatusBarKind.magic)[value3].value >= statusbars.all_of_kind(StatusBarKind.magic)[value3].max:
            scaling.scale_by_percent(mp.get_player_sprite(mp.all_players()[indexes[value3]]),
                100,
                ScaleDirection.UNIFORMLY,
                ScaleAnchor.MIDDLE)
            statusbars.all_of_kind(StatusBarKind.magic)[value3].set_color(5, 0)
            statusbars.all_of_kind(StatusBarKind.magic)[value3].value = 0
            statusbars.all_of_kind(StatusBarKind.energy)[value3].value = 0
            animation.stop_animation(animation.AnimationTypes.ALL,
                mp.get_player_sprite(mp.all_players()[indexes[value3]]))
            mp.get_player_sprite(mp.all_players()[indexes[value3]]).say_text("Hydrogen power", 1000, True)
            if day != 0:
                mp.get_player_sprite(mp.all_players()[indexes[value3]]).set_image(list2[indexes[value3]])
            else:
                mp.get_player_sprite(mp.all_players()[indexes[value3]]).set_image(list3[indexes[value3]])
        value3 += 1
statusbars.on_status_reached(StatusBarKind.magic,
    statusbars.StatusComparison.GTE,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gte_type_percentage)

def co2_position(num3: number):
    global hole_X, hole_Y
    hole_X = [15, 20, 75, 82, 117, 126, 32]
    hole_Y = [19, 92, 37, 83, 19, 93, 61]
    strawberry.set_position(hole_X[num3], hole_Y[num3])

def on_status_reached_comparison_gte_type_percentage2(status):
    value2 = 0
    while value2 <= len(indexes) - 1:
        if statusbars.all_of_kind(StatusBarKind.energy)[value2].value >= statusbars.all_of_kind(StatusBarKind.energy)[value2].max and day != 0:
            statusbars.all_of_kind(StatusBarKind.magic)[value2].set_color(5, 13)
            animation.run_image_animation(mp.get_player_sprite(mp.all_players()[indexes[value2]]),
                animations[indexes[value2]],
                500,
                True)
        value2 += 1
statusbars.on_status_reached(StatusBarKind.energy,
    statusbars.StatusComparison.GTE,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gte_type_percentage2)

def spawnEnemy():
    global IceCream
    IceCream = sprites.create(img("""
            .........bbbb...........
                    .......bb1111bb.........
                    ......bb111111bbbbb.....
                    ......b1111111ddd11b....
                    ......b11111111d1111b...
                    ...bbbd11111111d1111b...
                    ..b11111111111111111bb..
                    .b11111111111111111d11b.
                    .b111d11111111111111111b
                    cdd1d111111111111111111c
                    cdddd11111111111111111dc
                    cddbd11111d11111dd111dc.
                    .cbbdd111dddd11ddbdddcc.
                    .ccbbdddddbdddddddbcc...
                    ...cccdddbbbdddddcc.....
                    ......ccccccccccc.......
        """),
        SpriteKind.enemy)
    IceCream.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    IceCream.set_velocity(25, 25)
    IceCream.set_bounce_on_wall(True)

def on_button_multiplayer_b_pressed(player2):
    if energy_1.value >= energy_1.max and mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.ONE),
        mp.MultiplayerButton.B):
        magic_1.value += 1
    elif energy_2.value >= energy_2.max and mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.TWO),
        mp.MultiplayerButton.B):
        magic_2.value += 1
    elif energy_3.value >= energy_3.max and mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.THREE),
        mp.MultiplayerButton.B):
        magic_3.value += 1
    elif energy_4.value >= energy_4.max and mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.FOUR),
        mp.MultiplayerButton.B):
        magic_4.value += 1
    else:
        pass
mp.on_button_event(mp.MultiplayerButton.B,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_b_pressed)

def on_on_overlap2(sprite, otherSprite):
    if day != 0:
        if sprite == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.ONE),
                MultiplayerState.score,
                score_co2)
            energy_1.value += score_co2
        elif sprite == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.TWO),
                MultiplayerState.score,
                score_co2)
            energy_2.value += score_co2
        elif sprite == mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)):
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.THREE),
                MultiplayerState.score,
                score_co2)
            energy_3.value += score_co2
        else:
            mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.FOUR),
                MultiplayerState.score,
                score_co2)
            energy_4.value += score_co2
        otherSprite.destroy(effects.bubbles, 100)
        music.ba_ding.play()
        sprite.say_text("+O2", 500, True)
sprites.on_overlap(SpriteKind.player, SpriteKind.fruit1, on_on_overlap2)

IceCream: Sprite = None
strawberry: Sprite = None
hole_Y: List[number] = []
hole_X: List[number] = []
day = 0
index = 0
magic_4: StatusBarSprite = None
magic_3: StatusBarSprite = None
magic_2: StatusBarSprite = None
magic_1: StatusBarSprite = None
energy_4: StatusBarSprite = None
energy_3: StatusBarSprite = None
energy_2: StatusBarSprite = None
energy_1: StatusBarSprite = None
penalty = 0
score_co2 = 0
indexes: List[number] = []
animations: List[List[Image]] = []
list3: List[Image] = []
list2: List[Image] = []
list2 = [assets.image("""
        bac0
    """),
    assets.image("""
        bac9
    """),
    assets.image("""
        bac8
    """),
    assets.image("""
        bac10
    """)]
list3 = [assets.image("""
        bac1_notte
    """),
    assets.image("""
        bac2_notte
    """),
    assets.image("""
        bac3_notte
    """),
    assets.image("""
        bac4_notte
    """)]
player_lists = [mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)),
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)),
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)),
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR))]
animations = [assets.animation("""
        lampeggio0
    """),
    assets.animation("""
        lampeggio5
    """),
    assets.animation("""
        lampeggio1
    """),
    assets.animation("""
        lampeggio6
    """)]
indexes = [0, 1, 2, 3]
score_co2 = 5
penalty = -10
set_up_for_players(4)
spawnEnemy()
energy_1 = statusbars.create(10, 2, StatusBarKind.energy)
energy_2 = statusbars.create(10, 2, StatusBarKind.energy)
energy_3 = statusbars.create(10, 2, StatusBarKind.energy)
energy_4 = statusbars.create(10, 2, StatusBarKind.energy)
energy_1.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
energy_2.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)))
energy_3.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)))
energy_4.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)))
for value4 in statusbars.all_of_kind(StatusBarKind.energy):
    value4.set_color(2, 13)
    value4.value = 0
    value4.max = 50
    value4.position_direction(CollisionDirection.BOTTOM)
magic_1 = statusbars.create(10, 2, StatusBarKind.magic)
magic_2 = statusbars.create(10, 2, StatusBarKind.magic)
magic_3 = statusbars.create(10, 2, StatusBarKind.magic)
magic_4 = statusbars.create(10, 2, StatusBarKind.magic)
magic_1.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
magic_2.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)))
magic_3.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)))
magic_4.attach_to_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)))
for value5 in statusbars.all_of_kind(StatusBarKind.magic):
    value5.value = 0
    value5.max = 50
    value5.set_color(5, 0)

def on_update_interval():
    global strawberry
    if day != 0:
        strawberry = sprites.create_projectile_from_side(assets.image("""
            co_text
        """), 11, 21)
        co2_position(randint(1, 7))
        strawberry.set_velocity(randint(-50, 50), randint(-50, 50))
        strawberry.set_kind(SpriteKind.fruit1)
        strawberry.set_bounce_on_wall(True)
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global strawberry
    if day == 0:
        strawberry = sprites.create_projectile_from_side(assets.image("""
            co_text
        """), 11, 21)
        co2_position(randint(1, 7))
        strawberry.set_velocity(randint(-50, 50), randint(-50, 50))
        strawberry.set_kind(SpriteKind.fruit1)
        strawberry.set_bounce_on_wall(True)
game.on_update_interval(4000, on_update_interval2)

def on_forever():
    global day
    scene.set_background_image(assets.image("""
        sfondo
    """))
    immagine_giorno = 0
    while immagine_giorno <= len(indexes) - 1:
        mp.get_player_sprite(mp.all_players()[indexes[immagine_giorno]]).set_image(list2[indexes[immagine_giorno]])
        animation.stop_animation(animation.AnimationTypes.ALL,
            mp.get_player_sprite(mp.all_players()[indexes[immagine_giorno]]))
        immagine_giorno += 1
    day = 1
    pause(20000)
    scene.set_background_image(assets.image("""
        sfondo_notte
    """))
    immagine_notte = 0
    while immagine_notte <= len(indexes) - 1:
        mp.get_player_sprite(mp.all_players()[indexes[immagine_notte]]).set_image(list3[indexes[immagine_notte]])
        animation.stop_animation(animation.AnimationTypes.ALL,
            mp.get_player_sprite(mp.all_players()[indexes[immagine_notte]]))
        immagine_notte += 1
    day = 0
    pause(10000)
    scene.set_background_image(assets.image("""
        sfondo
    """))
    pause(200)
    scene.set_background_image(assets.image("""
        sfondo_notte
    """))
    pause(200)
    scene.set_background_image(assets.image("""
        sfondo
    """))
    pause(200)
    scene.set_background_image(assets.image("""
        sfondo_notte
    """))
    pause(200)
    scene.set_background_image(assets.image("""
        sfondo
    """))
    pause(200)
    scene.set_background_image(assets.image("""
        sfondo_notte
    """))
forever(on_forever)

def on_update_interval3():
    if day == 0:
        for value6 in indexes:
            mp.change_player_state_by(mp.all_players()[value6], MultiplayerState.score, -1)
game.on_update_interval(500, on_update_interval3)
