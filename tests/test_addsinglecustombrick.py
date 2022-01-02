from renko import Renko


def test_addsinglecustombrick():
    # Initialize Renko object with empty price data
    rnk = Renko(1000, [])
    rnk.create_renko()

    # Will show an empty list
    print(rnk.bricks)

    rnk.add_single_custom_brick("down", 47124, 46376)

    print("Bricks after initial brick added-------------")
    print(rnk.bricks)
