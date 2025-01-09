class SortingAlgorithms:
    def sortScores(scoreList: list, playerList: list) -> tuple[list, list]:
        length = len(scoreList)

        if len(playerList) != length:
            raise Exception("List of differing lengths provided.")

        if length <= 1:
            return (scoreList, playerList)

        for i in range(1, length):
            scoreKey = scoreList[i]
            playerKey = playerList[i]
            j = i - 1
            while j >= 0 and scoreKey < scoreList[j]:
                scoreList[j + 1] = scoreList[j]
                playerList[j + 1] = playerList[j]
                j -= 1
            scoreList[j + 1] = scoreKey
            playerList[j + 1] = playerKey

        return scoreList, playerList
