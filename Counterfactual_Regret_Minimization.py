import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

"""The algorithm is as follows:

*   For each player, initialize all cumulative regrets to 0.
*   For some number of iterations:
    1.   Compute a regret-matching strategy profile. (If all regrets for a player are non-positive, use
         a uniform random strategy.)
    2.   Add the strategy profile to the strategy profile sum.
    3.   Select each player action profile according the strategy profile.
    4.   Compute player regrets.
    5.   Add player regrets to player cumulative regrets.
    6.   Return the average strategy profile, i.e. the strategy profile sum divided by the number of
iterations.


Over time, this process converges to a correlated equilibrium
"""

def getStrategy(regretSum,strategySum,num_actions=3):
  #remove negative values
  mystrategy=np.maximum(regretSum,0)
  #sum of positive regrets values used to normalize
  normalizingSum=np.sum(mystrategy)
  #if the regret is positive we normalize mystrategy
  #(normalizingSum always posituve except initial form or when code is broken)
  if normalizingSum>0:
    mystrategy/=normalizingSum
  #inital mystrategy is [0,0,0] which we need to make [0.33,0.33,0.33]
  else:
    mystrategy=np.ones(num_actions)/num_actions
  #add to strategySum
  strategySum+=mystrategy
  #strategySum is used for final average strategy
  return mystrategy,strategySum

#Here ROCK=0, PAPER=1, SCISSOR=2
def getAction(mystrategy):
  #this gives a uniform distribution of rock paper scissor choice according
  #to the probability distribution provided as parameter p
  action = np.random.choice([0,1,2], p=mystrategy)
  return action

def train(regretSum,oppStrategy,iterations,strategySum,num_actions=3):
  #Let's train this bad boy
  actionUtility=np.zeros(num_actions)
  for i in range(iterations):
    #get the current best strategy using the my past regrets
    mystrategy,strategySum=getStrategy(regretSum,strategySum,num_actions)
    print("mystrategy: "+ str(mystrategy))
    print("strategySum: "+ str(strategySum))

    #get my action according to mystrategy
    #get opponent action according to his retarded strategy
    myaction=getAction(mystrategy)
    oppAction=getAction(oppStrategy)
    print("Myaction: " + str(myaction) + ", OtherAction: " + str(oppAction))

    actionUtility[oppAction] = 0
    actionUtility[((oppAction + 1) % num_actions)] = 1
    actionUtility[((oppAction - 1) % num_actions)] = -1
    print("ActionUtility: "+ str(actionUtility))
    #add your regrets
    regretSum+=actionUtility-actionUtility[myaction]
    print("regretSum: "+ str(regretSum))
    print("-------------------------------------------------------------")
  return strategySum

#get the Average strategy
def getAverageStrategy(iterations,oppStrategy,num_actions=3):
  regretSum=np.zeros(num_actions)
  strategySum=np.zeros(num_actions)
  strategySum=train(regretSum,oppStrategy,iterations,strategySum)
  normalizingSum=np.sum(strategySum)
  if normalizingSum > 0:
    avgStrategy=strategySum/normalizingSum
  else:
    avgStrategy = np.ones(num_actions)/num_actions
  return avgStrategy

oppStrat = [0.3,0.3,0.4]
print("my Opponent's strategy is ",oppStrat)
print("-------------------------------------------------------------")
print("My max exploitative strategy is ", getAverageStrategy(10000,oppStrat,3))

"""RPS EQUILIBRIUM

In Rock Paper Scissors and every two-player zero-sum game: when both players use regret-matching
to update their strategies, the pair of average strategies converges to a Nash equilibrium as the number
of iterations tends to infinity. At each iteration, both players update their regrets as above and then
both each player computes their own new strategy based on their own regret tables.
"""

#train 2 players with their own strategies
def train2Player(iterations,regretSum1,regretSum2,p2Strat,oppStrategy,num_actions=3):
  actionUtility=np.zeros(num_actions)
  strategySum1=np.zeros(num_actions)
  strategySum2=np.zeros(num_actions)
  for i in range(iterations):
    strategy1,strategySum1=getStrategy(regretSum1,strategySum1,num_actions)
    action1=getAction(strategy1)
    strategy2,strategySum2=getStrategy(regretSum2,strategySum2,num_actions)
    action2=getAction(strategy2)
    actionUtility[action2] = 0
    actionUtility[((action2 + 1) % num_actions)] = 1
    actionUtility[((action2 - 1) % num_actions)] = -1
    regretSum1+=actionUtility-actionUtility[action1]
    regretSum2-=actionUtility-actionUtility[action2]
  return strategySum1,strategySum2

#get the normalised strategy after training both players and updating their strategy based on their regrets
def RPS_EQuilibrium(iterations,oppStrategy,num_actions=3):
  regretSum1=np.zeros(num_actions)
  regretSum2=np.zeros(num_actions)
  strategy1,strategy2 = train2Player(iterations,regretSum1,regretSum2,oppStrategy,3)
  if sum(strategy1)>0:
    strategy1/=sum(strategy1)
  if sum(strategy2)>0:
    strategy2/=sum(strategy2)
  return strategy1,strategy2

print(RPS_EQuilibrium(10000,[.7,.3,.3]))
