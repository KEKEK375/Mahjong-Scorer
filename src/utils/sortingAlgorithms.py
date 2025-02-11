class SortingAlgorithms:
    """
    A class containing sorting algorithms.

    Attributes:
        None

    Methods:
        sort_scores(score_list: list, player_list: list) -> tuple[list, list]:
            Sorts the scores and players in ascending order.
    """

    def sort_scores(score_list: list, player_list: list) -> tuple[list, list]:
        """
        Sorts the scores and players in ascending order.

        Parameters:
            score_list (list): A list of scores to be sorted.
            player_list (list): A list of players to be sorted.

        Returns:
            tuple[list, list]: A tuple containing the sorted scores and players.
        """
        
        length = len(score_list)

        if len(player_list) != length:
            raise Exception("List of differing lengths provided.")

        if length <= 1:
            return (score_list, player_list)

        for i in range(1, length):
            score_key = score_list[i]
            player_key = player_list[i]
            j = i - 1
            while j >= 0 and score_key < score_list[j]:
                score_list[j + 1] = score_list[j]
                player_list[j + 1] = player_list[j]
                j -= 1
            score_list[j + 1] = score_key
            player_list[j + 1] = player_key

        return score_list, player_list
