from consulting_system.models import *


def get_specialities():
    return ('Менеджер', 'Програміст', 'Водій', 'Референт', 'Перекладач')

def get_abilities():
    return ('швидкість та гнучкість мислення', 'вміння швидко приймати рішення', 'стійкість та концентрація уваги',
            'здорова пам\'ять', 'швидкість реакції', 'рухлива пам\'ять', 'фізична виносливість', 'координація рухів',
            'емоційно-вольова стійкість', 'відповідальність')

def get_candidates():
    candidates = Candidate.objects.all()
    return (c.name for c in candidates)

def get_ability_speciality_table(abilities):
    return {abilities[0]:[0.9, 0.8, 0.3, 0.5, 0.7], abilities[1]:[0.9, 0.5, 0.9, 0.4, 0.8],
            abilities[2]:[0.8, 0.9, 0.6, 0.5, 0.8], abilities[3]:[0.4, 0.3, 0.5, 0.5, 0.2],
            abilities[4]:[0.5, 0.1, 0.9, 0.2, 0.6], abilities[5]:[0.3, 0.2, 0.8, 0.2, 0.2],
            abilities[6]:[0.6, 0.2, 0.9, 0.3, 0.2], abilities[7]:[0.2, 0.2, 0.8, 0.3, 0.3],
            abilities[8]:[0.9, 0.5, 0.6, 0.9, 0.3], abilities[9]:[0.8, 0.5, 0.3, 0.8, 0.2]}

def get_ability_candidate_table(abilities):
    d = {}
    candidates = Candidate.objects.all()
    d[abilities[0]] = [c.a1 for c in candidates]
    d[abilities[1]] = [c.a2 for c in candidates]
    d[abilities[2]] = [c.a3 for c in candidates]
    d[abilities[3]] = [c.a4 for c in candidates]
    d[abilities[4]] = [c.a5 for c in candidates]
    d[abilities[5]] = [c.a6 for c in candidates]
    d[abilities[6]] = [c.a7 for c in candidates]
    d[abilities[7]] = [c.a8 for c in candidates]
    d[abilities[8]] = [c.a9 for c in candidates]
    d[abilities[9]] = [c.a10 for c in candidates]
    return d
    # return {abilities[0]: [0.9, 0.8, 0.7, 0.9, 1], abilities[1]: [0.6, 0.4, 0.8, 0.5, 0.6],
    #         abilities[2]: [0.5, 0.2, 0.3, 0.5, 0.9], abilities[3]: [0.5, 0.9, 0.5, 0.5, 0.2],
    #         abilities[4]: [1, 0.6, 0.5, 0.7, 0.4], abilities[5]: [0.4, 0.5, 1, 0.7, 0.8],
    #         abilities[6]: [0.5, 0.8, 0.9, 0.5, 0.4], abilities[7]: [0.5, 0.6, 0.7, 0.6, 0.5],
    #         abilities[8]: [0.8, 1, 0.2, 0.5, 0.6], abilities[9]: [0.3, 0.5, 0.9, 0.6, 0.8]}

