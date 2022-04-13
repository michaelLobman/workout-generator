import argparse

def main():
    parser = argparse.ArgumentParser(description = "Generate your custom workout program")
    parser.add_argument("-e", "--exercise", type=str, help="Enter exercise", required=True)
    parser.add_argument("-w", "--weight", type=float, help="Enter heaviest weight lifted", required=True)
    parser.add_argument("-r", "--reps", type=float, help="Enter amount of reps performed", required=True)
    args = parser.parse_args()

    def nearest_five(num):
        return 5 * round(num/5)  

    max = nearest_five(args.weight * args.reps * .0333 + args.weight)     
    working_max = nearest_five(max * .9)
  
    def calc_weight(pct):
        return nearest_five(working_max * pct)

    def get_workout():
        workout_tup = (
        {
            'title': 'Week 1',
            'rep_scheme': '3 x 5',
            'weights': (
                calc_weight(.65), 
                calc_weight(.75),
                calc_weight(.85)
            )
        },
        {
            'title': 'Week 2',
            'rep_scheme': '3 x 3',
            'weights': (
                calc_weight(.70),
                calc_weight(.80),
                calc_weight(.90)
            )
        },
        {
            'title': 'Week 3',
            'rep_scheme': '5 - 3 - 1',
            'weights': (
                calc_weight(.75),
                calc_weight(.85),
                calc_weight(.95)
            )
        },
        {
            'title': 'Week 4',
            'rep_scheme': '3 x 5',
            'weights': (
                calc_weight(.40),
                calc_weight(.50),
                calc_weight(.60)
            )
        }
        )
        for week in workout_tup :
            print('%s - %s' % (week['title'], args.exercise))
            print('Rep Scheme:', week['rep_scheme'])
            set_count = 1
            for weight in week['weights']:
                if set_count == 3 and week['title'] != 'Week 4' :
                    print('Set %i: %i pounds (as many reps as possible)' % (set_count, weight))
                else :
                    print('Set %i: %i pounds' % (set_count, weight))
                set_count = set_count + 1

    phase = 1
    while phase < 6 :
        print('__Phase %i__' % phase)
        get_workout()
        working_max = working_max + 5
        phase = phase + 1



main()


# def calc_weight(pct):
#         return nearest_five(working_max * pct) 







# from dataclasses import dataclass, field, asdict

# # might not need this

# class ValidationException(Exception):
#     pass

# @dataclass

# class Workout:
#     exercise: float
#     weight: float
#     reps: float

#     @staticmethod
#     def max(weight, reps):
#         nearest_five(weight * reps * 0.0333 + weight)

#     @staticmethod
#     def working_max(max):
#         nearest_five(max * 9)


# # def calc_weight(pct):
# #         return nearest_five(working_max * pct) 


# def nearest_five(num):
#     return 5 * round(num/5)

# def calc_weight(pct):
#     return nearest_five(working_max * pct)

# exercise = input('To begin, enter an exercise: ')
# print('Enter the heaviest weight you have recently performed for', exercise)

# while True :
#     try:
#         weight = float(input('Weight (in pounds): '))
#     except:
#         print('Enter a valid number for weight')
#         continue
#     break
# print('Enter the corresponding repetitions completed')
# while True:
#     try:
#         reps = float(input('Reps: '))
#     except:
#         print('Enter a valid number for repetitions')
#         continue
#     break

# max = nearest_five(weight * reps * 0.0333 + weight)
# working_max = nearest_five(max * .9)

# print('Your estimated one rep max is: %i pounds'%max)
# print('Please find your workout below:')

# def get_workout():
#     workout_tup = (
#     {
#         'title': 'Week 1',
#         'rep_scheme': '3 x 5',
#         'weights': (
#             calc_weight(.65), 
#             calc_weight(.75),
#             calc_weight(.85)
#         )
#     },
#     {
#         'title': 'Week 2',
#         'rep_scheme': '3 x 3',
#         'weights': (
#             calc_weight(.70),
#             calc_weight(.80),
#             calc_weight(.90)
#         )
#     },
#     {
#         'title': 'Week 3',
#         'rep_scheme': '5 - 3 - 1',
#         'weights': (
#             calc_weight(.75),
#             calc_weight(.85),
#             calc_weight(.95)
#         )
#     },
#     {
#         'title': 'Week 4',
#         'rep_scheme': '3 x 5',
#         'weights': (
#             calc_weight(.40),
#             calc_weight(.50),
#             calc_weight(.60)
#         )
#     }
#     )
#     for week in workout_tup :
#         print('%s - %s' % (week['title'], exercise))
#         print('Rep Scheme:', week['rep_scheme'])
#         set_count = 1
#         for weight in week['weights']:
#             if set_count == 3 and week['title'] != 'Week 4' :
#                 print('Set %i: %i pounds (as many reps as possible)' % (set_count, weight))
#             else :
#                 print('Set %i: %i pounds' % (set_count, weight))
#             set_count = set_count + 1

# phase = 1
# while phase < 6 :
#     print('__Phase %i__' % phase)
#     get_workout()
#     working_max = working_max + 5
#     phase = phase + 1