namespace SpriteKind {
    export const fruit2 = SpriteKind.create()
    export const fruit1 = SpriteKind.create()
    export const fruit5 = SpriteKind.create()
    export const co2 = SpriteKind.create()
}
function set_up_for_players (num: number) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    while (index <= num - 1) {
        mp.setPlayerSprite(mp.getPlayerByIndex(index), sprites.create(list2[index], SpriteKind.Player))
        mp.moveWithButtons(mp.getPlayerByIndex(index))
        mp.setPlayerState(mp.getPlayerByIndex(index), MultiplayerState.score, 20)
        mp.getPlayerSprite(mp.getPlayerByIndex(index)).setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
        mp.getPlayerSprite(mp.getPlayerByIndex(index)).setStayInScreen(true)
        index += 1
    }
}
info.onCountdownEnd(function () {
    if (mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score)) {
        mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.One))
    } else if (mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score)) {
        mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.Two))
    } else if (mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score)) {
        mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.Three))
    } else if (mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score) && mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score) > mp.getPlayerState(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score)) {
        mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.Four))
    } else {
        game.setGameOverMessage(true, "It's a Tie!!!")
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    if (day != 0) {
        if (sprite2 == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score, penalty)
            energy_1.value += penalty
        } else if (sprite2 == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score, penalty)
            energy_2.value += penalty
        } else if (sprite2 == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score, penalty)
            energy_3.value += penalty
        } else {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score, penalty)
            energy_4.value += penalty
        }
        otherSprite2.destroy(effects.fire, 100)
        scene.cameraShake(4, 100)
        music.zapped.play()
        spawnEnemy()
    }
})
function player_bars (num2: number) {
    if (statusbars.allOfKind(StatusBarKind.Energy)[num2].value >= statusbars.allOfKind(StatusBarKind.Energy)[num2].max) {
        statusbars.allOfKind(StatusBarKind.Magic)[num2].setColor(5, 13)
        animation.runImageAnimation(
        mp.getPlayerSprite(mp.allPlayers()[num2]),
        animations[num2],
        500,
        true
        )
    }
    if (statusbars.allOfKind(StatusBarKind.Magic)[num2].value >= statusbars.allOfKind(StatusBarKind.Magic)[num2].max) {
        scaling.scaleByPercent(mp.getPlayerSprite(mp.allPlayers()[num2]), 50, ScaleDirection.Uniformly, ScaleAnchor.Middle)
        statusbars.allOfKind(StatusBarKind.Magic)[num2].setColor(5, 0)
        statusbars.allOfKind(StatusBarKind.Magic)[num2].value = 0
        statusbars.allOfKind(StatusBarKind.Energy)[num2].value = 0
        animation.stopAnimation(animation.AnimationTypes.All, mp.getPlayerSprite(mp.allPlayers()[num2]))
    }
}
mp.onScore(0, function (player22) {
    for (let value of indexes) {
        if (mp.allPlayers()[value] == player22) {
            sprites.destroy(mp.getPlayerSprite(mp.allPlayers()[value]), effects.disintegrate, 500)
            indexes.removeAt(indexes.indexOf(value))
            if (indexes.length == 1) {
                mp.gameOverPlayerWin(mp.allPlayers()[indexes[0]])
                game.setGameOverMessage(true, "Ha vinto!!")
            }
        }
    }
})
statusbars.onStatusReached(StatusBarKind.Magic, statusbars.StatusComparison.GTE, statusbars.ComparisonType.Percentage, 100, function (status2) {
    for (let value3 = 0; value3 <= indexes.length - 1; value3++) {
        if (statusbars.allOfKind(StatusBarKind.Magic)[value3].value >= statusbars.allOfKind(StatusBarKind.Magic)[value3].max) {
            scaling.scaleByPercent(mp.getPlayerSprite(mp.allPlayers()[indexes[value3]]), 100, ScaleDirection.Uniformly, ScaleAnchor.Middle)
            statusbars.allOfKind(StatusBarKind.Magic)[value3].setColor(5, 0)
            statusbars.allOfKind(StatusBarKind.Magic)[value3].value = 0
            statusbars.allOfKind(StatusBarKind.Energy)[value3].value = 0
            animation.stopAnimation(animation.AnimationTypes.All, mp.getPlayerSprite(mp.allPlayers()[indexes[value3]]))
            mp.getPlayerSprite(mp.allPlayers()[indexes[value3]]).sayText("Hydrogen power", 1000, true)
            if (day != 0) {
                mp.getPlayerSprite(mp.allPlayers()[indexes[value3]]).setImage(list2[indexes[value3]])
            } else {
                mp.getPlayerSprite(mp.allPlayers()[indexes[value3]]).setImage(list3[indexes[value3]])
            }
        }
    }
})
function co2_position (num3: number) {
    hole_X = [
    15,
    20,
    75,
    82,
    117,
    126,
    32
    ]
    hole_Y = [
    19,
    92,
    37,
    83,
    19,
    93,
    61
    ]
    strawberry.setPosition(hole_X[num3], hole_Y[num3])
}
statusbars.onStatusReached(StatusBarKind.Energy, statusbars.StatusComparison.GTE, statusbars.ComparisonType.Percentage, 100, function (status) {
    for (let value2 = 0; value2 <= indexes.length - 1; value2++) {
        if (statusbars.allOfKind(StatusBarKind.Energy)[value2].value >= statusbars.allOfKind(StatusBarKind.Energy)[value2].max && day != 0) {
            statusbars.allOfKind(StatusBarKind.Magic)[value2].setColor(5, 13)
            animation.runImageAnimation(
            mp.getPlayerSprite(mp.allPlayers()[indexes[value2]]),
            animations[indexes[value2]],
            500,
            true
            )
        }
    }
})
function spawnEnemy () {
    IceCream = sprites.create(img`
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
        `, SpriteKind.Enemy)
    IceCream.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
    IceCream.setVelocity(25, 25)
    IceCream.setBounceOnWall(true)
}
mp.onButtonEvent(mp.MultiplayerButton.B, ControllerButtonEvent.Pressed, function (player2) {
    if (energy_1.value >= energy_1.max && mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.One), mp.MultiplayerButton.B)) {
        magic_1.value += 1
    } else if (energy_2.value >= energy_2.max && mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Two), mp.MultiplayerButton.B)) {
        magic_2.value += 1
    } else if (energy_3.value >= energy_3.max && mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Three), mp.MultiplayerButton.B)) {
        magic_3.value += 1
    } else if (energy_4.value >= energy_4.max && mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Four), mp.MultiplayerButton.B)) {
        magic_4.value += 1
    } else {
    	
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.fruit1, function (sprite, otherSprite) {
    if (day != 0) {
        if (sprite == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.One), MultiplayerState.score, score_co2)
            energy_1.value += score_co2
        } else if (sprite == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Two), MultiplayerState.score, score_co2)
            energy_2.value += score_co2
        } else if (sprite == mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three))) {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Three), MultiplayerState.score, score_co2)
            energy_3.value += score_co2
        } else {
            mp.changePlayerStateBy(mp.playerSelector(mp.PlayerNumber.Four), MultiplayerState.score, score_co2)
            energy_4.value += score_co2
        }
        otherSprite.destroy(effects.bubbles, 100)
        music.baDing.play()
        sprite.sayText("+O2", 500, true)
    }
})
let IceCream: Sprite = null
let strawberry: Sprite = null
let hole_Y: number[] = []
let hole_X: number[] = []
let day = 0
let index = 0
let magic_4: StatusBarSprite = null
let magic_3: StatusBarSprite = null
let magic_2: StatusBarSprite = null
let magic_1: StatusBarSprite = null
let energy_4: StatusBarSprite = null
let energy_3: StatusBarSprite = null
let energy_2: StatusBarSprite = null
let energy_1: StatusBarSprite = null
let penalty = 0
let score_co2 = 0
let indexes: number[] = []
let animations: Image[][] = []
let list3: Image[] = []
let list2: Image[] = []
list2 = [
assets.image`bac0`,
assets.image`bac9`,
assets.image`bac8`,
assets.image`bac10`
]
list3 = [
assets.image`bac1_notte`,
assets.image`bac2_notte`,
assets.image`bac3_notte`,
assets.image`bac4_notte`
]
let player_lists = [
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)),
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)),
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three)),
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Four))
]
animations = [
assets.animation`lampeggio0`,
assets.animation`lampeggio5`,
assets.animation`lampeggio1`,
assets.animation`lampeggio6`
]
indexes = [
0,
1,
2,
3
]
score_co2 = 5
penalty = -10
set_up_for_players(4)
spawnEnemy()
energy_1 = statusbars.create(10, 2, StatusBarKind.Energy)
energy_2 = statusbars.create(10, 2, StatusBarKind.Energy)
energy_3 = statusbars.create(10, 2, StatusBarKind.Energy)
energy_4 = statusbars.create(10, 2, StatusBarKind.Energy)
energy_1.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)))
energy_2.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)))
energy_3.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three)))
energy_4.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Four)))
for (let value4 of statusbars.allOfKind(StatusBarKind.Energy)) {
    value4.setColor(2, 13)
    value4.value = 0
    value4.max = 50
    value4.positionDirection(CollisionDirection.Bottom)
}
magic_1 = statusbars.create(10, 2, StatusBarKind.Magic)
magic_2 = statusbars.create(10, 2, StatusBarKind.Magic)
magic_3 = statusbars.create(10, 2, StatusBarKind.Magic)
magic_4 = statusbars.create(10, 2, StatusBarKind.Magic)
magic_1.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)))
magic_2.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)))
magic_3.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three)))
magic_4.attachToSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Four)))
for (let value5 of statusbars.allOfKind(StatusBarKind.Magic)) {
    value5.value = 0
    value5.max = 50
    value5.setColor(5, 0)
}
game.onUpdateInterval(1000, function () {
    if (day != 0) {
        strawberry = sprites.createProjectileFromSide(assets.image`co_text`, 11, 21)
        co2_position(randint(1, 7))
        strawberry.setVelocity(randint(-50, 50), randint(-50, 50))
        strawberry.setKind(SpriteKind.fruit1)
        strawberry.setBounceOnWall(true)
    }
})
game.onUpdateInterval(4000, function () {
    if (day == 0) {
        strawberry = sprites.createProjectileFromSide(assets.image`co_text`, 11, 21)
        co2_position(randint(1, 7))
        strawberry.setVelocity(randint(-50, 50), randint(-50, 50))
        strawberry.setKind(SpriteKind.fruit1)
        strawberry.setBounceOnWall(true)
    }
})
forever(function () {
    scene.setBackgroundImage(assets.image`sfondo`)
    for (let immagine_giorno = 0; immagine_giorno <= indexes.length - 1; immagine_giorno++) {
        mp.getPlayerSprite(mp.allPlayers()[indexes[immagine_giorno]]).setImage(list2[indexes[immagine_giorno]])
        animation.stopAnimation(animation.AnimationTypes.All, mp.getPlayerSprite(mp.allPlayers()[indexes[immagine_giorno]]))
    }
    day = 1
    pause(20000)
    scene.setBackgroundImage(assets.image`sfondo_notte`)
    for (let immagine_notte = 0; immagine_notte <= indexes.length - 1; immagine_notte++) {
        mp.getPlayerSprite(mp.allPlayers()[indexes[immagine_notte]]).setImage(list3[indexes[immagine_notte]])
        animation.stopAnimation(animation.AnimationTypes.All, mp.getPlayerSprite(mp.allPlayers()[indexes[immagine_notte]]))
    }
    day = 0
    pause(10000)
    scene.setBackgroundImage(assets.image`sfondo`)
    pause(200)
    scene.setBackgroundImage(assets.image`sfondo_notte`)
    pause(200)
    scene.setBackgroundImage(assets.image`sfondo`)
    pause(200)
    scene.setBackgroundImage(assets.image`sfondo_notte`)
    pause(200)
    scene.setBackgroundImage(assets.image`sfondo`)
    pause(200)
    scene.setBackgroundImage(assets.image`sfondo_notte`)
})
game.onUpdateInterval(500, function () {
    if (day == 0) {
        for (let value6 of indexes) {
            mp.changePlayerStateBy(mp.allPlayers()[value6], MultiplayerState.score, -1)
        }
    }
})
