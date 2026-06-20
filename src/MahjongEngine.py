from typing import List

class Tile:
    def __init__(self, category: str, subtype: str, number: int, raw_code: str):
        self.category: str = category
        self.subtype: str = subtype
        self.number: int = number
        self.raw_code: str = raw_code

class Group:
    def __init__(self, group_type: str, visibility: str, tiles: List[Tile]):
        self.type: str = group_type
        self.visibility: str = visibility
        self.tiles: List[Tile] = tiles

    def is_honor(self) -> bool:
        pass

    def is_suit(self) -> bool:
        pass

class Hand:
    def __init__(self, player_wind: str, round_wind: str, groups: List[Group], flowers: List[Tile], winning_tile: Tile):
        self.player_wind: str = player_wind
        self.round_wind: str = round_wind
        self.groups: List[Group] = groups
        self.flowers: List[Tile] = flowers
        self.winning_tile: Tile = winning_tile

    def has_own_flower(self) -> bool:
        pass

    def is_all_concealed(self) -> bool:
        pass

class PlayResult:
    def __init__(self, full_visual: str, base_score: int, doubles: int, total: int, style: str, history: List[str]):
        self.full_visual: str = full_visual
        self.base_score: int = base_score
        self.doubles: int = doubles
        self.total: int = total
        self.style: str = style
        self.history: List[str] = history

    def package_output(self) -> str:
        pass

class MahjongEngine:
    def __init__(self):
        pass

    def process_line(self, raw_line: str) -> PlayResult:
        pass
    
    def parse_string(self, line: str) -> Hand:
        pass

    def verify_classic_hand(self, hand: Hand) -> str:
        pass

    def calculate_base(self, hand: Hand) -> int:
        pass

    def calculate_doubles(self, hand: Hand) -> int:
        pass