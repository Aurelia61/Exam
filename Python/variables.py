# coding: utf-8

nb_animals = 0
lenght_race = 0

skill = []

animals = []

specie={
    'Porc-épic':{
        'name_specie' : 'Porc-épic',
        'velocity_max' : 20,
        'recovery_tired' : 50,
        'skill' : [
            {
            'skill_name' : 'Porc qui pique',
            'skill_description' :"Laisse des épines sur le sol",
            'skill_effect' : "Tous les animaux derrière lui augmentent imédiatement leur fatigue de 20%.",
            'skill_activation' : 5,
            'skill_delay' : 10
            },
            {
            'skill_name' : 'Porc-épic comp 2',
            'skill_description' :"Porc-épic descrip 2",
            'skill_effect' : "Porc-épic effet 2",
            'skill_activation' : 3,
            'skill_delay' : 10
            }
        ]
    },
    'Lièvre':{
        'name_specie' : 'Lièvre',
        'velocity_max' : 60,
        'recovery_tired' : 10,
        'skill' : [
            {
            'skill_name' : 'Lièvre comp 1',
            'skill_description' :"Lièvre descrip 1",
            'skill_effect' : "Lièvre effet 1",
            'skill_activation' : 5,
            'skill_delay' : 20
            },
            {
                'skill_name' : 'Lièvre comp  2',
                'skill_description' :"Lièvre descrip  2",
                'skill_effect' : "Lièvre effet  2",
                'skill_activation' : 3,
                'skill_delay' : 30
            }
        ]
    }
}