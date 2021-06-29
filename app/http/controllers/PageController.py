"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller


class PageController(Controller):
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request):
        companies = [
            {
                "name": "Samudayik Laghubitta Bittiya Sanstha Limited",
                "symbol": "SLBSL",
                "prices": [
                    {"price": 1535, "price_at": "Jun-29"}
                ],
                "dividents": [
                    {"rate": 32, "divident_at": "फागुन ५"}
                ],
            },
            {
                "name": "Sana Kisan Bikas Laghubitta Bittiya sanstha Limited",
                "symbol": "SKBBL",
                "prices": [
                    {"price": 1637, "price_at": "Jun-29"}
                ],
                "dividents": [
                    {"rate": 25, "divident_at": "फागुन ५"}
                ],
            }
        ]
        return view.render("front.index", {"companies": companies})
