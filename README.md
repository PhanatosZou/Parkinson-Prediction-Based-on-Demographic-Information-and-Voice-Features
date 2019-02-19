### Parkinson's disease is a long-term degenerative disorder of the central nervous system, whose causes are still shrouded in mystery. People who suffer from Parkinson's disease are likely to be faced with both serious thinking and behavioral problems. And the public's awareness is increased in recent years.

My project uses demographic and vocal features to diagnose Parkinson's disease by machine learning algorithms. 

Firstly, we pay much attention to demographic features, which are not heated signals in this field. The reason is that we want a 'taste' of causality, even without random experiments. A strongly correlated demographic feature will help with prevention. And we do uncover the correlation between age and Parkinson's disease.

Secondly, my project considers vocal features as well. The thing is different people have different numbers of vocal samples, which means if we just add the demographic features as prefixes to the vocal data, then we might obtain different diagnoses for a same patient. We can use Bagging to fix this problem, but patients are treated unevenly because we actually work with some unreasonable weights implicitly. Eventually, we apply a simple and straightforward data processing to handle this.

To sum up, my project systematically combines demographic and vocal features and uses machine learning models in Parkinson diagnosis. my results provide good insights for both prevention and management.
