Bolognese
=========
Bolognese is a command line tool for tracking macro nutrients.

Configuration
-------------
Bolognese stores all food diaries, recipes, foods and configuration in `json`-format in the `$HOME/.config/bolognese` directory. All files can be managed using the `bolognese` command, but can also be edited manually.

### Foods
Foods are stored in the `$HOME/.config/bolognese/food` directory. Each file contains nutritional information for one food item as well as serving sizes. If, for example, `100g` is listed as a serving, then `100g` of that item corresponds to the nutritional information listed. The following example shows the nutritional information for an orange.
```
alcohol: 0.0
carbs: 10.4
fat: 0.0
fiber: 2.0
protein: 0.8
saturated_fat: 0.0
servings:
- 100g
- 0.5555
sodium: 158.0
sugar: 0.0
```

### Recipes
Recipes are stored in the `$HOME/.config/bolognese/recipes` directory. Each file contains information for one recipe as well as the serving sizes. The following example shows the information my usual breakfast. Recipes can also include other recipes recursively.
```
items:
- food: generic/oats
  serving: 100g
- food: generic/rasins
  serving: 30g
- food: generic/skim-milk
  serving: 280g
servings:
- 1
```

### Nutritional Goals
The nutritional goals are stored in the `$HOME/.config/bolognese/config.yml` directory.
```
alcohol: 0.0
carbs: 400
fat: 89.0
fiber: 38
protein: 200.0
saturated_fat: 40
sodium: 2300
sugar: 95
```

### Food diaries
The daily food diaries are stored in the `$HOME/.config/bolognese/config.yml` directory and contains all foods and recipes for each day. The following is a snippet of a day.
```
- food: generic/granny-smith-apple
  servings: '1'
- recipe: breakfast
  servings: '1'
- food: vores/hummus
  servings: 35g
```

Usage
-----
Bolognese is terminal based. The arguments can be explored by running `bolognese --help`.
