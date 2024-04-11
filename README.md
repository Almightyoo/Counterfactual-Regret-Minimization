## ROCK PAPER SCISSOR USING CONTERFACTUAL REGRET MINIMIZATION



https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/b035ec27-9b06-480a-a04f-013addfafc32







This document describes an implementation of Counterfactual Regret Minimization (CFR) for the classic game of Rock-Paper-Scissors (RPS). 
CFR is a powerful algorithm in game theory that allows agents to learn optimal strategies in games with imperfect information. 
This is useful for imperfect information games because there is luck involved in it but just just need to have 
the best strategy to actually exploit weaknesses or even if you don't have the best strategy then you must
update your strategy according to your past regrets
I'm linking this research paper that is good for beginners and helped me a lot to study this concept.  
An Introduction to Counterfactual Regret Minimization Todd W. Neller and Marc Lanctot   -----> http://modelai.gettysburg.edu/2013/cfr/cfr.pdf


**What is CFR?**   
CFR is an iterative algorithm where agents track their regret for not playing different actions in past encounters. 
Regret represents the potential gain they missed by not choosing a specific action. 
Over time, the agents adjust their strategies based on these regrets, 
favoring actions with higher accumulated regret. 

**Why do we use CFR?**  
Imperfect information games are unpredictable because of its luck factor. But the same things make it interesting because when there is luck involved
there is money because anyone can be lucky right?
As they say "Most people are just one spin away from generational wealth". Well, the main difference between imperfect information games is that if you have perfect information games
for example chess, you know there is a much high chance of the person with a higher rating to win the game
But here giving a rating is impossible. When there is involvement of luck people start to take chances and if they lose they blame on luck.
But in reality this luck can be controlled by using the optimum strategy to not lose (minimize regrets)


## CODE
**getAction()**  
<img width="641" alt="Screen Shot 2024-04-11 at 4 30 15 AM" src="https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/7d32b9b9-cf43-4bf7-b101-3bbed03a34d8">  
This piece of code returns an action according to your strategy.  
This is how the distribution works. It does a uniform prob distribution according to your startegy.
<img width="653" alt="Screen Shot 2024-04-11 at 4 31 32 AM" src="https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/741a18ea-6a54-4c27-8512-f9cdc261381f">  

**getStrategy()**  
<img width="622" alt="Screen Shot 2024-04-11 at 4 34 24 AM" src="https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/12e46e92-0b62-4314-9fa2-5d229315633b">  


**train()**  
<img width="683" alt="Screen Shot 2024-04-11 at 4 35 23 AM" src="https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/68b4d927-b5c3-4c1d-bd1e-1e5d90d63a7b">  

**getAverageStrategy()**  
<img width="816" alt="Screen Shot 2024-04-11 at 4 37 51 AM" src="https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/ef67de8e-50c4-462b-9b69-63f22fbfb622">



![bar_chart_animation (1)](https://github.com/Almightyoo/Counterfactual-Regret-Minimization/assets/117665293/f20a11db-0404-4b9f-a325-1d1c136f6f33)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
