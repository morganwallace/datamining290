#HW-MRjob

###unique_review.py
``$ python unique_review.py yelp_academic_dataset_review.json -q``

	45	"I7lOTTYxHkjc144oAoL0-w"

So the most unique review was **"I7lOTTYxHkjc144oAoL0-w"** with **45** unique words.
Finding the review using the ``egrep`` command: 

``$ egrep "I7lOTTYxHkjc144oAoL0-w" yelp_academic_dataset_review.json``

you get:

	{"votes": {"funny": 4, "useful": 2, "cool": 1}, "user_id": "FxxYCRPcpd__yhRRmmtyMQ", "review_id": "I7lOTTYxHkjc144oAoL0-w", "stars": 3, "date": "2009-03-18", "text": "Oh, mein Gott... vere to shtart?\n\nIf you vant to git tenked, kawm heeya. Mein friend ordert unt Hefeweizen end gut a long, tall gless det held a pint... DAT VAS JOOST FOOR HEEMSELV!\n\nDer German food, I doont like so mawch. Too hivy end too mawch vid da meats. Isht too mawch fur me de brats, de schnitzels, und also de saurbraten. Isht too mawch expensif bisides. Der bawr isht too shmawll ven de peeple kawn liter awn int de nite. Dere's no room to efin stend vithaut bawmpeen sumvawn. I VANT ROOM TO DENSE INT DIS PLESS!!!\n\nSree stawz only fur de beeya. Eef eet vasnt fur de beeya, I'te gif dis pless two staws fur der food. Evrywan shute kawm chick dis pless aut awn der veekends ven der heepster kinders tun diss pless into a discotek. Isht reel fawn, ya?", "type": "review", "business_id": "I_N5b-CA6j0TFMpy1xYKdQ"}
	
Lol, now I see why the review has the most unique words

-----

### user_similarity.py
Run this code to test on a small batch:

``head -n 4000 yelp_academic_dataset_review.json | python user_similarity.py``

Run this command for the whole json file:

``python user_similarity.py yelp_academic_dataset_review.json -q``