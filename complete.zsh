#!/bin/zsh

compdef _bolognese bolognese

function _bolognese {
    local line

    _arguments -C \
        "-h" \
        "--help" \
        "1: :(config diary food recipe)" \
        "*::arg:->args"

    case $line[1] in
        config)
            _bolognese_config
        ;;
        diary)
            _bolognese_diary
        ;;
        food)
            _bolognese_food
        ;;
        recipe)
            _bolognese_recipe
        ;;
    esac
}

function _bolognese_config {
    _arguments \
        "-h" \
        "--help" \
        "--carbs" \
        "--protein" \
        "--fat" \
        "--saturated_fat" \
        "--alcohol" \
        "--sugar" \
        "--fiber" \
        "--sodium"
}

function _bolognese_food {
    local line

    _arguments -C \
        "1: :(edit copy move remove import list add)" \
        "*::arg:->args"

    case $line[1] in
        edit)
            _bolognese_food_edit
        ;;
        add)
            _bolognese_food_edit
        ;;
        move)
            _bolognese_food_move
        ;;
        copy)
            _bolognese_food_move
        ;;
        remove)
            _bolognese_food_remove
        ;;
        list)
            _bolognese_food_list
        ;;
        import)
            _bolognese_food_import
        ;;
    esac
}

function _bolognese_food_edit {
    foods=$(bolognese food list)
    _arguments \
        "1: :($foods)" \
        "-h" \
        "--help" \
        "--carbs" \
        "--protein" \
        "--fat" \
        "--saturated_fat" \
        "--alcohol" \
        "--sugar" \
        "--fiber" \
        "--sodium"
}

function _bolognese_food_move {
    foods=$(bolognese food list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($foods)" \
        "2: :($foods)"
}

function _bolognese_food_remove {
    foods=$(bolognese food list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($foods)"
}

function _bolognese_food_list {
    _arguments \
        "-h" \
        "--help"
}

function _bolognese_food_import {
    foods=$(bolognese food list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($foods)" \
        "2:" \
}

function _bolognese_recipe {
    local line

    _arguments -C \
        "1: :(edit copy move remove list add add-food add-recipe)" \
        "*::arg:->args"

    case $line[1] in
        edit)
            _bolognese_recipe_edit
        ;;
        add)
            _bolognese_recipe_edit
        ;;
        move)
            _bolognese_recipe_move
        ;;
        copy)
            _bolognese_recipe_move
        ;;
        remove)
            _bolognese_recipe_remove
        ;;
        list)
            _bolognese_recipe_list
        ;;
        add-food)
            _bolognese_recipe_add_food
        ;;
        add-recipe)
            _bolognese_recipe_add_recipe
        ;;
    esac
}

function _bolognese_recipe_edit {
    recipes=$(bolognese recipe list)
    _arguments \
        "1: :($recipes)" \
        "-h" \
        "--help" \
        "--servings"
}

function _bolognese_recipe_move {
    recipes=$(bolognese recipe list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($recipes)" \
        "2: :($recipes)"
}

function _bolognese_recipe_remove {
    recipes=$(bolognese recipe list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($recipes)"
}

function _bolognese_recipe_list {
    _arguments \
        "-h" \
        "--help"
}

function _bolognese_recipe_add_food {
    foods=$(bolognese food list)
    recipes=$(bolognese recipe list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($recipes)" \
        "2: :($foods)" \
        "3: "
}

function _bolognese_recipe_add_recipe {
    recipes=$(bolognese recipe list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($recipes)" \
        "2: :($recipes)" \
        "3:"
}

function _bolognese_diary {
    local line

    _arguments -C \
        "1: :(edit show add-food add-recipe)" \
        "*::arg:->args"

    case $line[1] in
        edit)
            _bolognese_diary_edit
        ;;
        show)
            _bolognese_diary_edit
        ;;
        add-food)
            _bolognese_diary_add_food
        ;;
        add-recipe)
            _bolognese_diary_add_recipe
        ;;
    esac
}

function _bolognese_diary_edit {
    _arguments \
        "-h" \
        "--help" \
        "--date"
}

function _bolognese_diary_add_food {
    foods=$(bolognese food list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($foods)" \
        "2: " \
        "--date" \
        "--recursive"
}

function _bolognese_diary_add_recipe {
    recipes=$(bolognese recipe list)
    _arguments \
        "-h" \
        "--help" \
        "1: :($recipes)" \
        "2: " \
        "--date"
}

