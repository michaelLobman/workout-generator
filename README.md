# 5/3/1 Workout Generator

Welcome to a quick workout template I threw together when I found myself spending too much time figuring out percentages at the gym.

The workout template is based on Wendler's 5-3-1 strength training program that centers around four main exercises: Squat, Bench Press, Deadlift, and Military Press.

This simple CLI will ask which exercise you're looking to improve upon and the heaviest weight (and reps) you have recently performed for it.

From there, it will give you a 20-week rep scheme - divided into five 4-week phases.

```terminal
$ python3 orm.py -e ["ENTER EXERCISE IN QUOTES"] -w [ENTER WEIGHT LIFTED] -r [ENTER NUMBER OF REPS PERFORMED]
```

I am building out a front end to make the process easier - but this works in a pinch.