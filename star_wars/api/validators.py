from api.fetches import verify_user


class SaveRatingValidator:
    def __init__(self, cid=None, rating=None):
        self.cid = cid
        self.rating = rating
        self.message = {'message': 'success'}
        self.status = 200
        self.is_valid = True

        self._verify_number_integer()
        self._verify_number_range()
        self._verify_user()

    def _verify_number_range(self):
        if not (self.rating < 6 and self.rating > 0):
            self.message = {'message': 'rating is out the range'}
            self.is_valid = False
            self.status = 400

    def _verify_user(self):
        if not verify_user(self.cid):
            self.message = {'message': f'this id:{self.cid} does not exist'}
            self.is_valid = False
            self.status = 400  

    def _verify_number_integer(self):
        if not type(self.rating) is int:
            self.message = {'message': f'rating is not an integer'}
            self.is_valid = False
            self.status = 400
