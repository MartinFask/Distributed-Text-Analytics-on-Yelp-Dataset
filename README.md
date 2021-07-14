# Distributed-Text-Analytics-on-Yelp-Dataset

---

### run unigram:
  python3 umapper.py < /yelp-data/yelp_tip.csv | sort | python3 ureducer.py > unigrams.txt
  
### run bigram:
  python3 bmapper.py < /yelp-data/yelp_tip.csv | sort | python3 breducer.py > bigrams.txt
  
### run trigram:
  python3 tmapper.py < /yelp-data/yelp_tip.csv | sort | python3 treducer.py > trigrams.txt

---

### To generate `checkinsbyday.txt`
    python3 checkinsmapper.py | sort | python3 checkinsreducer.py > checkinsbyday.txt

---
