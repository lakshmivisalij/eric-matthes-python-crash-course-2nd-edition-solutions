def sandwich(*itemslist):
    print('Make a sandwich with:')
    for i in itemslist:
        print('- '+ i.title())

sandwich('tomato', 'lettuce')
sandwich('cheese')
sandwich('cheese', 'pepporoni', 'tomato', 'lettuce', 'onions')

