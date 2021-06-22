# checks for the best current hand
def analyzeHand(currentCards):
    # check how many cards there are
    numCards = len(currentCards)

    # declare hand flags 
    royalFlush = False
    flush = False
    straight = False
    fourOfAKind = False
    threeOfAKind = False

    if numCards >= 5:
        # declare and initialize counters
        clubCounter = 0
        diamondCounter = 0
        heartCounter = 0
        spadeCounter = 0

        # check for flush
        for i in range(numCards):
            if currentCards[i][1] == 'c':
                clubCounter += 1
            elif currentCards[i][1] == 'd':
                diamondCounter += 1
            elif currentCards[i][1] == 'h':
                heartCounter += 1
            elif currentCards[i][1] == 's':
                spadeCounter += 1
        if clubCounter >= 5 or diamondCounter >= 5 or heartCounter >= 5 or spadeCounter >= 5:
            flush = True

        # check for straight
        consecutiveCounter = 0
        for i in range(numCards):
            if i + 1 < numCards:
                if (int(royalToNumber(currentCards[i][0])) + 1) == int(royalToNumber(currentCards[i + 1][0])):
                    consecutiveCounter += 1
                else:
                    if consecutiveCounter < 4:
                        consecutiveCounter = 0
        if consecutiveCounter >= 4:
            straight = True
        # check for royal flush
        if checkForRoyalFlush(currentCards):
            royalFlush = True

    # initialize array for num of rank repitions
    numRanks = [0] * 13
    
    # initialize to 0
    for i in range(13):
        numRanks[i] = 0

    # add repitition to array
    for i in range(numCards):
        numRanks[int(royalToNumber(currentCards[i][0])) - 1] += 1

    # check for four of kind
    if numCards > 3:
        for i in range(13):
            if numRanks[i] == 4:
                fourOfAKind = True
                break
    # check for three of a kind
    if fourOfAKind == False:
        for i in range(13):
            if numRanks[i] == 3:
                threeOfAKind = True
                break
    
    # check for pairs
    numPairs = 0
    for i in range(13):
        if numRanks[i] == 2:
            numPairs += 1


    # Print the correct hand
    if royalFlush:
        print("Royal Flush!")
    elif (flush and straight):
        print("Straight Flush!")
    elif flush:
        print("Flush!")
    elif straight:
        print("Straight!")
    elif fourOfAKind:
        print("Four of a kind!")
    elif threeOfAKind and (numPairs >= 1):
        print("Full house!")
    elif threeOfAKind:
        print("Three of a kind!")
    elif numPairs >= 2:
        print("Two Pair!")
    elif numPairs == 1:
        print("Pair!")
    else:
        print("High card!")
# changes royals into b,c,d to help with sorting the array
def identifyRoyals(card):
    if card[0] == 'J':
        return 'B'
    if card[0] == 'Q':
        return 'C'
    if card[0] == 'K':
        return 'D'
    return card[0]
# converts 10 and royals to numbers
def royalToNumber(card):
    if card[0] == 'A':
        return 10
    if card[0] == 'B':
        return 11
    if card[0] == 'C':
        return 12
    if card[0] == 'D':
        return 13
    return card[0]
# check for royal flush
def checkForRoyalFlush(currentCards):
    if "1c" in currentCards:
        if "Ac" in currentCards:
            if "Bc" in currentCards:
                if "Cc" in currentCards:
                    if "Dc" in currentCards:
                        return True
    if "1d" in currentCards:
        if "Ad" in currentCards:
            if "Bd" in currentCards:
                if "Cd" in currentCards:
                    if "Dd" in currentCards:
                        return True
    if "1h" in currentCards:
        if "Ah" in currentCards:
            if "Bh" in currentCards:
                if "Ch" in currentCards:
                    if "Dh" in currentCards:
                        return True
    if "1s" in currentCards:
        if "As" in currentCards:
            if "Bs" in currentCards:
                if "Cs" in currentCards:
                    if "Ds" in currentCards:
                        return True
    return False

# main
live = True
# declare card array
currentCards = []

while live:
    # ask for card
    inputCard = input("Which card: ")
    # end
    if inputCard == "end":
        live = False
    # changes 10 into a to help sort the array
    if len(inputCard) == 3:
        inputCard = "A" + inputCard[2]
    # change royals to b,c,d to help sort the array
    inputCard = identifyRoyals(inputCard) + inputCard[1]

    # check if card is already in card list
    if inputCard not in currentCards:
        currentCards.append(inputCard)
    # sort the array
    currentCards.sort()
    # print the array
    print(currentCards)
    # analyze current hand
    analyzeHand(currentCards)
        
