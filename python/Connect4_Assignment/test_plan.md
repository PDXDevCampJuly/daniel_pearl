
Controller Tests
================

* update_board
 *

check_winner

check_tie

get_player_name

update_turn

turn_validator

get_turn

main


Model Tests
===========

* get_player
 * test for player that exists, should get back the existing player
 * test for player that doesn't exist, shouldn't get that player
 * test giving a non string type param, should raise error
* set_player
 * test adding player with a string
 * test adding a player that already exists
 * test adding a player with a non string name
* get_column
 * test asking for column that exists i.e. 1-7, we expect a list to be returned
 * test asking for a column that doesn't exits
 * test asking for a column with a non int index, is error raised
* get_row
 * test asking for row that may exists i.e. 1-6, we expect a list to be returned
 * test asking for a row that doesn't exits
 * test asking for a row with a non int index, is error raised
* add_piece
 * test asking to add to column that exists i.e. 1-7, we expect True if success
 * test asking for a column that doesn't exits, we expect false
 * test asking for a column that is full i.e. column row len > 6, we expect false
 * test asking for a column with a non int index, is error raised


View Tests
==========

* prompt_turn
 * prompt is given a single input, returns single char string
 * prompt is given multiple inputs, returns multiple char strings
* show_instructions
 * does it print instructions, horray
* win_statement
 * does win statement print
* tie_statement
 * does tie statement print
* print_board
 * does board print given a correct board
 * does board catch invalid sized boards
 * does board catch invalid type parameters
* prompt_name
 * prompt is given a single input, returns single char string
 * prompt is given multiple inputs, returns multiple char strings