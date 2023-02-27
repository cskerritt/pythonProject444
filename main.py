import dictionary as dictionary

# Ask the user for their name, work position, and shift
name = input("Enter your name: ")
position = input("Enter your work position: ")
shift = input("Enter your shift: ")

# Create a dictionary to store the questions and improvement options
checklist = {
    '1a-b': {
        'question': 'When sitting, is the chair height adjusted so your feet rest comfortably flat on the floor or '
                    'footrest, with your knees just slightly lower then your hips?',
        'yes_option': 'Your feet are resting comfortably on the floor or on a footrest, and your knees are slightly '
                      'lower than your hips.',
        'no_option': 'ACTION GOAL #1: Adjust the seat pan height so that your feet rest comfortably flat on the '
                     'floor, or on a footrest ',
        'strategies': 'If your feet do not rest comfortably flat on the floor. Try lowering your chair until your '
                      'feet rest comfortably flat on the floor and use a footrest. Additionally, your feet may rest '
                      'on the floor, but your knees are higher than your hips. Try raising the chair until your hips '
                      'are slightly higher than your knees.',
    },
    '2': {
        'question': 'When sitting, look at the depth of the seat pan, Is there a small gap (2 to 4 inches) between '
                    'the back of your legs and the front edge of the seat pan?',
        'yes_option': 'There is a 2- to 4-inch gap between the back of your knees and the front edge of the chair '
                      'when your back is against the chair.',
        'no_option': 'ACTION GOAL #2: Adjust the seat pan depth so that there is a 2-4 inch gap between the back of '
                     'your knees and the front edge of the chair when your back is against the chair.',
        'strategies': 'If there is more than 4 inches between the front edge of the seat pan and the back of your '
                      'knees, then try to slide the sear out(forward) to make it deeper and provide more support. Or '
                      'use a chair with a seat pan that has a 2- to 4 inch gap between the back of your knees and the '
                      'front edge of the chair when your back is against the chair.',
    },
    '3': {
        'question': 'When sitting, does the curve of the back of the chair fit comfortably into your low back?',
        'yes_option': 'The curve of the chair fits into the deepest part of the curve in your lower back.',
        'no_option': 'ACTION GOAL #3: Adjust the height of the back of the chair so that the curve of the back fits '
                     'into the deepest part of the curve in your lower back.',
        'strategies': 'If the curve in the chair back is too high or too low and does not fit into your lower back, '
                      'then try to reach back to feel the curve in your lower back, or use another chair that can be '
                      'adjusted to fit your lower back.',
    },
    '4': {
        'question': 'When sitting, does the back of the chair tilt back?',
        'yes_option': 'The back of the chair is upright or tilted back for comfort, and provides upper back support.',
        'no_option': 'ACTION GOAL #4: Adjust the tilt of the back of the chair so that the back of the chair is '
                     'upright or tilted back for comfort.',
        'strategies': 'If the chair back does not tilt back slightly and rock or lock into position, then use another '
                      'chair that tilts back slightly and rocks or locks into position.',
    },
    '5': {
        'question': 'When sitting, with your shoulders relaxed, are the armrests slightly below your elbows, '
                    'and your arms hang comfortably at your sides?',
        'yes_option': 'Armrests are adjusted so they are just slightly below your elbows when your shoulders are '
                      'relaxed.',
        'no_option': 'ACTION GOAL #5: Adjust the arms rests so that they are slightly below your elbows when your '
                     'shoulders are relaxed and your arms hand comfortably at your sides.',
        'strategies': 'If your shoulders are raised when resting on the armrests then try doing the following, '
                      'with your shoulders relaxed, lower the armrests to just slightly below your elbows. If you '
                      'reach down to rest on the armrests, then try to raise the armrests to just slightly below your '
                      'elbows when your shoulders are relaxed. If the armrests cannot be adjusted to slightly below '
                      'your elbows when your shoulders are relaxed, then try using another chair with adjustable arm '
                      'rests or remove the armrests.',
    },
    '6': {
        'question': 'When sitting, can you get your chair close enough to your keying, mousing, or writing surfaces '
                    'without reaching?',
        'yes_option': 'Armrests do not interfere with access to the keying, mousing or writing surface.',
        'no_option': 'ACTION GOAL #6: Adjust the armrests so that they do not interfere with access to keying, '
                     'mousing or writing surfaces.',
        'strategies': 'If the armrests interfere with access to keying, mousing or writing surfaces, then try to '
                      'adjust the armrests to their lowest positions. In this position they cannot be used for '
                      'resting, or remove the armrests.',
    },
    '7a-d': {
        'question': 'When keying, with your shoulders relaxed and your fingers curved, is the home row of the keys at '
                    'the same height as your elbows or slightly below your elbows?',
        'yes_option': 'Your shoulders are relaxed, and your elbows are close to your body; and/or your elbows are '
                      'bent to 90 degree or slightly greater on the inner angle; and/or the tops of the "home row" '
                      'keys are at the same height as your elbows; and/or your wrists are slightly straight(not bent).',
        'no_option': 'ACTION GOAL #7: Adjust the keyboard so that: Your shoulders are relaxed, and your elbows are '
                     'close to your body; your elbows are bent to 90 degrees, or slightly greater (inner angle); the '
                     'tops of the home row keys are at the same height as your elbows or slightly below your elbows ('
                     'negative tilt); your wrists are straight (not bent).',
        'strategies': 'If the keyboard is above elbow height then try to raise or lower the keyboard platform or your '
                      'chair until the tops of the home row keys are at the same height as your elbows or slightly '
                      'below your elbows when your shoulders are relaxed. Use a foot rest when necessary. If the '
                      'keyboard is too low and your wrists are bent, then try to tilt the back edge of your keyboard '
                      'platform slightly downward (negative tilt). Your arms will tilt downward, and your elbows will '
                      'open to slightly more than 90 degrees. Dont use the legs beneath the keyboard. If your '
                      'keyboard is at your elbow height, but you lean your wrists while keyboard, then try to use '
                      'wrist rest only for short periods between keying. For longer periods, remove your hands from '
                      'the keyboard and rest them in your lap. Also consider a sit-stand work station that allows you '
                      'to easily go from a seated to a standing position.',
    },
    '8': {
        'question': 'When positioning the cursor with a pointing device, is the pointing device positioned close to the'
                    'keyboard?',
        'yes_option': 'The pointing device is close to the keyboard.',
        'no_option': 'ACTION GOAL #8: Place the pointing device so that it is close to the keyboard.',
        'strategies': 'If the pointing device is a trackball that does not fit on the keyboard platform, try to use a '
                      'keyboard that does not have a 10-key number pad and place the trackball next to the keyboard; '
                      'or replace the keyboard platform with an adjustable keyboard platform wide enough to fit the '
                      'keyboard and the trackball. Adjust the height and tilt of the platform so that the tops of the '
                      'home row keys are at your elbow height, or slightly below your elbows (negative tilt), '
                      'when your shoulders are relaxed. If the pointing device is a mouse or a trackball that does '
                      'not fit on the keyboard platform, then try to remove the keyboard platform, place the keyboard '
                      'and pointing device on the work surface, with a mouse or track ball next to the keyboard, '
                      'raise the chair until the tops of the home row keys are at the same height as your elbows, '
                      'or slightly below your elbows, when your shoulders are relaxed, use a footrest, if necessary, '
                      'additionally adjust the height and distance of the monitor, if necessary. Or use a keyboard '
                      'with a built-in positioning device(touch pad or roller bar mouse).',
    },
    '9a-c': {
        'question': 'When organizing the work space, are you able to use your work surface and equipment without '
                    'over-reaching or using awkward postures?',
        'yes_option': 'Reaches performed frequently are within the "near" work space (your elbows remain at your '
                      'sides.); and/or reaches performed occasionally are within the "near" or "mid" work space(no '
                      'more than an arms length away); and/or you are not reaching across your body to work.',
        'no_option': 'ACTION GOAL #9: Organize the work space so that: reaches performed frequently are within the '
                     'near work space (no more than an arms length away), and you are not reaching across your body '
                     'to work.',
        'strategies': 'If you frequently lean to make reaches more than an arms length away, try to remove unnecessary '
                      'equipment and supplies from the work station and re-organize your work space by moving all '
                      'necessary equipment and supplies close, to no more than an arms length away, or to a location '
                      'where you must get up and walk to it. If you are using a keyboard position and you are keying, '
                      'mousing, and writing simultaneously, and you reach above and behind your keyboard to get to the '
                      'pointing device or the writing surface, the try to remove the keyboard platform; then place '
                      'the keyboard, pointing device and writing material directly on the work surface; raise the '
                      'chair until the tops of the home row keys are at the same height as your elbows, or slightly '
                      'below your elbows when your shoulders are relaxed. Use a foot rest if necessary and adjust the '
                      'height and distance of the monitor if necessary. Or try to replace the keyboard platform with '
                      'a height- and tilt- adjustable platform that is wide enough for the keyboard and pointing '
                      'device. Adjust the height and tilt of the keyboard platform until the tops of the home row '
                      'keys are the same height as your elbows, or slightly below your elbows (negative tilt) when '
                      'your shoulders are relaxed. If you reach across your body at your form station because your '
                      'work station does not match your dominant hand (handedness), then try to reverse the placement '
                      'of the computer equipment so that non-keying tasks are performs on your dominant side when you '
                      'are sitting at your keyboard. If you reach across your body to work work because file drawers '
                      'prevent you from having knee clearance beneath the work surface on your dominant side, '
                      'then reverse the placement of the file drawers so that they are beneath the work surface on '
                      'your non-dominant side.',
    },
    '10a': {
        'question': 'When viewing the monitor, is it in front of you and the top line of print is at or just below '
                    'eye level or even lower if you wear bifocal, trifocals, or progressive lenses; AND are you able '
                    'to scan the screen from top to bottom using only eye movement, and not head movements?',
        'yes_option': 'It is in front of you and and the top line of print is at or just below your eye level or even '
                      'lower if you wear bifocal, trifocals, or progressive lenses; AND you are able to scan the '
                      'screen from top to bottom by using only eye movements, not head movements.',
        'no_option': 'ACTION GOAL #10a: Adjust the height of the monitor so that it is directly in front of you and '
                     'the top line of print is at or just below eye level, or lower if you wear bifocal, trifocals, '
                     'or progressive lenses AND you are able to scan the screen from top to bottom using only eye '
                     'movements, not head movements. ',
        'strategies': 'If the top line of print is above eye level then try to lower the monitor (remove the computer '
                      'or monitor riser(s) from beneath the monitor) until the top line of print is at or slightly '
                      'below eye level, or lower if you wear bifocals, trifocals, or progressive lenses. Or raise '
                      'your chair until your eyes are at or just slightly above the top line of print, or even higher '
                      'if you wear bifocals, trifocals, or progressive lenses. Use a footrest, if necessary. If you '
                      'use head-movements to scan from top to bottom of the screen, then try to raise the monitor '
                      'until the top line or print is at at or slightly below your eye level, or even lower if you '
                      'wear bifocal, trifocals, or progressive lenses.',
    },
    '10b': {
        'question': 'When viewing the monitor, can you sit against your back and read the monitor screen from a '
                    'comfortable distance, without experiencing eye fatigue, blurred vision, or headaches?',
        'yes_option': 'You can sit against the back of the chair and read the monitor screen from a comfortable '
                      'distance without experiencing eye fatigue, blurred vision, or headaches.',
        'no_option': 'ACTION GOAL 10b: Start with the monitor an arms length away. Then adjust the distance of the '
                     'monitor so that you can sit against the back of the chair and read the monitor screen from a '
                     'comfortable distance, without experiencing eye fatigue, blurred vision, or headaches.',
        'strategies': 'If you have symptoms (eye fatigue, blurred vision, or headaches, then try to move the monitor '
                      'back until you can comfortably read the screen without experiencing symptoms. If you have '
                      'difficulty reading the screen, and lean forward to get a closer look, then move the monitor '
                      'closer until you can sit back and comfortably read the screen without symptoms.',
    },
    '10c': {
        'question': 'When viewing the monitor, is the monitor screen free of glare?',
        'yes_option': 'The monitor screen is free from glare.',
        'no_option': 'ACTION GOAL #10c: Adjust the tilt of the screen monitor so that the screen is free of glare.',
        'strategies': 'If there is glare on your monitor from task or overhead lighting then tilt the monitor down '
                      'slightly or dim task or overhead lights; draw blinds or curtains. If the glare on your monitor '
                      'comes from windows, then try to reposition the monitor so that it is at a right angle to the '
                      'light source. You can also use a glare screen, screen hood or even something like a file '
                      'folder that shades the screen.',
    },
    '11a-d': {
        'question': 'When reading the document, is the document off the flat work surface and at the same distance as '
                    'the monitor screen?',
        'yes_option': 'The document is off the flat work surface and in your line of vision; and/or the document is '
                      'directly next to the monitor or between the monitor and the keyboard; and/or the document is '
                      'at the same distance as, or closer than, the monitor; and/or you can look at the document and '
                      'the monitor by moving only your eyes, not your head.',
        'no_option': 'ACTION GOAL #11: Position the document so that, it is off the flat surface and in your line of '
                     'sight; it is directly next to the monitor and the keyboard; it is at the same distance as the '
                     'monitor or closer; you can shift your view between the document and the monitor by moving only '
                     'your eyes, not your head.',
        'strategies': 'If the document is on a flat surface or not directly next to you, then try to place the '
                      'document at the same height and distance as the monitor unless the print is too small to read. '
                      'If the print is hard to read, place the document closer to and at the same height as the '
                      'monitor. Also position the document between the monitor and the keyboard. If the document is '
                      'father away than the monitor then use a document holder that mounts to the monitor or is '
                      'positioned to either the left or right side of the monitor. Or position the document between '
                      'the monitor and the keyboard.',
    },
    '12': {
        'question': 'When using new software programs and operating system, have you been trained on the software '
                    'programs and operating systems you are using?',
        'yes_option': 'You are efficient in the most common tasks you perform; and/or your you reduce the stress and '
                      'frustration you experience when you cannot complete a task.',
        'no_option': 'ACTION GOAL #12: Ask your manager for instructions or training before you begin so that you are '
                     'efficient in the most common tasks you perform and you reduce the stress and frustration you '
                     'experience when you cannot complete a task.',
        'strategies': '',
    }
}
# Create dictionaries to store the responses and strategies
responses = {}
strengths = {}
opportunities = {}

import sys

# Iterate over the checklist and prompt the user to answer each question
for key, item in checklist.items():
    print(item['question'])
    sys.stdout.flush()
    response = input('Enter "Yes" or "No": ')
    while response.lower() not in ['yes', 'no']:
        response = input('Please enter "Yes" or "No": ')
    responses[key] = response.lower()
    if response.lower() == 'yes':
        strengths[key] = item['yes_option']
    else:
        opportunities[key] = item['no_option']

# Define a list of common strategies to consider
common_strategies = ['XX', 'XX', 'XX', 'XX']

# Print the results
print('\n\nResults:\n')

print(f'{name}, {position}, {shift}\n')

print('Strengths:')
for key, value in strengths.items():
    print(f'{checklist[key]["yes_option"]}: {value}')

print('\nOpportunities:')
for key, value in opportunities.items():
    print(f'{checklist[key]["no_option"]}: {value}\n')

print('Common strategies to consider:')
for strategy in common_strategies:
    print(f'- {strategy}')
