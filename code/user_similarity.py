from __future__ import division
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import re

WORD_RE = re.compile(r"[\w']+")

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/
    def extract_users(self, _, record):
        """Take in a record, yield <user, business_id>"""
        if record['type'] == 'review':
            # print record
            user=record["user_id"]
            business_id=record["business_id"]
            yield [user,business_id]
    
    # def count_business(self, user, businesses):
    #     yield [user,businesses]

    def user_reducer(self, user, businesses):
        """Take businesses for each user """
        biz_group=list(set(businesses))
        # print [user, businesses]
        yield ['key',[user, biz_group]]
    # def jaccard_reducer(self, user, businesses):
    #     yield
            
    def jaccard_compute(self, stat, users_and_reviews):
        # print list(users_and_reviews)
        everything=list(users_and_reviews)
        users=[i[0] for i in everything]
        # all_biz=[]
        # for i in everything:
        #     print i[1]
        #     all_biz.append(i[1])
        all_biz=[i[1] for i in everything]
        # print len(all_biz)
        for i in range(len(users)):
            me=all_biz[i]
            # print i
            for j in range(len(users)):
                # Make sure not to comare a review to itself
                if j is not i:
                    you=all_biz[j]
                    m11=len([x for x in you if x in me])
                    m01=len([x for x in you if x not in me])
                    m10=len([x for x in me if x not in you])
                    jaccard_coefficient=m11/(m11+m10+m01)
                    if jaccard_coefficient>0:
                        yield [[users[i], users[j]], jaccard_coefficient]



    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [
            self.mr(mapper=self.extract_users, reducer=self.user_reducer),
            self.mr(reducer=self.jaccard_compute)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
