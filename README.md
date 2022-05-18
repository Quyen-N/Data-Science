# Data-Science
**About the KDD99 dataset:**

link: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

KDD Cup 1999 Data
Abstract
This is the data set used for The Third International Knowledge Discovery and Data Mining Tools Competition, which was held in conjunction with KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. The competition task was to build a network intrusion detector, a predictive model capable of distinguishing between "bad" connections, called intrusions or attacks, and "good" normal connections. This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.

**How I solve this problem**

I used an autoencoder model to solve this problem. It has **encoder:** (50 input x 25 Dense x 3 Dense) x **decoder:** (25 Dense x 50 output).

**How to know if a connection is good or bad with this model?**

My python ver is 3.10
- First, clone this repo and set up needed libraries in requirements.txt with this command: pip install -r requirements.txt
- Second, run the main.py with this command: python main.py

The main.py will printout the result if the connection is "bad connection" or "normal.".

You can change the input to the main.py by changing data in samples.csv file, or change the path in main.py.

I am using threshold = 0.004 with Precision = 0.986 and Recall = 0.995.

If you want higher Recall please decrease the threshold, or increase it if you want higher Precision.

Thanks for interesting in my repo.
