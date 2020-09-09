def solution(numbers, user_hand_type):
    current_left_hand = '*'
    current_right_hand = '#'
    LEFT_SIDE_NUMS = [1, 4, 7]
    RIGHT_SIDE_NUMS = [3, 6, 9]
    keypad_coord = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3,0], 0: [3, 1], '#': [3, 2],
    }
    
    def get_nearest_hand(current_left_hand, current_right_hand, number):
        number_coord = keypad_coord[number]
        left_hand_coord = keypad_coord[current_left_hand]
        dist_from_left = sum([abs(x-y) for x,y in zip(number_coord, left_hand_coord)])

        right_hand_coord = keypad_coord[current_right_hand]
        dist_from_right = sum([abs(x-y) for x,y in zip(number_coord, right_hand_coord)])

        if dist_from_left == dist_from_right:
            return user_hand_type
        if dist_from_left < dist_from_right:
            return 'left'
        else:
            return 'right'

    hand_history = ''
    for number in numbers:
        if number in LEFT_SIDE_NUMS or (number not in RIGHT_SIDE_NUMS and get_nearest_hand(current_left_hand, current_right_hand, number) == 'left'):
            hand_history += 'L'
            current_left_hand = number
        else:
            hand_history += 'R'
            current_right_hand = number

    return hand_history
