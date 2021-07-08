import numpy as np
import numpy.random as npr
from constant import (
    action_list,
    action_base_score_dict,
)
from tqdm import tqdm

class BaseballSimulator():
    def __init__(
        self,
        batter_stats,
        n_inning=9,
        out_per_inning=3,
    ):
        self.batter_stats = batter_stats
        self.n_batter = len(self.batter_stats)
        self.n_inning = n_inning
        self.out_per_inning = out_per_inning

    def simulate_game(self, seed=None):
        if seed is not None:
            npr.seed(seed)

        score = 0
        i_batter = 0
        for inning in range(self.n_inning):
            (inning_score, i_batter) = self.simulate_inning(i_batter)
            score += inning_score

        return score

    def simulate_inning(self, i_batter):
        inning_score = 0
        inning_out = 0
        base_state = 0

        while inning_out < self.out_per_inning:
            action = npr.choice(
                action_list,
                p=self.batter_stats[i_batter]
            )
            if action == "out":
                inning_out += 1
            else:
                (action_score, base_state) = action_base_score_dict[action][base_state]
                inning_score += action_score
                
            i_batter = (i_batter + 1) % self.n_batter

        return (inning_score, i_batter)

def generate_batter_stat(
    pa,
    hits,
    double,
    triple,
    homerun,
    walk,
):
    single = (hits - double - triple - homerun)
    batter_stat = np.array([
        single, double, triple, homerun, walk
    ]) / pa
    batter_stat = np.append(batter_stat, 1 - batter_stat.sum())

    return batter_stat

if __name__ == "__main__":
    # data taken from https://www.baseball-reference.com/leagues/majors/bat.shtml
    avg_stat = generate_batter_stat(
        pa=37.29,
        hits=7.96,
        double=1.56,
        triple=0.13,
        homerun=1.18,
        walk=3.32+0.43+0.14, # (BB + HBP + IBB)
    )
    print(avg_stat)

    otani_stat = generate_batter_stat(
        pa=330,
        hits=81,
        double=18,
        triple=4,
        homerun=32,
        walk=36+3+5, # (BB + HBP + IBB)
    )
    print(otani_stat)

    ibb_stat = np.array([0, 0, 0, 0, 1, 0])

    #batter_stats=[avg_stat]*9
    #batter_stats = [avg_stat, otani_stat] + [avg_stat]*7
    batter_stats = [avg_stat]*8 + [otani_stat]# + [avg_stat]*5

    baseball_simulator = BaseballSimulator(
        batter_stats=batter_stats,
    )

    scores = np.zeros(10000)
    for i in tqdm(range(10000)):
        scores[i] = baseball_simulator.simulate_game()

    print(np.mean(scores), np.std(scores))
