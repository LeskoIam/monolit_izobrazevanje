import random
import time

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Player:

    def __init__(self, name: str, health: int, attack: int):
        """Represents basic player character

        :param name: name of the character
        :param health: health points
        :param attack: attack points
        """
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"Player {self.name} - health: {self.health}"

    def do_attack(self, other_player: "Player"):
        """Attack other player

        :param other_player: player to attack, same object type
        :raises ValueError
        """
        if self.name == other_player.name:
            raise ValueError("No harakiri allowed!")
        other_player.health -= random.randint(0, self.attack)

    def is_alive(self) -> bool:
        """Is player alive

        :return: bool
        """
        return self.health > 0
        # return bool(self.health)


class SpecialPlayer(Player):

    def __init__(self, name: str, health: int, attack: int, special_attack: int):
        self.special_attack = special_attack
        self.__last_attack_time = 0
        super(SpecialPlayer, self).__init__(name, health, attack)

    def do_special_attack(self, other_player):
        if self.__last_attack_time <= time.time() - 10:
            other_player.health -= random.randint(self.attack, self.special_attack)
            self.__last_attack_time = time.time()
        else:
            raise Exception("not enough time between attacks")


if __name__ == '__main__':
    player_1 = Player(name="Steve", health=100, attack=10)
    player_2 = Player(name="Jebediah", health=100, attack=5)

    # Izvedi napad
    player_1.do_attack(player_2)
    print(player_1)
    print(player_2)

    # player_1.do_attack(player_1)

    player_2.do_attack(player_1)
    print(player_1)
    print(player_2)

    # Je igralec še živ?
    print(player_1.is_alive())
    print(player_2.is_alive())

    sp = SpecialPlayer("test", 100, 12, 89)

    # print(sp.__last_attack_time)
    print(sp.__dict__)
    sp.do_special_attack(player_1)
    print(sp._SpecialPlayer__last_attack_time)
