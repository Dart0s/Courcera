from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffects(ABC, Hero):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffects):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Berserk')
        return positive_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Strength'] += 7
        stats['Perception'] -= 3
        stats['Endurance'] += 7
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        stats['Agility'] += 7
        stats['Luck'] += 7
        return stats


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Blessing')
        return positive_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 2
        stats['Perception'] += 2
        stats['Endurance'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        return stats


class AbstractNegative(AbstractEffects):

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('Weakness')
        return negative_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4
        return stats


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('EvilEye')
        return negative_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats


class Curse(AbstractNegative):
    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('Curse')
        return negative_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 2
        stats['Perception'] -= 2
        stats['Endurance'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        return stats


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_positive_effects())
    print(hero.get_stats())

    hero = Berserk(hero)
    print(hero.get_positive_effects())
    print(hero.get_stats())

    hero = Berserk(hero)
    print(hero.get_positive_effects())
    print(hero.get_stats())

    hero = Blessing(hero)
    print(hero.get_positive_effects())
    print(hero.get_stats())

    hero = Weakness(hero)
    print(hero.get_negative_effects())
    print(hero.get_stats())

    hero = hero.base
    print(hero.get_positive_effects())
    print(hero.get_stats())