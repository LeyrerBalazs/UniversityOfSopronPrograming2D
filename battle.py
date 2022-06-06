import exception

def _get_hp(user: object) -> int:
    """Életerő kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Életerő értéke
    """
    hp = 0
    for unit in user.units:
        hp += unit.hp * unit.amount
    return hp

def _get_defense(user: object) -> int:
    """Védekezés kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Védekezés értéke
    """
    defense = 0
    for unit in user.units:
        defense += unit.defense * unit.amount
    return defense

def _get_attack(user: object) -> int:
    """Támadás kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Támadás értéke
    """
    attack = 0
    for unit in user.units:
        attack += unit.attack * unit.amount
    return attack

def _get_summary(attack:int, defense:int) -> int:
    """Egyik támadása és másik védekezéséne különbsége

    Args:
        attack (int): Egyik támadása
        defense (int): Másik védekezése

    Returns:
        int: Egyik összes támadása
    """
    return attack - defense

def Unitsamount(user:object) -> int:
    """Hadseregszám meghatározása

    Args:
        user (object): Egyik user

    Returns:
        int: darabszám
    """
    amount = 0
    for unit in user.units:
        amount += unit.amount
    return amount

def Battle(user:object, enemy:object) -> bool:
    """Ez a függvény felelős a csata kimenetének megállapításáért.
    A szabálya az, hogy a hp-t, defense-t és attack-ot összesítve összeveti a másik értékeibel
    és ez alapján kiszámolja ki győzne előbb.

    Képlete:
    <user>_<property> = SZUM(<user>.<unit>.<property> * <user>.<unit>.amount)
    <user>_summary_attack = <user>_attack - <enemyuser>_defense
    <user>_need = <enemyuser>_hp / <user>_summary_attack
    
    Args:
        user (object): A felhasználó adatai.
        enemy (object): Az ellenség adatai.

    Returns:
        bool: Érték mely visszaadja a csata kimenetelét True = felhasználó nyert, False = ellenség nyert.
    """
    if Unitsamount(user) == 0 and Unitsamount(enemy) > 0:
        return 1
    elif Unitsamount(enemy) == 0 and Unitsamount(user) > 0:
        return 0
    else:
        user_need = _get_hp(enemy) / exception.is_null(_get_summary(_get_attack(user), _get_defense(enemy)))
        enemy_need = _get_hp(enemy) / exception.is_null(_get_summary(_get_attack(enemy), _get_defense(user)))
        if user_need > enemy_need:
            return 0
        elif user_need < enemy_need:
            return 1
        elif user_need == enemy_need:
            return 2