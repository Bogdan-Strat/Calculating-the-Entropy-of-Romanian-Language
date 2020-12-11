#Calculus of the entropy of Romanian language

Starting from the research done by Shannon, we note the work "Prediction and Entropy of Printed English", in which he presents 2 methods for estimating the entropy of the English language: 

1. "N-grams: the entropy of the next letter can be calculated statistically when N-1 previous letters are known." 

2. “Shannon calculates the entropy of each word in English and takes a weighted average. Shannon uses an approximation function to estimate entropy for over 8,000 words. The calculated value you get for entropy per word is 11.82 bits, and since the average word has 4.5 letters, the entropy is 2.62 bits per letter. "

Thus, to calculate the entropy of the Romanian language, we chose the FIRST method of solving presented by Shannon, so we follow the following steps to solve the problem:

* Choosing a representative text for the Romanian language and its processing: (I took as an example: “The most beloved of Earthlings” -by Marin Preda because it is a work close to the 21st century, using various lexical fields)
* Finding the probability of the letter gr + 1, when we know the first gr, and calculating the entropy
* Calculation of entropy using the formula:
  ∑ (frequency of occurrence of a group of letters gr / no) * (probability of occurrence of the next character after the group gr) * log2 (1 / probability of occurrence of the next character after the group gr)
  
  The code in the Entropy_F1_F2_F3_F4.py file calculates the entropy in case we know the first 0/1/2/3 letters and we need to find out the probability of the 1/2/3/4 letter occurring.
  The code in the Entropy_F0.py file calculates the entropy of the Romanian alphabet.
  The Entropy.txt file is the input I used. In it is the work "The most beloved of earthlings" written by Marin Preda.
  
  Shannon's results are (for 27 characters(including the space)):
  F0->4.76
  F1->4.03
  F2->3.32
  F3->3.1
  Fword->2.14

  Our results are (for 32 characters(including the space)):
  F0->5.0
  F1(gr=0): 4.10
  F2(gr=1):3.35
  F3(gr=2):2.86
  F4(gr=3):2.29


  
